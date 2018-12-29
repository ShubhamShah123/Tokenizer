# Shah Shubham.
# sbs8554
# 2018-08-23
#--------------------------------------------------
import re
import sys
#--------------------------------------------------
def processToken(token):
    # Regular Expresions
    int_regex = r"(^[+-]?[0-9]+$)"
    fp_regex = r"((^[+-]?[0-9]+)[.]([0-9]+$))"
    id_regex = r"^[_a-zA-Z][_a-zA-Z0-9]*$"
    int_match = re.search(int_regex, token)
    if int_match:
        print('> %s < matches INT' % token)
    else:
        fp_match = re.search(fp_regex, token)
        if fp_match:
            print('> %s < matches FP' % token)
        else:
            id_match = re.search(id_regex, token)
            if id_match:
                print('> %s < matches ID' % token)
            else:
                print('> %s < does not match' % token)
def main():
    fName = sys.argv[1]
    print('processing tokens from ' + fName + ' ...')

    with open(fName, 'r') as fp:
        lines = fp.read().replace('\r', '').split('\n')

    for line in lines:
        for token in line.split():
            processToken(token)
#--------------------------------------------------
if (__name__ == '__main__'):
    main()

#--------------------------------------------------
