package main

import "fmt"

func main() {
	for i := 1; i <= 100; i++ {
		if i%3 == 0 && i%5 == 0 {
			fmt.Println("CracklePop")
		} else if i%3 == 0 {
			fmt.Println("Crackle")
		} else if i%5 == 0 {
			fmt.Println("Pop")
		} else {
			fmt.Println(i)
		}
	}
}
