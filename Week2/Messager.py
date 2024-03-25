from datetime import datetime

def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")

class Messanger:
    def __init__(self, listeners=[]):
        self.listeners = listeners

    def send(self, message):
        print(message)
        print(self.listeners)
        for  listener in self.listeners:
            print(message)
            listener.receive(message)
        

    def receive(self, message):
        print("Message received at " + getCurrentTime()+": "+message)
        self.listeners.append(message)
        print(self.listeners)



class SaveMessages(Messanger):
    """A special kind of messanger that saves all messages"""
    def __init__(self, listeners=[]):
        super().__init__(listeners)
        self.messages = []

    def printMessages(self):
        for msg in self.messages:
            print(msg)
        self.messages.clear()

my_msg = SaveMessages([])
# Send some messages using the normal messanger class
for i in range(5):
    my_msg.send("This is message number " + str(i))

print("\n\nPrinting saved messages:\n")
my_msg.printMessages()
#my_msg.receive("Stop printing messages.")
