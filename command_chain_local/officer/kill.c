#include <stdlib.h>
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int main(int argc, char *argv[] )  {
    int pid;
    sscanf(argv[1],"%d",&pid); 
    kill(pid, SIGKILL);
}
