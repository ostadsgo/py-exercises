"""
Get interger number return power of 2
Parameters:
-----------
n: int
    An integer number

Return
------
outs: int
    Return square of n
"""

def square(n):
    pass

# -----------------------------------
def run_test():
    fn_name = "add_one"
    # Tests
    tests = {
        "test#1": {"param": (2,), "result": 4},
        "test#2": {"param": (0,), "result": 0},
        "test#3": {"param": (-1,), "result": 1},
        "test#4": {"param": (4,), "result": 16},
    }

    for name, value in tests.items():
        param = value["param"] if value.get("param") is not None else ()
        result = value.get("result")
        r = square(*param)
        if r == result:
            print(f"✅{name.upper()} passed.")
        else:
            print(f"❌{name.upper()} failed.")
            print(f"{fn_name}{param} Expect {result} but got {r}")
        

if __name__ == "__main__":
    run_test()
