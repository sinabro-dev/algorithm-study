package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

/*
[커스텀 타입 및 전역 변수]
1. type dummy
Golang 에서 Set 자료 구조를 사용하려면 map 을 이용해야 하는데, Set 자료 구조를 사용할 때는 map 의 key-value 에서 value 값은 필요 없는 값이다.
따라서 비어 있는 구조체 (dummy) 를 value 자료형으로 설정해서 메모리 낭비를 줄였다.

2. answer
문제에서 요구한 두 선거구간의 인구 차이 최솟값을 기록할 변수이다.

[풀이 흐름]
1. setPopulationAndGraph()
먼저 각 구역의 인구 수와 구역 간의 관계를 세팅한다.
이때 구역 간의 관계는 2차원 슬라이스 graph 로 표현한다.
예를 들어 graph[0] = {1, 3} 이면 첫번째 구역의 인접한 구역들은 두번째와 네번째 구역이다.

2-1. solve()
문제 풀이의 주요 표인트는 비트 연산으로 가능한 경우들을 처리한 것이다.
예를 들어 총 구역의 수가 4개라면, 0000 0001 0010 0011 ... 1111 이 표현가능하고,
네 자리의 각 자리가 구역을, 0 또는 1을 선거구을 표현한다고 생각하면 구역들을 두 가지 선거구로 나누는 모든 경우들을 표현할 수 있다.
0110 인 경우에는 구역 A 와 D 가 하나의 선거구, 구역 B 와 C 가 또 다른 선거구를 구성한다.
이렇게 먼저 선거구를 나누어 보고, 각 선거구에 속한 구역들이 연결되어 있는지 DFS 로 확인하는 흐름이다.

우선 answer 값을 최댓값인 최대 구역의 수 * 최대 인구수로 초기화한다.
그리고 각 구역들이 선거구 두 곳 중 어느 곳에 속할 지 나타내는 경우의 수는 2^(구역 개수) 이다.
numOfCase 가 비트 연산을 통해 가능한 경우의 수를 표현한다.
이후 00...0 인 경우와 11...1 인 경우, 즉 모든 구역이 하나의 선거구에 속하는 경우는 문제의 답이 될 수 없으므로 양 끝 경우는 제외하고 반복문을 돌며 check() 함수를 호출한다.

2-2. check(curCase int)
- curCase 는 00110...101 등과 같은 비트로 표현된 경우를 가르킨다.
먼저 선거구 A 와 B 의 인구수를 표현할 변수와 포함되는 구역을 기록할 Set 을 선언한다.
그리고 구역 수만큼 반복을 돌면서 curCase 에서 각 구역이 어는 선거구에 속하는지 확인하고 (비트 연산을 통해) 해당 선거구의 인구수와 Set 을 Update 한다.
예를 들어 총 구역의 수가 4개이고, curCase 가 0110 일 때  만약 i 값이 1 이면 area 값은 2^1 가 된다.
그리고 0110 (curCase) 와 0010 (area) 를 AND 연산해서 만약 연산 결과가 0 이 아니라면 area 가 curCase 의 1에 해당하는 선거구에 속하는 것이고, 0 이면 curCase 의 0에 해당하는 선거구에 속하는 것이다.
0110 & 0010 = 0010 이므로 선거구 A 에 속함을 알 수 있다. 만약 area 가 1000 이었다면, 0110 & 1000 = 0000 이므로 선거구 B 에 속할 것이다.
이 과정을 구역 수만큼 반복하면 각 구역이 두 선거구 중 어느 한 곳에 속하게 된다.

이후 두 선거구에 대해 dfs() 를 호출하면서 해당 선거구에 속한 구역들이 모두 연결되어 있는지 확인한다. (어느 한 구역을 시작으로 DFS 를 했을 때 훑지 못한 구역이 있다면 연결되어 있지 않음을 이용)
만약 연결되어 있지 않으면 check() 함수를 종료시켜 다음 curCase 로 넘어가고, 연결되어 있으면 두 선거구 인구 수 차를 계산 후 현재까지 최솟값이면 answer 를 Update 한다.

모든 경우에 대해 check() 함수 호출이 마무리되면, answer 변수에 저장된 값이 인구수 차의 최솟값이 된다.

[시간 복잡도]
1. setPopulationAndGraph()
인구수 저장을 위해 vertex 수만큼 반복하고, 구역 간의 관계를 기록하기 위해 edge 수만큼 반복하므로, O(V+E) 이다.

2-1. for curCase := 1; curCase+ 1 < numOfCase; curCase++ { ... }
가능한 경우의 수는 2^(vertex 수) 이므로, O(2^V) 이다.

2-2 check()
먼저 vertex 수만큼 반복해서 선거구를 나누므로, O(V) 만큼 소요한다.
그리고 DFS 를 하면서 각 선거구에 속한 vertex 와 edge 를 훑는다. O(V+E)

결국 O(V+E) + O(2^V) * O(V+E) 이므로, O(V * 2^V) 이다.
 */

type dummy struct {}

const (
	maxNumOfArea = 10
	maxPopulation = 100
)

var (
	sc *bufio.Scanner
	wr *bufio.Writer
	answer int
	numOfArea int
	population []int
	graph [][]int
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
	setPopulationAndGraph(scanInt())
	solve()
}

func setPopulationAndGraph(n int) {
	numOfArea = n

	population = make([]int, numOfArea)
	for i := range population {
		population[i] = scanInt()
	}

	graph = make([][]int, numOfArea)
	for i := range graph {
		graph[i] = make([]int, scanInt())
		for j := range graph[i] {
			graph[i][j] = scanInt() - 1
		}
	}
}

func solve() {
	answer = maxNumOfArea * maxPopulation
	numOfCase := 1 << len(population)
	for curCase := 1; curCase+ 1 < numOfCase; curCase++ {
		check(curCase)
	}
	if answer == maxNumOfArea * maxPopulation {
		wr.WriteString(strconv.Itoa(-1))
	} else {
		wr.WriteString(strconv.Itoa(answer))
	}
}

func check(curCase int) {
	populationA := 0
	populationB := 0
	districtA := map[int]dummy{}
	districtB := map[int]dummy{}

	for i := 0; i < numOfArea; i++ {
		area := 1 << i
		if area & curCase != 0 {
			districtA[i] = dummy{}
			populationA += population[i]
		} else {
			districtB[i] = dummy{}
			populationB += population[i]
		}
	}

	isVisit := map[int]dummy{}
	firstArea := getFirstInSet(&districtA)
	isVisit[firstArea] = dummy{}
	dfs(firstArea, &districtA, &isVisit)
	if !isAllAreaConnected(&districtA, &isVisit) {
		return
	}

	isVisit = map[int]dummy{}
	firstArea = getFirstInSet(&districtB)
	isVisit[firstArea] = dummy{}
	dfs(firstArea, &districtB, &isVisit)
	if !isAllAreaConnected(&districtB, &isVisit) {
		return
	}

	result := int(math.Abs(float64(populationA - populationB)))
	if result < answer {
		answer = result
	}
}

func isAllAreaConnected(pStrict *map[int]dummy, pIsVisit *map[int]dummy) bool {
	for element := range *pStrict {
		if !isExistInSet(element, pIsVisit) {
			return false
		}
	}
	return true
}

func dfs(curArea int, pDistrict *map[int]dummy, pIsVisit *map[int]dummy) {
	for _, adjacentArea := range graph[curArea] {
		if !isExistInSet(adjacentArea, pIsVisit) && isExistInSet(adjacentArea, pDistrict) {
			(*pIsVisit)[adjacentArea] = dummy{}
			dfs(adjacentArea, pDistrict, pIsVisit)
		}
	}
}

func getFirstInSet(pSet *map[int]dummy) int {
	for element := range *pSet {
		return element
	}
	return -1
}

func isExistInSet(element int, pSet *map[int]dummy) bool {
	_, ok := (*pSet)[element]
	return ok
}