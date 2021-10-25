def kaggle_link(file_path):
    '''
    Given a file path, outputs the direct link to that file over the internet
    '''
    from IPython.display import FileLink
    return FileLink(file_path)