#!/bin/python2.7

import os
import sys
from subprocess import Popen, PIPE
from multiprocessing import cpu_count
import threading
from time import time

RUN_TIMES = 10

standings = {
    'P1':{},
    'P2':{},
    'NONE':{}
}

if len(sys.argv) == 2:
    RUN_TIMES = int(sys.argv[1])

def print_results():
    os.system('clear')
    print "MATCHES LEFT:", RUN_TIMES
    for key in standings:
        total = 0
        print "\n", key, ":"
        for reason in standings[key]:
            print "\t", reason, ":", standings[key][reason]
            total += standings[key][reason]
        print "Total Won:", total
        print "\n#####"
    print "\n".join(time_log[-20:])

time_log = []

def run_prog():
    global RUN_TIMES, standings, time_log
    while RUN_TIMES >= 0:
        score_lock.acquire_lock()
        print_results()
        score_lock.release_lock()

        (stdout, stderr) = Popen(['bash', 'benchmark.sh'], stdout=PIPE).communicate()
        winner, reason, time_list = stdout.strip().split('\n')[-3:]

        score_lock.acquire_lock()
        if winner == "P2":
            open('loses', 'a+').write(stdout)
        time_log += [time_list]
        if reason in standings[winner]:
            standings[winner][reason] += 1
        else:
            standings[winner][reason] = 1
        RUN_TIMES -= 1
        score_lock.release_lock()

score_lock = threading.Lock()
CORES = 1#cpu_count()
threads = [threading.Thread(target=run_prog) for i in range(CORES)]

for i in range(CORES):
    threads[i].setDaemon(True)
    threads[i].start()

for i in range(CORES):
    threads[i].join()

open('benchmark.log', 'w+').write("\n".join(time_log[:10]))
