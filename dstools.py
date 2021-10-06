import json
import pandas as pd


def load_file(path, format='unknown'):
    def load_json():
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    def load_csv(header=0, delimiter=','):
        data = pd.read_csv(path, delimiter=delimiter, header=header)
        return data
    def load_txt_line_by_line():
        with open(path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        data = [line.strip() for line in data]
        return data
    format = path.split('.')[-1] if format=='unknown' else format
    if format == 'csv':
        return load_csv(path)
    elif format == 'json':
        return load_json(path)
    elif format == 'txt':
        return load_txt_line_by_line(path)
    else:
        raise ValueError('format not supported')

def write_file(var, path, format='unknown'):
    def write_json():
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(var, file)
    def write_csv():
        var.to_csv(path)
    def write_txt_line_by_line():
        with open(path, 'w', encoding='utf-8') as file:
            for idx, line in enumerate(var):
                file.write(line+'\n' if idx != len(var)-1 else line)
    format = path.split('.')[-1] if format=='unknown' else format
    if format == 'csv':
        return write_csv()
    elif format == 'json':
        return write_json()
    elif format == 'txt':
        return write_txt_line_by_line()
    else:
        raise ValueError('format not supported')