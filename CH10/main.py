class Box:
    def __init__(self, label: str, length: float, width: float, height: float):
        self.label = label
        self.length = length
        self.width = width
        self.height = height

    def volume(self) -> float:
        """Calculate the volume of the box."""
        # Multiply length, width, and height
        return self.length * self.width * self.height


def pack_truck(boxes: list, truck_volume: float) -> list:
    """Pack the truck using a greedy strategy based on box volumes."""
    # Sort boxes in descending order of volume
    boxes_sorted = sorted(boxes, key=lambda b: b.volume(), reverse=True)

    packed_boxes = []
    used_volume = 0

    # Iterate through sorted boxes
    for box in boxes_sorted:
        # If the box fits, add it
        if used_volume + box.volume() <= truck_volume:
            packed_boxes.append(box)
            used_volume += box.volume()

    return packed_boxes


if __name__ == "__main__":
    print("Welcome to the Truck Cargo Calculator")
    print("This program helps you calculate how to pack your cargo efficiently using a greedy algorithm.\n")

    # Input and calculate truck volume
    truck_length = float(input("Enter truck length: "))
    truck_width = float(input("Enter truck width: "))
    truck_height = float(input("Enter truck height: "))

    truck_volume = truck_length * truck_width * truck_height
    print(f"Truck volume: {truck_volume}\n")

    boxes = []  # List to store box objects

    # Input boxes
    while True:
        label = input("Enter box label (or type 'done' to finish): ")
        if label.lower() == "done":
            break

        length = float(input("Enter box length: "))
        width = float(input("Enter box width: "))
        height = float(input("Enter box height: "))

        boxes.append(Box(label, length, width, height))
        print()

    # Pack the truck and display results
    packed_boxes = pack_truck(boxes, truck_volume)

    total_used_volume = sum(box.volume() for box in packed_boxes)

    print("\nPacked Boxes:")
    for box in packed_boxes:
        print(f"{box.label} (Volume: {box.volume()})")

    print(f"\nTotal used volume: {total_used_volume}")
    print(f"Unused volume: {truck_volume - total_used_volume}")

    print("\nThank you for using the Truck Cargo Calculator.")
