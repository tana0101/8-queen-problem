# Lab 4: 8 queens problem

## 作者資訊
作者：林一
系級：資工3B
學號：00957101
* hackmd: https://hackmd.io/@tana0101/ai_lab4
* github: https://github.com/tana0101/8-queen-problem.git

## 實驗內容描述：
**使用不同的演算法解決一般與有障礙物的八皇后問題，並觀察其結果。**
Note：使用方式請參考README的usage。

### 功能簡述：
1. 運用基因演算法 (Genetic Algorithm) 找出八皇后問題的其中一解。
![](https://hackmd.io/_uploads/SJX3qhMSh.png =250x)　![](https://hackmd.io/_uploads/SkAYc3fSn.png =300x)
2. 參考基因演算法的過程，以 dfs, bfs 找出八皇后問題的所有解
* 解決一般的八皇后問題
![](https://hackmd.io/_uploads/ByCKU6mSn.png =250x)　![](https://hackmd.io/_uploads/r1y2IamHn.png =200x)
* 解決有障礙物的八皇后問題（障礙物以城堡代替）。
![](https://hackmd.io/_uploads/r1ZOq2XHn.png =250x)　![](https://hackmd.io/_uploads/Bkli52XS3.png =200x)
3. 輸出結果，並寫入 output.py 中。
* 輸出 棋盤svg 與 fitness結果的圖檔
![](https://hackmd.io/_uploads/S1_UYTXHh.png =800x)
* 開啟 lichess 編輯頁
![](https://hackmd.io/_uploads/HJp7YTXSh.png =300x)

4. 運用 argparse 控制運行的方式，使用方式請參考README的usage
* 設置計算的演算法
* 設置棋盤的隨機障礙物
* 設置棋盤的障礙物，並以 fen 輸入棋盤
```bash
>python 8queen.py -h
usage: 8queen.py [-h] [--dfs] [--bfs] [--setRock] [--setFen FEN]

Solve the eight queens problem.

options:
  -h, --help    show this help message and exit
  --dfs         Use depth-first search to solve the problem
  --bfs         Use breadth-first search to solve the problem
  --setRock     Set rock on the board
  --setFen FEN  Set fen on the board
```
## 實驗步驟

* Step 1：修改 Queens.py 並重新設計輸出方式，將其寫入 output.py 中方便引用。
* Step 2：8queen.py：參考基因演算法的過程，以 dfs, bfs 找出八皇后問題的所有解並評估盤面是否合理。
* Step 3：設計障礙物問題，提供障礙物隨機生成與人工讀入 fen 棋盤。

## Step 1：修改 Queens.py 並重新設計輸出方式，將其寫入 output.py 中方便引用：

* 修改 Queens.py，將基因演算法的棋盤轉換為 python-chess 套件，方便儲存、顯示與輸出。
* 完成以下三種功能：
1. 儲存棋盤的 svg 圖片到 genetic 資料夾
2. 將棋盤 svg 以網頁方式開啟
3. 將棋盤以 lichess 編輯頁開啟

### Queens.py
```python
if printBoard:
        # 儲存棋盤的 svg 圖片到 genetic 資料夾
        # 將棋盤 svg 以網頁方式開啟
        # 將棋盤以 lichess 編輯頁開啟
        output.showBoard(b = b, result_dir = "genetic") # 顯示與儲存棋盤
```
### output.py
* 運用 python-chss 輸出棋盤
```python
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
```
* 運用 webbrowser 開啟網頁
```python
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
```
![](https://hackmd.io/_uploads/HJp7YTXSh.png =300x)　![](https://hackmd.io/_uploads/SJoIc0XH2.png =350x)
* 儲存圖片，並將不同演算法的結果分類至不同的資料夾儲存
1. 儲存為 png 檔
```python
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
```
2. 儲存為 svg 檔
```python
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
```
![](https://hackmd.io/_uploads/S1_UYTXHh.png =800x)

## Step 2：8queen.py：參考基因演算法的過程，以 dfs, bfs 找出八皇后問題的所有解並評估盤面是否合理。

* 設計搜尋演算法： dfs, bfs
* 評估盤面是否合理

### 8queen.py
* dfs
```python
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
```
* bfs
```python
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
```
* 評估盤面是否合理
1. 檢查放置的位置是否有障礙物
2. 檢查放置的皇后，其攻擊線是否被障礙物遮擋
3. 檢查攻擊線上，是否有其他皇后
```python
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
            
    # ... 中間省略
    
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
```

## Step 3：設計障礙物問題，提供障礙物隨機生成與人工讀入 fen 棋盤。
* 設計能夠輸入參數，來設置棋盤的介面。
* 設計障礙物問題，如何生成與讀入。
### 8queen.py
* 設計輸入介面
1. 運用 argparse 設置輸入格式
```python
# 透過參數選擇使用的演算法
    parser = argparse.ArgumentParser(description='Solve the eight queens problem.')
    parser.add_argument('--dfs', dest='dfs', action='store_true', help='Use depth-first search to solve the problem')
    parser.add_argument('--bfs', dest='bfs', action='store_true', help='Use breadth-first search to solve the problem')
    parser.add_argument('--setRock', dest='setRock', action='store_true', help='Set rock on the board')
    parser.add_argument('--setFen', dest='fen', type=str, help='Set fen on the board')
    args = parser.parse_args()
```
```bash
>python 8queen.py -h
usage: 8queen.py [-h] [--dfs] [--bfs] [--setRandRock] [--setRock SETROCK] [--setFen FEN]

Solve the eight queens problem.

options:
  -h, --help         show this help message and exit
  --dfs              Use depth-first search to solve the problem
  --bfs              Use breadth-first search to solve the problem
  --setRandRock      Set random rock on the board
  --setRock SETROCK  Set the number of rock on the board
  --setFen FEN       Set fen on the board
```
2. 運用 try except 協助使用者
```python
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
```
* 設計障礙物問題（以城堡作為障礙物）
1. 障礙物隨機生成
```python
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
```
2. 障礙物生成固定的數量、隨機的位置
```python
# 設置固定數量的石頭
    if args.setRock:
        # 產生石頭的位置
        rock_pos = random.sample(range(64), args.setRock)
        for pos in rock_pos:
            board.set_piece_at(pos, chess.Piece(chess.ROOK, chess.WHITE))
        print("rock:")
        print(board)
        print()
```
3. 人工讀入 fen 棋盤
```python
# 以fen設置石頭位置
    if args.fen:
        board.set_fen(args.fen)
        print("rock:")
        print(board)
        print()
```
![](https://hackmd.io/_uploads/Byu20AQH3.png =300x)

## 實驗報告

### 實驗結果

本次實驗，針對在障礙物數量對八皇后問題的影響，做出了兩項猜測：

**(a). 障礙物數量可能影響解答數量**
**(b). 障礙物位置可能影響解答數量**

<hr>

#### **(a). 障礙物數量對解答數量的影響：**
* 控制變因：障礙物的位置都是隨機
* 操作變因：障礙物的數量

從以下的實驗結果，可以觀察到：
1. 在大多數的時候，有障礙物時，解答的數量會增加。
2. 在多數時候，障礙物越多時，解答的數量會增加。
3. <font color=red>但是障礙物數量與解答數量並沒有呈現絕對的正相關性，由於障礙物的位置都是隨機，所以推測是障礙物的位置對解答數量的影響更大。</font>

| 障礙物數量 | 解答數量 | 棋盤範例 |
| -------- | -------- | -------- |
| 0     | 92     | ![](https://hackmd.io/_uploads/SyHdBWrHn.png =100x)          |
| 1     | 88     | ![](https://hackmd.io/_uploads/ByxJtxBS3.png =100x)     |
| 2     | 848     | ![](https://hackmd.io/_uploads/HkWGFxBS3.png =100x)     |
| 3     | 254     | ![](https://hackmd.io/_uploads/SJtOFlrr2.png =100x)     |
| 4     | 1308     | ![](https://hackmd.io/_uploads/Hy1pYeBHn.png =100x)     |
| 5     | 2326     | ![](https://hackmd.io/_uploads/By9-9gBrn.png =100x)     |
| 6     | 196     | ![](https://hackmd.io/_uploads/BJEBqxSr3.png =100x)     |
| 7     | 1465     | ![](https://hackmd.io/_uploads/SysKclBB2.png =100x)     |
| 8     | 2183     | ![](https://hackmd.io/_uploads/SkHRqlrr3.png =100x)     |
| 9     | 1402     | ![](https://hackmd.io/_uploads/HyjmjgHHn.png =100x)     |
| 10     | 4473     | ![](https://hackmd.io/_uploads/HyStoerr2.png =100x)     |

#### **(b). 障礙物位置對解答的影響：**
* 控制變因：障礙物數量
* 操作變因：不同的障礙物位置

從以下的實驗結果，可以觀察到：
1. 障礙物位置對解答數量的影響巨大，四次實驗中，最少（468）與最多（4473）差了4005個解答數量，共差9.5倍。符合我們對(a).3推測的結果。
2. 由於實驗的次數甚少，難以推測位置與數量的關係，但就目前的實驗結果來看，障礙物越是靠近中央，解答的數量就會增加。

| 障礙物數量 | 解答數量 | 棋盤範例 |
| -------- | -------- | -------- |
| 10     | 4473     | ![](https://hackmd.io/_uploads/HyStoerr2.png =100x)     |
| 10     | 2006     | ![](https://hackmd.io/_uploads/SyYAjlHHn.png =100x)     |
| 10     | 468     | ![](https://hackmd.io/_uploads/BkGG3xBH2.png =100x)     |
| 10     | 2555     | ![](https://hackmd.io/_uploads/BJnDnxHBh.png =100x)     |

### 實驗心得

這一次的作業，由於有了上一回設計小精靈的經驗，所以用了專案的形式來重新設計。
* 大量運用套件
1. argparse：設計程式的輸入介面。
2. webbrowser：讓程式能夠開啟瀏覽器，搭配lichess做使用。
3. python-chess：運用chess套件，簡化開發的方式。
4. os：儲存檔案與分類資料夾。
* 設計輸入介面：運用 argparse 與 try except ，增加使用者體驗。
* 運用抽象化的 function 並設計接口，讓不同的演算法都能使用，減少開發難度、減少重複程式碼與增加擴充性

也因為此次作業相當靈活，所以就運用了上一回使用到的演算法，並搭配上八皇后的延伸問題，給自己一個不一樣的挑戰。否則如果只使用他人的程式做修改，學到的內容就有諸多限制，並且也會非常無趣。

從設計演算法、設計IO、設計 function 的串接方式到運用軟工的開發技巧，也讓這次的功課更加完整，也跨了不同的科目做練習。

### 實驗記錄
| 障礙物數量 | 解答數量 | 棋盤範例 |
| -------- | -------- | -------- |
| 1     | ![](https://hackmd.io/_uploads/ByOj_xrBh.png =140x)     | ![](https://hackmd.io/_uploads/ByxJtxBS3.png =180x)     |
| 2     | ![](https://hackmd.io/_uploads/rJABFlSBh.png =140x)     | ![](https://hackmd.io/_uploads/HkWGFxBS3.png =180x)     |
| 3     | ![](https://hackmd.io/_uploads/ByecFxBBn.png =140x)     | ![](https://hackmd.io/_uploads/SJtOFlrr2.png =180x)     |
| 4     | ![](https://hackmd.io/_uploads/BJZ15gSr3.png =140x)     | ![](https://hackmd.io/_uploads/Hy1pYeBHn.png =180x)     |
| 5     | ![](https://hackmd.io/_uploads/BJuM9eSH2.png =140x)     | ![](https://hackmd.io/_uploads/By9-9gBrn.png =180x)     |
| 6     | ![](https://hackmd.io/_uploads/r19I9gHBn.png =140x)     | ![](https://hackmd.io/_uploads/BJEBqxSr3.png =180x)     |
| 7     | ![](https://hackmd.io/_uploads/BJEscgBHn.png =140x)     | ![](https://hackmd.io/_uploads/SysKclBB2.png =180x)     |
| 8     | ![](https://hackmd.io/_uploads/SJ81jgrBn.png =140x)     | ![](https://hackmd.io/_uploads/SkHRqlrr3.png =180x)     |
| 9     | ![](https://hackmd.io/_uploads/ByCEilBH2.png =140x)     | ![](https://hackmd.io/_uploads/HyjmjgHHn.png =180x)     |
| 10     | ![](https://hackmd.io/_uploads/H1tcjxSS3.png =140x)    | ![](https://hackmd.io/_uploads/HyStoerr2.png =180x)     |
| 10     | ![](https://hackmd.io/_uploads/ryCkhxSHn.png =140x)    | ![](https://hackmd.io/_uploads/SyYAjlHHn.png =180x)     |
| 10     | ![](https://hackmd.io/_uploads/S1Em3erHn.png =140x)    | ![](https://hackmd.io/_uploads/BkGG3xBH2.png =180x)     |
| 10     | ![](https://hackmd.io/_uploads/BkFu2gSH2.png =140x)    | ![](https://hackmd.io/_uploads/BJnDnxHBh.png =180x)     |
