def makeunique(key, current_dict):
    version = 2
    new = str(key)

    while new in current_dict:
        new = key + str(version)
        version += 1

    return new

def parse(file, level=0):
    current_dict = dict()
    for line in file:
        line = line.replace(" ", "")

        if "{" in line:
            key = line.replace("{", "").replace('"', '').replace('\n', '')

            value = parse(file, level + 1)
            current_dict[makeunique(key, current_dict)] = value
            continue

        if "}" in line:
            return current_dict

        if ":" in line:
            key, value = tuple(line.replace('"', '').replace('\n', '').split(":"))
            current_dict[makeunique(key, current_dict)] = value

    return current_dict

def print_dict(dic, level=0):
    for key, value in dic.items():
        if type(value) is dict:
            print('\t' * level, key)
            print_dict(value, level + 1)
        else:
            print('\t' * level, key, ":", value)

name = 'ResNet_ScasNet.prototxt'


with open(name, 'r') as file:
    result_dict = parse(file)
    print_dict(result_dict)