from typing import Any, List


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


def get_data(data_list: List = None) -> List:
    """Recursively get dummy data to populate the linked list"""

    data = input("Kindly enter data to create new node: ")
    if data == '.':
        return data_list
    data_list = data_list or []

    if data == '':
        print('Please enter a valid data...')
    else:
        data_list.append(data)

    return get_data(data_list)


def main() -> None:
    head = Node(8)
    linked_list = LinkedList(head)

    data_list = get_data()

    for data in data_list:
        linked_list.push(data)

    while linked_list.next:
        print(linked_list.next.data)
        linked_list = linked_list.next


if __name__ == '__main__':
    main()
    input('Push Enter on your keyboard to exit...')
