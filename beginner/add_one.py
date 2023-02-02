"""
Get integer number and add one to it.
Parameters:
-----------
n: int
    An integer number

Return
------
outs: int
    Return n + 1
"""

def add_one(n):
    pass

# -----------------------------------
def run_test():
    fn_name = "add_one"
    # Tests
    tests = {
        "test#1": {"param": (2,), "result": 3},
        "test#2": {"param": (0,), "result": 1},
        "test#3": {"param": (-1,), "result": 0},
    }

    for name, value in tests.items():
        param = value["param"] if value.get("param") is not None else ()
        result = value.get("result")
        r = add_one(*param)
        if r == result:
            print(f"✅{name.upper()} passed.")
        else:
            print(f"❌{name.upper()} failed.")
            print(f"{fn_name}{param} Expect {result} but got {r}")
        

if __name__ == "__main__":
    run_test()
