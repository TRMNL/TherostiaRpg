class CharacterTemplate:
    def __init__(self, name, level, health, MaxHP, damage, XP, MaxXP, minMana, maxMana ,weapon, inventory): 
        self.name = name
        self.level = level
        self.health = health
        self.MaxHP = MaxHP
        self.damage = damage
        self.XP = XP
        self.MaxXP = MaxXP
        self.minMana = minMana
        self.maxMana = maxMana
        self.weapon = None
        self.inventory = {}

    def attack(self, target):
        total_damage = self.damage + self.weapon.bonus_damage
        target.health -= total_damage
        print(f"{self.name} attacks {target.name} with a {self.weapon.name} for {total_damage} damage!")
        
class EnemyTemplate:
    def __init__(self, name, health, damage, MaxHP, lvlstart, lvlcap): 
        self.name = name
        self.health = health
        self.damage = damage
        self.MaxHP = MaxHP
        self.lvlstart = lvlstart
        self.lvlcap= lvlcap

    def attack(self, target):  # ← Add this!
        target.health -= self.damage
        print(f"{self.name} attacks {target.name} for {self.damage} damage!")   