#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *old, *new;

	if (list == NULL || list->next == NULL)
		return (0);
	old = list;
	new = old->next;

	while (old != NULL && new->next != NULL
		&& new->next->next != NULL)
	{
		if (old == new)
			return (1);
		old = old->next;
		new = new->next->next;
	}
	return (0);
}

