
colors = {
    "red123":  0xEE0A0A, # rgb(238, 10, 10);
    "green456": 0x009328, # rgb(0, 147, 40);
    "magenta7": 0xB933AD, # rgb(185, 51, 173);
    "blueACE": 0x2850AD, # rgb(40, 80, 173);
    "orangeBDFM": 0xFF4B00, # rgb(255, 75, 0);
    "greenG": 0x6EFF32, # rgb(110, 255, 50);
    "brownJZ": 0x996633, # rgb(153, 102, 51);
    "grayL": 0xA7A9AC, # rgb(167, 169, 172);
    "yellowNQRW": 0xFCCC0A, # rgb(252, 204, 10);
    "grayS": 0x808183, # rgb(128, 129, 131);
    "black": 0x000000, # rgb(0, 0, 0);
    "white": 0xffffff,# rgb(255, 255, 255);
}

white = colors["white"]
black = colors["black"]

color_indices = [
    "red123",
    "green456",
    "magenta7",
    "blueACE",
    "orangeBDFM",
    "greenG",
    "brownJZ",
    "grayL",
    "yellowNQRW",
    "grayS",
    "black",
    "white"
]

line_colors = {
    "1": "red123",
    "2": "red123",
    "3": "red123",
    "4": "green456",
    "5": "green456",
    "6": "green456",
    "7": "magenta7",
    "A": "blueACE",
    "C": "blueACE",
    "E": "blueACE",
    "B": "orangeBDFM",
    "D": "orangeBDFM",
    "F": "orangeBDFM",
    "M": "orangeBDFM",
    "G": "greenG",
    "GS": "greenG",
    "J": "brownJZ",
    "Z": "brownJZ",
    "L": "grayL",
    "N": "yellowNQRW",
    "Q": "yellowNQRW",
    "R": "yellowNQRW",
    "W": "yellowNQRW",
    "S": "grayS"
}

def getColorByLine(line):
    return colors[line_colors[line]]