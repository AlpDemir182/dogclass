class Dog():
    no_legs = 4
    no_ears = 2
    no_nose = 1
    no_eyes = 2
    no_tail = 1

    def bark(self):
        print("Woof Woof!")

    def play(self):
        print("play with ball")

boomer = Dog()
golden_retriever = Dog()
german_shepherd = Dog()

print(boomer.no_eyes)
print(boomer.no_legs)
print(boomer.no_ears)
print(boomer.no_tail)
print(boomer.no_nose)
print(boomer.play())
print(boomer.bark())

print(boomer.bark())
print(golden_retriever.bark())
print(german_shepherd.bark())
