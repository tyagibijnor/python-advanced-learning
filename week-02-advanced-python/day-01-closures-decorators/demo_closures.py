from closures import make_counter, make_multiplier


def main():
    double = make_multiplier(2)
    triple = make_multiplier(3)

    print("Multiplier demonstrations")
    print(double(10))
    print(triple(20))

    counter = make_counter()

    print("Counter demonstrations")
    print(counter())
    print(counter())
    print(counter())


if __name__ == "__main__":
    main()
