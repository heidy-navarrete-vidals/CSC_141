five_words = {'string':
              'a sequence of characters enclosed in single or double quotes',
              'list':
              'a collection of items in a particular order',
              'f-string':
              'a set of strings that replace the name of any variable in braces with its value',
              'variable':
              'boxes you can store values in.',
              'value':
              'the information associated within a variable',
              'method':
              'an action that python can perform on a piece of data',
              'whitespace':
              'any nonprinting characters such as end-of-line symbols, spaces, and tabs',
              'syntax error':
              'a section of your program that Python does not recognize as valid code',
              'floats':
              'any number with a decimal point',
              'constants':
              'a value that stays the same throughout the program'
              }

for word, definition in five_words.items():
    print(f"\n{word.title()}:")
    print(f"{definition}")