type Node struct {
	node, weight int
}

type MinHeap []Node

func (h *MinHeap) Push(w Node) {
	*h = append(*h, w)
	h.Up(len(*h) - 1)
}

func (h *MinHeap) Up(idx int) {
	for h.Compare(idx, ParentNode(idx)) {
		h.Swap(ParentNode(idx), idx)
		idx = ParentNode(idx)
	}
}

func (h *MinHeap) Pop() Node {
	popped := (*h)[0]
	(*h)[0] = (*h)[len(*h)-1]
	(*h) = (*h)[:len(*h)-1]
	h.Down(0)
	return popped
}

func (h *MinHeap) Down(idx int) {
	lastIdx := len(*h) - 1
	l, r := LeftNode(idx), RightNode(idx)

	var childToCompare int
	for l <= lastIdx {
		if l == lastIdx {
			childToCompare = l
		} else if h.Compare(l, r) {
			childToCompare = l
		} else {
			childToCompare = r
		}

		if h.Compare(idx, childToCompare) {
			return
		}
		h.Swap(idx, childToCompare)
		idx = childToCompare
		l, r = LeftNode(idx), RightNode(idx)
	}
}

func (h *MinHeap) Swap(i, j int) {
	(*h)[i], (*h)[j] = (*h)[j], (*h)[i]
}

func (h *MinHeap) Compare(i, j int) bool {
	return (*h)[i].weight < (*h)[j].weight
}

func ParentNode(i int) int {
	return (i - 1) / 2
}

func LeftNode(i int) int {
	return 2*i + 1
}

func RightNode(i int) int {
	return 2*i + 2
}

func networkDelayTime(times [][]int, n int, k int) int {
	Q := &MinHeap{}
	Q.Push(Node{k, 0})

	arr := make([]int, n+1)
	for index, _ := range arr {
		arr[index] = -1
	}

	for len(*Q) > 0 {
		q := Q.Pop()
		node, time := q.node, q.weight

		if arr[node] == -1 {
			arr[node] = time
			for _, value := range times {
				if value[0] == node {
					Q.Push(Node{value[1], value[2] + time})
				}
			}
		}
	}

	if findNum(arr) == n {
		return findMax(arr)
	}

	return -1
}

func findNum(arr []int) int {
	count := 0

	for _, value := range arr {
		if value != -1 {
			count++
		}
	}

	return count
}

func findMax(arr []int) int {
	max := arr[0]

	for i := 1; i < len(arr); i++ {
		if arr[i] > max {
			max = arr[i]
		}
	}

	return max
}
