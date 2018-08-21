'''# Exercise: int set'''



class intSet(object):
    '''An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once.'''

    def __init__(self):
        '''Create an empty set of integers'''
        self.vals = []

    def insert(self, e_input):
        '''Assumes e is an integer and inserts e into self'''
        if not e_input in self.vals:
            self.vals.append(e_input)

    def member(self, e_input):
        '''Assumes e is an integer
           Returns True if e is in self, and False otherwise'''
        return e_input in self.vals

    def remove(self, e_input):
        '''Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self'''
        try:
            self.vals.remove(e_input)
        except:
            raise ValueError(str(e_input) + ' not found')

    def __str__(self):
        '''Returns a string representation of self'''
        self.vals.sort()
        return '{' + ','.join([str(e_input) for e_input in self.vals]) + '}'

    def intersect(self, other):
        '''combining the inputs'''
        list1 = intSet()
        for i in self.vals:
            if other.member(i):
                list1.insert(i)
        return list1

    def __length__(self):
        '''returning the length of the input'''
        return len(self)

# Your task is to define the following two methods for the intSet class:
#   1. Define an intersect method that returns a new intSet containing
#   elements that appear in both sets. In other words,
#      would return a new intSet of integers that appear in both s1 and s2.
#    Think carefully - what should happen if s1 and s2 have no
#      elements in common?

#   2. Add the appropriate method(s) so that len(s) returns the number of elements in s.

def main():
    '''main class'''
    set_a = intSet()
    set_b = intSet()
    data = input()
    data1 = input()
    l1_input = data.split()
    l2_input = data1.split()
    for i in l1_input:
        set_a.insert(int(i))
    for j in l2_input:
        set_b.insert(int(j))
    print(set_a.intersect(set_b))

if __name__ == "__main__":
    main()
