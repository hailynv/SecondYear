#ifndef __libllist_llist_h__
#define __libllist_llist_h__

#include <stdlib.h>

// ----- List and list node declarations ----------------------------------- //
struct ListNode;

typedef struct ListNode {
	struct ListNode *next;
	struct ListNode *prev;
	int value;
} ListNode;

typedef struct List {
	int count;
	ListNode *first;
	ListNode *last;
} List;

// ----- Function prototypes ----------------------------------------------- //
List *list_create();

ListNode *list_create_node(int);

List *list_destroy(List*);

void list_clear(List*);

int list_count(List*);

ListNode *list_first(List*);

ListNode *list_last(List*);

ListNode *list_find(List*, int);

void list_insert_after(List*, ListNode*, int);

void list_insert_before(List*, ListNode*, int);

int list_remove_node(List*, ListNode*);

bool list_remove_value(List*, int);
#endif
