
def check(A):
    n = len(A)
    for i in xrange(n):
        if i <= n - 3:
            if A[i] == 1 and A[i+1] == 2 and A[i+2] == 3:
                return True
    return False

def solution(A):
    print(A, check(A))
    
def main():
    solution([1, 2, 3, 4, 5, 6, 7, 8])
    solution([0, 2, 3, 4, 5, 6, 7, 8])
    solution([-1, 0, 1, 4, 5, 6, 7, 8])
    solution([1, 3, 2, 1, 2, 6, 7, 8])
    solution([4, 6, 8, 1, 2, 3, 2, 0])
    solution([1, 2, 4, 3, 4, 6, 8, 1, 2, 3])
    
if __name__ == "__main__":
    main()
