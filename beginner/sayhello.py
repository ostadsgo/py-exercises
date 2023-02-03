"""
Information
-----------
COPY RIGHT by Saeed Gholami @ 2023
Email: saeed.ghollami@gmail.com
Github: ostadsgo
Web: ostadsgo.github.io

Level
-----
Beginners


Description
-----------
Say hello to given a name.

Examples
-------
>>> say_hello("John")
Hello, John

Requirements
------------
  - Variables

Resources
---------

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
