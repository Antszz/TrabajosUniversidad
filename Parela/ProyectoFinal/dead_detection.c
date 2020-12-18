#include <stdio.h>
#include <stdlib.h>

#define FALSE 0
#define TRUE 1
#define MAX_COUNT 1000

int deadlockDetected = FALSE;
struct Stack {
    int top;
    int array[MAX_COUNT];
};

void push(struct Stack *stack, int data) {
    if (stack -> top == MAX_COUNT) {
        printf("Overflow");
        exit(1);
    }
    stack -> array[++(stack -> top)] = data;
}

int pop(struct Stack *stack) {
    if (stack -> top == -1) {
        printf("Underflow");
        exit(1);
    }
    int temp = stack -> array[(stack -> top)--];
    return temp;
}


void dfs(int **graph, int *visited, int *isOnStack, int source, int totalNodes, struct Stack *stack, int *isPartOfCycle) {
    int i = 0;
    if (isOnStack[source]) {
        if (!isPartOfCycle[source]) {
            printf("\nSe detecto dead lock : (");
            deadlockDetected = TRUE;
            i = stack -> top;
            while (stack -> array[i] != source) {
                i--;
            }
            while (i <= stack -> top) {
                isPartOfCycle[stack -> array[i]] = TRUE;
                printf("%d -> ", (stack -> array[i] + 1));
                i++;
            }
            printf("%d)", (source + 1));
        }
        return;
    }
    visited[source] = TRUE;
    push(stack, source);
    isOnStack[source] = TRUE;
    for (i = 0; i < totalNodes; i++) {
        if (graph[source][i] == 1) {
            dfs(graph, visited, isOnStack, i, totalNodes, stack, isPartOfCycle);
        }
    }
    pop(stack);
    isOnStack[source] = FALSE;
}


void detectDeadlock(int** graph, int n) {
    int* visited = (int *) malloc (sizeof(int) * n);
    int* isPartOfCycle = (int *) malloc (sizeof(int) * n);
    int* isOnStack = (int *) malloc (sizeof(int) * n);
    int i = 0;
    int j = 0;
    struct Stack stack;
    stack.top = -1;

    for (i = 0; i < n; i++) {
        visited[i] = FALSE;
        isOnStack[i] = FALSE;
        isPartOfCycle[i] = FALSE;
    }

    for (i = 0; i < n; i++) {
        if (visited[i] == FALSE) {
            dfs(graph, visited, isOnStack, i, n, &stack, isPartOfCycle);
            for (j = 0; j < n; j++) {
                isOnStack[j] = FALSE;
            }
        }
    }
    if (!deadlockDetected) {
    		printf("\nNo existe dead lock en este sistema");
    }
    free(visited);
    free(isPartOfCycle);
    free(isOnStack);
}

int main() {
    int numProcesses = 0;
    int numResources = 1;
    int numEdges = 0;
    int i = 0;
    int j = 0;
    int source;
    int sink;
    printf("Numero de procesos: ");
    scanf("%d", &numProcesses);
    printf("Numero de recursos: ");
	scanf("%d", &numResources);

    printf("Ingrese valores de la matriz:\n");
    int *usedResource = (int *) malloc (sizeof(int) * numResources);
    for (i = 0; i < numResources; i++) {
        usedResource[i] = FALSE;
    }

    int totalNodes = numProcesses + numResources;
    int** graph = (int **) malloc(sizeof(int *) * totalNodes);
    for (i = 0; i < totalNodes; i++) {
        graph[i] = (int *) malloc (sizeof(int) * totalNodes);
    }

    for (i = 0; i < totalNodes; i++) {
        for (j = 0; j < totalNodes; j++) {
			scanf("%d", &graph[i][j]);
        }
    }

    detectDeadlock(graph, totalNodes);
    free(usedResource);
    for (i = 0; i < totalNodes; i++) {
        free(graph[i]);
    }
    free(graph);
    printf("\n");
    return 0;
}
