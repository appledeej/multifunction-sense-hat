from sense_hat import SenseHat
import time

sense = SenseHat()

print("Welcome to appledeej's multi-function sense hat sensory doodle")
while True:
    print("1.Temperature")
    print("2.Humidity")
    print("3.Barometric Pressure")
    
    option = int(input("Please choose an option: "))

        

    if option == 1:
        sense = SenseHat()
        temp = sense.get_temperature()
        print("Temperature: %s C" % temp)
        temp = round(temp) 
        temp = str(temp)
        sense.show_message(temp,text_colour=[255, 0, 0]) 

    if option == 2:
        humidity = sense.get_humidity()
        print("Humidity: %s %%rH" % humidity)
        humidity = str(humidity)
        sense.show_message(humidity,text_colour=[255, 0, 0])
        
    if option == 3:
        pressure = sense.get_pressure()
        print("Pressure: %s Millibars" % pressure)
        pressure = str(pressure)
        sense.show_message(pressure,text_colour=[255, 0, 0])
        
        
    if option == 4: 
      while True:
        gyro_only = sense.get_gyroscope()
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))
