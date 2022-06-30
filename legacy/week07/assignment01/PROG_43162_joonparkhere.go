package main

import (
	"bufio"
	"os"
	"strconv"
)

var root []int

func solution(n int, computers [][]int) int {
	root = make([]int, n)
	for i := range root {
		root[i] = i
	}

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if computers[i][j] == 0 {
				continue
			}
			rootA, rootB := find(i), find(j)
			if rootA != rootB {
				union(i, j)
			}
		}
	}

	result := 0
	dummyMap := map[int]struct{}{}
	for i := 0; i < n; i++ {
		value := find(i)
		_, ok := dummyMap[value]
		if !ok {
			result++
			dummyMap[value] = struct{}{}
		}
	}

	return result
}

func find(vertex int) int {
	if root[vertex] == vertex {
		return vertex
	}
	root[vertex] = find(root[vertex])
	return root[vertex]
}

func union(vertexA, vertexB int) {
	rootA, rootB := root[vertexA], root[vertexB]
	if rootA != rootB {
		root[rootB] = rootA
	}
}

func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)

	n := scanInt()
	computers := make([][]int, n)
	for i := 0; i < n; i++ {
		computers[i] = make([]int, n)
		for j := 0; j < n; j++ {
			computers[i][j] = scanInt()
		}
	}

	networks := solution(n, computers)
	writer.WriteString(strconv.Itoa(networks))
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

func scanInt() int {
	scanner.Scan()
	num := 0
	for _, c := range scanner.Bytes() {
		num = num * 10 + int(c - '0')
	}
	return num
}
