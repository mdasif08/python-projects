from abc import ABC, abstractmethod

class Ticket(ABC):
    @abstractmethod
    def book_ticket(self):
        pass

class MakeMyTrip(Ticket):
    def book_ticket(self):
        name = input("Enter your name: ")
        phone_no = input("Enter your phone number: ")
        email_id = input("Enter your email address: ")
        journey_date = input("Enter the journey date: ")
        print(f"Thank you for booking with MakeMyTrip, {name}!")

class IRCTC(Ticket):
    def book_ticket(self):
        name = input("Enter your name: ")
        phone_no = input("Enter your phone number: ")
        email_id = input("Enter your email address: ")
        journey_date = input("Enter the journey date: ")
        trip_type = input("Select trip type (one-way/round-trip): ").lower()
        if trip_type == "round-trip":
            return_date = input("Enter the return date: ")
            print(f"Thank you for choosing IRCTC! Your round-trip is booked from {journey_date} to {return_date}.")
        else:
            print("Thank you for choosing IRCTC!")

class Indigo:
    def _init_(self, irctc):
        self.irctc = irctc

    def choose_transport_mode(self):
        print("Select mode of transport: Flight, Bus, or Train")
        mode = input("Enter your choice: ")
        print(f"You have chosen {mode} with IRCTC.")

# Example usage
if _name_ == "_main_":
    mmtrip = MakeMyTrip()
    mmtrip.book_ticket()

    irctc = IRCTC()
    irctc.book_ticket()

    indigo = Indigo(irctc)
    indigo.choose_transport_mode()