class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        hashmap = {1: "I", 5: "V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        roman = ""
        nums = str(num)
        if len(nums) == 4:
            roman += int(nums[0]) * hashmap[1000]
            nums = nums[1:]
        if len(nums) == 3:
            if int(nums) >= 500:
                if nums[0] == '9':
                    roman += "CM"
                else:
                    roman += hashmap[500] + (int(nums[0])-5) * hashmap[100]
            else:
                if nums[0] == '4':
                    roman += "CD"
                else:
                    roman += int(nums[0]) * hashmap[100]
            nums = nums[1:]
        if len(nums) == 2:
            if int(nums) >= 50:
                if nums[0] == '9':
                    roman += "XC"
                else:
                    roman += hashmap[50] + (int(nums[0])-5) * hashmap[10]
            else:
                if nums[0] == '4':
                    roman += "XL"
                else:
                    roman += int(nums[0]) * hashmap[10]
            nums = nums[1:]

        if len(nums) == 1:
            if int(nums) >= 5:
                if nums[0] == '9':
                    roman += "IX"
                else:
                    roman += hashmap[5] + (int(nums[0])-5)* hashmap[1]
            else:
                if nums[0] == '4':
                    roman += "IV"
                else:
                    roman += int(nums[0]) * hashmap[1]

        return roman

            
