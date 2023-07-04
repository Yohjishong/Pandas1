import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
num = np.arange(5, 10, 0.5)
print(num)
df = pd.read_excel('team.xlsx')
df['one'] = 1
df['Q1'].plot()
