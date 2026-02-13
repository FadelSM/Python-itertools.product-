from itertools import product

def solve():
    # Read the first line, split by space, and convert to integers
    a = list(map(int, input().split()))
    
    # Read the second line, split by space, and convert to integers
    b = list(map(int, input().split()))
    
    # Compute the cartesian product
    result = product(a, b)
    
    # Print the tuples separated by spaces
    # The * operator unpacks the product object into individual arguments for print
    print(*result)

if __name__ == "__main__":
    solve()
