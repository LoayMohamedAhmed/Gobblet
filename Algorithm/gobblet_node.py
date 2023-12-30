class GobbletNode:
    def __init__(self, length: int, color: str):  
        # Assuming color should be a single character
        if len(color) != 1:
            raise ValueError("Color should be a single character")

        self.length = length
        self.color = color
        self.next = None