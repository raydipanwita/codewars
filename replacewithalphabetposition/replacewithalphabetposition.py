import string
def alphabet_position(text):
    text = text.lower()
    alphabet = string.ascii_lowercase
    index_string = ""
    for letter in text:
        if letter in alphabet:
            index_string += str(alphabet.index(letter) + 1) + " "
    return index_string.rstrip()