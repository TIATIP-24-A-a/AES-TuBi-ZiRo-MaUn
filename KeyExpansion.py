# Rotation eines Wortes rechts nach links
def rot_word(word):
    return word[1:] + word[:1]


def key_expansion(key: str) -> list[bytes]:
    """
    Erstellt anhand Key, weitere Keys für die Runden
    AES 128 -> 11 Keys
    :param key:  Initial Key für die Erweiterung
    :return: Liste von Keys in bytes
    """
    round_keys: list[bytes] = [key.encode()]

    for i in range(10):
        round_key = round_keys[-1]
        round_key = rot_word(round_key)
        round_keys.append(round_key)

    return round_keys
