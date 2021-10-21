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