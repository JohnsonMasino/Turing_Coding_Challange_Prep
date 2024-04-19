"""
This code sums the item in the second array
to the last item in the first array and prints
the final array with the summed integer as the
last item in the first array replacing the initial
last item in it.

Code developed by Masino
"""

class Solution():
    def merge(self, arr1, arr2):
        merged = arr1[2] + arr2[0]
        arr1.pop(-1)
        arr1.append(merged)
        return arr1
    
    def show(self):
        a1 = [1,2,3]
        a2 = [1]
        print(self.merge(a1, a2))

if __name__ == "__main__":
    Solution().show()
print('\nCode developed by Masino')

"""
# AI code:
class Solution():
    def merge(self, arr1, arr2):
        arr1[-1] += arr2[0]  # Add the first item of arr2 to the last item of arr1
        return arr1
    
    def show(self):
        a1 = [1, 2, 3]
        a2 = [1]
        print(self.merge(a1, a2))

if __name__ == "__main__":
    Solution().show()"""