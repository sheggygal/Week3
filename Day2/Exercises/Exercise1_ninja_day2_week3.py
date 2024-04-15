class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_info = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_info)
        self.call_history.append(call_info)

    def show_call_history(self):
        print("Call History:")
        for call in self.call_history:
            print(call)

    def send_message(self, other_phone, content):
        message_info = {"to": other_phone.phone_number, "from": self.phone_number, "content": content}
        self.messages.append(message_info)

    def show_outgoing_messages(self):
        print("Outgoing Messages:")
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(message)

    def show_incoming_messages(self):
        print("Incoming Messages:")
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(message)

    def show_messages_from(self, other_phone):
        print(f"Messages from {other_phone.phone_number}:")
        for message in self.messages:
            if message["from"] == other_phone.phone_number:
                print(message)


phone1 = Phone("123-456-7890")
phone2 = Phone("987-654-3210")

phone1.call(phone2)
phone2.call(phone1)

phone1.send_message(phone2, "Hey, how are you?")
phone2.send_message(phone1, "I'm good, thanks!")

phone1.show_call_history()
print()
phone1.show_outgoing_messages()
print()
phone1.show_incoming_messages()
print()
phone1.show_messages_from(phone2)




