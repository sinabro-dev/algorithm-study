package main

import (
	"bufio"
	"os"
	"strconv"
)

/*
[커스텀 타입 및 전역 변수]
1. NodeInfo 구조체
트리의 각 노드마다 연결된 노드에 대한 정보를 나타낸다.
nextIdx 는 인접한 노드의 index 값이고, weight 는 연결된 간선의 가중치이다.

2. tree 2차원 슬라이스
입력받은 노드들의 관계 (트리) 를 나타내는 NodeInfo 타입의 2차원 슬라이스이다.
예를 들어 tree[1] = {{2, 5}, {3, 6}} 이라면,
index 가 1인 노드에 인접한 노드들은 index 가 2 와 3 인 노드이고, 각각 연결된 간선의 가중치는 5 과 6 이다.

3. treeDiameter
문제에서 요구하는 트리의 지름을 저장할 변수이다.

[풀이 흐름]
1. generateTree()
입력받은 노드들의 관계를 토대로 tree 를 구성한다.

2. for idx, adjacent := range tree {...}
tree 의 모든 노드들을 훑으면서 각 노드와 인접한 노드들에 대해 DFS 를 수행시킨다.
이때 트리의 지름 양 끝 점은 인접한 노드의 수가 1개인 노드일 수 밖에 없다.

3. dfsVisit(pIsVisit *[]bool, curIdx int, curWeight int)
- pIsVisit *[]bool: 각 노드를 방문했는지 기록하기 위한 슬라이스
- curIdx int: 현재 훑고있는 노드의 index 값
- curWeight int: 현재까지 훑어온 간선들의 가중치 총합
DFS 를 수행하며 아직 훑지 않은 노드들에 접근한다.
이때도 마찬가지로, 인접한 노드의 수가 1개인 노드만이 트리 지름의 끝 점이 될 수 있으므로,
해당 조건을 만족할 때 treeDiameter 값을 Update 할 수 있다.
모든 노드를 훑고나면 treeDiameter 값에 최댓값이 저장되어 있을 것이므로, 출력하면 문제의 답을 구할 수 있다.

[시간 복잡도]
1. generateTree()
vertex 수만큼 반복한다. O(V)

2-1. for idx, adjacent := range tree { ... }
모든 vertex 를 훑는다. O(V)

2-2. dfsVisit()
vertex 중에서도 인접한 vertex 수가 1개인 vertex 에 한해서 호출된다.
해당 vertex 를 기점으로 모든 vertex 에 대해서 edge 를 훑으므로 O(V+E) 이다.

결국 O(V) + O(V) * O(V+E) 이므로, O(V^2) 이다.
 */

type NodeInfo struct {
	nextIdx int
	weight int
}

var (
	sc           *bufio.Scanner
	wr           *bufio.Writer
	tree         [][]NodeInfo
	treeDiameter int
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
	generateTree(scanInt())
	numOfNode := len(tree)
	for idx, adjacent := range tree {
		if len(adjacent) == 1 {
			isVisit := make([]bool, numOfNode)
			dfsVisit(&isVisit, idx, 0)
		}
	}
	wr.WriteString(strconv.Itoa(treeDiameter))
}

func generateTree(numOfNode int) {
	tree = make([][]NodeInfo, numOfNode + 1)
	for i := 1; i < numOfNode; i++ {
		parentIdx, childIdx, weight := scanInt(), scanInt(), scanInt()
		tree[parentIdx] = append(tree[parentIdx], NodeInfo{nextIdx: childIdx, weight: weight})
		tree[childIdx] = append(tree[childIdx], NodeInfo{nextIdx: parentIdx, weight: weight})
	}
}

func dfsVisit(pIsVisit *[]bool, curIdx int, curWeight int) {
	(*pIsVisit)[curIdx] = true

	adjacent := tree[curIdx]
	if len(adjacent) == 1 && curWeight != 0 {
		if curWeight > treeDiameter {
			treeDiameter = curWeight
		}
		return
	}

	for _, nodeInfo := range adjacent {
		if !(*pIsVisit)[nodeInfo.nextIdx] {
			dfsVisit(pIsVisit, nodeInfo.nextIdx, curWeight + nodeInfo.weight)
		}
	}
}