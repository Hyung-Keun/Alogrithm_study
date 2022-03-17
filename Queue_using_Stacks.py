class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def empty(self):
        return self.output and self.input is None

    def push(self, x):
        self.input.append(x)

    #왜이리도 어렵게 구현하는건지참... 난 peek부분없이구현함..
    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

    def empty(self):
        return self.input == [] and self.output == []

    
