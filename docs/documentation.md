# AES Implementierung Dokumentation

Diese Dokumentation beschreibt die Implementierung des AES (Advanced Encryption Standard) Algorithmus in Python.

## Funktionen

### `split_blocks(text_bytes: bytes) -> list[list[list[int]]]`

Teilt den Text in Blöcke von 16 Bytes auf und wandelt diese in eine 4x4 Matrix um. Der letzte Block wird mit einem Padding aufgefüllt, falls nötig.

### `rot_word(word: list[int]) -> list[int]`

Rotiert ein Element von rechts nach links.

### `key_expansion(key: bytes) -> list[list[list[int]]]`

Erstellt anhand des Initial Keys weitere Keys für die Runden. AES 128 benötigt 11 Keys.

### `sub_word(word: list[int]) -> list[int]`

Ersetzt die Bytes im Word mit den Werten aus der S-Box.

### `sub_bytes(state: list[list[int]]) -> list[list[int]]`

Ersetzt die Bytes im State mit den Werten aus der S-Box.

### `bytes_to_matrix(data: bytes) -> list[list[int]]`

Wandelt die Bytes in eine 4x4 Matrix um. Die Daten müssen 16 Bytes lang sein.

### `matrix_to_bytes(matrix: list[list[int]]) -> bytes`

Wandelt die Matrix in Bytes um (column-major order).

### `shift_rows(state) -> list[list[int]]`

Verschiebt die Reihen im State zyklisch nach links.

### `add_round_key(state: list[list[int]], key: list[list[int]]) -> list[list[int]]`

Fügt den Round Key zum State mit XOR hinzu.

### `mix_columns(state) -> list[list[int]]`

Wendet die MixColumns-Transformation auf den State an.

### `encrypt(key: str, text: str) -> str`

Verschlüsselt den Text mit dem gegebenen Key. Der Key muss 16 Bytes lang sein. Der verschlüsselte Text wird in Base64 kodiert zurückgegeben.

## Vorbereitung

Bevor die Verarbeitung beginnt, muss noch einiges gemacht werden. Dies beinhaltet die Validierung und die Umwandlung in eine 4x4 Matrix.

### Key

Der `key` wird in Bytes umgewandelt und es wird geprüft, ob die exakte Länge von 16 Bytes erreicht wurde. Ist dies nicht der Fall, so wird eine `Exception` geworfen.

### Text

Der zu verschlüsselnde Text wird in Bytes umgewandelt und in Blöcke von 16 Bytes aufgeteilt. Der letzte Block wird mit einem Padding aufgefüllt, falls nötig.

## Beispiel

```python
from AES import encrypt

key = "This is a key123"
text = "This is some text to encrypt"

encrypted_text = encrypt(key, text)
print(encrypted_text)
```
