# Program : test case of square_of
# Description : test the function square_of
# Date : 24/05/2022
# Author : Christophe LAGAILLARDE
# Version : 1.0

from square_of import square_of


def test_square_of():
    assert(square_of(2) < 4 or square_of(2) > 4), "The program does not work"


test_square_of()