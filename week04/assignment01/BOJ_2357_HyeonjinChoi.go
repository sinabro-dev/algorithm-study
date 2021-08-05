package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

var (
	sc         *bufio.Scanner
	wr         *bufio.Writer
	intNum     int
	pairNum    int
	height     int
	minTreeArr []int
	maxTreeArr []int
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
	generateSegmentTree(0, intNum-1, 1)
	printAnswer()
}

func setting() {
	intNum, pairNum = scanInt(), scanInt()
	height = int(math.Ceil(math.Log2(float64(intNum))))
	minTreeArr = make([]int, (1 << (height + 1)))
	maxTreeArr = make([]int, (1 << (height + 1)))
}

// 세그먼트 트리처럼 각 구간에 합 대신 최솟값, 최댓값을 저장하는 트리 생성
func generateSegmentTree(startIdx, endIdx, index int) {
	if startIdx == endIdx {
		num := scanInt()
		minTreeArr[index] = num
		maxTreeArr[index] = num
	} else {
		midIdx := (startIdx + endIdx) / 2
		generateSegmentTree(startIdx, midIdx, index*2)
		generateSegmentTree(midIdx+1, endIdx, index*2+1)
		minTreeArr[index] = min(minTreeArr[index*2], minTreeArr[index*2+1])
		maxTreeArr[index] = max(maxTreeArr[index*2], maxTreeArr[index*2+1])
	}
}

func printAnswer() {
	for i := 0; i < pairNum; i++ {
		startIdx, endIdx := scanInt(), scanInt()
		min, max := findAnswer(1, intNum, startIdx, endIdx, 1)
		wr.WriteString(strconv.Itoa(min) + " " + strconv.Itoa(max) + "\n")
	}
}

// 주어진 범위(leftNode ~ rightNode) 내 최솟값과 최댓값을 탐색
func findAnswer(startIdx, endIdx, leftNode, rightNode, index int) (int, int) {
	// 범위를 벗어나면 예외상황 처리
	if leftNode > endIdx || rightNode < startIdx {
		return 1000000001, 0
	}

	if leftNode <= startIdx && endIdx <= rightNode {
		return minTreeArr[index], maxTreeArr[index]
	} else {
		midIdx := (startIdx + endIdx) / 2
		leftMin, leftMax := findAnswer(startIdx, midIdx, leftNode, rightNode, index*2)
		rightMin, rightMax := findAnswer(midIdx+1, endIdx, leftNode, rightNode, index*2+1)
		return min(leftMin, rightMin), max(leftMax, rightMax)
	}
}

func max(num1, num2 int) int {
	if num1 > num2 {
		return num1
	} else {
		return num2
	}
}

func min(num1, num2 int) int {
	if num1 < num2 {
		return num1
	} else {
		return num2
	}
}
