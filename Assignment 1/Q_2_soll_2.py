# Q 3. Write a python program to count the number of even and odd numbers from a series of numbers.
given_word = (input("enter the word you want to reverse :")) 
print("And the reversed word is :",end=" ")
reversed_word ="" 
count  = len(given_word)-1
while count >= 0:
    reversed_word = reversed_word + given_word [count]

    count = count-1
print(reversed_word)