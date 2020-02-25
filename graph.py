class Graph():
    def __init__(self):
        self.data = []
        self.diff = []
    def makeGraph(self, data):
        self.data = data
        m = int(max(self.data))
        self.diff = []
        for i in self.data:
            self.diff.append(m - i)
    
    def showGraph(self, max):
        for i in range(max):
            for j in range(len(self.diff)):
                if self.diff[j] != 0:
                    print('  ', end='')
                    self.diff[j] -= 1
                # elif self.diff[j] == -1:
                #     print('  ', end='')
                else:
                    print('■ ', end='')
                    # self.diff[j] = -1
            print()

                    