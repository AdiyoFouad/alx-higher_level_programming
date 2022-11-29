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
	listint_t* current = *head;
	listint_t* node, next_node;

	if (!head || !(*head))
		return null;

	node = malloc(sizeof(listint_t*));
	if (!node)
		return null;
	node->n = number;
	while (!current)
	{
		next_node = current->next;
		if (!next_node)
		{
			if (current->n <= number)
			{
				node->next = NULL;
				current->next = node;
			}
			else
				node->next = current;
		}
		else
		{
			if (current->n <= number && number <= next_node->n)
			{
				current->next = node;
				node->next = next_node;
				break;
			}
		}
		current = next_node;
	}
	return (node);
}
