#!/usr/bin/python

SIZE = 4

import sys
import dbhash
import random
from time import time
from multiprocessing import Process, Queue
from term2048.game import Game

def run_game(q):
    while True:
        g = Game(None,size=SIZE)
        while g.board.canMove():
            m = random.choice((1,2,3,4))
            g.incScore(g.board.move(m))

        if g.board.won():
            print g
        q.put(g.score)

def progress():
    now = time()
    rate = count / (now - start)
    output = "\r%i high %f g/s %i total" % (high_score,rate,count)
    sys.stdout.write(output)
    sys.stdout.flush()

if __name__ == '__main__':
    # Initialization
    start = time()
    count = 0
    high_score = 0
    procs = []
    freq = dbhash.open('results-%i.db'%SIZE,'c')
    q = Queue()

    # Start game processes
    for i in range(4):
        p = Process(target=run_game,args=(q,))
        procs.append(p)
        p.start()
    
    # Main loop to record scores
    try:
        while True:
            score = q.get()
            k = str(score)
            if k in freq:
                freq[k] = str(int(freq[k]) + 1)
            else:
                freq[k] = '1'
            if score > high_score:
                high_score = score
            count += 1
            progress()
            freq.sync()
    # Cleanup
    finally:
        for p in procs:
            p.terminate()
