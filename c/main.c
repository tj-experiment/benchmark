#include <stdio.h>
#include <time.h>


int main() {
    clock_t begin = clock();
    for (int i = 0; i < 10000000; ++i) {
        continue;
    }
    clock_t end = clock();
    double duration = (double)(end - begin) / CLOCKS_PER_SEC;

    printf("Took: %f milliseconds\n", duration);

    FILE *out = fopen("output.txt", "a");
    fprintf(out, "%f\n", duration);
	fclose(out);
	return 0;
}