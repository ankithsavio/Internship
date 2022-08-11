import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data\Extracted-data\Saccades\Saccades-1.csv')

plt.plot(np.arange(0,df['LeftPupilPoints-X'].shape[0]),df['LeftPupilPoints-X'],color='red')
plt.plot(np.arange(0,df['LeftPupilPoints-Y'].shape[0]),df['LeftPupilPoints-Y'],color='blue')
plt.plot(np.arange(0,df['RightPupilPoints-X'].shape[0]),df['RightPupilPoints-X'],color='green')
plt.plot(np.arange(0,df['RightPupilPoints-Y'].shape[0]),df['RightPupilPoints-Y'],color='yellow')

plt.title('Saccades 1')
plt.legend(['LeftPupilPoints-X','LefttPupilPoints-Y','RightPupilPoints-X','RightPupilPoints-Y'])
plt.show()
