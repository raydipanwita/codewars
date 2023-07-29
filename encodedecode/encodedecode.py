def encode(st):
    vowels = { "a" : 1 , "e" : 2 , "i" : 3 , "o" : 4 , "u" : 5}
    for x in vowels:
        st = st.replace(x, str(vowels[x]))
    return st
    
    
def decode(st):
    vowels = { "a" : 1 , "e" : 2 , "i" : 3 , "o" : 4 , "u" : 5}
    for keys, values in vowels.items():
        st = st.replace(str(values), keys)
    return st