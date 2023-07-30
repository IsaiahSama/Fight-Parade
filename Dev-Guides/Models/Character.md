# Character

Character are the base model for all Characters, including Player, enemies, and raid enemies.

The attributes for Characters are:

- name
- id
- level
- health
- power
- heal_chance
- crit_chance
- weapon
- armour
- ability
- passive
- tier

## Player / Fighter

Players (also referred to as Fighters) are the characters that the player will be using to play the game.

The unique attributes for players are:

- paradians (pcoins)
- inventory

## Enemies

Enemies are entities that the Player will encounter as they engage on quests and raids.

Unique attributes for enemies are:

- entry message
- attack_message
- xp_yield
- paradians_yield
- item

### Entry message

This is the message that is displayed when the enemy appears

### Attack_message

This is the message displayed when the enemy attacks. Will change if the enemy is wielding a weapon.

### Yields

When defeated, enemies will grant the player exp and paradians.

### Item

Enemies may sometimes hold an item, that they will drop for the player when defeated.
