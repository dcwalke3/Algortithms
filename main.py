"""
Name: Dakota Walker
Date: 02/23/21
Class: Algorithms
"""

import random, copy

from SelectionSort import SelectionSort
from BubbleSort import BubbleSort
from InsertionSort import InsertionSort
from Timer import Timer
from ConsoleClear import ConsoleClear


""" 

Hey Brandon left you a message in Timer.py if you are free to read it
Also reuploaded file just to say this.

"""

def main():
    ConsoleClear()
    while(True):
        
        """ 'data' is a dictonary just cause I prefer a dictonary with mutliple arrays in it verses having to do nested arrays."""
        data = {}

        listNum = input("Enter the number of list to sort: ")
        
        """ Validating if everything is numeric."""
        while(listNum.isnumeric() == False):
            ConsoleClear()
            print("Please make sure your input is numeric.")
            listNum = input("Enter the number of list to sort: ")
        
        listSize = input("Enter the Size of the List: ")

        while(listNum.isnumeric() == False):
            ConsoleClear()
            print("Please make sure your input is numeric.")
            print("Enter the number of list to sort: " + listNum)
            listNum = input("Enter the number of list to sort: ")

        """ Creates a list for each list desired. Adds each to a dictonary."""
        for i in range(int(listNum)):
            tempArray = []
            for j in range(int(listSize)):
                tempArray.append(random.randint(1, 100))
            data[i] = tempArray

        
        
        print("Begin Sorting...\n")

        """ Timer activates than the algorithm will go through each key(array) in the dictonary and make a deepcopy of it for use. """
        with Timer(True):  
            for key in data:
                dataCopy = copy.deepcopy(data[key])
                BubbleSort(dataCopy)
        print("Bubble Sort Complete\n\n")

   
        with Timer(True):
            for key in data:
                dataCopy = copy.deepcopy(data[key])
                SelectionSort(dataCopy)
                
        print("Selection Sort Complete\n\n")


        
        with Timer(True):
            for key in data:
                dataCopy = copy.deepcopy(data[key])
                InsertionSort(dataCopy)
        print("Insertion Sort Complete\n\n")

        option = input("Enter 'Q' to quit or any other key to continue: ").upper()
    
main()