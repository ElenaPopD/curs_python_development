class Observable:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def notify(self, event):
        for subscriber in self._subscribers:
            subscriber.notify(event)

class Subscriber:
    def notify(self, event):
        pass
