class Node:
    def __init__(self, data):
        self.value = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is not None:
            g = self.head
            while g.ref is not None:
                g = g.ref
            g.ref = new_node
        else:
            self.head = new_node

    def print_ll(self):
        if self.head is None:
            print("Linked List is Empty!!!")
        else:
            n = self.head
            while n is not None:
                print(n.value, "-->", end=" ")
                n = n.ref
            # print(n.value)

    def add_after(self, data, after_what):
        if self.head is None:
            print("Can't add after as Linked List empty")
        else:
            new_node = Node(data)
            n = self.head
            while n is not None:
                if n.value == after_what:
                    break
                else:
                    n = n.ref
            if n is None:
                print("The afterWhat Data is not present")
            else:
                new_node.ref = n.ref
                n.ref = new_node

    def add_before(self, data, before_what):
        if self.head is None:
            print("Can't add as Linkedlist is Empty")
        else:
            new_node = Node(data)
            g = self.head
            if g.value == before_what:
                new_node.ref = g
                self.head = new_node
            else:
                while g is not None:
                    if g.ref.value == before_what:
                        break
                    else:
                        g = g.ref
                if g is None:
                    print('beforeWhat data is not present in the Linked List')
                else:
                    new_node.ref = g.ref
                    g.ref = new_node

    def add_before2(self, data, before_what):
        if self.head is None:
            print("Can't add as Linked List is Empty.>>>")
            return
        if self.head.value == before_what:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.value == before_what:
                break
            n = n.ref
        if n is None:
            print('after_what data is not found')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_first(self):
        if self.head is None:
            print('Empty linked List')
            return
        self.head = self.head.ref

    def delete_last(self):
        if self.head is None:
            print('Empty linked list')
            return
        if self.head.ref is None:
            self.head = None
            return
        n = self.head
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete_by_value(self, val):
        if self.head is None:
            print('Empty Linked List..')
            return
        if self.head.value == val:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.value == val:
                break
            n = n.ref
        if n.ref is None:
            print("can't find the value in the Linked List.")
        else:
            n.ref = n.ref.ref


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_end(12)
    ll.add_end(16)
    ll.add_end(77)
    ll.add_begin(44)
    ll.add_after(32, 12)
    ll.add_after(99, 77)
    ll.add_after(98, 44)
    ll.add_before2(6, 99)
    ll.add_before2(33, 44)
    ll.add_before2(33, 16)

    # this is traversal
    ll.print_ll()
    print("\n\nAfter Deleting---->\n")
    ll.delete_first()
    ll.delete_last()
    # ll.delete_last()
    # ll.delete_last()
    # ll.delete_last()
    # ll.delete_last()
    # ll.delete_last()
    # ll.delete_last()
    # ll.delete_last()
    # ll.delete_last()
    # ll.delete_last()
    ll.delete_by_value(33)
    ll.delete_by_value(77)
    ll.delete_by_value(98)
    ll.delete_by_value(12)
    ll.delete_by_value(6)
    ll.delete_by_value(55)
    ll.delete_by_value(44)
    ll.delete_by_value(32)
    ll.delete_by_value(16)
    ll.delete_by_value(55)

    # this is traversal
    ll.print_ll()
