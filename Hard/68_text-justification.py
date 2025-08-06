# Problem 68: Text Justification
# Difficulty: Hard
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        sum = len(words[0])
        arr = []
        temp_arr = [words[0]]
        for i in range(1, len(words)):
            word = words[i]
            sum += len(word) + 1
            if sum > maxWidth:
                arr.append(temp_arr.copy())
                sum = len(word)
                temp_arr.clear()
            temp_arr.append(word)
        if temp_arr:
            arr.append(temp_arr)

        ans = []

        for i in range(len(arr)):
            string = " ".join(arr[i])
            num_spaces = maxWidth - len(string)
            if i == len(arr) - 1:
                ans.append(string + " " * num_spaces)
            else:
                spaces = (
                    num_spaces
                    if (len(arr[i]) - 1) == 0
                    else num_spaces // (len(arr[i]) - 1) + 1
                )
                print(spaces)
                remainder = (
                    0 if (len(arr[i]) - 1) == 0 else num_spaces % (len(arr[i]) - 1)
                )
                string = ""
                for j in range(len(arr[i])):
                    if j == len(arr[i]) - 1:
                        if len(arr[i]) != 1:
                            string += arr[i][j]
                        else:
                            string += arr[i][j] + (" " * (spaces))
                    else:
                        if j < remainder:
                            string += arr[i][j] + (" " * (spaces + 1))
                        else:
                            string += arr[i][j] + (" " * (spaces))
                ans.append(string)

        return ans
