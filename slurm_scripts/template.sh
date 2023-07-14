#!/usr/bin/env zsh

### Job name
#SBATCH --job-name=eva-vc__n-{n}__mu-{mu}__a-{alpha}__dist-{distribution}__d-{delta}

### declare the merged STDOUT/STDERR file
#SBATCH --output=/home/wy360425/eva_vc_diversity/slurm/outputs/eva-vc__n-{n}__mu-{mu}__a-{alpha}__dist-{distribution}__d-{delta}.out

### Request the time you need for execution in minutes
### The format for the parameter is: hour:minute:seconds,
#SBATCH --time=48:00:00

### ask for less tahn 4 GB memory per task=MPI rank
#SBATCH --mem-per-cpu=2000M   #M is the default and can therefore be omitted, but could also be K(ilo)|G(iga)|T(era)

### OPENMP Parallelization
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16

module load python/3.9.6
module load MATH
module load gurobi/9.1.1
module load gurobipy/911-3.9

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

export PYTHONPATH=/usr/local_rwth/sw/gurobi/gurobi911/linux64/lib:/usr/local_rwth/sw/gurobi/gurobi911/linux64/lib/python3.9_utf32:/usr/local_rwth/sw/python/3.9.6/x86_64/extra/lib/python3.9/site-packages::~/eva_vc_diversity/:/home/wy360425/eva_vc_diversity/
echo ${PYTHONPATH}
pip install -r requirements.txt
python3 main.py --n {n} --delta {delta} --mu {mu} --distribution {distribution} --alpha {alpha}

### end of executable commands
ENDTIME=$(date +%s)
DELTA=$(($ENDTIME - $STARTTIME))
DURATION=$(date -d@$DELTA -u +%H:%M:%S)
echo "------------------------------------------------------------"
echo "Finishing at $(date)"
echo "final spent time is $DURATION"
echo "------------------------------------------------------------"


