import sys

config = dict.fromkeys(['Q', 'Sigma', 'Gamma', 'Delta', 'S', 'I', 'F'], None)

def check_delta(current_state, current_character, current_stack):
    for x in config['Delta']:
        x = x.split(' ')
        if current_state == x[0] and current_character == x[1] and current_stack[0] == x[2]:
            print('FOUND TRANSITION')
        

def dpda_sim():
    my_input = input()
    current_state = config['S']
    current_stack = config['I']

    for x in range(0, len(my_input) - 1):
        if my_input[x] in config['Sigma']: #current character in alaphabet???
            print('Legal Character')
            check_delta(current_state, my_input[x], current_stack)
        else:
            print('Illegal Character')

def config_getter(config_location):
    global config

    with open(f'{config_location}Q.conf') as f:
        config['Q'] = f.read(1)

    with open(f'{config_location}Sigma.conf') as f:
        config['Sigma'] = f.readline()

    with open(f'{config_location}Gamma.conf') as f:
        config['Gamma'] = f.readline()

    with open(f'{config_location}delta.conf') as f:
        config['Delta'] = f.readlines()

    with open(f'{config_location}F.conf') as f:
        config['F'] = f.readline(),split(',')

    config['S'] = '0'

    config['I'] = config['Gamma'] [0]

def main(argv):
    if len(sys.argv) < 2:
        usage_string = 'usage: python ' + argv[0] + '/location/of/configuration/files'
        print(usage_string)
    else:
        config_getter()


main(sys.argv[])
