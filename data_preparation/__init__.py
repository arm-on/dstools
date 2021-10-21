def train_test_dev_split(items, train, test, do_shuffle=True):
    '''
    Split the data into training, testing, and development sets
    '''
    dev = 100-(train+test)
    from sklearn.model_selection import train_test_split
    train_items, temp_items = train_test_split(items, test_size=(test+dev)/100, random_state=42)
    test_items, dev_items = train_test_split(items, test_size=dev/(dev+test), random_state=42)
    return train_items, test_items, dev_items