## #11 Container With Most Water
## Data: 2017.1.13

class Solution(object):
    def maxArea(self, height):
        left_index, right_index = 0, len(height) - 1
        calcuV = lambda i, i_height, j, j_height: \
            (j - i) * min(i_height, j_height)
        container = calcuV(left_index, height[left_index],
                           right_index, height[right_index])
        while left_index < right_index :
            if height[left_index] < height[right_index]:
                left_index += 1
            else :
                right_index -= 1
            new_container = calcuV(left_index, height[left_index],
                           right_index, height[right_index])
            container = new_container if new_container > container else container
        return container
