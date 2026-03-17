from Vehicle import Dog, Cat

def main():
    dog = Dog("Rex", 3)
    cat = Cat("Murka", 2)

    animals = [dog, cat]

    for animal in animals:
        print(animal)
        print(animal.info())
        print(animal.speak())
        print("------")

if __name__ == "__main__":
    main()