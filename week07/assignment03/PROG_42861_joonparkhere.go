package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var roots []int

func solution(n int, costs [][]int) int {
	sort.Slice(costs, func(i, j int) bool {
		return costs[i][2] < costs[j][2]
	})

	roots = make([]int, n)
	for i := range roots {
		roots[i] = i
	}

	sum := 0
	for _, cost := range costs {
		rootA, rootB := find(cost[0]), find(cost[1])
		if rootA != rootB {
			sum += cost[2]
			union(cost[0], cost[1])
		}
	}

	return sum
}

func find(vertex int) int {
	if roots[vertex] == vertex {
		return vertex
	}
	roots[vertex] = find(roots[vertex])
	return roots[vertex]
}

func union(vertexA, vertexB int) {
	rootA, rootB := roots[vertexA], roots[vertexB]
	if rootA != rootB {
		roots[rootB] = rootA
	}
}

func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)

	inputArray := scanIntArray()
	n := len(inputArray) / 3
	costs := make([][]int, n)
	for i := range costs {
		costs[i] = make([]int, 3)
		costs[i][0] = inputArray[i * 3]
		costs[i][1] = inputArray[i * 3 + 1]
		costs[i][2] = inputArray[i * 3 + 2]
	}

	result := solution(n, costs)
	writer.WriteString(strconv.Itoa(result))
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

func scanIntArray() []int {
	scanner.Scan()
	idx := 0
	arr := make([]int, 1)
	for _, c := range scanner.Bytes() {
		if c == ',' {
			idx++
			arr = append(arr, 0)
		} else if (c >= '0') && (c <= '9') {
			arr[idx] = arr[idx] * 10 + int(c - '0')
		} else {
			continue
		}
	}
	return arr
}
