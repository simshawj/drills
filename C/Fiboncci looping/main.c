#include <stdio.h>

void help() {
	printf("Syntax: program <Number of Fibonacci numbers to display>\n");
}

int main(int argc, char* argv) {
	int iterations = 0;
	
	if(argc == 2) {
		iterations = 100;
	} else {
		help();
		return 1;
	}
	
	int a = 1;
	printf("Fibonacci number 0 is %d\n", a);
	int b = 1;
	printf("Fibonacci number 1 is %d\n", b);
	int i;
	for(i = 3; i < iterations; i++) {
		int c = a + b;
		a = b;
		b = c;
		printf("Fibonacci number %d is %d\n", i, b);
	}
	return 0;
}