package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

// Node 각 별에 대한 정보를 저장할 구조체
type Node struct {
	starIdx  int
	priority float64
}

// Heap 풀이 시 사용할 최소힙 (MinHeap) 을 표현할 구조체, 시작 index 는 0 이 아닌 1 로 설정
type Heap struct {
	item [maxNumOfStar + 1]Node
	size int
}

// find 찾고자 하는 별의 index 를 기준으로, Heap 내에서의 index 와 Node 정보를 반환
func (h *Heap) find(starIdx int) (int, Node) {
	for idx, node := range h.item {
		if starIdx == node.starIdx {
			return idx, node
		}
	}
	return 0, Node{}
}

// starIdx 를 갖는 별을 priority 기준으로 알맞은 위치를 찾고 해당 위치에 삽입
func (h *Heap) insert(starIdx int, priority float64) {
	idx := h.size + 1
	for idx > 1 {
		parent := h.getParent(idx)
		if priority >= h.item[parent].priority {
			break
		}
		h.item[idx] = h.item[parent]
		idx = parent
	}
	newNode := Node{starIdx, priority}
	h.item[idx] = newNode
	h.size++
}

// Heap 에 위치한 idx 를 기준으로 Node 를 찾고 해당 Node 의 priority 를 변경
func (h *Heap) change(idx int, newPriority float64) {
	if !h.canChangePriority(idx, newPriority) {
		return
	}

	saveStarIdx := h.item[idx].starIdx
	for {
		var target int
		if newPriority < h.item[idx].priority {
			target = h.getParent(idx)
			if (target == 0) || (newPriority >= h.item[target].priority) {
				break
			}
		} else {
			target = h.getLowPriorityChild(idx)
			if (target == 0) || (newPriority <= h.item[target].priority) {
				break
			}
		}
		h.item[idx] = h.item[target]
		idx = target
	}
	h.item[idx].starIdx = saveStarIdx
	h.item[idx].priority = newPriority
}

func (h *Heap) canChangePriority(idx int, newPriority float64) bool {
	if (idx < 1) || (idx > h.size) {
		return false
	}
	if newPriority == h.item[idx].priority {
		return false
	}
	return true
}

// delete 맨 앞에 위치한 Heap Node 를 삭제 및 반환
func (h *Heap) delete() Node {
	root := h.item[1]
	last := h.item[h.size]
	parent := 1
	for {
		child := h.getLowPriorityChild(parent)
		if (child == 0) || (last.priority <= h.item[child].priority) {
			break
		}
		h.item[parent] = h.item[child]
		parent = child
	}
	h.item[parent] = last
	h.size--
	return root
}

// getLowPriorityChild left child 와 right child 중에서 더 낮은 priority 를 가진 child 의 index 를 반환
func (h *Heap) getLowPriorityChild(idx int) int {
	if h.getLChild(idx) > h.size {
		return 0
	} else if h.getLChild(idx) == h.size {
		return h.getLChild(idx)
	} else {
		left := h.getLChild(idx)
		right := h.getRChild(idx)
		if h.item[left].priority < h.item[right].priority {
			return left
		} else {
			return right
		}
	}
}

func (h *Heap) getParent(idx int) int {
	return idx / 2
}

func (h *Heap) getLChild(idx int) int {
	return idx * 2
}

func (h *Heap) getRChild(idx int) int {
	return idx * 2 + 1
}

const (
	maxNumOfStar = 100
	maxDistance = 1415
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
	answer float64
	numOfStar int
	distance [][]float64
	isCheck []bool
)

func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)
	generatePositionAndDistance()
	findMSTbyPrim()
}

func generatePositionAndDistance() {
	type Position struct {
		x float64
		y float64
	}

	numOfStar = scanInt()
	position := make([]Position, numOfStar + 1)
	for i := 1; i <= numOfStar; i++ {
		x, y := scanFloat64(), scanFloat64()
		position[i] = Position{x, y}
	}

	distance = make([][]float64, numOfStar + 1)
	for i := 1; i <= numOfStar; i++ {
		distance[i] = make([]float64, numOfStar + 1)
		for j := 1; j <= numOfStar; j++ {
			powOfWidth := math.Pow(position[i].x - position[j].x, 2)
			powOfHeight := math.Pow(position[i].y - position[j].y, 2)
			distance[i][j] = math.Sqrt(powOfWidth + powOfHeight)
		}
	}
}

func scanInt() int {
	scanner.Scan()
	ret, _ := strconv.Atoi(scanner.Text())
	return ret
}

func scanFloat64() float64 {
	scanner.Scan()
	ret, _ := strconv.ParseFloat(scanner.Text(), 64)
	return ret
}

func findMSTbyPrim() {
	isCheck = make([]bool, numOfStar + 1)
	heap := Heap{}
	heap.size = 0

	for i := 1; i <= numOfStar; i++ {
		heap.insert(i, maxDistance)
	}
	heap.change(1, 0)

	for heap.size != 0 {
		node := heap.delete()
		answer += node.priority
		isCheck[node.starIdx] = true

		for curStarIdx := 1; curStarIdx <= numOfStar; curStarIdx++ {
			curDistance := distance[node.starIdx][curStarIdx]
			findIdx, findNode := heap.find(curStarIdx)
			if (!isCheck[curStarIdx]) && (curDistance < findNode.priority) {
				heap.change(findIdx, curDistance)
			}
		}
	}

	writer.WriteString(strconv.FormatFloat(answer, 'f', 2, 64))
}