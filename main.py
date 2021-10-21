import json
import pandas as pd


def load_file(path, format='unknown'):
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

def write_file(var, path, format='unknown'):
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

def gpu_tpu():
    '''
    Get the information about GPU or TPU's available
    '''
    try:
        import pynvml
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        device_name = pynvml.nvmlDeviceGetName(handle)
        return device_name
    except:
        try:
            import os
            from tensorflow.python.profiler import profiler_client

            tpu_profile_service_address = os.environ['COLAB_TPU_ADDR'].replace('8470', '8466')
            return profiler_client.monitor(tpu_profile_service_address, 100, 2)
        except:
            return 'running on CPU'


def colab_prevent_disconnection():
    '''
    Prevents Colab Session from Being Closed
    '''
    import IPython
    from google.colab import output

    display(IPython.display.Javascript('''
    function ClickConnect(){
    btn = document.querySelector("colab-connect-button")
    if (btn != null){
        console.log("Click colab-connect-button"); 
        btn.click() 
        }
    
    btn = document.getElementById('ok')
    if (btn != null){
        console.log("Click reconnect"); 
        btn.click() 
        }
    }
    
    setInterval(ClickConnect,60000)
    '''))

    print("Done.")


def kaggle_link(file_path):
    '''
    Given a file path, outputs the direct link to that file over the internet
    '''
    from IPython.display import FileLink
    return FileLink(file_path)

def train_test_dev_split(items, train, test, do_shuffle=True):
    '''
    Split the data into training, testing, and development sets
    '''
    if do_shuffle == True:
        from random import shuffle
        shuffle(items)
    all_len = len(items)
    tr_len = int(all_len*train)
    te_len = int(all_len*test)
    train_items = items[:tr_len]
    test_items = items[tr_len:tr_len+te_len]
    dev_items = items[tr_len+te_len:]
    return train_items, test_items, dev_items