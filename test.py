import simpleconfig


def main():

    settings = simpleconfig.Config('config.test.ini')
    print settings
    settings.hosted.name = "Richard"
    settings.save()
    exit(0)


if __name__ == '__main__':
    main()
