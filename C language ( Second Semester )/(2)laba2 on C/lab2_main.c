#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

typedef struct Node {
    double value;
    struct Node* prev;
    struct Node* next;
} Node;

typedef struct {
    Node* head;
    Node* tail;
} List;

void init_list(List* list)
{
    list->head = NULL;
    list->tail = NULL;
}

void push_back(List* list, Node* node)
{
    node->prev = list->tail;
    node->next = NULL;

    if (list->tail != NULL)
        list->tail->next = node;
    else
        list->head = node;

    list->tail = node;
}

Node* pop_front(List* list)
{
    if (list->head == NULL)
        return NULL;

    Node* node = list->head;
    list->head = node->next;

    if (list->head != NULL)
        list->head->prev = NULL;
    else
        list->tail = NULL;

    node->prev = NULL;
    node->next = NULL;
    return node;
}

Node* pop_back(List* list)
{
    if (list->tail == NULL)
        return NULL;

    Node* node = list->tail;
    list->tail = node->prev;

    if (list->tail != NULL)
        list->tail->next = NULL;
    else
        list->head = NULL;

    node->prev = NULL;
    node->next = NULL;
    return node;
}

void print_list(const List* list)
{
    Node* current = list->head;
    while (current != NULL) {
        printf("%.2f", current->value);
        if (current->next != NULL)
            printf(" <-> ");
        current = current->next;
    }
    printf("\n");
}

void free_list(List* list)
{
    Node* current = list->head;
    while (current != NULL) {
        Node* next = current->next;
        free(current);
        current = next;
    }
    list->head = NULL;
    list->tail = NULL;
}

void reorder_list(List* original, List* result)
{
    while (original->head != NULL) {
        Node* from_front = pop_front(original);
        push_back(result, from_front);

        if (original->head != NULL) {
            Node* from_back = pop_back(original);
            push_back(result, from_back);
        }
    }
}

int main(void)
{
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);

    srand((unsigned int)time(NULL));

    int n;
    printf("Введіть кількість елементів (n > 0): ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        fprintf(stderr, "Помилка: n має бути цілим числом більше 0.\n");
        return 1;
    }

    List original;
    List result;
    init_list(&original);
    init_list(&result);

    for (int i = 0; i < n; i++) {
        Node* node = (Node*)malloc(sizeof(Node));
        if (node == NULL) {
            fprintf(stderr, "Помилка: не вдалося виділити пам'ять.\n");
            free_list(&original);
            return 1;
        }
        node->value = (double)(rand() % 9000 + 1000) / 100.0;
        push_back(&original, node);
    }

    printf("\nВихідний список:\n");
    print_list(&original);

    reorder_list(&original, &result);

    printf("\nСписок після перекомпонування:\n");
    print_list(&result);

    free_list(&result);

    return 0;
}