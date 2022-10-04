from utils.utils import get_data, print_linkedlist


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

def main() -> None:
    head = Node(8)
    linked_list = LinkedList(head)

    data_list = get_data()

    for data in data_list:
        linked_list.push(data)
        
    print_linkedlist(linked_list)
        
    linked_list.reverse()
    
    print_linkedlist(linked_list)

if __name__ == '__main__':
    main()
    input('Push Enter on your keyboard to exit...')
