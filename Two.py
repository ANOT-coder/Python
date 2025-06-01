class linearQueue:
    def __init__(self,size):
        self.queue=[None]*size
        self.size=size
        self.front=-1
        self.rear=-1
    
    def enqueue(self,item):
        if self.rear==self.size-1:
            print("stack overflow")
        else:
            if self.front==-1:
                self.front=0
            else:
                self.rear+=1
            self.queue[self.rear]=item
            print(f'the item to be inserted{item}')
    
    def dequeue(self):
        if self.front==-1 and self.front>self.rear:
            print("stack underflow")
        else:
            self.queue[self.front]=None
            self.front+=1
            print(f'the dequeued item is {self.queue[self.front]}')

    def traverse(self):
        if self.front==-1 and self.front>=self.rear:
            print("stack underflow")
        else:
            for i in range(self.front, self.rear+1):
                print(self.queue[i])
            print()

def main():
    size=int(input('enter the size of the queue: '))
    q=linearQueue(size)

    print('\n__queue operations__')
    print('1. enqueue')
    print('2. dequeue')
    print('3. traverse')
   

    while True:
        choice=input('Enter your choice: ')
        if choice=='1':
            item=input('Enter value to enqueue: ')
            q.enqueue(item)
        elif choice=='2':
            q.dequeue()
        elif choice=='3':
            q.traverse()
     
           
        else:
            print('Invalid choice. Choose 1-9.')

if __name__=='__main__':
    main()

    
                
