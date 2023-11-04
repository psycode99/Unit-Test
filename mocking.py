from unittest.mock import Mock


def side_effect():
    print('Updating Database')


def main():
    mock = Mock(side_effect=side_effect)
    mock()

main()