import numpy as np
import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt

########################  D = 1.2  ########################
flow_rate_array = []
for file_index in range(1,4):
      file_data = []
      with open("src/main/resources/c/states1.2_200_" + str(file_index) + ".txt", "r") as frame:
            for line in frame:
                  if line == "\n":
                        break
                  file_data.append(float(line))
            flow_rate_array.append(file_data)
      frame.close()

data1 = pd.DataFrame(flow_rate_array)
error1 = data1.std()
########################  D = 1.8  ########################
flow_rate_array = []
for file_index in range(1,4):
      file_data = []
      with open("src/main/resources/c/states1.8_260_" + str(file_index) + ".txt", "r") as frame:
            for line in frame:
                  if line == "\n":
                        break
                  file_data.append(float(line))
            flow_rate_array.append(file_data)
      frame.close()

data2 = pd.DataFrame(flow_rate_array)
error2 = data2.std()

########################  D = 2.4  ########################
flow_rate_array = []
for file_index in range(1,4):
      file_data = []
      with open("src/main/resources/c/states2.4_320_" + str(file_index) + ".txt", "r") as frame:
            for line in frame:
                  if line == "\n":
                        break
                  file_data.append(float(line))
            flow_rate_array.append(file_data)
      frame.close()

data3 = pd.DataFrame(flow_rate_array)
error3 = data3.std()

########################  D = 3.0  ########################
flow_rate_array = []
for file_index in range(1,4):
      file_data = []
      with open("src/main/resources/c/states3.0_380_" + str(file_index) + ".txt", "r") as frame:
            for line in frame:
                  if line == "\n":
                        break
                  file_data.append(float(line))
            flow_rate_array.append(file_data)
      frame.close()

data4 = pd.DataFrame(flow_rate_array)
error4 = data4.std()

# fig, ax = plt.subplots()
# ax.errorbar(data1.mean(axis=0),list(range(1,201)), xerr=error1, fmt='.', label="D=1.2 - N=200", linewidth=2, capsize=6, color= "red")
# ax.errorbar(data2.mean(axis=0),list(range(1,261)), xerr=error2, fmt='.', label="D=1.8 - N=260",linewidth=2, capsize=6, color= "blue")
# ax.errorbar(data3.mean(axis=0),list(range(1,321)), xerr=error3, fmt='.', label="D=2.4 - N=320",linewidth=2, capsize=6, color= "yellow")
# ax.errorbar(data4.mean(axis=0),list(range(1,381)), xerr=error4, fmt='.', label="D=3.0 - N=380",linewidth=2, capsize=6, color= "green")

# ax.errorbar(data1.mean(axis=0),list(range(1,201)), fmt='.', label="D=1.2 - N=200", linewidth=2, capsize=6, color= "red")
# ax.errorbar(data2.mean(axis=0),list(range(1,261)), fmt='.', label="D=1.8 - N=260",linewidth=2, capsize=6, color= "blue")
# ax.errorbar(data3.mean(axis=0),list(range(1,321)), fmt='.', label="D=2.4 - N=320",linewidth=2, capsize=6, color= "yellow")
# ax.errorbar(data4.mean(axis=0),list(range(1,381)), fmt='.', label="D=3.0 - N=380",linewidth=2, capsize=6, color= "green")

# ax.errorbar(flo,list(range(1,201)), fmt='.', label="D=3.0 - N=380",linewidth=2, capsize=6, color= "green")

# plt.ylabel("Partícula")
# plt.xlabel("Tiempo de salida (s)")
# plt.legend()
# plt.show()

################################  Beyond the spider verse ################################

flow_rate_dict = {}
for num in data1.mean(axis=0):
    for possible_values in range(0,67):
            if (num > possible_values and num < 5 + possible_values):
                if flow_rate_dict.get(possible_values) is None:
                        flow_rate_dict[possible_values] = 0
                flow_rate_dict[possible_values] += 1/5

print(flow_rate_dict)

fig, ax = plt.subplots()
ax.errorbar(list(flow_rate_dict),list(flow_rate_dict.values()), fmt='.', linewidth=2, capsize=6, color= "red")
plt.ylabel("Partícula")
plt.xlabel("Tiempo de salida (s)")
plt.legend()
plt.show()


