import bubblesort

def test_unsorted():
    # test unsorted list
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    assert bubblesort.bubble_Sort(unsorted_list) == [11, 12, 22, 25, 34, 64, 90]

def test_sorted():
    # test sorted list
    sorted_list = [11, 12, 22, 25, 34, 64, 90]
    assert bubblesort.bubble_Sort(sorted_list) == [11, 12, 22, 25, 34, 64, 90]

def test_reverse():
    # test reversed list
    Reversed_List = [90, 11, 22, 12, 25, 34, 64]
    assert bubblesort.bubble_Sort(Reversed_List) == [11, 12, 22, 25, 34, 64, 90]

def test_empty():
    # test empty list
    Empty_List = []
    assert bubblesort.bubble_Sort(Empty_List) == []

def test_duplicatelements():
    # test duplicate elements list 
    duplicatelements_List = [64, 64, 34, 25, 12, 22, 11, 90]
    assert bubblesort.bubble_Sort(duplicatelements_List) == [11, 12, 22, 25, 34, 64, 64, 90]