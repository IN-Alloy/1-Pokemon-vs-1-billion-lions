import random

def simulate_Smeargle_battle():
    recycle_pp = 10
    recover_pp = 5
    surf_pp = 15
    has_leppa_berry = True
    Smeargle_hp = 248
    lions_defeated = 0
    lion_damage = 2

    while Smeargle_hp > 0 and lions_defeated < 100000000:  # Stop the simulation at 1 billion lions or if Smeargle faints
        while True:
            # Determine the move to be used randomly
            move_to_use = random.choice(["Recycle", "Recover", "Surf"])

            # Check if the selected move can be used (PP > 0)
            if (move_to_use == "Recycle" and recycle_pp > 0) or (move_to_use == "Recover" and recover_pp > 0) or (move_to_use == "Surf" and surf_pp > 0):
                break

        if move_to_use == "Recycle":
            # Recycle restores the Leppa Berry
            has_leppa_berry = True
            recycle_pp -= 1
            Smeargle_hp -= lion_damage #lions attack
        elif move_to_use == "Recover":
            # If Recover is used, consume 1 PP and heal 200 HP
            recover_pp -= 1
            Smeargle_hp +=  124
            if Smeargle_hp > 248: Smeargle_hp = 248
            Smeargle_hp -= lion_damage #lions attack
        elif move_to_use == "Surf":
            # If Surf is used, consume 1 PP and defeat 1 lion
            surf_pp -= 1
            lions_defeated += 1
            
        # If any move (Recycle, Recover, or Surf) hits 0 PP, use Leppa Berry if available
        if recycle_pp == 0:
            # Use Leppa Berry on Recycle if available
            if has_leppa_berry:
                recycle_pp = 10
                has_leppa_berry = False
        if surf_pp == 0:
            # Use Leppa Berry on Surf if available
            if has_leppa_berry:
                surf_pp = 15
                has_leppa_berry = False
        if recover_pp == 0:
            # Use Leppa Berry on Recover if available
            if has_leppa_berry:
                recover_pp = 5
                has_leppa_berry = False
                        
        # Check if any move has run out of PP
        if recycle_pp == 0 and recover_pp == 0 and surf_pp == 0:
            break

        # Print an update every 1000 turns
        if lions_defeated % 10000 == 0:
            print(f"Turn {lions_defeated}: Smeargle is still battling...")

    return lions_defeated

# Run the simulation
simulation_result = simulate_Smeargle_battle()

# Print the final result
print(f"Simulation Result: Smeargle defeated {simulation_result} lions.")
