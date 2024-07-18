import json


def read_json(json_file: str) -> dict:
    with open(json_file, 'r') as f:
        return json.load(f)


if __name__ == '__main__':
    json_filepath = '../uint16_scale_factor.json'
    print(read_json(json_filepath))
    # {'key': 'value'}
