import sys
import os
from shutil import copyfile

path=sys.argv[1]
new_file_place=sys.argv[2]


arr=os.listdir(path)
#print(arr) # works      #prints all files in array

exp_num=[]
counter=0
for x in arr:
    lit=x.split('_') #split after first _
    actual_number=lit[1] #put the number
    exp_num.append(actual_number)
    counter=counter+1


#arr2 = list(set(exp_num))   #makes list of all numbers
#print(arr2)

for x in arr:
    lit=x.split('_') #split after first _
    actual_number=lit[1]
    directory = new_file_place + "/" + actual_number
    if not os.path.exists(directory):
        os.makedirs(directory)
        copyfile(path + "/"+ x, directory + "/" + x)
        #copy file over
    else:
        copyfile(path + "/"+ x, directory + "/" + x)
        #copy file to directory
