package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	scanner  = bufio.NewScanner(os.Stdin)
	writer   = bufio.NewWriter(os.Stdout)
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
	numOfWork := scanIntArray()[0]
	costInfo := make([]int, numOfWork)
	maxCost := 0

	for cur := 0; cur < numOfWork; cur++ {
		inputArray := scanIntArray()
		curCost := inputArray[0]
		numOfPrecede := inputArray[1]

		for i := 0; i < numOfPrecede; i++ {
			precede := inputArray[2 + i] - 1
			if costInfo[cur] < costInfo[precede] {
				costInfo[cur] = costInfo[precede]
			}
		}

		costInfo[cur] += curCost
		if costInfo[cur] > maxCost {
			maxCost = costInfo[cur]
		}
	}
	writer.WriteString(strconv.Itoa(maxCost))
	writer.Flush()
}
