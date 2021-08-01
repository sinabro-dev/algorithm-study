package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

type Assignment struct {
	deadline int
	reward   int
}

// max heap 구현
type MaxHeap []int

func (h *MaxHeap) Push(vals int) {
	*h = append(*h, vals)
	h.Up(len(*h) - 1)
}

func (h *MaxHeap) Up(idx int) {
	for h.Compare(idx, ParentNode(idx)) {
		h.Swap(ParentNode(idx), idx)
		idx = ParentNode(idx)
	}
}

func (h *MaxHeap) Pop() int {
	popped := (*h)[0]
	(*h)[0] = (*h)[len(*h)-1]
	(*h) = (*h)[:len(*h)-1]
	h.Down(0)
	return popped
}

func (h *MaxHeap) Down(idx int) {
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

func (h *MaxHeap) Swap(i, j int) {
	(*h)[i], (*h)[j] = (*h)[j], (*h)[i]
}

func (h *MaxHeap) Compare(i, j int) bool {
	return (*h)[i] > (*h)[j]
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
	sc         *bufio.Scanner
	wr         *bufio.Writer
	assNum     int
	assignment []Assignment
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
	setting()
	priorityQueue := &MaxHeap{}

	answer := 0

	// 우선순위 큐를 이용하여 조건에 부합하는 보상 저장
	for i := 0; i < assNum; i++ {
		dealine := assignment[i].deadline
		priorityQueue.Push(-assignment[i].reward)

		if len(*priorityQueue) > dealine {
			priorityQueue.Pop()
		}
	}

	for len(*priorityQueue) > 0 {
		answer += priorityQueue.Pop()
	}

	wr.WriteString(strconv.Itoa(-answer))
}

// 데드라인과 보상(컵라면수)에 대한 입력을 받음
func setting() {
	assNum = scanInt()
	assignment = make([]Assignment, assNum)

	for i := 0; i < assNum; i++ {
		assignment[i].deadline = scanInt()
		assignment[i].reward = scanInt()
	}

	// 데드라인에 대하여 오름차순으로 정렬
	sort.Slice(assignment, func(i, j int) bool {
		return assignment[i].deadline < assignment[j].deadline
	})
}
