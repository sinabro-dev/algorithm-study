package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

var (
	dayNum int
	queryNum int
	tree []int
)

func main() {
	defer writer.Flush()

	setUp()
	solve()
}

func setUp() {
	inputArr := scanIntArr()
	dayNum, queryNum = inputArr[0], inputArr[1]

	treeSize := int(math.Pow(2, math.Ceil(math.Log2(float64(dayNum))) + 1))
	tree = make([]int, treeSize)
}

func solve() {
	for i := 0; i < queryNum; i++ {
		query := scanIntArr()
		switch query[0] {
		case 1:
			update(query[1], query[2])
			break
		case 2:
			result := find(query[1], query[2])
			writer.WriteString(strconv.Itoa(result) + "\n")
			break
		}
	}
}

func update(target, value int) {
	idx := len(tree) / 2 + target - 1
	for idx >= 1 {
		tree[idx] += value
		idx /= 2
	}
}

func find(left, right int) int {
	sum := 0
	idxL, idxR := len(tree) / 2 + left - 1, len(tree) / 2 + right - 1
	for idxL < idxR {
		if idxL & 1 == 1 {
			sum += tree[idxL]
			idxL++
		}
		if idxR & 1 == 0 {
			sum += tree[idxR]
			idxR--
		}

		idxL /= 2
		idxR /= 2
	}
	if idxL == idxR {
		sum += tree[idxL]
	}

	return sum
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

func scanIntArr() []int {
	scanner.Scan()
	arr := make([]int, 1)
	idx := 0
	mark := 1
	for _, c := range scanner.Bytes() {
		if c == ' ' {
			arr = append(arr, 0)
			idx++
			continue
		}
		if c == '-' {
			mark = -1
			continue
		}
		arr[idx] = arr[idx] * 10 + mark * int(c - '0')
	}
	return arr
}
