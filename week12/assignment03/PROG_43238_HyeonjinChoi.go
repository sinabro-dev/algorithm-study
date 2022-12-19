func solution(n int, times []int) int64 {
	sort.Slice(times, func(i, j int) bool {
		return times[i] < times[j]
	})

	var answer, start, mid, end int64 = 0, 1, 0, int64(times[len(times)-1] * n)

	for start <= end {
		mid = (start + end) / 2
		var count int64 = 0

		for i := 0; i < len(times); i++ {
			count += mid / int64(times[i])
		}

		if count < int64(n) {
			start = mid + 1
		} else {
			if mid <= end {
				answer = mid
			}

			end = mid - 1
		}
	}

	return answer
}
