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
        # TODO: Experiment with a self.count variable that allows you to make spells that last multiple rounds.
heal1 = Spell()
heal1.name = "Heal α"
heal1.desc = "A basic healing spell."
heal1.manaCost = 10
heal1.number = 25
heal1.healing = True

heal2 = Spell()
heal2.name = "Heal λ"
heal2.dexc = "An intermediate healing spell."
heal2.manaCost = 20
heal2.number = 50
heal2.healing = True

heal3 = Spell()
heal3.name = "Heal Ω"
heal3.desc = "An advanced healing spell."
heal3.manaCost = 40
heal3.number = 100
heal3.healing = True

freeze1 = Spell()
freeze1.name = "Freeze α"
freeze1.desc = "Deals a small amount of damage and has a 20% chance to freeze enemies."
freeze1.manaCost = 10
freeze1.number = 20
freeze1.damage = True
freeze1.chance = 20

freeze2 = Spell()
freeze2.name = "Freeze λ"
freeze2.desc = "Deals a small amount of damage and has a 35% chance to freeze enemies."
freeze2.manaCost = 20
freeze2.number = 40
freeze2.damage = True
freeze2.chance = 35

freeze3 = Spell()
freeze3.name = "Freeze Ω"
freeze3.desc = "Deals a small amount of damage and has a 50% chance to freeze enemies."
freeze3.manaCost = 30
freeze3.number = 60
freeze3.damage = True
freeze3.chance = 50