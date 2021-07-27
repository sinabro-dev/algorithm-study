package main

import (
	"bufio"
	"os"
	"strconv"
)

type Pos struct {
	row int
	col int
}

type Status string

const (
	None = Status("None")
	Air = Status("Air")
	Cheese  = Status("Cheese")
	Melting = Status("Melting")
)

var (
	sc *bufio.Scanner
	wr *bufio.Writer
	board [][]Status
)

func init() {
	sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)

	wr = bufio.NewWriter(os.Stdout)
}

func main() {
	defer wr.Flush()
	generateBoard(scanInt(), scanInt())
	result := solve()
	wr.WriteString(strconv.Itoa(result))
}

func generateBoard(N, M int) {
	/*
	모눈 종이의 각 칸이 외부 공기인지, 내부 공기인지, 치즈인지 세팅을 하는 과정
	 */
	board = make([][]Status, N)
	for i := range board {
		board[i] = make([]Status, M)
	}

	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			curState := None
			if scanInt() == 1 {
				curState = Cheese
			}
			board[i][j] = curState
		}
	}

	setVertexToAirState()
}

func solve() int {
	/*
	처음부터 1시간이 지날 때마다 녹을 수 있는 칸에 위치한 치즈를 구하는 과정을 반복
	더이상 녹을 수 있는 치즈가 없는 경우 걸린 시간을 반환
	 */
	meltingPos := getPosToBeMelted()

	var time int
	var pos Pos
	for time = 0; len(meltingPos) != 0; time++ {
		for _, pos = range meltingPos {
			board[pos.row][pos.col] = None
		}
		setVertexToAirState()
		meltingPos = getPosToBeMelted()
	}

	return time
}

func getPosToBeMelted() (result []Pos) {
	/*
	앞으로 녹을 수 있는 치즈의 위치를 찾는 과정
	 */
	rowSize := len(board)
	colSize := len(board[0])

	for i := 1; i < rowSize - 1; i++ {
		for j := 1; j < colSize - 1; j++ {
			if isToBeMelted(i, j) {
				board[i][j] = Melting
				result = append(result, Pos{row: i, col: j})
			}
		}
	}
	return
}

func isToBeMelted(rowPos, colPos int) bool {
	/*
	치즈가 위치한 칸에서 외부 공기로 둘러싸인 변이 2개 이상이면 참 값을 반환
	 */
	if board[rowPos][colPos] != Cheese {
		return false
	}

	exposedSide := 0
	if board[rowPos-1][colPos] == Air {
		exposedSide++
	}
	if board[rowPos][colPos-1] == Air {
		exposedSide++
	}
	if board[rowPos][colPos+1] == Air {
		exposedSide++
	}
	if board[rowPos+1][colPos] == Air {
		exposedSide++
	}

	if exposedSide >= 2 {
		return true
	}
	return false
}

func setVertexToAirState() {
	/*
	모눈 종이에서 치즈가 위치하지 않은 곳은 우선 모두 None 상태로 되돌려 놓은 후
	BFS 를 이용해 외부 공기인지, 내부 공기인지 판단하여 기록
	 */
	rowSize := len(board)
	colSize := len(board[0])

	for i := 0; i < rowSize; i++ {
		for j := 0; j < colSize; j++ {
			if board[i][j] != Cheese {
				board[i][j] = None
			}
		}
	}

	queue := make(chan Pos, len(board) * len(board[0]))
	queue <- Pos{0, 0}

	for ; len(queue) != 0; {
		currentPos := <- queue
		for _, pos := range findAdjacentPosNonState(currentPos) {
			board[pos.row][pos.col] = Air
			queue <- pos
		}
	}
}

func findAdjacentPosNonState(pos Pos) (result []Pos) {
	rowSize := len(board)
	colSize := len(board[0])

	if (pos.row - 1 >= 0) && (board[pos.row - 1][pos.col] == None) {
		result = append(result, Pos{pos.row - 1, pos.col})
	}
	if (pos.col - 1 >= 0) && (board[pos.row][pos.col - 1] == None) {
		result = append(result, Pos{pos.row, pos.col - 1})
	}
	if (pos.col + 1 < colSize) && (board[pos.row][pos.col + 1] == None) {
		result = append(result, Pos{pos.row, pos.col + 1})
	}
	if (pos.row + 1 < rowSize) && (board[pos.row + 1][pos.col] == None) {
		result = append(result, Pos{pos.row + 1, pos.col})
	}
	return
}

func scanInt() int {
	sc.Scan()
	num, _ := strconv.Atoi(sc.Text())
	return num
}