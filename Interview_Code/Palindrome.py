import re
import sys

# Used to get the word list file from command line
# Example command: 'python Palindrome.py test_words.txt'
input_file = sys.argv[1]


def palindrome(word):
    """
    Checks if word is a palindrome
    :param word:
    :return Boolean:
    """
    return word == word[::-1]


palindrome_dict = {}


def update(word, palindrome_dict):
    """
    Used to update the dictionary when Palindrome is found
    :param word:
    :param palindrome_dict:
    :return updated dict count:
    """
    if word not in palindrome_dict:
        palindrome_dict[word] = 1
        return palindrome_dict
    else:
        palindrome_dict[word] += 1  # Counts number of times palindrome occurs
        return palindrome_dict


#  Reads desired .txt file to be searched for Palindromes
with open(input_file, "r") as in_f:
    for line in in_f:
        for word in line.split():
            word = re.sub(r'[^\w]', '', word.lower())  # removes non-word char and capitalization
            if palindrome(word) and len(word) > 1:
                palindrome_dict = update(word, palindrome_dict)
            else:
                continue
    in_f.close()

#  Prints found palindromes to .txt file
with open("found_palindromes.txt", "w") as fp:  # fp = found palindrome
    for item, val in palindrome_dict.items():
        fp.write(" ".join((item, str(val), "\n")))
    fp.close()

print("Done! File saved as found_palindromes.txt")
