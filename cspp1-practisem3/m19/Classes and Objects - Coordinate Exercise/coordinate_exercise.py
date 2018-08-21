'''# Exercise: coordinate'''

# Consider the following code from the last lecture video:

class Coordinate(object):
    '''class'''
    def __init__(self, x_input, y_input):
        self.x_input = x_input
        self.y_input = y_input

    def get_x_input(self):
        '''# Getter method for a Coordinate object's x_input coordinate.
        # Getter methods are better practice than just accessing an attribute directly_input'''
        return self.x_input

    def get_y_input(self):
        '''# Getter method for a Coordinate object's y_input coordinate'''
        return self.y_input

    def __str__(self):
        return '<' + str(self.get_x_input()) + ',' + str(self.get_y_input()) + '>'

    def __eq__(self, other):
        if self.get_x_input() == other.get_x_input() and self.get_y_input() == other.get_y_input():
            return True
        return False

    def __repr__(self):
        return 'Coordinate(' + str(self.get_x_input()) + ',' + str(self.get_y_input()) + ')'

# Your task is to define the following two methods for the Coordinate class:
# Add an __eq__ method that returns True if coordinates refer to same point

def main():
    '''main function'''
    data = input()
    data = data.split(' ')
    data = list(map(int, data))
    print(Coordinate(data[0], data[1]) == Coordinate(data[2], data[3]))
    print(Coordinate(data[4], data[5]).__repr__())

if __name__ == "__main__":
    main()
