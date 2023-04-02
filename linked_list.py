
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class S_LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        self.head = Node(data, self.head)

    def push_back(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        current = self.head
        while current.next is not None:
            current = current.next
        if current.next is None:
            current.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("linked list is empty.")
            return

        current = self.head
        list_string = ''
        while current is not None:
            list_string += str(current.data) + '-->'
            current = current.next
        print(list_string)

    # Create new linked list with data list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.push_back(data)

    def get_size(self):
        size = 0
        current = self.head
        while current is not None:
            size += 1
            current = current.next
        return size

    # Remove node at index
    def remove_at(self, index):
        if self.get_size() - 1 < index or index < 0:
            raise Exception("Index out of bounds.")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 1
        while current is not None:
            if count == index:
                current.next = current.next.next
                break
            current = current.next
            count += 1

    # Insert node at index
    def insert_at(self, index, data):
        if self.get_size() - 1 < index or index < 0:
            raise Exception("Index out of bounds.")
        if index == 0:
            self.push_front(data)
            return
        current = self.head
        count = 1
        while current is not None:
            if count == index:
                # current.next = Node(data, current.next.next) # Incorrect
                current.next = Node(data, current.next) # Alternate approach
                break
            current = current.next
            count += 1

    # Methods to implement
    # Search for first occurrence of data_after value in list
    # Insert data_to_insert after data_after node
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        # Determine if value is in list
        current = self.head
        while current is not None:
            if current.data == data_after:
                current.next = Node(data_to_insert, current.next)
                return
            current = current.next
        print('Data not found.')

    # Remove first node that contains data
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print('Data not found.')

def main():
    linked_list = S_LinkedList()
    linked_list.push_front(15)
    linked_list.push_front(16)
    linked_list.push_front(17)
    linked_list.push_back(50)
    linked_list.print()
    linked_list.insert_values([5, 10, 20, 30])
    linked_list.remove_at(1)
    linked_list.print()
    linked_list.insert_at(0, 85)
    linked_list.print()
    linked_list.insert_at(1, 86)
    linked_list.print()
    linked_list.insert_at(3, 88)
    linked_list.print()
    print(f'Length: {linked_list.get_size()}')
    linked_list.print()
    linked_list.insert_after_value(85, 50)
    linked_list.print()
    linked_list.remove_by_value(50)
    linked_list.print()


if __name__ == '__main__':
    main()
