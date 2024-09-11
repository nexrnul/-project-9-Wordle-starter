import os
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

def csrCphr(message, alphabet): 
    for char in (message): 
        search =alphabet.index(char)
        yield search

def csrShift(inpshift, alph):
    indexes = (list(csrCphr(msg, characters)))
    shiftd_output= []
    for i in indexes:
        ushift = (i + inpshift) % len(alph)
        charshift = alph[ushift]
        shiftd_output.append(charshift)
    return ''.join(shiftd_output)

msg = "frozen"
shift = 2    
key = (csrShift(shift, characters))
#os.system('clear')




