import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

flow_rate_array = []
with open("src/main/resources/states1.txt", "r") as frame:
        next(frame)
        prev_time = next(frame)
        prev_particles = 200
        for line in frame:
            if line == "\n":
                  try:
                        particle_count = next(frame)
                        current_time = next(frame)
                        if float(current_time) - float(prev_time) > 1.0:
                              prev_time = current_time
                              flow_rate_array.append(prev_particles - int(particle_count))
                              prev_particles = int(particle_count)
                  except Exception as e:
                        print(e)

frame.close()

plt.plot(flow_rate_array, marker='o',linestyle="")
plt.show()