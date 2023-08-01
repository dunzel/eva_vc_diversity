import os


def get_table():
    ns = [50, 100, 200]
    mus = [2, 16, 32, 64]
    deltas = [2, 8]
    dists = ["uniform1", "poisson"]
    # fixed alpha to unconstrained case

    latex_table_2 = ""
    csv_table_2 = "n,mu,delta,distribution,mean_vc_overlap,std_vc_overlap,avg_node_degree,avg_node_leaves\n"

    for n in ns:
        latex_table_2 += "\\multirow{4}{*}{" + str(n) + "} "

        for mu in mus:
            latex_table_2 += "& " + str(mu) + " "

            for delta in deltas:
                for dist in dists:
                    file_loc_base = "../../results/unconstrained"
                    file_loc_exp = file_loc_base + "/n-" + str(n) + "_d-" + str(delta) + "_m-" + str(mu) + "_" + dist

                    with open(file_loc_exp + "/log.txt", "r") as f:
                        lines = f.readlines()
                        last_line = lines[-1]
                        last_line = last_line.split(",")

                        mean_vc_overlap = round(float(last_line[-4]), 2)
                        std_vc_overlap = round(float(last_line[-3]), 2)
                        avg_node_degree = round(float(last_line[-2]), 2)
                        avg_node_leaves = round(float(last_line[-1]), 2)

                        # force to 2 decimal places e.g. 0.00
                        mean_vc_overlap = "{:.2f}".format(mean_vc_overlap)
                        std_vc_overlap = "{:.2f}".format(std_vc_overlap)
                        avg_node_degree = "{:.2f}".format(avg_node_degree)
                        avg_node_leaves = "{:.2f}".format(avg_node_leaves)

                    latex_table_2 += "& " + str(mean_vc_overlap) + " & " + str(std_vc_overlap) + " & " + str(avg_node_degree) + " & " + str(avg_node_leaves) + " "
                    csv_table_2 += str(n) + "," + str(mu) + "," + str(delta) + "," + dist + "," + str(mean_vc_overlap) + "," + str(std_vc_overlap) + "," + str(avg_node_degree) + "," + str(avg_node_leaves) + "\n"

            latex_table_2 += "\\\\\n"
        latex_table_2 += "\\cline{1-18}\\addlinespace\n"

    with open("table_2_body.tex", "w") as f:
        f.write(latex_table_2)

    with open("table_2_results.csv", "w") as f:
        f.write(csv_table_2)


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    get_table()
