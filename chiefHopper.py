import math

def chiefHopper(arr):
    # Start with 0 energy at the end
    energy = 0
    
    # Iterate through the heights in reverse
    for h in reversed(arr):
        # We need to find the minimum E such that 2E - h >= current_energy
        # E >= (current_energy + h) / 2
        # We use (energy + h + 1) // 2 to perform integer ceiling division
        energy = (energy + h + 1) // 2
        
    return energy

# Example:
# heights = [3, 4, 3, 2, 4]
# Step 1 (h=4): (0+4+1)//2 = 2
# Step 2 (h=2): (2+2+1)//2 = 2
# Step 3 (h=3): (2+3+1)//2 = 3
# Step 4 (h=4): (3+4+1)//2 = 4
# Step 5 (h=3): (4+3+1)//2 = 4
# Result: 4
