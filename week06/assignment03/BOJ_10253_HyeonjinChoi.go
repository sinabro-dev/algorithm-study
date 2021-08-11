package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	sc *bufio.Scanner
	wr *bufio.Writer
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
	count := scanInt()

	for i := 0; i < count; i++ {
		numerator, denominator := scanInt(), scanInt()
		wr.WriteString(strconv.Itoa(calc(numerator, denominator)) + "\n")
	}
}

func calc(numerator, denominator int) int {
	for numerator != 1 {
		// numerator/denominator >= 1/x 을 만족하는 x 구하기
		x := denominator/numerator + 1
		numerator = numerator*x - denominator
		denominator = denominator * x
		
		gcd := findGcd(numerator, denominator)

		if gcd != -1 {
			numerator /= gcd
			denominator /= gcd
		}
	}

	return denominator
}

func findGcd(num1, num2 int) int {
// 최대공약수 구하는 함수 (유클리드 알고리즘 이용)
	if num2 == 0 {
		return num1
	} else {
		return findGcd(num2, num1%num2)
	}
}
