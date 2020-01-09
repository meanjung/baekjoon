//1149
#include<stdio.h>
int min(int a, int b) {
	if (a < b)
		return a;
	else return b;
}
int main() {
	int N;
	scanf("%d", &N);
	int house[1001][3];
	int result[1001][3];
	for (int i = 1; i <= N; i++)
		scanf("%d%d%d", &house[i][0],&house[i][1],&house[i][2]);
	result[0][0] = result[0][1] = result[0][2] = house[0][0] = house[0][1] = house[0][2] = 0;
	for (int i = 1; i <= N; i++) {
		result[i][0] = min(result[i - 1][1], result[i - 1][2]) + house[i][0];
		result[i][1] = min(result[i - 1][0], result[i - 1][2]) + house[i][1];
		result[i][2] = min(result[i - 1][0], result[i - 1][1]) + house[i][2];
	}
	int ss = min(min(result[N][0], result[N][1]), result[N][2]);
	printf("%d", ss);
}