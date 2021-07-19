package main

import (
	"bufio"
	"os"
	"strconv"
)

type node struct {
	cost int
	prev []int
	next []int
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
	numOfNode int
	time []int
	first []int
	last []int
	tree []node
)

func scanInt() int {
	scanner.Scan()
	num, _ := strconv.Atoi(scanner.Text())
	return num
}

func main() {
	scanner.Split(bufio.ScanWords)

	generateTree()
	findMinCost()

	writer.Flush()
}

func generateTree() {
	numOfNode = scanInt()
	time = make([]int, numOfNode)
	tree = make([]node, numOfNode)

	for idx := 0; idx < numOfNode; idx++ {
		time[idx] = scanInt()
		numOfPrev := scanInt()

		if numOfPrev == 0 {
			tree[idx] = node{cost: time[idx], prev: nil, next: make([]int, 0)}
			first = append(first, idx)
			continue
		}

		tree[idx] = node{cost: 0, prev: make([]int, 0), next: make([]int, 0)}
		for i := 0; i < numOfPrev; i++ {
			prevIdx := scanInt() - 1
			tree[prevIdx].next = append(tree[prevIdx].next, idx)
			tree[idx].prev = append(tree[idx].prev, prevIdx)
		}
	}
}

func findMinCost() {
	queue := make([]int, 0)

	for _, i := range first {
		queue = append(queue, i)
	}

	for len(queue) != 0 {
		idx := queue[0]
		queue = queue[1:]

		next := tree[idx].next
		if len(next) == 0 {
			last = append(last, idx)
			continue
		}

		for _, i := range next {
			if !isPrevFinished(i) {
				continue
			}
			prevCost := getMaxCostInPrev(i)
			tree[i].cost = prevCost + time[i]
			queue = append(queue, i)
		}
	}

	result := 0
	for _, i := range last {
		if tree[i].cost > result {
			result = tree[i].cost
		}
	}
	writer.WriteString(strconv.Itoa(result))
}

func isPrevFinished(idx int) bool {
	for i := range tree[idx].prev {
		if tree[i].cost == 0 {
			return false
		}
	}
	return true
}

func getMaxCostInPrev(idx int) int {
	max := 0
	for _, i := range tree[idx].prev {
		if tree[i].cost > max {
			max = tree[i].cost
		}
	}
	return max
}
