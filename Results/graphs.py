import os
import math

import pandas as pd
import seaborn as sns
sns.set_theme(style="darkgrid")

import matplotlib
import matplotlib.pyplot as plt

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)

sorting_names = {
    "SAT": ("SAT", "SAT Resolution/Verification"),
}

best_cases = {
    "verif": lambda x, y: x,
    "resolution": lambda x, y: y,
}

worst_cases = {
    "verif": lambda x, y: x*y,
    "resolution": lambda x, y: math.pow(2, y) + math.pow(2, y)*x*y,
}


def graph_langage(data, type, langage, min_values=500, max_values=512000):
    ax =  sns.lineplot(data=data, x="m", y="time_exe")
    ax.legend(["SAT"])
    ax.set(xlabel='n', ylabel='Temps d\'execution en secondes', title="resultats pour le {}, avec le langage {}".format(sorting_names[type][1], langage))
    plt.tight_layout()
    file_save_path = os.path.join("graphs" ,"{}_{}.png".format(sorting_names[type][0], langage))
    plt.savefig(file_save_path)
    plt.close()


def graph_function(n, list_values):
    best_case_values = [best_cases["verif"](n, value) for value in list_values]
    ax =  sns.lineplot(x=list_values, y=best_case_values)
    ax.legend(["ctm(n, m)"])
    ax.set(xlabel='m', ylabel='nombre d\'iterations', title='Gm SAT Verification')
    plt.tight_layout()
    file_save_path = os.path.join("graphs" ,"ctm_SAT_ver.png")
    plt.savefig(file_save_path)
    plt.close()

    best_case_values = [best_cases["resolution"](n, value) for value in list_values]
    ax =  sns.lineplot(x=list_values, y=best_case_values)
    ax.legend(["ctm(n, m)"])
    ax.set(xlabel='m', ylabel='nombre d\'iterations', title='Gm SAT Verification')
    plt.tight_layout()
    file_save_path = os.path.join("graphs" ,"ctm_SAT_res.png")
    plt.savefig(file_save_path)
    plt.close()

    worst_case_values = [worst_cases["verif"](n, value) for value in list_values]
    ax =  sns.lineplot(x=list_values, y=worst_case_values)
    ax.legend(["ctp(n, m)"])
    ax.set(xlabel='m', ylabel='nombre d\'iterations', title='Gp SAT Resolution')
    plt.tight_layout()
    file_save_path = os.path.join("graphs" ,"ctp_SAT_ver.png")
    plt.savefig(file_save_path)
    plt.close()

    worst_case_values = [worst_cases["resolution"](n, value) for value in list_values]
    ax =  sns.lineplot(x=list_values, y=worst_case_values)
    ax.legend(["ctp(n, m)"])
    ax.set_xlim(175, 200)
    ax.set(xlabel='m', ylabel='nombre d\'iterations', title='Gp SAT Resolution')
    plt.tight_layout()
    file_save_path = os.path.join("graphs" ,"ctp_SAT_res.png")
    plt.savefig(file_save_path)
    plt.close()


def main():

    for sorting_name in sorting_names:
        # reading data
        c_values = pd.read_csv("{}_C.csv".format(sorting_names[sorting_name][0]))
        graph_langage(c_values, sorting_name, "C")

        java_values = pd.read_csv("{}_JAVA.csv".format(sorting_names[sorting_name][0]))
        graph_langage(java_values, sorting_name, "JAVA")

        list_val =  [x//100 for x in c_values["m"].tolist()[:10]]
        graph_function(100, list_val)


if __name__ == '__main__':
    main()
