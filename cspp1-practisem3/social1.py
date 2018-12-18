def follow(network, p1, p2):
	if p1 in network:
		network[p1] = network[p1] + [p2]
	else:
		network[p1] = [p2]
	return network

def unfollow(network, p1, p2):
	if p1 in network:
		network[p1].remove(p2)
		network.update()
	return network

def delete(network, p1):
	if p1 in network:
		del network[p1]
		for key in network:
			if p1 in network[key]:
				network[key].remove(p1)
	return network

def main():
	network = eval(input())
	lines = int(input())
	for i in range(lines):
		i += 1
		line = input()
		output = line.split(" ")
		if output[0] == "follow":
			network = follow(network, output[1], output[2])
		elif output[0] == "unfollow":
			network = unfollow(network,output[1],output[2])
		else:
			network = delete(network, output[1])

	print(network)


if __name__ == "__main__":
    main()