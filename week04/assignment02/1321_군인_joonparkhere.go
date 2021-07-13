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
	treeLenAtLastHeight int
	tree []int
)

func scanInt() int {
	scanner.Scan()
	ret, _ := strconv.Atoi(scanner.Text())
	return ret
}

func main() {
	scanner.Split(bufio.ScanWords)

	//inputAndGenerateTreeVer1()
	inputAndGenerateTreeVer2()
	executeCommand()

	writer.Flush()
}

func inputAndGenerateTreeVer1() {
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

func inputAndGenerateTreeVer2() {
	numOfArmy = scanInt()
	treeSize := int(math.Pow(2, math.Ceil(math.Log2(float64(numOfArmy))) + 1))
	treeLenAtLastHeight = treeSize / 2	// 트리 맨 아래 부분의 길이 == 트리 맨 아래 부분의 시작 index
	tree = make([]int, treeSize)

	for i := 0; i < numOfArmy; i++ {
		// leaf 노드들 값 입력
		tree[treeLenAtLastHeight+ i] = scanInt()
	}
	for i := numOfArmy; i < treeLenAtLastHeight; i++ {
		// 나머지 노드들은 빈 노드이므로 0 입력
		tree[i] = 0
	}
	for i := treeLenAtLastHeight - 1; i >= 1; i-- {
		// 왼쪽 child 와 오른쪽 child 를 합치면 parent
		tree[i] = tree[i * 2] + tree[i * 2 + 1]
	}
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
	//updateTreeVer1(1, 0, numOfArmy - 1, army, diff)
	updateTreeVer2(army, diff)
}

func updateTreeVer1(treeIdx, start, end, target, diff int) {
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
	updateTreeVer1(treeIdx * 2, start, mid, target, diff)
	updateTreeVer1(treeIdx * 2 + 1, mid + 1, end, target, diff)
}

func updateTreeVer2(target, diff int) {
	treeIdx := treeLenAtLastHeight + target	// 트리 맨 아래 부분의 시작 index 에 Update 하고자 하는 target 을 더함
	for treeIdx >= 1 {
		// target 을 포함하는 범위의 합을 보관하고 있는 노드들을 방문하며 diff 만큼 Update
		tree[treeIdx] += diff
		treeIdx /= 2
	}
}

func findBelongArmy() {
	armySerialNum := scanInt()
	//result := findByPartialSumVer1(1, 0, numOfArmy - 1, &armySerialNum)
	result := findByPartialSumVer2(armySerialNum)
	writer.WriteString(strconv.Itoa(result + 1) + "\n")
}

func findByPartialSumVer1(treeIdx, start, end int, partialSum *int) int {
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
	return findByPartialSumVer1(treeIdx * 2, start, mid, partialSum) + findByPartialSumVer1(treeIdx * 2 + 1, mid + 1, end, partialSum)
}

func findByPartialSumVer2(partialSum int) int {
	treeIdx := 1
	for {
		if treeIdx >= treeLenAtLastHeight {
			// leaf 노드에 위치함을 의미
			return treeIdx - treeLenAtLastHeight
		}

		if partialSum > tree[treeIdx * 2] {
			// partialSum 이 왼쪽 child 보다 크면 그만큼 partialSum 을 빼주고 오른쪽 child 로 접근
			partialSum -= tree[treeIdx * 2]
			treeIdx = treeIdx * 2 + 1
		} else {
			// partialSum 이 왼쪽 child 보다 작거나 같으면 왼쪽 child 로 접근
			treeIdx *= 2
		}
	}
}
