colors = {
    "red123":  0xdb0f0f,      # R:db G:0f B:0f -> RBG: db0f0f
    "green456": 0x1602ad,    # R:16 G:ad B:02 -> RBG: 1602ad
    "magenta7": 0xb3a512,    # R:b3 G:12 B:a5 -> RBG: b3a512
    "blueACE": 0x05a14e,     # R:05 G:4e B:a1 -> RBG: 05a14e
    "orangeBDFM": 0xff0d59,  # R:ff G:59 B:0d -> RBG: ff0d59
    "greenG": 0x5e1fcc,     # R:5e G:cc B:1f -> RBG: 5e1fcc
    "brownJZ": 0x732642,    # R:73 G:42 B:26 -> RBG: 732642
    "grayL": 0xa7aca9,     # R:a7 G:a9 B:ac -> RBG: a7aca9 (Note: 0xA7A9AC became 0xa7aca9)
    "yellowNQRW": 0xfc0ac8,  # R:fc G:c8 B:0a -> RBG: fc0ac8
    "grayS": 0x808381,     # R:80 G:81 B:83 -> RBG: 808381
    "black": 0x000000,     # R:00 G:00 B:00 -> RBG: 000000
    "white": 0xffffff      # R:ff G:ff B:ff -> RBG: ffffff
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