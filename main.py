import chess
import chess.pgn
import csv
from itertools import islice



    
def normalize(moves):
    result = ""
    for move in moves.split():
        if len(move)== 5 and  move[-1].isdigit():
            result += move[:3] + " " + move[3:]
        else:
            result += move[:2] + " " + move[2:]
        result += " "
    result = result[:-1]
    return(result)

def convert_san_to_pgn(fen, san_moves):
    board = chess.Board(fen)
    game = chess.pgn.Game.from_board(board)
    node = game
    moves = san_moves.split()
    
    for i in range(0, len(moves), 2):
        move_from, move_to = moves[i], moves[i + 1]
        uci_string = f"{move_from}{move_to}"
        move = chess.Move.from_uci(uci_string)
        node = node.add_variation(move)
        board.push(move)
    #hinky part here#
    pgn_game = chess.pgn.StringExporter(headers=False, variations=False, comments=True)
    pgn_moves = game.accept(pgn_game)
    return(pgn_moves)

file_path = 'lichess_db_puzzle.csv'
start_line = 100000
end_line = 200000
with open(file_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)

    for _ in range(start_line - 1):
        next(csv_reader)

    for row in islice(csv_reader, end_line - start_line + 1):
        fen = row[1]
        san_moves = normalize(row[2])
        if int(row[3]) > 2100 and ("mateIn4" in row[7].split() or "mateIn5" in row[7].split()):
            data = convert_san_to_pgn(fen,san_moves)
            ans = [data[i] for i in range(1,len(data)) if data[i-1]==" " and not data[i].isdigit()]
            real_ans = [ans[i] for i in range(len(ans)) if i%2==1]
            if "Q" not in real_ans and "N" not in real_ans and "B" in real_ans and "R" in real_ans:
                #print(data)
                #print(real_ans)
                print(row[0])
            else:
                continue
                
