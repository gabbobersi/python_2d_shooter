- [x] Reorganize in packages
- [x] Enemies
  - [x] Fix enemy movement
    - Move in random direction
      - [x] Get a new direction (only if we have reached the previous one)
    - [x] Limit the enemy movement inside screen boundary
  - [x] When the enemy has been hit by a bullet, it should be destroyed
- [x] Collision Manager

## Today
- [x] Enemies Spawner
  - You told the spawner what to spawn and where
  - [x] Random enemies spawn each time the enemy dies
- [x] Inventory system
  - [x] Player has an inventory
  - [x] From the start, player will has 5 bullets
  - [x] Each time player fires, bullets number decrease by 1
- [x] Loot system
  - [x] Ammunition boxes
    - Spawned in place of killed enemy
    - Static (no movement)
    - Each ammunition add 3 bullets
- [x] Bullet counter label


## Next time
- [ ] Fix the buggy main menu
- [ ] Implement interactive label
  - [ ] From the main menu, go to QUIT or test level scene
- [ ] Kill counter (with timer). 
  - The more the kill counter grows, ...(buff or money?!?!)
- [ ] Lifes system
- [ ] Save the last player position to keep when the player stops
- [ ] Draw some sprites 
  - [ ] player
  - [ ] enemy
  - [ ] bullet 