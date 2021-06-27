package main

import (
	"fmt"
)

// 큐 구현
type Queue struct {
	data []int
}

func (q *Queue) is_empty() bool {
	return len(q.data) == 0
}
func (q *Queue) peek() int {
	front := q.data[0]

	if !q.is_empty() {
		q.data = q.data[1:]
	}

	return front
}
func (q *Queue) enqueue(num int) {
	q.data = append(q.data, num)
}

var (
	dx = [4]int{0, 1, 0, -1}
	dy = [4]int{-1, 0, 1, 0}
)

func main() {

	var row, col, input int

	// 맵 입력
	fmt.Scan(&row, &col)

	paperMap := make([][]int, row)
	for i := 0; i < row; i++ {
		paperMap[i] = make([]int, col)
	}

	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			fmt.Scan(&input)
			paperMap[i][j] = input
		}
	}

	// 치즈가 녹는 시간 파악
	count := 0

	for {
		// bfs 험수의 반환 값을 통해 치즈가 녹았는지 여부 판별
		if bfs(row, col, paperMap) {
			count++
		} else {
			break
		}
	}

	fmt.Println(count)
}

func bfs(row, col int, paperMap [][]int) bool {
	/*
		bfs를 이용하여
		치즈의 노출 횟수를 구하고
		녹으면 기본값 0으로 초기화하며
		치즈가 녹았는지 여부를 반환하는 함수
	*/
	xQueue := Queue{}
	yQueue := Queue{}
	xQueue.enqueue(0)
	yQueue.enqueue(0)

	// 방문여부를 확인하는 슬라이스
	visit := make([][]bool, row)
	for i := 0; i < row; i++ {
		visit[i] = make([]bool, col)
	}

	// 해당 지점이 바깥 공기로부터 노출된 횟수를 저장하는 슬라이스
	countContact := make([][]int, row)
	for i := 0; i < row; i++ {
		countContact[i] = make([]int, col)
	}

	// bfs를 통해 외부에서 치즈를 탐색
	for {
		// 만약 큐가 비어있다면 반복문 종료
		if xQueue.is_empty() || yQueue.is_empty() {
			break
		}

		// 현재 큐 front에 저장되어있는 x, y 좌표
		curX := xQueue.peek()
		curY := yQueue.peek()

		// 반약 현재 좌표의 지점을 방문했다면 continue
		if visit[curY][curX] {
			continue
		}

		visit[curY][curX] = true

		// 상하좌우 이동하면서 치즈 탐색
		for i := 0; i < 4; i++ {
			x := curX + dx[i]
			y := curY + dy[i]

			// 만약 맵의 범위를 벗어난다면 continue
			if x < 0 || y < 0 || x >= col || y >= row {
				continue
			}

			// 이동지점이 치즈라면 노출횟수 +1, 치즈가 아니면 큐에 저장
			if paperMap[y][x] == 1 {
				countContact[y][x]++
			} else if !visit[y][x] {

				xQueue.enqueue(x)
				yQueue.enqueue(y)
			} else {
			}
		}
	}

	// 노출횟수가 2 이상이면 녹는 것으로 간주
	checkMelt := false

	for i := 1; i < row-1; i++ {
		for j := 1; j < col-1; j++ {
			if countContact[i][j] > 1 {
				paperMap[i][j] = 0
				// 녹는 부분이 존재하면 checkMelt 값을 true로 변경
				checkMelt = true
			}
		}
	}

	return checkMelt
}
