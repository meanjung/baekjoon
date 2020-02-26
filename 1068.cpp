#include<stdio.h>
typedef struct Node {
	int value;
	int parent;
};
int main() {
	int N;
	scanf("%d", &N);
	Node nodes[50];
	int p,root;
	for (int i = 0; i < N; i++) {
		scanf("%d", &p);
		nodes[i].parent = p;
		if (p == -1) root = i;
		else nodes[p].value++;
	}
	int d;
	scanf("%d", &d);
	if (nodes[d].parent >= 0) nodes[nodes[k].parent].value--;
	nodes[d].parent = -2;
	int ans = 0;
	for (int i = 0; i < N; i++) {
		if (nodes[i].value) continue;
		p = nodes[i].parent;
		while (p >= 0) p = nodes[p].parent;
		if (p == -1) ans++;
	}
	printf("%d", ans);
		

}