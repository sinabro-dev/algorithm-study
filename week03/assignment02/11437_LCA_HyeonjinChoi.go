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

// 정점의 부모 정점과 깊이를 저장하기 위한 구조체
type Node struct {
	parentNode int
	depth      int
}

var (
	sc       *bufio.Scanner
	wr       *bufio.Writer
	nodeNum  int
	treeArr  []Tree
	nodeArr  []Node
	checkArr []bool
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
	nodeArr = make([]Node, nodeNum+1)
	checkArr = make([]bool, nodeNum+1)
	q.Enqueue(1)
	nodeArr[1] = Node{0, 0}
	checkArr[1] = true

	for {
		if q.IsEmpty() {
			break
		}

		curNode := q.Peek()

		for _, node := range treeArr[curNode].linkedNode {
			if !checkArr[node] {
				q.Enqueue(node)
				nodeArr[node] = Node{curNode, nodeArr[curNode].depth + 1}
				checkArr[node] = true
			}
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
	newNode1, newNode2 := compareDepth(node1, node2)

	for {
		if newNode1 == newNode2 {
			return newNode1
		} else {
			newNode1 = nodeArr[newNode1].parentNode
			newNode2 = nodeArr[newNode2].parentNode
		}
	}
}

// 두 정점 각각의 깊이를 비교하여 더 높은 정점이 낮은 정점의 깊이만큼 이동하는 함수
func compareDepth(node1, node2 int) (int, int) {
	newNode1, newNode2 := node1, node2

	if nodeArr[node1].depth > nodeArr[node2].depth {
		for i := 0; i < nodeArr[node1].depth-nodeArr[node2].depth; i++ {
			newNode1 = nodeArr[newNode1].parentNode
		}
	} else if nodeArr[node1].depth < nodeArr[node2].depth {
		for i := 0; i < nodeArr[node2].depth-nodeArr[node1].depth; i++ {
			newNode2 = nodeArr[newNode2].parentNode
		}
	}

	return newNode1, newNode2
}
