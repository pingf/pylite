class Counter:
    def __init__(self):
        self.numbers = ["one", "two", "three", "four", "five"]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration()

        item = self.numbers[self.index] 
        self.index += 1
        return item

for number in Counter():
    print(number)
