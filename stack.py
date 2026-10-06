class Stack(object):
    def __init__(self):
        self.pilha = []
    def push(self,item):
        if self.is_full() == False:
            self.pilha.append(item)
    def pop(self):
        topo = self.pilha[-1]
        del self.pilha[-1]
        return topo
    def pop_all(self):
        while not self.is_empty():
            self.pop()
    def top(self):
        return self.pilha[-1]
    def is_empty(self):
        return len(self.pilha) == 0
    def is_full(self):
        return False
    