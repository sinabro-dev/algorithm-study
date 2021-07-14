package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
	numOfLeafNode int
	tree []int
	cache map[int]int
)

func scanInt() int {
	scanner.Scan()
	ret, _ := strconv.Atoi(scanner.Text())
	return ret
}

func main() {
	scanner.Split(bufio.ScanWords)
	solve()
	writer.Flush()
}

func solve() {
	numOfCase := scanInt()
	for i := 0; i < numOfCase; i++ {
		numOfDVD := scanInt()
		numOfQuery := scanInt()
		initTreeAndCache(numOfQuery, numOfDVD)

		for j := 0; j < numOfQuery; j++ {
			DVDIdx := scanInt()
			position := findPartialSum(cache[DVDIdx])
			writer.WriteString(strconv.Itoa(position - 1) + " ")

			numOfRemainQuery := numOfQuery - (j + 1)
			updateTree(DVDIdx, numOfRemainQuery)
		}
		writer.WriteString("\n")
	}
}

func initTreeAndCache(numOfQuery, numOfDVD int) {
	numOfLeafNode = int(math.Pow(2, math.Ceil(math.Log2(float64(numOfQuery + numOfDVD)))))
	treeSize := int(math.Pow(2, math.Ceil(math.Log2(float64(numOfQuery + numOfDVD)) + 1)))
	tree = make([]int, treeSize)
	cache = make(map[int]int)

	for i := 0; i < numOfQuery; i++ {
		tree[numOfLeafNode + i] = 0
	}
	for i := 0; i < numOfDVD; i++ {
		tree[numOfLeafNode + numOfQuery + i] = 1
		cache[i + 1] = numOfQuery + i + 1
	}
	for i := numOfQuery + numOfDVD; i < numOfLeafNode; i++ {
		tree[numOfLeafNode + i] = 0
	}
	for i := numOfLeafNode - 1; i >= 1; i-- {
		tree[i] = tree[i * 2] + tree[i * 2 + 1]
	}
}

func findPartialSum(target int) int {
	partialSum := 0
	treeIdx := 1
	start := 1
	end := numOfLeafNode

	for {
		if start == end {
			partialSum += tree[treeIdx]
			return partialSum
		}

		mid := (start + end) / 2
		if target > mid {
			partialSum += tree[treeIdx * 2]
			treeIdx = treeIdx * 2 + 1
			start = mid + 1
		} else {
			treeIdx *= 2
			end = mid
		}
	}
}

func updateTree(dvdIdx, numOfRemainQuery int) {
	target := cache[dvdIdx]
	treeIdxToRemove := numOfLeafNode + target - 1
	treeIdxToInsert := numOfLeafNode + numOfRemainQuery
	for treeIdxToRemove != treeIdxToInsert {
		tree[treeIdxToRemove] -= 1
		tree[treeIdxToInsert] += 1
		treeIdxToRemove /= 2
		treeIdxToInsert /= 2
	}
	cache[dvdIdx] = numOfRemainQuery + 1
}
