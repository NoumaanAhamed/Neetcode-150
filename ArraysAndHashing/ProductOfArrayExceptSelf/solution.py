# def productExceptSelf(nums):
#     n = len(nums)
#     result = []

#     for i in range(n):
#         product = 1
#         for j in range(n):
#             if i != j:
#                product *= nums[j]
#         result.append(product)
#     print(result)

# def productExceptSelf(nums):
#     n = len(nums)
#     leftProducts = [1] * n
#     leftProduct = 1
#     rightProducts = [1] * n
#     rightProduct = 1

#     # use same result list by exchanging left and right product with result  

#     for i in range(n):
#         leftProducts[i] = leftProduct
#         leftProduct *= nums[i]

#     for i in range(n-1,-1,-1):
#         rightProducts[i] = rightProduct
#         rightProduct *= nums[i]

#     result = []
#     for i in range(n):
#         result.append(leftProducts[i]*rightProducts[i])

#     print(result)

def productExceptSelf(nums):
    total_product = 1
    zero_count = 0  # Count the number of zeroes in the array

    # Calculate the total product and count the number of zeroes
    for num in nums:
        if num != 0:
            total_product *= num
        else:
            zero_count += 1

    result = []
    for num in nums:
        if num != 0:
            if zero_count >= 1:
                result.append(0)
            else:
                result.append(total_product // num)
        elif zero_count == 1:
            # If there's only one zero in the array, the result for that index is the total product
            # Otherwise, for multiple zeroes, the result is 0 as the product will be 0.
            result.append(total_product)
        else:
            result.append(0)

    return result


productExceptSelf([1,2,3,4])