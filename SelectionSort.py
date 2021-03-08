"""
Name: Dakota Walker
Date: 02/20/21
Class: Algorithms
"""

def SelectionSort(array):
    for i in range(len(array)):

        """ Could also be called minIndex but decided to go with minValue due to how it is used later. """
        minValue = i

        """
        Basically the opposite of the bubble sort in terms of looping where instead of stopping at 1 before the end of
        the last iteration we start i past the the first element in the list.
        """
        for j in range(i+1, len(array)):
            if array[minValue] > array[j]:
                minValue = j
        
        """ 
        Changes the values so that the first element in the array (or the one it is on) is
        now the lowest. Done at the end to hopefully make it more efficient by reducing swaps
        thus reducing memory usage and run time. 
        """
        temp = array[minValue]
        array[minValue] = array[i]
        array[i] = temp
    
    