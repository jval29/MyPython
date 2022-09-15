# Use it to generate the E-mail(s)
# To plug as a Module use import like:
#       from email_generator import f_genemail
# to obtain generated Email-list call function:
#       f_genemail()
# Call function without parameters to obtain 1 email in list with default options.
# Call function with single number parameter to obtain any quantity You want, like:
#       f_genemail(20)  ---  if You want 20 emails in list
# Call function with all parameters f_genemail(a,'b',c,d,'e','f') where:
#       a - (int) how many emails You need
#       b - (str) special symbols allowed in the <name> , default is '-_'
#       c - (int) minimal <name> length , default is 4
#       d - (int) maximal <name> length, default is 9
#       e - (str) the name of <Domain> if You need fixed, default is '' - to be generated
#       f - (str) the name of <Zone> if You need fixed, default is '' - to be generated
# Examples:
#       f_genemail(10,'+-',5,12,'','')
#       f_genemail(50,'',4,8,'mail','com')

import random

if __name__ == '__main__':
    print('*** E-Mail generator v.1.00.2 ***\nWe use template for Generation  - <name>@<domain>.<zone>')

    while True:  # Collecting Parameters for Generation
        while True:  # Quantity of emails
            vQuantity = (input('How many E-mails do You need? (default is "1"): '))
            if vQuantity == '':
                vQuantity = '1'
                print('Quantity used by default (1)')
            try:  # Int check
                vQuantityInt = int(vQuantity)
                if vQuantityInt >= 1:
                    break
                print('Enter Positive Number, Please')
            except ValueError:
                print('Only Numbers, Please')

        while True:  # Special sybmols  allowed
            vAddNewSymb = input('What Special Symbols do You want to allow in the <Name>? (default is "-" and "_"): ')
            if vAddNewSymb == '':
                liAddSymb = ['-', '_']
                print('Special symbols in the <Name> is used by default: ' + str(liAddSymb))
            else:
                liAddSymb = list(vAddNewSymb)
            break

        while True:  # Minimal Name Length
            vMinNameLen = (input('Enter minimal <Name> Length (default is "4"): '))
            if vMinNameLen == '':
                vMinNameLen = '4'
                print('Minimal <Name> Length used by default (4)')
            try:  # Int check
                vMinNameLenInt = int(vMinNameLen)
                if 3 <= vMinNameLenInt <= 6:
                    break
                print('Enter Number between 3 and 6 , Please')
            except ValueError:
                print('Only Numbers, Please')

        while True:  # Maximal Name Length
            vMaxNameLen = (input('Enter maximal <Name> Length (default is "9"): '))
            if vMaxNameLen == '':
                vMaxNameLen = '9'
                print('Maximal <Name> Length used by default (9)')
            try:  # Int check
                vMaxNameLenInt = int(vMaxNameLen)
                if 4 <= vMaxNameLenInt <= 20:
                    break
                print('Enter Number between 4 and 20 , Please')
            except ValueError:
                print('Only Numbers, Please')

        while True:  # Add Solid-Domain option
            vDomain = input(
                'Enter solid <Domain> name or just press Enter on empty field, if You want to randomise <Domain>: ')
            if 2 <= len(vDomain) <= 12 or vDomain == '':
                break
            print('Make sure that <Domain> length is between 2 and 12 characters')

        while True:  # Add Solid-Zone option
            vZone = input(
                'Enter solid <Zone> name or just press Enter on empty field, if You want to randomise <Zone>: ')
            if 2 <= len(vZone) <= 5 or vZone == '':
                break
            print('Make sure that <Zone> length is between 2 and 5 characters')
        break


# End of the Generation parameters gathering


# Main generator function (parameters order: (vQuantity)(liAddSymb)(vMinNameLen)(vMaxNameLen)(vDomain)(vZone))
def f_genemail(vQuantityF=1, liAddSymbF=None, vMinNameLenF=4, vMaxNameLenF=9, vDomainF='', vZoneF=''):
    # Symbols lists
    liVowel = ('a', 'e', 'i', 'o', 'u')
    liConsonant = ('b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'qu', 'v', 'r', 'w', 'y', 'j', 's', 't', 'x',
                   'z', 'th', 'ss', 'ch', 'sh', 'll', 'sc')
    liZones = ('com', 'org', 'io', 'ru', 'us', 'de', 'fr', 'uk')
    if liAddSymbF in ('', None):  # Correction of the List that contains Symbols
        liSymb = ['ight', '-', '_']
    else:
        liSymb = ['ight'] + liAddSymbF

    liEMails = []  # List to gather generated Emails

    # Main cycle of generation
    for vCounter in range(int(vQuantityF)):

        # Name Generator
        vCountNameTotal = random.randint(vMinNameLenF, vMaxNameLenF)
        vName = ''
        vChanceVowel, vChanceConsonant, vChanceSymb = -10, +50, -100  # Initial correction of chances to be chosen
        for vCountName in range(vCountNameTotal):  # Name generation cycle
            if (random.randint(1, 100) + vChanceVowel) > 70:
                vName = vName + liVowel[random.randint(0, len(liVowel)-1)]
                vChanceVowel, vChanceConsonant, vChanceSymb = -20, 0, 0
            elif (random.randint(1, 100) + vChanceConsonant) > 50:
                vName = vName + liConsonant[random.randint(0, len(liConsonant)-1)]
                vChanceVowel, vChanceConsonant, vChanceSymb = +40, -20, 0
            elif (random.randint(1, 100) + vChanceSymb) > 60:
                vName = vName + liSymb[random.randint(0, len(liSymb)-1)]
                vChanceVowel, vChanceConsonant, vChanceSymb = +20, +20, -100
            else:
                vName = vName + str(random.randint(0, 9))
                vChanceVowel, vChanceConsonant, vChanceSymb = -15, -25, -25
            if len(vName) >= (vCountNameTotal - 2):
                vChanceSymb = -100
            if len(vName) >= (vCountNameTotal):
                break

        # Domain generator
        if vDomainF == '':
            vDomainN = ''
            vCountDomainTotal = random.randint(3, 8)
            vChanceVowel = -10
            for vCountDomain in range(vCountDomainTotal):  # Domain generation cycle
                if (random.randint(1, 100) + vChanceVowel) > 60:
                    vDomainN = vDomainN + liVowel[random.randint(0, len(liVowel)-1)]
                    vChanceVowel = -20
                else:
                    vDomainN = vDomainN + liConsonant[random.randint(0, len(liConsonant)-1)]
                    vChanceVowel = +40
                if len(vDomainN) >= vCountDomainTotal:
                    break
        else:
            vDomainN = vDomainF

        # Zone generator
        if vZoneF == '':
            vZoneN = liZones[random.randint(0, len(liZones)-1)]
        else:
            vZoneN = vZoneF

        vNewEmail = str('{}@{}.{}').format(vName, vDomainN, vZoneN)
        liEMails.append(vNewEmail)
    # End of Main cycle of generation
    return liEMails


# End of Main generator function

if __name__ == '__main__':
    while True:
        print('Emails successfully created:')
        print(f_genemail(int(vQuantity), liAddSymb, int(vMinNameLen), int(vMaxNameLen), vDomain, vZone))
        vExit = input('Press Enter to Generate again or type "N" to Quit: ').lower()
        if vExit in ('n', 'no', 'e', 'exit', 'quit', 'q'):
            break
