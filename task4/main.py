import json

INPUT_FILE = "output.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, 'r') as f:
        output = []
        lines = f.read().splitlines()
        column_names = lines[0].split(',')
        for index_l, line in enumerate(lines):
            d = dict()
            if index_l == 0:
                continue
            entries = line.split(',')
            for index_r, column_name in enumerate(column_names):
                d[column_name] = entries[index_r]
            output.append(d)
    return output


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
