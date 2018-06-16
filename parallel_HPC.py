from joblib import Parallel, delayed
import datetime
import multiprocessing
import time
import numpy as np
import os
import sys

def processInput(i):
    time = datetime.datetime.now()
    print 'Runing %s in process %s'%(i,os.getpid())
    os.system(i)
    print 'End run %s in process %s.  \nTotal time %ds\n'%(i,os.getpid(),(datetime.datetime.now() - time).total_seconds())
    return [i,(datetime.datetime.now() - time).total_seconds(), os.getpid()]

def read_list():
    F = open("list_of_jobs.txt", "r")
    X = []
    while True:
        linea = F.readline()
        if not linea: break
        X.append(linea[:-1])
    F.close()
    return X

if __name__ == '__main__':
    inputs = read_list()
    #print read_list()
    #num_cores = multiprocessing.cpu_count()
    num_cores = int(sys.argv[1])
    results = Parallel(n_jobs=4)(delayed(processInput)(i) for i in inputs)
    W = open('log.txt','w')
    for i in range(len(results)):
        print >> W, '%s - %.3fs - process:%d'%(results[i][0], results[i][1], results[i][2])
    W.close()
