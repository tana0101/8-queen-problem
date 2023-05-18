# 8 queens problem

此專案的目的是使用不同的演算法解決一般與有障礙物的八皇后問題，並觀察其結果。

This project aims to solve the 8 queens problem with and without obstacles using different algorithms and observe the results.

+ 運用基因演算法 (Genetic Algorithm) 找出八皇后問題的其中一解。
Use genetic algorithm (Genetic Algorithm) to find one of the solutions to the 8 queens problem.
![Genetic_1](https://hackmd.io/_uploads/SJX3qhMSh.png =250x)　![Genetic_2](https://hackmd.io/_uploads/SkAYc3fSn.png =300x)

+ 解決有障礙物的八皇后問題（障礙物以城堡代替）。
Solve the 8 queens problem with obstacles (obstacles are replaced by castles).
![obstacles_1](https://hackmd.io/_uploads/r1ZOq2XHn.png =250x)　![obstacles_2](https://hackmd.io/_uploads/Bkli52XS3.png =200x)



## Installation

+ 若要在您的本地端執行此專案，請依照以下步驟進行：

1. 執行以下指令安裝所需的套件：
```bash
pip install -r requirements.txt
```
這個指令會安裝此專案所需的所有套件。

<hr>

+ To run this project on your local machine, follow these steps:

1. Install the required dependencies by running the following command:
```bash
pip install -r requirements.txt
```
This will install all the necessary packages for this project.

## Usage

+ 執行dfs, bfs演算法找出八皇后問題的所有解：
```bash
python 8queen.py --dfs
python 8queen.py --bfs
```
注意：必須選擇一種演算法。

+ 執行dfs, bfs演算法找出有障礙物的八皇后問題的所有解：
```bash
python 8queen.py --dfs --setRock
python 8queen.py --bfs --setRock
```
注意：Rock的位置是隨機產生的，每次執行程式都會不一樣。

+ 執行dfs, bfs演算法找出以fen設置有障礙物棋盤的八皇后問題的所有解：
```bash
python 8queen.py --dfs --setFen "棋盤fen"
python 8queen.py --dfs --setFen "8/3R4/8/8/3R4/5R2/8/8 w - - 0 1"
```
注意：棋盤fen可以用[這個網站](https://lichess.org/editor)產生，障礙物ROCK我們以城堡代替，可以參考[範例](https://lichess.org/editor/8/3R4/8/8/3R4/5R2/8/8_w_-_-_0_1?color=white)。

+ 執行基因演算法找出八皇后問題的其中一解：
```bash
python Queen.py
```
注意：因為基因演算法的隨機性可能造成短時間內無法找到解，這時請重新執行程式。

請按照以上規則執行程式。如有任何問題，請聯絡開發人員。

<hr>

+ Run dfs, bfs algorithm to find all solutions to the 8 queens problem:
```bash
python 8queen.py --dfs
python 8queen.py --bfs
```
Note: You must choose one algorithm.

+ Run dfs, bfs algorithm to find all solutions to the 8 queens problem with obstacles:
```bash
python 8queen.py --dfs --setRock
python 8queen.py --bfs --setRock
```
Note: The position of Rock is randomly generated and will be different each time the program is run.        

+ Run dfs, bfs algorithm to find all solutions to the 8 queens problem with obstacles set by fen:
```bash
python 8queen.py --dfs --setFen "棋盤fen"
python 8queen.py --dfs --setFen "8/3R4/8/8/3R4/5R2/8/8 w - - 0 1"
```
Note: The chessboard fen can be generated with [this website](https://lichess.org/editor), and the obstacle ROCK is replaced by the castle, you can refer to [example](https://lichess.org/editor/8/3R4/8/8/3R4/5R2/8/8_w_-_-_0_1?color=white).

+ Run the genetic algorithm to find one solution to the 8 queens problem:
```bash
python Queen.py
```

Note: Because the randomness of the genetic algorithm may cause the solution to not be found in a short time, please run the program again.

Please run the program according to the above rules. If you have any questions, please contact the developer.



## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository and clone it to your local machine.
2. Create a new branch and make your changes.
3. Push your changes to your forked repository.
4. Create a pull request to merge your changes into the main repository.
