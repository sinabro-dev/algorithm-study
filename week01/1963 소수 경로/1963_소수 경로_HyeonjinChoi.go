package main

import "fmt"

func sieve_of_eratosthenes(prime *[10000]int) {
	/*
		대량의 소수를 빠르게 구하기 위해
		에라토스테네스의 체 알고리즘 사용
	*/
	for i := 2; i < 10000; i++ {
		if prime[i] != 0 {
			for j := i * 2; j < 10000; j += i {
				prime[j] = 0
			}
		}
	}
}

// 큐 구현
type Queue struct {
	data []int
}

func (q *Queue) is_empty() bool {
	return len(q.data) == 0
}
func (q *Queue) peek() int {
	return q.data[0]
}
func (q *Queue) enqueue(num int) {
	q.data = append(q.data, num)
}
func (q *Queue) dequeue() {
	if !q.is_empty() {
		q.data = q.data[1:]
	}
}

func change_digit(baseNum int, digit int, position int) int {
	/*
		수의 한 자릿수를 변경하는 함수
	*/
	temp := baseNum
	pow := 1

	for i := 0; i < position-1; i++ {
		baseNum /= 10
		pow *= 10
	}
	value := baseNum % 10

	return temp - (value * pow) + (digit * pow)
}

func bfs(start int, prime *[10000]int, check *[10000]int) {
	/*
		bfs를 이용하여 한 자릿수씩 바꿔가며
		주어진 소수에서 바뀐 소수로 이동한 횟수를
		check 배열에 저장하는 함수
	*/
	q := Queue{}
	q.enqueue(start)
	check[start] = 0
	var nextPrime int

	for {
		// 만약 큐가 비어있다면 반복문 종료
		if q.is_empty() {
			break
		}

		// 현재 큐에 저장된 소수
		curPrime := q.peek()
		q.dequeue()

		// 한 자릿수씩 바꾸며 조건에 부합하는 소수 큐에 저장, check 배열에 이동횟수 저장
		for i := 4; i > 0; i-- {
			for j := 0; j < 10; j++ {
				nextPrime = change_digit(curPrime, j, i)
				if nextPrime >= 1000 && prime[nextPrime] != 0 && check[nextPrime] == -1 {
					check[nextPrime] = check[curPrime] + 1
					q.enqueue(nextPrime)
				}
			}
		}
	}
}

func main() {

	var times int

	// 횟수 입력
	fmt.Scan(&times)

	for i := 0; i < times; i++ {
		// 시작, 끝 소수 입력
		var startValue int
		var endValue int

		fmt.Scan(&startValue)
		fmt.Scan(&endValue)

		// 소수, 이동횟수 저장할 배열 생성
		var prime [10000]int
		var check [10000]int

		for j := 2; j < 10000; j++ {
			prime[j] = j
		}
		for j := 0; j < 10000; j++ {
			check[j] = -1
		}

		// 에라토스테네스의 체를 이용하여 소수만 남기고 0으로 초기화
		sieve_of_eratosthenes(&prime)

		// bfs를 이용하여 주어진 소수에서 각 소수까지 이동횟수 구하기
		bfs(startValue, &prime, &check)

		// check 배열에서 찾으려는 소수의 배열값이 -1이면 주어진 수에서 변환 불가능한 것으로 간주
		if check[endValue] != -1 {
			fmt.Printf("%d\n", check[endValue])
		} else {
			fmt.Printf("Impossible\n")
		}
	}
}
