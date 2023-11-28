from tailcallexception import *


@tail_call_optimized
def factor(num, largest_factor):
    mod_result = num % largest_factor
    if mod_result == 0:
        print(f'prime = {largest_factor}')
        new_num = num // largest_factor
        factor(new_num, largest_factor)
    elif num <= largest_factor:
        print(f'largest prime = {largest_factor}')
    else:
        factor(num, largest_factor + 1)


if __name__ == '__main__':
    factor(600851475143, 2)
