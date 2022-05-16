# Q 3. Write a python program to count the number of even and odd numbers from a series of numbers.
given_num = [22,67,87,98,99,65,88,66,44,22,33]
count_even = 0
count_odd = 0
for i in given_num:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Total even numbers in given_data are ;",count_even,"And ""total odd numbers in given_data are",count_odd)







