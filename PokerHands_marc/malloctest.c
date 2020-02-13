#include <time.h>
#include <stdlib.h>
#include <stdio.h>
int main()
{
    unsigned long bytes_malloc = sizeof(int)*1000000000000000;
    int *test = malloc(bytes_malloc);    
}