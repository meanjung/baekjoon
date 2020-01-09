//2231¹ø
#include<stdio.h>
#include<math.h>
int num(int x) {
	int ten = 1;
	int i = 0;
	while (x / ten != 0) {
		ten *= 10;
		i++;
	}
	ten = ten / 10;
	i--;
	return i;
}
int main() {
	int check = 1;
	int N;
	scanf("%d", &N);
	int i;
	for (i = 1; i < N; i++) {
		int semi_sum = 0;
		int s = i;
		for (int j = num(i); j >= 0; j--)
		{
			semi_sum += s / (int)pow(10,j);
			s = s % (int)pow(10, j);
			
		}
		if (semi_sum + i == N)
		{
			check = 0;
			break;
		}
	}
	if (check == 0)
		printf("%d", i);
	else
		printf("0");
}