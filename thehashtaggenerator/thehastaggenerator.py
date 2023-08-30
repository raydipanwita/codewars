import string
def generate_hashtag(s):
    if len(s) <= 0 :
        return False
    newword = (string.capwords(s)).replace(" ", "")
    if len(newword) >= 140:
        return False
    return "{}{}".format("#", newword)