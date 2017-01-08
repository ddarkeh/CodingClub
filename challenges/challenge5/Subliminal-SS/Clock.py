#! /usr/local/bin/python3
import re
import time

def f_FowardTime(v_InputTime):
   l_TimeList = v_InputTime.split(":")
   v_sec = int(l_TimeList[2])
   v_min = int(l_TimeList[1])
   v_hou = int(l_TimeList[0])
   v_TotalSeconds = (v_hou * 3600) + (v_min * 60) + v_sec
   v_TotalSeconds = v_TotalSeconds + 1
   v_OutputTime = time.strftime('%H:%M:%S', time.gmtime(v_TotalSeconds))
   return v_OutputTime

#START OF MAIN PROGRAM
v_InputCheck = False

while (v_InputCheck == False):
   v_Input = input("Enter the Time to Start From in HH24:MM:SS")
   #v_Input = "23:50:59"
   re_Input = re.compile("^[0-2][0-3]:[0-5][0-9]:[0-5][0-9]$")
   result = re_Input.match(v_Input)
   if result:
       v_InputCheck = True
   else:
       v_InputCheck = False


v_Time = v_Input

print(v_Time)

while True:
   v_Time = f_FowardTime(v_Time)
   print(v_Time)
   time.sleep(1)
