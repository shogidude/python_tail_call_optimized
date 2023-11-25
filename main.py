import sys


class TailCallException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(func):
    def wrapper(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailCallException(args, kwargs)
        else:
            while True:
                try:
                    return func(*args, **kwargs)
                except TailCallException as e:
                    args = e.args
                    kwargs = e.kwargs

    return wrapper


@tail_call_optimized
def factor(num, largest_factor):
    mod_result = num % largest_factor
    if mod_result == 0:
        print(f'prime = {largest_factor}')
        new_num = num // largest_factor
        factor(new_num, largest_factor)
    elif num == largest_factor:
        print(f'largest prime = {largest_factor}')
    else:
        factor(num, largest_factor + 1)


if __name__ == '__main__':
    factor(600851475143, 2)
