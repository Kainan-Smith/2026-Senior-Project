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
        self.defeated = False

testDummy = Enemy()
testDummy.name = "Test Dummy"
testDummy.maxHealth = 200
testDummy.currentHealth = testDummy.maxHealth
testDummy.xpGiven = 50
testDummy.moneyGiven = 25
testDummy.itemDropped = items.skull

# Regular Area Enemies:

wolf = Enemy()
wolf.name = "Wolf"
wolf.maxHealth = 200
wolf.strength = 2
wolf.endurance = 2
wolf.attackMod = 1 + (wolf.strength * 0.2)
wolf.defenseMod = 1 - (wolf.endurance / 10)
wolf.currentHealth = wolf.maxHealth
wolf.itemDropped = items.wolfClaw
wolf.xpGiven = 40
wolf.moneyGiven = 20

hawk = Enemy()
hawk.name = "Hawk"
hawk.maxHealth = 300
hawk.strength = 3
hawk.endurance = 3
hawk.attackMod = 1 + (hawk.strength * 0.2)
hawk.defenseMod = 1 - (hawk.endurance / 10)
hawk.currentHealth = hawk.maxHealth
hawk.itemDropped = items.hawkTalon
hawk.xpGiven = 60
hawk.moneyGiven = 30

goblin = Enemy()
goblin.name = "Goblin"
goblin.maxHealth = 400
goblin.strength = 4
goblin.endurance = 4
goblin.attackMod = 1 + (goblin.strength * 0.2)
goblin.defenseMod = 1 - (goblin.endurance / 10)
goblin.currentHealth = goblin.maxHealth
goblin.itemDropped = items.goblinEye
goblin.xpGiven = 80
goblin.moneyGiven = 40

skeleton = Enemy()
skeleton.name = "Skeleton"
skeleton.maxHealth = 500
skeleton.strength = 5
skeleton.endurance = 5
skeleton.attackMod = 1 + (skeleton.strength * 0.2)
skeleton.defenseMod = 1 - (skeleton.endurance / 10)
skeleton.currentHealth = skeleton.maxHealth
skeleton.itemDropped = items.skull
skeleton.xpGiven = 100
skeleton.moneyGiven = 50

orc = Enemy()
orc.name = "Orc"
orc.maxHealth = 600
orc.strength = 6
orc.endurance = 6
orc.attackMod = 1 + (orc.strength * 0.2)
orc.defenseMod = 1 - (orc.endurance / 10)
orc.currentHealth = orc.maxHealth
orc.itemDropped = items.orcFang
orc.xpGiven = 120
orc.moneyGiven = 60

golem = Enemy()
golem.name = "Golem"
golem.maxHealth = 700
golem.strength = 7
golem.endurance = 7
golem.attackMod = 1 + (golem.strength * 0.2)
golem.defenseMod = 1 - (golem.endurance / 10)
golem.currentHealth = golem.maxHealth
golem.itemDropped = items.golemHead
golem.xpGiven = 140
golem.moneyGiven = 70

wyrm = Enemy()
wyrm.name = "Wyrm"
wyrm.maxHealth = 800
wyrm.strength = 8
wyrm.endurance = 8
wyrm.attackMod = 1 + (wyrm.strength * 0.2)
wyrm.defenseMod = 1 - (wyrm.endurance / 10)
wyrm.currentHealth = wyrm.maxHealth
wyrm.itemDropped = items.wyrmTooth
wyrm.xpGiven = 160
wyrm.moneyGiven = 80

demon = Enemy()
demon.name = "Demon"
demon.maxHealth = 900
demon.strength = 9
demon.endurance = 9
demon.attackMod = 1 + (demon.strength * 0.2)
demon.defenseMod = 1 - (demon.endurance / 10)
demon.currentHealth = demon.maxHealth
demon.itemDropped = items.demonWing
demon.xpGiven = 180
demon.moneyGiven = 90

# Bosses:

gargoyle = Enemy()
gargoyle.name = "Gargoyle"
gargoyle.maxHealth = 700
gargoyle.strength = 7
gargoyle.endurance = 7
gargoyle.attackMod = 1 + (gargoyle.strength * 0.2)
gargoyle.defenseMod = 1 - (gargoyle.endurance / 10)
gargoyle.currentHealth = gargoyle.maxHealth

king = Enemy()
king.name = "Corrupted King Averitt"
king.maxHealth = 1000
king.strength = 10
king.endurance = 10
king.attackMod = 1 + (king.strength * 0.2)
king.defenseMod = 1 - (king.endurance / 10)
king.currentHealth = king.maxHealth