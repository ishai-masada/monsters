### Abilities

def hard_punch(player, enemy):
	enemy.hp -= 15 
	return f'hp has been reduced to: {enemy.hp}'

def push(player, enemy):
    enemy.hp -= 13
    return f'hp has been reduced to: {enemy.hp}'

def wiggle(player, enemy):
	enemy.hp -= 17
	return f'hp  has been reduced to: {enemy.hp}'

def fire_attack(player, enemy):
	enemy.hp -= 20
	return f'hp  has been reduced to: {enemy.hp}'

def nibble(player, enemy):
	enemy.hp -= 9
	return f'hp  has been reduced to: {enemy.hp}'

def crush(player, enemy):
	enemy.hp -= 3
	return f'hp  has been reduced to: {enemy.hp}'

def spear_attack(player, enemy):
	enemy.hp -= 3
	return f'hp  has been reduced to: {enemy.hp}'

def sting(player, enemy):
	enemy.hp -= 15
	return f'hp  has been reduced to: {enemy.hp}'
