import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

flow_rate_dict = {}
with open("src/main/resources/c/states1.2_200_1.txt", "r") as frame:
      for line in frame:
            num = int(float(line))
            for possible_values in range(0,67):
                  if (num > possible_values and num < 5 + possible_values):
                        if flow_rate_dict.get(possible_values) is None:
                              flow_rate_dict[possible_values] = 0
                        flow_rate_dict[possible_values] += 1/5
frame.close()

print(flow_rate_dict)

fig, ax = plt.subplots()
ax.errorbar(list(flow_rate_dict),list(flow_rate_dict.values()), fmt='.', linewidth=2, capsize=6, color= "red")
plt.ylabel("Partícula")
plt.xlabel("Tiempo de salida (s)")
plt.legend()
plt.show()
# plt.plot(flow_rate_dict, marker='.',linestyle="")
# plt.show()

# flow_rate_array = []
# with open("src/main/resources/states1.txt", "r") as frame:
#         next(frame)
#         prev_time = next(frame)
#         prev_particles = 200
#         for line in frame:
#             if line == "\n":
#                   try:
#                         particle_count = next(frame)
#                         current_time = next(frame)
#                         if float(current_time) - float(prev_time) > 1.0:
#                               prev_time = current_time
#                               flow_rate_array.append(prev_particles - int(particle_count))
#                               prev_particles = int(particle_count)
#                   except Exception as e:
#                         print(e)

# print(flow_rate_array)



