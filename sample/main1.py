import RPi.GPIO as GPIO
import time
from time import sleep
import serial
import time
import urllib.request
import board
import busio as io
import adafruit_mlx90614
import time
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
import lcdlib as lcd

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Initialise display on pins and width
lcd.init(25,24,23,17,18,22,16)

# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0


# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Initialize library.
disp.begin(contrast=40)

# Clear display.
disp.clear()
disp.display()


def measure():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()

  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * 34300)/2

  return distance

def measure_average():
  # This function takes 3 measurements and
  # returns the average.
  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance


# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 12
GPIO_ECHO    = 26

print ("Ultrasonic Measurement")
# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer=17
GPIO.setup(buzzer,GPIO.OUT)
#Run forever loop

while True:
  url='https://obscure-cliffs-43212.herokuapp.com/pythontoExpress'
  headers={}
  lcd.string("ENTER BARCODE :",LCD_LINE_1)
  barcode = input("enter BArcode:")
  lcd.string(barcode,LCD_LINE_1)
  sleep(1)
  headers['barcode']=barcode
  GPIO.output(buzzer,GPIO.HIGH)
  sleep(0.5)
  GPIO.output(buzzer,GPIO.LOW)
  i = 50 
  temp = "0"
  while i >= 0:
    
    distance = measure_average()
    print( distance)
    if distance < 10:
        
        tempp = mlx.object_temperature
        far = ((9*tempp) / 5) + 35.7
        tempinLong = str(far)
        print(tempinLong , type(tempinLong))
        temp = tempinLong[:5]
        print("Value of temp is : " + temp)
        lcd.string("TEMPERATURE IS:",LCD_LINE_1)
        lcd.string(temp,LCD_LINE_2)
        time.sleep(3)
        break    
        if far > 100:
            
            GPIO.output(buzzer,GPIO.HIGH)
            sleep(10)
            GPIO.output(buzzer,GPIO.LOW)
            break
    i = i-1
    print(i)
  if temp !="0":
      try:
          headers['temp'] = temp
          req=urllib.request.Request(url, headers=headers)
          resp=urllib.request.urlopen(req)
          data=resp.read()
      
      except Exception as e:
          print("network error")
          lcd.string("CHECK INTERNET",LCD_LINE_1)
          time.sleep(10)
      GPIO.output(buzzer,GPIO.HIGH)
      sleep(0.5)
      GPIO.output(buzzer,GPIO.LOW)
      sleep(0.5)
      GPIO.output(buzzer,GPIO.HIGH)
      sleep(0.5)
      GPIO.output(buzzer,GPIO.LOW)
      lcd.string("SUCCESSFULL!!!",LCD_LINE_1)
      time.sleep(2)
  else:
        lcd.string("YOUR TEMPERATURE",LCD_LINE_1)
        lcd.string("NOT FOUND!!!",LCD_LINE_2)
        time.sleep(2)
 
  
      