import RPi.GPIO as GPIO
import time

# on/off functions:
def liteon(pin, tiim):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(tiim)
def liteoff(pin, tiim):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(tiim)
    return 0

# to use Raspberry Pi board pin numbers:
GPIO.setmode(GPIO.BOARD)

# setup GPIO output channel:
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# blink GPIO07 5 Times. Green pin 7, yello pin 11, red pin 13:
for i in range(0, 5):
    liteon(7, 2)
    liteoff(7, 0.1)
    liteon(11, 2)
    liteoff(11, 0.1)
    liteon(13, 2)
    liteoff(13, 0.1)
print("Done")
GPIO.cleanup()