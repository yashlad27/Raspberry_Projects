from gpiozero import Button, TrafficLights, Buzzer, LED
from time import sleep

button = Button(21)
# led = LED(25)
lights = TrafficLights(25, 8, 7)
buzzer = Buzzer(15)

while True:
    button.wait_for_press()
    lights.green.on()
    sleep(1)
    lights.amber.on()
    sleep(1)
    lights.red.on()
    sleep(1)
    lights.off()

