//1992
#include<stdio.h>
#include<stdlib.h>
void func(int size, int x, int y, int**array) {
	int check = 1;
	int start = array[y][x];

	if (size == 1)
		printf("%d", array[y][x]);
	
	for (int i = y; i < y + size; i++) {
		for (int j = x; j < x + size; j++) {
			if (start != array[i][j]) {
				check = 0;
				break;
			}
		}
		if (check == 0)
			break;
	}
	if (check == 1) printf("%d", array[y][x]);
	else {
		printf("(");
		func(size / 2, x, y, array);
		func(size / 2, x + 
			size / 2, y, array);
		func(size / 2, x, y + size / 2, array);
		func(size / 2, x + size / 2, y + size / 2, array);
		printf(")");
	}

}
int main() {
	int N;
	scanf("%d", &N);
	int**array = (int**)malloc(sizeof(int*)*N);
	for (int i = 0; i < N; i++)
		array[i] = (int*)malloc(sizeof(int)*N);	
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			scanf("%d", &array[i][j]);
	func(N, 0, 0, array);

}