#!/usr/bin/python3
import RPi.GPIO as GPIO
import math, sys, os
import random
import subprocess
import socket
import pygame
import pygame.mixer
from pygame.mixer import Sound

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.mixer.init()
c=0
last = 1

def count(pin):
    global c
    c = c + 1

GPIO.add_event_detect(24, GPIO.BOTH)

while True:
    try:
        if GPIO.event_detected(24):
            current = GPIO.input(24)
            if(last != current):
                if(current == 0):
                    GPIO.add_event_detect(11, GPIO.BOTH, callback=count, bouncetime=5)
                else:
                    GPIO.remove_event_detect(11)
                    number = int(c/2)


                    print ("You dialled", number)
                    if number == 1:
                        choon = Sound('/home/pi/phones/hanging.wav')
                        choon.play()
                    elif number == 2:
                        choon = Sound('/home/pi/phones/callme.wav')
                        choon.play()
                    elif number == 3:
                        choon = Sound('/home/pi/phones/clarksville.wav')
                        choon.play()
                    elif number == 4:
                        choon = Sound('/home/pi/phones/hesonthephone.wav')
                        choon.play()
                    elif number == 5:
                        choon = Sound('/home/pi/phones/payphone.wav')
                        choon.play()
                    elif number == 6:
                        choon = Sound('/home/pi/phones/ring.wav')
                        choon.play()
                    elif number == 7:
                        choon = Sound('/home/pi/phones/sidewinder.wav')
                        choon.play()
                    elif number == 8:
                        choon = Sound('/home/pi/phones/telephone.wav')
                        choon.play()
                    elif number == 9:
                        choon = Sound('/home/pi/phones/whydontcall.wav')
                        choon.play()
                    elif number == 10:
                        os.system("sudo shutdown -h now")

                    c= 0


                last = GPIO.input(24)

    finally:
        GPIO.cleanup
