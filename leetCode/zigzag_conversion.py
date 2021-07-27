

# 14 = (3*2+(3-2)) * 2 - 3
# 14 = (4*2+(4-2)) * 2 - 4
# 14 = (5*2+(5-2)) * 2 - 5

# nrows*4 + (nrows-2) *n_repetitions - (n_repetitions-1)*nrows
# all = nrows*3 - 2*n_repetitions
# n_repetitions = int((all - nrows*3)/2) + 1
# 3 = int((14 - 3 * 3) / 2) + 1
# 2 = int((14 - 4 * 3) / 2) + 1
# 1 = int((14 - 5 * 3) / 2) + 1
# all = 5*3 - 2 = 13 < 14
# n_cols = n_repetitions*nrows - n_repetitions + 1

# all = n_rows * n_cols - (n_rows - 1) * x



# nrows = 3
# length = 14
# -> ncols = 7
#     P       A       H       N
#     A   P   L   S   I   I   G
#     Y       I       R
# index : 0 -> 0
#         4 -> 1
#         8 -> 2
#         12 -> 3

#         1 -> 4
#         3 -> 5
#         5 -> 6
#         7 -> 7
#         9 -> 8
#         11 -> 9
#         13 -> 10

#         2 -> 11
#         6 -> 12
#         10 -> 13

# if nrows = 4:
#     ncols = 7
#     P           I           N
#     A       L   S       I   G
#     Y   A       H   R
#     P           I
# index:
#         0 -> 0
#         6 -> 1
#         12 -> 2

#         1 -> 3
#         5 -> 4
#         7 -> 5
#         11 -> 6
#         13 -> 7

#         2 -> 8
#         4 -> 9
#         8 -> 10
#         10 -> 11

#         3 -> 12
#         9 -> 13

#     P               H
#     A           S   I
#     Y       I       R
#     P   L           I   G
#     A               N

# # my naive solution
# def convert(s: str, n_rows: int) -> str:
#     final_s = ""
#     n = len(s)
#     if n_rows == 1:
#         return s
#     if n_rows == 2:
#         n_cols = int(n/2) + 1;
#     else:
#         if (n - n_rows*3)/2 <= 0 and (n - n_rows*3)/2 >= -1:
#             n_repetitions = 2
#         elif (n - n_rows*3)/2 < -1:
#             n_repetitions = 1
#         elif (n - n_rows*3)/2 < 1 and (n - n_rows*3)/2 > 0:
#             n_repetitions = 2
#         else:
#             n_repetitions = int((n - n_rows*3)/2) + 1
#         n_cols = n_repetitions*n_rows - n_repetitions + 1

#     matrix = []

#     for i in range(n_rows):
#         temp = []
#         for j in range(n_cols):
#             temp.append("")
#         matrix.append(temp)
#     direction = "down" # up
#     row = 0
#     col = 0
#     count = 0
#     print(n_rows, n_cols, n, n_repetitions)
#     while (count < n):
#         print(row, col, count)
#         matrix[row][col] = s[count]
#         count += 1

#         if row <= 0:
#             direction = "down"
#         if row >= n_rows - 1:
#             direction = "up"

#         if direction == "down":
#             row = row + 1
#         elif direction == "up":
#             col = col + 1
#             row = row - 1

#     convert_s = ""
#     for i in range(n_rows):
#         for j in range(n_cols):
#             convert_s+=matrix[i][j]

#     return convert_s

def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # index of the current row of outp list
        lin = 0
        # this variable is used to keep track of zigzag location
        # by moving between rows of outp list
        pl = 1
        # create a list of string with numRows element to store the result
        # as we step following the zigzag direction
        outp = [""] * numRows
        # loop through the strings
        for i in range(len(s)):
            # add current character to appropriate row (current row, we change the row when hit top or bottom)
            outp[lin] += s[i]
            # if numRows > 1 -> do the zigzag,
            # otherwise keep the result the same as input text
            if numRows > 1:
                lin += pl
                # change the direction (row) when reach top or bottom
                if lin == 0 or lin == numRows -1:
                    pl *= -1
        outputStr = ""
        for j in range(numRows):
            outputStr += outp[j]
        return outputStr
if __name__ == "__main__":

    s= "jeidmnjgga;dpeeq"

    # expected output: PAHNAPLSIIGYIR
    print(convert(s, 3) )

