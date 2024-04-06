#Clean the screen
import os
def Clear_Screen():
      os.system('cls' if os.name == 'nt' else 'clear')   

#My buss        
class Buss:
        passagerare = []
        antal_passagerare = 25
        def run(self):  
#Opening for user
                print("Välkommen till Buss-simulatorn")
#Loop and menu choices
                while True:
                        print("Välj ett av följande i menyn\n")
                        print("1. Boka din bussplats här!") 
                        print("2. Antal passagerare och deras ålder")
                        print("3. Beräkna totala åldern på passagerarna")
                        print("4. Beräkna genomsnittliga åldern på passagerarna")
                        print("5. Avsluta\n")
                        choice = input ("Ange ditt val: ")
                        print()
#statements for menu choices                        
                        if choice == "1":
                                self.add_passenger()
                        elif choice == "2":
                                self.print_buss()
                        elif choice == "3":
                                self.calc_total_age()
                        elif choice == "4":
                                self.calc_average_age()
                        elif choice == "5":
                                self.exit_program()
                                break
                        else:
                                print("Vänligen försök igen")
#Menuchoice 1 - Add passenger to buss
        def add_passenger(self):
                if len(self.passagerare) < self.antal_passagerare:
                        name = input("Skriv in passagerarens namn: ")
                        age = int(input("Skriv in din ålder: "))
                        while True:
                                gender = input("Skriv in om du är man eller kvinna: ")
                                if gender.lower() == "man" or gender.lower() == "kvinna":
                                        break
                                else:
                                        print("Ogiltigt val. Vänligen försök igen.")
                        Clear_Screen()
                        passenger = {"namn": name, "ålder": age, "kön": gender}                                
                        self.passagerare.append(passenger)
#If they successfully got a seat                        
                        print("Du har nu en bokad plats!\n")
                        input("Tryck Enter för att återgå till menyn")
                        Clear_Screen()
#If the bus is full                        
                else:
                        print("Bussen är tyvärr fullbokad!")
                        input("Tryck Enter för att återgå till menyn")
                        Clear_Screen()

#Menuchoice 2 - Booked passengers and their age
        def print_buss(self):
                for i, passenger in enumerate(self.passagerare):
                        print(f"Passagerare {i+1}: Ålder: {passenger['ålder']}")
                print(f"Totalt antal passagerare: {len(self.passagerare)} \n")
                input("Tryck Enter för att återgå till menyn")
                Clear_Screen()

#Menuchoice 3 - Calculate total age
        def calc_total_age(self):
                Clear_Screen()
                total_age = sum(int(passenger['ålder']) for passenger in self.passagerare)
                print(f"Total ålder på passagerarna: {total_age}\n")
                input("Tryck Enter för att återgå till menyn")
                Clear_Screen()

#Menuchoice 4 - Calculate average age
        def calc_average_age(self):
                if self.passagerare:
                        total_age = sum(int(passenger['ålder']) for passenger in self.passagerare)
                        average_age = total_age / len(self.passagerare)
                        print(f"Genomsnittliga ålder på passagerarna: {average_age}\n")
                        input("Tryck Enter för att återgå till menyn")
                        Clear_Screen()
                else:
                        print("Inga passagerare finns")
                        input("Tryck Enter för att återgå till menyn")
                        Clear_Screen()
 #Menuchoice 5 - Exit program                      
        def exit_program(self):
                print("Avslutar programmet")
                exit()
                
if __name__ == "__main__":
    minbuss = Buss()
    minbuss.run()