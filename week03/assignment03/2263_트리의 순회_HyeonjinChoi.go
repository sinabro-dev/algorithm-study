package main

import (
	"bufio"
	"os"
	"strconv"
)

type Node struct {
	parent int
	left   int
	right  int
}

var (
	sc           *bufio.Scanner
	wr           *bufio.Writer
	nodeNum      int
	inOrderArr   []int
	postOrderArr []int
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
	solve(0, nodeNum-1, nodeNum-1)
}

// 인오더, 포스트오더에 해당하는 수를 입력받는 함수
func setting() {
	nodeNum = scanInt()
	inOrderArr = make([]int, nodeNum)
	postOrderArr = make([]int, nodeNum)

	for i := 0; i < nodeNum; i++ {
		inOrderArr[i] = scanInt()
	}

	for i := 0; i < nodeNum; i++ {
		postOrderArr[i] = scanInt()
	}
}

// 인자로 받은 범위 내에서 루트를 찾고 출력, 이후 좌측 우측 자식정점 순으로 반복
func solve(startIdx, endIdx, rootIdx int) {
	midIdx := findIdx(postOrderArr[rootIdx])
	wr.WriteString(strconv.Itoa(inOrderArr[midIdx]) + " ")

	if startIdx <= midIdx-1 {
		solve(startIdx, midIdx-1, rootIdx-1-(endIdx-midIdx))
	}

	if midIdx+1 <= endIdx {
		solve(midIdx+1, endIdx, rootIdx-1)
	}
}

// inOrderArr[]에서 인자로 받은 값에 해당하는 인덱스를 찾는 함수
func findIdx(num int) int {
	for index, data := range inOrderArr {
		if data == num {
			return index
		}
	}

	return -1
}
