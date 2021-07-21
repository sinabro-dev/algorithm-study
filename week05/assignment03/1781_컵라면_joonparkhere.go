package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
	numOfTask int
	info [][]int
)

func scanIntArray() []int {
	scanner.Scan()
	idx := 0
	arr := make([]int, 1)
	for _, c := range scanner.Bytes() {
		if c == ' ' {
			idx++
			arr = append(arr, 0)
			continue
		}
		arr[idx] = arr[idx] * 10 + int(c - '0')
	}
	return arr
}

func main() {
	inputInfo()
	solve()
	writer.Flush()
}

func inputInfo() {
	numOfTask = scanIntArray()[0]
	info = make([][]int, numOfTask + 1)

	for i := 0; i < numOfTask; i++ {
		inputArray := scanIntArray()
		deadline, reward := inputArray[0], inputArray[1]
		info[deadline] = append(info[deadline], reward)
	}
}

func solve() {
	maxHeap := heap{items: make([]int, numOfTask + 1), size: 0}
	result := 0
	for deadline := numOfTask; deadline >= 1; deadline-- {
		for _, reward := range info[deadline] {
			maxHeap.insert(reward)
		}
		result += maxHeap.delete()
	}
	writer.WriteString(strconv.Itoa(result))
}

type heap struct {
	items []int
	size int
}

func (h *heap) insert(priority int) {
	idx := h.size + 1
	for idx > 1 {
		parent := idx / 2
		if priority <= h.items[parent] {
			break
		}
		h.items[idx] = h.items[parent]
		idx = parent
	}
	h.items[idx] = priority
	h.size++
}

func (h *heap) delete() int {
	if h.size == 0 {
		return 0
	}
	root := h.items[1]
	last := h.items[h.size]
	parent := 1
	for {
		child := h.getHighPriorityChild(parent)
		if (child == 0) || (h.items[child] <= last) {
			break
		}
		h.items[parent] = h.items[child]
		parent = child
	}
	h.items[parent] = last
	h.size--
	return root
}

func (h *heap) getHighPriorityChild(idx int) int {
	if idx * 2 > h.size {
		return 0
	} else if idx * 2 == h.size {
		return idx * 2
	} else {
		left, right := h.items[idx * 2], h.items[idx * 2 + 1]
		if left > right {
			return idx * 2
		} else {
			return idx * 2 + 1
		}
	}
}
