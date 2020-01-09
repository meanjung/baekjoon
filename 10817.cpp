//10817
#include<stdio.h>
int main() {
	int A, B, C;
	scanf("%d%d%d", &A, &B, &C);
	int result;
	if (A <= B) {
		if (B <= C)
			result = B;
		else {
			if (C <= A)
				result = A;
			else
				result = C;
		}
	}
	else {//A>B
		if (B >= C)
			result = B;
		else {//B<C
			if (C <= A)
				result = C;
			else
				result = A;
		}
	}
	printf("%d", result);
}