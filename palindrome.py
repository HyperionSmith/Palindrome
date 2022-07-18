"""
palindrome.py
"""

from collections import deque
#Finished product!

#Function that will do what we need. This is setting up the list we will use to store the word in
def is_palindrome(letters):
    #This will give a ValueError if no one enters a string
    if len(letters) < 1:
        raise ValueError("You need to actually enter a string!")

    #The capital letters was messing me up. No capital letters no problem!
    word_holder = deque(letters.lower())

    #We will compare the first and last letter and pop our way to the middle
    while len(word_holder) > 1:
        first = word_holder.popleft()
        last = word_holder.pop()
        #Uncomment the bit below to see how this works
        """
        print(first)
        print(last)
        """
        if first != last:
            print(letters.capitalize())
            print("That's not a palindrome!\n")
            return False

    print(letters.capitalize())
    print("That's a palindrome alright!\n")
    return True


#I have no clue what an empty string is
#letters = input("Enter you word/number/sentance: ")
letters = "AbAcAbA"
is_palindrome(letters)
