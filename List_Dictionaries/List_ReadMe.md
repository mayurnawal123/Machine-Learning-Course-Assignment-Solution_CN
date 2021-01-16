LISTS 

From Scratch:  a = [1, 2, 3, 4, 5]

Initialize: a = [None] * 3 , b = [[] for _ in range(3)] 

Copy: >>> a = [[1], [2]] >>> b = list(a) >>> b[0][0] = 123 >>> a[[123], [2]]>>> b[[123], [2]]

DeepCopy: >>> a = [[1], [2]] >>> b = copy.deepcopy(a) >>> b[0][0] = 123 >>> a [[1], [2]] >>> b [[123], [2]]

List Comprehension : [x if x > 5 else 0 for x in range(10)]   [(x, y) for x in range(3) for y in range(2)]

enumerate

Stacks:  no separate DS needed, List has pop and append. 
class Stack: 
    def __init__(self):
        self.__list = []
    def push(self, val):
        self.__list.append(val)
    def pop(self):
        return self.__list.pop()
    def __iter__(self):
        return iter(self.__list)

stack = Stack() stack.push(1) stack.push(2)
for s in stack:
    print(s)

Sort:  l = [5, 4, 3, 2, 1] >>> l.sort() >>> l.sort(reverse = True) : It is inplace and returns none 




