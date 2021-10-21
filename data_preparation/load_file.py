def load_file(path, format='unknown'):
    import json
    import pandas as pd
    '''
    Load a file into a variable
    '''
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