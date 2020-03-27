#include <stdlib.h>
#include <stdbool.h>
#include "linked_list.h"

/* FINISHED FUNCTIONS */

// Creates a new List struct and initializes it (the node pointers are NULL and
// the count = 0) and then returns a pointer to it.
List *list_create(void) {
    struct List* list = (struct List*) malloc(sizeof(struct List));
    int count = 0;
    list->first = NULL;
    list->last = NULL;
    return list; 
}

// Creates a new ListNode struct and initializes it (the node pointers are NULL
// and the value is set to the passed parameter) and then returns a pointer to
// it.
ListNode *list_create_node(int value) {
  struct ListNode* node = (struct ListNode*) malloc(sizeof(struct ListNode));
  node->value = value;
  node->next = NULL;
  node->prev = NULL;
  return node;
}

// Returns the count in the list structure.
int list_count(List *list) {
  return list->count;
}

// Returns the first node in the list.
ListNode *list_first(List *list) {
  return list->first;
}

// Returns the last node in the list.
ListNode *list_last(List *list) {
  return list->last;
}

// Frees any nodes in the list but leaves the list structure.
void list_clear(List *list) {
  ListNode *node = list->first;
  while(node != NULL) {
    free(node);
    node = node->next;
  }
  list->first = NULL;
  list->last = NULL;
  list->count = 0;
}

// Finds a node in the list with the passed value and returns a pointer to the
// node.  If no matching node is found, returns NULL.
ListNode *list_find(List *list, int value) {
    ListNode *currentNode = list->first;
    while(currentNode != NULL) {
      if(currentNode->value == value) {
          return currentNode;
      }
      currentNode = currentNode->next;
    } 
      return NULL;
}

// Inserts a node in the list after the node containing value.  If no node has
// the passed value insert at the end of the list.
void list_insert_after(List *list, ListNode *node, int value) {
  ListNode *insertionNode = list_find(list,value);
  //only node
  if(list->count == 0) {
    list->first = node;
    list->last = node;
    node->next = NULL;
    node->prev = NULL;
  }
  //adding node at the end
  else if (insertionNode == list->last || insertionNode == NULL) {
    node->prev = list->last;
    list->last->next = node;
    node->next = NULL;
    list->last = node;
  }
  //adding a new node after an old node
  else {
    node->next = insertionNode->next;
    if(insertionNode->next != NULL) {
      insertionNode->next->prev = node;
    }
    insertionNode->next = node;
    node->prev = insertionNode;
  }
  list->count = list->count + 1;
}

// Removes the specified node from the list and frees it.  The node's value
// is saved and returned.
int list_remove_node(List *list, ListNode *node) {;
    if(node == list->first) {
      list->first = node->next;
    }
    if(node == list->last) {
      list->last = node->prev;
    }
    if(node->next != NULL) {
      node->next->prev = node->prev;
    }
    if(node->prev != NULL) {
      node->prev->next = node->next;
    }
    list->count = list->count - 1;
    int val = node->value;
    free(node);
    return val;
}

// Removes the node with the specified value from the list and return true.  If
// a node with the value is not found in the list, return false.
bool list_remove_value(List* list, int value) {
  if(list_find(list,value) == NULL) {
    return false;
  }
    ListNode *node = list_find(list,value);
    list_remove_node(list,node);
    return true;
}

// Inserts a node in the list before the node containing value.  If no node has
// the passed value insert at the beginning of the list.
void list_insert_before(List *list, ListNode *node, int value) {
   ListNode *insertionNode = list_find(list,value);
  //only node
  if(list->count == 0) {
    list->first = node;
    list->last = node;
    node->next = NULL;
    node->prev = NULL;
  }
  //adding node at the beginning
  else if (insertionNode == list->first || insertionNode == NULL) {
    node->next = list->first;
    node->prev = NULL;
    list->first->prev = node;
    list->first = node;
  }
  //adding a new node before an old node
  else {
    node->prev = insertionNode->prev;
    insertionNode->prev = node;
    node->next = insertionNode;
    if(node->prev != NULL) {
      node->prev->next = node;
    }
  }
  list->count = list->count + 1;
  
}

// Frees any nodes in the list and then frees the list structure.
List *list_destroy(List *list) {
  list_clear(list);
  free(list);
  return NULL;
}





