import "sort"

func solution(distance int, rocks []int, n int) int {
	sort.Slice(rocks, func(i, j int) bool {
		return rocks[i] < rocks[j]
	})

	size := len(rocks)
	subDistance := make([]int, size+1)
	subDistance[0] = rocks[0]
	subDistance[size] = distance - rocks[size-1]

	for i := 1; i < size; i++ {
		subDistance[i] = rocks[i] - rocks[i-1]
	}

	left, right := 1, distance
	mid := (left + right) >> 1

	for right-left > 1 {
		current, removed := 0, 0

		for i := 0; i < size+1; i++ {
			current += subDistance[i]

			if current < mid {
				removed++
			} else {
				current = 0
			}
		}

		if removed > n {
			right = mid
		} else {
			left = mid
		}

		mid = (left + right) >> 1
	}

	return mid
}
