package main

import (
	"bufio"
	"os"
	"strconv"
)

/*
[커스텀 타입 및 전역 변수]
1. type Node
트리에서 연결된 노드들의 정보를 저장하기 위한 구조체이다.

2. distance
어떤 노드로부터 가장 경로가 긴 노드까지의 길이를 나타내는 변수이다.

3. endNode
트리의 루트 노드로부터 가장 경로가 긴 노드를 나타내는 변수이다.

[풀이 흐름]
1. connectNode()
부모 노드, 자식 노드, 가중치를 입력받아 서로 연결시킨다.
linkedArr[i] -> i번 노드와 연결된 노드들의 배열
costArr[i] -> i번 노드에 대한 간선 가중치들의 배열
linkedArr[i].inf[j], costArr[i].inf[j] ->
i번 노드와 linkedArr[i].inf[j]번 노드가 연결되어있고, 간선의 가중치는 costArr[i].inf[j]

2. findFarthestNode()
루트 노드로부터 가장 먼 노드를 우선 구하고 그 노드로부터 가장 먼 노드를 구한다면,
양 끝의 노드를 구할 수 있고 트리의 지름을 구할 수 있다.

findFarthestNode()는 DFS를 진행하면서 인자로 받은 노드로부터 경로가 가장 긴 노드를 구하는 함수이다.
전역변수 distance 에는 가중치 합의 최댓값을 저장하고, endNode 에는 그 때의 노드 값을 저장한다.
처음에 루트 노드로부터 가장 먼 노드를 구하고 reset()한 이후에 그 노드로부터 가장 먼 노드를 구한다.

3. reset()
DFS를 두 번 진행해야하는 문제이기 때문에 첫번째 DFS를 마친 이후에
가중치의 합을 저장한 distance 와 DFS를 진행할 때 사용한 visitArr[] 를 초기화시킨다.

[시간 복잡도]
1. connectNode()
(모든 노드의 개수) - 1만큼 입력을 받기 때문에 O(N)이다.

2. findFarthestNode()
DFS를 진행하면서 모든 연결된 노드를 탐색하기 때문에 O(N^2)이다.

3. reset()
visitArr()를 모두 탐색하므로 O(N)이다.

따라서 O(N) + O(N^2) + O(N)이므로, O(N^2)이다.
*/

type Node struct {
	inf []int
}

var (
	sc        *bufio.Scanner
	wr        *bufio.Writer
	size      int
	distance  int
	endNode   int
	visitArr  []bool
	linkedArr []Node
	costArr   []Node
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
	connectNode()
	findFarthestNode(1, 0)
	reset()
	findFarthestNode(endNode, 0)
	wr.WriteString(strconv.Itoa(distance))
}

func connectNode() {
	size = scanInt()
	visitArr = make([]bool, size+1)
	linkedArr = make([]Node, size+1)
	costArr = make([]Node, size+1)
	var parentNode, childNode, cost int
	distance = 0

	for i := 0; i < size-1; i++ {
		parentNode, childNode, cost = scanInt(), scanInt(), scanInt()
		linkedArr[parentNode].inf = append(linkedArr[parentNode].inf, childNode)
		costArr[parentNode].inf = append(costArr[parentNode].inf, cost)
		linkedArr[childNode].inf = append(linkedArr[childNode].inf, parentNode)
		costArr[childNode].inf = append(costArr[childNode].inf, cost)
	}
}

func findFarthestNode(curNode, cost int) {
	visitArr[curNode] = true

	if distance < cost {
		distance = cost
		endNode = curNode
	}

	for index, node := range linkedArr[curNode].inf {
		if !visitArr[node] {
			findFarthestNode(node, cost+costArr[curNode].inf[index])
		}
	}
}

func reset() {
	distance = 0

	for index, _ := range visitArr {
		visitArr[index] = false
	}
}
