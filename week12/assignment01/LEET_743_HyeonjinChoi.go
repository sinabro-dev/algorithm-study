package main

import (
	"bufio"
	"os"
	"strconv"
)

type Node struct {
	end, weight int
}

type MinHeap []Node

func (h *MinHeap) Push(w Node) {
	*h = append(*h, w)
	h.Up(len(*h) - 1)
}

func (h *MinHeap) Up(idx int) {
	for h.Compare(idx, ParentNode(idx)) {
		h.Swap(ParentNode(idx), idx)
		idx = ParentNode(idx)
	}
}

func (h *MinHeap) Pop() Node {
	popped := (*h)[0]
	(*h)[0] = (*h)[len(*h)-1]
	(*h) = (*h)[:len(*h)-1]
	h.Down(0)
	return popped
}

func (h *MinHeap) Down(idx int) {
	lastIdx := len(*h) - 1
	l, r := LeftNode(idx), RightNode(idx)

	var childToCompare int
	for l <= lastIdx {
		if l == lastIdx {
			childToCompare = l
		} else if h.Compare(l, r) {
			childToCompare = l
		} else {
			childToCompare = r
		}

		if h.Compare(idx, childToCompare) {
			return
		}
		h.Swap(idx, childToCompare)
		idx = childToCompare
		l, r = LeftNode(idx), RightNode(idx)
	}
}

func (h *MinHeap) Swap(i, j int) {
	(*h)[i], (*h)[j] = (*h)[j], (*h)[i]
}

func (h *MinHeap) Compare(i, j int) bool {
	return (*h)[i].weight < (*h)[j].weight
}

func ParentNode(i int) int {
	return (i - 1) / 2
}

func LeftNode(i int) int {
	return 2*i + 1
}

func RightNode(i int) int {
	return 2*i + 2
}

var (
	sc    *bufio.Scanner
	wr    *bufio.Writer
	n     int
	k     int
	times [][]int
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
	networkDelayTime(times, n, k)
}

func setting() {
	num := scanInt()
	times = make([][]int, num)
	for i := 0; i < n; i++ {
		times[i] = make([]int, 3)
		times[i][0], times[i][1], times[i][2] = scanInt(), scanInt(), scanInt()
	}

	n, k = scanInt(), scanInt()
}

func networkDelayTime(times [][]int, n int, k int) int {
	Q := &MinHeap{}
	Q.Push(Node{k, 0})

	var arr []Node

	for {
		q := Q.Pop()
		endNode, time := q.end, q.weight

		if findNode()
	}
}

func findNode(arr []Node, value int) bool {
	for _, node := range arr {
		if node.end == value {
			return true
		}
	}

	return false
}
