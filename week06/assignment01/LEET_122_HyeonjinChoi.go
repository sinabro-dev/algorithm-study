func maxProfit(prices []int) int {
    buyArr := make([]int, len(prices))
	buyArr[0] = -prices[0]
	sellArr := make([]int, len(prices))
	sellArr[0] = 0

	for i := 1; i < len(prices); i++ {
		if buyArr[i-1] > sellArr[i-1]-prices[i] {
			buyArr[i] = buyArr[i-1]
		} else {
			buyArr[i] = sellArr[i-1] - prices[i]
		}

		if sellArr[i-1] > buyArr[i-1]+prices[i] {
			sellArr[i] = sellArr[i-1]
		} else {
			sellArr[i] = buyArr[i-1] + prices[i]
		}
	}

	return sellArr[len(prices)-1]
}
