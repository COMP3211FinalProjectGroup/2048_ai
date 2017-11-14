"""
benchmark algorithms and output results.
this file uses multiprocessing and bypass the graphical output so the speed is 100x
modified from Github (https://gist.github.com/fungus/9821090)

@author: WONG, Ngo Yin
1. use txt file instead of database
2. migrate to python 3
3. now can use different algorithms
"""

#please remember to change the algorithm when use


import sys
import random
from time import time
from multiprocessing import Process, Queue
from term2048.game import Game

from term2048 import randomMove

def run_game(q1, q2):
    while True:
        g = Game()
        while g.board.canMove():
            m = randomMove.next_move()
            g.incScore(g.board.move(m))

        if g.board.won():
            print(g)
        q1.put(g.score)
        q2.put(g.board.won())

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

    q1 = Queue()
    q2 = Queue()

    file_name = input("file name: ")

    file_name += ".txt"

    out_file = open(file_name,"w")


    # Start game processes
    for i in range(4):
        p = Process(target=run_game,args=(q1, q2))
        procs.append(p)
        p.start()
    
    # Main loop to record scores
    try:
        while True:
            score = q1.get()
            won = q2.get()
            k = str(score)
            if score > high_score:
                high_score = score

            out_file.write(str(count)+"\t")
            out_file.write(str(score)+"\t")
            out_file.write(str(won)+"\t")
            out_file.write("\n")
            out_file.flush()
            count += 1
            progress()
    # Cleanup
    finally:
        for p in procs:
            p.terminate()
