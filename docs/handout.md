# Verschlüsselung: AES 128

Gruppenarbeit von Rodrigo Zihlmann, Matthias Unternährer und Tuan Binh Tran

# Einleitung

Dieses Handout beschreibt unsere Lösung zur Python-Aufgabe "Verschlüsselung: AES".
Dabei sind unsere Funktion und Tests beschrieben. Auch unsere Gedanken sind festgehalten.

Die Ziele und Bewertung sind der Aufgabe "Übung II: Fortgeschrittene Algorithmen" zu entnehmen: https://github.com/fhirter/Software-Engineering/blob/master/ProgrammingBasicsAndAlgorithms/Exercises/Advanced/Tasks.md


# Ziele

- Fokus auf die 128-bit Variante von AES
- Fokus auf Encryption
- Decryption Optional bzw. wenn genügend Zeit vorhanden
- Die Encryption liefert den verschlüsselten Text in Base64 zurück
- Bei Komplexeren Funktionen, wird die Logik vereinfacht und im Code beschrieben


# Projektstruktur

Das Repository ist im Github aufzufinden: https://github.com/TIATIP-24-A-a/AES-TuBi-ZiRo-MaUn

Beischreibung der Projektstruktur:

- `/`: Root
  - `AES.py`: AES 128 mit allen benötigten Funktionen
  - `AES_Test.py`: Unit-Tests für `AES.py`
  - `.gitignore`: Ignorieren von Dateien im Git
  - `README.md`: Das README File
  - `docs/handout.md`: Du bist hier

# Beschreibung der AES 128 Verschlüsselung

Die AES 128 akzeptiert zwei String Parameter. Beim ersten Parameter handelt es sich um den `key`. Mit dem zweiten Parameter, `text` wird der zuverschlüsselte Text angegeben.

Der `key` muss genau aus 16 bytes bestehen. Dies wird validiert und es wird eine Exception geworfen.
Der `text` kann eine beliebige Länge haben. 


Die Funktion wandelt zum Start die beiden Parametern in bytes um. Dies ist für die Weiterverarbeitung wichtig.
Ebenfalls werden die bytes in ein 4x4 Matrix umgewandelt. 

Die AES 128 umfasst verschiedene Funktionen, welche bei der Encryption benötigt wird:

- Key Expansion
- Erste Runde
  - Add Round Key
- Restliche Runden
  - Sub Bytes
  - Shift Rows
  - Mix Columns (Wird in der letzten Runde nicht ausgeführt)
  - Add Round Key

# Unit Tests

Die Unit-Tests wurde im TDD-Verfahren erstellt.
Da AES aus verschiedenste Funktionen besteht, wurde diese geprüft.

Für die detaillierte Implementation siehe `AES_Test.py`.


# Erkenntnisse
- AES ist komplex
- Zusammenspiel von verschiedenen Algorithmen ist schwierig

# Quellen
- AES: Step-by-Step In-Depth: https://medium.com/@dillihangrae/aes-advanced-encryption-standard-step-by-step-in-depth-understanding-62a9db709902
- AES: How to Design Secure Encryption: https://www.youtube.com/watch?v=C4ATDMIz5wc&pp=ygUDYWVz
- AES key schedule: https://en.wikipedia.org/wiki/AES_key_schedule
- AES Key Expansion Algorithm: https://www.tutorialspoint.com/cryptography/cryptography_aes_key_expansion_algorithm.htm
- The AES Key Schedule explained: https://braincoke.fr/blog/2020/08/the-aes-key-schedule-explained/#aes-key-schedule