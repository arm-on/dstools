def train_test_dev_split(items, train, test, dev):
    assert train+test+dev==100, "partitions should sum to 100"
    num_items = len(items)
    num_train = int(num_items*train/100)
    num_test = int(num_items*test/100)
    train_items = items[:num_train]
    test_items = items[num_train:num_train+num_test]
    dev_items = items[num_train+num_test:]
    return train_items, test_items, dev_items

