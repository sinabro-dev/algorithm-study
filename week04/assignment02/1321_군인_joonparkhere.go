package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
	numOfArmy int
	numOfCommand int
	tree []int
)

func scanInt() int {
	scanner.Scan()
	ret, _ := strconv.Atoi(scanner.Text())
	return ret
}

func main() {
	scanner.Split(bufio.ScanWords)

	inputAndGenerateTree()
	executeCommand()

	writer.Flush()
}

func inputAndGenerateTree() {
	numOfArmy = scanInt()
	treeSize := int(math.Pow(2, math.Ceil(math.Log2(float64(numOfArmy))) + 1))
	tree = make([]int, treeSize)
	initTree(1, 0, numOfArmy - 1)
}

func initTree(treeIdx, start, end int) int {
	if start == end {
		// leaf 노드에 도달한 경우
		tree[treeIdx] = scanInt()
		return tree[treeIdx]
	}
	mid := (start + end) / 2
	tree[treeIdx] = initTree(treeIdx * 2, start, mid) + initTree(treeIdx * 2 + 1, mid + 1, end)
	return tree[treeIdx]
}

func executeCommand() {
	numOfCommand = scanInt()
	for i := 0; i < numOfCommand; i++ {
		commandType := scanInt()
		switch commandType {
		case 1:
			updateArmyInfo()
			break
		case 2:
			findBelongArmy()
			break
		}
	}
}

func updateArmyInfo() {
	army := scanInt() - 1
	diff := scanInt()
	updateTree(1, 0, numOfArmy - 1, army, diff)
}

func updateTree(treeIdx, start, end, target, diff int) {
	if (target < start) || (target > end) {
		// target 이 현재 유효 범위 외부에 있는 경우 예외 처리
		return
	}
	tree[treeIdx] += diff	// target 이 유효 범위 내에 속하므로 diff 만큼 Update
	if start == end {
		// leaf 노드인 경우 예외 처리
		return
	}
	mid := (start + end) / 2
	updateTree(treeIdx * 2, start, mid, target, diff)
	updateTree(treeIdx * 2 + 1, mid + 1, end, target, diff)
}

func findBelongArmy() {
	armySerialNum := scanInt()
	result := findByPartialSum(1, 0, numOfArmy - 1, &armySerialNum)
	writer.WriteString(strconv.Itoa(result + 1) + "\n")
}

func findByPartialSum(treeIdx, start, end int, partialSum *int) int {
	if *partialSum <= 0 {
		// partialSum 이 0 이하인 경우 더 이상 진행할 필요 없으므로 예외 처리
		return 0
	}
	if (start == end) && (*partialSum <= tree[treeIdx]) {
		// leaf 노드이면서 partialSum 이 현재 유효 범위 내의 합보다 작거나 같은 경우
		*partialSum -= tree[treeIdx]
		return start	// partialSum 이 음수가 되므로 해당 leaf 노드가 찾고자 하는 답임
	}
	if *partialSum > tree[treeIdx] {
		// partialSum 이 현재 유효 범위 내의 합보다 큰 경우
		*partialSum -= tree[treeIdx]
		return 0	// partialSum 이 아직 양수 이므로 0을 반환
	}
	mid := (start + end) / 2
	return findByPartialSum(treeIdx * 2, start, mid, partialSum) + findByPartialSum(treeIdx * 2 + 1, mid + 1, end, partialSum)
}
