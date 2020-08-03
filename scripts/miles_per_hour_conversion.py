def convert_MPH_to_MPS(speed):
    # convert miles per hour (MPH) -> meter per second (MPS)
    mps = speed / 2.237
    return mps


def get_MPS(data):
    # print result
    return f"Your speed in meter per second is {data:.2f}"


def get_user_MPH():
    # get user miles per hour speed for conversion
    while True:
        try:
            mph = float(input("What's your speed in miles per hour?\n"))
            if isinstance(mph, float):
                break
        except ValueError:
            print("Please enter a float value (ex: 2.00)")

    return mph


def loop_app(number):
    # how many times to run the app
    for _ in range(number):
        app()


def app():
    # the main app
    mph = get_user_MPH()
    mps = convert_MPH_to_MPS(mph)

    result = get_MPS(mps)
    print(result)


def start():
    # start the app
    loop_app(3)


if __name__ == "__main__":
    start()
