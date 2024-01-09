class BancomatException(Exception):
    pass

class BancomatFaraBani(BancomatException):
    pass

class FonduriInsuficient(BancomatException):
    pass

class PinGresit(BancomatException):
    pass