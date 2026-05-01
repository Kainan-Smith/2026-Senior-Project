class Enemy:
    def __init__(self):
        self.maxHealth = 0
        self.currentHealth = self.maxHealth
        self.damge = 0

goblin = Enemy()
goblin.maxHealth = 100
goblin.damage = 30
goblin.currentHealth = goblin.maxHealth