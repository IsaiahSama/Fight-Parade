# Stats

As it sounds, the Stats class will take care of managaging and maintaining the core statistics of all Characters (players and enemies) alike.

These core statistics are:

- Level
- paradians
- exp
- max_exp
- tier
- health
- base_health
- power
- base_power
- defense
- base_defense
- crit_chance
- base_crit
- heal_chancne
- base_heal

## About Bases

Originally, when players set out on battles, a copy of their stats would be made, and that copy is what would take part in combat. This means that their original stats (apart from xp, level, money, items) would remain unaffected by the battle.

For this game however, this will no longer be the case. This means that when the player gets injured in battle, the player will retain those injuries post battle (although they will regen at a quicker rate).

In this game, you can modify your various stats via skills, gears and items. Bases serve to keep track of the unmodified stat.
