import abc


class AbstractValidator(object):
    __metaclass__  = abc.ABCMeta
    @abc.abstractmethod
    def validate(self, to_be_validated):
        """validate the input"""

class This_is_not_int(Exception):
    pass

class InputDataValidator(AbstractValidator):
    def __init__(self):
        self.output = ""

    def validate_if_number_is_range_1_9(self, input):
        if input >=1 and input <=9:
            return True
        else:
            return False

    def validate_if_number_is_int(self, input):
        try:
             int(input)
        except ValueError:
            return False
        else:
            return True

    def validate(self, data):

        if self.validate_if_number_is_int(data):
           if self.validate_if_number_is_range_1_9(data):
               self.output = "True"
           else:
               self.output = "The number is in bad range!\n"
        else:
            self.output = "That's not an int!\n"
        return self.output