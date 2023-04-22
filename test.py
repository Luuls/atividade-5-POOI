import subprocess as sub
import sys

input_path = sys.argv[1] + '.in'
with open(input_path, 'r') as input_file:
    input_data = input_file.read()

test_cases = input_data.strip().split('\n\n')

program_to_run = sys.argv[1] + '.py'
for i, test_case in enumerate(test_cases, 1):
    output = sub.check_output(f'python {program_to_run}', input=test_case, text=True)

    print(f'### TEST {i}:\n')
    print(output.strip(), '\n')
