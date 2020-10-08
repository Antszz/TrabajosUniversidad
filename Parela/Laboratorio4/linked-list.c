#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

struct list_node_s {
	int data;
	struct list_node_s* next;
	pthread_mutex_t mutex;
};

int Member(int value) {
	struct list_node_s* temp_p;

	pthread_mutex_lock(&head_p_mutex);
	temp_p = head_p;
	while (temp_p != NULL && temp_p->data < value) {
		if (temp_p->next != NULL)
			pthread_mutex_lock(&(temp_p->next->mutex));
		if (temp_p == head_p)
			pthread_mutex_unlock(&head_p_mutex);
		pthread_mutex_unlock(&(temp_p->mutex));
		temp_p = temp_p->next;
	}
	if (temp_p == NULL || temp_p->data > value) {
		if (temp_p == head_p)
			pthread_mutex_unlock(&head_p_mutex);
		if (temp_p != NULL)
			pthread_mutex_unlock(&(temp_p->mutex));
		return 0;
	} else {
		if (temp_p == head_p)
			pthread_mutex_unlock(&head_p_mutex);
		pthread_mutex_unlock(&(temp_p->mutex));
		return 1;
	}
}

int main(){
	return 0;
}