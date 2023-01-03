colors = {
    "red123":  0xdb0f0f,
    "green456": 0x16ad02,
    "magenta7": 0xb312a5,
    "blueACE": 0x054ea1,
    "orangeBDFM": 0xff590d,
    "greenG": 0x5ecc1f,
    "brownJZ": 0x734226,
    "grayL": 0xA7A9AC,
    "yellowNQRW": 0xfcc80a,
    "grayS": 0x808183,
    "black": 0x000000,
    "white": 0xffffff
}

white = colors["white"]
black = colors["black"]

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