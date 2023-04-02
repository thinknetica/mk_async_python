import time


def long_operation():
    print("Starting long operation")
    time.sleep(5)
    print("Long operation completed")


if __name__ == "__main__":
    print("Start")
    long_operation()
    print("End")

