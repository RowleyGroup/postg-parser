from numpy import matrix

class Coefficients(matrix):
    def __init__(self, postg_data):
        self.postg_data = postg_data
