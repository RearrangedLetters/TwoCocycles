import numpy as np

from Evaluation.Auxiliary.Parser import parse_two_cocycles
from Evaluation.G.G import G
from Evaluation.QStar import omega, Q_star
from src.NumericalBase import NumericalBase


def mapping_to_latex_tablebody(base, row_labels, mapping, decimal_places=3):
    body = ""
    number_format = "{:1." + str(decimal_places) + "f}"
    for i, r in enumerate(mapping):
        row = ""
        for j, c in enumerate(r):
            row = row + "&" + number_format\
                .format(base.evaluate(mapping[i][j]))\
                .replace("j", "i")
        body = body + "\t" + row_labels[i] + row + "\\\\\n"
    return body


def to_latex_tabular(group, base, i, element_names, decimal_places=3, file="two_cocycles"):
    two_cocycle = parse_two_cocycles(group, base.base, file)[i]
    table_header = "\\begin{tabular}{rcccccc}" \
                   "\n\t& $1$ & $d$ & $d^2$ & $c$ & $cd$ & $cd^2$ \\\\\\hline\n"
    table_body = mapping_to_latex_tablebody(base, element_names, two_cocycle.mapping, decimal_places)
    table_footer = "\\end{tabular}"
    return table_header + table_body + table_footer


group_element_names = ["$1$", "$d$", "$d^2$", "$c$", "$cd$", "$cd^2$"]
print(to_latex_tabular(G, NumericalBase(Q_star.base), 2, group_element_names, decimal_places=3, file="../G/two_cocycles"))
