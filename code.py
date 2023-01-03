import time
import board
import terminalio
import displayio
import colors
from secrets import secrets
from adafruit_display_text.label import Label
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.rect import Rect
from adafruit_bitmap_font import bitmap_font
from adafruit_matrixportal.matrix import Matrix
from adafruit_matrixportal.network import Network

DATA_SOURCE = "https://subway-arrivals.herokuapp.com/sign/" + secrets["sign_id"]
DATA_LOCATION = []
font = terminalio.FONT

matrix = Matrix(width = 128, height = 32, bit_depth=4)
display = matrix.display
boot_message = displayio.Group()
boot_text = Label(font, color=colors.white, text="Starting up", x=4, y=14)
boot_message.append(boot_text)
display.show(boot_message)
network = Network(status_neopixel=board.NEOPIXEL, debug=False)
boot_text.text = "Connecting to\nssid " + secrets["ssid"] + "..."
boot_text.y = 6
display.show(boot_message)

def get_data():
    ret = []
    currTime = time.struct_time(time.localtime())
    print(currTime.tm_hour, ":", currTime.tm_min, ":", currTime.tm_sec)

    try:
        ret = network.fetch_data(DATA_SOURCE, json_path=DATA_LOCATION)
    except:
        print("~~~~~~~~~~~~~~~~ Fetch error ~~~~~~~~~~~~~~~~")
        time.sleep(.5)
        ret = get_data()

    return ret

def create_arrival(index, routeId, minutesUntil, headsign):
    yIndex = 7
    if (index > 1):
        yIndex = yIndex + 17

    if routeId == 'GS':
        routeId = 'S'

    route = routeId[0]

    arrivalRow = displayio.Group()
    arrivalIndexlabel = Label(font,
        color=colors.white,
        text=str(index),
        x=0,
        y=yIndex)
    routeIdlabel = Label(font,
        color=colors.black,
        text=route,
        x=11,
        y=yIndex)
    
    if minutesUntil > settings["warnTime"]:
        minutesUntilLabel = Label(font,
            color=colors.white,
            text=str(minutesUntil) + "min",
            y=yIndex)
    else:
        minutesUntilLabel = Label(font,
            color=colors.getColorByLine('B'),
            text=str(minutesUntil) + "min",
            y=yIndex)
    if minutesUntil < 10:
        minutesUntilLabel.x = 128-23
    else:
        minutesUntilLabel.x = 128-29

    headsignLabel = Label(font,
        color=colors.white,
        text=headsign[0:12],
        x=23,
        y=yIndex)
    
    if len(routeId) > 1 and routeId[1] == "X":
        leftTriangleScrim = Triangle(6, yIndex, 13, yIndex - 7, 13, yIndex + 7, fill=colors.getColorByLine(route))
        rightTriangleScrim = Triangle(13, yIndex - 7, 13, yIndex + 7, 20, yIndex, fill=colors.getColorByLine(route))
        arrivalRow.append(leftTriangleScrim)
        arrivalRow.append(rightTriangleScrim)
    else:
        circleScrim = Circle(13, yIndex, 7, fill=colors.getColorByLine(route))
        arrivalRow.append(circleScrim)
    
    arrivalRow.append(arrivalIndexlabel)
    arrivalRow.append(routeIdlabel)
    arrivalRow.append(headsignLabel)
    arrivalRow.append(minutesUntilLabel)

    return arrivalRow

def draw_arrivals(firstIndex, secondIndex):
    firstArrivalData = data[firstIndex]
    secondArrivalData = data[secondIndex]

    arrival1 = create_arrival(
        firstIndex,
        firstArrivalData["routeId"],
        firstArrivalData["minutesUntil"],
        firstArrivalData["headsign"]
    )

    arrival2 = create_arrival(
        secondIndex,
        secondArrivalData["routeId"],
        secondArrivalData["minutesUntil"],
        secondArrivalData["headsign"]
    )
    
    megaGroup = displayio.Group()
    megaGroup.append(arrival1)
    megaGroup.append(arrival2)
    display.show(megaGroup)
    

data = get_data()
settings = data[0]
network.get_local_time()

while True:
    if settings["rotating"] and settings["signOn"]:
        i = 2
        while i <= settings["numArrivals"]:
            if settings["signOn"] and settings["rotating"]:
                draw_arrivals(1, i)
                startTime = time.monotonic()
                data = get_data()
                settings = data[0]
                elapsed = time.monotonic() - startTime
                time.sleep(abs(settings["rotationTime"] - elapsed))
                i = i + 1
    elif settings["signOn"]:
        draw_arrivals(1, 2)
        time.sleep(5)
        data = get_data()
        settings = data[0]
    else:
        rect = Rect(0, 0, 128, 32, fill=colors.black)
        mask = displayio.Group()
        display.show(mask)
        time.sleep(3)
        data = get_data()
        settings = data[0]
