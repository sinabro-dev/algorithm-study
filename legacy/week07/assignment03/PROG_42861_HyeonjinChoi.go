import "sort"

func solution(n int, costs [][]int) int {
    answer := 0
	parentArr := make([]int, n)

	for i := 0; i < n; i++ {
		parentArr[i] = i
	}

	sort.Slice(costs, func(i, j int) bool {
		return costs[i][2] < costs[j][2]
	})

	for i := 0; i < len(costs); i++ {
		first, second := findParent(costs[i][0], parentArr), findParent(costs[i][1], parentArr)

		if first != second {
			answer += costs[i][2]
			parentArr[second] = first
		}
	}

	return answer
}

func findParent(node int, parentArr []int) int {
	if parentArr[node] == node {
		return node
	} else {
		return findParent(parentArr[node], parentArr)
	}
}
