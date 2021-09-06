package main

import (
	"bufio"
	"os"
	"strconv"
)

type Building struct {
	info []int
}

type Queue struct {
	data []int
}

func (q *Queue) IsEmpty() bool {
	return len(q.data) == 0
}
func (q *Queue) Peek() int {
	front := q.data[0]

	if !q.IsEmpty() {
		q.data = q.data[1:]
	}

	return front
}
func (q *Queue) Enqueue(num int) {
	q.data = append(q.data, num)
}

var (
	sc          *bufio.Scanner
	wr          *bufio.Writer
	caseNum     int
	costArr     []int
	indegreeArr []int
	buildingArr []Building
	answerArr   []int
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
	caseNum = scanInt()
	costArr = make([]int, caseNum+1)
	indegreeArr = make([]int, caseNum+1)
	buildingArr = make([]Building, caseNum+1)
	answerArr = make([]int, caseNum+1)

	for i := 1; i <= caseNum; i++ {
		setting(i)
	}

	bfs()

	for i := 1; i <= caseNum; i++ {
		wr.WriteString(strconv.Itoa(answerArr[i]) + "\n")
	}
}

func setting(index int) {
	costArr[index] = scanInt()

	for {
		buildingNum := scanInt()
		if buildingNum == -1 {
			break
		}

		buildingArr[buildingNum].info = append(buildingArr[buildingNum].info, index)
		indegreeArr[index]++
	}
}

func bfs() {
	q := Queue{}

	for i := 1; i <= caseNum; i++ {
		if indegreeArr[i] == 0 {
			q.Enqueue(i)
			answerArr[i] = costArr[i]
		}
	}

	for !q.IsEmpty() {
		front := q.Peek()

		for i := 0; i < len(buildingArr[front].info); i++ {
			index := buildingArr[front].info[i]
			answerArr[index] = max(answerArr[index], answerArr[front]+costArr[index])

			indegreeArr[index]--
			if indegreeArr[index] == 0 {
				q.Enqueue(index)
			}
		}
	}
}

func max(num1, num2 int) int {
	if num1 >= num2 {
		return num1
	} else {
		return num2
	}
}
