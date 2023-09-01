# Evolutionary Diversity Optimization for Minimum Vertex Cover Problem
This repository contains the source code for the paper "Evolutionary Diversity Optimization With An Example Application For Vertex Covers". 
The paper can be found in the directory "paper" as "ECSE23-EDO-camera-ready.pdf". 
Furthermore, the paper directory contains the code for the generating the tables and figures in the paper.

The directory "results" contains the results of our experiments. The first subdirectories distinguish between the constrained (with alpha) and unconstrained version of the problem.
The second level of subdirectories distinguishes between graph size, delta (average node degree), population size and mutation strategy.

The directory "slurm_scripts" contains the scripts used to run the experiments on the HPC cluster of RWTH Aachen University. 
Based on the file "template.sh" and "script_generator.py" the scripts were generated and moved to the subdirectory "executable_scripts".
The scripts were then executed on the cluster using the command "sbatch <script_name>.sh". General logs were written to the subdirectory "outputs".

The core source code of our implementation of the EDO algorithm can be found in the directory "eva_algos". 
We seperated the code into the following files:
- "inital_population.py": Contains the functions for generating the initial population.
- "operators.py": Contains the implementation of the MultiNodeSwap mutation operator.
- "fitness_functions.py": Contains the fitness functions that calculate the diversity but also measures for the structure of the solutions in the population.
- "utils.py": Contains auxiliary functions used in multiple files.
- "mu_plus_one_ea_custom.py": Contains the implementation of the mu+1 EA with the MultiNodeSwap mutation operator.

The directory "instances" contains our randomly generated graph instances and also the scripts to generate, load and render them.

The directory "misc" contains the gurobi solver for the ILP formulation of the MVC problem. We need this solver to calculate the optimal solution for the instances.

## Requirements 
The requirements to run the code are listed in the file "requirements.txt". In general, you need python 3.7 and the packages listed in the file.
This repository contains also a docker file that can be used to run the code in a docker container.

## Running the code
To run the code, you can use the following command:
```
python3 main.py
```

You can use the following arguments:

| Argument       | Description                          |
|----------------|--------------------------------------|
| --n            | The number of vertices in the graph. |
| --delta        | The average node degree of the graph. |
| --alpha        | The alpha parameter of the EDO algorithm. |
| --mu           | The population size of the EDO algorithm. |
| --distribution | The mutation strategy of the EDO algorithm. |

For example, to run the EDO algorithm with own parameters, you can use the following command:
```
python3 main.py -n 100 -delta 2 -alpha 0.5 -mu 64 -distribution poisson
```

If these arguments are not enough, you can also change the parameters in the file "settings.py".
There you can find some more advanced parameters that can be changed. For example, you can change the number of maximal iterations, the random seed and more.

If you have any questions, feel free to contact us at:
[daniel.zelenak@rwth-aachen.de](mailto:daniel.zelenak@rwth-aachen.de)

