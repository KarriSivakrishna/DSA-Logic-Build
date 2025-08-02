class Solution:
    def generate(self, numRows):
        triangle = []  # This will store the final result

        for i in range(numRows):
            row = [1] * (i + 1)  # Start with all 1s in the row

            # Update values inside the row (not the first or last)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)  # Add the row to the triangle

        return triangle
