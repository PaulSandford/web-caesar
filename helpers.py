
def alphabet_position(lett):
    lett = lett.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    return alpha.index(lett)

def rotate_character(char, rot):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if type(rot) == str:
        rot = alphabet_position(rot)
    ind = (rot + alphabet_position(char))%26
    
    if alpha.find(char) >= 0:
        return alpha[ind]
    else:
        return alpha[ind].upper()