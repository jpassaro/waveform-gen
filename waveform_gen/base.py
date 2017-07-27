from pydub.generators import SignalGenerator

class PeriodicSignal(SignalGenerator):
    """A periodic signal based on a frequency.

    This takes a number between 0.0 and 1.0 and implements the periodic
    function in terms of that.

    :param freq: frequency in Hertz (periods per second)
    :param periodic_function: a periodic function. If not specified, uses
        the method from the class. If specified, should have the same
        signature as :meth:`.MySignal.periodic_function`.
    """
    def __init__(self, frequency, periodic_function=None, **kwargs):
        super(PeriodicSignal, self).__init__(**kwargs)
        self.freq = frequency
        if periodic_function is not None:
            self.periodic_function = periodic_function

    def generate(self):
        n = 0
        period_in_samples = self.sample_rate / self.freq
        while True:
            place = n / period_in_samples
            yield self.periodic_function(place - int(place))
            n += 1

    @staticmethod
    def periodic_function(fraction_of_period):
        """Given the part of a period, returns a float between -1.0 and 1.0."""
        raise NotImplementedError


class OddPeriodicSignal(PeriodicSignal):
    """A periodic signal where the second half of the period is exactly
    negative the first half.

    :param half_arc_function: potentially replaces builtin half_arc_function
    """
    def __init__(self, frequency, half_arc_function=None, **kwargs):
        if 'periodic_function' in kwargs:
            raise ValueError
        super(OddPeriodicSignal, self).__init__(frequency, **kwargs)
        if half_arc_function is not None:
            self.half_arc_function = half_arc_function

    @classmethod
    def periodic_function(cls, fraction_of_period):
        y = cls.half_arc_function(((4 * fraction_of_period) % 2.0) - 1)
        if fraction_of_period >= 0.5:
            y *= -1
        return y

    @staticmethod
    def half_arc_function(x):
        """Returns a number from -1.0 to 1.0. (Most likely positive.)

        :param x: a number from -1.0 to 1.0
        """
        raise NotImplementedError
