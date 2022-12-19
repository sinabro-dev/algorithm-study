package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	sc             *bufio.Scanner
	wr             *bufio.Writer
	caseNum        int
	divisor        int = 1000000
	attendanceInfo [][2][3]int
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
	caseNum = scanInt()
	attendanceInfo = make([][2][3]int, caseNum+1)
}

func solve() {
	attendanceInfo[1][0][0] = 1
	attendanceInfo[1][1][0] = 1
	attendanceInfo[1][0][1] = 1

	for i := 2; i <= caseNum; i++ {
		attendanceInfo[i][0][0] = (attendanceInfo[i-1][0][0] + attendanceInfo[i-1][0][1] + attendanceInfo[i-1][0][2]) % divisor
		attendanceInfo[i][0][1] = (attendanceInfo[i-1][0][0]) % divisor
		attendanceInfo[i][0][2] = (attendanceInfo[i-1][0][1]) % divisor
		attendanceInfo[i][1][0] = (attendanceInfo[i-1][0][0] + attendanceInfo[i-1][0][1] + attendanceInfo[i-1][0][2] + attendanceInfo[i-1][1][0] + attendanceInfo[i-1][1][1] + attendanceInfo[i-1][1][2]) % divisor
		attendanceInfo[i][1][1] = (attendanceInfo[i-1][1][0]) % divisor
		attendanceInfo[i][1][2] = (attendanceInfo[i-1][1][1]) % divisor
	}
}

func printAnswer() {
	answer := attendanceInfo[caseNum][0][0] + attendanceInfo[caseNum][0][1] + attendanceInfo[caseNum][0][2] + attendanceInfo[caseNum][1][0] + attendanceInfo[caseNum][1][1] + attendanceInfo[caseNum][1][2]
	wr.WriteString(strconv.Itoa(answer % divisor))
}
