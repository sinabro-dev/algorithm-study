package main

import (
	"bufio"
	"os"
	"strconv"
)

type Queue struct {
	data []int
}

func (q *Queue) IsEmpty() bool {
	return len(q.data) == 0
}

func (q *Queue) Peek() int {
	front := q.data[0]

	if !q.IsEmpty() {
		q.data = q.data[1:]
	}

	return front
}

func (q *Queue) Enqueue(num int) {
	q.data = append(q.data, num)
}

// 정점의 연결 정보를 나타내는 구조체
type Tree struct {
	linkedNode []int
}

var (
	sc        *bufio.Scanner
	wr        *bufio.Writer
	nodeNum   int
	treeArr   []Tree
	depthArr  []int
	checkArr  []bool
	parentArr [][]int
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
	findParentAndDepth()
	printCommonParent()
}

// 정점의 연결 정보를 입력받아 저장하는 함수
func setting() {
	nodeNum = scanInt()
	treeArr = make([]Tree, nodeNum+1)

	for i := 0; i < nodeNum-1; i++ {
		node1, node2 := scanInt(), scanInt()
		treeArr[node1].linkedNode = append(treeArr[node1].linkedNode, node2)
		treeArr[node2].linkedNode = append(treeArr[node2].linkedNode, node1)
	}
}

// BFS 알고리즘을 이용하여 모든 정점의 부모 정점와 깊이를 구하는 함수
func findParentAndDepth() {
	q := Queue{}
	depthArr = make([]int, nodeNum+1)
	checkArr = make([]bool, nodeNum+1)
	parentArr = make([][]int, nodeNum+1)
	for i := 0; i < nodeNum+1; i++ {
		parentArr[i] = make([]int, 20)
	}

	q.Enqueue(1)
	depthArr[1] = 0
	checkArr[1] = true
	// parentArr[i][j] : i번 정점의 2^j번째 부모 정점
	parentArr[1][0] = 1

	for {
		if q.IsEmpty() {
			break
		}

		curNode := q.Peek()

		for _, node := range treeArr[curNode].linkedNode {
			if !checkArr[node] {
				q.Enqueue(node)
				depthArr[node] = depthArr[curNode] + 1
				checkArr[node] = true
				parentArr[node][0] = curNode
			}
		}
	}

	for i := 1; i < 20; i++ {
		for j := 1; j < nodeNum+1; j++ {
			// 어떤 정점의 2^i번째 부모 정점은, 그 정점의 2^(i-1)번째 부모 정점의 2^(i-1)번째 부모 정점
			parentArr[j][i] = parentArr[parentArr[j][i-1]][i-1]
		}
	}
}

func printCommonParent() {
	num := scanInt()

	for i := 0; i < num; i++ {
		node1, node2 := scanInt(), scanInt()
		wr.WriteString(strconv.Itoa(compareParent(node1, node2)) + "\n")
	}
}

// 두 정점 각각의 부모 정점을 비교하여 공통 조상을 찾는 함수
func compareParent(node1, node2 int) int {
	newNode1, newNode2 := node1, node2

	if depthArr[node1] > depthArr[node2] {
		newNode1, newNode2 = node2, node1
	}

	for i := 19; i >= 0; i-- {
		sub := depthArr[newNode2] - depthArr[newNode1]

		// 비트연산을 통해 깊이 차를 빠르게 구함
		if sub >= (1 << i) {
			newNode2 = parentArr[newNode2][i]
		}
	}

	if newNode1 == newNode2 {
		return newNode1
	} else {
		// LCA를 구할 때까지 반복
		for i := 19; i >= 0; i-- {
			if parentArr[newNode1][i] != parentArr[newNode2][i] {
				newNode1 = parentArr[newNode1][i]
				newNode2 = parentArr[newNode2][i]
			}
		}

		return parentArr[newNode1][0]
	}
}
