class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[1]]

        while len(lst)<numRows:

            new_row=[1]
            last_row=lst[-1]

            for i in range(len(last_row)-1):
                new_row.append(last_row[i] + last_row[i+1])

            new_row +=[1]
            lst.append(new_row)

        return lst

 #       numRows = int(input())

    #    print(pascals_triangle(numRows))

