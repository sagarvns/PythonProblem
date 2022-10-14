class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def addFirst(self, value):
        newnode = ListNode(value)
        newnode.next = self.head
        self.head = newnode

    def lastNode(self):
        start = self.head
        if start is None:
            return None
        while start.next is not None:
            start = start.next
        return start.value

    def addLast(self, newvalue):
        newnode = ListNode(newvalue)
        start = self.head
        if start is None:
            self.head = newnode
            return

        while start.next is not None:
            start = start.next
        start.next = newnode

    def traverse(self):
        start = self.head
        while start is not None:
            print(start)
            start = start.next
        print()

    def __len__(self):
        count = 0
        start = self.head
        while start is not None:
            count += 1
            start = start.next
        return count

    def sum(self):
        sum = 0

        start = self.head
        while start is not None:
            sum += start.value
            start = start.next
        return sum

    def find(self, value):
        start = self.head
        while start is not None:
            if start.value == value:
                return True
            start = start.next
        return False


# .62 vs 1.58 vs .66
head = LinkedList()
for i in range(1, 7):
    head.addLast(i)

head.traverse()
print(head.lastNode())

# print(len(head))
# print(head.sum())
# print(head.find(74))
