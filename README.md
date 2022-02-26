# Chess API 
Simple API to get possile moves of any chess figure based on field or to check does move of figure is possible.
## Technologies used in project
- Python == 3.9.5
- Flask == 2.0.3
- PyTest == 7.0.1

## Manual to API
### To Check all possible moves of figure:
    http://localhost:8000/api/opt1/{figure}/{current_field}
#### example: 
    http://localhost:8000/api/opt1/rook/h8

### To check is move is valid for figure on field:
    http://localhost:8000/api/opt2/{figure}/{current_field}/{destination_field}
#### example: 
    http://localhost:8000/api/opt2/rook/h2/h8

#### All figures in chess game:
    [pawn, rook, bishop, knight, queen, king]

#### All possible fields on chess board:
    [ A1, B1, C1, D1, E1, F1, G1, H1 ]
    [ A2, B2, C2, D2, E2, F2, G2, H2 ]
    [ A3, B3, C3, D3, E3, F3, G3, H3 ]
    [ A4, B4, C4, D4, E4, F4, G4, H4 ]
    [ A5, B5, C5, D5, E5, F5, G5, H5 ]
    [ A6, B6, C6, D6, E6, F6, G6, H6 ]
    [ A7, B7, C7, D7, E7, F7, G7, H7 ]
    [ A8, B8, C8, D8, E8, F8, G8, H8 ]

## Manual to start aplication:
    1. This command is going to download repository from github
        git clone https://github.com/SMajev/ChessREST.git

    2. This command will install all requirement packages from python repository:
        pip3 install -r requirements.txt

    3. Last command is use to run Flask server 
        python3 main/app.py

    
