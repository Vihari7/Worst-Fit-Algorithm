# Define a class to represent a memory block
class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.free = size
        self.allocated_to = []

# Define a class for the Worst Fit Allocator
class WorstFitAllocator:
    def __init__(self, blocks):
        self.blocks = blocks
        self.process_allocation = {}  # Dictionary to track process allocation
    
    # Method to allocate memory to a process
    def allocate(self, process_name, size):
        print(f"\nAllocating {process_name} ({size} KB):")
        largest_block = None  # Variable to track the largest suitable block
        largest_index = -1    # Index of the largest suitable block

        # Find the largest block that can fit the process
        for i, block in enumerate(self.blocks):
            if block.free >= size and (largest_block is None or block.free > largest_block.free):
                largest_block = block
                largest_index = i

        # If a suitable block is found
        if largest_block:
            largest_block.allocated_to.append(process_name)
            largest_block.free -= size
            self.process_allocation[process_name] = (largest_index + 1, size)
            print(f"Process {process_name} allocated to Block {largest_index + 1}.")
            print(f"Updated Block {largest_index + 1}: {largest_block.free} KB free.")
        else:
            print(f"Process {process_name} could not be allocated. No suitable block found.")

    # Method to deallocate memory from a process
    def deallocate(self, process_name):
        print(f"\nDeallocating {process_name}:")
        if process_name in self.process_allocation: # Check if the process is allocated
            block_index, size = self.process_allocation.pop(process_name)
            block = self.blocks[block_index - 1]
            block.allocated_to.remove(process_name)
            block.free += size
            print(f"Process {process_name} deallocated from Block {block_index}.")
        else:
            print(f"Process {process_name} not found in any block.")
    
    # Method to display the current memory state
    def display_memory_state(self):
        print("\nMemory State:")
        for i, block in enumerate(self.blocks):
            if block.allocated_to:
                status = f"Allocated to {', '.join(block.allocated_to)}"
            else:
                status = "Free"
            print(f"Block {i + 1}: {block.free} KB free ({status}).")

# Initialize memory blocks with predefined sizes
block_sizes = [100, 500, 200, 300, 600]
blocks = [MemoryBlock(size) for size in block_sizes]

# Create an instance of the Worst Fit Allocator
allocator = WorstFitAllocator(blocks)

# Display the initial state of memory
print("Initial Memory State:")
allocator.display_memory_state()

# Main loop for user interaction
while True:
    print("\nOptions:")
    print("1. Allocate")
    print("2. Deallocate")
    print("3. Exit")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1: # Allocate memory
        process_name = input("Enter the name of the process to allocate: ")
        process_size = int(input("Enter the size of the process in KB: "))
        allocator.allocate(process_name, process_size)
        allocator.display_memory_state()
    elif choice == 2: # Deallocate memory
        process_name = input("Enter the name of the process to deallocate: ")
        allocator.deallocate(process_name)
        allocator.display_memory_state()
    elif choice == 3: # Exit the program
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
