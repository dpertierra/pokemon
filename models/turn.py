class Turn:
    def __init__(self):
        self.command1 = None
        self.command2 = None

    def canStart(self):
        return self.command1 and self.command2
