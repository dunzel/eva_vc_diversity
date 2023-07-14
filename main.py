from eva_algos.mu_plus_one_ea_custom import mu_plus_one_ea


if __name__ == "__main__":
    # set the random seed
    # # n, delta, mu, alpha
    # ns = [50, 100, 200, 400]
    # deltas = [2, 4, 8]
    # mus = [2, 10, 25, 50]
    # distributions = ["uniform1", "uniform2", "uniform3", "poisson"]
    # alphas = [None, 0.05, 0.1, 0.5]  # !!! set POPULATION_GENERATOR to heuristic !!!
    #
    # for n in ns:
    #     for delta in deltas:
    #         for mu in mus:
    #             for distribution in distributions:
    #                 for alpha in alphas:
    #                     pass

    mu_plus_one_ea()
