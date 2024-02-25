#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Nation.h"
#include "User_compare.h"

extern void init_struct(Nation *n);
extern int file_opener(char *filename, char (*arr)[BUF_SIZE]);
extern void buf_parser(char (*buf)[BUF_SIZE], int row, Nation *arr);
extern void print_one(int i, int row, Nation *arr);
extern void print_all(int row, Nation *arr);
extern void remove_newline(char *buf, int len);

void search_by_name(int row, Nation *arr) { 
    char tmp[100] = {0};
    printf("찾을 국가명을 입력하세요 >> ");
    fflush(stdin); fgets(tmp, 100, stdin); fflush(stdin);
    remove_newline(tmp, 100);
    for (int i = 0; i < row; i++) { if (strcmp(tmp, arr[i].name) == 0) { print_one(i, row, arr); return; } }
    printf("찾는 정보가 없습니다.\n");
}

void sort_by_column(int row, Nation *arr) {
    int col = -1;
    printf("열을 선택하세요 (1. 확진자, 2. 치료중, 3. 위중증, 4. 사망자, 5. 완치자, 6. 치명률, 7. 완치율, 8. 발생률, 9. 인구수) >> ");
    scanf("%d", &col);
    fflush(stdin);
    if (col < 1 || col > 9) { printf("찾는 정보가 없습니다.\n"); return; }
    if (col == 1) { qsort(arr, row, sizeof(Nation), compare_confirmed); }
    else if (col == 2) { qsort(arr, row, sizeof(Nation), compare_curing); }
    else if (col == 3) { qsort(arr, row, sizeof(Nation), compare_critical); }
    else if (col == 4) { qsort(arr, row, sizeof(Nation), compare_dead); }
    else if (col == 5) { qsort(arr, row, sizeof(Nation), compare_cured); }
    else if (col == 6) { qsort(arr, row, sizeof(Nation), compare_fatality_rate); }
    else if (col == 7) { qsort(arr, row, sizeof(Nation), compare_cure_rate); }
    else if (col == 8) { qsort(arr, row, sizeof(Nation), compare_incidence); }
    else if (col == 9) { qsort(arr, row, sizeof(Nation), compare_population); }
    return;
}

void set_mode(char (*buf)[BUF_SIZE], int row, Nation *arr) {
    buf_parser(buf, row, arr);
    int mode = 0;
    do {
        printf("------------------------------------------\n");
        printf("    1. 국가별 코로나 현황 검색\n");
        printf("    2. 특정 열에 따라 정렬하기\n");
        printf("    3. 모든 내용 출력하기\n");
        printf("    0. 프로그램 종료\n");
        printf("------------------------------------------\n");
        printf("\n");
        printf("메뉴를 선택하세요 >> ");
        scanf("%d", &mode);
        printf("\n");
        if (mode < 0 || mode > 3) { printf("잘못된 값을 입력했습니다.\n"); continue; }
        else if (mode == 0) { break; }
        else if (mode == 1) { search_by_name(row, arr); }
        else if (mode == 2) { sort_by_column(row, arr); }
        else if (mode == 3) { print_all(row, arr); }
        else { printf("프로그램 오류\n"); continue; }
    } while (mode != 0);
}

int main() {
    char buf[ROW_SIZE][BUF_SIZE] = {0};
    Nation data[ROW_SIZE] = {0};
    int row = file_opener("data.csv", buf);
    row -= 2;

    set_mode(buf, row, data);
    printf("프로그램을 종료합니다.\n");
    return 0;
}