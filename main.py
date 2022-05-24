# Program : main
# Description : excecute square_of
# Date : 27/05/22
# Author : Christophe LAGAILLARDE
# Version : 1.0

from square_of import square_of


def main() -> None:
    try:
        print(square_of(int(input("Input a number, we will tell it's square: "))))
    except ValueError:
        print("only integer")


if __name__ == "__main__":
    main()


