class Solution:
    def __init__(self, radius, x_center, y_center):
        self.r  = radius
        self.xc = x_center
        self.yc = y_center
        

    def randPoint(self):
        xs = 2.*self.r*random.random() - self.r
        ys = 2.*self.r*random.random() - self.r
        while xs**2 + ys**2 > self.r**2:
            xs = 2.*self.r*random.random() - self.r
            ys = 2.*self.r*random.random() - self.r
        return [self.xc + xs, self.yc + ys]