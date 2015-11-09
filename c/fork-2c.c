int main(int argc, char *argv[])

{

int child1, child2;

int ret;

// Bela explained that he isn't sure of the exact type, but this is taken as a correct typedef.

https://myhire.googleplex.com/a/google.com/feedback/#dossier:c=google.com-2001408&sig=90ceedfddecc0065d11de766752cf6d67632939e 26/72

9/8/2014 Bela Lubkin - My gHire

status_type status;

child1 = fork();

switch(child1) {

case ­1: perror(“child1 fork”); exit(1); break;

case 0: /* this is the child */

execv(“/bin/ls”, 0);

perror(“child1 exec”);

break;

break;

default: /* parent */

}

child2 = fork();

switch(child2) {

case ­1: perror(“child2 fork”); exit(1); break;

case 0: /* this is the child */

execv(“/bin/fsck”, 0);

perror(“child2 exec”);

break;

break;

default: /* parent */

}

ret = wait(&status);

if (ret < 0) {

perror(“wait”);

}

if (ret == child1) {

printf(“oh happy day, child1 finished first!\n”);

} else if (ret == child2) {

// Candidate is read on Lewis Carroll.

printf(“callooh callay, child2 finished first!\n”);

} else {

printf(“how peculiar, some child pid %d finished, that I didn’t even start!?!?\n”, ret);

}

exit(0);

}

void shaddup()

{

int fd;

dup2(2, 3); /* stash stderr */

fd = open(“/dev/null”, O_WRONLY);

dup2(fd, 1);

// Note, it may have been advantageous to leave stderr un­redirected. I didn't probe.

dup2(fd, 2);

// Note that Bela never closes the file in the child processes.

}

