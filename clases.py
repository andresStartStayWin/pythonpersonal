def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        spam = "nonlocal spam"

    def do_global():
        spam = "global spam"

    spam = "test spam"
    do_local()
    print(spam)
    do_nonlocal()
    print(spam)
    do_global()
    print(spam)

scope_test()
print(spam)
