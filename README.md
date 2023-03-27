# CircuitPython Powered Subway Sign!
The subway arrivals sign is a CircuitPython-powered LED sign which displays the upcoming train arrivals at the subway stations of your choosing! This repository contains the code for the sign itself.

## Project overview
The subway arrivals sign needs three overall components in place to get up and running:
1. [The subway arrivals sign API](https://github.com/dzaharia1/subway-schedules) (YOU MUST START HERE)
2. [The subway arrivals web app](https://github.com/dzaharia1/subway-sign-app), which is the front-end that you will use to configure which stations your sign tracks, and other settings, like when it should turn off at night and turn on in the morning
3. The subway sign itself (this repository)

This tutorial will cover the construction and setup of the sign itself.

__*YOU MUST FIRST [SET UP AND DEPLOY THE API](https://github.com/dzaharia1/subway-schedules) AND [SET UP AND DEPLOY THE APP](https://github.com/dzaharia1/subway-sign-app) FOR THIS TUTORIAL TO WORK*__

## A bit more about this sign
The sign requires a few materials:

- [The Adafruit Matrix Portal](https://www.adafruit.com/product/4745). This wonderful Arduino- AND CircuitPython-compatible, wifi-enabled board is custom designed to work with the RGB matrix this project relies on. Thanks to this board, you won't have to solder _anything_ to get this sign working.
- Two [64x32 RGB LED Matrices, also from Adafruit](https://www.adafruit.com/product/2277). You will need TWO of these matrices! This sign will not run properly on one. You can use matrices of any pitch of your choosing (therefore any size) as long as the two are identical.
- One [Chemcast Black LED Acrylic from TAP Plastics](https://www.tapplastics.com/product/plastics/cut_to_size_plastic/black_led_sheet/668). More information later in the tutorial on how to size this sheet down. Adafruit sells a very similar product, but it isn't large enough for this project.
- A pack of [PRO UGlu Dashes](https://www.amazon.com/dp/B06XCCRPRY?ref=nb_sb_ss_w_as-reorder-t1_k1_1_8&amp=&crid=GOHAITNCFYSI&amp=&sprefix=pro+uglu)

