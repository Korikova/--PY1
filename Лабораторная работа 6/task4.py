import json

INPUT_FILE = "input.csv"
# был изменен файл input.csv


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as file:
        dict_ = []
        for index, line in enumerate(file):
            line_ = line.strip(new_line).split(delimiter)
            if index == 0:
                headers = line_
                continue
            dict_.append({})   # добавляем новый словарь
            for i, _ in enumerate(headers):
                dict_[-1][headers[i]] = line_[i]
    return dict_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
