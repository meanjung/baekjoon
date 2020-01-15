#include<stdio.h>
#include<string.h>
int main() {
	int N;
	scanf("%d", &N);
	char list[100][14];
	for (int i = 0; i < N; i++)
		scanf("%s", list[i]);
	int i;
	int len;
	for (i = 0; i < N; i++) {
		len = strlen(list[i]);
		for (int j = N-1; j >= i; j--) {
			if (len == strlen(list[j])) {
				for (int k = 0; k <len; k++) {
					if (list[i][k] != list[j][len - k - 1])
						break;
					if (k == len - 1)
						goto EXIT;
				}
			}

		}
	}
EXIT:
	printf("%d ", len);
	printf("%c", list[i][(len-1)/2]);
}