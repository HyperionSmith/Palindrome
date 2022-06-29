from collections import deque

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
letters = "a"
is_palindrome(letters)
letters = "bb"
is_palindrome(letters)
letters = "abc"
is_palindrome(letters)
letters = "laval" #Laval near Motreal is actually a very nice place :) Eat at lucille's!
is_palindrome(letters)
letters = "toronto"
is_palindrome(letters)
letters = "Able was I ere I saw Elba"
is_palindrome(letters)
#I know this fella was supposed to go first but he's the ValueError
letters = ""
is_palindrome(letters)

#letters = input("Enter you word/number/sentance: ") #Uncomment me and try me! I'm fun
#is_palindrome(letters)
