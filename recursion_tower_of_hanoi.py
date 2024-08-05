number_of_disks = 4
A = list(range(number_of_disks, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n<= 0:
        return
    #move n-1 disks from source to auxiliary
    move(n-1, source, target, auxiliary)

    #move the nth disk form source to target
    target.append(source.pop())

    #display progress
    print(A, B, C, '\n')

    #move the n-1 disk that we left on auxiliary onto target
    move(n-1, auxiliary, source, target)

#initiate call from source A to target C with auxiliary B
move(number_of_disks, A, B, C)