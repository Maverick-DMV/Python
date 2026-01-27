import board
import digitalio
import time
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL,10)
led.brightness = 0.1

while True:
    led[0] = (0,255,0)
    led[1] = (255,0,0)
    led[2] = (0,255,0)
    led[3] = (255,0,0)
    led[4] = (0,255,0)
    led[5] = (255,0,0)
    led[6] = (0,255,0)
    led[7] = (255,0,0)
    led[8] = (0,255,0)
    led[9] = (255,0,0)
