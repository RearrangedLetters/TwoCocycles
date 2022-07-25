import numpy as np

from Parser import parse_roots


def to_latex_tabular(line=17):
    index = int(line / 17)
    roots = parse_roots(26, "../G/twococycles")
    root = roots[index].root
    number_format = "{:10.7f}"
    q = complex(root[25][0], root[25][1])
    q_str = number_format.format(q)
    q_conj_str = number_format.format(complex(q.real, -q.imag))
    R = np.array([number_format.format(complex(r[0], r[1])) for r in root[:25]])
    R = R.reshape(5, 5)
    table_header = "\\begin{tabular}{lllllll}\n" \
                   "\n& $ 1 $ & $ d $ & $ d^2 $ & $ c $ & $ cd $ & $ cd^2 $ \\\\\\hline\n" \
                   + " $ 1 $ & " + ((q_str + " & ") * 6)[:-2] + " \\\\"
    table_body = ""
    group_element_names = ["$ 1 $", "$ d $", "$ d^2 $", "$ c $", "$ cd $", "$ cd^2 $"]
    for i, row in enumerate(R):
        table_row = q_conj_str
        for j in row:
            table_row = table_row + " & " + "$ " + j + " $"
        table_body = table_body + group_element_names[i + 1] + " & " + table_row + " \\\\ \n"
    table_body = table_body.replace("j", "i")
    table_footer = "\\end{tabular}"
    return table_header + "\n" + table_body + "\n" + table_footer


print(to_latex_tabular())
