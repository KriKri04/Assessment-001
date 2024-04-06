class PriorityQueueNode:
    """A node in the priority queue representing an element with an ID, name, and priority level."""

    def __init__(self, id: int, name: str, priority: int) -> None:
        """
        Initializes a PriorityQueueNode with the provided ID, name, and priority.

        Args:
            id (int): The unique identifier for the node.
            name (str): The name or label associated with the node.
            priority (int): The priority level of the node.
        """
        self.id: int = id
        self.name: str = name
        self.priority: int = priority
        self.next: PriorityQueueNode = None
        self.prev: PriorityQueueNode = None

    def __str__(self) -> str:
        """
        Returns a string representation of the PriorityQueueNode.

        Returns:
            str: A string representation of the node including its ID, name, and priority level.
        """
        return f'id:{str(self.id)} name: {str(self.name)} priority: {str(self.priority)}'


class PriorityQueue:
    """A priority queue implementation using linked list."""

    def __init__(self) -> None:
        """Initializes an empty priority queue."""
        self.head = None
        self.tail = None
        self.next_id = 1  # the id-s must start from 1

    def get_next_id(self) -> int:
        """
        Returns the next available ID for a node in the priority queue.

        Returns:
            int: The next available ID.
        """
        id = self.next_id
        self.next_id += 1
        return id
    
    def is_empty(self) -> bool:
        """
        Checks if the priority queue is empty.

        Returns:
            bool: True if the priority queue is empty, False otherwise.
        """
        return self.head is None

    def insert(self, name: str, priority: int) -> None:
        """
        Inserts a new node with the given name and priority into the priority queue.

        Args:
            name (str): The name or label associated with the node.
            priority (int): The priority level of the node.
        """
        new_node = PriorityQueueNode(self.get_next_id(), name, priority)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            iter = self.head
            while iter is not None and iter.priority < priority:
                iter = iter.next
            if iter is None:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                if iter == self.head:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                else:
                    iter.prev.next = new_node
                    new_node.prev = iter.prev
                    iter.prev = new_node
                    new_node.next = iter

    def remove(self) -> tuple[int, str, int] | tuple[None, None, None]:
        """
        Removes and returns the node with the highest priority from the priority queue.

        Returns:
            tuple[int, str, int] | tuple[None, None, None]: A tuple containing the ID, name, and priority of the removed node,
                or (None, None, None) if the priority queue is empty.
        """
        if self.is_empty():
            return None, None, None
        else:
            temp = self.tail
            if self.tail == self.head:
                self.tail.prev = None
                self.head = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            return temp.id, temp.name, temp.priority
        
    def peek(self) -> PriorityQueueNode:
        """
        Returns the node with the highest priority without removing it from the priority queue.

        Returns:
            PriorityQueueNode: The node with the highest priority.
        """
        return self.tail

    def traverse(self) -> None:
        """Traverses the priority queue and prints each node."""
        if self.is_empty():
            print("Empty Queue")
        else:
            iterator = self.head
            while iterator is not None:
                print(iterator)
                iterator = iterator.next
    

if __name__ == "__main__":
    pq = PriorityQueue() 
    pq.insert("Plane 1", 1)
    pq.insert("Plane 2", 2)
    pq.insert("Plane 3", 3)
    pq.insert("Plane 4", 1)
    pq.insert("Plane 5", 2)
    pq.insert("Plane 6", 0)
    pq.insert("Plane 7", 0)
    pq.insert("Plane 8", 1)
    print()
    print(pq.peek())
    print()
    pq.traverse()
    print()
    pq.remove()
    print(pq.peek())
    pq.remove()
    print(pq.peek())
    pq.remove()
    print(pq.peek())
