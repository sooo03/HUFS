#ifndef __USER_COMPARE
#define __USER_COMPARE
#include "Nation.h"

int compare_confirmed(const void *a, const void *b) {
    Nation tmp1 = *(Nation *)a;
    Nation tmp2 = *(Nation *)b;
    if (tmp1.confirmed < tmp2.confirmed) { return   1; }
    if (tmp1.confirmed > tmp2.confirmed) { return -1; }
    if (tmp1.population < tmp2.population) { return 1; }
    if (tmp1.population > tmp2.population) { return -1; }
    return 0;
}

int compare_curing(const void *a, const void *b) {
    Nation tmp1 = *(Nation *)a;
    Nation tmp2 = *(Nation *)b;
    if (tmp1.curing < tmp2.curing) { return 1; }
    if (tmp1.curing > tmp2.curing) { return -1; }
    if (tmp1.population < tmp2.population) { return 1; }
    if (tmp1.population > tmp2.population) { return -1; }
    return 0;
}

int compare_critical(const void *a, const void *b) { 
    Nation tmp1 = *(Nation *)a;
    Nation tmp2 = *(Nation *)b;
    if (tmp1.critical < tmp2.critical) { return 1; }
    if (tmp1.critical > tmp2.critical) { return -1; }
    if (tmp1.population < tmp2.population) { return 1; }
    if (tmp1.population > tmp2.population) { return -1; }
    return 0;
}
int compare_dead(const void *a, const void *b) { 
    Nation tmp1 = *(Nation *)a;
    Nation tmp2 = *(Nation *)b;
    if (tmp1.dead < tmp2.dead) { return 1; }
    if (tmp1.dead > tmp2.dead) { return -1; }
    if (tmp1.population < tmp2.population) { return 1; }
    if (tmp1.population > tmp2.population) { return -1; }
    return 0;
}
int compare_cured(const void *a, const void *b) { 
    Nation tmp1 = *(Nation *)a;
    Nation tmp2 = *(Nation *)b;
    if (tmp1.cured < tmp2.cured) { return 1; }
    if (tmp1.cured > tmp2.cured) { return -1; }
    if (tmp1.population < tmp2.population) { return 1; }
    if (tmp1.population > tmp2.population) { return -1; }
    return 0;
}
int compare_fatality_rate(const void *a, const void *b) { 
    Nation tmp1 = *(Nation *)a;
    Nation tmp2 = *(Nation *)b;
    if (tmp1.fatality_rate < tmp2.fatality_rate) { return 1; }
    if (tmp1.fatality_rate > tmp2.fatality_rate) { return -1; }
    if (tmp1.population < tmp2.population) { return 1; }
    if (tmp1.population > tmp2.population) { return -1; }
    return 0;
}
int compare_cure_rate(const void *a, const void *b) { 
    Nation tmp1 = *(Nation *)a;
    Nation tmp2 = *(Nation *)b;
    if (tmp1.cure_rate < tmp2.cure_rate) { return 1; }
    if (tmp1.cure_rate > tmp2.cure_rate) { return -1; }
    if (tmp1.population < tmp2.population) { return 1; }
    if (tmp1.population > tmp2.population) { return -1; }
    return 0;
}
int compare_incidence(const void *a, const void *b) { 
    Nation tmp1 = *(Nation *)a;
    Nation tmp2 = *(Nation *)b;
    if (tmp1.incidence < tmp2.incidence) { return 1; }
    if (tmp1.incidence > tmp2.incidence) { return -1; }
    if (tmp1.population < tmp2.population) { return 1; }
    if (tmp1.population > tmp2.population) { return -1; }
    return 0;
}

int compare_population(const void *a, const void *b) { 
    Nation tmp1 = *(Nation *)a;
    Nation tmp2 = *(Nation *)b;
    if (tmp1.population < tmp2.population) { return 1; }
    if (tmp1.population > tmp2.population) { return -1; }
    return 0;
}

#endif