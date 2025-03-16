from MyMath import mymath

math = mymath()

print("Absolute Values")
print(f"Absolute of -10: {math.absolute(-10)}")
print(f"Absolute of 5: {math.absolute(5)}\n")

print("Average Values")
nums1 = [10, 20, 30, 40]
nums2 = [5, 15, 25]
nums3 = []

print(f"Average of {nums1}: {math.average(nums1)}")
print(f"Average of {nums2}: {math.average(nums2)}")
print(f"Average of empty list: {math.average(nums3)}")