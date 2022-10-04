from typing import Any, List


from utils.utils import get_data, print_linkedlist

class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

    def set_next(self, next):
        self.next = next
        return next


class LinkedList:
    def __init__(self, next: Node) -> None:
        self.next = next

    def push(self, data: Any) -> Node:
        next = Node(data)
        next.set_next(self.next)
        self.next = next


def main() -> None:
    head = Node(8)
    linked_list = LinkedList(head)

    data_list = get_data()

    for data in data_list:
        linked_list.push(data)

    print_linkedlist(linked_list)


if __name__ == '__main__':
    main()
    input('Push Enter on your keyboard to exit...')
