package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

type PreWork struct {
	work []int
}

var (
	sc         *bufio.Scanner
	wr         *bufio.Writer
	workNum    int
	costArr    []int
	endTimeArr []int
	workArr    []PreWork
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
	wr.WriteString(strconv.Itoa(solve()))
}

func setting() {
	workNum = scanInt()
	costArr = make([]int, workNum+1)
	workArr = make([]PreWork, workNum+1)

	for i := 1; i <= workNum; i++ {
		costArr[i] = scanInt()
		preWorkNum := scanInt()

		// 선행 작업에 대한 정보 저장
		for j := 0; j < preWorkNum; j++ {
			workArr[i].work = append(workArr[i].work, scanInt())
		}
	}
}

func solve() int {
	endTimeArr = make([]int, workNum+1)
	max := 0

	// 선행 작업의 소요 시간을 더하여 총 소요 시간을 구함
	for i := 1; i <= workNum; i++ {
		curTime := 0

		for j := 0; j < len(workArr[i].work); j++ {
			curTime = int(math.Max(float64(curTime), float64(endTimeArr[workArr[i].work[j]])))
		}

		endTimeArr[i] = curTime + costArr[i]
	}

	// 작업 완료 시간을 비교하여 모든 작업을 완료하는 시간을 나타내는 최댓값을 구한 후 반환
	for i := 1; i <= workNum; i++ {
		max = int(math.Max(float64(max), float64(endTimeArr[i])))
	}

	return max
}
