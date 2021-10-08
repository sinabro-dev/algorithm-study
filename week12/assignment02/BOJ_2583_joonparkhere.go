package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var (
	graph [][]bool
)

func main() {
	defer writer.Flush()

	setUp()
	solve()
}

func setUp() {
	inputArr := scanIntArray()
	rowSize, colSize := inputArr[0], inputArr[1]

	graph = make([][]bool, rowSize)
	for i := range graph {
		graph[i] = make([]bool, colSize)
	}

	for i := 0; i < inputArr[2]; i++ {
		squarePosition := scanIntArray()
		for row := squarePosition[1]; row < squarePosition[3]; row++ {
			for col := squarePosition[0]; col < squarePosition[2]; col++ {
				graph[row][col] = true
			}
		}
	}
}

func solve() {
	areas := make([]int, 0)
	rowSize, colSize := len(graph), len(graph[0])

	for i := 0; i < rowSize; i++ {
		for j := 0; j < colSize; j++ {
			if graph[i][j] {
				continue
			}

			area := bfs(i, j)
			areas = append(areas, area)
		}
	}

	sort.Ints(areas)
	writer.WriteString(strconv.Itoa(len(areas)) + "\n")
	for _, area := range areas {
		writer.WriteString(strconv.Itoa(area) + " ")
	}
}

func bfs(row, col int) int {
	queue := make([][2]int, 0)

	numOfArea := 1
	graph[row][col] = true
	queue = append(queue, [2]int{row, col})

	dRow := []int{1, 0, -1, 0}
	dCol := []int{0, 1, 0, -1}

	for len(queue) != 0 {
		curRow, curCol := queue[0][0], queue[0][1]
		queue = queue[1:]

		for i := 0; i < len(dRow); i++ {
			nextRow, nextCol := curRow + dRow[i], curCol + dCol[i]
			if isOutOfIndex(nextRow, nextCol) {
				continue
			}

			if !graph[nextRow][nextCol] {
				numOfArea++
				graph[nextRow][nextCol] = true
				queue = append(queue, [2]int{nextRow, nextCol})
			}
		}
	}

	return numOfArea
}

func isOutOfIndex(row, col int) bool {
	rowSize, colSize := len(graph), len(graph[0])

	if row < 0 || row >= rowSize {
		return true
	}
	if col < 0 || col >= colSize {
		return true
	}
	return false
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

func scanIntArray() []int {
	scanner.Scan()
	idx := 0
	array := make([]int, 1)
	for _, c := range scanner.Bytes() {
		if c == ' ' {
			idx++
			array = append(array, 0)
			continue
		}
		array[idx] = array[idx] * 10 + int(c - '0')
	}
	return array
}
