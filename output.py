# Description: 輸出圖片、棋盤、網頁到指定資料夾，
#              其目的是為了方便觀察結果，並且可以快速比較不同演算法的結果。




# showBoard: 顯示與儲存棋盤
# b: 棋盤, result_dir: 儲存圖片的資料夾
import chess
def showBoard(b, result_dir = "images"):
    board = chess.Board()
    print("Board:")
    print("\n")
    for i in range(8):
        for j in range(8):
            if b[i][j]==8 or b[i][j]==1:
                board.set_piece_at(chess.square(j, i), None)
            else:
                board.set_piece_at(chess.square(j, i), chess.Piece(chess.QUEEN, chess.WHITE))
    print(board)
    showBoardWeb(board = board, result_dir = result_dir)

# showBoardWeb: 將棋盤儲存為 svg 圖檔後，以網頁方式、lichess 編輯頁開啟
# board: 棋盤, result_dir: 儲存圖片的資料夾, file: 儲存圖片的檔名
import webbrowser 
import chess.svg
def showBoardWeb(board, result_dir = "images"):
    # 產生board.svg
    board_svg = chess.svg.board(board=board)
    file_name = save_svg_file(board_svg = board_svg, file = "board", result_dir = result_dir)

    # 開啟圖片board.svg
    webbrowser.get('windows-default').open_new(file_name)

    # 開啟lichess editor
    fen = board.fen()
    url = 'https://lichess.org/editor/' + fen + '?color=white'
    webbrowser.get('windows-default').open_new(url)

# save_image_file: 將圖片儲存為 png 檔，並以編號方式命名
# file: 儲存圖片的檔名, result_dir: 儲存圖片的資料夾, idx: 編號
import matplotlib.pyplot as plt
import os
def save_image_file(file, result_dir = "images", idx = 0):
    if not os.path.exists(result_dir):  # 如果文件夾不存在，創建文件夾
        os.makedirs(result_dir)
    if os.path.exists(os.path.join(result_dir, f"{file}.png")):
        idx += 1
    while os.path.exists(os.path.join(result_dir, f"{file}_{idx}.png")):
        idx += 1
    if idx == 0:
        plt.savefig(os.path.join(result_dir, f"{file}.png"))
    else:
        plt.savefig(os.path.join(result_dir, f"{file}_{idx}.png"))

# save_svg_file: 將棋盤儲存為 svg 圖檔，並以編號方式命名
# board_svg: 棋盤, file: 儲存圖片的檔名, result_dir: 儲存圖片的資料夾, idx: 編號
def save_svg_file(board_svg, file, result_dir = "images", idx = 0):
    if not os.path.exists(result_dir):  # 如果文件夾不存在，創建文件夾
        os.makedirs(result_dir)
    if os.path.exists(os.path.join(result_dir, f"{file}.svg")):
        idx += 1
    while os.path.exists(os.path.join(result_dir, f"{file}_{idx}.svg")):
        idx += 1
    if idx == 0:
        with open(os.path.join(result_dir, f"{file}.svg"), "w") as f:
            f.write(board_svg)
        file_name = os.path.join(result_dir, f"{file}.svg")
    else:
        with open(os.path.join(result_dir, f"{file}_{idx}.svg"), "w") as f:
            f.write(board_svg)
        file_name = os.path.join(result_dir, f"{file}_{idx}.svg")
    return file_name