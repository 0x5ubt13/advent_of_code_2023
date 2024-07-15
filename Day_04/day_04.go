package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	/* test input

	 */

	testData := []string{
		"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
		"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
		"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
		"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
		"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
		"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"}

	parsedMap := make(map[int][]string)
	for _, card := range testData {
		cardSlice := strings.Split(card, ":")[0]
		numbersSlice := strings.Split(card, ":")[1]
		num, err := strconv.Atoi(strings.Split(cardSlice, " ")[1])
		if err != nil {
			log.Fatal(err)
		}
		parsedMap[num] = strings.Split(numbersSlice, "|")
	}

	score := getScore(parsedMap)
	fmt.Println(score)

	// Sort and print ordered
	//keySlice := make([]int, 0)
	//for key := range parsedMap {
	//	num, err := strconv.Atoi(key)
	//	if err != nil {
	//		fmt.Printf("Error: %s\n", err)
	//	}
	//	keySlice = append(keySlice, num)
	//}
	//
	//sort.Ints(keySlice)
	//
	//for _, key := range keySlice {
	//	fmt.Printf("Key: %d, Value: %s\n", key, parsedMap[key])
	//}

}

func getScore(parsedMap map[int][]string) int {
	//testData := []string{
	//	"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
	//	"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
	//	"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
	//	"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
	//	"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
	//	"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"}
	for _, value := range parsedMap {
		for _, num := range value[0] {
			fmt.Println(value)
			fmt.Println(value[0])
			fmt.Printf("%s\n", strconv.Itoa(int(num)))
		}
	}
	return 0
}

func getInput(filename string) []int64 {
	lines := make([]int64, 0)

	f, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer func(f *os.File) {
		err := f.Close()
		if err != nil {
			fmt.Printf("Error closing file: %s\n", err)
		}
	}(f)

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		intLine, err2 := strconv.ParseInt(scanner.Text(), 10, 64)
		if err2 != nil {
			log.Fatal(err2)
		}

		lines = append(lines, intLine)
	}
	return lines
}
