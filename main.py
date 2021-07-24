# This file contains selection, insert, bubble, merge, and
# quick sorts, and a function to generate a random list of
# size quantity with numbers ranging from 0 to quantity
from random import seed
from random import randint


# Random list generator, with arg quantity
def random_list(quantity: int) -> int:
    seed()
    rand_list = []

    for item in range(0, quantity):
        rand_list.append(randint(0, quantity*2))
    return rand_list

# Selection Sort
def selection_sort(sort_me):
  length = len(sort_me)
  for item in range(length):
    min_index = item
    for index in range(item+1, length):
        if sort_me[index] < sort_me[min_index]:
          min_index = index
    sort_me[item], sort_me[min_index] = sort_me[min_index], sort_me[item]

# Insertion Sort
def insertion_sort(sort_me, length):
  if length <= 1:
    return
  
  insertion_sort(sort_me,length-1)
  last = sort_me[length-1]
  j = length - 2
  while (j >= 0 and sort_me[j]>last):
    sort_me[j+1] = sort_me[j]
    j -= 1
  sort_me[j+1] = last

# Bubble Swap
def bubble_sort(sort_me):
  for item in sort_me:
    for index in range(len(sort_me)-1):
      if sort_me[index] > sort_me[index+1]:
        sort_me[index], sort_me[index+1] =sort_me[index+1], sort_me[index]  
  



test_list = random_list(20)
print("Original list: \n", test_list)

selection_sort(test_list)
print("Selection Sort: \n", test_list)

test_list = random_list(25)
print("Original list(insertion sort): \n", test_list)

insertion_sort(test_list,len(test_list))
print("Insertion sort: \n", test_list)

test_list = random_list(20)
print("Original list(Bubble sort): \n", test_list)

bubble_sort(test_list)
print("Bubble sort: \n", test_list)

