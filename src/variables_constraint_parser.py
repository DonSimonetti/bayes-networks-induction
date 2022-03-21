import re
import pickle

source_file = open("alarm_variables_constraints.txt", "r")
data = source_file.read()

filtered_data = data \
    .replace("variable ", "").replace("  type discrete ", "").replace("{\n", "= ").replace("}\n", "").replace(";", "") \
    .replace(" ", "")

lines_list = filtered_data.split("\n")

for i in lines_list:
    lines_list[lines_list.index(i)] = re.sub(r"[=][\[][0-5][\]]", "", i).replace("}", "").replace("{", "=")
lines_list.remove("")

variables = {}
for i in lines_list:
    _str = i.split("=")
    _str[1] = _str[1].split(",")
    variables[_str[0]] = _str[1]

output_file = open("variables_constraints.obj","wb")
pickle.dump(variables,output_file)
output_file.close()

input_file = open("variables_constraints.obj","rb")
data = pickle.load(input_file)
input_file.close()

assert (data == variables)
