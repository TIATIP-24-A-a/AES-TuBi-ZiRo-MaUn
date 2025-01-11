# AES-TuBi-ZiRo-MaUn
PA2

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