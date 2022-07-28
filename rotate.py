"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #14 - Image Rotation (rotate.py)


Author: Wonjun Lee

Difficulty Level: 7/10

Prompt: Our RACECAR captured an image represented by an n x n matrix, where each 
cell is a pixel represented by an integer. However, when we attached the camera to 
the RACECAR, we rotated the camera 90 degrees to the left. Therefore, when reading 
an image, we have to rotate each pixel 90 degrees to the right to get the right 
value. Given an n x n matrix, write a function that rotates each cell 90 degrees to the right.

Constraints: 1 <= n <= 10 ; Don’t Use Numpy For This!!!

Test Cases:
Input = [[1,2],[3,4]] ;                                     Output = [[3,1],[4,2]]
Input = [[1,2,3], [4,5,6], [7,8,9]] ;                       Output = [[7,4,1], [8,5,2], [9,6,3]]
Input = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] ;  Output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

class Solution:
    def rotate(self,matrix):
        # type matrix: List[List[int]]
        # return: List[List[int]]
        m = []
        for i in range(0, len(matrix)):
            m.append(matrix[:, i])
        return m
        # TODO: Write code below to return a nested list with the solution to the prompt
        pass

def main():
    array1 = input().split(" ")
    array2 = input().split(" ")
    array3 = input().split(" ")
    array4 = input().split(" ")
    array5 = input().split(" ")


    for x in range (0, len(array1)):
        array1[x] = int(array1[x])

    for x in range (0, len(array2)):
        array2[x] = int(array2[x])

    if len(array5) > 1:
        for x in range (0, len(array3)):
            array3[x] = int(array3[x])

        for x in range (0, len(array4)):
            array4[x] = int(array4[x])

        for x in range (0, len(array5)):
            array5[x] = int(array5[x])

        matrix = [array1,array2,array3,array4,array5] 

    elif len(array4) > 1:
        for x in range (0, len(array4)):
            array4[x] = int(array4[x])

        for x in range (0, len(array3)):
            array3[x] = int(array3[x])

        matrix = [array1,array2,array3,array4] 

    elif len(array3) > 1:
        for x in range (0, len(array3)):
            array3[x] = int(array3[x])
        matrix = [array1,array2,array3]

    else:
        matrix = [array1,array2]  

    tc1 = Solution()
    ans = tc1.rotate(matrix)
    print(ans)

if __name__ == "__main__":
    main()