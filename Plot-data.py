import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data\Extracted-data\Saccades\Saccades-1.csv')
#split column by comma
# df[['LeftPupilPoints1','LeftPupilPoints2']] = df['LeftPupilPoints'].str.split(',',expand=True)
# df[['RightPupilPoints1','RightPupilPoints2']] = df['RightPupilPoints'].str.split(',',expand=True)
# df['LeftPupilPoints1']=df['LeftPupilPoints1'].astype(float)
# df['LeftPupilPoints2']=df['LeftPupilPoints2'].astype(float)
# df['RightPupilPoints1']=df['RightPupilPoints1'].astype(float)
# df['RightPupilPoints2']=df['RightPupilPoints2'].astype(float)


plt.plot(np.arange(0,df['LeftPupilPoints-X'].shape[0]),df['LeftPupilPoints-X'],color='red')
plt.plot(np.arange(0,df['LeftPupilPoints-Y'].shape[0]),df['LeftPupilPoints-Y'],color='blue')
plt.plot(np.arange(0,df['RightPupilPoints-X'].shape[0]),df['RightPupilPoints-X'],color='green')
plt.plot(np.arange(0,df['RightPupilPoints-Y'].shape[0]),df['RightPupilPoints-Y'],color='yellow')

plt.title('Saccades 1')
plt.legend(['LeftPupilPoints-X','LefttPupilPoints-Y','RightPupilPoints-X','RightPupilPoints-Y'])
plt.show()
