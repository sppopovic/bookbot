import string

#print("hello world")

def open_book(filename):
    file_contents = ""
    with open(filename) as f:
        file_contents = f.read()
    return file_contents

def word_count(s):
    words = s.split()
    #print(len(words))
    return words

def letter_count(s):
    ls = s.lower()
    letters = {}
    for letter in string.ascii_lowercase:
        letters[letter] = ls.count(letter)
    #print(letters)
    return letters

def report(file_name, words, letters):
    print(f"--- Begin report of {file_name} ---")
    print(f"{len(words)} words found in the document")
    print("\n")
    for letter in string.ascii_lowercase:
        print(f"The '{letter}' character was found {letters[letter]} times")
    print("--- End report ---")

def main():
    fn = "books/frankenstein.txt"
    file_contents = open_book(fn)
    words = word_count(file_contents)
    letters = letter_count(file_contents)
    report(fn, words, letters)
    


main()


