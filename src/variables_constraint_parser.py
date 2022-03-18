import re

source_file = open("alarm_variables_constraints.txt", "r")
data = source_file.read()

filtered_data = data \
    .replace("variable ", "").replace("  type discrete ", "").replace("{\n", "= ").replace("}\n", "").replace(";", "") \
    .replace(" ", "")

lines_list = filtered_data.split("\n")

for i in lines_list:
    lines_list[lines_list.index(i)] = re.sub(r"[=][\[][0-5][\]]", "", i).replace("}", "").replace("{", "=")

print(lines_list)
