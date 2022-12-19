package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var (
	sc        *bufio.Scanner
	wr        *bufio.Writer
	M         int
	N         int
	K         int
	count     int
	answerArr []int
	dx        = [4]int{1, 0, -1, 0}
	dy        = [4]int{0, 1, 0, -1}
	mapArr    [][]int
	visitArr  [][]bool
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

func main() {
	defer wr.Flush()
	setting()
	solve()
	printAnswer()
}

func setting() {
	M, N, K = scanInt(), scanInt(), scanInt()

	mapArr = make([][]int, M)
	for i := 0; i < M; i++ {
		mapArr[i] = make([]int, N)
	}

	visitArr = make([][]bool, M)
	for i := 0; i < M; i++ {
		visitArr[i] = make([]bool, N)
	}
}

func solve() {
	painting()

	for i := 0; i < M; i++ {
		for j := 0; j < N; j++ {
			if mapArr[i][j] == 0 && !visitArr[i][j] {
				count = 0
				dfs(i, j)
				answerArr = append(answerArr, count)
			}
		}
	}
}

func painting() {
	for i := 0; i < K; i++ {
		x1, y1, x2, y2 := scanInt(), scanInt(), scanInt(), scanInt()

		for j := y1; j < y2; j++ {
			for k := x1; k < x2; k++ {
				mapArr[j][k] = 1
			}
		}
	}
}

func dfs(y, x int) {
	if mapArr[y][x] == 0 && !visitArr[y][x] {
		visitArr[y][x] = true
		count++

		for i := 0; i < 4; i++ {
			X := x + dx[i]
			Y := y + dy[i]

			if X >= 0 && X < N && Y >= 0 && Y < M {
				dfs(Y, X)
			}
		}
	}
}

func printAnswer() {
	sort.Slice(answerArr, func(i, j int) bool {
		return answerArr[i] < answerArr[j]
	})

	num := len(answerArr)

	wr.WriteString(strconv.Itoa(num) + "\n")

	for i := 0; i < num; i++ {
		wr.WriteString(strconv.Itoa(answerArr[i]) + " ")
	}
}
