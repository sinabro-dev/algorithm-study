package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)

	for i := scanInt(); i > 0; i-- {
		solve(scanInt(), scanInt())
	}
}

func solve(above, below int) {
	for {
		gcd := findGCD(above, below)
		above /= gcd
		below /= gcd
		if above == 1 {
			break
		}
		unit := int(math.Ceil(float64(below) / float64(above)))
		above = above * unit - below
		below = below * unit
	}
	writer.WriteString(strconv.Itoa(below) + "\n")
}

func findGCD(a, b int) int {
	for a != 0 {
		n := b % a
		b = a
		a = n
	}
	return b
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

func scanInt() (num int) {
	scanner.Scan()
	for _, c := range scanner.Bytes() {
		num = num * 10 + int(c - '0')
	}
	return
}
