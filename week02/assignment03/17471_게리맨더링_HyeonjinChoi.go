package main

import "fmt"

/*
[커스텀 타입 및 전역 변수]
1. type Queue
같은 선거구인 구역들이 모두 연결되어있는지 확인할 떄 사용하기 위한 자류구조, 큐이다.

2. index
배열을 참조하는 과정에서 조건에 충족하는 값의 인덱스를 나타내기 위한 변수로서, 체크포인트이다.

[풀이 흐름]
1. connectNode()
구역의 수와 각 구역의 인구, 그리고 인접한 구역의 정보들을 입력받고 각 구역을 연결한다.
population[i] -> i번 구역의 인구
graphArr[i][j] -> i번 구역과 j번 구역의 연결 여부

2-1. findMinDiff()
선거구는 두 개밖에 존재하지 않는다는 사실을 이용하여, 전체 구역의 수를 이진법으로 활용하는 방식을 사용한다.

반복문을 통해 1부터 시작하여 (전체 구역의 수)^2 - 1의 값까지 이진수로 바꾸어 groupArr[] 에 저장하고,
isConnected() 를 통해 0과 1로 나누어진 구역들이 서로 연결되어있는지 판별한다.
두 선거구는 각각 0 또는 1의 값을 갖는 것으로 간주한다.

체크포인트 역할인 index 값으로 해당 회차에서 같은 선거구 내 구역들이 모두 연결되었는지 판별한다.
모두 연결되었다면,
반복문을 모두 돌아 index 값이 모든 구역의 수보다 커지게 되고 다음 조건문을 실행한다.
연결되지 않은 구역이 있다면,
반복문 중간에 탈출하여 index 값이 모든 구역의 수보다 작게 되고 다음 조건문을 넘어간다.

다음 조건문은 두 선거구의 인구 차를 구한다.
0 값을 갖는 선거구는 + 값을, 1 값을 갖는 선거구는 - 값을 sum 값에 더한다.
이후 answer 에 대입하여 반복문이 끝날 때까지 sum 의 절댓값 중 더 큰 값으로 갱신한다.

answer 값이 1001(초기값)이 아니면, 그대로 반환하고
1001이면, -1을 반환한다.

2-2. isConnected()
0 또는 1의 인자를 받았을 때, 해당 값을 갖는 같은 선거구 내 모든 구역이 연결되어있는지 판별한다.

같은 선거구이면서 방문하지 않았고 연결되어있다면 visitArr[] 값이 true로 전환된다.
findMinDiff() 에서 0, 1을 각각 인자로 사용하여 함수를 실행시켜서 visitArr[] 의 모든 값을 true로 전환한다.
만약 false 값이 존재한다면 모두 연결된 것이 아닌 것으로 판별한다.

[시간 복잡도]
1. connectNode()
구역의 수만큼 반복하여 입력 받기 때문에 O(N)이다.

2-1. findMinDiff()
구역의 수만큼 자릿수를 갖는 이진수를 돌아야하기 때문에 O(2^N + (iConnected() 의 시간복잡도))이다.

2-2. isConnected()
큐가 비어있을 때까지 모든 구역을 돌며 visitArr[] 을 확인하기 때문에 O(N^2)이다.

따라서 O(N) + O(2^N) + O(N^2)이므로, O(2^N)이다.
*/

type Queue struct {
	data []int
}

func (q *Queue) isEmpty() bool {
	return len(q.data) == 0
}
func (q *Queue) peek() int {
	front := q.data[0]

	if !q.isEmpty() {
		q.data = q.data[1:]
	}

	return front
}
func (q *Queue) enqueue(num int) {
	q.data = append(q.data, num)
}

var (
	size          int
	min           int
	index         int
	populationArr []int
	graphArr      [][]bool
	groupArr      []int
	visitArr      []bool
)

func main() {
	connectNode()
	fmt.Println(findMinDiff())
}

func connectNode() {
	fmt.Scan(&size)
	populationArr = make([]int, size+1)
	groupArr = make([]int, size+1)
	visitArr = make([]bool, size+1)
	graphArr = make([][]bool, size+1)

	for i := 0; i < size+1; i++ {
		graphArr[i] = make([]bool, size+1)
	}

	for i := 1; i < size+1; i++ {
		fmt.Scan(&populationArr[i])
	}

	for i := 1; i < size+1; i++ {
		var count, linkedNode int
		fmt.Scan(&count)

		for j := 0; j < count; j++ {
			fmt.Scan(&linkedNode)
			graphArr[i][linkedNode] = true
			graphArr[linkedNode][i] = true
		}
	}
}

func findMinDiff() int {
	answer := 1001
	times := 1

	for times != pow(size)-1 {
		num := times

		for i := 1; i < size+1; i++ {
			groupArr[i] = num % 2
			num /= 2
			visitArr[i] = false
		}
		fmt.Println("g(b):", groupArr) //test
		isConnected(0)
		isConnected(1)
		fmt.Println("g(a):", groupArr) //test
		fmt.Println("v:", visitArr)    //testtt
		for index = 1; index < size+1; index++ {
			if !visitArr[index] {
				break
			} else {
			}
		}

		if index > size {
			sum := 0

			for i := 1; i < size+1; i++ {
				if groupArr[i] == 0 {
					sum += populationArr[i]
				} else {
					sum -= populationArr[i]
				}
			}

			if answer > absoluteValue(sum) {
				answer = absoluteValue(sum)
			}
		}

		times++
	}

	if answer != 1001 {
		return answer
	} else {
		return -1
	}
}

func isConnected(digit int) {
	q := Queue{}

	for index = 1; index < size+1; index++ {
		if groupArr[index] == digit {
			break
		} else {
		}
	}

	q.enqueue(index)
	visitArr[index] = true

	for !q.isEmpty() {
		curPos := q.peek()

		for i := 1; i < size+1; i++ {
			if groupArr[i] == digit && !visitArr[i] && graphArr[i][curPos] {
				q.enqueue(i)
				visitArr[i] = true
			}
		}
	}
}

func pow(times int) int {
	answer := 1

	for i := 0; i < times; i++ {
		answer *= 2
	}

	return answer
}

func absoluteValue(num int) int {
	if num >= 0 {
		return num
	} else {
		return -num
	}
}
