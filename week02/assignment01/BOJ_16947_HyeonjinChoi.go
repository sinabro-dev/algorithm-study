package main

import (
	"bufio"
	"os"
	"strconv"
)

/*
[커스텀 타입 및 전역 변수]
1. type Stack
DFS를 진행할 때 사용하기 위한 자료구조이다.

2. checkPoint
어느 역부터 순환선인지 나타내기 위한 변수이다.

3. cycle[]
각 역에 부여된 값을 통해 순환선인지 판별하기 위한 배열이다.

[풀이 흐름]
1. connectNode()
역의 개수와 역과 역의 연결 정보를 입력받아 연결시킨다.

2. checkCycle()
1번 역부터 시작하여 연결된 역을 탐색하며 cycle[]에 1씩 증가하는 수인
separateNum 을 부여한다. separateNum 의 초기값은 1이다.
DFS를 진행하며 연결된 역을 탐색할 때 4가지 경우가 생길 수 있다.

1) 연결된 역의 cycle[] 값이 0보다 크고, 탐색한 역과 연결된 역의 cycle[] 값의 차가 1보다 크다.
2) 연결된 역의 cycle[] 값이 0보다 크지만, 탐색한 역과 연결된 역의 cycle[] 값의 차가 1보다 크지 않다.
3) 연결된 역의 cycle[] 값이 0이다.
4) 연결된 역의 cycle[] 값이 0보다 작다.

1)의 경우 방문한 역을 만난 것이고 노드가 최소 3개 이상이어야함을 만족한다.
이때 방문한 역이 부여받은 수보다 큰 값을 갖는 역들은 모두 순환선에 속하는 것으로 간주한다.
예) 1-2-3-4-5 순으로 수를 부여받은 상태에서 5를 부여받은 역이 다음에 2를 부여받은 역과 연결된다면,
checkPoint 값은 2가 되고 checkPoint 이상의 값을 갖는 역들은 순환선에 속한 것이다.
2)의 경우 cycle[] 값의 차가 1이라는 것은 이전 역을 탐색했다는 것을 의미한다.
3)의 경우 탐색해야할 역으로 스택에 저장하여 DFS를 이어서 진행한다.
4)의 경우 cycle[] 값이 -1인데, 이것은 더이상 탐색할 역이 존재하지 않을 경우 부여되는 값으로
-1을 부여받고 스택에서 빠져나오며 DFS를 이어서 진행한다.

3-1. printDistance()
모든 역을 돌면서 순환선과의 거리를 출력한다.

3-2. findDistance()
인자로 받은 역과 순환선 사이의 거리를 구한다.
순환선에 속한 역의 cycle[] 값은 checkPoint 이상의 값을 갖기 때문에
조건을 만족하면 바로 반환하고, 만족하지 못하면 DFS를 이어서 진행한다.

[시간 복잡도]
1. connectNode()
역의 개수만큼 입력받기 떄문에 O(N)이다.

2. checkCycle()
모든 역에 대한 DFS를 진행하기 때문에 O(N^2)이다.

3-1. printDistance()
역의 개수만큼 출력하기 때문에 O(N)이다.

3-2. findDistance()
모든 역에 대한 DFS를 진행하기 때문에 O(N^2)이다.

따라서 O(N) + O(N^2) + O(N) * O(N^2)이므로, O(N^3)이다.
*/

type Stack struct {
	data []int
}

func (s *Stack) IsEmpty() bool {
	return len(s.data) == 0
}

func (s *Stack) Peek() int {
	if !s.IsEmpty() {
		return s.data[len(s.data)-1]
	} else {
		return -1
	}
}

func (s *Stack) Pop() {
	if !s.IsEmpty() {
		s.data = s.data[0 : len(s.data)-1]
	}
}

func (s *Stack) Push(num int) {
	s.data = append(s.data, num)
}

var (
	sc         *bufio.Scanner
	wr         *bufio.Writer
	size       int
	checkPoint int
	linkedArr  []Stack
	visitArr   []bool
	cycle      []int
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
	checkCycle(1)
	printDistance()
}

func connectNode() {
	var num1, num2 int
	size = scanInt()
	linkedArr = make([]Stack, size+1)
	visitArr = make([]bool, size+1)
	cycle = make([]int, size+1)

	for i := 0; i < size; i++ {
		num1, num2 = scanInt(), scanInt()
		linkedArr[num1].Push(num2)
		linkedArr[num2].Push(num1)
	}
}

func checkCycle(start int) {
	var empty bool
	separateNum := 1
	s := Stack{}
	s.Push(start)

	for {
		top := s.Peek()
		cycle[top] = separateNum
		separateNum++
		empty = true

		for _, node := range linkedArr[top].data {
			if cycle[node] > 0 && cycle[top]-cycle[node] > 1 {
				checkPoint = cycle[node]
				return
			} else if cycle[node] == 0 {
				s.Push(node)
				empty = false
				break
			}
		}

		if empty {
			cycle[top] = -1
			separateNum -= 2
			s.Pop()
		}
	}
}

func printDistance() {
	for i := 1; i < size+1; i++ {
		wr.WriteString(strconv.Itoa(findDistance(i)) + " ")
		reset()
	}
}

func findDistance(node int) int {
	var empty bool
	count := 0
	s := Stack{}
	s.Push(node)

	for {
		top := s.Peek()
		visitArr[top] = true
		empty = true

		if cycle[top] >= checkPoint {
			return count
		} else {
			for _, node := range linkedArr[top].data {
				if visitArr[node] {
					continue
				} else {
					s.Push(node)
					count++
					empty = false
					break
				}
			}
		}

		if empty {
			count--
			s.Pop()
		}
	}
}

func reset() {
	for index, _ := range visitArr {
		visitArr[index] = false
	}
}
