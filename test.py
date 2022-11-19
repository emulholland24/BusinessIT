from proofpoint import checkSentence
# use valid and invalid strings to test the class
# valid strings
sentence1 = checkSentence('The quick brown fox said “hello Mr lazy dog”.')
sentence2 = checkSentence('The quick brown fox said hello Mr lazy dog.')
sentence3 = checkSentence('One lazy dog is too few, 13 is too many.')
sentence4 = checkSentence('One lazy dog is too few, thirteen is too many.')
sentence5 = checkSentence('How many "lazy dogs" are there?')
# invalid strings
sentence6 = checkSentence('The quick brown fox said "hello Mr. lazy dog".')
sentence7 = checkSentence('the quick brown fox said “hello Mr lazy dog".')
sentence8 = checkSentence('"The quick brown fox said “hello Mr lazy dog."')
sentence9 = checkSentence('One lazy dog is too few, 12 is too many.')
sentence10 = checkSentence('Are there 11, 12, or 13 lazy dogs?')
sentence11 = checkSentence('There is no punctuation in this sentence')

# test upper case function
# valid
sentence1.checkUpperCase()
# invalid
sentence7.checkUpperCase()

# test quotation marks function
# valid
sentence5.checkQuotationMarks()
# invalid
sentence4.checkQuotationMarks()

# test termination character function
# valid
sentence5.checkTerminationChar()
# invalid
sentence11.checkTerminationChar()

# test period function
# valid
sentence5.checkPeriod()
# invalid
sentence11.checkPeriod()

# test number function
# valid
sentence3.checkNum()
# invalid
sentence10.checkNum()

# test validate function
# valid
sentence1.validate()
sentence2.validate()
sentence3.validate()
# invalid
sentence6.validate()
sentence7.validate()
sentence8.validate()





