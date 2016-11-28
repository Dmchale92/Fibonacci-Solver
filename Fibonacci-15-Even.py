"""
Generate a range of fibonacci numbers and pull the first 15 even Fibonacci numbers into evenFib.
Every third number is even so generate the first 45 terms. The 45th term is 1,134,903,170.
"""


class FibonacciSolver(object):
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("[Fibonacci-15-Even.py]-[TEST] - Running Unit Tests...")
        self.test_even_terms_for_range()
        print('[Fibonacci-15-Even.py]-[TEST] - Unit Tests completed...')
        return True

    @staticmethod
    def f():
        a, b = 0, 1
        yield a
        yield b
        while True:
            a, b = b, a + b
            yield b

    def sub_fib(self, start_number=1, end_number=10):
        for cur in self.f():
            if cur > end_number:
                return
            if cur >= start_number:
                yield cur

    def even_terms_for_range(self, start_number=1, end_number=10):
        all_fib = self.sub_fib(start_number, end_number)
        even_fib = []

        for i in all_fib:
            if len(even_fib) == 15:
                break
            if i % 2 == 0:
                even_fib.append(i)
            else:
                continue
        return even_fib

    def test_even_terms_for_range(self):
        first_two_even_terms = [2, 8]
        get_terms = (self.even_terms_for_range(1, 10))
        try:
            assert get_terms == first_two_even_terms
            print('[Fibonacci-15-Even.py]-[TEST] - [test_even_terms_for_range] - PASS')
            return True
        except Exception as e:
            print("[Fibonacci-15-Even.py]-[TEST] - [test_even_terms_for_range] - FAIL: " + str(e))
            return False

if __name__ == '__main__':
    """
        Instantiate FibonacciSolver() and run built-in unit tests
    """
    fs = FibonacciSolver()
    fs()
