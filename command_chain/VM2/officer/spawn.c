#include <stdio.h>
#include <unistd.h>


int main() {
	while(1) {
		if (fork() == 0) {
			return 0;
		} else {
			sleep(1);
		}
	}

}
