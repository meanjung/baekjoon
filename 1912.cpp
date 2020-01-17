#include<stdio.h>
#include<stdlib.h>
#define max(a,b) (a<b)?b:a
int main() {
	int n;
	scanf("%d", &n);
	int*list = (int*)malloc(sizeof(int)*n);
	int*result = (int*)malloc(sizeof(int)*n);
	for (int i = 0; i < n; i++)
		scanf("%d", &list[i]);
	result[0] = list[0];
	int res = result[0];
	for (int i = 1; i < n; i++) {
		result[i] = max(result[i - 1]+list[i], list[i]);
		res = max(result[i], res);
	}
	printf("%d", res);
	
}