import items

class Enemy:
    def __init__(self):
        self.nae = "Enemy"
        self.maxHealth = 0
        self.currentHealth = 0
        self.strength = 0
        self.endurance = 0
        self.baseDamage = 0
        self.attackMod = 1
        self.defenseMod = 1
        self.condition = None
        self.currentWeapon = items.basicSword
        self.xpGiven = 0
        self.moneyGiven = 0
        self.itemDropped = None

testDummy = Enemy()
testDummy.name = "Test Dummy"
testDummy.maxHealth = 200
testDummy.currentHealth = testDummy.maxHealth
testDummy.xpGiven = 50
testDummy.moneyGiven = 25
testDummy.itemDropped = items.skull

# Regular Area Enemies:

wolf = Enemy()
wolf.itemDropped = items.wolfClaw

hawk = Enemy()
hawk.itemDropped = items.hawkTalon

goblin = Enemy()
goblin.name = "Goplin"
goblin.maxHealth = 400
goblin.strength = 2
goblin.endurance = 0
goblin.attackMod = 1 + (goblin.strength * 0.2)
goblin.defenseMod = 1 - (goblin.endurance / 10)
goblin.currentHealth = goblin.maxHealth
goblin.itemDropped = items.goblinEye

skeleton = Enemy()
skeleton.itemDropped = items.skull

orc = Enemy()
orc.itemDropped = items.orcFang

golem = Enemy()
golem.itemDropped = items.golemHead

wyrm = Enemy()
wyrm.itemDropped = items.wyrmTooth

demon = Enemy()
demon.itemDropped = items.demonWing

# Bosses:

gargoyle = Enemy()

king = Enemy()