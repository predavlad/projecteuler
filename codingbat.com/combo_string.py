def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    return a + b + a

assert combo_string('Hello', 'hi') == 'hiHellohi'
assert combo_string('hi', 'Hello') == 'hiHellohi'
assert combo_string('aaa', 'b') == 'baaab'