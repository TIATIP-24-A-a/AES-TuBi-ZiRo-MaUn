import base64

S_BOX = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
]


R_CON = [
    [0x01, 0x00, 0x00, 0x00],
    [0x02, 0x00, 0x00, 0x00],
    [0x04, 0x00, 0x00, 0x00],
    [0x08, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00],
    [0x20, 0x00, 0x00, 0x00],
    [0x40, 0x00, 0x00, 0x00],
    [0x80, 0x00, 0x00, 0x00],
    [0x1B, 0x00, 0x00, 0x00],
    [0x36, 0x00, 0x00, 0x00],
]


def split_blocks(text_bytes: bytes) -> list[list[list[int]]]:
    """
    Teilt den Text in Blöcke von 16 Bytes auf in einem 4x4 Matrix
    Der letzte Block wird mit einem Padding aufgefüllt, falls nötig
    """

    block_size = 16
    padding_char = b' '

    blocks: list[list[list[int]]] = []
    length = len(text_bytes)
    amount_blocks = length // block_size

    for i in range(amount_blocks):
        start = i * block_size
        end = i * block_size + block_size
        block_matrix = bytes_to_matrix(text_bytes[start:end])
        blocks.append(block_matrix)

    if length % block_size != 0:
        last_block = text_bytes[block_size * (length // block_size):]

        # Letzter Block mit Padding auffüllen
        last_block_len = len(last_block)
        padding_size = block_size - last_block_len
        last_block += padding_char * padding_size

        blocks.append(bytes_to_matrix(last_block))

    return blocks



def rot_word(word: list[int]) -> list[int]:
    """
    Rotation eines Elements von rechts nach links
    """

    return word[1:] + word[:1]


def key_expansion(key: bytes) -> list[list[list[int]]]:
    """
    Erstellt anhand Key, weitere Keys für die Runden
    AES 128 -> 11 Keys
    :param key:  Initial Key für die Erweiterung
    :return: Liste von Key-Matrix
    """
    initial_key_matrix = bytes_to_matrix(key)
    round_keys: list[list[list[int]]] = [initial_key_matrix]

    for i in range(10):
        previous = round_keys[-1]
        new = []

        # Das letzte Word wird rotiert und durch die S-Box ersetzt
        last_word = previous[-1]
        rotated_word = rot_word(last_word)
        substituted_word = sub_word(rotated_word)
        substituted_word[0] ^= R_CON[i][0]

        # Erstes Word generieren
        first_word = [substituted_word[i] ^ previous[0][i] for i in range(4)]
        new.append(first_word)

        # Restliche Words generieren
        for j in range(1, 4):
            new_word = [previous[j][i] ^ new[j - 1][i] for i in range(4)]
            new.append(new_word)

        round_keys.append(new)

    return round_keys


def sub_word(word: list[int]) -> list[int]:
    return [S_BOX[b >> 4][b & 0x0F] for b in word]


def sub_bytes(state: list[list[int]]) -> list[list[int]]:
    """
    Ersetzt die Bytes im State mit den Werten aus der S-Box
    :param state: 4x4 Matrix
    :return: Neuer State
    """

    for row in range(4):
        for col in range(4):
            byte = state[row][col]
            row_index = (byte >> 4) & 0x0F
            col_index = byte & 0x0F
            state[row][col] = S_BOX[row_index][col_index]

    return state


def bytes_to_matrix(data: bytes) -> list[list[int]]:
    """
    Wandelt die Bytes in ein 4x4 Matrix um
    :param data: Muss 16 Bytes sein
    :return: 4x4 Matrix
    """
    if len(data) != 16:
        raise ValueError('Data must be 16 bytes')

    d = data
    matrix = [
        [d[0], d[4], d[8], d[12]],
        [d[1], d[5], d[9], d[13]],
        [d[2], d[6], d[10], d[14]],
        [d[3], d[7], d[11], d[15]],
    ]

    return matrix

def matrix_to_bytes(matrix: list[list[int]]) -> bytes:
    """
    Wandelt die Matrix in Bytes um (column-major order)
    :param matrix: 4x4 Matrix
    :return: Bytes
    """
    return bytes([matrix[row][col] for col in range(4) for row in range(4)])


def shift_rows(state):
    return [state[i][i:] + state[i][:i] for i in range(4)]


def add_round_key(state: list[list[int]], key: list[list[int]]) -> list[list[int]]:
    """
    Fügt den Round Key zum State mit XOR hinzu
    :param state: aktueller State
    :param key: Round Key zum Hinzufügen
    :return: Neuer State
    """
    new_state: list[list[int]] = []

    # State und Key wird per XOR neugeschrieben
    for state_row_bytes, key_row_bytes in zip(state, key):
        row_state: list[int] = []
        for state_col_byte, key_col_byte in zip(state_row_bytes, key_row_bytes):
            row_state.append(state_col_byte ^ key_col_byte)

        new_state.append(row_state)

    return new_state

# Simple function to apply MixColumns
def mix_columns(state):
    # Process each column
    for i in range(4):
        # Take the values in each column (a, b, c, d) from state
        a = state[0][i]
        b = state[1][i]
        c = state[2][i]
        d = state[3][i]

        # Normalerweise wird es mit einem Gallius Feld berechnet. Einfachheitshalber simulieren wir dies mit simplen addition und subtraktionen.
        state[0][i] = a + b + c + d  # This is a simple sum of the values (just for illustration)
        state[1][i] = a + b - c + d
        state[2][i] = a - b + c + d
        state[3][i] = a + b + c - d

    return state

def encrypt(key: str, text: str) -> str:
    key_bytes = key.encode()
    text_bytes = text.encode()

    if len(key_bytes) != 16:
        raise Exception("Key must be 16 bytes")

    round_keys = key_expansion(key_bytes)
    blocks = split_blocks(text_bytes)
    encrypted_blocks = []

    # Jeder Block durchläuft 11 Runden. Wobei die erste Runde und die letzte Runde sich unterscheiden
    for block in blocks:

        # Erste Runde
        state = add_round_key(block, round_keys[0])

        # 9 Runden
        for i in range(1, 10):
            state = sub_bytes(state)
            state = shift_rows(state)
            state = mix_columns(state)
            state = add_round_key(state, round_keys[i])

        # Letzte Runde
        state = sub_bytes(state)
        state = shift_rows(state)
        state = add_round_key(state, round_keys[10])

        encrypted_blocks.append(matrix_to_bytes(state))

    # Alle verschlüsselten Blöcke zusammenfügen
    encrypted_bytes = b"".join(encrypted_blocks)

    # Base64 Encoding
    encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')
    
    return encrypted_base64