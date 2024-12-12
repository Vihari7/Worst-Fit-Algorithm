class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.free = size
        self.allocated_to = []

class WorstFitAllocator:
    def __init__(self, blocks):
        self.blocks = blocks
        self.process_allocation = {}

class WorstFitAllocator:
    def __init__(self, blocks):
        self.blocks = blocks
        self.process_allocation = {}  # Dictionary to track process allocation

    def allocate(self, process_name, size):
        print(f"\nAllocating {process_name} ({size} KB):")
        largest_block = None
        largest_index = -1
        for i, block in enumerate(self.blocks):
            if block.free >= size and (largest_block is None or block.free > largest_block.free):
                largest_block = block
                largest_index = i

        if largest_block:
            largest_block.allocated_to.append(process_name)
            largest_block.free -= size
            self.process_allocation[process_name] = (largest_index + 1, size)
            print(f"Process {process_name} allocated to Block {largest_index + 1}.")
            print(f"Updated Block {largest_index + 1}: {largest_block.free} KB free.")
        else:
            print(f"Process {process_name} could not be allocated. No suitable block found.")

    def deallocate(self, process_name):
        print(f"\nDeallocating {process_name}:")
        if process_name in self.process_allocation:
            block_index, size = self.process_allocation.pop(process_name)
            block = self.blocks[block_index - 1]
            block.allocated_to.remove(process_name)
            block.free += size
            print(f"Process {process_name} deallocated from Block {block_index}.")
        else:
            print(f"Process {process_name} not found in any block.")

    def display_memory_state(self):
        print("\nMemory State:")
        for i, block in enumerate(self.blocks):
            if block.allocated_to:
                status = f"Allocated to {', '.join(block.allocated_to)}"
            else:
                status = "Free"
            print(f"Block {i + 1}: {block.free} KB free ({status}).")
