
class ValidateException(Exception):
    pass

class BaseValidator(object):
    def __init__(self):
        self.empty_values = []

    def prepare_value(self, value):
        return value

    def to_python(self, value):
        return value

    def is_valid(self,value):
        return False

    def validate(self, value):
        if value in self.empty_values:
            raise ValidateException('Invalid Value')

    def __call__(self, value):
        return self.validate(value)

class StringValidator(BaseValidator):
    '''is string???'''
    def validate(self, value):
        if isinstance(value,(str,unicode)):
            return value
        else:
            raise ValidateException('Invalid Value')

class CellPhoneValidator(BaseValidator):
    cellphone_starts=[
        '130', '131', '132', '133', '134', '135', '136', '137', '138', '139',
        '145', '147',
        '150', '151', '152', '153', '155', '156', '157', '158', '159',
        '176', '178',
        '180', '181', '182', '183', '184', '185', '186', '187', '188', '189'
    ]

    def validate(self, value):

        value=value.strip()
        if len(value) == 11:
            if value[:3] in self.cellphone_starts:
                return True
        return False

class EmailValidator(BaseValidator):
    pass

class AddressValidator(BaseValidator):
    pass

class DateValidator(BaseValidator):
    pass

class TimeValidator(BaseValidator):
    pass

class DateTimeValidator(BaseValidator):
    pass

class BirthdayValidator(BaseValidator):
    pass

class EmailValidator(BaseValidator):
    pass

