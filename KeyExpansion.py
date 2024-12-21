# Rotation eines Wortes rechts nach links
def rot_word(word):
    return word[1:] + word[:1]

def key_expansion(key):
    round_keys = [key]

    for i in range(10):
        round_key = round_keys[-1]
        round_key = rot_word(round_key)
        round_keys.append(round_key)

    return round_keys


