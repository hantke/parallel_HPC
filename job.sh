#/bin/bash 
#$ -j y 
#$ -cwd 
#$ -m n 
#$ -pe orte-20 20 
#$ -l h_rt=47:00:00 
 
python parallel_HPC.py 20
##Recomended -pr orte-40 40 ... python parallel_HPC.py 40
