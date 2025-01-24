import gpiozero
import time

led = gpiozero.LED(12)

for i in range(5):
	led.on()
	time.sleep(0.5)
	led.off()
	time.sleep(0.5)
	
quit()
