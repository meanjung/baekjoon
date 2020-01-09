#include<stdio.h>
#include<stdlib.h>
int max(int a, int b) {
	if (a < b) return b;
	else return a;
}
int main(void) {
	int n;
	scanf("%d", &n);
	int **list=(int**)malloc(sizeof(int*)*(n+1));
	int **result = (int**)malloc(sizeof(int*)*(n + 1));
	for (int i = 0; i <= n; i++)
	{
		list[i] = (int*)malloc(sizeof(int)*n);
		result[i] = (int*)malloc(sizeof(int)*n);
	}
	
	result[0][0] = list[0][0] = 0;

	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < i; j++)
			scanf("%d", &list[i][j]);
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < i; j++)
		{
			if (j == 0)
				result[i][j] = result[i - 1][0] + list[i][j];
			else if (j == i - 1)
				result[i][j] = result[i - 1][j - 1] + list[i][j];
			else
				result[i][j] = max(result[i - 1][j - 1], result[i - 1][j]) + list[i][j];
		}
	}
	int ss = result[n][0];
	for (int i = 1; i < n; i++)
	{
		if (ss < result[n][i])
			ss = result[n][i];
	}
	printf("%d", ss);

}
