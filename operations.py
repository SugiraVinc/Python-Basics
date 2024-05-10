def calculate_storage(filesize):
    block_size = 4096
    # Use integer division to find out how many blocks are needed
    # Ceiling division is used to ensure that even a file of size 1 byte uses one block
    blocks_needed = filesize // block_size + (filesize % block_size != 0)
    # Multiply the number of blocks by the block size to get the total storage needed
    storage_needed = blocks_needed * block_size
    return storage_needed

# Example usage:
print(calculate_storage(1))   # Output: 4096
print(calculate_storage(4097)) # Output: 8192