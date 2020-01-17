#include<stdio.h>
#include<stdlib.h>
int find_min(int*house, int*office) {
	int min_h = house[0];
	int min_o = office[0];
	for (int i = 1; i < sizeof(house) / sizeof(int); i++)
		if (min_h > house[i])
			min_h = house[i];
	for (int i = 1; i < sizeof(office) / sizeof(int); i++)
		if (min_o > office[i])
			min_o = office[i];
	if (min_o > min_h)
		return min_h;
	else
		return min_o;
}
int find_max(int*house, int*office) {
	int max_h = house[0];
	int max_o = office[0];
	for (int i = 1; i < sizeof(house) / sizeof(int); i++)
		if (max_h < house[i])
			max_h = house[i];
	for (int i = 1; i < sizeof(office) / sizeof(int); i++)
		if (max_o < office[i])
			max_o = office[i];
	if (max_o < max_h)
		return max_h;
	else
		return max_o;
}
int main() {
	int n,d;
	scanf("%d", &n);
	int*house = (int*)malloc(sizeof(int)*n);
	int*office = (int*)malloc(sizeof(int)*n);
	for (int i = 0; i < n; i++) 
		scanf("%d%d", &house[i],&office[i]);
	scanf("%d", &d);
	int min = find_min(house, office);
	int max = find_max(house, office);
	int*result = (int*)malloc(sizeof(int)*(max - min - d + 1));
	int k = 0;
	while (1) {
		result[k] = 0;
		for (int i = 0; i < n; i++) {
			if (house[i] >= min && house[i] <= (min+d) && office[i] >= min && office[i] <= (min+d))
				result[k]++;
		}
		k++;
		min++;
		if (min + d > max)
			break;
	}
	int res = result[0];
	for (int i = 0; i < k;i++) {
		if (res < result[i])
			res = result[i];
	}
	printf("%d", res);
}