import inventory
charStats = {
    "Level": 1,

    "Constitution": 1,      # Affects Health
    "Arcana": 1,            # Affects Mana
    "Attunement": 1,        # Affects Spell Slots
    "Intelligence": 1,      # Affects Spell Damage Modifier
    "Strength": 1,          # Affects Attack Modifier
    "Endurance": 1,         # Affects Defense Modifier

    "Health": 100,
    "Mana": 100,
    # Modifiers are from 0 to 100
    "Spell Damage Modifier": 1,
    "Attack Modifier": 1,
    "Defense Modifier": 1,  # Damage is calculated in combat as: damageTaken = incomingDamage - (incomingDamage * "Defense Modifier")
}

def showPlayerStats(playerStats):
    for key, value in charStats.items():
        print(f"{key:<25}{value:>5}")

showPlayerStats(charStats)