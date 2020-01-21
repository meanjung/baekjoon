#include<stdio.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;

int check_func(int start, int end, int c,int*slist) {
	int mid = (end + start) / 2;
	int result;
	if (start > end)
		return 0;
	else {
		if (slist[mid] < c)
			result = check_func(mid + 1, end, c, slist);
		else if (slist[mid] > c)
			result = check_func(start, mid - 1, c, slist);
		else
			return 1;
	}
	return result;
}
int main() {
	int N;
	scanf("%d", &N);
	int*slist = (int*)malloc(sizeof(int)*N);
	for (int i = 0; i < N; i++)
		scanf("%d", &slist[i]);

	int M;
	scanf("%d", &M);
	int*check_list = (int*)malloc(sizeof(int)*M);
	for (int i = 0; i < M; i++)
		scanf("%d", &check_list[i]);

	sort(slist, slist + N);

	for (int i = 0; i < M; i++) {
		int c = check_list[i];
		int start = 0; int end = N - 1;
		if (check_func(start, end, c,slist) == 1)
			printf("1 ");
		else printf("0 ");

	}
}