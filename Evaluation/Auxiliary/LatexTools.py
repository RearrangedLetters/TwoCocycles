import numpy as np

from Parser import parse_roots, twococycle_from_root

number_format = "{:1.5f}"


def matrix_to_latex_tablebody(row_labels, M):
    body = ""
    for i, r in enumerate(M):
        row = ""
        for j in r:
            entry = complex(j[0], j[3])
            row = row + " & $" + number_format.format(entry).replace("j", "i") + "$"
        body = body + "\t" + row_labels[i] + row + "\\\\\n"
    return body.replace("  ", " ")


def to_latex_tabular(line=33):
    index = int(line / 17)
    twococycle = twococycle_from_root(parse_roots(26, "../G/twococycles")[index])
    table_header = "\\begin{tabular}{rcccccc}" \
                   "\n\t& $1$ & $d$ & $d^2$ & $c$ & $cd$ & $cd^2$ \\\\\\hline\n"
    group_element_names = ["$1$", "$d$", "$d^2$", "$c$", "$cd$", "$cd^2$"]
    table_body = matrix_to_latex_tablebody(group_element_names, twococycle.mapping)
    table_footer = "\\end{tabular}"
    return table_header + table_body + table_footer


print(to_latex_tabular())
