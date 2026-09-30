def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def get_user_name(user):
    if user is None or not isinstance(user, dict):
        raise TypeError("user must be a dictionary")
    if "name" not in user:
        raise KeyError("user dictionary must contain a 'name' key")
    name = user["name"]
    if not isinstance(name, str):
        raise TypeError("user['name'] must be a string")
    return name.upper()