#include <stdio.h>

int main() {
    int a[3], *x, *y, *z;
    for (x = &a[0], y = &a[1], z = &a[3]; x < z; x++)
    *x = x - y;
    printf("a[0]=%d a[1]=%d a[2]=%d¥n", a[0], a[1], a[2]);
    return 0;
}