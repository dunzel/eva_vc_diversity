import os


def get_table():
    ns = [50, 100, 200]
    mus = [2, 16, 32, 64]
    delta = 4  # fixed delta to 4
    dists = ["uniform1", "poisson"]
    alphas = [0.05, 0.5, -1]

    latex_table_3 = ""
    csv_table_3 = "n,mu,alpha,distribution,gen,d_rho,best_rho\n"

    for n in ns:
        latex_table_3 += "\\multirow{4}{*}{" + str(n) + "} "

        for mu in mus:
            latex_table_3 += "& " + str(mu) + " "

            for alpha in alphas:
                for dist in dists:
                    file_loc_base_con = "../../results/constrained_" + str(alpha)
                    file_loc_base_uncon = "../../results/unconstrained"

                    if alpha == -1:
                        file_loc_base_con = file_loc_base_uncon

                    file_loc_exp = file_loc_base_con + "/n-" + str(n) + "_d-" + str(delta) + "_m-" + str(mu) + "_" + dist
                    file_loc_low = file_loc_base_uncon + "/n-" + str(n) + "_d-" + str(0) + "_m-" + str(mu) + "_uniform1"
                    file_loc_upp = file_loc_base_uncon + "/n-" + str(n) + "_d-" + str(n-1) + "_m-" + str(mu) + "_uniform1"

                    with open(file_loc_exp + "/log.txt", "r") as f:
                        lines = f.readlines()
                        last_line = lines[-1]
                        last_line = last_line.split(",")

                        gen = int(last_line[0])
                        d_rho_res = float(last_line[2])

                    with open(file_loc_low + "/log.txt", "r") as f:
                        lines = f.readlines()
                        last_line = lines[-1]
                        last_line = last_line.split(",")
                        d_rho_low = float(last_line[2])

                    with open(file_loc_upp + "/log.txt", "r") as f:
                        lines = f.readlines()
                        last_line = lines[-1]
                        last_line = last_line.split(",")
                        d_rho_upp = float(last_line[2])

                    # linear interpolation
                    d_rho_expected = d_rho_low + (delta / (n - 1)) * (d_rho_upp - d_rho_low)
                    d_rho_ratio = round(d_rho_res / d_rho_expected * 100, 1)

                    with open(file_loc_exp + "/ilp_min_vc.txt", "r") as f:
                        lines = f.readlines()
                        ilp_min_vc = lines[0]
                        ilp_min_vc = ilp_min_vc.split(",")

                    with open(file_loc_exp + "/best_found_vc.txt", "r") as f:
                        lines = f.readlines()
                        best_found_vc = lines[0]
                        best_found_vc = best_found_vc.split(",")

                    best_rho = round(((len(best_found_vc) / len(ilp_min_vc)) - 1) * 100, 1)

                    latex_table_3 += "& " + str(gen) + " & " + str(d_rho_ratio) + " & " + str(best_rho) + " "
                    csv_table_3 += str(n) + "," + str(mu) + "," + str(alpha) + "," + dist + "," + str(gen) + "," + str(d_rho_ratio) + "," + str(best_rho) + "\n"

            latex_table_3 += "\\\\\n"
        latex_table_3 += "\\cline{1-20}\\addlinespace\n"

    with open("table_3_body.tex", "w") as f:
        f.write(latex_table_3)

    with open("table_3_results.csv", "w") as f:
        f.write(csv_table_3)


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    get_table()
