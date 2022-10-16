import os
import os.path
import datetime


def f_SnR(vFind, vReplace, vSearchPath):  # Main Function
    global vReplaceAgree
    for vSearchPlace in os.listdir(path=vSearchPath):
        vSearchPlace = vSearchPath + '\\' + vSearchPlace
        if os.path.isdir(vSearchPlace):  # Search in sub-dir (recursion)
            f_SnR(vFind, vReplace, vSearchPlace)
        elif os.stat(vSearchPlace).st_size < 102400:
            with open(vSearchPlace, 'r') as vTextTmp:
                try:
                    vTextTmp = vTextTmp.read()
                except UnicodeDecodeError:
                    continue

            if vFind in vTextTmp:
                print(f'<{vFind}> found in <{vSearchPlace}>')
                with open('ReplaceLog.log', 'a') as ReplaceLog:
                    ReplaceLog.write('\n')
                if vReplaceAgree in ('any', 'all'):  # replace all w/o confirmation
                    vTextTmpCorrected = vTextTmp.replace(vFind, vReplace)
                    with open(vSearchPlace, 'w') as vFileForUpd:
                        vFileForUpd.write(vTextTmpCorrected)
                    vReplaceEvent = f'<{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}> ' \
                                    f'Replaced <{vFind}> to <{vReplace}> in <{vSearchPlace}> \n'
                    print('\t' + vReplaceEvent)
                    with open('ReplaceLog.log', 'a') as ReplaceLog:
                        ReplaceLog.write(vReplaceEvent.strip())

                else:  # ask for confirmation
                    vReplaceAgree = input(f'Replace <{vFind}> to <{vReplace}>? \n'
                                          f'Press Enter to confirm \n'
                                          f'Enter < No > to decline \n'
                                          f'Enter < All > to replace ALL without confirmations \n'
                                          f' \t [ ]: ').lower().strip()
                    if vReplaceAgree not in ('n', 'no', 'nn'):
                        vTextTmpCorrected = vTextTmp.replace(vFind, vReplace)
                        with open(vSearchPlace, 'w') as vFileForUpd:
                            vFileForUpd.write(vTextTmpCorrected)
                        vReplaceEvent = f'<{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}> ' \
                                        f'Replaced <{vFind}> to <{vReplace}> in <{vSearchPlace}> \n'
                        print('\t' + vReplaceEvent)
                        with open('ReplaceLog.log', 'a') as ReplaceLog:
                            ReplaceLog.write(vReplaceEvent.strip())
                    else:
                        print('Replace declined')

        else:  # not found  - continue search
            continue


print('***seek_n_replace ver.1.00.01 (c)jval29*** \n')

while True:  # Parameters gathering, start main function, ask for repeat
    vReplaceAgree = 'y'
    vFindInp = input('Enter search text: ')
    vReplaceInp = input('Enter text to replacement: ')

    while True:  # Check Path for correctness
        try:
            vSearchPathInp = input('Enter path where You want to search: ')
            vSearchPathInp = fr'{vSearchPathInp}'
            if os.listdir(vSearchPathInp):
                break
            else:
                print('Directory is empty.')
                continue
        except (OSError, PermissionError):
            print('Wrong Path or No permissions')
            continue
    print()
    f_SnR(vFindInp, vReplaceInp, vSearchPathInp)

    vExit = input('Want to make a new seek_n_replace? (y/n): ').lower()
    if vExit in ('', 'y', 'yes'):
        continue
    else:
        break
