class Puzzle:
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

    def csrCphr(message, alphabet): 
        for char in (message): 
            #search =alphabet.index(char)
            yield alphabet.index(char)

#My Ceaser Shift code from previous semester ported over and slightly modified 
    def csrShift(inpshift, alph):
        indexes = list(Puzzle.csrCphr("frozen", alph))
        shiftd_output= []
        for i in indexes:
            ushift = (i + inpshift) % len(alph)
            charshift = alph[ushift]
            shiftd_output.append(charshift)
        return ''.join(shiftd_output)

    def encrypt_msg(msg, shift):
        encrypted_msg = Puzzle.csrShift(shift, Puzzle.characters)
        riddle = input("(hint: answer related to your surroundings)").lower()
        return riddle


