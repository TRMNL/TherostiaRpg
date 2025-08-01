import random

def level_up(character):
    leveled = False
    while character.XP >= character.MaxXP:
        character.level += 1
        character.XP -= character.MaxXP
        character.MaxXP = int(character.MaxXP * 1.8)

        hp_gain = random.randint(4, 8) + int(character.level * 0.5)
        dmg_gain = 0
        if character.level <= 5:
            dmg_gain = random.choice([1, 2])
        elif character.level <= 10:
            dmg_gain = 1
        elif character.damage < 80:
            dmg_gain = 1 if random.random() < 0.6 else 0

        character.MaxHP += hp_gain
        character.damage += dmg_gain
        leveled = True

        print(f"\n🎉 You leveled up to level {character.level}!")
        print(f"🩸 +{hp_gain} MaxHP | 🗡️ +{dmg_gain} Damage | 🎯 XP needed: {character.MaxXP}")
    return leveled
