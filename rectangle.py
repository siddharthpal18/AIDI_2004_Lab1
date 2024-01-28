def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    - length (float): Length of the rectangle.
    - width (float): Width of the rectangle.

    Returns:
    - float: Area of the rectangle.
    """
    area = length * width
    return area

def main():
    # Get user input for length and width
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the area
    area = calculate_rectangle_area(length, width)

    # Display the result
    print(f"The area of the rectangle with length {length} and width {width} is: {area}")

if __name__ == "__main__":
    main()
