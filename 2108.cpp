#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define SWAP(x,y,t) ((t)=(x), (x)=(y), (y)=(t))
int partition(int*array, int start, int end) {
	int q = start;
	int low = start;
	int high = end+1;
	int t;
	do {
		do {
			low++;
		} while (low <= end && array[low] < array[q]);
		do {
			high--;
		} while (high >= start && array[high] > array[q]);
		if (low < high)
			SWAP(array[low], array[high], t);
	} while (low < high);
	SWAP(array[start], array[high], t);
	return high;
}

void quick_sort(int*array, int start, int end) {
	if (start < end) {
		int q = partition(array, start, end);
		quick_sort(array, start, q-1);
		quick_sort(array, q + 1, end);
	}
}
int main() {
	int N;
	scanf("%d", &N);
	int*array = (int*)malloc(sizeof(int)*N);
	int sum = 0;
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &array[i]);
		sum += array[i];
	}
	//»ê¼úÆò±Õ
	printf("%.0f\n", roundf((float)sum / N));
	//ÄüÁ¤·Ä, Áß¾Ó°ª
	quick_sort(array, 0, N - 1);
	int mid = (N - 1) / 2;
	printf("%d\n", array[mid]);
	//ÃÖºó°ª
	int*freq = (int*)malloc(sizeof(int)*N);
	for (int i = 0; i < N; i++)
		freq[i] = 0;
	freq[0]++;
	for (int i = 1; i < N; i++) {
		int x = array[i];
		int j;
		for (j = 0; j < i; j++) {
			if (x == array[j])
			{
				freq[j]++;
				break;
			}
		}
		if (j == i)
			freq[i]++;
	}
	int maxfreqindex = 0;
	for (int i = 1; i < N; i++) {
		if (freq[i] > freq[maxfreqindex])
			maxfreqindex = i;
	}
	printf("%d\n", array[maxfreqindex]);
	//¹üÀ§
	int max = array[N - 1];
	int min = array[0];
	printf("%d", max - min);
}