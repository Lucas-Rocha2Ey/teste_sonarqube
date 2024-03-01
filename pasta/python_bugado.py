class BugClass:
    @staticmethod
    def no_parameter():
        print("No parameters here")

    def another_error():
        print("No 'self' parameter here")


def wrongNameFunction():

    print(INVALID_VARIABLE)

def string_format_issue():

    print("Hello %s" % age)

def nested_conditions(i):
    if i < 10:
if i < 5 and ...:
            print("Nested conditionals")

INVALID_VARIABLE = "This is defined after being used"
bugObject = BugClass()
bugObject.no_parameter()
bugObject.another_error()

wrongNameFunction()

string_format_issue()

nested_conditions(3)
