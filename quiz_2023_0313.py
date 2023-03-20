from machine import Pin,Timer

Gp1 = Pin(3, mode=Pin.IN, pull=Pin.PULL_UP)
Gp2 = Pin(2, mode=Pin.IN, pull=Pin.PULL_UP)
Gp3 = Pin(1, mode=Pin.OUT)

def toggle_buttons(timer):
    Gp1.value(not Gp1.value())
    Gp2.value(not Gp2.value())
    while True:
    if Gp1.value() == 1 and Gp2.value() == 1:
        Gp3.on()
    else:
        Gp3.off()

timer = machine.Timer(0)
timer.init(period=1000, mode=machine.Timer.PERIODIC, callback=toggle_buttons)