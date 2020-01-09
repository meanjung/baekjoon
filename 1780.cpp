#include<stdio.h>
#include<stdlib.h>
int minusone = 0;
int zero = 0;
int one = 0;
void move(int size, int y, int x,int**array) {
	int check = 1;//true
	int start = array[y][x];

	for (int i = y; i < y + size; i++) {
		for (int j = x; j < x + size; j++) {
			if (start != array[i][j]) {
				check = 0;//false
				break;
			}
		}
		if (check == 0)break;
	}

	if (check == 1) {
		if (start == -1)minusone++;
		else if (start == 0)zero++;
		else one++;
	}
	else {
		for (int i = 0; i < 3; i++)
			for (int j = 0; j < 3; j++)
				move(size / 3, y + (i*size / 3), x + (j*size / 3), array);
	}
}
int main() {
	int N;
	scanf("%d", &N);
	int **array = (int**)malloc(sizeof(int*)*N);
	
	for (int i = 0; i < N; i++)
		array[i] = (int*)malloc(sizeof(int)*N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &array[i][j]);
		}
	}
	move(N, 0, 0,array);
	printf("%d\n%d\n%d\n", minusone, zero, one);
	
}