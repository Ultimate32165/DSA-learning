# ==================================================

def gcd(a, b):

    # Find Minimum of a and b
    result = min(a, b)

    while result > 0:
        if a % result == 0 and b % result == 0:
            break
        result -= 1

    # Return gcd of a and b
    return result


if __name__ == '__main__':
    a = 60
    b = 32
    print(gcd(a, b))

# ==================================================
# [Approach - 2] Euclidean Algorithm using Subtraction - O(min(a,b)) Time and O(min(a,b)) Space
# ==================================================
