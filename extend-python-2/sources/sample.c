#include <math.h>
#include <stdio.h>
#include <stdlib.h>

/*
 * Simple example
*/

int gcd(int x, int y) {
    int g = y;
    while (x > 0) {
        g = x;
        x = y % x;
        y = g;
    }

    return g;
}


/*
 * Example with pointer parameter.
*/

int divide(int a, int b, int *rest) {
    int quot = a / b;
    *rest = a % b;
    return quot;
}

/*
 * Example with array parameters.
*/

double avg(double *data, int length) {
    double total = 0.0;
    for (int i=0; i < length; i++) {
        total += data[i];
    }
    return total / length;
}


/*
 * Example with data structures.
*/

typedef struct Point {
    double x, y;
} Point;


double distance(Point *p1, Point *p2) {
    return hypot(p1->x - p2->x, p1->y - p2->y);
}


/*
 * Example with callbacks
*/

void sum_with_cb(int x, int y, void (*callback)(int)) {
    callback(x+y);
}


/*
 * Example returning a int array
*/

int* range(int length, int start) {
    int *data = (int *) malloc(length);

    for (int i=0; i < length; i++) {
        data[i] = start;
        start += 1;
    }

    return data;
}
