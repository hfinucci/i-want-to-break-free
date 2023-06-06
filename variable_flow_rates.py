import numpy as np
import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset

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
# ax.errorbar(data1.mean(axis=0),list(range(1,201)), xerr=error1, fmt='.', label="D=1.2", linewidth=2, capsize=6, color= "#194747")
# ax.errorbar(data2.mean(axis=0),list(range(1,261)), xerr=error2, fmt='.', label="D=1.8",linewidth=2, capsize=6, color= "#6d3210")
# ax.errorbar(data3.mean(axis=0),list(range(1,321)), xerr=error3, fmt='.', label="D=2.4",linewidth=2, capsize=6, color= "#7cc8da")
# ax.errorbar(data4.mean(axis=0),list(range(1,381)), xerr=error4, fmt='.', label="D=3.0",linewidth=2, capsize=6, color= "#c3ae7f")
# mpl.rcParams['savefig.transparent'] = True
# ax.errorbar(data1.mean(axis=0),list(range(1,201)), fmt='.', label="D=1.2 - N=200", linewidth=2, capsize=6, color= "red")
# ax.errorbar(data2.mean(axis=0),list(range(1,261)), fmt='.', label="D=1.8 - N=260",linewidth=2, capsize=6, color= "blue")
# ax.errorbar(data3.mean(axis=0),list(range(1,321)), fmt='.', label="D=2.4 - N=320",linewidth=2, capsize=6, color= "yellow")
# ax.errorbar(data4.mean(axis=0),list(range(1,381)), fmt='.', label="D=3.0 - N=380",linewidth=2, capsize=6, color= "green")
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


flow_rate_dict2 = {}
for num in data2.mean(axis=0):
    for possible_values in range(0,67):
            if (num > possible_values and num < 5 + possible_values):
                if flow_rate_dict2.get(possible_values) is None:
                        flow_rate_dict2[possible_values] = 0
                flow_rate_dict2[possible_values] += 1/5

flow_rate_dict3 = {}
for num in data3.mean(axis=0):
    for possible_values in range(0,67):
            if (num > possible_values and num < 5 + possible_values):
                if flow_rate_dict3.get(possible_values) is None:
                        flow_rate_dict3[possible_values] = 0
                flow_rate_dict3[possible_values] += 1/5

flow_rate_dict4 = {}
for num in data4.mean(axis=0):
    for possible_values in range(0,67):
            if (num > possible_values and num < 5 + possible_values):
                if flow_rate_dict4.get(possible_values) is None:
                        flow_rate_dict4[possible_values] = 0
                flow_rate_dict4[possible_values] += 1/5


# fig, ax = plt.subplots()
# ax.errorbar(list(flow_rate_dict),list(flow_rate_dict.values()), fmt='.', label="D=1.2", linewidth=2, capsize=6, color= "#194747")
# ax.errorbar(list(flow_rate_dict2),list(flow_rate_dict2.values()), fmt='.', label="D=1.8", linewidth=2, capsize=6, color= "#6d3210")
# ax.errorbar(list(flow_rate_dict3),list(flow_rate_dict3.values()), fmt='.', label="D=2.4", linewidth=2, capsize=6, color= "#7cc8da")
# ax.errorbar(list(flow_rate_dict4),list(flow_rate_dict4.values()), fmt='.', label="D=3.0", linewidth=2, capsize=6, color= "#c3ae7f")
# plt.ylabel("Q (1/m/s)")
# plt.xlabel("Tiempo (s)")
# plt.legend()
# mpl.rcParams['savefig.transparent'] = True
# plt.show()


flow_rate_dict = {k: v for k, v in flow_rate_dict.items() if k >= 15 and k <= 40}
flow_rate_dict2 = {k: v for k, v in flow_rate_dict2.items() if k >= 15 and k <= 40}
flow_rate_dict3 = {k: v for k, v in flow_rate_dict3.items() if k >= 15 and k <= 40}
flow_rate_dict4 = {k: v for k, v in flow_rate_dict4.items() if k >= 15 and k <= 40}


arr1 = np.array(list(flow_rate_dict.values()))
arr2 = np.array(list(flow_rate_dict2.values()))
arr3 = np.array(list(flow_rate_dict3.values()))
arr4 = np.array(list(flow_rate_dict4.values()))


fig, ax = plt.subplots()
# ax.errorbar(x=[1.2,1.8,2.4,3.0],y=[arr1.mean(), arr2.mean(), arr3.mean(), arr4.mean()], yerr=[arr1.std(), arr2.std(), arr3.std(), arr4.std()], fmt='.', linewidth=2, capsize=6, color= "#7cc8da")
# plt.ylabel("Q (1/m/s)")
# plt.xlabel("Ancho de la puerta (m)")
# mpl.rcParams['savefig.transparent'] = True
# plt.show()

x = np.array([1.2,1.8,2.4,3.0]).reshape((-1, 1))
y = np.array([arr1.mean(), arr2.mean(), arr3.mean(), arr4.mean()])

reg = LinearRegression().fit(x,y)

# plt.scatter(x, y,color='g')
plt.plot(x, reg.predict(x), color='#c3ae7f', label="Regresión Lineal")
ax.errorbar(x=[1.2,1.8,2.4,3.0],y=[arr1.mean(), arr2.mean(), arr3.mean(), arr4.mean()], yerr=[arr1.std(), arr2.std(), arr3.std(), arr4.std()], fmt='.', linewidth=2, capsize=6, color= "#7cc8da")
plt.ylabel("Q (1/m/s)")
plt.xlabel("Ancho de la puerta (m)")
plt.legend()
mpl.rcParams['savefig.transparent'] = True


plt.show()
plt.show()
print(reg.score(x,y))

