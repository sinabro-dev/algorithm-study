package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

var (
	sc         *bufio.Scanner
	wr         *bufio.Writer
	daysLived  int
	numOfQuery int
	tree       []int
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
}

func setting() {
	daysLived, numOfQuery = scanInt(), scanInt()
	tree = make([]int, int(math.Pow(2, math.Ceil(math.Log2(float64(daysLived)))+1)))
}

func solve() {
	for i := 0; i < numOfQuery; i++ {
		separatorNum, day, priceOrDay := scanInt(), scanInt(), scanInt()

		if separatorNum == 1 {
			update(1, 1, daysLived, day, priceOrDay)
		} else {
			wr.WriteString(strconv.Itoa(query(1, 1, daysLived, day, priceOrDay)) + "\n")
		}
	}
}

func update(node, start, end, index, value int) {
	if start == end {
		tree[node] += value
		return
	}

	mid := (start + end) >> 1

	if index <= mid {
		update(node<<1, start, mid, index, value)
	} else {
		update((node<<1)+1, mid+1, end, index, value)
	}

	tree[node] = tree[node<<1] + tree[(node<<1)+1]
}

func query(node, start, end, queryStart, queryEnd int) int {
	if queryStart > end || queryEnd < start {
		return 0
	}

	if queryStart <= start && end <= queryEnd {
		return tree[node]
	}

	mid := (start + end) >> 1

	return query(node<<1, start, mid, queryStart, queryEnd) + query((node<<1)+1, mid+1, end, queryStart, queryEnd)
}
