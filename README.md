# CircuitPython Powered Subway Sign!
The subway arrivals sign is a CircuitPython-powered LED sign which displays the upcoming train arrivals at the subway stations of your choosing! This repository contains the code for the sign itself.

## Project overview
The subway arrivals sign needs three overall components in place to get up and running:
1. [The subway arrivals sign API](https://github.com/dzaharia1/subway-schedules) (YOU MUST START HERE)
2. [The subway arrivals web app](https://github.com/dzaharia1/subway-sign-app), which is the front-end that you will use to configure which stations your sign tracks, and other settings, like when it should turn off at night and turn on in the morning
3. The subway sign itself (this repository)

This tutorial will cover the construction and setup of the sign itself.

__⚠️ Important: __ __*YOU MUST FIRST [SET UP AND DEPLOY THE API](https://github.com/dzaharia1/subway-schedules) AND [SET UP AND DEPLOY THE APP](https://github.com/dzaharia1/subway-sign-app) FOR THIS TUTORIAL TO WORK*__

## Materials you will need
The sign requires a few materials:

- [The Adafruit Matrix Portal](https://www.adafruit.com/product/4745). This wonderful Arduino- AND CircuitPython-compatible, wifi-enabled board is custom designed to work with the RGB matrix this project relies on. Thanks to this board, you won't have to solder _anything_ to get this sign working.
- Two [64x32 RGB LED Matrices at your preferred size, also from Adafruit](https://www.adafruit.com/product/2277). You will need TWO of these matrices! The size (determined by the "pitch" or distance bewteen each LED) is up to you, but the resolution must be 32x64. You will have to order your diffuser to match the size you choose for the matrix. More on this in the next section.
- One [Chemcast Black LED Acrylic sheet from TAP Plastics](https://www.tapplastics.com/product/plastics/cut_to_size_plastic/black_led_sheet/668). More information later in the tutorial on how to size this sheet to order. Adafruit sells a very similar product, but it isn't large enough for this project.
- A pack of [PRO UGlu Dashes](https://www.amazon.com/dp/B06XCCRPRY?ref=nb_sb_ss_w_as-reorder-t1_k1_1_8&amp=&crid=GOHAITNCFYSI&amp=&sprefix=pro+uglu) These are super clear, super tacky little squares of stickiness. We'll use them to attach the diffuser and LED matrices, without blocking any of the light from the LEDs.
- A power supply that provides at least 5 volts. A standard USB-C brick will do the trick.

## Order your acrylic diffuser
This plastic sheet has a few jobs. It's the main skeleton for the sign, holding the two LED matrices together. It also significantly increases the legibility of the sign, making it more practical. Finally, it reduces the cast brightness, while preserving surface brightness, preventing a blaring-bright nuisance in your home. I sourced mine from TAP Plastics, who custom cuts their acrylic sheets to order. We'll need a custom size for the size of LED matrix you chose to buy.

### Determine the size of your LED matrices
First, determine the overall size of your combined LED panel, which is the two LED matrices side-by side. On the product page of the LED matrix you purchased, scroll down to the "technical details" section for the overall dimensions of the matrix.

### Determine the size of your diffuser
I sized my diffuser to be .5" larger than the combined LED panel in height and width. So the diffuser has to be overall 1" larger than the LED panel in both height and width. This way, the text on our sign can use the edge-to-edge space of the LED panel and still have some margin around it for legibility and aesthetics. Here's the simple calculation for your diffuser size:

The height of your diffuser is `<height of LED matrix> + 1` inches.

The width of your diffuser is `(<width of LED matrix> * 2) + 1` inches.

So, for example, if you chose the 4mm pitch LED matrix, which has an overall dimension of 10" width by 5" height, then your acrylic diffuser's dimensions are:

height = `5 + 1` = 6"

width = `10 * 2 + 1` = 21"


### Order your diffuser
Finally, we're ready to purchase the diffuser. Head on over to [TAP Plastics](https://www.tapplastics.com/product/plastics/cut_to_size_plastic/black_led_sheet/668) to input the dimensions you need and place the order. There will only be one option for color and thickness. Then just input the dimensions you figured out in the previous section and place your order. Once it arrives, you can proceed with this tutorial

## Build the sign

### Measure and mark
Let's do some measurements before placing the LED panels to make sure they're dead center and in alignment with the diffuser.

Grab a straight-edge ruler, and some tool you can use to lightly mark the glossy side of the plastic with the "outline" of the led panels. I used my smallest precision flathead screwdriver for this purpose. Dry erase is another option, but I found it rubbing off too easily. Don't worry– as long as you mark gently the etching from the flathead screwdriver will not show through the diffuser once your project is assembled!

Lay the acrylic sheet __satin side down__ on a soft, completely clean surface like a cutting board, or even some cardboard. The glossy side will face the LED panel, while the satin side will face outward. Let's avoid scratching the satin side in any way. From each corner of the acrylic sheet, use your straight edge and screwdriver to mark .5" away from the sheet's edges. __Your markings should be made only on the glossy side of the sheet__.

Connect the markings with lines to form a centered rectangle .5" smaller than the sheet in both dimensions. If you sized and ordered your sheet correctly, this rectangle should be the identical dimensions to your LED panels side-by-side. If your drawn rectangle is significantly different in size from your LED matrices side-by-side, check all of your measurements again.

### Mount the LED panel to the diffuser
It's time to break into the UGlu dashes. Place a generous number of evenly-spaced dashes around the outermost edges of the LED panels, _starting with the corners_. The LEDs on the panels are bright enough that the dashes will not be visible through the diffuser. So don't be shy about including enough dashes to ensure a secure joint.

Use the guide markings you made in the last section to carefully place the first panel onto the diffuser. Here's how I made sure to keep things neat:

Start by aligning one of the _longer edges of the LED panel_ with your rectangle, and then carefully rotate the panel downward until the UGlue dashes contact the plastic surface.

__⚠️ Important:__ __*Before you mount the next panel, check which port of the LED panel you just placed is facing the center. The ports are marked as `data_in` and `data_out`.*__ __The matrices should be in the same orientation so that the `data_in` port of one is beside the `data_out` port on the other.__  

Align the _shorter_ edges of the two panels, with the second one rotated away from the plastic, to keep the dashes from touching. Once the panel edges are aligned, carefully rotate the panel toward the plastic until the dashes make contact, all the while keeping its edge aligned with its sibling. Once the dashes make contact gently, but firmly press the two panels against the plastic diffuser to ensure a tight bond.

### Wire up the works
The LED matrix comes packaged with a ribbon cable, for chaining it with other matrices, and a power cable, for... power. The ribbon cable does _not_ transmit power, so we'll be using both of these cables to assemble the display.

First, attach the MatrixPortal to the `data_in` port closest to the edge of the display. There is a tab on one side of the MatrixPortal's connector that only allows it to be mounted in one orientation.

Next use one of the included ribbon cables to chain the two LED matrices.
 
Now for the power. Attach both of the included power cables to the LED matrices using the molex-style connectors on the back. Then, use a Philips-head screwdriver to attach the ground (black) and 5V (red) cable ends to the corresponding screw leads on the MatrixPortal.

### Test
With the sign assembled, let's quickly test it using the demo code that the MatrixPortal came with. Simply plug the USB-C port on the MatrixPortal to a USB-C power supply, like the one you would use for your iPad, laptop or cell phone, and watch it turn on! You should see a "sandy" pile of pixels. Rotate and tilt the assembly to watch them shift around. You may not see the whole LED panel being used for the demo. 

If the lights on the MatrixPortal board come on, but you don't see the demo software on the LED matrix, you might have a wiring problem. Unplug the USB-C cable, and check to make sure that:
- The ribbon cable connects the `data_out` port on one LED matrix to the `data_in` port on the other.
- The molex-like power cables are firmly plugged into the back of the LED matrices. It can take a firm hand!
- The red and black cables, respectively, are connected to the correct leads on the MatrixPortal board. Remember: black for GND, red for 5V. 


## Program the MatrixPortal  
Home stretch! It's time to get the subway sign software onto the MatrixPortal.

### Install CircuitPython
Your MatrixPortal may be set up by default to be an Arduino-compatible board. Pretty cool, I know, but the subway sign software is actually written in a Python variant designed for microcontrollers, called CircuitPython. Follow [this guide](https://learn.adafruit.com/adafruit-MatrixPortal-m4/install-circuitpython) to get CircuitPython installed onto your MatrixPortal.

__*Make sure you install CircuitPython 8.x or above for this project.*__

### Create your secrets.py
The subway sign code is designed not to include any sensitive information you need to get the board running. That's for your security, and in no small part, mine as well. So the way we'll get the sign connected to your wifi to your deployment of the subway sign API, we'll create a mystical file called `secrets.py`.

In a text editor of your choice, create a blank document. Paste the following snippet, and replace the `<parts between alligators>` with your own information.

```python
secrets = {
  'ssid': '<your wifi name>',
  'password': '<your wifi password>',
  'api': '<your subway sign api endpoint, starting with https://>',
  'sign_id': '<your four-letter subway sign id>',
  'aio_username': '<your adafruit io username>',
  'aio_key': '<your adafruit io key>'
}
```

Now save that file to the root directory of your MatrixPortal. It will appear in your file manager as an external volume called `CIRCUITPY`.

### Install the required CircuitPython libraries
Many, if not all, CircuitPython projects rely _heavily_ on libraries, and both Adafruit and the CircuitPython community have made an incredible selection of extremely useful ones. I made liberal use of them for this project. Let's get them installed onto the MatrixPortal.

Head on over to the releases page of the CircuitPython Libraries Bundle and download the 8.x libraries. Unzip the downloaded archive, and navigate to the 'lib' folder within. Find the following files and folders, and copy each into the `lib` folder on your CIRCUITPY drive:

```
- adafruit_bitmap_font
- adafruit_display_shapes
- adafruit_display_text
- adafruit_fakerequests.mpy
- adafruit_io
- adafruit_matrixportal
- adafruit_minimqtt
- neopixel.mpy
```

### Copy the code to the board

Finally it's time to fetch the subway sign code and push it to the board. Clone the code from this repository by running the following in the terminal of your choice:

```bash
$ git clone https://github.com/dzaharia1/subway-sign-python.git
$ cd subway-sign-python
$ cp *.py /Volumes/CIRCUITPY
```

Instantly upon running that last line of code, your MatrixPortal should reboot, and the subway sign software should start running! Head to the subway sign app you deployed, enter the sign code at the prompt, hit "Find my sign" and play around with your settings to get your sign running exactly as you need it. Any settings change should take effect within seconds.

Sign not running properly? Try a few things:
- Check your libraries. Did you make sure to copy _every_ library listed above into the `lib` folder of your CIRCUITPY drive?
- Check that you downloaded the correct library bundle for the version of CircuitPython that you installed onto your MatrixPortal
- Review the values you input into the secrets.py file

__⚠️ Important: Don't yank the USB-C cable from your MatrixPortal at this point. Take the time to eject the CIRCUITPY drive, and then remove the cable to replace it with your long-term power source.__
