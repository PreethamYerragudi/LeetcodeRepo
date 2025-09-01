# Problem 661: Image Smoother
# Difficulty: Easy
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def isValid(cell):
            x, y = cell
            return x >= 0 and y >= 0 and x < len(img) and y < len(img[0])
        dirs = [
            (0,0),
            (1,0),
            (0,1),
            (-1,0),
            (0,-1),
            (1,1),
            (1,-1),
            (-1,1),
            (-1,-1),
        ]
        new_img = [[0] * len(img[0]) for _ in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[0])):
                cells = []
                for dir in dirs:
                    if isValid((i + dir[0], j + dir[1])):
                        cells.append(img[i + dir[0]][j + dir[1]])
                new_img[i][j] = sum(cells) // len(cells)
        return new_img