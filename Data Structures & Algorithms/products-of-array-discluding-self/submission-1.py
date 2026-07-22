class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hashset = set()
        if len(nums) == 1:
            return nums
        res = []
        low, high = 0, len(nums)
        for i in range(len(nums)):
            product_is_zero = False
            product = 0
            hashset.add(i)
            print(f'This is nums[i]: {nums[i]}')
            for j in range(high - low):
                print(f'This is nums[j]: {nums[j]}')
                if j not in hashset:
                    if nums[j] == 0:
                        print('I GET HERE')
                        product_is_zero = True
                    if product == 0:
                        product = nums[j]
                        print(f'Setting product: {product}')
                        continue
                    if product != 0:
                        product = product * nums[j]
                        print(f'This is the accumilating product: {product}')
            print(f'This is the product: {product}')
            if product_is_zero == True:
                res.append(0)
                hashset.remove(i)
                continue
            res.append(product)
            hashset.remove(i)
        return res
                

        