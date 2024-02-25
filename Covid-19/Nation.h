#ifndef __NATION
#define __NATION

#define ROW_SIZE 300
#define BUF_SIZE 1000

typedef struct _node {
    char name[BUF_SIZE];
    int     confirmed;
    int     curing;
    int     critical;
    int     dead;
    int     cured;
    float   fatality_rate;
    float   cure_rate;
    int     incidence;
    int     population;
} Nation;

#endif