class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Adds an element to the end of the queue."""
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Removes and returns the front element of the queue."""
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        return self.items.pop(0)

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.items) == 0

    def display(self):
        """Displays the queue elements."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue:", " <- ".join(map(str, self.items)))

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print("Dequeued:", q.dequeue())
q.display()
