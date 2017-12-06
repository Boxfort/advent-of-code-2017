#Read list
#Increment value
#Jump

instructions = list()
input_file = "5.txt"

if __name__ == '__main__':

    ip = 0
    steps = 0

    with open(input_file) as f:
        instructions = map(int, f.read().splitlines())

    while ip >= 0 and ip <= len(instructions) - 1:
        jump = instructions[ip] + ip
        instructions[ip] += 1
        ip = jump
        steps += 1

    print steps
