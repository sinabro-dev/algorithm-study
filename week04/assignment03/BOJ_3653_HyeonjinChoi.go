package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	sc       *bufio.Scanner
	wr       *bufio.Writer
	n        int
	m        int
	max      int
	treeSize int
	treeArr  []int
	dvdPos   []int
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
	solve()
}

func solve() {
	caseNum := scanInt()

	for i := 0; i < caseNum; i++ {
		setting()
		findAnswer()
	}
}

func setting() {
	max = 100001
	treeSize = 1 << 19
	treeArr = make([]int, treeSize)
	dvdPos = make([]int, max)

	n, m = scanInt(), scanInt()
	initTree(1, 1, n+m)

	for i := 1; i <= n; i++ {
		dvdPos[i] = m + i
		update(1, 1, n+m, dvdPos[i], 1)
	}
}

// DVD 위치 초기화
func initTree(node, startNode, endNode int) {
	treeArr[node] = 0

	if startNode == endNode {
		return
	}

	left := node * 2
	right := node*2 + 1
	midNode := (startNode + endNode) / 2
	initTree(left, startNode, midNode)
	initTree(right, midNode+1, endNode)
}

// index에 해당하는 말단 정점을 value 값으로 갱신
func update(node, startNode, endNode, index, value int) {
	if startNode == endNode {
		treeArr[node] = value
		return
	}

	left := node * 2
	right := node*2 + 1
	midNode := (startNode + endNode) / 2

	if index > midNode {
		update(right, midNode+1, endNode, index, value)
	} else {
		update(left, startNode, midNode, index, value)
	}

	treeArr[node] = treeArr[left] + treeArr[right]
}

func findAnswer() {
	next := m

	for i := 1; i <= m; i++ {
		target := scanInt()
		wr.WriteString(strconv.Itoa(query(1, 1, n+m, 1, dvdPos[target]-1)) + " ")

		update(1, 1, n+m, dvdPos[target], 0)
		dvdPos[target] = next
		next--
		update(1, 1, n+m, dvdPos[target], 1)
	}

	wr.WriteString("\n")
}

func query(index, startNode, endNode, left, right int) int {
	if (right < startNode) || (endNode < left) {
		return 0
	}

	if (left <= startNode) && (endNode <= right) {
		return treeArr[index]
	}

	midNode := (startNode + endNode) / 2
	leftNode := index * 2
	rightNode := index*2 + 1

	return query(leftNode, startNode, midNode, left, right) + query(rightNode, midNode+1, endNode, left, right)
}
