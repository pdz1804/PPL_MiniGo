
class ErrorToken(Exception):
    def __init__(self,s):
        self.message = "ErrorToken "+ s

class UncloseString(Exception):
    def __init__(self,s):
        self.message = "Unclosed string: "+ s

class IllegalEscape(Exception):
    def __init__(self,s):
        self.message = "Illegal escape in string: "+ s



