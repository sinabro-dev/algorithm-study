package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

type node struct {
	min int
	max int
}

const (
	minItem = 1
	maxItem = 1000000000
)

var (
	scanner   = bufio.NewScanner(os.Stdin)
	writer    = bufio.NewWriter(os.Stdout)
	numOfItem int
	numOfCase int
	itemArr   []int
	minTree   []int
	maxTree   []int
	tree      []node
)

func main() {
	//inputNum()
	//generateTreeVer1()
	//findTargetVer1()
	//generateTreeVer2()
	inputAndGenerateTreeVer3()
	findTargetVer2()

	writer.Flush()
}

func scanInt() int {
	scanner.Scan()
	ret, _ := strconv.Atoi(scanner.Text())
	return ret
}

func scanIntArray() []int {
	scanner.Scan()
	ret := []int{0, 0}

	idx := 0
	text := scanner.Text()
	for _, c := range text {
		if c == ' ' {
			idx++
			continue
		}
		ret[idx] = ret[idx] * 10 + int(c - '0')
	}
	return ret
}

func min(valueA, valueB int) int {
	if valueA < valueB {
		return valueA
	} else {
		return valueB
	}
}

func max(valueA, valueB int) int {
	if valueA > valueB {
		return valueA
	} else {
		return valueB
	}
}

func inputNum() {
	inputArray := scanIntArray()
	numOfItem = inputArray[0]
	numOfCase = inputArray[1]

	itemArr = make([]int, numOfItem)
	for idx := range itemArr {
		itemArr[idx] = scanInt()
	}
}

func generateTreeVer1() {
	treeSize := int(math.Pow(2, math.Ceil(math.Log2(float64(numOfItem))) + 1))
	minTree = make([]int, treeSize)
	initMinTreeVer1(0, numOfItem - 1, 1)
	maxTree = make([]int, treeSize)
	initMaxTreeVer1(0, numOfItem - 1, 1)
}

func initMinTreeVer1(start, end, index int) int {
	if start == end {
		minTree[index] = itemArr[start]
		return minTree[index]
	}
	mid := (start + end) / 2
	valueA := initMinTreeVer1(start, mid, index * 2)
	valueB := initMinTreeVer1(mid + 1, end, index * 2 + 1)

	minTree[index] = min(valueA, valueB)
	return minTree[index]
}

func initMaxTreeVer1(start, end, index int) int {
	if start == end {
		maxTree[index] = itemArr[start]
		return maxTree[index]
	}
	mid := (start + end) / 2
	valueA := initMaxTreeVer1(start, mid, index * 2)
	valueB := initMaxTreeVer1(mid + 1, end, index * 2 + 1)

	maxTree[index] = max(valueA, valueB)
	return maxTree[index]
}

func generateTreeVer2() {
	treeSize := int(math.Pow(2, math.Ceil(math.Log2(float64(numOfItem))) + 1))
	tree = make([]node, treeSize)
	initTreeVer2(0, numOfItem - 1, 1)
}

func initTreeVer2(start, end, index int) node {
	if start == end {
		tree[index] = node{min: itemArr[start], max: itemArr[start]}
		return tree[index]
	}
	mid := (start + end) / 2
	nodeA := initTreeVer2(start, mid, index * 2)
	nodeB := initTreeVer2(mid + 1, end, index * 2 + 1)

	tree[index] = node{min: min(nodeA.min, nodeB.min), max: max(nodeA.max, nodeB.max)}
	return tree[index]
}

func inputAndGenerateTreeVer3() {
	inputArray := scanIntArray()
	numOfItem = inputArray[0]
	numOfCase = inputArray[1]

	treeSize := int(math.Pow(2, math.Ceil(math.Log2(float64(numOfItem))) + 1))
	tree = make([]node, treeSize)
	initTreeVer3(0, numOfItem - 1, 1)
}

func initTreeVer3(start, end, index int) node {
	if start == end {
		num := scanInt()
		tree[index] = node{min: num, max: num}
		return tree[index]
	}
	mid := (start + end) / 2
	nodeA := initTreeVer3(start, mid, index * 2)
	nodeB := initTreeVer3(mid + 1, end, index * 2 + 1)

	tree[index] = node{min: min(nodeA.min, nodeB.min), max: max(nodeA.max, nodeB.max)}
	return tree[index]
}

func findTargetVer1() {
	for i := 0; i < numOfCase; i++ {
		targetStart, targetEnd := scanInt() - 1 , scanInt() - 1
		resultMin := findMinVer1(targetStart, targetEnd, 0, numOfItem - 1, 1)
		resultMax := findMaxVer1(targetStart, targetEnd, 0, numOfItem-1, 1)
		writer.WriteString(strconv.Itoa(resultMin) + " " + strconv.Itoa(resultMax) + "\n")
	}
}

func findMinVer1(targetStart, targetEnd, start, end, index int) int {
	if (targetStart > end) || (targetEnd < start) {
		return maxItem
	}
	if (targetStart <= start) && (targetEnd >= end) {
		return minTree[index]
	}
	mid := (start + end) / 2
	valueA := findMinVer1(targetStart, targetEnd, start, mid, index * 2)
	valueB := findMinVer1(targetStart, targetEnd, mid + 1, end, index * 2 + 1)
	return min(valueA, valueB)
}

func findMaxVer1(targetStart, targetEnd, start, end, index int) int {
	if (targetStart > end) || (targetEnd < start) {
		return minItem
	}
	if (targetStart <= start) && (targetEnd >= end) {
		return maxTree[index]
	}
	mid := (start + end) / 2
	valueA := findMaxVer1(targetStart, targetEnd, start, mid, index * 2)
	valueB := findMaxVer1(targetStart, targetEnd, mid + 1, end, index * 2 + 1)
	return max(valueA, valueB)
}

func findTargetVer2() {
	for i := 0; i < numOfCase; i++ {
		inputArray := scanIntArray()
		targetStart, targetEnd := inputArray[0] - 1, inputArray[1] - 1
		result := findMinAndMaxVer2(targetStart, targetEnd, 0, numOfItem - 1, 1)
		writer.WriteString(strconv.Itoa(result.min) + " " + strconv.Itoa(result.max) + "\n")
	}
}

func findMinAndMaxVer2(targetStart, targetEnd, start, end, index int) node {
	if (targetStart > end) || (targetEnd < start) {
		return node{min: maxItem, max: minItem}
	}
	if (targetStart <= start) && (targetEnd >= end) {
		return tree[index]
	}
	mid := (start + end) / 2
	nodeA := findMinAndMaxVer2(targetStart, targetEnd, start, mid, index * 2)
	nodeB := findMinAndMaxVer2(targetStart, targetEnd, mid + 1, end, index * 2 + 1)
	return node{min: min(nodeA.min, nodeB.min), max: max(nodeA.max, nodeB.max)}
}
