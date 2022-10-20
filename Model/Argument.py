def check_start(word, pattern):
    return word.startswith(pattern)

def check_end(word, pattern):
    return word.endswith(pattern)

def create_check_at_position(position):
    def check_at_position(word, pattern):
        return word[position:].startswith(pattern)
    return check_at_position

def check_constant(word,pattern):
    return True



class Argument:

    def __init__(self, markers, arguments, check):
        self.markers = markers
        self.arguments = arguments
        self.check = check

    def find_argument(self, word):
        for i in range(len(self.markers)):
            if self.check(word, self.markers[i]):
                return self.arguments[i]
        print('The name '+word+'contained none of the required patterns. Returning blank.')
        return ''



class ArgumentStart(Argument):

    def __init__(self, markers = [], arguments = []):
        super().__init__(markers, arguments, check_start)



class ArgumentEnd(Argument):

    def __init__(self, markers = [], arguments = []):
        super().__init__(markers, arguments, check_end)



class ArgumentPosition(Argument):

    def __init__(self, position, markers = [], arguments = []):
        super().__init__(markers, arguments, create_check_at_position(position))



class ArgumentConstant(Argument):

    def __init__(self, argument):
        super().__init__([True], [argument], check_constant)
