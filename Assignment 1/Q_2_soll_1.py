# Write a python program that accepts a word from  the user and reverse it.

word = (input("Enter the word you want to reverse : "))
lenght = len(word)
print(" And the word after being reversed is  :",end=" ")
for i in range (lenght-1,-1,-1):
    print(word[i],end="")




