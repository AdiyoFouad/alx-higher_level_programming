#include "lists.h"

/**
 * insert_node - function that insert a number into a sorted
 * singly linked list
 * @head: head of the list
 * @n: number that will be insert in the list
 * Return: the adress of the new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (node == NULL  || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	
	new->next = node->next;
	node->next = new;

	return (new);
}
