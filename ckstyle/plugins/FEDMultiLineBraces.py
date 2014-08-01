#/usr/bin/python
#encoding=utf-8

from .Base import *

class FEDMultiLineBraces(RuleSetChecker):
    
    '''{
        "summary":"多行CSS风格的括号检查",
        "desc":"用于检查多行风格下的 <code>{</code> 和 <code>}</code> 的编写风格，前后空格符和回车符的情况等。"
    }'''

    def __init__(self):
        self.id = 'multi-line-brace'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg_shouldEnterAfterOpenningBrace = 'should "enter" after the opening brace in "${selector}"'
        self.errorMsg_shouldEnterBeforeClosingBrace = 'should "enter" before the closing brace in "${selector}"'
        self.errorMsg_extraSpaceAfterOpeningBrace = 'extra "space" after the opening brace in "${selector}"'
        self.errorMsg_everyAttrShouldInSingleLine = 'every name/value should in single line in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        singleLine = ruleSet.getSingleLineFlag()
        if singleLine:
            return True

        value = ruleSet.roughValue
        splited = value.split('\n')
        if splited[0].strip() != '':
            self.errorMsg = self.errorMsg_shouldEnterAfterOpenningBrace
            return False

        if splited[0].strip() == '' and splited[0].startswith(' '):
            self.errorMsg = self.errorMsg_extraSpaceAfterOpeningBrace
            return False

        ruleLength = len(ruleSet.getRules())
        if ruleLength != 0 and len(value.strip().split('\n')) != ruleLength:
            self.errorMsg = self.errorMsg_everyAttrShouldInSingleLine
            return False

        if not value.replace(' ', '').endswith('\n'):
            self.errorMsg = self.errorMsg_shouldEnterBeforeClosingBrace
            return False

        return True 
