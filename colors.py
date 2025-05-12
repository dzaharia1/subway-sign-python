colors = {
    "red123":  0xdb0f0f,
    "green456": 0x101fad,
    "magenta7": 0xb312a5,
    "blueACE": 0x054e00,
    # "orangeBDFM": 0xFF5500,
    "orangeBDFM": 0xFF004F,
    "greenG": 0x4400FF,
    "brownJZ": 0x732642,
    "grayL": 0xA7ACA9,
    "yellowNQRW": 0xFF0FD3,
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