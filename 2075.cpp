#include<stdio.h>
#include<queue>
using namespace std;

priority_queue<int> pq;

int main() {
	int N;
	scanf("%d", &N);
	int a;
	for (int i = 0; i < N*N; i++) {
		scanf("%d", &a);
		pq.push(-a);
		if (pq.size() > N)
			pq.pop();
	}
	printf("%d", -pq.top());
}