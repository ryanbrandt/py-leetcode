from threading import Event, Lock


class FooBar:
    '''
    Concurrency problem

    Two threads are firing off foo and bar asynchronously n times.
    Ensure that these methods are called synchronously
    foo -> bar -> foo -> bar...

    Simple problem solvable with Event

    Difficulty: Medium
    '''

    def __init__(self, n):
        self.n = n

        self.foo_e = Event()
        self.bar_e = Event()

        self.foo_e.set()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.foo_e.wait()
            printFoo()
            self.foo_e.clear()
            self.bar_e.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.bar_e.wait()
            printBar()
            self.bar_e.clear()
            self.foo_e.set()
