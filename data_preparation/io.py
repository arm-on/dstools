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
    def load_csv():
        with open(path) as f:
            first_line = f.readline()
        columns = first_line.split(',')
        columns = [c.replace('.','') for c in columns]
        no_header = False
        for c in columns:
            if c.isnumeric():
                no_header = True
                break
        if no_header == True:
            return pd.read_csv(path, header=None)
        return pd.read_csv(path)
    def load_txt_line_by_line():
        with open(path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        data = [line.strip() for line in data]
        return data
    format = path.split('.')[-1] if format=='unknown' else format
    if format == 'csv':
        return load_csv()
    elif format == 'json':
        return load_json()
    elif format == 'txt':
        return load_txt_line_by_line()
    else:
        raise ValueError('format not supported')

def write_file(var, path, format='unknown'):
    import json
    import pandas as pd
    '''
    Write a variable into a file
    '''
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