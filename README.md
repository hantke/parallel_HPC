# parallel_HPC


Run a serial of one jobs from a list (in list_of_jobs.txt), it runs them with a limit of threads. When a CPU finish, it will start with the next job on the list.
All CPU will be in use until the number of unrun jobs is lower than the number of CPU.

How to Run:
python parallel_HPC ncpu
with ncpu the number of threads you want to use (eg. 20 for orte-20 in the cluster

qsub job.sh to run them on the cluster.

Comments are welcome. If you want to improve, make more elegant or fix the code, you are all welcome to participate, I will add you to the git folder ASAP.

