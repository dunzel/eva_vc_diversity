ns = [50, 100, 200]
mus = [2, 16, 32, 64]
deltas = [2, 8] #4,
distributions = ["uniform1", "poisson"]
alphas = [-1] # , 0.05, 0.5

# n, delta, mu, distributions, alpha are the indices of the columns
# iterate over the files in ../results

table1 = []
table2 = []

for alpha in alphas:
    file_location_1 = "../results"
    if alpha == -1:
        file_location_1 += "/unconstrained"
    else:
        file_location_1 += "/constrained_" + str(alpha)

    for n in ns:
        file_location_2 = file_location_1 + "/n-" + str(n)

        for delta in deltas:
            file_location_3 = file_location_2 + "_d-" + str(delta)

            for mu in mus:
                file_location_4 = file_location_3 + "_m-" + str(mu)

                for distribution in distributions:
                    file_location_5 = file_location_4 + "_" + distribution

                    # get last line of file
                    with open(file_location_5  + "/log.txt", "r") as f:
                        lines = f.readlines()
                        last_line = lines[-1]
                        last_line = last_line.split(",")

                        # the structure of last_line is:
                        # generation, unique_ind, population_fitness, best_ind_vc_cnt, mean_vc_overlap, std_vc_overlap, avg_node_degree, avg_node_leafes

                        # we extract the following values for table 1:
                        # generation, population_fitness, best_ind_vc_cnt
                        generation = int(last_line[0])
                        population_fitness = round(float(last_line[2]) / (n * (mu**2 - mu)), 4) * 100

                    with open(file_location_5 + "/ilp_min_vc.txt", "r") as f:
                        lines = f.readlines()
                        ilp_min_vc = lines[0]
                        ilp_min_vc = ilp_min_vc.split(",")

                    with open(file_location_5 + "/best_found_vc.txt", "r") as f:
                        lines = f.readlines()
                        best_found_vc = lines[0]
                        best_found_vc = best_found_vc.split(",")

                    vc_ratio = round((len(best_found_vc) - len(ilp_min_vc)) / n * 100, 2)
                    print(n, "m " + str(mu), "d " + str(delta), distribution)
                    print(generation, population_fitness, vc_ratio)
                    print("=====")


