class CustomException(Exception):

    pass


def div_ex(divider):
    try:
        if divider == 13:
            raise CustomException("unlucky!")
        print(100 / divider)
    except ZeroDivisionError:
        print("AA")
    except CustomException:
        print("BB")
        raise
    else:
        print("CC")
    finally:
        print("end")
    print("hello")

