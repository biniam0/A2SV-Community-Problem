if __name__ == '__main__':
    N = int(input())
    result = []

    for i in range(N):
        command = list(input().split())
        idx = 0
        if len(command) > 1:
            idx = command[1]
        val = command[-1]
        if command[0] == "insert":
            result.insert(int(idx), int(val))
        elif command[0] == "remove":
            result.remove(int(val))
        elif command[0] == "append":
            result.append(int(val))
        elif command[0] == "sort":
            result.sort()
        elif command[0] == "pop":
            result.pop()
        elif command[0] == "reverse":
            result.reverse()
        else:
            print(result)
