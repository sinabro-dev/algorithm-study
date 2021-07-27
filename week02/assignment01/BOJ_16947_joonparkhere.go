package main

import (
	"bufio"
	"os"
	"strconv"
)

/*
[커스텀 타입 및 전역 변수]
type color 는 그래프 탐색할 때 각 정점의 방문 현황을 나타낸다.
아직 탐색 전 (white), 탐색 중 (grey), 탐색 완료 (black) 으로 표현한다.

2차원 슬라이스는 adjacent 는 그래프를 표현하는 자료 구조이다.
예를 들어 adjacent[0] = {1, 2} 이면 index 0인 정점의 인접한 정점은 index 1과 2인 정점임을 나타낸다.

슬라이스 memo 는 index 가 정점을 가르키며, 해당 정점이 cycle 과의 떨어진 거리를 나타낸다.
사이클에 속하는 정점이면 해당 정점을 index 로 하는 memo 값은 0이 될 것이다.

[풀이 흐름]
1. generateAdjacent()
정점의 개수와 간선을 입력받아, adjacent 슬라이스에 기록한다.

2. initMemo()
본격적으로 풀이를 하기 전, memo 슬라이스의 각 값들을 초기화한다. 초기화 값은 가능한 최댓값인 정점의 개수로 한다.

3. recordCycleByMemoization()
DFS 로 사이클을 찾는다.
이때 정점 방문 여부를 기록할 슬라이스 info 와 추후 사이클 판단할 때 사용하기 위해 각 정점의 부모 노드를 기록할 슬라이스 parent 를 활용한다.
DFS 도중, 인접한 정점의 color 가 grey 이고, 부모 정점도 아니라면 사이클이 존재함을 의미한다.
사이클을 탐지한 순간, 슬라이스 parent 에 기록된 것의 역순서로 되돌아가면서 각 정점을 index 로 하는 슬라이스 memo 값을 0으로 변경한다.

4. findDistanceFromCycle()
사이클에 속하지 않는 정점이 얼마나 사이클로부터 떨어져 있는 지를 DFS 를 이용해 구한다.
이때 사이클과 떨어진 거리가 1인 (코드 상에서는 분기-fork-라고 표현) 정점을 찾아서 슬라이스 fork 에 기록한다.
기록된 분기점이 시작점이 되어 DFS 를 시작한다.
각 정점을 방문할 때마다 인접한 정점를 index 로 하는 슬라이스 memo 값을 변경한다.

5. memo 출력
4번까지 과정을 마치면 모든 정점을 index 로 하는 슬라이스 memo 값이 정상 반영된 것이다.
이를 출력하면 풀이가 끝난다.

[시간 복잡도]
main() 함수에서 generateAdjacent() 와 solve() 를 차례로 호출하므로 각 함수들의 시간 복잡도를 먼저 살펴보자.

1. generateAdjacent() 함수
vertex 수만큼 반복한다. O(V)

2. solve() - initMemo() 함수
vertex 수만큼 반복한다. O(V)

3. solve() - recordCycleByMemoization() 함수
가장 상위의 반복문은 dfsWithMemo() 함수를 호출한다.
dfsWithMemo() 함수에서도 반복문을 도는데, 두 반복문은 결국 모든 vertex 를 훑는 것이 목적이므로 O(V) 이다.
그리고 특정 경우 (사이클 탐지) 에 memoCycle() 함수를 호출한다.
memoCycle() 함수는 사이클을 이루는 vertex 수만큼 반복 호출이 된다. 모든 vertex 가 사이클에 속한다면, 최대 O(V) 이다.
따라서  O(V^2) 만큼 소요한다.

4. solve() - findDistanceFromCycle() 함수
fork 를 찾는 반복문에서 모든 vertex 를 훑으므로 O(V) 이다.
그리고 BFS 를 하는 부분은 모든 vertex 와 edge 를 훑으므로 O(V+E) 이다.

결국 O(V) + O(V) + O(V^2) + O(V+E) 이다. 이때 문제에서 vertex 수와 edge 수는 같으므로,
최종 시간복잡도는 O(V^2) 이다.
 */

var (
	sc *bufio.Scanner
	wr *bufio.Writer
	adjacent [][]int
	memo []int
)

type color int

const (
	white = color(0)
	grey = color(1)
	black = color(2)
)

type vertex struct {
	state color
	distance int
}

func init() {
	sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	wr = bufio.NewWriter(os.Stdout)
}

func scanInt() (num int) {
	sc.Scan()
	num, _ = strconv.Atoi(sc.Text())
	return
}

func main() {
	defer wr.Flush()
	generateAdjacent(scanInt())
	solve()
}

func generateAdjacent(numOfVertex int) {
	adjacent = make([][]int, numOfVertex)
	for i := 0; i < numOfVertex; i++ {
		idx1 := scanInt() - 1
		idx2 := scanInt() - 1
		adjacent[idx1] = append(adjacent[idx1], idx2)
		adjacent[idx2] = append(adjacent[idx2], idx1)
	}
}

func solve() {
	initMemo()
	recordCycleByMemoization()
	findDistanceFromCycle()
	for _, value := range memo {
		wr.WriteString(strconv.Itoa(value) + " ")
	}
}

func initMemo() {
	numOfVertex := len(adjacent)
	memo = make([]int, numOfVertex)
	for i := range memo {
		memo[i] = numOfVertex
	}
}

func recordCycleByMemoization() {
	colorType := make([]color, len(adjacent))
	parent := make([]int, len(adjacent))

	for i := range adjacent {
		if colorType[i] == white {
			dfsWithMemo(&colorType, &parent, i)
		}
	}
}

func dfsWithMemo(pColorType *[]color, pParent *[]int, curIdx int) {
	colorType := *pColorType
	parent := *pParent
	colorType[curIdx] = grey

	for _, idx := range adjacent[curIdx] {
		if colorType[idx] == white {
			parent[idx] = curIdx
			dfsWithMemo(&colorType, &parent, idx)
		} else if (colorType[idx] == grey) && (idx != parent[curIdx]) {
			memoCycle(&parent, curIdx, idx)
		}
	}

	colorType[curIdx] = black
}

func memoCycle(pParent *[]int, curIdx, targetIdx int) {
	memo[curIdx] = 0
	if curIdx == targetIdx {
		return
	}
	memoCycle(pParent, (*pParent)[curIdx], targetIdx)
}

func findDistanceFromCycle() {
	fork := make([]int, 0)
	info := make([]vertex, len(adjacent))
	for i := range memo {
		if memo[i] == 0 {
			info[i].state = black
			continue
		}
		for _, j := range adjacent[i] {
			if memo[j] == 0 {
				fork = append(fork, i)
				break
			}
		}
	}

	queue := make(chan int, len(adjacent))
	for _, forkIdx := range fork {
		info[forkIdx].state = black
		info[forkIdx].distance = 1
		queue <- forkIdx
	}

	for ; len(queue) != 0; {
		curIdx := <- queue
		memo[curIdx] = info[curIdx].distance

		for _, idx := range adjacent[curIdx] {
			if info[idx].state == white {
				info[idx].state = black
				info[idx].distance = memo[curIdx] + 1
				queue <- idx
			}
		}
	}
}