# from django.test import TestCase
#
#
# # # Create your tests here.
# # for i in range(20):
# #     if i == 9:
# #         break
# #     print(i)
# #     else:
# #         print("循环结束")
# #
# import re
#
# a = "I am a smart boy"
# num = 's\nmss'
# print(num.strip())
# # b = re.sub(r'\s', '', a)
# # print(b)
# # list1 = [i for i in b]
# # print(list1)
# list2 = [i for i in a.split('a')]
# print(list2)
# li = [1, 2, 3]
# num = li.sort()
# print(li)
#
# # class Solution(object):
# #     def twoSum(self, nums, target):
# #         li2 = []
# #         for i in range(len(nums)):
# #             for j in range(i + 1, len(nums)):
# #                 if nums[i] == nums[j]:
# #                     li2 = [i for i in range(len(nums)) if nums[i] + nums[j] == target]
# #                 elif nums[i] + nums[j] == target:
# #                     li2.append(nums.index(nums[i]))
# #                     li2.append(nums.index(nums[j]))
# #         return li2
# #
# #
# # nums = [2, 5, 5, 11]
# # target = 10
# # s = Solution()
# # print(s.twoSum(nums, target))
#
# # class Solution(object):
# #     def reverse(self, num):
# #         if num:
# #             return 1
# #         try:
# #             num > 100
# #         except:
# #             return 2
# #
# #
# # s = Solution()
# # print(s.reverse(123))
# #
# # import re
# #
# # num = input("请输入一个字符串:")
# #
# # if re.findall(r'^13\d{9}$', num):
# #     print("这是正确的！！！")
# # else:
# #     print("错误")