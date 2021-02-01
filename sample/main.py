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

from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont


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

font = ImageFont.load_default()

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
GPIO_TRIGGER = 16
GPIO_ECHO    = 21

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
  image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
  draw = ImageDraw.Draw(image)
  draw.rectangle((1,1,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
  draw.text((3,20), 'Scan Barcode', font=font)
  disp.image(image)
  disp.display()
  barcode = input("enter BArcode:")
  # Load image and convert to 1 bit color.
  image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
  draw = ImageDraw.Draw(image)
  draw.rectangle((1,1,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
  draw.text((3,20), barcode, font=font)

  #Display Image
  disp.image(image)
  disp.display()
  time.sleep(1)
  disp.clear()
  disp.display()
  headers['barcode']=barcode
  GPIO.output(buzzer,GPIO.HIGH)
  sleep(0.5)
  GPIO.output(buzzer,GPIO.LOW)

  while True:
    distance = measure_average()
    print(distance)
    if distance < 10:
      
      tempp = mlx.object_temperature+2
      far = ((9*tempp) / 5) + 32
      tempinLong = str(far)
      temp = tempinLong[:5]
      #tempp=str(temp)
      #headers['temp']=tempp
      print(tempp)
      print(far)
      print("Value of temp is : " + temp)
        # Load image and convert to 1 bit color.
      image= Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
      draw = ImageDraw.Draw(image)
      draw.rectangle((1,1,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
      draw.text((3,20), temp, font=font)

      #Display Image
      disp.image(image)
      disp.display()
      time.sleep(5)
      disp.clear()
      disp.display()
      break

  if far > 100:
      
    GPIO.output(buzzer,GPIO.HIGH)
    sleep(10)
    GPIO.output(buzzer,GPIO.LOW)
    break
  try:
      headers['temp'] = temp
      req=urllib.request.Request(url, headers=headers)
      resp=urllib.request.urlopen(req)
      data=resp.read()
      
  except Exception as e:
      print("network error")
      # Load image and convert to 1 bit color.
      image= Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
      draw = ImageDraw.Draw(image)
      draw.rectangle((1,1,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
      draw.text((3,20),'NO Connection', font=font)

      #Display Image
      disp.image(image)
      disp.display()
      time.sleep(10)
      disp.clear()
      disp.display()
      
    
  GPIO.output(buzzer,GPIO.HIGH)
  sleep(0.5)
  GPIO.output(buzzer,GPIO.LOW)
  sleep(0.5)
  GPIO.output(buzzer,GPIO.HIGH)
  sleep(0.5)
  GPIO.output(buzzer,GPIO.LOW)


   

    

        
  print("end")