import pandas as pd
import math
import re

oui_non = lambda x: "oui" if x is True else "non"

def generate_latex_tabels(data, diviser, langage):
    past_cmpt = 0
    i = 0
    string = ""
    for value in diviser:
        i += 1
        string += r"\begin{table}[H]" + "\n\t" + r"\centering" + "\n\t\t" + r"\begin{tabular}{|"
        ls = "l|" * (value+2)
        string += ls
        string += r"}\hline"
        string += "\n"
        string += generate_tabel_elements(data[past_cmpt:value+past_cmpt])
        string +="\t"
        string += r"\end{tabular}"
        string +="\n"
        string += r"\caption{"
        string +="Resultats des execution en {}, Partie {} \n".format(langage, i)
        string +=r"}"
        string +="\n"
        string += r"\end{table}"
        string += "\n\n"
        past_cmpt += value
    return string

def generate_tabel_elements(data):
    string = ""
    string += "\tn "
    for i in data.index.tolist():
        n = data.loc[i, "m"]
        string += "& ${}$ ".format(constructing_n(n))
    string += r" \\ \hline"

    string += "\n\tT(n)"
    for i in data.index.tolist():
        string += "& ${}$ ".format(data.loc[i, "time_exe"])
    string += r" \\ \hline"

    string += "\n\tresoud"
    for i in data.index.tolist():
        string += "& {} ".format(oui_non(bool(data.loc[i, "value"])))

    string += r" \\ \hline"
    string += "\n"
    return string

def constructing_n(number):
    number = str(number)
    first_digit = number[0]
    second_part = number[1:]
    power = len(number) - 1
    result = first_digit
    if second_part != "":
        match = re.search(r"0+$", second_part[1:3])
        if match == None:
            if power < 2:
                result += second_part[0]
                if second_part[1:3] != "":
                    result += "." + second_part[1:3]
            else:
                result += "." + second_part[:3] + r"*10^" + str(power)
        else:
            match = re.search(r"[1-9]+", second_part[:3])
            if match == None:
                if power < 2:
                    result += "0"
                else:
                    result += r"*10^" + str(power)
            else:
                if power < 2:
                    result += second_part[0]
                    match = re.search(r"0+", second_part[1:3])
                    if second_part[1:3] != "" and match is not None:
                        result += "." + second_part[1:3]
                else:
                    match = re.search(r"([1-9]?0*[1-9]+)", second_part[:3])
                    result += "." + match[0] + r"*10^" + str(power)
    return result


def main():
    file_string = ""

    # reading data
    c_values = pd.read_csv("SAT_C.csv")
    java_values = pd.read_csv("SAT_JAVA.csv")

    file_string += "\n\n\n"

    file_string += "\n\n** JAVA **\n\n"
    file_string += generate_latex_tabels(c_values, (8,7), "C")

    file_string += "\n\n\n** C **\n\n"
    file_string += generate_latex_tabels(java_values, (8,7), "JAVA")

    with open("latexTables.LT", "w") as file:
        file.write(file_string)

if __name__ == '__main__':
    main()
