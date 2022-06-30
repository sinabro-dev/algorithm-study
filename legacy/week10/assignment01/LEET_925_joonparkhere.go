package main

import (
	"bufio"
	"os"
	"strings"
)

func isLongPressedName(name string, typed string) bool {
	nameIdx, typedIdx := 0, 0
	for {
		if isBothEnd(name, typed, nameIdx, typedIdx) {
			return true
		}
		if isOnlyOneEnd(name, typed, nameIdx, typedIdx) {
			return false
		}

		nextNameIdx, nextTypedIdx := nextNonRepeatIndex(name, typed, nameIdx, typedIdx)
		repeatName, repeatTyped := nextNameIdx - nameIdx + 1, nextTypedIdx - typedIdx + 1

		if name[nextNameIdx] != typed[nextTypedIdx] {
			return false
		}
		if repeatName > repeatTyped {
			return false
		}

		nameIdx = nextNameIdx + 1
		typedIdx = nextTypedIdx + 1
	}
}

func isBothEnd(name, typed string, nameIdx, typedIdx int) bool {
	if (nameIdx >= len(name)) && (typedIdx >= len(typed)) {
		return true
	}
	return false
}

func isOnlyOneEnd(name, typed string, nameIdx, typedIdx int) bool {
	if (nameIdx >= len(name)) && (typedIdx < len(typed)) {
		return true
	}
	if (nameIdx < len(name)) && (typedIdx >= len(typed)) {
		return true
	}
	return false
}

func nextNonRepeatIndex(name, typed string, nameIdx, typedIdx int) (int, int) {
	for {
		if (nameIdx + 1 >= len(name)) || (name[nameIdx] != name[nameIdx + 1]) {
			break
		}
		nameIdx++
	}
	for {
		if (typedIdx + 1 >= len(typed)) || (typed[typedIdx] != typed[typedIdx + 1]) {
			break
		}
		typedIdx++
	}
	return nameIdx, typedIdx
}

func main() {
	defer writer.Flush()
	scanner.Scan()
	inputName := scanner.Text()
	scanner.Scan()
	inputTyped := scanner.Text()
	name := strings.Split(inputName, "\"")[1]
	typed := strings.Split(inputTyped, "\"")[1]
	if isLongPressedName(name, typed) {
		writer.WriteString("True")
	} else {
		writer.WriteString("False")
	}
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)
