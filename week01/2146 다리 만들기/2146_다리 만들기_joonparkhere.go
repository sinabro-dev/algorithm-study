package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

type Pos struct {
	x int
	y int
}

const (
	sea = int(0)
	notSpecificLand = int(10000)
)

var (
	sc          *bufio.Scanner
	wr          *bufio.Writer
	sideLength  int
	numOfIsland int
	board       [][]int
)

func init() {
	sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)

	wr = bufio.NewWriter(os.Stdout)
}

func main() {
	defer wr.Flush()
	generateBoard(scanInt())
	result := solve()
	fmt.Println(result)
}

func generateBoard(N int) {
	sideLength = N
	board = make([][]int, sideLength)
	for i := range board {
		board[i] = make([]int, sideLength)
	}

	/*
		각 위치가 바다인지, 육지인지 기록
		바다인 경우 0, 육지인 경우 10000 으로 기록
	*/
	for i := 0; i < sideLength; i++ {
		for j := 0; j < sideLength; j++ {
			board[i][j] = scanInt() * notSpecificLand
		}
	}

	/*
		각 섬을 Grouping 하는 과정
		육지인 board 값 (현재는 10000) 이 해당 섬의 index 값으로 Update
		ex) 총 섬의 개수가 3개인 경우,
		첫번째 섬에 속한 육지의 board 값은 1로 두번째 섬에 속한 육지의 board 값은 2로 ... 설정
	*/
	var i, j int
	for i = 0; i < sideLength; i++ {
		for j = 0; j < sideLength; j++ {
			// 현재 board 값이 0이라면, 아직 특정 섬으로 구분짓지 않은 육지이므로 Update 해야함
			if board[i][j] == notSpecificLand {
				// 전역 변수 numOfIsland 는 총 섬의 개수를 저장하는 용도이자, 각 섬의 index 값으로 활용하기도 함
				numOfIsland++

				// Queue 를 활용한 섬 구분짓기
				queue := make(chan Pos, sideLength * sideLength)
				board[i][j] = numOfIsland
				queue <- Pos{i, j}

				for ; len(queue) != 0; {
					curPos := <- queue
					adjacent := findAdjacentByCondition(curPos, notSpecificLand)
					for _, pos := range adjacent {
						board[pos.x][pos.y] = numOfIsland
						queue <- pos
					}
				}
			}
		}
	}
}

func solve() (result int) {
	result = sideLength * sideLength

	/*
		각각의 섬에 속하는 육지 중에서도 해변인 육지의 board 값을 2차원 슬라이스로 가져오는 과정
	*/
	seaSide := findSeaSide()

	/*
		섬과 섬 사이의 최소 거리를 구하는 과정을 반복
		중복 계산하지 않도록 Combination 형태의 반복문을 수행
	*/
	for i := 0; i < len(seaSide); i++ {
		for j := i + 1; j < len(seaSide); j++ {
			// 각 섬에 속하는 좌표와 좌표 사이의 거리 중 최솟값이 곧 섬과 섬 사이의 최소 거리
			length := findShortestBridgeLengthByCoordinate(seaSide[i], seaSide[j])
			if length < result {
				result = length
			}
		}
	}
	return
}

func findSeaSide() (result [][]Pos) {
	result = make([][]Pos, numOfIsland)
	for i := 0; i < sideLength; i++ {
		for j := 0; j < sideLength; j++ {
			pos := Pos{i, j}
			if isSeaSide(pos) {
				idx := board[i][j] - 1
				result[idx] = append(result[idx], pos)
			}
		}
	}
	return
}

func findShortestBridgeLengthByCoordinate(from, to []Pos) (result int) {
	result = sideLength * sideLength
	for _, begin := range from {
		for _, end := range to {
			value := int(math.Abs(float64(begin.x-end.x)) + math.Abs(float64(begin.y-end.y))) - 1
			if value < result {
				result = value
			}
		}
	}
	return
}

func isSeaSide(pos Pos) bool {
	if board[pos.x][pos.y] == sea {
		return false
	}

	adjacent := findAdjacentByCondition(pos, sea)
	if len(adjacent) > 0 {
		return true
	}
	return false
}

func findAdjacentByCondition(pos Pos, condition int) (result []Pos) {
	if (pos.x - 1 >= 0) && (board[pos.x - 1][pos.y] == condition) {
		result = append(result, Pos{pos.x - 1, pos.y})
	}
	if (pos.y - 1 >= 0) && (board[pos.x][pos.y - 1] == condition) {
		result = append(result, Pos{pos.x, pos.y - 1})
	}
	if (pos.y + 1 < sideLength) && (board[pos.x][pos.y + 1] == condition) {
		result = append(result, Pos{pos.x, pos.y + 1})
	}
	if (pos.x + 1 < sideLength) && (board[pos.x + 1][pos.y] == condition) {
		result = append(result, Pos{pos.x + 1, pos.y})
	}
	return
}

func scanInt() int {
	sc.Scan()
	num, _ := strconv.Atoi(sc.Text())
	return num
}