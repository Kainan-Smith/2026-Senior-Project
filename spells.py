class Spell:
    def __init__(self):
        self.name = "Spell Name"    # The name of the spell.
        self.desc = ""              # A brief description of the spell.
        self.known = False          # Does the player know the spell?
        self.manaCost = 0           # The amount of mana required to cast the spell.
        self.number = 0             # Either base damage or base healing for the spell.
        self.damage = False         # Does the spell do damage?.
        self.healing = False        # Does the spell heal you?.
        self.chance = 0             # If the spell has a random chance to have an effect, this value will be used as a %.
        self.lasts = 0              # How long does the spell last?
        self.condition = "None"

heal1 = Spell()
heal1.name = "Minor Heal"
heal1.desc = "A basic healing spell."
heal1.manaCost = 10
heal1.number = 25
heal1.known = True
heal1.healing = True

heal2 = Spell()
heal2.name = "Major Heal"
heal2.dexc = "An intermediate healing spell."
heal2.manaCost = 20
heal2.number = 50
heal2.healing = True

heal3 = Spell()
heal3.name = "Full Heal"
heal3.desc = "An advanced healing spell."
heal3.manaCost = 40
heal3.number = 100
heal3.healing = True

freeze1 = Spell()
freeze1.name = "Frost"
freeze1.desc = "Deals a small amount of damage and has a 60% chance to freeze enemies."
freeze1.manaCost = 10
freeze1.number = 20
freeze1.damage = True
freeze1.chance = 60
freeze1.known = True
freeze1.condition = "Frozen"

freeze2 = Spell()
freeze2.name = "Icicle"
freeze2.desc = "Deals a small amount of damage and has a 80% chance to freeze enemies."
freeze2.manaCost = 20
freeze2.number = 40
freeze2.damage = True
freeze2.chance = 80
freeze2.condition = "Frozen"

freeze3 = Spell()
freeze3.name = "Glacier"
freeze3.desc = "Deals a small amount of damage and has a 100% chance to freeze enemies."
freeze3.manaCost = 30
freeze3.number = 60
freeze3.damage = True
freeze3.chance = 100
freeze3.condition = "Frozen"

burn1 = Spell()
burn1.name = "Kindle"
burn1.desc = "Deals a small amount of damage and has a 60% chance to burn enemies."
burn1.manaCost = 10
burn1.number = 20
burn1.damage = True
burn1.chance = 60
burn1.known = True
burn1.condition = "Burned"

burn2 = Spell()
burn2.name = "Blaze"
burn2.desc = "Deals a small amount of damage and has a 80% chance to burn enemies."
burn2.manaCost = 20
burn2.number = 40
burn2.damage = True
burn2.chance = 80
burn2.condition = "Burned"

burn3 = Spell()
burn3.name = "Inferno"
burn3.desc = "Deals a small amount of damage and has a 100% chance to burn enemies."
burn3.manaCost = 30
burn3.number = 60
burn3.damage = True
burn3.chance = 100
burn3.condition = "Burned"

lightning1 = Spell()
lightning1.name = "Thunder"
lightning1.desc = "Deals a large amount of damage, small chance to crit."
lightning1.manaCost = 10
lightning1.number = 30 # Was changed from 40 for testing
lightning1.damage = True
lightning1.chance = 100
lightning1.known = True
lightning1.condition = "Crit"

lightning2 = Spell()
lightning2.name = "Lightning Bolt"
lightning2.desc = "Deals a large amount of damage, small chance to crit."
lightning2.manaCost = 20
lightning2.number = 80
lightning2.damage = True
lightning2.chance = 20
lightning2.condition = "Crit"

lightning3 = Spell()
lightning3.name = "Stormcloud"
lightning3.desc = "Deals a large amount of damage, small chance to crit."
lightning3.manaCost = 30
lightning3.number = 120
lightning3.damage = True
lightning3.chance = 30
lightning3.condition = "Crit"

# TODO: Think about adding earth spells

allSpells = [
    heal1, heal2, heal3,
    freeze1, freeze2, freeze3,
    burn1, burn2, burn3,
    lightning1, lightning2, lightning3
]