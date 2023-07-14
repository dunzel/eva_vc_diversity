#!/usr/bin/env zsh

### Job name
#SBATCH --job-name=eva-vc__n-50__mu-64__a-0.05__dist-uniform2__d-4

### declare the merged STDOUT/STDERR file
#SBATCH --output=/home/wy360425/eva_vc_diversity/slurm_scripts/outputs/eva-vc__n-50__mu-64__a-0.05__dist-uniform2__d-4.out

### Request the time you need for execution in minutes
### The format for the parameter is: hour:minute:seconds,
#SBATCH --time=48:00:00

### ask for less tahn 4 GB memory per task=MPI rank
#SBATCH --mem-per-cpu=2000M   #M is the default and can therefore be omitted, but could also be K(ilo)|G(iga)|T(era)

### OPENMP Parallelization
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16

module load Python/3.10.4
module load Gurobi/10.0.0

### Change to the work directory
cd $HOME/eva_vc_diversity/ || exit

STARTTIME=$(date +%s)
echo "------------------------------------------------------------"
echo "SLURM JOB NAME: $SLURM_JOB_NAME"
echo "SLURM JOB ID: $SLURM_JOBID"
echo "Running on nodes: $SLURM_NODELIST"
echo "Number of CPUs: $SLURM_CPUS_PER_TASK"
echo "Started at $(date)"
echo "------------------------------------------------------------"
### beginning of executable commands
python3 main.py --n 50 --delta 4 --mu 64 --distribution uniform2 --alpha 0.05

### end of executable commands
ENDTIME=$(date +%s)
DELTA=$(($ENDTIME - $STARTTIME))
DURATION=$(date -d@$DELTA -u +%H:%M:%S)
echo "------------------------------------------------------------"
echo "Finishing at $(date)"
echo "final spent time is $DURATION"
echo "------------------------------------------------------------"


