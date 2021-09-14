package main

import (
	"bufio"
	"os"
	"strconv"
)

type Location struct {
	x int
	y int
}

var (
	sc       *bufio.Scanner
	wr       *bufio.Writer
	N        int
	M        int
	dx       = [4]int{0, 1, 0, -1}
	dy       = [4]int{-1, 0, 1, 0}
	location []Location
	mapArr   [][]byte
	answer   int
)

func init() {
	sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	wr = bufio.NewWriter(os.Stdout)
}

func scanInt() int {
	sc.Scan()
	num, _ := strconv.Atoi(sc.Text())
	return num
}

func scanString() string {
	sc.Scan()
	return sc.Text()
}

func main() {
	defer wr.Flush()
	setting()
	solve()
	printAnswer()
}

func setting() {
	N, M = scanInt(), scanInt()
	answer = 11

	mapArr = make([][]byte, N)
	for i := 0; i < N; i++ {
		mapArr[i] = make([]byte, M)
		temp := scanString()
		for j := 0; j < M; j++ {
			mapArr[i][j] = temp[j]

			if mapArr[i][j] == 'o' {
				location = append(location, Location{i, j})
			}
		}
	}
}

func solve() {
	for i := 0; i < 4; i++ {
		x1, y1, x2, y2 := location[0].x, location[0].y, location[1].x, location[1].y
		move(x1, y1, x2, y2, 1, i)
	}
}

func move(x1, y1, x2, y2, count, direction int) {
	if answer < count {
		return
	}

	if count > 10 {
		answer = min(answer, count)
		return
	}

	X1, Y1, X2, Y2 := x1+dx[direction], y1+dy[direction], x2+dx[direction], y2+dy[direction]

	if checkOutside(X1, Y1) && checkOutside(X2, Y2) {
		return
	} else if checkOutside(X1, Y1) || checkOutside(X2, Y2) {
		answer = min(answer, count)
		return
	}

	if mapArr[X1][Y1] == '#' {
		X1, Y1 = x1, y1
	}

	if mapArr[X2][Y2] == '#' {
		X2, Y2 = x2, y2
	}

	for i := 0; i < 4; i++ {
		move(X1, Y1, X2, Y2, count+1, i)
	}
}

func checkOutside(x, y int) bool {
	if x < 0 || y < 0 || x >= N || y >= M {
		return true
	} else {
		return false
	}
}

func min(num1, num2 int) int {
	if num1 < num2 {
		return num1
	} else {
		return num2
	}
}

func printAnswer() {
	if answer > 10 {
		answer = -1
	}

	wr.WriteString(strconv.Itoa(answer))
}
