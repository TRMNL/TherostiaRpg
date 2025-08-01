# Modding Therostia

In enemies.json all you need to do is add 
"Mob Name": {
"lvlstart": 1, (**What level the mob starts showing up**)
"lvlcap": 10, (**What level the mob stops showing**)
"Health": 9,  (**Health of enemy**)
"MaxHP": 9, (**MaxEnemy Health**)
"Damage": 2, (**Damage it deals**)
"SpawnChance": 0.15, (**Mob Spawn chance 0 to 1**)
"XP": 6,  (**How much xp the mob gives**)
"LootTable": { (**What the mob drops with item drop chance**)
	"Item name": LootChance   (**Can stack multple Items**)
}


# Files Easy to add and edit
enemies.json
Items/
	-   Crafting
	-	Currency
	-	Food
	-	Potions
	-	Junk
weapons.json

## WIP

Multiple Systems are not done these include 

1) Saving and Loading 
2) Currency implementation 
3) Magic spells and proper implementation
4) A buy and sell shop system

## Will add on a later date
1) Mini Bosses and bosses
2) Arena for gold rewards
3) Adventurers guild with a S rate ranking system
4) Crafting system
5)  Armor equipment
6)  Story line quests
