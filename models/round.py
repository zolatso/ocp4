import datetime


class Round:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.start_date = kwargs.get("start_date", datetime.datetime.now().date())
        self.matches = kwargs["matches"]
        self.complete = kwargs.get("complete", False)


def main():
    pass


if __name__ == "__main__":
    main()
