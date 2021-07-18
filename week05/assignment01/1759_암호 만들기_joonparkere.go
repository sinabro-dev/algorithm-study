package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
	lenOfPassword int
	numOfAlphabet int
	alphabets []byte
)

func scanInt() int {
	scanner.Scan()
	num, _ := strconv.Atoi(scanner.Text())
	return num
}

func scanByte() byte {
	scanner.Scan()
	return scanner.Bytes()[0]
}

func main() {
	scanner.Split(bufio.ScanWords)

	inputAlphabet()
	solve()

	writer.Flush()
}

func inputAlphabet() {
	lenOfPassword, numOfAlphabet = scanInt(), scanInt()

	alphabets = make([]byte, numOfAlphabet)
	for idx := range alphabets {
		alphabets[idx] = scanByte()
	}

	sort.Slice(alphabets, func(i, j int) bool {
		return alphabets[i] < alphabets[j]
	})
}

func solve() {
	cases := findPossibleCases()
	for idx := len(cases) - 1; idx >= 0; idx-- {
		findPassword(cases[idx])
	}
}

func findPossibleCases() []int {
	cases := make([]int, 0)

	bit := (1 << lenOfPassword) - 1
	for bit < (1 << numOfAlphabet) {
		cases = append(cases, bit)
		temp := bit | ((bit & -bit) - 1)
		bit = (temp + 1) | (((^temp & -^temp) - 1) >> (getNumOfLastZeros(bit) + 1))
	}
	return cases
}

func getNumOfLastZeros(bit int) int {
	count := 0
	for (bit & 1) == 0 {
		count++
		bit >>= 1
	}
	return count
}

func findPassword(bit int) {
	vowelCount := 0
	password := make([]byte, 0)

	pos := -1
	msb := 1 << numOfAlphabet

	for msb > 0 {
		pos++
		msb >>= 1
		if bit & msb == 0 {
			continue
		}

		alphabet := alphabets[pos]
		password = append(password, alphabet)
		if isVowel(alphabet) {
			vowelCount++
		}
	}

	if (vowelCount >= 1) && (vowelCount+2 <= lenOfPassword) {
		writer.WriteString(string(password) + "\n")
	}
}

func isVowel(alphabet byte) bool {
	switch alphabet {
	case 'a', 'e', 'i', 'o', 'u':
		return true
	}
	return false
}
