class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print('Queue overflow')
            return

        if self.front == -1:  
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = item
        print(f'Item being inserted is: {item}')

    def dequeue(self):
        if self.front == -1:
            print('Queue underflow')
            return

        removed_item = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f'Dequeued item is: {removed_item}')

    def traverse(self):
        if self.front == -1:
            print("Queue underflow")
            return

        print("Queue items:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

def main():
    size = int(input('Enter the size of the queue: '))
    q = CircularQueue(size)

    print('\n__Queue Operations__')
    print('1. Enqueue')
    print('2. Dequeue')
    print('3. Traverse')
    print('4. Exit')

    while True:
        choice = input('\nEnter your choice: ')
        if choice == '1':
            item = input('Enter value to enqueue: ')
            q.enqueue(item)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.traverse()
        elif choice == '4':
            break
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    main()
