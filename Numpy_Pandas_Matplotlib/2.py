import csv
import numpy as np
import pandas
import matplotlib
#with open('A:/Periodical 1/CGHS_dispensary_list_1.csv') as f:
 #   reader = csv.DictReader(f)
    #print(reader)
    
#csv = np.genfromtxt('CGHS_dispensary_list_1.csv', delimiter="'")

f = pandas.read_csv("CGHS_dispensary_list_1.csv")
#print(len(f))
print("The number of wellness centers with a doctor count > 5 is:")
print(len(f[f.doctorCount>5]))
