'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie
    '''
    string_dict = {}
    for i in data:
        res = data.split("\n")
        res = res[:len(res)-1]
        for k,v in enumerate(res):
            res[k] = v.split("follows ")
            if res[k][0] not in string_dict:
                string_dict[res[k][0]] = res[k][1].split(',')
            else:
                string_dict[res[i][0]].append(res[k][1].split(','))
        return string_dict
    return string_dict

def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(string))

if __name__ == "__main__":
    main()
