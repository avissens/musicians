class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician): #A new class of drummers
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Stick", "Hand", "Mallet"]) 
        
    def counting(self): #counting to 4
        for i in range(1,5):
            print(i)
            
    def combust(self): #producing combustion sound
        print("Bang!")
        
class Band(object): #A new class Band to hire and fire members
    def __init__(self):
        self.band_members = []
        
    def hire(self):
#hiring band members
        band_members = ["drummer", "guitarist", "bassist"]
        members = []
        while len(members) < 3:
            new_member = input("Are you: guitarist, bassist or drummer? ")
            if new_member not in members and new_member in band_members:
                members.append(new_member)
                print("You are hired!")
            elif new_member not in band_members:
                print("Sorry, I didn't get that...")
                continue
            else:
                print("Sorry, we have already hired one...")
                continue
        print(members)
        
    def fire(self):
#firing band members
        band_members = {"drummer":"hired", "guitarist":"hired", "bassist":"hired"}
        for i in band_members:
            ask_member = input("Did you practice our gig yesterday?" + "\nyes/no: ")
            if ask_member == "no":
                band_members[i] = "fired"
                print("You are fired!")
            elif ask_member == "yes":                    
                print("Well done!")
            else:
                ask_member = input("I didn't get that... Did you practice our gig yesterday?" + "\nyes/no: ")
        print(band_members)
    
    def play_solo(self):
#playing solo
        nick.counting()
        paul.solo(5)
        bob.solo(5)
        
if __name__ == "__main__":
    bandx = Band()
    bob = Guitarist()
    nick = Drummer()
    paul = Bassist()
    bandx.hire()
    bandx.fire()
    bandx.play_solo()
    


