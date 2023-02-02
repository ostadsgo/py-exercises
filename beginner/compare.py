"""
Compare tow integers
Parameters:
-----------
n: int
    An integer number

Return
------
outs: int
    if x bigger than y return 1
    if x and y equal 0 return: return 0
    otherwise return -1
"""

def compare(x, y):
    pass

# -----------------------------------
def run_test():
    fn_name = "compare"
    # Tests
    tests = {
        "test#1": {"param": (2, 3), "result": -1},
        "test#2": {"param": (0, 5), "result": -1},
        "test#3": {"param": (-1, -5), "result": 1},
        "test#4": {"param": (4, 0), "result": 1},
        "test#4": {"param": (0, 0), "result": 0},
    }

    for name, value in tests.items():
        param = value["param"] if value.get("param") is not None else ()
        result = value.get("result")
        r = compare(*param)
        if r == result:
            print(f"✅{name.upper()} passed.")
        else:
            print(f"❌{name.upper()} failed.")
            print(f"{fn_name}{param} Expect {result} but got {r}")
        

if __name__ == "__main__":
    run_test()
