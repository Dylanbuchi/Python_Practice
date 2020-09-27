import json


def read_list_json(filename):
    data = json.load(open(filename))
    for dic in data['names']:
        print(f"name: {dic['name']} age: {dic['age']}")
    return data


def read_simple_json(filename):
    data = json.load(open(filename))
    return data


def create_json_file(data, filename):
    json.dump(data, open(filename, 'w'), indent=4, sort_keys=True)


def append_json_list(data, filename):
    dic = read_list_json(filename)
    temp = dic['names']
    temp.append(data)
    create_json_file(dic, filename)


if __name__ == "__main__":

    path = r'./modules/files/'
    numbers_file = 'numbers.json'

    names_file = 'names.json'

    data = {'name': 'Yuri', 'age': 23}
    create_json_file(data, rf'{path}{numbers_file}')
    append_json_list(data, rf'{path}{names_file}')

    read_simple_json(rf'{path}{numbers_file}')
    read_list_json(rf'{path}{names_file}')
