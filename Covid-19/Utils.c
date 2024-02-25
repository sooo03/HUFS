#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Nation.h"


void print_one(int i, int row, Nation *arr) {
    if (i >= row || i < 0) { printf("찾는 정보가 없습니다.\n"); return; }
    printf("[%s] 확진자: %d명, 치료중: %d명, 위중증: %d명, 사망자: %d명, 완치자: %d명, 치명률: %.2f%%, 완치율: %.2f%%, 발생률: %d, 인구: %d명\n", 
        arr[i].name, arr[i].confirmed, arr[i].curing, arr[i].critical, arr[i].dead, arr[i].cured, arr[i].fatality_rate, arr[i].cure_rate, arr[i].incidence, arr[i].population);
}

void print_all(int row, Nation *arr) { for (int i = 0; i < row; i++) { print_one(i, row, arr); } }

void remove_newline(char *buf, int len) { for (int i = 0; i < len; i++) { if (buf[i] == '\n') { buf[i] = '\0'; } } }

void init_struct(Nation *n) {
    memset(n->name, '\0', BUF_SIZE);
    n->confirmed = n->curing = n->critical = n->dead = n->cured = n->population = 0;
    n->fatality_rate = n->cure_rate = n->incidence = 0;
}

int file_opener(char *filename, char (*arr)[BUF_SIZE]) {
    FILE *fp = fopen(filename, "rt");
    if (fp == NULL) { printf("Cannot open the data file!\n"); exit(1); }
    int cnt = 0;
    while (!feof(fp) && cnt < ROW_SIZE) { fgets(arr[cnt], BUF_SIZE, fp); remove_newline(arr[cnt], BUF_SIZE); cnt++; }
    fclose(fp);
    return cnt;
}

void buf_parser(char (*buf)[BUF_SIZE], int row, Nation *arr) {
    int cnt = 0;
    int index_parser = 0;
    int name_parser = 0;
    char *tmp;
    if (arr == NULL || buf == NULL) { return; }
    for (int i = 0; i < row; i++) {
        cnt = index_parser = name_parser = 0;
        init_struct(&arr[i]);
        for (int j = 0; j < BUF_SIZE; j++) {
            if (buf[i+1][j] == ',' && index_parser == 0) { index_parser = j; }
            else if (buf[i+1][j] == ',' && name_parser == 0) { name_parser = j; }
            else if (index_parser != 0 && name_parser != 0) { break; }
        }
        strncpy(arr[i].name, &buf[i+1][index_parser+1], name_parser-index_parser-1);
        tmp = buf[i+1] + name_parser + 1;
        cnt = sscanf(tmp, "%d,%d,%d,%d,%d,%f,%f,%d,%d\n",
        &arr[i].confirmed, &arr[i].curing, &arr[i].critical, &arr[i].dead, &arr[i].cured, &arr[i].fatality_rate, &arr[i].cure_rate, &arr[i].incidence, &arr[i].population); 
        if (cnt < 4) { printf("Cannot parse the string! [%d]\n", cnt); print_one(i, row, arr); exit(1); }
        
        /* Debugging */ /* printf("Total %d in [%d] ", row, i); print_one(i, row, arr); */
    }
    return;
}