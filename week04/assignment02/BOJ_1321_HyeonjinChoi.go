package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

var (
	sc      *bufio.Scanner
	wr      *bufio.Writer
	unitNum int
	treeArr []int
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
	printAnswer()
}

func setting() {
	unitNum = scanInt()
	treeArr = make([]int, int(math.Pow(2, math.Ceil(math.Log2(float64(unitNum)))+1)))

	for i := 1; i <= unitNum; i++ {
		updateTree(1, unitNum, i, 1)
	}
}

// index에 해당하는 부대에 num 값을 할당하는 함수
func updateTree(startIdx, endIdx, index, node int) {
	if startIdx == endIdx {
		treeArr[node] += scanInt()
		return
	}

	midIdx := (startIdx + endIdx) / 2

	if index <= midIdx {
		updateTree(startIdx, midIdx, index, node*2)
	} else {
		updateTree(midIdx+1, endIdx, index, node*2+1)
	}

	// 구간 내 부대의 군사 수를 합
	treeArr[node] = treeArr[node*2] + treeArr[node*2+1]
}

func printAnswer() {
	count := scanInt()

	for i := 0; i < count; i++ {
		if scanInt() == 1 {
			updateTree(1, unitNum, scanInt(), 1)
		} else {
			wr.WriteString(strconv.Itoa(findUnitNum(1, unitNum, scanInt(), 1)) + "\n")
		}
	}
}

// index에 해당하는 군인이 속한 부대를 탐색하는 함수
func findUnitNum(startIdx, endIdx, index, node int) int {
	midIdx := (startIdx + endIdx) / 2

	if startIdx == endIdx {
		return startIdx
	} else if treeArr[node*2] >= index {
		return findUnitNum(startIdx, midIdx, index, node*2)
	} else {
		return findUnitNum(midIdx+1, endIdx, index-treeArr[node*2], node*2+1)
	}
}
