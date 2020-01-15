#include<stdio.h>
int main() {
	int M, N;
	scanf("%d%d", &M, &N);
	int result[4000];
	int m = 0;
	char list[50][50];
	for (int i = 0; i < M; i++)
		scanf("%s", list[i]);

	for (int i = 0; i < M - 7; i++) {
		for (int j = 0; j < N - 7; j++) {
			result[m] = 0;
			result[m + 1] = 0;
			for (int k = 0; k < 8; k++) {
				for (int k2 = 0; k2 < 8; k2++) {
					if ((k + k2) % 2 == 0){
						if (list[i][j] != list[i + k][j + k2]) result[m]++;
						else result[m + 1]++;
					}
					else {
						if (list[i][j] == list[i + k][j + k2]) result[m]++;
						else result[m + 1]++ ;
					}
				}
			}
			m += 2;
		}
	}
	int min = result[0];
	for (int i = 1; i < m; i++)
		min = (min > result[i]) ? result[i] : min;
	printf("%d", min);
}