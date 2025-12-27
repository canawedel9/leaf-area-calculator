# 1. Lists and List Comprehension
numbers = [1, 2, 3, 4, 5]
squared = [n**2 for n in numbers]
print(f"Squared numbers: {squared}")

# 2. Dictionaries
plant_data = {
    # Plant identity
    "species": "Solanum lycopersicum",
    "variety": "Cherry Tomato",
    "plant_id": "T-CT-1",
    "location": "Greenhouse A",
    
    # Morphology
    "leaf_count": 12,
    "height_cm": 45.5,
    "stem_diameter_mm": 5.2,
    "flower_count": 3,

    # Health
    "health": "healthy",    
    "pest_detected": False,
    "disease": None,

    # Environmental conditions
    "soil_type": "loamy",
    "soil_ph" : 6.5,
    "irrigation_level": "moderate",
    "light_exposure": "full sun",

    # Timeline
    "age_days": 30,
    "date_planted" : "2025-11-27",
    "last_measure" : "2025-12-27",

    # Notes
    "notes": "Growing well, good color"
}
print(f"Species: {plant_data['species']}")
print(f"Plant ID: {plant_data['plant_id']}")
print(f"Location: {plant_data['location']}")
print(f"Health Status: {plant_data['health']}")
print(f"Leaf Count: {plant_data['leaf_count']}")
print(f"Height: {plant_data['height_cm']} cm")
print(f"Age: {plant_data['age_days']} days")


# 3. Functions
def calculate_area(length, width):
    """Calculate area of rectangle"""
    return length * width

#def calculate_leaf_area(length, width, shape_factor):
    '''
    Calculate leaf area from length and width per leaf shape type.
    Parameters:
    Length (float): l of leaf in cm
    Width (float): w of leaf in cm
    shape_factor (float): Correction factor (default 0.6)
                         - 0.5-0.6 for narrow leaves (bamboo, grass)
                         - 0.7 for typical broadleaf
                         - 0.75-0.8 for round leaves

    Returns:
    float: estimated leaf area in cm^2
    '''
    if length <= 0 or width <= 0:
        return 0
    area = length * width * shape_factor
    return area
# print("\n" + "="*40)
# print("Narrow leaf (grass):", calculate_leaf_area(15, 1.5, 0.6))
# print("Broadleaf (typical: tomato):", calculate_leaf_area(10, 5, 0.7))
# print("Round leaf (e.g., lotus):", calculate_leaf_area(8, 8, 0.8))

def calculate_leaf_area(length, width, shape_factor=0.7):
    """Clculate single leaf area"""
    return length * width * shape_factor

def calculate_total_leaf_area(leaf_measurements):
    """
    Calculate total area for multiple leaves
    Parameters:
    leaf_measurements (list): List of Tuples [(length, with, )]
    
    Returns:
    dict: Dictionary with individual and total areas"""
    
    areas = []
    
    print("\n" + "="*40)
    print("Leaf Area Measurements:")

    for i, (length, width) in enumerate(leaf_measurements, 1):
        area = calculate_leaf_area(length, width)
        areas.append(area)
        print(f"leaf {i}: {length} x {width} cm = {area:.2f} cm^2")
    
    total = sum(areas)
    average = total / len(areas) if areas else 0

    return {
        "individual_areas": areas,
        "total_area": total,
        "average_area": average,
        "leaf_count": len(areas)
    }

#test
leaves = {
    (10, 5),    #leaf1
    (8, 4),     #leaf2
    (12, 6),    #leaf3
    (9, 4.5)    #leaf4
}

result = calculate_total_leaf_area(leaves)

print("\n" + "-"*40)
print(f"Total leaves measured: {result['leaf_count']}")
print(f"Total leaf area: {result['total_area']:.2f} cm^2")
print(f"Average leaf area: {result['average_area']:.2f} cm^2")
print("="*40)


# 4. File handling
with open("test.txt", "w") as f:
    f.write("This is a test file")

with open("test.txt", "r") as f:
    content = f.read()
    print(content)

# 5. Classes for later
class Leaf:
    def __init__(self, species, length):
        self.species = species
        self.length = length
    def describe(self):
        return f"{self.species} leaf with length {self.length}cm"

my_leaf = Leaf("Oak", 8.5)
print(my_leaf.describe())
print("="*40)