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

fig, ax = plt.subplots()
ax.errorbar(data1.mean(axis=0),list(range(1,201)), xerr=error1, fmt='.', label="d=1.2", linewidth=2, capsize=6, color= "#194747")
ax.errorbar(data2.mean(axis=0),list(range(1,261)), xerr=error2, fmt='.', label="d=1.8",linewidth=2, capsize=6, color= "#6d3210")
ax.errorbar(data3.mean(axis=0),list(range(1,321)), xerr=error3, fmt='.', label="d=2.4",linewidth=2, capsize=6, color= "#7cc8da")
ax.errorbar(data4.mean(axis=0),list(range(1,381)), xerr=error4, fmt='.', label="d=3.0",linewidth=2, capsize=6, color= "#c3ae7f")
mpl.rcParams['savefig.transparent'] = True
plt.ylabel("Cantidad de partículas salientes")

plt.xlabel("Tiempo de salida (s)")
plt.legend()
plt.show()

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


fig, ax = plt.subplots()
ax.errorbar(list(flow_rate_dict),list(flow_rate_dict.values()), fmt='.', label="d=1.2", linewidth=2, capsize=6, color= "#194747")
ax.errorbar(list(flow_rate_dict2),list(flow_rate_dict2.values()), fmt='.', label="d=1.8", linewidth=2, capsize=6, color= "#6d3210")
ax.errorbar(list(flow_rate_dict3),list(flow_rate_dict3.values()), fmt='.', label="d=2.4", linewidth=2, capsize=6, color= "#7cc8da")
ax.errorbar(list(flow_rate_dict4),list(flow_rate_dict4.values()), fmt='.', label="d=3.0", linewidth=2, capsize=6, color= "#c3ae7f")
plt.ylabel("Q (1/m/s)")
plt.xlabel("Tiempo (s)")
plt.legend()
mpl.rcParams['savefig.transparent'] = True
plt.show()


flow_rate_dict = {k: v for k, v in flow_rate_dict.items() if k >= 15 and k <= 40}
flow_rate_dict2 = {k: v for k, v in flow_rate_dict2.items() if k >= 15 and k <= 40}
flow_rate_dict3 = {k: v for k, v in flow_rate_dict3.items() if k >= 15 and k <= 40}
flow_rate_dict4 = {k: v for k, v in flow_rate_dict4.items() if k >= 15 and k <= 40}


arr1 = np.array(list(flow_rate_dict.values()))
arr2 = np.array(list(flow_rate_dict2.values()))
arr3 = np.array(list(flow_rate_dict3.values()))
arr4 = np.array(list(flow_rate_dict4.values()))


# fig, ax = plt.subplots()
# ax.errorbar(x=[1.2,1.8,2.4,3.0],y=[arr1.mean(), arr2.mean(), arr3.mean(), arr4.mean()], yerr=[arr1.std(), arr2.std(), arr3.std(), arr4.std()], fmt='.', linewidth=2, capsize=6, color= "#7cc8da")
# plt.ylabel("Q (1/m/s)")
# plt.xlabel("Ancho de la puerta (m)")
# mpl.rcParams['savefig.transparent'] = True
# plt.show()

# reg = LinearRegression().fit(x,y)

# plt.scatter(x, y,color='g')
# plt.plot(x, reg.predict(x), color='#c3ae7f', label="Regresión Lineal")
# ax.errorbar(x=[1.2,1.8,2.4,3.0],y=[arr1.mean(), arr2.mean(), arr3.mean(), arr4.mean()], yerr=[arr1.std(), arr2.std(), arr3.std(), arr4.std()], fmt='.', linewidth=2, capsize=6, color= "#7cc8da")
# plt.ylabel("Q (1/m/s)")
# plt.xlabel("Ancho de la puerta (m)")
# plt.legend()
# mpl.rcParams['savefig.transparent'] = True

# plt.show()
# plt.show()
# print(reg.score(x,y))


# Datos de la simulación
y = np.array([1.2,1.8,2.4,3.0])
x = np.array([arr1.mean(), arr2.mean(), arr3.mean(), arr4.mean()])

# Función para calcular el error cuadrático medio
def calcular_error(y_real, y_pred):
    return np.sum((y_real - y_pred) ** 2)

n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
mean_x = np.mean(x)
mean_y = np.mean(y)
sum_x_squared = np.sum(x ** 2)

m = (sum_xy - n * mean_x * mean_y) / (sum_x_squared - (1/n) * (sum_x)**2)
# Ordenada al origen
b = (sum_y - m * sum_x) / n

# Mostrando la curva de error en función del parámetro de ajuste
parametros = np.linspace(-1, 5, 50000)  # Rango de valores para el parámetro de ajuste
errores = []
parametros_arr = []

for parametro in parametros:
    y_pred = parametro * x + b
    error = calcular_error(y, y_pred)
    parametros_arr.append(parametro)
    errores.append(error)

correct_index = errores.index(np.min(errores))

plt.plot(parametros, errores, color="#194747")
plt.scatter(parametros[errores.index(np.min(errores))], np.min(errores), color="#6d3210")
plt.xlabel('Parámetro de ajuste')
plt.ylabel('Error cuadrático medio')
plt.show()

# Mostrando la recta de regresión y los datos de la simulación
# plt.scatter(y, x, color='red')
plt.errorbar(x=[1.2,1.8,2.4,3.0],y=[arr1.mean(), arr2.mean(), arr3.mean(), arr4.mean()], yerr=[arr1.std(), arr2.std(), arr3.std(), arr4.std()], fmt='.', linewidth=2, capsize=6, color= "#7cc8da")

plt.plot(parametros_arr[correct_index-500] * x + b, x, color='#c3ae7f', linestyle='dashed', label='Líneas de regresión no optimizada')
plt.plot(parametros_arr[correct_index-250] * x + b, x, color='#c3ae7f', linestyle='dashed')
plt.plot(parametros_arr[correct_index] * x + b, x, color='#6d3210', label='Línea de regresión de menor error')
plt.plot(parametros_arr[correct_index+250] * x + b, x, color='#c3ae7f', linestyle='dashed')
plt.plot(parametros_arr[correct_index+500] * x + b, x, color='#c3ae7f', linestyle='dashed')
plt.ylabel("Q (1/m/s)")
plt.xlabel("Ancho de la puerta (m)")
plt.legend()
mpl.rcParams['savefig.transparent'] = True
plt.show()




# x = np.array([1.2,1.8,2.4,3.0])
# y = np.array([arr1.mean(), arr2.mean(), arr3.mean(), arr4.mean()])

# # Rango de valores para la pendiente
# slope_range = np.linspace(-1, 5, 500)

# # Calcula el error cuadrático medio (MSE) para cada pendiente en el rango
# mse_values = []
# for slope in slope_range:
#     y_pred = slope * x + (np.mean(y) - slope * np.mean(x))
#     mse = np.mean((y - y_pred)**2)
#     mse_values.append(mse)

# # Encuentra la pendiente que minimiza el error (MSE)
# best_slope = slope_range[np.argmin(mse_values)]
# best_intercept = np.mean(y) - best_slope * np.mean(x)

# # Calcula los valores predichos de y utilizando la mejor pendiente e intercepto
# y_pred = best_slope * x + best_intercept

# # Graficar los datos y la mejor línea de ajuste
# plt.figure(figsize=(10, 4))
# plt.subplot(1, 2, 1)
# plt.scatter(x, y)
# plt.plot(x, y_pred, color='red')
# plt.ylabel("Q medio (partuculas/s)", fontsize=14)
# plt.xlabel("Ancho de la puerta (m)", fontsize=14)
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)

# # Graficar la curva del error
# plt.subplot(1, 2, 2)
# plt.plot(slope_range, mse_values)
# plt.scatter(best_slope, np.min(mse_values), color='red')
# plt.xlabel('Pendiente', fontsize=14)
# plt.ylabel('Error cuadrático medio (MSE)', fontsize=14)
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)

# plt.tight_layout()
# plt.show()

# # Imprimir la pendiente y el error
# print("Pendiente (slope):", best_slope)
# print("Error cuadrático medio (MSE):", np.min(mse_values))


