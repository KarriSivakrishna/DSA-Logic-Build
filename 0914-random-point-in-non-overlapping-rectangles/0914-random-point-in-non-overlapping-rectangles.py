class Solution:

    def __init__(self, rects: 'List[List[int]]'):
        self.rects_weight = []
        self.rects = rects
        for [x1,y1,x2,y2] in rects:
            self.rects_weight.append((x2-x1+1)*(y2-y1+1))
        
    def pick(self) -> 'List[int]':
        [x1,y1,x2,y2] = random.choices(self.rects, weights = self.rects_weight)[0]
        x = random.randrange(x1,x2+1)
        y = random.randrange(y1,y2+1)
        return [x,y]