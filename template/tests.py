# -----------------------------------
# Test area (Do not touch this area)
# -----------------------------------
class Color:
    SUCC = "\33[92m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Message:
    SUCC_ICON = "✅"
    FAILED_ICON = "❌"
    SUCC = "{}{}Test passed{}."
    FAILED = "--> {}{}{} Expect {}{}{} but got {}{}{}🤦"


def assert_equals(fn, param, expect):
    result = fn(*param)
    if result == expect:
        m = Message.SUCC.format(Message.SUCC_ICON, Color.SUCC, Color.ENDC)
        print(m)
        return True
    m = Message.FAILED.format(
        fn.__name__,
        param,
        Message.FAILED_ICON,
        Color.SUCC,
        expect,
        Color.ENDC,
        Color.FAIL,
        result,
        Color.ENDC
    )
    print(m)




