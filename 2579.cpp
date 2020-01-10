//2579
#include<stdio.h>
#include<stdlib.h>
int max(int a, int b) {
	if (a < b)
		return b;
	else return a;
}
int main() {
	int n;
	scanf("%d", &n);
	int*stair = (int*)malloc(sizeof(int)*(n+1));
	int*result = (int*)malloc(sizeof(int)*(n+1));
	stair[0] = result[0] = 0;
	for (int i = 1; i <= n; i++)
		scanf("%d", &stair[i]);

	result[1] = stair[1];
	result[2] = max(result[1] + stair[2], stair[2]);
	for (int i = 3; i <= n; i++)
		result[i] = max(result[i - 3] + stair[i - 1] + stair[i], result[i - 2] + stair[i]);
	printf("%d", result[n]);
}