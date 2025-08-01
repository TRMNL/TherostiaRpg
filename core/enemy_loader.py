# core/enemy_loader.py
import json
import random
from core.character import EnemyTemplate

def load_enemies():
    with open("enemies.json", "r") as f:
        return json.load(f)

def spawn_enemy(character):
    enemy_data = load_enemies()

    valid_enemies = {
        name: data for name, data in enemy_data.items()
        if character.level >= data["lvlstart"] and character.level <= data["lvlcap"]
    }

    if not valid_enemies:
        return None, None, None

    names = list(valid_enemies.keys())
    weights = [valid_enemies[n]["SpawnChance"] for n in names]
    chosen = random.choices(names, weights=weights, k=1)[0]
    props = valid_enemies[chosen]

    # I THINK I FUCKED THIS UP AHHHHHHHHHHHHHHHHHHHHHH 
    # Improve enemys later todo
    level_percent = (character.level - props["lvlstart"]) / (props["lvlcap"] - props["lvlstart"])
    hp_scale = 1 + (0.5 * level_percent)
    dmg_scale = 1 + (0.6 * level_percent)

    base_hp = int(props["Health"] * hp_scale)
    base_dmg = int(props["Damage"] * dmg_scale)

    #=== enemies Elite versions
    is_elite = random.random() < 0.10
    name = f"Elite {chosen}" if is_elite else chosen
    if is_elite:
        base_hp = int(base_hp * 1.5)
        base_dmg = int(base_dmg * 1.5)
        props["XP"] = int(props["XP"] * 1.5)

    enemy = EnemyTemplate(
        name=name,
        health=base_hp,
        damage=base_dmg,
        MaxHP=base_hp,
        lvlstart=props["lvlstart"],
        lvlcap=props["lvlcap"]
    )
    return enemy, props["LootTable"], props["XP"]
