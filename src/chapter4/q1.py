# Question 1 for Duane Plots, Chapter 4
import matplotlib.pyplot as plt
from src.entity.duane_plot import PlotEntity

DATA_PATH_Q1A = 'data/chapter4/execises/q1a.csv'
DATA_PATH_Q1B = 'data/chapter4/execises/q1b.csv'
DATA_PATH_Q1C = 'data/chapter4/execises/q1c.csv'
DATA_PATH_Q1D = 'data/chapter4/execises/q1d.csv'

q1a = PlotEntity(DATA_PATH_Q1A, 'System #1')
q1b = PlotEntity(DATA_PATH_Q1B, 'System #2')
q1c = PlotEntity(DATA_PATH_Q1C, 'System #3')
q1d = PlotEntity(DATA_PATH_Q1D, 'System #5')

fig, axes = plt.subplots(2,2,sharex=True)

q1a.plot(axes[0,0])
q1b.plot(axes[0,1])
q1c.plot(axes[1,0])
q1d.plot(axes[1,1])

plt.subplots_adjust(wspace=0.4)
plt.suptitle('Question 1 -> Duane plots')
plt.savefig('data/chapter4/figs/Figure_1.png')
plt.show()
