import traceback


class Errors(object):

    def exceptionalHandling(self):
        try:
            a = 10
            b = 15
            c = 10

            d = (a + b) / c
            print(d)

        # printing actual exception

        except:
            traceback.print_stack()


e1 = Errors()  # You need this line to create the object
e1.exceptionalHandling()  # You need to call the method using e1