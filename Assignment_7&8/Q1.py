class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        
        current = self.head
        if not current:
            print("Linked list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_end(self, data):
        
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, data):
        
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        
        current = self.head

       
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"Node with value {key} not found.")
            return

        prev.next = current.next
        current = None

ll = LinkedList()

while True:
    print("\nChoose an option:")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Delete node")
    print("4. Display linked list")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        value = int(input("Enter value to insert at beginning: "))
        ll.insert_at_beginning(value)
    elif choice == "2":
        value = int(input("Enter value to insert at end: "))
        ll.insert_at_end(value)
    elif choice == "3":
        value = int(input("Enter value to delete: "))
        ll.delete_node(value)
    elif choice == "4":
        ll.display()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
