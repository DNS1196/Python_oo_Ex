"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        """initiate the serial generator
        Args:
            start (int, optional): Defaults to 100.
        """
        self.start = self.next = start

    def __repr__(self):
        """Shows representation"""

        return f"<SerialGenerator start = {self.start} next = {self.next}>"
        

    def generate(self): 
        """Generates the serial numbers incrementing 1 by 1"""
        self.next += 1
        return self.next -1

    def reset(self):
        """Reset the serial number back to the start number"""

        self.next = self.start