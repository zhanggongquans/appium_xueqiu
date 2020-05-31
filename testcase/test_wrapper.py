def extend(func):
    def hello(*args, **kwargs):
        print("hello")
        func(*args, **kwargs)
        print("good bye")

    return hello


@extend
def tmp():
    print("tmp")


def tmp1():
    print("tmp1")


def test_wrapper():
    tmp()
    extend(tmp1)()
