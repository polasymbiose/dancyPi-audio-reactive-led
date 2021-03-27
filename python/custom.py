from rpi_ws281x import *
import time, math
import config
import argparse
from random import randint, randrange, shuffle
LED_STRIP = ws.SK6812W_STRIP
mystrip = PixelStrip(config.N_PIXELS, config.LED_PIN, config.LED_FREQ_HZ, config.LED_DMA, config.LED_INVERT, config.BRIGHTNESS, 0, LED_STRIP)

def strobe(strip, wait_ms=400, strobe_count=1, pulse_count=12):
  from random import randrange
  """LED als springender Ball"""
  for strobe in range(strobe_count):    
      for pulse in range(pulse_count):
          for i in range(strip.numPixels()):
              strip.setPixelColor(i, Color(0,0,0,255))
          strip.show()
          time.sleep(randrange(0,45,1)/1000.0)
          for i in range(strip.numPixels()):
              strip.setPixelColor(i, Color(0,0,0,0))
          strip.show()
      time.sleep(wait_ms/1000.0)
      
def colorWipe(strip, color = Color(0,0,0,255), wait_ms=5):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0,255))
        strip.show()
        time.sleep(wait_ms / 1000.0)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0,0))
        strip.show()
        time.sleep(wait_ms / 10000.0)

def pulsing_light(strip, wait_ms=500, iterations=10):
    """Helle LIchteffekte in Kette"""
    position = 0
    for i in range(strip.numPixels() * 2):
        position = position+1
        for j in range(strip.numPixels()):
            print("asdf", j+position)
            print(round(((math.sin(j+position) * 127 + 128)/255)*255))
            strip.setPixelColor(j,Color(0, 0, 0, round(((math.sin(j+position) * 127 + 128)/255)*255)))
        strip.show()
        time.sleep(wait_ms/1000.0)


def randomFx(strip,sparkle_delay=1):
    
    randomlist = []
    for i in range(0,int(config.N_PIXELS / 4)):
        n = randint(1,config.N_PIXELS)
        randomlist.append(n)
    
    maxValue = 255
    valueDivider = 5
    
    valuelist = []
    

    for i in range(0,maxValue):
        valuelist.append(i)
    
    for i in reversed(range(1, maxValue)):
        valuelist.append(i)
   
    
    
    # pixel= randint(0,strip.numPixels())
    # speed_delay=randint(10,100)
    # for i in range(strip.numPixels()):
    #     strip.setPixelColor(i, Color(0,0,0,55))
    
    # for i in range(int(strip.numPixels() / 4)):
    #     randomLed= randint(0,strip.numPixels())
    #     randomValue = randint(70, 255)
    #     strip.setPixelColor(i * 4, Color(0,0,0,round(((math.sin(i * 4) * 127 + 128)/255)*255)))
    #     strip.show()
        
    # for j in 4: 
    #     for i in range(strip.numPixels()):
    #         strip.setPixelColor(i, Color(0,0,0,int(50*j)))
    #     strip.show()
        
    print(randrange(0,255,1))
    numrange = range(strip.numPixels())
    for j in valuelist:
        # print(j)
        for i in numrange:
            # print(i)
            if i in randomlist:
                strip.setPixelColor(i, Color(0,0,j,22))
            else:
                strip.setPixelColor(i, Color(0,0,0, 22))
        strip.show()
    
        # time.sleep(0)
    
    # time.sleep(speed_delay/1000.0)
    # strip.setPixelColor(pixel, Color(0,0,0,0))
    # strip.show()
    
def fadebackup(r1,g1,b1,w1, r2,g2,b2,w2, steps,interval):
    lastUpdate = time.time() - interval
    for i in range(1, steps + 1):
        r = round(((r1 * (steps - i)) + (r2 * i)) / steps)
        g = round(((g1 * (steps - i)) + (g2 * i)) / steps)
        b = round(((b1 * (steps - i)) + (b2 * i)) / steps)
        w = round(((w1 * (steps - i)) + (w2 * i)) / steps)

        while ((time.time() - lastUpdate) < interval):
            pass
        # print("{: 3d} ({:0.3f}s): {:03d}, {:03d}, {:03d}, {:03d}".format(i, time.time() - lastUpdate, r, g, b, w))
        color = Color(r, g, b, w)
        for j in range(mystrip.numPixels()):
            mystrip.setPixelColor(j, color)
        mystrip.show()

        lastUpdate = time.time()




def random(r1,g1,b1,w1, r2,g2,b2,w2, steps,interval):
    randomlist2 = []
    lastUpdate = time.time() - interval
    r = list(range(300))
    rnolist = list(range(300))

    shuffle(rnolist)

    for i in range(0,int(config.N_PIXELS / 3)):
        n = randint(1,config.N_PIXELS)
        randomlist2.append(n)

    
    # for i in range(1, steps + 1):
    #     r = round(((r1 * (steps - i)) + (r2 * i)) / steps)
    #     g = round(((g1 * (steps - i)) + (g2 * i)) / steps)
    #     b = round(((b1 * (steps - i)) + (b2 * i)) / steps)
    #     w = round(((w1 * (steps - i)) + (w2 * i)) / steps)

  
        
    for j in range(1, 300):
        while ((time.time() - lastUpdate) < interval):
            pass
        # print("{: 3d} ({:0.3f}s): {:03d}, {:03d}, {:03d}, {:03d}".format(i, time.time() - lastUpdate, r, g, b, w))
        ind = rnolist[j]
        color = Color(0, 0, 0, 255) if j in randomlist2 else Color(0, 0, 0, 10)
        mystrip.setPixelColor(ind, color)
        mystrip.show()
    lastUpdate = time.time()

 
# def build(strip, interval):
#     divider =8
#     lastUpdate = time.time() - interval
#     adder = round(300 / divider)
    
#     while True:
#         for j in range(300):
#             mystrip.setPixelColor(j, Color(0,0,0,22))
#         mystrip.show()
#         for j in range(0, adder):
#             while ((time.time() - lastUpdate) < interval):
#                 pass
#             # print("{: 3d} ({:0.3f}s): {:03d}, {:03d}, {:03d}, {:03d}".format(i, time.time() - lastUpdate, r, g, b, w))
#             mystrip.setPixelColor(j, Color(0,0,0,255))
#             mystrip.setPixelColor(j + adder, Color(0,0,0,255))
#             mystrip.setPixelColor(j + adder + adder, Color(0,0,0,255))
#             mystrip.setPixelColor(j + adder + adder + adder, Color(0,0,0,255))
#             mystrip.setPixelColor(j + adder + adder + adder + adder, Color(0,0,0,255))
#             mystrip.setPixelColor(j + adder + adder + adder + adder + adder, Color(0,0,0,255))
#             mystrip.setPixelColor(j + adder + adder + adder + adder + adder + adder, Color(0,0,0,255))
#             mystrip.show()
#             lastUpdate = time.time()
#         for j in range(1, adder):
#             while ((time.time() - lastUpdate) < interval):
#                 pass
#             # print("{: 3d} ({:0.3f}s): {:03d}, {:03d}, {:03d}, {:03d}".format(i, time.time() - lastUpdate, r, g, b, w))
#             mystrip.setPixelColor(j, Color(0,0,0,22))
#             mystrip.setPixelColor(j + adder, Color(0,0,0,22))
#             mystrip.setPixelColor(j + adder + adder, Color(0,0,0,22))
#             mystrip.setPixelColor(j + adder + adder + adder, Color(0,0,0,22))
#             mystrip.setPixelColor(j + adder + adder + adder + adder, Color(0,0,0,22))
#             mystrip.setPixelColor(j + adder + adder + adder + adder + adder, Color(0,0,0,22))
#             mystrip.setPixelColor(j + adder + adder + adder + adder + adder + adder, Color(0,0,0,22))
#             mystrip.show()
#             lastUpdate = time.time()


def snow_sparklerandomFx(strip,sparkle_delay=1):
    from random import randint
    pixel= randint(0,strip.numPixels())
    print(pixel)
    speed_delay=randint(100,1000)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0,0))
    strip.show()
    time.sleep(speed_delay/1000.0)
    strip.setPixelColor(pixel, Color(0,0,0,255))
    strip.show()
    time.sleep(sparkle_delay/1000.0)

def sinewave():
    for j in range(1, 300):
        color = Color(0, 0, 0, 255)
        mystrip.setPixelColor(j, color)
        mystrip.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    mystrip.begin()
 
    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
    try:
        while True:
            #Entkommentieren um Programm auszuwählen
            # colorWipe(mystrip)
            #theaterChase(strip)
            # strobe(mystrip)
            # pulsing_light(mystrip)
            # randomFx(mystrip)
            # random(0,0,0,0, 0,0,0,255, 40,0.025)
            # build(mystrip, 0.000001)
            sinewave()
            # snow_sparkle(mystrip)
            #strobe(strip)
            #bouncing_balls()
    except KeyboardInterrupt:
        if args.clear:
            colorWipe(mystrip, Color(0, 0, 0, 0), 10)