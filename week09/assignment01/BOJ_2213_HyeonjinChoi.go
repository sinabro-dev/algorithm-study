package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

type Graph struct {
	node []int
}

var (
	sc        *bufio.Scanner
	wr        *bufio.Writer
	size      int
	weightArr []int
	graphArr  []Graph
	answerArr []int
	dpArr     [][]int
	visitArr  []bool
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
}

func setting() {
	size = scanInt()
	weightArr = make([]int, size+1)
	graphArr = make([]Graph, size+1)

	for i := 1; i <= size; i++ {
		weightArr[i] = scanInt()
	}

	for i := 1; i < size; i++ {
		node1, node2 := scanInt(), scanInt()
		graphArr[node1].node = append(graphArr[node1].node, node2)
		graphArr[node2].node = append(graphArr[node2].node, node1)
	}
}

func solve() {
	visitArr = make([]bool, size+1)
	dpArr = make([][]int, size+1)
	for i := 0; i <= size; i++ {
		dpArr[i] = make([]int, 2)
	}

	dfs(1)

	if dpArr[1][0] > dpArr[1][1] {
		tracking(-1, 1, 0)
		wr.WriteString(strconv.Itoa(dpArr[1][0]) + "\n")
	} else {
		tracking(-1, 1, 1)
		wr.WriteString(strconv.Itoa(dpArr[1][1]) + "\n")
	}

	printNode()
}

func dfs(cur int) {
	visitArr[cur] = true
	dpArr[cur][1] = weightArr[cur]

	for _, node := range graphArr[cur].node {
		if !visitArr[node] {
			dfs(node)
			dpArr[cur][0] += max(dpArr[node][0], dpArr[node][1])
			dpArr[cur][1] += dpArr[node][0]
		}
	}
}

func tracking(prev, cur, state int) {
	if state == 1 {
		answerArr = append(answerArr, cur)

		for _, node := range graphArr[cur].node {
			if node == prev {
				continue
			}

			tracking(cur, node, 0)
		}
	} else {
		for _, node := range graphArr[cur].node {
			if node == prev {
				continue
			}
			if dpArr[node][0] > dpArr[node][1] {
				tracking(cur, node, 0)
			} else {
				tracking(cur, node, 1)
			}
		}
	}
}

func printNode() {
	sort.Slice(answerArr, func(i, j int) bool {
		return answerArr[i] < answerArr[j]
	})

	for _, data := range answerArr {
		wr.WriteString(strconv.Itoa(data) + " ")
	}
}

func max(num1, num2 int) int {
	if num1 >= num2 {
		return num1
	} else {
		return num2
	}
}
