# 8 queens problem

* hackmd: https://hackmd.io/@tana0101/ai_lab4
* github: https://github.com/tana0101/8-queen-problem.git

此專案的目的是使用不同的演算法解決一般與有障礙物的八皇后問題，並觀察其結果。

This project aims to solve the 8 queens problem with and without obstacles using different algorithms and observe the results.

+ 運用基因演算法 (Genetic Algorithm) 找出八皇后問題的其中一解。<br>
Use genetic algorithm (Genetic Algorithm) to find one of the solutions to the 8 queens problem.<br>
<img src="https://github.com/tana0101/8-queen-problem/blob/main/src/c_1.png?raw=true" alt="Image" style="width:250px;"> <img src="https://github.com/tana0101/8-queen-problem/blob/main/src/c_2.png?raw=true" alt="Image" style="width:300px;">

+ 解決有障礙物的八皇后問題（障礙物以城堡代替）。<br>
Solve the 8 queens problem with obstacles (obstacles are replaced by castles).<br>
<img src="https://github.com/tana0101/8-queen-problem/blob/main/src/c_3.png?raw=true" alt="Image" style="width:250px;"> <img src="https://github.com/tana0101/8-queen-problem/blob/main/src/c_4.png?raw=true" alt="Image" style="width:200px;">


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

+ 執行dfs, bfs演算法找出八皇后問題的所有解：
```bash
python 8queen.py --dfs
python 8queen.py --bfs
```
注意：必須選擇一種演算法。

+ 執行dfs, bfs演算法找出有障礙物的八皇后問題的所有解：
```bash
python 8queen.py --dfs --setRandRock
python 8queen.py --bfs --setRandRock
```
注意：Rock的位置是隨機產生的，每次執行程式都會不一樣。

+ 執行dfs, bfs演算法找出有障礙物的八皇后問題的所有解，障礙物數量由setRock設置：
```bash
python 8queen.py --dfs --setRock 障礙物數量
python 8queen.py --dfs --setRock 10
```

+ 執行dfs, bfs演算法找出有障礙物的八皇后問題的所有解，障礙物位置由fen設置：
```bash
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
python 8queen.py --dfs --setRandRock
python 8queen.py --bfs --setRandRock
```
Note: The position of the Rock is randomly generated and will be different each time the program is run.

+ Run dfs, bfs algorithm to find all solutions to the 8 queens problem with obstacles, the number of obstacles is set by setRock:
```bash
python 8queen.py --dfs --setRock number of obstacles
python 8queen.py --dfs --setRock 10
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
