class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

class stack:

    def __init__(self):
        self.top = None
        self.numberOfNodes = 0

    def isempty(self):
        return self.top == None
    
    def push(self, value):
        
        new_node = Node(value)

        new_node.next = self.top

        self.top = new_node

        self.numberOfNodes += 1

    def traverse(self):

        current = self.top

        while current != None:

            print(current.data)
            current = current.next

    def peek(self):
        if self.top == None:
            print('Stack is empty')
        else:
            return print(self.top.data)
        
    def pop(self):

        if (self.isempty()):
            return 'Stack Empty'
        
        else:

            data = self.top.data

            self.top = self.top.next

            self.numberOfNodes -= 1

            return data
        


def reverse_string(text):
    
    s = stack()

    for alphabet in text:
        s.push(alphabet)

    result = ''


    while (not s.isempty()):
        result = result + s.pop()

    return (result)

# def string_work(text):

#     word = 'uuurr'

#     ustack = stack()
#     rstack = stack()

#     for alphabet in text:
#         ustack.push(alphabet)

#     for letter in word:
#         if letter == "u":
#             x = ustack.pop()
#             rstack.push(x)
#         else:
#             y = rstack.pop()
#             ustack.push(y)

#     result = ''


#     while (not ustack.isempty()):
#         result =  ustack.pop() + result

#     return (result)


# print(string_work('hello'))



def find_celeb(M):

    s = stack()

    for i in range(len(M)):
        s.push(i)

    while s.numberOfNodes >= 2:

        i = s.pop()
        j = s.pop()

        if M[i][j] == 0:
            s.push(i)
        else:
            s.push(j)

        celeb = s.pop()

        for i in range(len(M)):
                if M[i][celeb] == 0 or M[celeb][i] == 1:
                    print('No one is a celebrity')

        print("The celebrity is", celeb)


M = [
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
     ]

#find_celeb(M)



def varification(equation):

    s = stack()

    for character in equation:
        if character == '(' or character == '{' or character == '[':
            s.push(character)
        elif character == ')' or character == '}' or character == ']':
            if (s.isempty()) == True:
                return print('equation is not valid')
            else:
                top = s.pop()

        if (character == ')' and top != '(') or (character == '}' and top != '{') or (character == ']' and top != '['):
            print('equation is not valid')
            return
                
            

    

    if (s.isempty()) == True:
        return (s.traverse, print('equation is valid'))
    else:
        return (s.traverse, print('equation is not valid'))
    
#varification("{[(a + b) + (c + d)]}")

s = stack()

def enqueue(value):
    
        s.push(value)

def dequeue():
    t = stack()

    values = []
    while s.isempty() != True:
        values.append(s.pop())
    
    for value in values:
        t.push(value)

    deleted_value = t.pop()

    new_values = []

    while t.isempty() != True:
        new_values.append(t.pop())
    
    for value in new_values:
        s.push(value)

    return print(deleted_value)

enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)

print(s.traverse())

dequeue()

print(s.traverse())
    










        

    



