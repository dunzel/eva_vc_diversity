import os

import matplotlib.pyplot as plt
import pandas as pd


def get_line_graph():
    df_uniform = pd.read_csv("../../results/unconstrained/n-50_d-2_m-64_uniform1/log.txt")
    df_poisson = pd.read_csv("../../results/unconstrained/n-50_d-2_m-64_poisson/log.txt")

    df_uniform.columns = ['generation', 'unique_ind', 'population_fitness', 'best_ind_vc_cnt', 'mean_vc_overlap', 'std_vc_overlap', 'avg_node_degree', 'avg_node_leafes']
    df_poisson.columns = df_uniform.columns

    titles = {
        'unique_ind': 'Unique Individuals',
        'population_fitness': 'Population Fitness',
        'best_ind_vc_cnt': 'VC Size Of Best Individual',
        'mean_vc_overlap': "Mean Overlap of VC's",
        'std_vc_overlap': "Standard Deviation Overlap of VC's",
        'avg_node_degree': 'Average Node Degree',
        'avg_node_leafes': 'Average Node Leafes'
    }

    attributes = df_uniform.columns[4:]

    fig, axs = plt.subplots(4, figsize=(5, 8))

    for i, attr in enumerate(attributes):
        axs[i].plot(df_uniform['generation'], df_uniform[attr], label='Uniform', color='black', linestyle='-')
        axs[i].plot(df_poisson['generation'], df_poisson[attr], label='Poisson', color='grey', linestyle='dashed')
        axs[i].set_title(titles[attr])
        axs[i].set_xlabel('Generations')

        if attr == 'population_fitness':
            axs[i].set_yscale('log')

        axs[i].legend()

    plt.tight_layout()
    plt.savefig("line_graph_2.pdf")


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    get_line_graph()
