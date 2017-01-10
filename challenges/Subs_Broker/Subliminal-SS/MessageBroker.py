#! /usr/local/bin/python3

import threading
import time
import random
from tkinter import *
from tkinter import ttk
import os
import sys

l_MessageQueue = []
l_producers = []
v_produced = 0
l_consumers = []
v_consumed = 0
producerActive = True
consumerActive = True

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

def producerStart(producer_ref):
    global v_produced
    global l_producers
    tbo_input.insert(INSERT, 'Producer Started\n')
    l_producers.append(producer_ref)
    while (producerActive == True):
        v_gen_count = random.randint(1, 10)
        for i in range(v_gen_count):
            v_temp = random.randint(1, 7)
            v_produced = v_produced + 1
            l_MessageQueue.append(v_temp)
            tbo_input.insert(INSERT, str(v_temp) + "\n")
        time.sleep(1)
    else:
        l_producers.remove(producer_ref)
        tbo_input.insert(INSERT, 'Producer Stopped\n')

def consumerStart(consumer_ref):
    global v_consumed
    global l_consumers
    tbo_output.insert(INSERT, 'Consumer %s' % consumer_ref + " Created\n")
    l_consumers.append(consumer_ref)
    while (consumerActive == True):
        if (len(l_MessageQueue) > 0):
            v_pop_temp = l_MessageQueue.pop(0)
            v_pop_day = "NA"
            v_pop_day = dayofweek(v_pop_temp)
            v_consumed = v_consumed + 1
            tbo_output.insert(INSERT, v_pop_day + "\n")
        else:
            time.sleep(0.5)
    else:
        l_consumers.remove(consumer_ref)
        tbo_output.insert(INSERT, 'Consumer %s Stopped\n' %consumer_ref)

def reporterStart():
    global v_produced
    global v_consumed
    global l_MessageQueue
    global l_consumers
    global l_producers
    global producerActive
    global consumerActive

    while True:
        tbo_queue.delete(1.0, END)
        v_Queue = "\n".join("{0}".format(n) for n in l_MessageQueue)
        tbo_queue.insert(INSERT, v_Queue)

        tbo_consumerCount.delete(1.0, END)
        tbo_consumerCount.insert(INSERT, len(l_consumers))

        tbo_producerCount.delete(1.0, END)
        tbo_producerCount.insert(INSERT, len(l_producers))

        tbo_queueDepth.delete(1.0, END)
        tbo_queueDepth.insert(INSERT, len(l_MessageQueue))

        tbo_producerActive.delete(1.0, END)
        tbo_producerActive.insert(INSERT, str(producerActive))

        tbo_consumerActive.delete(1.0, END)
        tbo_consumerActive.insert(INSERT, str(consumerActive))

        tbo_producerRunTot.delete(1.0, END)
        tbo_producerRunTot.insert(INSERT, str(v_produced))

        tbo_consumerRunTot.delete(1.0, END)
        tbo_consumerRunTot.insert(INSERT, str(v_consumed))

        time.sleep(0.5)

def producerCall():
    global producerActive
    producerActive = True
    producer = threading.Thread(target=producerStart, args=(1,))
    producer.start()

def producerStop():
    global producerActive
    producerActive = False
    tbo_input.insert(INSERT, 'Producer Stopping...\n')

def consumerCall():
    global consumerActive
    consumerActive = True
    for i in range(1,10):
        consumer = threading.Thread(target=consumerStart, args=(i,))
        consumer.start()

def consumerStop():
    global consumerActive
    consumerActive = False
    tbo_output.insert(INSERT, 'Consumers Stopping...\n')

root = Tk()
root.title("Message Tool")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=2)
mainframe.rowconfigure(0, weight=2)

##Column 1
Column1 = 1
ttk.Label(mainframe, text="Input").grid(column=Column1-1, row=1, columnspan=2)

tbo_input = Text(mainframe, height=30, width=30)
tbo_input.grid(column=Column1-1, row=2, columnspan=2)

but_ProducerStart = ttk.Button(mainframe, text="Start New Producer", command=producerCall)
but_ProducerStart.grid(column=Column1-1, row=3, columnspan=2)

but_ProducerStop = ttk.Button(mainframe, text="Stop All Producers", command=producerStop)
but_ProducerStop.grid(column=Column1-1, row=4, columnspan=2)

ttk.Label(mainframe, text="Active Producers:").grid(column=Column1-1, row=5)
tbo_producerCount = Text(mainframe, height=1, width=5)
tbo_producerCount.grid(column=Column1, row=5)

ttk.Label(mainframe, text="Producer Active?:").grid(column=Column1-1, row=6)
tbo_producerActive = Text(mainframe, height=1, width=5)
tbo_producerActive.grid(column=Column1, row=6)

ttk.Label(mainframe, text="Total Produced:").grid(column=Column1-1, row=7)
tbo_producerRunTot = Text(mainframe, height=1, width=5)
tbo_producerRunTot.grid(column=Column1, row=7)

ttk.Label(mainframe, text=" ").grid(column=Column1+1, row=1)

##Column 2
Column2 = 5
ttk.Label(mainframe, text="Message Queue").grid(column=Column2-1, row=1, columnspan=2)
tbo_queue = Text(mainframe, height=30, width=30)
tbo_queue.grid(column=Column2-1, row=2, columnspan=2)

ttk.Label(mainframe, text="Queue Depth:").grid(column=Column2-1, row=4)
tbo_queueDepth = Text(mainframe, height=1, width=5)
tbo_queueDepth.grid(column=Column2, row=4)

ttk.Label(mainframe, text=" ").grid(column=Column2+1, row=1)

##Column 3
Column3 = 10
ttk.Label(mainframe, text="Output").grid(column=Column3-1, row=1, columnspan=2)
tbo_output = Text(mainframe, height=30, width=30)
tbo_output.grid(column=Column3-1, row=2, columnspan=2)

but_consumerStart = ttk.Button(mainframe, text="Start consumers", command=consumerCall)
but_consumerStart.grid(column=Column3-1, row=3, columnspan=2 )

but_ConsumersStop = ttk.Button(mainframe, text="Stop Consumers", command=consumerStop)
but_ConsumersStop.grid(column=Column3-1, row=4, columnspan=2)

ttk.Label(mainframe, text="Active Producers:").grid(column=Column3-1, row=5)
tbo_consumerCount = Text(mainframe, height=1, width=5)
tbo_consumerCount.grid(column=Column3, row=5)

ttk.Label(mainframe, text="Producer Active?:").grid(column=Column3-1, row=6)
tbo_consumerActive = Text(mainframe, height=1, width=5)
tbo_consumerActive.grid(column=Column3, row=6)

ttk.Label(mainframe, text="Total Consumed:").grid(column=Column3-1, row=7)
tbo_consumerRunTot = Text(mainframe, height=1, width=5)
tbo_consumerRunTot.grid(column=Column3, row=7)

reporter = threading.Thread(target=reporterStart)

reporter.start()

root.mainloop()
sys.exit
