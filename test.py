import os
import sys

if len(sys.argv) != 2:
    print("Usage: python expects 1 arg")
    sys.exit(1)

word = sys.argv[1]
file_to_test = os.environ.get('FILE_TO_TEST')

if not file_to_test:
    print("ERROR: env 'FILE_TO_TEST' not declared")
    sys.exit(2)

if not os.path.isfile(file_to_test):
    print("ERROR: cannot open this file: ${file_to_test}")
    sys.exit(127)

    try:
        with open(file_to_test, 'r') as file:
            content = file.read()
    except Exception as e:
            print('ERROR: cannot convert the code')
    if word not in file_to_test:
            print(f'TEST FAILED: ${word} wasnt found in ${file_to_test}')
            sys.exit(1)
    print(f'TEST PASSED: ')
    sys.exit(1)