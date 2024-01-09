from observable import Observable, Subscriber

class Comanda(Observable):
    
    def ajuns_easybox(self):
        mesaj = "Comanda a ajuns in locker"
        print(mesaj)
        self.notify(mesaj)


class EmailSubscriber(Subscriber):

    def notify(self, event):
        print(f"Trimit un email cu {event}")


class SMSSubscriber(Subscriber):
     
     def notify(self, event):
        print(f"Trimit un SMS cu {event}")


class AppSubscriber(Subscriber):
    
    def notify(self, event):
        print(f"Trimit o notificare cu {event}")


comanda = Comanda()
email = EmailSubscriber()
sms = SMSSubscriber()
app = AppSubscriber()

comanda.subscribe(email)
comanda.subscribe(sms)
comanda.subscribe(app)

comanda.ajuns_easybox()
