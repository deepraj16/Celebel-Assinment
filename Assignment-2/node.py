class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Add a node to the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        """Print the entire list"""
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index)"""
        if not self.head:
            raise IndexError("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index must be 1 or greater.")

        if n == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            print(f"Deleted node at index {n}: {deleted_data}")
            return

        curr = self.head
        count = 1
        while curr and count < n - 1:
            curr = curr.next
            count += 1

        if not curr or not curr.next:
            raise IndexError("Index out of range.")

        deleted_data = curr.next.data
        curr.next = curr.next.next
        print(f"Deleted node at index {n}: {deleted_data}")


# ----------- Test Code -----------
if __name__ == "__main__":
    ll = LinkedList()

    # Adding sample data
    print("Adding nodes to list:")
    for i in [10, 20, 30, 40, 50]:
        ll.add_node(i)
        ll.print_list()

    print("\nDeleting 3rd node (value 30):")
    ll.delete_nth_node(3)
    ll.print_list()

    print("\nAttempting to delete node at index 10 (out of range):")
    try:
        ll.delete_nth_node(10)
    except IndexError as e:
        print("Error:", e)

    print("\nDeleting 1st node (head node):")
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nClearing list and attempting to delete from empty list:")
    # Clear list
    while True:
        try:
            ll.delete_nth_node(1)
        except IndexError as e:
            print("Error:", e)
            break
    ll.print_list()
