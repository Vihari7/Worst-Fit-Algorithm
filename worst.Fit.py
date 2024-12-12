class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.free = size
        self.allocated_to = []

class WorstFitAllocator:
    def __init__(self, blocks):
        self.blocks = blocks
        self.process_allocation = {}

