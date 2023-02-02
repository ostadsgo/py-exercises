"""
Get tow number and compare each other.
Parameters:
-----------
x: int
    An integer number
y: int
    An integer number
Return
------
outs: int
    If x bigger than y return True otherwise return False
"""

def add_one(x, y):
    pass
        
            

# -----------------------------------
def run_test():
    fn_name = "add_one"
    # Tests
    tests = {
        "test#1": {"param": (2,3), "result": False},
        "test#2": {"param": (0, 0), "result": False},
        "test#3": {"param": (-1,-5), "result": True},
        "test#4": {"param": (2,1), "result": True},
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
