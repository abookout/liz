import liz

def assertTrue(val):
    try:
        assert val == True
    except AssertionError:
        print(f"assertTrue failed: {val}")

def assertEqual(a, b):
    try:
        assert a == b
    except AssertionError:
        print(f"assertEqual failed: {a} != {b}")


def main():
    assertTrue(liz.check_sublist(['b', 'c'], ['a', 'b', 'c']))
    assertEqual(liz.get_phones("liz"), ["L", "IH", "Z"])


if __name__ == "__main__":
    main()