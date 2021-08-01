package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
	numOfItem int
	numOfGroup int
	weights []int
)

func scanIntArray() []int {
	scanner.Scan()
	idx := 0
	array := make([]int, 1)
	for _, c := range scanner.Bytes() {
		if c == ' ' {
			idx++
			array = append(array, 0)
			continue
		}
		array[idx] = array[idx] * 10 + int(c - '0')
	}
	return array
}

func main() {
	defer writer.Flush()
	large, sum := input()
	solve(large, sum)
}

func input() (int, int) {
	inputArray := scanIntArray()
	numOfItem, numOfGroup = inputArray[0], inputArray[1]

	weights = make([]int, numOfItem)
	large, sum := 0, 0

	inputArray = scanIntArray()
	for idx, weight := range inputArray {
		weights[idx] = weight
		if large < weight {
			large = weight
		}
		sum += weight
	}

	return large, sum
}

func solve(large, curSum int) {
	left, right := large, curSum
	for left <= right {
		mid := (left + right) / 2
		if canPartition(mid) {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}

	targetSum := left
	writer.WriteString(strconv.Itoa(targetSum) + "\n")

	curSum, itemCount, remainNumOfGroup := 0, 0, numOfGroup
	for idx, weight := range weights {
		curSum += weight
		itemCount++

		if curSum > targetSum {
			writer.WriteString(strconv.Itoa(itemCount - 1) + " ")
			curSum = weight
			itemCount = 1
			remainNumOfGroup--
		}

		if remainNumOfItem := numOfItem-idx; remainNumOfItem == remainNumOfGroup {
			break
		}
	}

	for i := 0; i < remainNumOfGroup; i++ {
		writer.WriteString(strconv.Itoa(itemCount) + " ")
		itemCount = 1
	}
}

func canPartition(mid int) bool {
	curSum, groupCount := 0, 1
	for _, weight := range weights {
		curSum += weight
		if curSum > mid {
			curSum = weight
			groupCount++
		}
	}
	return groupCount <= numOfGroup
}
