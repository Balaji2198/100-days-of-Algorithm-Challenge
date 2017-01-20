'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Input Format:
A single line of five space-separated integers.

Output Format:
Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)
'''

input_array = map(int, raw_input().split(' '))
maximum = max(input_array)
minimum = min(input_array)
total = sum(input_array)
print total - maximum, total - minimum