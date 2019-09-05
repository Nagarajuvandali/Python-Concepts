def argv(*args):
    value = ""
    print(type(args))
    for i in args:
        value = value + " " + i
    return value


def kwargs(**args):
    print(type(args))
    for key, value in args.items():
        print("{} {}".format(key, value))


def args_kwargs(arg1, *args, **kwargs):
    print(type(arg1))
    print("arg_1:", arg1)
    print(type(args))
    for i in args:
        print("args", i)
    print(type(kwargs))
    for key, value in kwargs.items():
        print("kwargs: {} {}".format(key, value))



print(argv("If", "the", "door", "doesnt", "open","for", "you", "then", "its not", "your door"))

kwargs(first='nagaraju', last='vandali', qualification='B.Tech')

print(args_kwargs(2,"I", "love", "coding",first='nagaraj', last='vandali', qualification='B.Tech'))
