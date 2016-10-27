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
        self.hire_list = ["drummer", "guitarist", "bassist"]
        self.band_members = []
        self.hired_list = []
        
    def hire(self):
#hiring band members
        for item in self.hire_list:
            while True:
                new_member = input("Are you a guitarist, bassist or drummer? ")
                if new_member not in self.band_members and new_member in self.hire_list:
                    self.band_members.append(new_member)
                    self.hired_list.append(new_member)
                    print("You are hired!")
                    break
                elif new_member in self.band_members:
                    print("Sorry, we have already hired one...")
                    break
                else:
                    print("Sorry, I didn't get that...")
                    continue
        print(self.band_members)
        return self.band_members, self.hired_list
            
    def fire(self):
#firing band members
        for item in self.hired_list:
            ask_member = input("Did you practice our gig yesterday?" + "\nyes/no: ")
            if ask_member == "no":
                self.band_members.remove(item)
                print("You are fired!")
            elif ask_member == "yes":                    
                print("Well done!")
            else:
                ask_member = input("I didn't get that... Did you practice our gig yesterday?" + "\nyes/no: ")
        print(self.band_members)
        return self.band_members

    def check_drummer(self):
#checking if there is a drummer
        if "drummer" in self.band_members:
            print("Let's play then!")
            return True
        else:
            print("Sorry, but we don't have a drummer!")
            return False
    def check_bassist(self):
#checking if there is a bassist
        if "bassist" in self.band_members:
            return True    
    def check_guitarist(self):
#checking if there is a guitarist
        if "guitarist" in self.band_members:
            return True 
"""            
    def play_solo(self):
#playing solo
        for member in self.band_members:
            if "drummer" in self.band_members:
                member.solo(6)
            if "guitarist" in self.band_members:
                member.solo(6)
            if "bassist" in self.band_members:
                member.solo(6)
"""
#creating instances for each class            
bandx = Band()
bob = Guitarist()
nick = Drummer()
paul = Bassist()
    
if __name__ == "__main__":
    bandx.hire()
    bandx.fire()
    drummer = bandx.check_drummer()
    if drummer == True:
        nick.counting()
        nick.solo(6)
    bassist = bandx.check_bassist()
    if bassist == True:
        bob.solo(6)
    guitarist = bandx.check_guitarist()
    if guitarist == True:
        paul.solo(6)        
        