import "math"

var (
	flag  int
	ans   int = 0
	board []int
)

func solution(n int) int {
    board = make([]int, n+1)
	findAnswer(n, 1, 0)
	return ans
}

func findAnswer(num, cur, queenNum int) {
	if queenNum == num {
		ans++
		return
	}

	for i := 1; i <= num; i++ {
		flag = 1

		for j := 1; j < cur; j++ {
			if board[j] == i || math.Abs(float64(board[j]-i)) == math.Abs(float64(j-cur)) {
				flag = 0
				break
			}
		}

		if flag == 1 {
			board[cur] = i
			findAnswer(num, cur+1, queenNum+1)
			board[cur] = 0
		}
	}
}
