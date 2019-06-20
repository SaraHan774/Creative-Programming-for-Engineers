class Functions:

    mark = [38, 45, 36, 37, 12, 50, 49]

    @staticmethod
    def print_mark(m=mark):
        print("mark = %s" % m)
        for num, score in enumerate(m, 1):
            if score >= 40:
                print("student %d passed the exam. " % num)
            else:
                print("student %d did not pass the exam. " % num)


if __name__ == '__main__':
    functions = Functions()

    functions.print_mark()
