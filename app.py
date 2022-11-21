# class to create sentence isntances and to organise functions
class checkSentence():
    # assign the object with a string to perform checks on
    def __init__(self, sentence):
        self.sentence = str(sentence)

    def checkUpperCase(self):
        # check if first character by using index of string and check if it is a capital letter
        if self.sentence[0].isupper():
            return True
        else:
            return False

    def checkQuotationMarks(self):
        # check if the number of quotation marks is even. Modulus returns the remainder of a division so if division by two remainder is 0 then it is even
        if self.sentence.count('"') % 2 == 0:
            return True
        else:
            return False

    def checkTerminationChar(self):
        # check if the last character is a period, exclamation mark or question mark. [-1] is used to access the last character
        if self.sentence[-1] in [".", "?", "!"]:
            return True
        else:
            return False

    def checkPeriod(self):
        # check if there is period characters
        if self.sentence.count('.') == 0:
            if self.checkTerminationChar():
                return True
            else:
                return False
        # check if last charcter is a period. if it is a period the count must be 1. 
        elif self.sentence[-1] == '.' and self.sentence.count('.') == 1:
            return True
        # if it is not a period the count must be 0 as no other periods are allowed.
        elif self.sentence[-1] != '.' and self.sentence.count('.') == 0:
            return True
        else:
            return False

    def checkNum(self):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        # remove commas
        new_str = ''
        for character in self.sentence:
            if character != ',':
                new_str = new_str + character
        # check string for numbers below 13
        for i in new_str.split():
            if i in numbers:
                return False
        return True
        
            
    def validate(self):
        # check all rules
        if not self.checkUpperCase():
            return print('String does not start with a capital letter.')
        elif not self.checkQuotationMarks():
            return print('String does not have an even number of quotation marks.')
        elif not self.checkTerminationChar():
            return print('String does not end in ".", "!" or "?"')
        elif not self.checkPeriod():
            return print('String has period characters other than the last character.')
        elif not self.checkNum():
            return print('Numbers below thirteen in the string are not spelt out.')
        else:
            return print ('String is valid.')
    
