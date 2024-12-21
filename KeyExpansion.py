# Rotation eines Wortes rechts nach links
def rot_word(word):
    return word[1:] + word[:1]

def key_expansion(key):
    return [key,
            'aaaaaaaaaaaaaaaa',
            'aaaaaaaaaaaaaaaa',
            'aaaaaaaaaaaaaaaa',
            'aaaaaaaaaaaaaaaa',
            'aaaaaaaaaaaaaaaa',
            'aaaaaaaaaaaaaaaa',
            'aaaaaaaaaaaaaaaa',
            'aaaaaaaaaaaaaaaa',
            'aaaaaaaaaaaaaaaa',
            'aaaaaaaaaaaaaaaa']