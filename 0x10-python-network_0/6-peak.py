#!/usr/bin/python3
""" Find peak value of a list """

def find_peak(list_of_integers):
    """
        Usage: Find the peak value of a list
        Attributes:
            list_of_integers: A list of integers
        Return: peak value
    """
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
