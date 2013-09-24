#include "apue.h"

static void sig_int(int);

int
main(int argc, char* argv[])
{
	
	if(signal(SIGINT, sig_int) == SIG_ERR) {
		printf("signal error");
	}
	
	double i;
	for(i = 10.0; i >= 0.0; i -= 1.0 ) {
		printf("number: %f\n", 10.0 / i);
	}
	printf("foo\n");

		
}

void
sig_int(int signo)
{
	printf("divide by zero detected");
}