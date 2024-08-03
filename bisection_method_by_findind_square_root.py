def square_root_bisection(square_target, accuracy = 1e-7, max_iteration = 100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined.")
    if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
    elif square_target == 0:
        root = 0
        print(f"The square root of {square_target} is 0")
    
    else:
        low = 0
        high = max(1, square_target)
        root = None

        for _ in range(max_iteration):
            mid = (low + high)/2
            square_mid = mid ** 2

            if abs(square_mid - square_target) < accuracy:
                root = mid 
                break
            elif square_mid < square_target:
                low = mid
            else: 
                high = mid
        
        if root is None:
            print(f"Failed to converge within {max_iteration} iterations.")
        else:
            print(f"The square root of {square_target} is approximately {root}")
    return root

N = 23
square_root_bisection(N)