import InsersionSort

def test_unsorted():
    # test unsorted list
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    assert InsersionSort.insertion_sort(unsorted_list) == [11, 12, 22, 25, 34, 64, 90]

def test_sorted():
    # test sorted list
    sorted_list = [11, 12, 22, 25, 34, 64, 90]
    assert InsersionSort.insertion_sort(sorted_list) == [11, 12, 22, 25, 34, 64, 90]

def test_reverse():
    # test reversed list
    Reversed_List = [90, 11, 22, 12, 25, 34, 64]
    assert InsersionSort.insertion_sort(Reversed_List) == [11, 12, 22, 25, 34, 64, 90]

def test_empty():
    # test empty list
    Empty_List = []
    assert InsersionSort.insertion_sort(Empty_List) == []

def test_duplicatelements():
    # test duplicate elements list
    duplicatelements_List = [64, 64, 34, 25, 12, 22, 11, 90]
    assert InsersionSort.insertion_sort(duplicatelements_List) == [11, 12, 22, 25, 34, 64, 64, 90]
