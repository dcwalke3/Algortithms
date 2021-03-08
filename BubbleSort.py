"""
Assignment: Bubble-Sort Algorithm
Name: Dakota Walker
Class: Algorithms
Date: 2021/02/04
"""

import random
def BubbleSort(array):
   
    #Loops through array
    for i in range((len(array))-1):
        
        #Basically says go through until right before where you stopped last time.
        for j in range((len(array))-i-1):
            
            """
            Compare the two numbers.
            Make sure you keep is sortArray[j] instead of sortArray[i]. That is what caused it to not work.
            It will still say proper comparisons where at 20 numbers compareCount=190, but it will say like 14 swaps
            and only last two nums will be right.
            """

            if (array[j]>array[j+1]):
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp    

