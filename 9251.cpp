#include<stdio.h>
#include<string.h>
int main() {
	char string1[1000];
	char string2[1000];
	int result[1000] = { 0, };
	scanf("%s", string1);
	scanf("%s", string2);
	int check = 0;
	int s = 0;
	for (int i = 0; i < strlen(string1); i++) {
		for (int j = i; j < strlen(string1); j++) {
			char ch = string1[j];
			for (int k = s; k < strlen(string2); k++) {
				if (ch == string2[k]) {
					result[check]++;
					s = k + 1;
					break;
				}
			}
		}
		s = 0;
		check++;
	}
	int max = result[0];
	for (int i = 0; i < sizeof(result) / sizeof(int); i++) {
		if (max < result[i])
			max = result[i];
	}
	printf("%d", max);
}
