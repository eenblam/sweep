from re import match

class GameCommand(object):
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.row = None
        self.col = None
        self.action = None
        self.valid = False

        self.input_string = raw_input().strip()
        if self.match_quit():
            return
        elif self.match_check():
            return
        elif self.match_flag():
            return
        else:
            return

    def match_quit(self):
        result = match('^quit$', self.input_string)
        if result is None:
            return False
        self.valid = True
        self.action = 'quit'
        return True

    def match_check(self):
        result = match('^check (\d+) (\d+)$', self.input_string)
        if result is None:
            return False
        self.valid = True
        self.action = 'check'
        self.row = int(result.group(1))
        self.col = int(result.group(2))
        return True

    def match_flag(self):
        result = match('^flag (\d+) (\d+)$', self.input_string)
        if result is None:
            return False
        self.valid = True
        self.action = 'flag'
        self.row = int(result.group(1))
        self.col = int(result.group(2))
        return True

class MenuCommand(object):
    def __init__(self):
        self.action = None
        self.valid = False

        self.input_string = raw_input().strip()
        if self.match_new():
            return
        elif self.match_quit():
            return
        else:
            return

    def input_error(self):
        print('Please enter one of the following:')
        print('\t"new" to start a new game')
        print('\t"quit" to quit')

    def match_new(self):
        result = match('^new$', self.input_string)
        if result is None:
            return False
        self.action = 'new'
        self.valid = True
        return True

    def match_quit(self):
        result = match('^quit$', self.input_string)
        if result is None:
            return False
        self.action = 'quit'
        self.valid = True
        return True
