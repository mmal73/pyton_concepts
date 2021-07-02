if __name__ == '__main__':
    x = int(input()) + 1
    y = int(input()) + 1
    z = int(input()) + 1
    n = int(input())
    permutations = [ [i, j, k] for i in range(0, x) for j in range(0, y) for k in range(0, z) if i+j+k != n ]
    print(permutations)