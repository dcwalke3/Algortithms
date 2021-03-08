"""
Name: Dakota Walker
Date: 02/23/21
Class: Algorithms
"""

import random

def InsertionSort(array):

    """  Did 1 instead of 0 so I could say i-1 easily versuses having to do +1 in a lot more spots. """
    for i in range(1, len(array)):

        lowestValue = array[i]

        """  
        'j' is the counter. Ignore the joke in comments below if you don't want to read it.

        'j'. The nested looping variable forever since nested looping began(IDK on that).
        Never forget to include your secondary best friend 'j'.
        Even when no nested for loop is present. Also, thank you for taking your time
        to read my stupid joke.
        """
        
        j = i-1


        """ 
        Basically loops through array until the current index is less than first index. It then switches them. 
        This is better than bubble sort because you are forgoing redundant swaps and iterations when they are 
        not needed. 
        """
        while(j >= 0 and array[j] > lowestValue):
            array[j+1] = array[j]
            j-=1
        
        """ Changes the previous lowest value to current lowest value. """
        array[j+1] = lowestValue
    

        