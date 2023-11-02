#include "lists.h"
/*
 * insert_node - listint_t 
 * @head: node pointing
 * @number: int number
 *
 * Return: new node
 */

listint_t *_insert_node(listint_t **head, int number)
{
        listint_t *current;
        listint_t *new = NULL;

        current = *head;

        new = malloc(sizeof(listint_t));
        if (!new)
                return (NULL);

        new->n = number;

        if (*head == NULL || (*head)->n >= number)
        {
                new->next = *head;
                *head = new;
                return (new);
        }

        while (current->next && current->next->n < number)
                current = current->next;

        new->next = current->next;
        current->next = new;

        return (new);
}
