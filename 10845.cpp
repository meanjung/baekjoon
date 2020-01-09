#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAX 100
typedef struct QueueType {
	int queue[MAX];
	int front;
	int rear;
	int size;
}QueueType;
int empty(QueueType*q) {
	if (q->front == q->rear)
		return 1;
	else
		return 0;
}
void push(QueueType*q, int data) {
	q->rear = (q->rear + 1) % MAX;
	q->size++;
	q->queue[q->rear] = data;
}
int pop(QueueType*q) {
	if (empty(q) == 1)
		return -1;
	else
	{
		q->size--;
		q->front = (q->front + 1) % MAX;
		return q->queue[q->front];
	}
}
int size(QueueType*q) {
	return q->size;
}
int front(QueueType*q) {
	if(empty(q)==0)
		return q->queue[q->front + 1];
	else return -1;
}
int back(QueueType*q) {
	if (empty(q) == 0)
		return q->queue[q->rear];
	else return -1;
}
int main() {
	QueueType*q = (QueueType*)malloc(sizeof(QueueType));
	q->size = 0;
	q->front = 0;
	q->rear = 0;
	char string[6];
	int data;
	int N;
	scanf("%d", &N);
	int*result = (int*)malloc(sizeof(int)*N);
	int k = 0;
	for (int i = 0; i < N; i++) {
		scanf("%s", string);
		if (!strcmp(string, "push")) {
			scanf("%d", &data);
			push(q, data);
		}
		else if (!strcmp(string, "front"))
		{
			result[k++] = front(q);
		}
		else if (!strcmp(string, "back"))
			result[k++] = back(q);
		else if (!strcmp(string, "size"))
			result[k++] = size(q);
		else if (!strcmp(string, "empty"))
			result[k++] = empty(q);
		else if (!strcmp(string, "pop"))
			result[k++] = pop(q);
	}
	for (int i = 0; i < k; i++)
		printf("%d\n", result[i]);
}