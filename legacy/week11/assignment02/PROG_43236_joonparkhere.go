package main

import (
	"fmt"
	"sort"
)

func solution(distance int, rocks []int, n int) int {
	sort.Slice(rocks, func(i, j int) bool {
		return rocks[i] < rocks[j]
	})

	left := 0
	right := distance

	for left <= right {
		mid := (left + right) / 2

		remove := 0
		prev := 0
		for _, rock := range rocks {
			if remove > n {
				break
			}

			if rock - prev < mid {
				remove++
				continue
			}
			prev = rock
		}

		if remove <= n {
			left = mid + 1
		}
		if remove > n {
			right = mid - 1
		}
	}

	return (left + right) / 2
}

func main() {
	answer := solution(23, []int{2, 14, 11, 21, 17}, 2)
	fmt.Println(answer)
}
