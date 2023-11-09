# Demonstration of buffer overflow
def buffer_overflow():
    # Creating a list with 10 elements initialized to 0
    buffer = [0] * 10
    print("Initial buffer:", buffer)
    # Attempting buffer overflow with index 10
    buffer[10] = 1
    print("Buffer after attempt to overflow:", buffer)


#  Prevention for buffer overflow
def python_prevention():
    # Creating a list with 10 elements initialized to 0
    buffer = [0] * 10
    try:
        # Attemtp to overflow the buffer
        buffer[10] = 1
    except IndexError:
        # Handling of the IndexError if overflow is detected
        print("Buffer overflow detected and prevented!")

    # Here is the main block function to execute


if __name__ == "__main__":
    print("Demonstrating Buffer Overflow:")
    # This is where I call the function to demonstrate the buffer overflow
    buffer_overflow()
    print("\nDemonstrating Python's Prevention Mechanism:")
    # This is where I call the function to demonstrate Python's prevention mechanism
    python_prevention()
