#include<stdio.h>
#include<string.h>
int main() {
	char A[50];
	char B[50];
	scanf("%s", A);
	scanf("%s", B);
	int dif[50] = { 0, };
	for (int i = 0; i <= strlen(B) - strlen(A); i++) {
		int k = i;
		for (int j = 0; j < strlen(A); j++) {
			if (B[k] != A[j])
				dif[i]++;
			k++;
		}
	}
	int min = dif[0];
	for (int i = 1; i <= strlen(B)-strlen(A); i++) {
		if (min > dif[i])
			min = dif[i];
	}
	printf("%d", min);
}