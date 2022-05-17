class Node:
    def __init__(self, data):
        self.value = data
        self.n_ref = None
        self.p_ref = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_dll(self):
        if self.head is None:
            print('Doubly Linked List is Empty.')
            return
        n = self.head
        while n is not None:
            print(n.value, "--->", end=" ")
            n = n.n_ref

    def print_dll_reverse(self):
        if self.head is None:
            print('Doubly Linked list is Empty,from Reverse')
            return
        n = self.head
        while n.n_ref is not None:
            n = n.n_ref
        p = n
        while p is not None:
            print("<---", p.value,  end=" ")
            p = p.p_ref

    def add_begin(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            li = self.head
            new_node = Node(data)
            new_node.p_ref = li.p_ref
            new_node.n_ref = li
            li.p_ref = new_node
            self.head = new_node
            return

    def add_end(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        li = self.head
        while li.n_ref is not None:
            li = li.n_ref
        new_node = Node(data)
        new_node.n_ref = li.n_ref
        new_node.p_ref = li
        li.n_ref = new_node

    def add_after(self, data, after_what):
        if self.head is None:
            print('Empty List can not add after')
            return
        li = self.head
        while li is not None:
            if li.value == after_what:
                break
            li = li.n_ref
        if li is None:
            print('After what value is not present')
        else:
            new_node = Node(data)
            new_node.p_ref = li
            new_node.n_ref = li.n_ref
            if li.n_ref is not None:
                li.n_ref.p_ref = new_node
            li.n_ref = new_node

    def add_before(self, data, before_what):
        if self.head is None:
            print('List is Empty can add before')
            return
        if self.head.value == before_what:
            new_node = Node(data)
            new_node.p_ref = self.head.p_ref
            new_node.n_ref = self.head
            self.head.p_ref = new_node
            self.head = new_node
        else:
            li = self.head
            while li is not None:
                if li.value == before_what:
                    break
                li = li.n_ref
            if li is None:
                print('before what value is not find.')
            else:
                new_node = Node(data)
                new_node.n_ref = li
                new_node.p_ref = li.p_ref
                li.p_ref.n_ref = new_node
                li.p_ref = new_node

    def delete_begin(self):
        if self.head is None:
            print('Linked List is Empty.')
            return
        if self.head.n_ref is None:
            self.head = None
            print('now list become Empty after deleting the only node')
            return
        self.head = self.head.n_ref
        self.head.p_ref = None

    def delete_end(self):
        if self.head is None:
            print('Linked List is Empty.')
            return
        if self.head.n_ref is None:
            self.head = None
            print('now list become Empty after deleting the only node')
            return
        li = self.head
        while li.n_ref.n_ref is not None:
            li = li.n_ref
        li.n_ref = None

    def delete_by_value(self, data):
        if self.head is None:
            print('linked list is empty')
            return
        if self.head.value == data:
            if self.head.n_ref is None:
                self.head = None
                print('now list become Empty after deleting the only node')
                return
            self.head = self.head.n_ref
            self.head.p_ref = None
            return
        li = self.head
        while li is not None:
            if li.value == data:
                break
            li = li.n_ref
        if li is None:
            print('can not find the data value to delete')
        else:
            li.p_ref.n_ref = li.n_ref
            if li.n_ref is not None:
                li.n_ref.p_ref = li.p_ref


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.add_begin(23)
    dll.add_begin(54)
    dll.add_end(12)
    dll.add_end(45)
    dll.add_end(66)
    dll.add_end(88)
    dll.add_after(22, 88)
    dll.add_before(37, 22)
    dll.add_before(38, 54)
    dll.add_before(38, 4)
    dll.delete_end()
    dll.delete_begin()
    dll.delete_by_value(54)
    dll.delete_by_value(23)
    dll.delete_by_value(45)
    print('This is froward traversal')
    dll.print_dll()
    print()
    print('This is backward traversal')
    dll.print_dll_reverse()
