package main

import (
	"bufio"
	"math"
	"os"
	"sort"
	"strconv"
)

// 별의 x, y좌표를 나타내는 구조체
type Location struct {
	xPos float64
	yPos float64
}

// 두 정점(별)과 거리를 나타내는 구조체
type Edge struct {
	node1    int
	node2    int
	distance float64
}

var (
	sc          *bufio.Scanner
	wr          *bufio.Writer
	starNum     int
	cost        float64
	starArr     []Location
	distanceArr []Edge
	nodeNumArr  []float64
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

func scanFloat() float64 {
	sc.Scan()
	num, _ := strconv.ParseFloat(sc.Text(), 64)
	return num
}

func main() {
	defer wr.Flush()
	setting()
	sortDistance()
	findMinCost()
	wr.WriteString(strconv.FormatFloat(cost, 'f', 4, 64) + "\n")
}

// 별의 정보를 입력받고 starArr[]에 저장하는 함수
func setting() {
	var x, y float64
	starNum = scanInt()
	starArr = make([]Location, starNum)

	for i := 0; i < starNum; i++ {
		x, y = scanFloat(), scanFloat()
		starArr[i] = Location{x, y}
	}
}

// 별들 사이의 거리를 distanceArr[]에 저장하고 거리에 대한 오름차순으로 정렬하는 함수
func sortDistance() {
	distanceArr = make([]Edge, 0)

	for i := 0; i < starNum-1; i++ {
		for j := i + 1; j < starNum; j++ {
			distanceArr = append(distanceArr, Edge{i, j, findDistance(starArr[i], starArr[j])})
		}
	}

	sort.Slice(distanceArr, func(i, j int) bool {
		return distanceArr[i].distance < distanceArr[j].distance
	})
}

// 두 점의 거리를 구하는 함수
func findDistance(star1, star2 Location) float64 {
	a := star1.xPos - star2.xPos
	b := star1.yPos - star2.yPos
	c := math.Sqrt(math.Pow(a, 2) + math.Pow(b, 2))

	return c
}

// 거리가 짧은 간선 순으로 별자리 생성하는 함수
func findMinCost() {
	nodeNumArr = make([]float64, starNum)
	separateNum := 1.0
	cost = 0

	// nodeNumArr[]를 통해 사이클 형성 방지
	for _, data := range distanceArr {
		if nodeNumArr[data.node1] == nodeNumArr[data.node2] {
			if nodeNumArr[data.node1] != 0 {
				continue
			} else {
				nodeNumArr[data.node1] = separateNum
				nodeNumArr[data.node2] = separateNum
				separateNum++
				cost += data.distance
			}
		} else {
			if nodeNumArr[data.node1] == 0 {
				nodeNumArr[data.node1] = nodeNumArr[data.node2]
				cost += data.distance
			} else if nodeNumArr[data.node2] == 0 {
				nodeNumArr[data.node2] = nodeNumArr[data.node1]
				cost += data.distance
			} else {
				matchSeparateNum(nodeNumArr[data.node1], nodeNumArr[data.node2])
				cost += data.distance
			}
		}
	}
}

// nodeNumArr[] 값을 비교하여 큰 값으로 통일시키는 함수
func matchSeparateNum(num1, num2 float64) {
	max := math.Max(num1, num2)
	min := math.Min(num1, num2)

	for index, data := range nodeNumArr {
		if data == min {
			nodeNumArr[index] = max
		}
	}
}
