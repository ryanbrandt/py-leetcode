from threading import Lock


class Foo:
    '''
    Concurrency problem

    Configure the class such that, given 3 threads are accessing the same instance
    and calling first, second and third in different orders, these methods are 
    fired in the order first -> second -> third

    Easy problem to solve with locks

    Difficulty: Easy
    '''

    def __init__(self):
        self.locks = (Lock(), Lock())

        self.locks[0].acquire()
        self.locks[1].acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.locks[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.locks[0]:
            printSecond()
            self.locks[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.locks[1]:
            printThird()
