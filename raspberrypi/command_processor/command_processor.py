#!/usr/bin/python
import time
import os
from subprocess import call
while(1):
	f = open("/home/pi/voice-control-robot/raspberrypi/command_processor/command.txt", "r")
	command = f.read()
	if(command == "stop"):
		print("stopping")
		f = open("command.txt", "w")
		f.write("idle")
		call(["python", "../stop.py"])
	if(command == "forward"):
		print("forward")
		f = open("command.txt", "w")
		f.write("idle")
		call(["python", "../forward.py"])
	time.sleep(0.1)
