import sys

config = dict.fromkeys(['Q', 'Sigma', 'Gamma', 'Delta', 'S', 'I', 'F'], None)

def check_delta(current_state, current_character, current_stack):
    '''
        
    '''
    print('current state is ' + current_state + ', current character is ' + current_character + ', and the current stack is ' + current_stack)
    for x in config['Delta']:
        x = x.split(' ')
        if current_state == x[0] and current_character == x[1] and current_stack[0] == x[2]:
            if len(x) == 5:
                print('FOUND TRANSITION')
                return x[3].rstrip(), x[4].rstrip()
            else:
                print('FOUND TRANSITION')
                return x[3].rstrip(), current_stack[1:].rstrip()

    for x in config['Delta']:
        x = x.split(' ')
        if 'L' == x[0] and current_state == x[1] and current_stack[0] == x[2]:
            print('FOUND LAMBDA TRANSITION')
            return x[3].rstrip(), current_stack[1:].rstrip()

    return None, '0'

def dpda_sim():
    '''

    '''
    my_input = input()
    current_state = config['S']
    current_stack = config['I']

    for x in range(0, len(my_input)):
        if my_input[x] in config['Sigma']: #current character in alaphabet???
            print('Legal Character')
            current_state, current_stack = check_delta(current_state, my_input[x], current_stack)
            if len(current_stack) == 0:
                current_stack = '0'
            if current_state == None:
                print('REJECTED')
                break
        else:
            print('Illegal Character')
            print('REJECTED')
            break

        if x + 1 == len(my_input) and current_state in config['F']:
            print('ACCEPTED')

        elif x + 1 == len(my_input):
            while(current_state or current_state == 0):
                current_state, current_stack = check_delta(current_state, '', '0')
                if current_state in config['F']:
                    print('ACCEPTED')
                    break


def config_getter(config_location):
    '''

    '''
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
        config['F'] = f.readline().split(',')
        for x, value in enumerate(config['F']):
            config['F'][x] = value.rstrip()

    config['S'] = '0'

    config['I'] = config['Gamma'] [0]

def main(argv):
    '''

    '''
    if len(sys.argv) < 2:
        usage_string = 'usage: python ' + argv[0] + '/location/of/configuration/files'
        print(usage_string)
    else:
        config_getter(argv[1])
        dpda_sim()


main(sys.argv)
