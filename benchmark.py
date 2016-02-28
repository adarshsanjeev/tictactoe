#!/bin/python2.7

import os
import sys
from subprocess import Popen, PIPE

RUN_TIMES = 10

standings = {
    'P1':{},
    'P2':{},
    'NONE':{}
}

if len(sys.argv) == 2:
    RUN_TIMES = int(sys.argv[1])

def print_results():
    for key in standings:
        total = 0
        print "\n", key, ":"
        for reason in standings[key]:
            print "\t", reason, ":", standings[key][reason]
            total += standings[key][reason]
        print "Total Won:", total
        print "\n#####"

while RUN_TIMES:
    (stdout, stderr) = Popen(['bash', 'benchmark.sh'], stdout=PIPE).communicate()
    os.system('clear')
    print "MATCHES LEFT:", RUN_TIMES
    print_results()
    winner, reason = stdout.strip().split('\n')
    if reason in standings[winner]:
        standings[winner][reason] += 1
    else:
        standings[winner][reason] = 1
    RUN_TIMES -= 1
