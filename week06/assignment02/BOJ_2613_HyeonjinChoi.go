package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	sc           *bufio.Scanner
	wr           *bufio.Writer
	marbleNum    int
	groupNum     int
	max          int
	marbleSumArr []int
	answerArr    []int
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
	solve()
	printAnswer()
}

func setting() {
	marbleNum, groupNum = scanInt(), scanInt()
	marbleSumArr = make([]int, marbleNum+2)
	answerArr = make([]int, groupNum+1)

	for i := 0; i < marbleNum; i++ {
		marbleSumArr[i+1] = scanInt() + marbleSumArr[i]
	}
}
 
func solve() {
	left, right := 1, marbleSumArr[marbleNum]

	// parametric search
	for left <= right {
		mid := (left + right) / 2

		// mid 값이 그룹의 합 중 최대일 때 주어진 그룹의 개수만큼 분할 가능한지 판별
		if check(mid) {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}

	max = left
	// 그룹의 합 중 최댓값인 max에 대해 check() 실행
	check(max)
}

func check(num int) bool {
// num 값을 그룹의 합 중 최대로 하였을 때 최소 몇 그룹으로 나눌 수 있는지 구하는 함수
	temp := groupNum
	left := 0

	for left < marbleNum {
		right := marbleNum + 1 - temp

		for marbleSumArr[right]-marbleSumArr[left] > num {
			right--
		}

		answerArr[temp] = right - left
		temp--

		if temp < 0 {
			break
		}

		left = right
	}

	return temp == 0
}

func printAnswer() {
	wr.WriteString(strconv.Itoa(max) + "\n")

	for i := groupNum; i > 0; i-- {
		wr.WriteString(strconv.Itoa(answerArr[i]) + " ")
	}
}
