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
        print("\n")
            
    def combust(self): #producing combustion sound
        print("Bang!")
        
class Band(object): #A new class Band to hire and fire members
    def __init__(self):
        self.band_members = {"drummer": None, "guitarist": None, "bassist": None}
        
    def hire(self):
#hiring band members
            for item in self.band_members:
                while True:
                    new_member = input("Are you a guitarist, bassist or drummer? ")
                    if new_member in self.band_members and self.band_members[item] == None:
                        self.band_members[item] = True
                        print("You are hired!")
                        print(self.band_members)
                        break
                    elif new_member in self.band_members and self.band_members[item] == True:
                        print("Sorry, we have already hired one...")
                        print(self.band_members)
                        break
                    else:
                        print("Sorry, I didn't get that...")
                        print(self.band_members)
                        continue
            print(self.band_members)
            return self.band_members
    def fire(self):
#firing band members
        for i in self.band_members:
            ask_member = input("Did you practice our gig yesterday?" + "\nyes/no: ")
            if ask_member == "no":
                self.band_members[i] = False
                print("You are fired!")
            elif ask_member == "yes":                    
                print("Well done!")
            else:
                ask_member = input("I didn't get that... Did you practice our gig yesterday?" + "\nyes/no: ")
        print(self.band_members)
        return self.band_members
        
    def play_solo(self):
#playing solo
            if self.band_members["drummer"] == True:
                print("Let's play then!")
                nick.counting()
                nick.solo(6)
                if self.band_members["guitarist"] == True:
                    bob.solo(6)
                if self.band_members["bassist"] == True:
                    paul.solo(6)
                else:
                    print("Oops, we need to hire more musicians...")
            else:
                print("Sorry, but we don't have a drummer!")        

if __name__ == "__main__":
    bandx = Band()
    bob = Guitarist()
    nick = Drummer()
    paul = Bassist()
    bandx.hire()
    bandx.fire()
    bandx.play_solo()