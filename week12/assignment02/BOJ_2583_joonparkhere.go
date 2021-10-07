package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var (
	graph [][]int
	dRow  = []int{1, 0, -1, 0}
	dCol  = []int{0, 1, 0, -1}
)

type pos struct {
	row int
	col int
}

func main() {
	defer writer.Flush()

	setUp()
	solve()
}

func setUp() {
	inputArr := scanIntArray()
	rowSize, colSize := inputArr[0], inputArr[1]

	graph = make([][]int, rowSize)
	for i := range graph {
		graph[i] = make([]int, colSize)
	}

	for i := 0; i < inputArr[2]; i++ {
		squarePosition := scanIntArray()
		for row := squarePosition[1]; row < squarePosition[3]; row++ {
			for col := squarePosition[0]; col < squarePosition[2]; col++ {
				graph[row][col] = -1
			}
		}
	}
}

func solve() {
	areas := make([]int, 0)
	for i := 0; i < len(graph); i++ {
		for j := 0; j < len(graph[0]); j++ {
			if graph[i][j] < 0 {
				continue
			}

			area := bfs(i, j)
			areas = append(areas, area)
		}
	}

	sort.Slice(areas, func(i, j int) bool {
		return areas[i] < areas[j]
	})

	writer.WriteString(strconv.Itoa(len(areas)) + "\n")
	for _, area := range areas {
		writer.WriteString(strconv.Itoa(area) + " ")
	}
}

func bfs(row, col int) int {
	queue := make([]pos, 0)

	numOfArea := 1
	queue = append(queue, pos{row, col})
	graph[row][col] = -1

	for len(queue) != 0 {
		curPos := queue[0]
		queue = queue[1:]

		for i := 0; i < 4; i++ {
			nextRow := curPos.row + dRow[i]
			nextCol := curPos.col + dCol[i]

			if nextRow < 0 || nextRow >= len(graph) || nextCol < 0 || nextCol >= len(graph[0]) {
				continue
			}

			if graph[nextRow][nextCol] >= 0 {
				numOfArea++
				graph[nextRow][nextCol] = -1
				queue = append(queue, pos{nextRow, nextCol})
			}
		}
	}

	return numOfArea
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
