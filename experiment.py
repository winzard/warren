import getopt
import random
import sys


def red():
    return random.choice([0.05, 0.2, 1, 3, 3, 3])

def blue():
    return random.choice([0.95, 1, 1, 1, 1, 1.1])

def green():
    return random.choice([0.8, 0.9, 1.1, 1.1, 1.2, 1.4])


def emulate(r, g, b, steps=20):
    amount = 1000.0
    for _ in range(steps):
        _r = amount*r
        _g = amount*g
        _b = amount*b
        amount = _r*red() + _g*green() + _b*blue()
    return amount

if __name__ == "__main__":
    steps = 20
    r = 33
    b = 33
    g = 34
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hr:g:b:", ["steps="])
    except getopt.GetoptError:
        print('experiment.py -r Red Fund % -g Green Fund % -b Blue Fund % --steps= Steps [20]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('experiment.py -r Red Fund % -g Green Fund % -b Blue Fund % --steps= Steps [20]')
            sys.exit()
        elif opt in ["-g"]:
            g = int(arg)
        elif opt in ["-r"]:
            r = int(arg)
        elif opt in ["-b"]:
            b = int(arg)
        elif opt in ["--steps"]:
            steps = int(arg)
    if r + g + b == 100:
        print(emulate(float(r/100), float(g/100), float(b/100), steps=steps))
    else:
        print(r, g, b, type(r))
