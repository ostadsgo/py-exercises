""" What this exercise is about.

Parameters:
-----------
param: type
    Description

Return
------
outs: type
    What will be returned.
"""

def function_name(n):
    pass

# -----------------------------------
# Test area (Do not touch this area)
# -----------------------------------
class Color:
    SUCC = "\33[92m"
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def run_test():
    fn = function_name
    # Tests
    tests = [ 
        {"param": (0,) , "result": True},
        {"param": (0,) , "result": True},
    ]

    for i, test in enumerate(tests, 1):
        param = test["param"]
        result = test["result"]
        call_result = fn(*param)
        if call_result == result:
            print(f"✅{Color.SUCC}Test#{i} passed{Color.ENDC}.")
        else:
            print(f"❌{Color.FAIL}Test#{i} failed.{Color.ENDC}")
            print(f"--> {fn.__name__}{param} Expect {Color.SUCC}{result}{Color.ENDC} but got {Color.FAIL}{call_result}{Color.ENDC}🤦‍")

if __name__ == "__main__":
    run_test()
