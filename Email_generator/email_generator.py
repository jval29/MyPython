
""" Use it to generate the E-mail(s)
To plug as a Module use import like:
      from email_generator import generate_emails
to obtain generated Email-list call function:
      generate_emails()
Call function without parameters to obtain 1 email in list with default options.
Call function with single number parameter to obtain any quantity You want, like:
      generate_emails(20)  ---  if You want 20 emails in list
Call function with all parameters generate_emails(emailsQuantity: int = 1,
                                                  allowedSymbols: list = None,
                                                  minNameLen: int = 4,
                                                  maxNameLen: int = 9,
                                                  solidDomain: str = None,
                                                  solidZone: str = None)

Examples:
      generate_emails(10, '+-', 5, 12)
      generate_emails(50, None, 4, 8, 'mail', 'com') """


import random


# Main generator function
def generate_emails(emailsQuantity: int = 1, allowedSymbols: list = None,
                    minNameLen: int = 4, maxNameLen: int = 9,
                    solidDomain: str = None, solidZone: str = None) -> list:
    # Symbols lists
    vowelsList = ('a', 'e', 'i', 'o', 'u')
    consonantList = ('b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'qu', 'v', 'r', 'w', 'y', 'j', 's', 't', 'x',
                   'z', 'th', 'ss', 'ch', 'sh', 'll', 'sc')
    zonesList = ('com', 'org', 'io', 'ru', 'us', 'de', 'fr', 'uk')
    if not allowedSymbols:  # Correction of the List that contains Symbols
        symbolsList = ['ight', '-', '_']
    else:
        symbolsList = ['ight'] + allowedSymbols

    emailsList = []  # List to gather generated Emails

    # Main cycle of generation
    for emailsCounter in range(int(emailsQuantity)):

        # Name Generator
        countNameTotal = random.randint(minNameLen, maxNameLen)
        userName = ''
        chanceVowel, chanceConsonant, chanceSymbol = -10, +50, -100  # Initial correction of chances to be chosen
        for vCountName in range(countNameTotal):  # Name generation cycle
            if (random.randint(1, 100) + chanceVowel) > 70:
                userName = userName + vowelsList[random.randint(0, len(vowelsList)-1)]
                chanceVowel, chanceConsonant, chanceSymbol = -20, 0, 0
            elif (random.randint(1, 100) + chanceConsonant) > 50:
                userName = userName + consonantList[random.randint(0, len(consonantList)-1)]
                chanceVowel, chanceConsonant, chanceSymbol = +40, -20, 0
            elif (random.randint(1, 100) + chanceSymbol) > 60:
                userName = userName + symbolsList[random.randint(0, len(symbolsList)-1)]
                chanceVowel, chanceConsonant, chanceSymbol = -10, 0, -100
            else:
                userName = userName + str(random.randint(0, 9))
                chanceVowel, chanceConsonant, chanceSymbol = -15, -25, -25
            if len(userName) >= (countNameTotal - 2):
                chanceSymbol = -100
            if len(userName) >= countNameTotal:
                if len(userName) > maxNameLen:
                    userName = userName[:maxNameLen]
                break

        # Domain generator
        if not solidDomain:
            generatedDomain = ''
            countDomainTotal = random.randint(3, 8)
            chanceVowel = -10
            for countDomain in range(countDomainTotal):  # Domain generation cycle
                if (random.randint(1, 100) + chanceVowel) > 60:
                    generatedDomain = generatedDomain + vowelsList[random.randint(0, len(vowelsList)-1)]
                    chanceVowel = -20
                else:
                    generatedDomain = generatedDomain + consonantList[random.randint(0, len(consonantList)-1)]
                    chanceVowel = +40
                if len(generatedDomain) >= countDomainTotal:
                    break
        else:
            generatedDomain = solidDomain

        # Zone generator
        if not solidZone:
            generatedZone = zonesList[random.randint(0, len(zonesList)-1)]
        else:
            generatedZone = solidZone

        newEmail = f'{userName}@{generatedDomain}.{generatedZone}'
        emailsList.append(newEmail)
    # End of Main cycle of generation
    return emailsList
# End of Main generator function


if __name__ == '__main__':
    print('*** E-Mail generator v.1.00.3 (c)jval29 ***\nWe use template for Generation  - <name>@<domain>.<zone>')

    while True:  # Collecting Parameters for Generation
        while True:  # Quantity of emails
            reqQuantity = input('How many E-mails do You need? (default is "1"): ')
            if reqQuantity == '':
                reqQuantity = '1'
                print('Quantity used by default (1)')
            try:  # Int check
                quantityInt = int(reqQuantity)
                if quantityInt >= 1:
                    break
                print('Enter Positive Number, Please')
            except ValueError:
                print('Only Numbers, Please')

        while True:  # Special sybmols  allowed
            incNewSymb = input('What Special Symbols do You want to allow in the <Name>? (default is "-" and "_"): ')
            if incNewSymb == '':
                addedSymbols = ['-', '_']
                print('Special symbols in the <Name> is used by default: ' + str(addedSymbols))
            else:
                addedSymbols = list(incNewSymb)
            break

        while True:  # Minimal Name Length
            reqMinNameLen = input('Enter minimal <Name> Length (default is "4"): ')
            if reqMinNameLen == '':
                reqMinNameLen = '4'
                print('Minimal <Name> Length used by default (4)')
            try:  # Int check
                if 3 <= int(reqMinNameLen) <= 6:
                    break
                print('Enter Number between 3 and 6 , Please')
            except ValueError:
                print('Only Numbers, Please')

        while True:  # Maximal Name Length
            reqMaxNameLen = input('Enter maximal <Name> Length (default is "9"): ')
            if reqMaxNameLen == '':
                reqMaxNameLen = '9'
                print('Maximal <Name> Length used by default (9)')
            try:  # Int check
                if 4 <= int(reqMaxNameLen) <= 20:
                    break
                print('Enter Number between 4 and 20 , Please')
            except ValueError:
                print('Only Numbers, Please')

        while True:  # Add Solid-Domain option
            reqDomain = input(
                'Enter solid <Domain> name or just press Enter on empty field, if You want to randomise <Domain>: ')
            if 2 <= len(reqDomain) <= 12 or reqDomain == '':
                break
            print('Make sure that <Domain> length is between 2 and 12 characters')

        while True:  # Add Solid-Zone option
            reqZone = input(
                'Enter solid <Zone> name or just press Enter on empty field, if You want to randomise <Zone>: ')
            if 2 <= len(reqZone) <= 5 or reqZone == '':
                break
            print('Make sure that <Zone> length is between 2 and 5 characters')
        break
    # End of the Generation parameters gathering

    while True:
        print('Emails successfully created:')
        print(generate_emails(int(reqQuantity), addedSymbols, int(reqMinNameLen), int(reqMaxNameLen), reqDomain, reqZone))
        vExit = input('Press Enter to Generate again or type "N" to Quit: ').lower().strip()
        if vExit in ('n', 'no', 'e', 'exit', 'quit', 'q'):
            break
