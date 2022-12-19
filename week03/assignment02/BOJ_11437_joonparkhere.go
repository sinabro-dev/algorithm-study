package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

type Node struct {
	depth int
	adjacent []int
}

const (
	maxNumOfVertex = 500000
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
	numOfVertex int
	log2NumOfVertex int
	tree []Node
	parent [][]int
)

func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)

	inputEdge()
	findParentAndDepth()
	findLCAVer2()
}

func scanInt() int {
	scanner.Scan()
	ret, _ := strconv.Atoi(scanner.Text())
	return ret
}

func inputEdge() {
	numOfVertex = scanInt()
	log2NumOfVertex = int(math.Ceil(math.Log2(float64(numOfVertex))))

	tree = make([]Node, numOfVertex + 1)
	parent = make([][]int, numOfVertex + 1)
	for i := range parent {
		parent[i] = make([]int, log2NumOfVertex)
		for j := range parent[i] {
			parent[i][j] = -1
		}
	}

	for i := 1; i < numOfVertex; i++ {
		idxA, idxB := scanInt(), scanInt()
		parent[idxA][0] = -1
		parent[idxB][0] = -1
		tree[idxA].adjacent = append(tree[idxA].adjacent, idxB)
		tree[idxB].adjacent = append(tree[idxB].adjacent, idxA)
	}
}

func findParentAndDepth() {
	queue := make([]int, 0)

	parent[1][0] = 0
	tree[1].depth = 0
	queue = append(queue, 1)

	for len(queue) > 0 {
		curIdx := queue[0]
		queue = queue[1:]
		for _, idx := range tree[curIdx].adjacent {
			// idx 에 해당하는 Node 의 parent 가 -1 이면 아직 방문을 하지 않았고, 그렇지 않으면 전에 방문을 했다는 의미
			if parent[idx][0] != -1 {
				continue
			}
			parent[idx][0] = curIdx
			tree[idx].depth = tree[curIdx].depth + 1
			queue = append(queue, idx)
		}
	}
}

// 이전 풀이 방법
func findLCAVer1() {
	numOfCase := scanInt()
	for i := 0; i < numOfCase; i++ {
		idxA, idxB := scanInt(), scanInt()
		depthA, depthB := tree[idxA].depth, tree[idxB].depth

		for depthA != depthB {
			if depthA < depthB {
				idxB = parent[idxB][0]
				depthB = tree[idxB].depth
			} else {
				idxA = parent[idxA][0]
				depthA = tree[idxA].depth
			}
		}

		for idxA != idxB {
			idxA = parent[idxA][0]
			idxB = parent[idxB][0]
		}
		writer.WriteString(strconv.Itoa(idxA) + "\n")
	}
}

func findLCAVer2() {
	findAllParent()

	numOfCase := scanInt()
	for i := 0; i < numOfCase; i++ {
		idxA, idxB := scanInt(), scanInt()
		if tree[idxA].depth < tree[idxB].depth {
			idxA, idxB = idxB, idxA
		}

		depthA, depthB := tree[idxA].depth, tree[idxB].depth
		gap := depthA - depthB

		for cnt := int(math.Ceil(math.Log2(maxNumOfVertex))); cnt != -1; cnt-- {
			if (gap & (1 << cnt)) != 0 {
				idxA = parent[idxA][cnt]
			}
		}

		if idxA != idxB {
			for cnt := log2NumOfVertex - 1; cnt >= 0; cnt-- {
				if (parent[idxA][cnt] != -1) && (parent[idxA][cnt] != parent[idxB][cnt]) {
					idxA = parent[idxA][cnt]
					idxB = parent[idxB][cnt]
				}
			}
			idxA = parent[idxA][0]
		}
		writer.WriteString(strconv.Itoa(idxA) + "\n")
	}
}

func findAllParent() {
	// 한 노드가 가질 수 있는 모든 부모들의 최대 개수는 트리의 높이 (log2NumOfVertex) 라고 할 수 있다.
	for cnt := 1; cnt < log2NumOfVertex; cnt++ {
		for idx := 2; idx <= numOfVertex; idx++ {
			if parent[idx][cnt - 1] == -1 {
				continue
			}
			parent[idx][cnt] =  parent[parent[idx][cnt - 1]][cnt - 1]
		}
	}
}