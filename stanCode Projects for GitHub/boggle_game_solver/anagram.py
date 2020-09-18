"""
stanCode SC101 Assignment 5 Problem 4
File: anagram.py
Name: Tiffany Lin
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 22

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variables
words = []                    # A list containing all the vocabs in the dictionary
n = 0                         # Counting the number of anagrams found
anagrams = []                 # A list containing all the anagrams found


def main():
    """
    Each of the anagrams of the word input by the user will be found and printed on Console, respectively;
    and the final result, including the total number and all anagrams found, will be shown at the end.
    """
    read_dictionary()
    print(f"Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)")
    while True:
        vocab = str(input('Find anagram for: '))
        if vocab == EXIT:
            break
        else:
            find_anagrams(vocab)


def find_anagrams(s):
    """
    :param s: (str) The vocabulary input by user
    :return: Anagrams found
    """
    global n, anagrams
    # Resets the constant after each search
    n = 0
    anagrams = []

    # Case insensitive
    s = s.lower()

    # Use the index of str to form all possible combinations
    combination = []
    for i in range(len(s)):
        combination.append(i)

    print('Searching...')
    find_anagrams_helper(s, '', combination, [])

    print(f"{n} anagrams: {anagrams}")


def find_anagrams_helper(s, current_s, combination, current_c):
    """
    :param s: (str) The vocabulary input by user
    :param current_s: (str) Saving the combination of word found
    :param combination: A list containing the index of the s to help find anagrams
    :param current_c: A list saving the combination of index formed
    :return: (str) Anagram found
    """
    global anagrams, n

    if len(current_s) == len(s):
        if current_s in words and current_s not in anagrams:
            print(f"Found: {current_s}")
            print('Searching...')

            anagrams.append(current_s)
            n += 1
    else:
        for num in combination:
            if num in current_c:
                pass
            else:
                current_c.append(num)
                x = current_s
                current_s += s[num]
                if has_prefix(current_s):
                    find_anagrams_helper(s, current_s, combination, current_c)

                current_c.pop()
                current_s = x


def has_prefix(sub_s):
    """
    :param sub_s: (str) The anagram in formation
    :return: (bool) Whether there are words that start with sub_s in the dictionary
    """
    global words
    t = 0
    for word in words:
        if word.startswith(sub_s) is True:
            t += 1
    if t > 0:
        return True


def read_dictionary():
    """
    :return: A list containing all the vocabs from the dictionary
    """
    global words
    with open(FILE, 'r') as f:
        for word in f:
            word = word.strip()
            words.append(word)
    return words


if __name__ == '__main__':
    main()
