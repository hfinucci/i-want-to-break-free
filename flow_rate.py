import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# flow_rate_dict = {}
# with open("src/main/resources/c/states1.2_200_1.txt", "r") as frame:
#       for line in frame:
#             num = int(float(line))
#             for possible_values in range(0,67):
#                   if (num > possible_values and num < 5 + possible_values):
#                         if flow_rate_dict.get(possible_values) is None:
#                               flow_rate_dict[possible_values] = 0
#                         flow_rate_dict[possible_values] += 1/5
# frame.close()

# print(flow_rate_dict)

# fig, ax = plt.subplots()
# ax.errorbar(list(flow_rate_dict),list(flow_rate_dict.values()), fmt='.', linewidth=2, capsize=6, color= "red")
# plt.ylabel("Partícula")
# plt.xlabel("Tiempo de salida (s)")
# plt.legend()
# plt.show()

flow_rate_array = []
for file_index in range(1,11):
      file_data = []
      with open("src/main/resources/b/states" + str(file_index) + ".txt", "r") as frame:
            for line in frame:
                  if line == "\n":
                        break
                  file_data.append(float(line))
            flow_rate_array.append(file_data)
      frame.close()

data1 = pd.DataFrame(flow_rate_array)
error1 = data1.std()


fig, ax = plt.subplots()
ax.errorbar(data1.mean(axis=0),list(range(1,201)), xerr=error1, fmt='.', label="D=1.2", linewidth=2, capsize=6, color= "#194747")
plt.ylabel("Partícula")
mpl.rcParams['savefig.transparent'] = True
plt.xlabel("Tiempo de salida (s)")
plt.legend()
plt.show()

      