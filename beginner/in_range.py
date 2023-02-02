""" Is x in range between 0 and n noninclusivly; 

Parameters:
-----------
x: int
    A number
n: int
    A number

Return
------
outs: bool
    If x is in range of 0..n returns true otherwise returns false
"""

def in_range(x, n):
    return x in range(0, n)

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
    fn = in_range
    # Tests
    tests =[ 
        {"param": (2, 10), "result": True},
        {"param": (0, 3), "result": True},
        {"param": (-1, -5), "result": False},
        {"param": (4, 3), "result": False},
        {"param": (0, 3), "result": True},
        {"param": (-1, 3), "result": False},
        {"param": (1, 3), "result": False},
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
