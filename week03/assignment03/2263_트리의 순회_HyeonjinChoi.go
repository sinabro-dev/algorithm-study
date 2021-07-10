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
	generateTree()
}

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

func generateTree() {
	
}
