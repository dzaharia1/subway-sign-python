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

matrix = Matrix(width = 128, height = 32)
display = matrix.display
network = Network(status_neopixel=board.NEOPIXEL, debug=False)
font = terminalio.FONT

def get_data():
    ret = []
    try:
        ret = network.fetch_data(DATA_SOURCE, json_path=DATA_LOCATION)
    except:
        display.show(None)
        print("Fetch error")
        time.sleep(.5)
        ret = get_data()

    return ret

def create_group(index, routeId, minutesUntil, headsign):
    yIndex = 8
    if (index > 1):
        yIndex = yIndex + 15

    if routeId == 'GS':
        routeId = 'S'

    route = routeId[0]

    arrivalRow = displayio.Group()
    arrivalIndexlabel = Label(font,
        color=colors.white,
        text=str(index))
    arrivalIndexlabel.x = 0
    arrivalIndexlabel.y = yIndex
    routeIdlabel = Label(font,
        color=colors.black,
        text=route)
    routeIdlabel.x = 10
    routeIdlabel.y = yIndex
    
    if minutesUntil > settings["warnTime"]:
        minutesUntilLabel = Label(font,
            color=colors.white,
            text=str(minutesUntil) + "min")
    else:
        minutesUntilLabel = Label(font,
            color=colors.getColorByLine('B'),
            text=str(minutesUntil) + "min")
    if minutesUntil < 10:
        minutesUntilLabel.x = 128-23
    else:
        minutesUntilLabel.x = 128-29
    
    minutesUntilLabel.y = yIndex

    headsignLabel = Label(font,
        color=colors.white,
        text=headsign[0:13])
    headsignLabel.x = 21
    headsignLabel.y = yIndex
    
    if len(routeId) > 1 and routeId[1] == "X":
        leftTriangleScrim = Triangle(6, yIndex, 12, yIndex - 6, 12, yIndex + 6, fill=colors.getColorByLine(route))
        rightTriangleScrim = Triangle(12, yIndex - 6, 12, yIndex + 6, 18, yIndex, fill=colors.getColorByLine(route))
        arrivalRow.append(leftTriangleScrim)
        arrivalRow.append(rightTriangleScrim)
    else:
        circleScrim = Circle(12, yIndex, 6, fill=colors.getColorByLine(route))
        arrivalRow.append(circleScrim)
    
    arrivalRow.append(arrivalIndexlabel)
    arrivalRow.append(routeIdlabel)
    arrivalRow.append(headsignLabel)
    arrivalRow.append(minutesUntilLabel)

    return arrivalRow

def draw_arrivals(firstIndex, secondIndex):
    firstArrivalData = data[firstIndex]
    secondArrivalData = data[secondIndex]

    arrival1 = create_group(
        firstIndex,
        firstArrivalData["routeId"],
        firstArrivalData["minutesUntil"],
        firstArrivalData["headsign"]
    )

    arrival2 = create_group(
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
                print("Request took", elapsed, "seconds")
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
