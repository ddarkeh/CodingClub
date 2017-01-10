#! /usr/local/bin/python3

import threading
import time
import random
from tkinter import *
from tkinter import ttk

def dayofweek(v_dow_num):
    if (v_dow_num==1):
        v_pop_day="Monday"
    if (v_dow_num==2):
        v_pop_day="Tuesday"
    if (v_dow_num==3):
        v_pop_day="Wednesday"
    if (v_dow_num==4):
        v_pop_day="Thursday"
    if (v_dow_num==5):
        v_pop_day="Friday"
    if (v_dow_num==6):
        v_pop_day="Saturday"
    if (v_dow_num==7):
        v_pop_day="Sunday"
    return(v_pop_day)

def producer(name):
    print('%s' % name + " Created")
    while True:
        v_gen_count = random.randint(1, 10)
        for i in range(v_gen_count):
            v_temp = random.randint(1, 7)
            l_MessageQueue.append(v_temp)
            #print('Producer: %s' % num + " produced " + str(v_temp))
            tbo_input.insert(INSERT, str(v_temp) + "\n")
            l_MessageIn.append(v_temp)
        time.sleep(2)


    print('Producer Destroyed')
    return

def consumer(num):
    print('Consumer %s' % num + " Created")
    while True:
        if (len(l_MessageQueue) > 0):
            v_pop_temp = l_MessageQueue.pop(0)
            v_pop_day = "NA"
            v_pop_day = dayofweek(v_pop_temp)
            #print('Consumer %s' % num + " Converted " + str(v_pop_temp) + " to " + "\"" + v_pop_day + "\"")
            tbo_output.insert(INSERT, v_pop_day + "\n")
            l_MessageOut.append(v_pop_day)
        else:
            time.sleep(10)
    return

def reporter():
    while True:
        tbo_queue.delete(1.0, END)
        v_Queue = "\n".join("{0}".format(n) for n in l_MessageQueue)
        tbo_queue.insert(INSERT, v_Queue)
        time.sleep(0.1)

root = Tk()
root.title("Message Tool")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

lbl_input = ttk.Label(mainframe, text="Input")
lbl_input.grid(column=1, row=1)
tbo_input = Text(mainframe, height=50, width=40)
tbo_input.grid(column=1, row=2)

lbl_queue = ttk.Label(mainframe, text="Message Queue")
lbl_queue.grid(column=2, row=1)
tbo_queue = Text(mainframe, height=50, width=40)
tbo_queue.grid(column=2, row=2)

lbl_output = ttk.Label(mainframe, text="Output")
lbl_output.grid(column=3, row=1)
tbo_output = Text(mainframe, height=50, width=40)
tbo_output.grid(column=3, row=2)

l_MessageIn = []
l_MessageOut = []
l_MessageQueue = []

for i in range(1,10):
    consumers = threading.Thread(target=consumer, args=(i,))
    consumers.start()

producer = threading.Thread(target=producer, args=("Producer",))
reporter = threading.Thread(target=reporter)
producer.start()
reporter.start()

root.mainloop()
