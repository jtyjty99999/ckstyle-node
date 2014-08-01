class ERROR_LEVEL:
    ERROR = 0
    WARNING = 1
    LOG = 2

class Checker():
    def __init__(self):
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = '_default_msg'
    def check(self, xxx, config):
        pass
    def getMsg(self):
        return self.errorMsg
    def getLevel(self):
        return self.errorLevel

class RuleChecker(Checker):
    def __init__(self):
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = ''
    def check(self, rule, config):
        return True

class RuleSetChecker(Checker):
    def __init__(self):
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = ''
    def check(self, ruleSet, config):
        return True

class StyleSheetChecker(Checker):
    def __init__(self):
        self.errorLevel = ERROL_LEVEL.LOG
        self.errorMsg = ''
    def check(self, styleSheet, config):
        return True

class ExtraChecker(Checker):
    def __init__(self):
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = ''
    def check(self, ruleSet, config):
        return True