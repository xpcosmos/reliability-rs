import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DATA_PATH = "exercices/data/chapter 4/q1.csv"

# %% Read Data
data = pd.read_csv(DATA_PATH)

# %% Duane Metrics

data["duane_plot"] = data["i"] / data["t_i"]

for i in ["duane_plot", "t_i"]:
    data["log_" + i] = np.log(data[i])

data.plot(y="log_duane_plot", x="log_t_i", kind="scatter")
plt.ylim((-8, -5.5))
plt.show()