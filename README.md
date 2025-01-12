# AES-TuBi-ZiRo-MaUn

Diese AES Verschlüsselung sollte **NICHT** verwendet werden.

# Dependencies installieren

Ist das Repo gekloned, kann mit folgenden Befehl, die benötigten Dependencies installiert werden:

```bash
pip install -r requirements.txt
```

## Requirements.txt aktualisieren

Nach der Installation einer Depedency kann mittels `pipreqs`, das `requirements.txt` neu generiert werden.

`pipreqs` installieren:
```bash
pip install pipreqs
```

`requirements.txt` neugenerieren:
```bash
pipreqs --encoding=utf8 --ignore .venv --force ./
```


## Flowchart AES Encryption
```mermaid
---
title: 
---
graph TD
    
id0([Input: Text and Key])-->id1[Convert Text & Key to bytes]
id1 ---> id7[Convert to 4x4 blocks]
id1 ---> id2
id2[Key]--> id4{Key is 16 bytes?}
id4 -- Yes --> id5[Run Key expansion]
id4 -- No --> id6([Raise Exception])
id7 --> id8[for each block]
id5 ---> id8
id8 ---->id9{First Round?}

subgraph TD Roundkey Function
    id9 --Yes--> id10[add Roundkey]
    id10 ---> id11[replace with S_Box]
    id9 -- No --> id11
    id11 --> id12[shift Rows]
    id12 --> id13{last Round?}
    id13 -- No --> id14[shift Cols]
    id14 ---> id8
end


id13 -----------> id15([Encrypted Text])



```