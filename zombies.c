#include <stdlib.h>
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

const int SIZE = 100;    // Maximum number of zombies we can create
int processes[SIZE];    // Stores the pid of zombies
int number_spawned = 0;    // Keeps track of the number of zombies spawned
int is_spawning = 1;    // Boolean that indicates if zombies are spawning

// Called when Ctrl + C is pressed
void handler(int num) {
	is_spawning = 0;    // Stop spawning zombies
}

int main() {
	printf("zombie spawner pid: (%d)\n", getpid());
	signal(SIGINT, handler);
	
	// We start spawning zombies by default
	while(is_spawning == 1) {
		int pid = fork();
		if (pid == 0) {
			printf("zombie (%d) spawned...\n", getpid());
			return 0;
		} else {
			processes[number_spawned] = pid;    // Store the pid of the new zombie
			number_spawned = number_spawned + 1;
			sleep(1);
		}
	}
	
	// Kill all the zombies we spawned (happends after we pressed Ctrl + C
	for (int i = 0; i < SIZE; i++) {
		if (processes[i] != 0) {
			printf("killed zombie (%d) \n", processes[i]);
	  		kill(processes[i], SIGKILL);
  		}
	}
	
	while(1) {
		printf("waiting...");
		sleep(10);
	}

}
