from typing import List


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


def print_linkedlist(linked_list) -> None:
    while (curent_node:=linked_list.next):
        print(curent_node.next.data)
        linked_list = curent_node.next    