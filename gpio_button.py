from gpiozero import Button, LED
from time import sleep
led = LED(17)

button = Button(2)

button.wait_for_press()
led.on()
sleep(3)
led.off()

# print("You pushed me!")
