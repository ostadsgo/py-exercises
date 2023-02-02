"""
Calcualte area of a rectangle.
If width or hight is not positive interger number 
returns zero.
Parameters:
-----------
width: int
    Width of the rectangle.
height: int
    Hight of the rectangle
Return
------
outs: int
    Calculate area and return the result.
"""

def say_hello(name):
    return 1


# -----------------------------------
def run_test():
    fn_name = "say_hello"
    # Tests
    tests = {
        "test#1": {"param": ("john",), "result": "Hello, john"},
        "test#2": {"param": ("Marry",), "result": "Hello, Marry"},
        "test#3": {"param": ("",), "result": "Invalid"},
    }

    for name, value in tests.items():
        param = value["param"] if value.get("param") is not None else ()
        result = value.get("result")
        r = say_hello(*param)
        if r == result:
            print(f"✅{name.upper()} passed.")
        else:
            print(f"❌{name.upper()} failed.")
            print(f"{fn_name}{param} Expect {result} but got {r}")
        

if __name__ == "__main__":
    run_test()
