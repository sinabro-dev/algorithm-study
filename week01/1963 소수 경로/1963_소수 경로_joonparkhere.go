package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

type Node struct {
	isVisit bool
	value int
	pathLen int
}

type Queue []*Node

func (q *Queue) IsEmpty() bool {
	return len(*q) == 0
}

func (q *Queue) Push(value *Node) {
	*q = append(*q, value)
}

func (q *Queue) Pop() *Node {
	if q.IsEmpty() {
		return nil
	}
	node := (*q)[0]
	*q = (*q)[1:]

	return node
}

const (
	maxNumber = 9999
	minNumber = 1000
)

var (
	sc *bufio.Scanner
	wr *bufio.Writer
	primeNumbers []int
)

func init() {
	sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)

	wr = bufio.NewWriter(os.Stdout)
}

func main() {
	defer wr.Flush()
	numOfCase := scanInt()
	primeNumbers = findPrimeNumbers()
	for i := 0; i < numOfCase; i++ {
		result := solve(scanInt(), scanInt())
		if result == -1 {
			wr.WriteString("Impossible\n")
		} else {
			wr.WriteString(strconv.Itoa(result) + "\n")
		}
	}
}

func findPrimeNumbers() (result []int) {
	/*
		에라토스테네스의 체를 이용한 소수 찾기 과정
		범위 내의 최대 수까지 배열을 할당하고 배열 값은 각 index 와 동일하게 세팅
		소수가 아닌 경우 해당 수를 가리키는 index 의 배열 값은 0으로 Update
	*/
	arr := make([]int, maxNumber+ 1)
	for i := range arr {
		arr[i] = i
	}

	for i := 2; i <= maxNumber; i++ {
		// 소수가 아닌 경우에는 다음 반복으로 넘어감
		if arr[i] == 0 {
			continue
		}
		// 소수라면 해당 수의 배수들은 소수가 아니므로 배열 값 Update
		for j := i * 2; j <= maxNumber; j += i {
			arr[j] = 0
		}
	}

	// 네 자리 숫자 중에서 소수인 수를 골라서 배열에 저장
	for i := minNumber; i <= maxNumber; i++ {
		if arr[i] == i {
			result = append(result, i)
		}
	}
	return
}

func solve(beginValue, endValue int) (result int) {
	/*
	처음 비밀번호에서 목표로 하는 비밀번호까지 바꾸는 데 필요한 최소 횟수를 구하는 과정
	BFS 를 이용
	 */

	// 목표 비밀번호가 현재와 같은 경우 예외 처리
	if beginValue == endValue {
		return 0
	}

	// BFS 할 때 필요한 데이터들을 기록하는 배열
	nodes := make([]Node, maxNumber + 1)
	for _, number := range primeNumbers {
		nodes[number].isVisit = false
		nodes[number].value = number
		nodes[number].pathLen = maxNumber
	}

	queue := Queue{}

	startNode := nodes[beginValue]
	startNode.isVisit = true
	startNode.pathLen = 0

	queue.Push(&startNode)

	for ; !queue.IsEmpty(); {
		curNode := queue.Pop()
		changeableNumbers := findChangeableNumbers(curNode.value)
		for _, number := range changeableNumbers {
			if nodes[number].isVisit {
				continue
			}
			nodes[number].isVisit = true
			nodes[number].pathLen = curNode.pathLen + 1
			queue.Push(&nodes[number])
		}
	}
	result = nodes[endValue].pathLen
	return
}

func findChangeableNumbers(number int) (result []int) {
	for _, target := range primeNumbers {
		if number == target {
			continue
		}

		sum := 0
		tmpNumber := number
		tmpTarget := target
		digits := make([]int, 4)
		for i := range digits {
			digits[i] = int(math.Abs(float64((tmpTarget % 10) - (tmpNumber % 10))))
			sum += digits[i]

			tmpNumber /= 10
			tmpTarget /= 10
		}

		for _, digit := range digits {
			if digit == sum {
				result = append(result, target)
			}
		}
	}
	return
}

func scanInt() int {
	sc.Scan()
	num, _ := strconv.Atoi(sc.Text())
	return num
}