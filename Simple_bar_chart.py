
#Write a Python Program to plot a simple bar chart

import pandas as pd
import matplotlib.pyplot as plt

data = [['E001','M',34,123,'Normal',350],
        ['E002','F',40,114,'Overweight',450],
        ['E003','F',37,135,'Obesity',69],
        ['E004','M',30,139,'Underweight',189]]

df= pd.DataFrame(data,columns =['EMPID','Gender','Age','Sales','BMI','Income'])

plt.bar(df['Age'],df['Sales'])
plt.xlabel('Age')
plt.ylabel('Sales')
plt.show()
