import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
import csv


ifile  = open('file_directory', "rb")   # reads a column of data from directed path
reader = csv.reader(ifile,delimiter=',')    # column separator (could be others ; :)

header = reader.next()                  # read first row as title
column = header.index("column_title")   # input column

x = []               # This loop is to remove any unwanted elements
for row in reader:
    col = row[column]
    x.append(col)
nan = 'str_to_remove'
y0 = [i for i in x if nan not in i]


y = list(map(float, y0))    # convert list to float

print('y:', y)              # data details
print('#_elements', len(y0))
max_value = max((y))
min_value = min((y))
num_bins =  20              # numbers of bin decide accuracy of distrubution


print('max_value:', max_value)
print('min_value:', min_value)
print('num_bins:', num_bins)

n,bins,patches = plt.hist(y, num_bins, facecolor='blue', label= 'data_label')
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.legend()
plt.show()