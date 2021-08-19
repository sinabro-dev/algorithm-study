func solution(n int, computers [][]int) int {
    visit := make([]bool, n)
	count := 0

	for i := 0; i < n; i++ {
		if !visit[i] {
			count++
			dfs(i, visit, computers)
		}
	}

	return count
}

func dfs(node int, visit []bool, computers [][]int) {
    visit[node] = true

	for index, data := range computers[node] {
		if data == 1 && !visit[index] {
			dfs(index, visit, computers)
		}
	}
}
