import sys

config = dict.fromkeys(['Q', 'Sigma', 'Gamma', 'Delta', 'S', 'I', 'F'], None)

def transition(currentState):
    cs = currentState[2]
    cc = currentState[0]
    ts = currentState[1][len(stackContents) - 1]

def dpda_sim():
    my_input = input()

    for x in range(0, len(my_input) - 1):
        if my_input[x] in config['Sigma']: #current character in alaphabet???
            print('Legal Character')
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

    config['S'] = 0

    config['I'] = config['Gamma'] [0]

def main(argv):
    if len(sys.argv) < 2:
        usage_string = 'usage: python ' + argv[0] + '/location/of/configuration/files'
        print(usage_string)
    else:
        config_getter()


main(sys.argv[])
