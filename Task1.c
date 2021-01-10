#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 8 + 2
#define BUFFER_COUNT 255

int main() {
	// File descriptors initialization
	FILE* input,* output;
	fopen_s(&input, "input.txt", "r");
	fopen_s(&output, "output.txt", "w");

	char buffer[BUFFER_SIZE];
	char storage[BUFFER_COUNT][BUFFER_SIZE];

	int counter = 0;
	int faulty_counter = 0;
	int good_counter = 0;
	int parity_bit = 0;

	// Input from file and count
	while (fgets(buffer, sizeof(buffer), input)) {
		// Get rid of fgets's trailing newline
		buffer[BUFFER_SIZE - 2] = '\0';
		// Check if faulty (all zeros or parity mismatch) - save if not
		if (strcmp(buffer, "00000000") != 0 && buffer[7] == buffer[3]) {
			strcpy_s(storage[good_counter], sizeof(storage[good_counter]), buffer);
			good_counter++;
		}
		else
			faulty_counter++;
		counter++;
	}

	// Output to file:
	// 1. Number of objects
	fprintf(output, "Number of all objects: %d\n", counter);

	// 2. Number of faulty objects
	fprintf(output, "Number of faulty objects: %d\n", faulty_counter);
	
	// 3. All not faulty objects
	fprintf(output, "List of non-faulty objects: ");
	for (int i = 0; i < good_counter; i++) {
		fprintf(output, "%s ", storage[i]);
	}
	
	int fclose(FILE * input);
	int fclose(FILE * output);

	return 0;
}