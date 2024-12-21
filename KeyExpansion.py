# Rotation eines Wortes rechts nach links
def rot_word(word):
    return word[1:] + word[:1]

def key_expansion(key):
    return [10,9,8,7,6,5,4,3,2,1,0]