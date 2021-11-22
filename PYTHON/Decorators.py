def announce(f):
    def wrapper():
        print("About to be running")
        f()
        print("Done!")
    return wrapper

@announce
def hello():
    print("Hello World!")

hello()