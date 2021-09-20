package main

import (
    "time"
    "fmt"
    "log"
    "os"
)


func main() {
    start := time.Now()
    for i := 1; i < 10_000_000; i++ {
        continue;
    }
    end := time.Since(start).Milliseconds()

    fmt.Printf("Took: %d milliseconds\n", end)

    message := fmt.Sprintf("%d\n", end)

    f, err := os.OpenFile(
        "output.txt",
        os.O_APPEND|os.O_WRONLY|os.O_CREATE,
        0644,
    )

    if err != nil {
		log.Fatal(err)
	}

	_, err = f.WriteString(message)

	if err != nil {
		log.Fatal(err)
	}

    f.Close()
}