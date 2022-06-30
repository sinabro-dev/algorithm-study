import "sort"

// 작업 정보에 대한 구조체
type Job struct {
	start int
	burst int
}

// min heap 
type MinHeap []Job

func (h *MinHeap) Push(w Job) {
	*h = append(*h, w)
	h.Up(len(*h) - 1)
}

func (h *MinHeap) Up(idx int) {
	for h.Compare(idx, ParentNode(idx)) {
		h.Swap(ParentNode(idx), idx)
		idx = ParentNode(idx)
	}
}

func (h *MinHeap) Pop() Job {
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
	return (*h)[i].burst < (*h)[j].burst
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

func solution(jobs [][]int) int {
    sort.Slice(jobs, func(i, j int) bool {
		return jobs[i][0] < jobs[j][0]
	})

	priorityQueue := &MinHeap{}
	time := 0
	average := 0
	index := 0

	for {
		for j := index; j < len(jobs); j++ {
      // time(ms) 시점까지 요청들어왔던 작업 확인 
			if jobs[j][0] > time {
				break
			}

			priorityQueue.Push(Job{jobs[j][0], jobs[j][1]})
			index++
		}
    
		if len(*priorityQueue) > 0 { // 처리해야할 작업이 있을 경우
			job := priorityQueue.Pop()
			time += job.burst
			average = average + time - job.start
		} else if index < len(jobs) { // 요청들어올 때까지 시간 경과
			time++
		} else {
			break
		}
	}

	return average / len(jobs)
}
