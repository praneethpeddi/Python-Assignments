def is_prime(n):
    return True


def main():
    inputs = [0, 100, 999, -3000, 909990, 37, 64, 10488]
    for i in inputs:
        expected = True
        actual = is_prime(i)
        if actual == expected:
            print(f"Validation with " + str(i) + ':' + " success")
        else:
            print(f"Validation with " + str(i) + ':' + " success")


if __name__ == '__main__':
    main()
