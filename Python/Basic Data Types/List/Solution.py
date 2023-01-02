if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(1, N+1):
        operation,*arg = input().split()
        value = list(map(int,arg))
        if operation == 'insert':
            lst.insert(value[0],value[1])
        elif operation == 'print':
            print(lst)
        elif operation == 'remove':
            lst.remove(value[0])
        elif operation == 'append':
            lst.append(value[0])
        elif operation == 'sort':
            lst.sort()
        elif operation == 'pop':
            lst.pop()
        elif operation == 'reverse':
            lst.reverse()
        