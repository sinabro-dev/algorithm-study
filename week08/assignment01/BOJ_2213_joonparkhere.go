package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var (
	weights     []int
	tree        []node
	memoWeights []int
	memoCases   []cases
	elements    []int
)

type node struct {
	parent   int
	children []int
}

type cases bool
const caseA cases = false	// 어떤 노드를 포함하지 않고 자식 노드들을 포함하는 경우
const caseB cases = true	// 어떤 노드를 포함하고 자식 노드들을 포함하지 않는 경우

func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)

	input()
	solve()
}

func input() {
	numOfNode := scanInt()

	weights = make([]int, numOfNode+1)
	for i := 1; i <= numOfNode; i++ {
		weights[i] = scanInt()
	}

	graph := make([][]int, numOfNode+1)
	for i := 0; i < numOfNode-1; i++ {
		nodeA, nodeB := scanInt(), scanInt()
		graph[nodeA] = append(graph[nodeA], nodeB)
		graph[nodeB] = append(graph[nodeB], nodeA)
	}

	tree = make([]node, numOfNode+1)
	initTree(graph, 0, 1)
}

func initTree(graph [][]int, parent, current int) {
	for _, adjacent := range graph[current] {
		if adjacent == parent {
			tree[current].parent = adjacent
			continue
		}
		initTree(graph, current, adjacent)
		tree[current].children = append(tree[current].children, adjacent)
	}
}

func solve() {
	memoWeights = make([]int, len(tree))
	memoCases = make([]cases, len(tree))
	memoization(1)

	elements = make([]int, 0)
	findElements(1)
	sort.Ints(elements)

	writer.WriteString(strconv.Itoa(memoWeights[1]) + "\n")
	for _, e := range elements {
		writer.WriteString(strconv.Itoa(e) + " ")
	}
}

func memoization(current int) {
	for _, child := range tree[current].children {
		memoization(child)
	}

	weightA, weightB := 0, weights[current]
	for _, child := range tree[current].children {
		weightA += memoWeights[child]

		for _, grandchild := range tree[child].children {
			weightB += memoWeights[grandchild]
		}
	}

	if weightA >= weightB {
		memoWeights[current] = weightA
		memoCases[current] = caseA
	} else {
		memoWeights[current] = weightB
		memoCases[current] = caseB
	}
}

func findElements(current int) {
	switch memoCases[current] {
	case caseA:
		for _, child := range tree[current].children {
			findElements(child)
		}
	case caseB:
		elements = append(elements, current)
		for _, child := range tree[current].children {
			for _, grandchild := range tree[child].children {
				findElements(grandchild)
			}
		}
	}
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

func scanInt() int {
	scanner.Scan()
	num := 0
	for _, c := range scanner.Bytes() {
		num = num * 10 + int(c - '0')
	}
	return num
}
