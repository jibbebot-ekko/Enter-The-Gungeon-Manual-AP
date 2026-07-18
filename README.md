# Enter-The-Gungeon-Manual-AP

# Required software
- The newest release of this .apworld which can be found in releases
- Archipelago client
- The latest release of manual Archipelago
- A legal copy of Enter the Gungeon on PC
- BepInExPack for Enter the Gungeon https://thunderstore.io/c/enter-the-gungeon/p/BepInEx/BepInExPack_EtG/
- Mod the Gungeon API https://thunderstore.io/c/enter-the-gungeon/p/MtG_API/Mod_the_Gungeon_API/

# Setup Guide
1. Download Thunderstore and, through it, BepInExPack and Mod the Gungeon API.
2. Download and install this .apworld (either double click or put in custom worlds folder).
3. Adjust the .yaml file to your liking and send it to the AP host. If you are the host, put the .yaml in the players folder of your Archipelago install.
4. If you don't have the manual client, download and install the latest version.
5. Connect to the multiworld using the manual client.
6. Launch ETG through the thunderstore launcher with BepInExPack and mod the Gungeon API active and start playing.

# How does this randomizer work?
Gungeoneers and chambers beyond the Keep of the Lead Lord are locked, items you receive will unlock gungeoneers and chamber keys which allow you to progress deeper into the Gungeon. To finish the game, you have to kill the past of a set amount of gungeoneers, this amount can be adjusted in the options file.
Location checks are the first and second chest of each chamber, the shops, bosses, killing the past, and master rounds. The yaml includes options to have these be checks for each gungeoneer individually or just once.
To check of each location, unlock or destroy each chest, buy at least one item from the store, defeat the boss, and acquire its master round.
Shortcuts and other useful items are also available in the pool, their use is detailed below. Some items require use of the console which can be accessed using F2 ingame.
Death link is available, you send a deathlink if you lose a run, receiving a deathlink means going back to the breach, or dying intentionally once if you have any items (i.e. Clone) that prevent death.

Items you can receive:

- Chamber key x
Chamber keys unlock the chambers of the gungeon, you are only allowed to progress to a chamber (including secret chambers) if you have the corresponding key.

- Prime Primer, Obsidian Shell Casing, Arcane Gunpowder, Planar Lead.
All parts of the bullet that can kill the past are required to access the past.

- The Pilot, The Marine, etc.
Receiving a gungeoneer unlocks that gungeoneer as playable. By default, you start with one random gungeoneer, which you can see in the received items tab of the manual client. Some gungeoneers, such as the cultist and cut content gungeoneers cannot be selected normally. To play as these gungeoneers use the "character" command in the console (e.g. "character cosmonaut").

- Shortcut Chamber x
These items unlock their respective shortcut, you are only allowed to use the shortcuts of chambers you have access to normally (Have the key + Previous chamber unlocked)

- Progressive starting keys, blanks, armor
These items allow the player to start with additional boons at the start of the run. For blanks, armor, and keys spawn in an amount equal to the number of progressive starting x of that type you have using the "spawn item" command (e.g. "spawn item blank 2" if you have 2 progressive starting blank). Do this at the start of each new run.

- Progressive starting chest
Similar to progressive starting item, this allows the player to start with a little extra at the start. The table below dictates what kind of chest you start with depending on how many progressive starting chest items you have. Spawn in your starting chest at the start of each run using "spawn chest x normal" replacing x with the kind of chest you should receive.

| Progressive starting chest amount  | Chest type |
| ------------- | ------------- |
| 1-2 | brown  |
| 3-4  | blue  |
| 5-6 | green |
| 7-8 | red |
| 9-10 | black |
| 11+ | rainbow |

- Coupon for x
These coupons can be exchanged for their corresponding item once per coupon. Use them during a run by using the "spawn" command in the console. Keep track of which coupons have been used, as they are valid for one use each.

- Alternate outfit/gun
These unlock the cosmetic alternate outfits/guns of their corresponding gungeoneers.
