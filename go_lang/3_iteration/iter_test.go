package iteration

import (
	"fmt"
	"strings"
	"testing"
)

func TestRepeat(t *testing.T) {
	repeated := Repeat("a", 5)
	expected := "aaaaa"

	if repeated != expected {
		t.Errorf("expected %q but got %q", expected, repeated)
	}
}

func BenchmarkRepeat(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Repeat("a", 5)
	}
}

func ExampleRepeat() {
	fmt.Println(Repeat("j", 6))
	// Output: jjjjjj
}

func ExampleContainsAny() {
	fmt.Println(strings.ContainsAny("cool", "oo"))
	// Output: true
}

func ExampleAPIRepeat() {
	fmt.Println("His name was " + strings.Repeat("scary ", 2) + "terry.")
	// Output: His name was scary scary terry.
}
