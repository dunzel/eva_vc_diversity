# load the template.sh file
# and replace in the file the values {n}, {delta}, {mu}, {distribution}, {alpha} by corresponding variables

# n, delta, mu, distributions, alpha
ns = [200]  # 200, 400
deltas = [2, 4, 8]
mus = [2, 16, 32]  # 64
distributions = ["uniform1", "poisson"]  # "uniform2", "uniform3"
alphas = [-1, 0.05, 0.5]  # 0.1

for n in ns:
    for delta in deltas:
        for mu in mus:
            for distribution in distributions:
                for alpha in alphas:
                    with open("template.sh", "r") as f:
                        template = f.read()
                        template = template.replace("{n}", str(n))
                        template = template.replace("{delta}", str(delta))
                        template = template.replace("{mu}", str(mu))
                        template = template.replace("{distribution}", str(distribution))
                        template = template.replace("{alpha}", str(alpha))
                        # create this new file first and save then the edited template in it
                        with open(f"./first_runs/{n}_{delta}_{mu}_{distribution}_{alpha}.sh", "w") as f:
                            f.write(template)