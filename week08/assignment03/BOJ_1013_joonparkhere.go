package main

import (
	"bufio"
	"os"
	"regexp"
)

func main() {
	defer writer.Flush()

	compile, _ := regexp.Compile("^(100+1+|01)+$")
	for i := scanInt(); i > 0; i-- {
		solveVer2(compile, scanBytes())
		//solveVer1(scanBytes())
	}
}

func solveVer2(compile *regexp.Regexp, signal []byte) {
	if compile.Match(signal) {
		writer.WriteString("YES\n")
	} else {
		writer.WriteString("NO\n")
	}
}

func solveVer1(signal []byte) {
	for idx := 0; idx < len(signal); {
		if idx < 0 {
			writer.WriteString("NO\n")
			return
		}
		switch signal[idx] {
		case '1':
			idx = findNextIndexAsFirstSubSignal(signal, idx+1)
		case '0':
			idx = findNextIndexAsSecondSubSignal(signal, idx+1)
		}
	}
	writer.WriteString("YES\n")
}

func findNextIndexAsFirstSubSignal(signal []byte, idx int) int {
	if (idx >= len(signal)) || (signal[idx] != '0') {
		return -1
	}
	idx += 1

	countOfZero := countContinuousTarget(signal, idx, '0')
	if countOfZero <= 0 {
		return -1
	}
	idx += countOfZero

	countOfOne := countContinuousTarget(signal, idx, '1')
	if countOfOne <= 0 {
		return -1
	}
	idx += countOfOne

	return idx
}

func countContinuousTarget(signal []byte, idx int, target byte) int {
	count := 0
	for ; idx < len(signal); idx++ {
		if signal[idx] != target {
			break
		}
		if (target == '1') && (!isBelong(signal, idx)) {
			break
		}
		count++
	}
	return count
}

func isBelong(signal []byte, idx int) bool {
	if (idx < len(signal)-2) && (signal[idx+1] == '0') && (signal[idx+2] == '0') {
		return false
	}
	return true
}

func findNextIndexAsSecondSubSignal(signal []byte, idx int) int {
	if (idx >= len(signal)) || (signal[idx] != '1') {
		return -1
	}
	idx += 1

	return idx
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

func scanInt() int {
	scanner.Scan()
	num := 0
	for _, c := range scanner.Bytes() {
		num = num * 10 + int(c-'0')
	}
	return num
}

func scanBytes() []byte {
	scanner.Scan()
	return scanner.Bytes()
}
