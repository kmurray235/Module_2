import random

#Project: Defeat the Evil Wizard  
# Base Character class
class Character:
    def __init__(self, name, health, attack_power, defense_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense_power = defense_power       
        self.max_health = health  # Store the original health for maximum limit
    

    #Attacks for random damage
    def attack(self, opponent):
        attack_damage = random.randint(1,10)
        opponent.health -= attack_damage
        print(f"{self.name} attacks {opponent.name} for {attack_damage} damage!")
        if opponent.health >= opponent.max_health:
         opponent.health == opponent.max_health
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
        
        
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}, Defense Power: {self. defense_power}")


    #Attack to heal health
    def health_attack(self):
        health_gain = random.randint(1,5)
        self.health += health_gain

        if self.health < self.max_health:
         print(f"{self.name} regenerates {health_gain} health!")
       
        if self.health >= self.max_health:
         self.health == self.max_health
         print(f" {self.name} is fully healed. Current health: {self.max_health}")



# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, defense_power=50)  # Boost health and attack power

    # Add your power attack method here
    def special_attack(self, opponent):
        attack_gain = random.randint(1,10)
        calculate_attack_increase = (attack_gain/10)*100
        self.attack_power += calculate_attack_increase
        print(f"\n{opponent.name} is shaken. {self.name} attack raised to {self.attack_power}\n"
              f"{opponent.name}'s defense is now {opponent.defense_power}\n")
       
    def special_defense(self,opponent):
        health_gain = random.randint(1,10)
        self.health += health_gain

        if self.health >= self.max_health:
         self.health == self.max_health
         print(f"{self.name} is at the max health of {self.max_health}")

        if self.health < self.max_health:
         print(f"{self.name} calls upon the elders to gain "+ str(health_gain) + " in health")
         
        print(f"{opponent.name} is thinking fast")
       

    
# Mage class (inherits from Character)
class Mage(Character):
    
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, defense_power=25)  # Boost attack power

    # Add your cast spell method here
    def special_defense(self,opponent):
        spell_defense=random.randint(1,5)
        spell_names = ["Water spell", "Fire spell", "Earth spell"]
        random_spell = random.choice(spell_names)
        print (f"{self.name}  cast {random_spell} ! Spell increases attack by {spell_defense} points" )
        print (f"{opponent.name} is getting nervous!")

    def special_attack(self, opponent):
        spell_attack = random.randint(1,5)
        health_bonus = (spell_attack * 2)
        opponent.health -= health_bonus
        print(f"{self.name} gains {health_bonus} in health and does {health_bonus} in attack to {opponent.name}")
        print(f"Current health for {opponent.name} is {opponent.health}")




# Archer class (inherits from Character)
class Archar(Character):
    def __init__(self, name,):
        super().__init__(name, health=100, attack_power=100,defense_power=75)
       
       

    # Archer's special ability: Doubles the rate of attack(increases accercy) 
    # Acceracy is normally 25% 
    # increases to 75% 
    # or Changes of a critical hit increase 
    # Something with arrows

    def special_attack(self,opponent):  
        accuracy = random.randint(1,10)
        calculate_accuracy = (accuracy/10)*100
        damage = (calculate_accuracy * self.attack_power) + self.attack_power
        print (f"Archer calls flaming arrows to rain down upon you")
        print(f"Archer deals total damage of {damage} to {opponent.name}")
        opponent.health -= damage
        print(f"{opponent.name} health is now {opponent.health}")


    #Archer's special ability: uses sneaky skills to dodge
    def special_defense(self,opponent):         
        print (f"Archer throws a smoke bomb! {opponent.name}'s attack misses")
        print (f"Health was uneffected. Current health level{self.health}")


# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=200, defense_power=150)
        

    #Paladin does something with double damage
    def special_attack(self, opponent):
        attack_strength = random.randint(1,10)
        double_damage = (attack_strength *2)
        opponent.self.health -= double_damage
        print(f"Paladin deals double damage for a total of {double_damage}")
        print(f"The {opponent.name}'s health is now {opponent.health} !")

    #Palaid's special ability: it can block any attack
    def special_defense(self, opponent):                                                                          
        """Uses a shield to lower defense"""
        shield_power =random.randint(1,5)
        opponent.defense_power -= shield_power
        print(f"\n{opponent.name} is shaken. Their defense lowers by {shield_power}\n"
              f"{opponent.name}'s defense is now {opponent.defense_power}\n")
        print (f"Paladin blocks the attack with a shield. Health is uneffective")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, defense_power=50)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        if self.health >= self.max_health:
            self.health == self.max_health
        print (f"{self.name} is at max health! Current health is {self.max_health}")
        if self.health < self.max_health:
         print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def special_attack(self, opponent):
        cast_spell = random.randint(1,10)
        opponent.attack_power -= cast_spell
        print(f"{self.name} casts a spell to lower {opponent.name} attack power to {opponent.attack_power}")
#_______________________________________________________________________________________________


           

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")  
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archar(name)        
    elif class_choice == '4':
        return Paladin(name)        
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)



# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            random.choice([player.special_attack(wizard), player.special_defense(wizard)])
            
        elif choice == '3':
            player.health_attack()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            random.choice([wizard.special_attack(player),  wizard.attack(player)])
           

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
        exit()
    

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()
   

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)


if __name__ == "__main__":
    main()
