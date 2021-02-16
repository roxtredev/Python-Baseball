import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, "..")


#print("********************************************************")
#from pathlib import Path
#import os
#print(os.path.dirname(os.path.abspath(__file__)))
#print("**-------------------**")
#print(sys.path)
#print("********************************************************")
#from . import data as d
#from .data import games


from stats import data as d


attendance = d.games.loc[(d.games['type'] == 'info') & (d.games['multi2'] == 'attendance'), ['year', 'multi3']]
attendance.columns = ['year', 'attendance']

attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])

attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')

plt.xlabel('Year')
plt.ylabel('Attendance')

plt.axhline(y=attendance['attendance'].mean(), label='Mean', linestyle='--', color='green')

plt.show()
