def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    answer = answer.strip().lower()

    if check(answer):
        print("Yes")
    else:
        print("No")

def check(a):
    if a == "42" or a == "forty-two" or a == "forty two":
        return True
    else:
        return False

main()
