from .hashmap import Hashmap

def test_get_apple():
    hashmap =  Hashmap()
    hashmap.add("apple", "Used for apple sauce")

    actual = hashmap.find("apple")
    expected = "Used for apple sauce"

    assert actual == expected

def test_internals():
    hashmap = Hashmap()
    hashmap.add("ahmad", 30)
    hashmap.add("silent", True)
    hashmap.add("listen", "to him")

    actual = []

    for bucket in hashmap._buckets:
        if bucket:
            actual.append(bucket.display())
    expected = [[["silent", True], ["listen", "to him"]], [["ahmad", 30]]] 

    assert actual == expected