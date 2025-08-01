# # [Approach - 1] Division by 2 - O(log₂(n)) Time and O(log₂(n)) Space

# # function to convert decimal to binary
# import math


# def decToBinary(n):
#     binArr = []

#     while n > 0:
#         bit = n % 2
#         binArr.append(str(bit))
#         n = n // 2

#     # reverse the string
#     binArr.reverse()
#     return "".join(binArr)


# if __name__ == "__main__":
#     n = 12
#     print(decToBinary(n))


# # [Approach - 2] Using Head Recursion - O(log₂(n)) Time and O(log₂(n)) Space

# def decToBinaryRec(n, binArr):
#     # Base Case
#     if n == 0:
#         return

#     # Recur for smaller bits.
#     decToBinaryRec(n // 2, binArr)

#     # Add MSB of current number to the binary list
#     binArr.append(str(n % 2))

# # Function to convert decimal to binary


# def decToBinary(n):
#     if n == 0:
#         return "0"

#     binArr = []
#     decToBinaryRec(n, binArr)
#     return "".join(binArr)


# if __name__ == "__main__":
#     n = 12
#     print(decToBinary(n))


# # [Approach - 3] Using Bitwise Operators - O(log₂(n)) Time and O(log₂(n)) Space


# def decToBinary(n):

#     # String to store the binary representation
#     bin = ""

#     while n > 0:
#         # Finding (n % 2) using bitwise AND operator
#         # (n & 1) gives the least significant bit (LSB)
#         bit = n & 1

#         bin += str(bit)

#         # Right shift n by 1 (equivalent to n = n // 2)
#         # This removes the least significant bit (LSB)
#         n = n >> 1

#     return bin[::-1]


# if __name__ == "__main__":
#     n = 13
#     print(decToBinary(n))


# # [Approach - 4] Using Built-in Methods - O(log₂(n)) Time and O(log₂(n)) Space


# def decToBinary(n):
#     return bin(n)[2:]


# if __name__ == "__main__":
#     n = 12
#     print(decToBinary(n))


def Dec2Bin(n):
    binArr = []
    while (n > 0):
        binArr.append(str(n % 2))
        n = n//2

    return "".join(binArr[::-1])


print(Dec2Bin(4))
