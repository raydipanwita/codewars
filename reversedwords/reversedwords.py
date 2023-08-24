def reverse_words(text):
  #go for it
    text = text.split(" ")
    newstring = ""
    for x in text:
        newstring += x[::-1] + " "
    return newstring.strip()