# Problem 832: Flipping an Image
# Difficulty: Easy
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        """
            U:
                I: 2D array
                O: 2D array
                C: N/A
                E: An empty image -> an empty array
            P:
                loop through every row, invert it and then flip it
            I:
        """
        flippedImage = []
        for row in image:
            flippedRow = []
            row = list(map(lambda x: int(not x), row))
            for col in range(len(image[0]) - 1, -1, -1):
                flippedRow.append(row[col])
            flippedImage.append(flippedRow)
        return flippedImage

                