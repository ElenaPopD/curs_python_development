class Chain(object):
    max_amount = 0
    def __init__(self, nume):
        self.nume = nume
    def set_next(self, next):
        self.next = next

    def can_handle(self, request):
        return request <= self.max_amount

    def handle(self, request):
        if self.can_handle(request):
            print(f"Aprobat de catre {self.nume}")
            return "Ok"
        else:
            print(f"Pasat mai departe catre {self.next.nume}")
            return self.next.handle(request)