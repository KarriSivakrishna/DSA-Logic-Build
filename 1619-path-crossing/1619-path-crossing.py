class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = set()
        visited.add((0, 0))

        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            else:
                x -= 1

            current_pos = (x, y)
            if current_pos in visited:
                return True  # Path crosses itself
            else:
                visited.add(current_pos)

        return False  # Path does not cross itself
