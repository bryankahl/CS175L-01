import matplotlib.pyplot as plt
import numpy as np
#CS 175 L
#Bryan Kahl
#expensePieChart

def main():
    py_list = []
    slice_labels=[]
    file = open('expenses.txt', 'r')
    line = file.readlines()
    for x in line:
        try:
            x = x.strip('\n')
            n = x.split('\t')
            num = int(n[1])
            py_list.append(num)
            slice_labels.append(n[0])
        except ValueError:
            break
    data = np.array(py_list)
    plt.pie(py_list, labels=slice_labels)
    plt.title('Expenses')
    #slice_labels = ['Rent','Gas','Food','Clothing','Car Payment','Misc']
    plt.show()

main()
