import abc


class AbstractValidator(object):
    __metaclass__  = abc.ABCMeta
    @abc.abstractmethod
    def validate(self, to_be_validated):
        """validate the input"""


class InputDataValidator(AbstractValidator):
    def validate_if_number_is_int(self, input):
        try:
            val = int(input)
            return val
        except ValueError:
            print("That's not an int!")