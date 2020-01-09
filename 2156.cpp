#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main() {
	int n;
	scanf("%d", &n);
	int*list = (int*)malloc(sizeof(int)*n);
	int*result = (int*)malloc(sizeof(int)*n);
	for (int i = 0; i < n; i++)
		scanf("%d", &list[i]);
	result[0] = list[0];
	if (n > 1)
		result[1] = list[0] + list[1];
	for (int i = 2; i < n; i++) {
		                 //연속 0번        //연속 1번               //연속 2번
		result[i] = fmax(result[i-1], fmax(result[i - 2] + list[i], result[i - 3] + list[i-1] + list[i]));
	}
	printf("%d\n", result[n-1]);
}