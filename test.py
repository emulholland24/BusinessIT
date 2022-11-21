from app import checkSentence

# creates instaces using valid strings to test
sentence1 = checkSentence('The quick brown fox said "hello Mr lazy dog".')
sentence2 = checkSentence('The quick brown fox said hello Mr lazy dog.')
sentence3 = checkSentence('One lazy dog is too few, 13 is too many.')
sentence4 = checkSentence('One lazy dog is too few, thirteen is too many.')
sentence5 = checkSentence('How many "lazy dogs" are there?')

#  create instances using invalid strings to test
sentence6 = checkSentence('The quick brown fox said "hello Mr. lazy dog".')
sentence7 = checkSentence('the quick brown fox said "hello Mr lazy dog".')
sentence8 = checkSentence('"The quick brown fox said "hello Mr lazy dog."')
sentence9 = checkSentence('One lazy dog is too few, 12 is too many.')
sentence10 = checkSentence('Are there 11, 12, or 13 lazy dogs?')
sentence11 = checkSentence('There is no punctuation in this sentence')


# test valid sentences
sentence1.validate()
sentence2.validate()
sentence3.validate()
sentence4.validate()
sentence5.validate()

# test invalid sentences

# this should show error message for checkPeriod
sentence6.validate()

# this should show error message for checkUpperCase
sentence7.validate()

# this should show error message for checkUpperCase
sentence8.validate()

# this should show error message for checkNum
sentence9.validate()

# this should show error message for checkNum
sentence10.validate()

# this should show error message for checkTerminationChar
sentence11.validate() 