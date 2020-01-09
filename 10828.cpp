#include<stdio.h>
#include<string.h>
#define MAX 100
int stack[MAX];
int result[MAX];
int topindex=-1;
int pop() {
	if (topindex == -1)
		return -1;
	else return stack[topindex--];
}
int size() {
	return topindex + 1;
}
int top() {
	if (topindex == -1)
		return -1;
	else return stack[topindex];
}
void push(int data) {
	stack[++topindex] = data;
}
int empty() {
	if (topindex == -1) return 1;
	else return 0;
}
int main() {
	for (int i = 0; i < sizeof(stack); i++)
	{
		stack[i] = 0;
		result[i] = 0;
	}
	char string[MAX];
	int data;
	int N;
	int k = 0;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%s", string);
		if (!strcmp(string, "push")) {
			scanf("%d", &data);
			push(data);
		}
		else if (!strcmp(string, "pop"))
			result[k++]=pop();
		else if (!strcmp(string, "top"))
			result[k++] = top();
		else if (!strcmp(string, "empty"))
			result[k++] = empty();
		else if (!strcmp(string, "size"))
			result[k++] = size();
	}
	for (int i = 0; i < k; i++)
		printf("%d\n", result[i]);


}