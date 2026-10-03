class InvalidInputError(Exception):
    """Custom exception raised when user input validation fails."""

def parse_positive_float(value_str: str, field_name: str) -> float:
    """
    Raises InvalidInputError if invalid.
    """
    if not value_str or not value_str.strip():
        raise InvalidInputError(f"{field_name} cannot be empty.")

    try:
        val = float(value_str.strip())
    except ValueError:
        raise InvalidInputError(
            f"{field_name} must be a valid numerical value.")

    if val <= 0:
        raise InvalidInputError(f"{field_name} must be greater than zero.")

    return val
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculates BMI given weight in kilograms and height in meters.
    Formula: weight / (height^2)
    """
    if height_m <= 0:
        raise InvalidInputError("Height must be greater than 0.")
    if weight_kg <= 0:
        raise InvalidInputError("Weight must be greater than 0.")
    return round(weight_kg / (height_m**2), 2)

def classify_bmi(bmi: float) -> str:
    """Classifies a numerical BMI value into WHO standard categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal Weight"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

def category_color(category: str) -> float :
    """Returns the hex color code corresponding to each BMI category."""
    colors = {
        "Underweight": "#3498db",  # Blue
        "Normal Weight": "#2ecc71",  # Green
        "Overweight": "#e67e22",  # Orange
        "Obese": "#e74c3c",}#RED

    return colors.get(category, "#95a5a6") #Default gray}