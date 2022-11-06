#write a program to display unique vowels present in the given word.
vowels=["a", "e", "i", "o", "u"]
word=input("Enter the word to search for vowels")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print("The number of vowels is",len(found))            