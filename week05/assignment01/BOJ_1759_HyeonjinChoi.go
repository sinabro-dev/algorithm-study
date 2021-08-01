package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var (
	sc         *bufio.Scanner
	wr         *bufio.Writer
	answerLen  int
	inputLen   int
	inputArr   []byte
	answerArr  []byte
	checkVowel []bool
)

func init() {
	sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	wr = bufio.NewWriter(os.Stdout)
}

func scanInt() int {
	sc.Scan()
	num, _ := strconv.Atoi(sc.Text())
	return num
}

func scanByte() byte {
	sc.Scan()
	return sc.Bytes()[0]
}

func main() {
	defer wr.Flush()
	setting()
	solve(0, -1, 0, 0)
}

func setting() {
	answerLen, inputLen = scanInt(), scanInt()
	answerArr = make([]byte, 15)
	inputArr = make([]byte, inputLen)
	checkVowel = make([]bool, 26)

	for i := 0; i < inputLen; i++ {
		inputArr[i] = scanByte()
	}

	// 입력받은 문자들을 사전순으로 정렬
	sort.Slice(inputArr, func(i, j int) bool {
		return inputArr[i] < inputArr[j]
	})

	// 입력받은 문자 중 모음이면 checkVowel[]의 해당 인덱스 값을 true로 갱신
	for i := 0; i < inputLen; i++ {
		if inputArr[i] == 'a' || inputArr[i] == 'e' || inputArr[i] == 'i' || inputArr[i] == 'o' || inputArr[i] == 'u' {
			checkVowel[i] = true
		}
	}
}

func solve(position, previous, consonant, vowel int) {
	if position == answerLen {
		// 단어 길이도 조건에 부합하고, 자음 및 모음의 수도 조건에 부합하면 출력
		if consonant >= 2 && vowel >= 1 {
			for i := 0; i < answerLen; i++ {
				wr.WriteString(string(answerArr[i]))
			}
			wr.WriteString("\n")
			return
		}
	}

	// 정렬된 문자들을 바탕으로 재귀 방식을 통한 탐색
	for i := previous + 1; i < inputLen; i++ {
		current := inputArr[i]
		answerArr[position] = current

		if checkVowel[i] {
			solve(position+1, i, consonant, vowel+1)
		} else {
			solve(position+1, i, consonant+1, vowel)
		}
	}
}
