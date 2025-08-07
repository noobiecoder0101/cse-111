

def read_list(filename):
    list_o_stuff = []
    with open(filename, "rt") as province_file:
        for line in province_file:
            good_line = line.strip()
            list_o_stuff.append(good_line)

    return list_o_stuff

def main():
    p_list = read_list("provinces.txt")
    poped_list = p_list.pop(0)
    p_list.pop(-1)
    for i in range(len(p_list)):
        if p_list[i] == "AB":
            p_list[i] = "Alberta"
    count = p_list.count("Alberta")
    print (count)