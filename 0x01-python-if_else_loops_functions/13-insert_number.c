#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *top = *head, *begin;

        begin = malloc(sizeof(listint_t));
        if (begin == NULL)
                return (NULL);
        begin->n = number;

        if (top == NULL || top->n >= number)
        {
                begin->next = top;
                *head = begin;
                return (begin);
        }

        while (top && top->next && top->next->n < number)
                top = top->next;

        begin->next = top->next;
        top->next = begin;

        return (begin);
}
