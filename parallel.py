from joblib import Parallel, delayed
import multiprocessing
import time
import numpy as np
import os
# what are your inputs, and what operation do you want to
# perform on each input. For example...
inputs = range(10)
def processInput(i):
    print 'Runing i=',i,os.getpid()
    time.sleep(20-2*i)
    print 'end run i=',i,os.getpid()
    return i * i
num_cores = multiprocessing.cpu_count()
results = Parallel(n_jobs=4)(delayed(processInput)(i) for i in inputs)
print results, num_cores

