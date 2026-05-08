class Enemy:
    def __init__(self):
        self.nae = "Enemy"
        self.maxHealth = 0
        self.currentHealth = 0
        self.strength = 0
        self.endurance = 0
        self.baseDamage = 0
        self.physicalAttackMod = 1
        self.defenseMod = 1
        self.condition = "None"

goblin = Enemy()
goblin.name = "Goplin"
goblin.maxHealth = 100
goblin.strength = 2
goblin.endurance = 2
goblin.baseDamage = 10
goblin.physicalAttackMod = 1 + (goblin.strength * 0.2)
goblin.defenseMod = 1 - (goblin.endurance / 10)
goblin.currentHealth = goblin.maxHealth