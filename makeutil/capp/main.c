#include <stdio.h>
#include <time.h>

int main(void) {
    time_t now = time(NULL);
    printf("this is C app\n");
    printf("Run time: %ld\n", now);
    return 0;
}
