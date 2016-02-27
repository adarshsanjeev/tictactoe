#!/bin/python2.7

import os
from subprocess import Popen, PIPE

RUN_TIMES = 100

standings = {
    'P1':{},
    'P2':{},
    'NONE':{}
}

while RUN_TIMES:
    (stdout, stderr) = Popen(['bash', 'benchmark.sh'], stdout=PIPE).communicate()
    winner, reason = stdout.strip().split('\n')
    if reason in standings[winner]:
        standings[winner][reason] += 1
    else:
        standings[winner][reason] = 1
    RUN_TIMES -= 1

for key in standings:
    total = 0
    print key, ":"
    for reason in standings[key]:
        print "\t", reason, ":", standings[key][reason]
        total += standings[key][reason]
    print "Total Won:", total
    print "\n#####\n"
