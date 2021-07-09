package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	scanner     = bufio.NewScanner(os.Stdin)
	writer      = bufio.NewWriter(os.Stdout)
	numOfVertex int
	inorder     []int
	postorder   []int
	cache map[int]int
)

func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)

	inputInorderAndPostorder()
	//splitTreeVer1(0, 0, numOfVertex)
	//splitTreeVer2(inorder, postorder)
	processToCache()
	splitTreeVer3(inorder, postorder, 0)
}

func inputInorderAndPostorder() {
	numOfVertex = scanInt()
	inorder = make([]int, numOfVertex)
	for i := 0; i < numOfVertex; i++ {
		inorder[i] = scanInt()
	}
	postorder = make([]int, numOfVertex)
	for i := 0; i < numOfVertex; i++ {
		postorder[i] = scanInt()
	}
}

func scanInt() int {
	scanner.Scan()
	ret, _ := strconv.Atoi(scanner.Text())
	return ret
}

func splitTreeVer1(beginIdxAtInorder, beginIdxAtPostorder, size int) {
	if size == 1 {
		writer.WriteString(strconv.Itoa(inorder[beginIdxAtInorder]) + " ")
		return
	}

	// Post-order 의 시작 index 에 Sub Tree 크기를 더하고 1 을 빼면, 마지막 Post-order index 이다.
	lastIdxAtPostorder := beginIdxAtPostorder + size - 1
	root := postorder[lastIdxAtPostorder]
	writer.WriteString(strconv.Itoa(root) + " ")

	// 위에서 구한 root 가 In-order 에서는 어느 index 에 위치했는지 찾는다.
	var splitIdxAtInorder int
	for idx := beginIdxAtInorder; idx < numOfVertex; idx++ {
		if inorder[idx] == root {
			splitIdxAtInorder = idx
			break
		}
	}

	// In-order 에서의 root index 를 기점으로 앞부분과 뒷부분 Sub Tree 에 대해 재귀 함수 처리한다.
	frontSplitSize := splitIdxAtInorder - beginIdxAtInorder
	if frontSplitSize > 0 {
		splitTreeVer1(beginIdxAtInorder, beginIdxAtPostorder, frontSplitSize)
	}

	backSplitSize := size - frontSplitSize - 1
	if backSplitSize > 0 {
		splitTreeVer1(splitIdxAtInorder + 1, beginIdxAtPostorder +frontSplitSize, backSplitSize)
	}
}

func splitTreeVer2(subInorder, subPostorder []int) {
	if len(subInorder) == 0 {
		return
	}

	lastIdxAtSubPostorder := len(subPostorder)-1
	root := subPostorder[lastIdxAtSubPostorder]
	writer.WriteString(strconv.Itoa(root) + " ")

	var splitIdx int
	for idx, value := range subInorder {
		if value == root {
			splitIdx = idx
			break
		}
	}

	splitTreeVer2(subInorder[:splitIdx], subPostorder[:splitIdx])
	splitTreeVer2(subInorder[splitIdx+1:], subPostorder[splitIdx:lastIdxAtSubPostorder])
}

func processToCache() {
	cache = make(map[int]int)
	for idx, value := range inorder {
		cache[value] = idx
	}
}

func splitTreeVer3(subInorder, subPostorder []int, offset int) {
	if len(subInorder) == 0 {
		return
	}

	lastIdxAtSubPostorder := len(subPostorder) - 1
	root := subPostorder[lastIdxAtSubPostorder]
	writer.WriteString(strconv.Itoa(root) + " ")
	splitIdx := cache[root] - offset

	frontSubInorder := subInorder[: splitIdx]
	frontSubPostorder := subPostorder[: splitIdx]
	splitTreeVer3(frontSubInorder, frontSubPostorder, offset)

	backSubInorder := subInorder[splitIdx + 1 :]
	backSubPostorder := subPostorder[splitIdx : lastIdxAtSubPostorder]
	splitTreeVer3(backSubInorder, backSubPostorder, offset + len(frontSubInorder) + 1)
}