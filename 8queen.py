# Description: 運用dfs, bfs解決一般與有障礙物的八皇后問題的所有解，
#              並挑選隨機的棋盤結果輸出成 svg 圖片後，儲存到 dfs, bfs 資料夾，
#              再用網頁瀏覽器開啟棋盤 svg 圖片與 lichess 編輯頁。             




import argparse
import chess
import queue
import random
import output

def is_valid(board, row, col):
    # 此位置有沒有被放置過石頭
    if board.piece_at(chess.square(col, row)) == chess.Piece(chess.ROOK, chess.WHITE):
        return False

    # 從col,row往左上檢查
    for i in range(1, row+1):
        # 有沒有超出棋盤
        if col-i < 0 or row-i < 0:
            break
        # 有沒有在皇后的攻擊線上
        if board.piece_at(chess.square(col-i, row-i)) == chess.Piece(chess.QUEEN, chess.WHITE):
            return False
        # 有沒有石頭擋住了攻擊線
        if board.piece_at(chess.square(col-i, row-i)) is not None:
            break

    # 從col,row往右上檢查
    for i in range(1, row+1):
        # 有沒有超出棋盤
        if col+i > 7 or row-i < 0:
            break
        # 有沒有在皇后的攻擊線上
        if board.piece_at(chess.square(col+i, row-i)) == chess.Piece(chess.QUEEN, chess.WHITE):
            return False
        # 有沒有石頭擋住了攻擊線
        if board.piece_at(chess.square(col+i, row-i)) is not None:
            break

    # 從col,row往左下檢查
    for i in range(1, min(8-row, col+1)):
        # 有沒有超出棋盤
        if col-i < 0 or row+i > 7:
            break
        # 有沒有在皇后的攻擊線上
        if board.piece_at(chess.square(col-i, row+i)) == chess.Piece(chess.QUEEN, chess.WHITE):
            return False
        # 有沒有石頭擋住了攻擊線
        if board.piece_at(chess.square(col-i, row+i)) is not None:
            break

    # 從col,row往右下檢查
    for i in range(1, min(8-row, 8-col)):
        # 有沒有超出棋盤
        if col+i > 7 or row+i > 7:
            break
        # 有沒有在皇后的攻擊線上
        if board.piece_at(chess.square(col+i, row+i)) == chess.Piece(chess.QUEEN, chess.WHITE):
            return False
        # 有沒有石頭擋住了攻擊線
        if board.piece_at(chess.square(col+i, row+i)) is not None:
            break

    # 從col,row往上檢查
    for i in range(row+1):
        # 有沒有超出棋盤
        if row-i < 0:
            break
        # 有沒有在皇后的攻擊線上
        if board.piece_at(chess.square(col, row-i)) == chess.Piece(chess.QUEEN, chess.WHITE):
            return False
        # 有沒有石頭擋住了攻擊線
        if board.piece_at(chess.square(col, row-i)) is not None:
            break
    
    # 從col,row往下檢查
    for i in range(row+1):
        # 有沒有超出棋盤
        if row+i > 7:
            break
        # 有沒有在皇后的攻擊線上
        if board.piece_at(chess.square(col, row+i)) == chess.Piece(chess.QUEEN, chess.WHITE):
            return False
        # 有沒有石頭擋住了攻擊線
        if board.piece_at(chess.square(col, row+i)) is not None:
            break
    
    # 從col,row往左檢查
    for i in range(col+1):
        # 有沒有超出棋盤
        if col-i < 0:
            break
        # 有沒有在皇后的攻擊線上
        if board.piece_at(chess.square(col-i, row)) == chess.Piece(chess.QUEEN, chess.WHITE):
            return False
        # 有沒有石頭擋住了攻擊線
        if board.piece_at(chess.square(col-i, row)) is not None:
            break
    
    # 從col,row往右檢查
    for i in range(col+1):
        # 有沒有超出棋盤
        if col+i > 7:
            break
        # 有沒有在皇后的攻擊線上
        if board.piece_at(chess.square(col+i, row)) == chess.Piece(chess.QUEEN, chess.WHITE):
            return False
        # 有沒有石頭擋住了攻擊線
        if board.piece_at(chess.square(col+i, row)) is not None:
            break

    # 沒有在皇后的攻擊線上，回傳True
    return True

# deep first search，用遞迴實作
def dfs(board, row, solutions):
    if row == 8:
        solutions.append(board.copy())
        return
    
    for col in range(8):
        if is_valid(board, row, col):
            board.set_piece_at(chess.square(col, row), chess.Piece(chess.QUEEN, chess.WHITE))
            dfs(board, row+1, solutions)
            board.remove_piece_at(chess.square(col, row))

# breadth first search，用queue實作
def bfs(board, solutions):
    q = queue.Queue()
    q.put((board, 0))

    while not q.empty():
        curr_board, curr_row = q.get()

        if curr_row == 8:
            solutions.append(curr_board.copy())
            continue

        for col in range(8):
            if is_valid(curr_board, curr_row, col):
                new_board = curr_board.copy()
                new_board.set_piece_at(chess.square(col, curr_row), chess.Piece(chess.QUEEN, chess.WHITE))
                q.put((new_board, curr_row+1))

if __name__ == "__main__":
    # 透過參數選擇使用的演算法
    parser = argparse.ArgumentParser(description='Solve the eight queens problem.')
    parser.add_argument('--dfs', dest='dfs', action='store_true', help='Use depth-first search to solve the problem')
    parser.add_argument('--bfs', dest='bfs', action='store_true', help='Use breadth-first search to solve the problem')
    parser.add_argument('--setRock', dest='setRock', action='store_true', help='Set rock on the board')
    parser.add_argument('--setFen', dest='fen', type=str, help='Set fen on the board')
    args = parser.parse_args()

    # 建立空棋盤
    board = chess.Board()
    board.clear()
    solutions = []

    # 隨機設置石頭
    if args.setRock:
        # 隨機產生石頭的位置
        rock_num = random.randint(1, 8)
        rock_pos = random.sample(range(64), rock_num)
        for pos in rock_pos:
            board.set_piece_at(pos, chess.Piece(chess.ROOK, chess.WHITE))
        print("rock:")
        print(board)
        print()

    # 以fen設置石頭位置
    if args.fen:
        board.set_fen(args.fen)
        print("rock:")
        print(board)
        print()

    # 計算並且儲存檔案
    # 透過try except來判斷使用者是否有輸入dfs或bfs
    try:
        if args.dfs and args.bfs:
            raise Exception("Cannot use both dfs and bfs")
        elif args.dfs:
            dfs(board, 0, solutions)
            algorithm_name = "dfs"
            print("dfs:")
        elif args.bfs:
            bfs(board, solutions)
            algorithm_name = "bfs"
            print("bfs:")
        else:
            raise Exception("Please read the usage of README.md, and choose one algorithm to solve the problem")
    except Exception as e:
        print(e)
        exit(1)

    # 輸出所有答案
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}:")
        print(solution.fen())
        print(solution)
        print()

    # 輸出總共有幾個答案
    print("------------------------------------------")
    print(f"Total {len(solutions)} solutions")
    print("------------------------------------------\n")

    # 隨機挑選一個答案輸出
    rand = random.randint(0, len(solutions)-1)
    print(f"Random solution {rand+1}:")
    print(solutions[rand].fen())
    print(solutions[rand])
    fen = solutions[rand].fen()

    # 儲存棋盤的 svg 圖片到 algorithm_name 資料夾
    # 將棋盤 svg 以網頁方式開啟
    # 將棋盤以 lichess 編輯頁開啟
    output.showBoardWeb(solutions[rand], result_dir = algorithm_name)
