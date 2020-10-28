word = str(input("Please enter a word: "))

reversedword = word[::-1]
if reversedword == word:
    print(word+" is a palindrome")
else:
    print(word+" is not a palindrome")



