package main

import "fmt"

var dx = [4]int{0, 1, 0, -1}
var dy = [4]int{-1, 0, 1, 0}

// 큐 구현
type Queue struct {
	data []int
}
func (q *Queue) is_empty() bool {
	return len(q.data) == 0
}
func (q *Queue) peek() int {
	return q.data[0]
}
func (q *Queue) enqueue(num int) {
	q.data = append(q.data, num)
}
func (q *Queue) dequeue() {
	if !q.is_empty() {
		q.data = q.data[1:]
	}
}

func compare_num(num1, num2 int) int {
	/*
		두 수의 대소 비교
	*/
	if num1 < num2 {
		return num1
	} else {
		return num2
	}
}

func separate_island(x, y, sideLen, islandNum int, island [][]int) {
	/*
		떨어져있는 섬들을 구분하기 위해서
		bfs를 이용하여
		각각 개별번호 부여하는 함수
	*/
	xQueue := Queue{}
	yQueue := Queue{}
	xQueue.enqueue(x)
	yQueue.enqueue(y)
	island[y][x] = islandNum

	for {
		// 만약 큐가 비어있다면 반복문 종료
		if xQueue.is_empty() || yQueue.is_empty() {
			break
		}

		// 현재 큐 front에 저장되어있는 x, y 좌표
		curX := xQueue.peek()
		xQueue.dequeue()
		curY := yQueue.peek()
		yQueue.dequeue()

		// 상하좌우 이동하며 섬의 가장자리까지 탐색
		for i := 0; i < 4; i++ {
			x = curX + dx[i]
			y = curY + dy[i]

			// 맵의 범위를 벗어나면 continue
			if x < 0 || y < 0 || x >= sideLen || y >= sideLen {
				continue
			}

			// 이동한 지점이 섬이라면 큐에 저장
			if island[y][x] == 1 {
				island[y][x] = islandNum
				xQueue.enqueue(x)
				yQueue.enqueue(y)
			}
		}
	}
}

func find_island(x, y, sideLen, islandNum int, island [][]int) int {
	/*
		섬의 한 지점에서 다른 섬까지
		최소 거리를 구하는 함수
	*/
	xQueue := Queue{}
	yQueue := Queue{}
	weightQueue := Queue{}
	xQueue.enqueue(x)
	yQueue.enqueue(y)
	weightQueue.enqueue(0)

	// 방문 여부를 확인하는 슬라이스
	visit := make([][]bool, sideLen)
	for i := 0; i < sideLen; i++ {
		visit[i] = make([]bool, sideLen)
	}

	// 
	for {
		// 만약 큐가 비어있다면 -1(비정상)로 반환
		if xQueue.is_empty() || yQueue.is_empty() {
			return -1
		}

		// 현재 큐 front에 저장되어있는 x, y 좌표와 weight 
		curX := xQueue.peek()
		xQueue.dequeue()
		curY := yQueue.peek()
		yQueue.dequeue()
		curWeight := weightQueue.peek()
		weightQueue.dequeue()

		// 상하좌우 이동하며 번호가 다른 섬 탐색
		for i := 0; i < 4; i++ {
			x := curX + dx[i]
			y := curY + dy[i]

			// 맵의 범위를 벗어나면 continue
			if x < 0 || y < 0 || x >= sideLen || y >= sideLen {
				continue
			}

			// 만약 이동지점이 섬이 아니면 큐에 저장, 번호가 다른 섬이면 거리 반환
			if island[y][x] == 0 && !visit[y][x] {
				visit[y][x] = true
				xQueue.enqueue(x)
				yQueue.enqueue(y)
				weightQueue.enqueue(curWeight + 1)
				continue
			} else if island[y][x] != 0 && island[y][x] != islandNum {
				return curWeight
			} else {
				continue
			}
		}
	}
}

func main() {
	var sideLen, input int

	// 맵 입력
	fmt.Scan(&sideLen)

	island := make([][]int, sideLen)

	for i := 0; i < sideLen; i++ {
		island[i] = make([]int, sideLen)
	}

	for i := 0; i < sideLen; i++ {
		for j := 0; j < sideLen; j++ {
			fmt.Scan(&input)
			island[i][j] = input
		}
	}

	// 서로 다른 섬에 개별 번호 부여
	islandNum := 2

	for i := 0; i < sideLen; i++ {
		for j := 0; j < sideLen; j++ {
			if island[i][j] == 1 {
				separate_island(j, i, sideLen, islandNum, island)
				islandNum++
			}
		}
	}

	// 맵의 모든 지점으로부터 최소 거리를 구하고, 그 중 최솟값 결정
	min := 2 * (sideLen - 1)
	var signal int

	for i := 0; i < sideLen; i++ {
		for j := 0; j < sideLen; j++ {
			if island[i][j] > 1 {
				signal = find_island(j, i, sideLen, island[i][j], island)
				// signal 값이 -1이면 비정상으로 간주
				if signal == -1 {
					continue
				}

				min = compare_num(min, signal)
			}
		}
	}

	fmt.Println(min)
}
