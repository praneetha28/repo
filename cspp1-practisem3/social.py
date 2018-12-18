def create_social_network(data):
    dictinary = {}
    for i in data:
        res = data.split("\n")
        res = res[:len(res)-1]
        for k,v in enumerate(res):
            res[k] = v.split("follows ")
            if res[k][0] not in dictinary:
                dictinary[res[k][0]] = res[k][1].split(",")
            else:
                dictinary[res[i][0]].append(res[k][1].split(","))
        return dictinary
    return dictinary



def main():
    n = int(input())
    string = ''
    for i in range(n):
        string += input()
        string += '\n'

    print(create_social_network(string))


if __name__ == "__main__":
    main()
