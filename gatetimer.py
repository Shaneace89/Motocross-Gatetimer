import RPi.GPIO as GPIO
import time
import os

localtime = time.asctime( time.localtime(time.time()) )

sensor = 4
redone = 17
redtwo = 10
green = 22 
choice = 0
clearchoice = 0
racer = "default"
shanefast = 0.0
seanfast = 0.0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(redone, GPIO.OUT)
GPIO.setup(redtwo, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

def raceloop(racer, current_state, previous_state):
     print("")
     print racer + " get ready!"
     time.sleep(1.5)
     print("      3")
     time.sleep(1.5)
     print("      2")
     GPIO.output(redone, 1)
     time.sleep(1.5)
     print("      1")
     GPIO.output(redtwo, 1)
     time.sleep(1.5)
     GPIO.output(redone, 0)
     GPIO.output(redtwo, 0)
     GPIO.output(green, 1)
     print("*****GO!*****\n")

     while current_state != True:
         time.sleep(0.1)
         previous_state = current_state
         current_state = GPIO.input(sensor)
         if (current_state != previous_state and current_state != False):
             new_state = "HIGH" if current_state else "LOW"
             print racer + "'s Start Time"
             start = time.asctime( time.localtime(time.time()) )
             starttimer = time.time()
             print start
             GPIO.output(green ,0)
     time.sleep(10.0)        #******change for how long lap time is roughly in secs******
     previous_state = False
     current_state = False
     while current_state != True:
         time.sleep(0.1)
         previous_state = current_state
         current_state = GPIO.input(sensor)
         if (current_state != previous_state and current_state != False):
             new_state = "HIGH" if current_state else "LOW"
             print racer + "'s End Time"
             end = time.asctime( time.localtime(time.time()) )
             endtimer = time.time()
             print end
     elapsed = endtimer - starttimer
     print "Lap time: ", ("%.3f" % elapsed)
     f = open('fastestlaps.txt', 'a')
     f.write(racer + "'s Lap Time: ")
     f.write("%.3f" % elapsed)
     f.write("     " + end)
     f.write("\n")
     f.close()
     return elapsed

while (choice != 9):
  previous_state = False
  current_state = False
  print("")
  print("_________________Main Menu_________________")
  print"1. Shane          Last Lap: ", ("%.3f" % shanefast)
  print"2. Sean           Last Lap: ", ("%.3f" % seanfast)
  print("3. New Racer")
  print("4. Print times to screen")
  print("5. Linux")
  print("8. Clear .txt file")
  print("9. Close\n")

  choice = input('Enter your selection: ')

  if choice == 1:
    racer = 'Shane'
    shanefast = raceloop(racer, current_state, previous_state)
  elif choice == 2:
    racer = 'Sean'
    seanfast = raceloop(racer, current_state, previous_state)
  elif choice == 3:
    racer = raw_input('Please enter new Racer Name: ')
    raceloop(racer, current_state, previous_state)
  elif choice == 4:
    print " "
    inputFile = open("fastestlaps.txt", 'r')
    lineList = inputFile.readlines()
    lineList.sort()
    for line in lineList:
       print(line.rstrip())
  elif choice == 5:
    linuxChoice = 0
    while (linuxChoice != 9):
      print("")
      print("_________________Linux Menu_________________")
      print("1. ls -l")
      print("2. pwd")
      print("3. cp fastestlaps.txt -> fastestcopy.txt")
      print("4. cat fastestlaps.txt")
      print("5. cat fastestcopy.txt")
      print("6. Custom Linux Command *input needed")
      print("9. Exit to Main Menu")
      print("")
      linuxChoice = input('Enter your selection: ')
      print("")
      if linuxChoice == 1:
        os.system('ls -l')
      elif linuxChoice == 2:
        os.system('pwd')
      elif linuxChoice == 3:
        os.system('cp fastestlaps.txt fastestcopy.txt')
        print("Copy successful")
      elif linuxChoice == 4:
        os.system('cat fastestlaps.txt')
      elif linuxChoice == 5:
        os.system('cat fastestcopy.txt')
      elif linuxChoice == 6:
        linuxCommand = raw_input('Please enter linux command: ')
        print("")
        os.system(linuxCommand)
      elif linuxChoice == 9:
        continue
      else:
        print("\nIncorrect input, please try again")
  elif choice == 8:
    clearchoice = input('Are you sure you want to clear fastestlaps.txt? 1 YES or 0 NO ')
    if clearchoice == 1:
       f = open('fastestlaps.txt', 'w')
  elif choice == 9:
    break
  else:
    print("\nIncorrect input, please try again")
