#stacks
class Stack:
    def __init__(self,size):
        self.stack=[None]*size
        self.size=size
        self.top=-1
    
    def push(self,item):
        if self.top==self.size-1:
            print("stack overflow!!!")
        else:
            self.top+=1
            self.stack[self.top]=item
            print(f'{item} is pushed into the stack')

    def pop(self):
        if self.top==-1:
            print("stack is underflow!!!")
        else:
            removed=self.stack[self.top]
            self.stack[self.top]=None
            self.top-=1
            print(f'the popped item is{removed}')
    
    def peek(self):
        if self.top==-1:
            print('stack  underflow ')
        else:
            print(f'the last element in the stack is {self.stack[self.top]}')

    def display(self):
        if self.top==-1:
            print('stack  underflow')
        else:
            print('stack data')
            for i in range(self.size-1,-1,-1):
                print(self.stack[i])

    def Sum(self):
        sum = 0
        if self.top == -1:
            print("stack underflow")
        else:
            for i in range(self.top + 1):
                if self.stack[i] is not None:
                    sum += int(self.stack[i])
            print(f"sum = {sum}")
            return sum

    def display_odds(self):
        print("Odd numbers in the stack:")
        for i in range(self.top + 1):
            val = int(self.stack[i])
            if val % 2 != 0:
                print(val)

   
    def display_alternate(self):
        print("Alternate elements in the stack:")
        for i in range(0, self.top + 1, 2):
            print(self.stack[i])

    def reverse_stack(self):
        print("Stack in reversed order:")
        for i in range(self.top, -1, -1):
            print(self.stack[i])

def main():
    size=int(input('enter the size of the stack: '))
    s=Stack(size)

    print('\n__stack operations__')
    print('1. push')
    print('2. pop')
    print('3. peek')
    print('4. display')
    print('5. sum')
    print('6. display odd numbers')
    print('7. display alternate elements')
    print('8. reverse and display stack')
    print('9. exit')

    while True:
        choice=input('Enter your choice: ')
        if choice=='1':
            value=input('Enter value to push: ')
            s.push(value)
        elif choice=='2':
            s.pop()
        elif choice=='3':
            s.peek()
        elif choice=='4':
            s.display()
        elif choice=='5':
            s.Sum()
        elif choice=='6':
            s.display_odds()
        elif choice=='7':
            s.display_alternate()
        elif choice=='8':
            s.reverse_stack()
        elif choice=='19':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Choose 1-9.')

if __name__=='__main__':
    main()
