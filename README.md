This is for a Mini project that simulates how the Worst Fit  algorithm works in dynamic memory allocation. 

# 🌟 **Worst Fit Memory Allocation Algorithm**

## 📘 **Introduction**
This project implements the **Worst Fit algorithm** for dynamic memory allocation. The algorithm assigns memory blocks to processes by choosing the largest available block, aiming to reduce fragmentation and maximize the efficiency of memory usage. The implementation is in Python, offering a user-friendly interface for memory allocation and deallocation.

---

## 🛠️ **Features**
-  Accepts user input for process sizes and block sizes.
-  Allocates memory using the Worst Fit strategy.
-  Deallocates memory for reusability.
-  Displays the current state of memory after each operation.
-  Handles errors when no suitable block is found.

---

## ⚠️ **Limitations**
-  Assumes memory block sizes remain fixed.
-  Does not support preemptive allocation.
-  All blocks are independent; no merging of adjacent free blocks is implemented.

---

## 📜 **Assumptions**
-  Memory blocks are fixed in size and do not overlap.
-  Processes request memory in kilobytes (KB).
-  Each process has a unique identifier.
-  Memory allocation is non-preemptive; allocated memory remains in use until explicitly deallocated.

---

## 🧑‍💻 **How It Works**
1. **Initialization**: Memory blocks are defined with fixed sizes.
2. **User Interaction**: Provides a menu for allocation, deallocation, and exiting.
3. **Allocation**:
   -  Finds the largest memory block that can fit the requested process size.
   -  Allocates the process to the block and updates its free space.
4. **Deallocation**:
   -  Frees the memory used by a process and updates the block's free space.
5. **Display**:
   -  Shows the current memory state, including free and allocated blocks.

---

## 🖥️ **Requirements**
- **Programming Language**: Python 3.11 or later.
- **Development Environment**: Any Python IDE or terminal.

---

## 🚀 **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/Vihari7/Worst-Fit-Algorithm.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Worst-Fit-Algorithm
   ```
3. Run the application:
   ```bash
   python worst_Fit.py  
   ```

---

## 🎮 **Usage**
1. **Allocate Memory**:
   - Select option 1 from the menu.
   - Enter the process name and size in KB.
   - The system will allocate the process to the largest suitable block.
2. **Deallocate Memory**:
   - Select option 2 from the menu.
   - Enter the process name to deallocate.
   - The memory block will be updated with the newly freed space.
3. **Exit**:
   - Select option 3 to terminate the program.

### 💡 Example Workflow
1. Initial memory blocks: [100, 500, 200, 300, 600 KB].
2. Allocate ProcessA (300 KB): Allocates to Block 5 (600 KB).
3. Allocate ProcessB (200 KB): Allocates to Block 2 (500 KB).
4. Deallocate ProcessA: Frees Block 5.

---

## 🔮 **Future Enhancements**
- Add a graphical user interface (GUI) for better interaction.
- Support merging of adjacent free memory blocks.
- Compare performance with other allocation strategies like Best Fit and First Fit.
- Implement real-time memory allocation and deallocation.

---
