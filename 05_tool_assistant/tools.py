# The SDK reads the docstrings, along with type hints, to build the description
# it sends the model

def get_weather(city:str) -> str:
    """Get the current weather for a city

    Args:
        city: Name of city, e.g. "Dublin"
    """
    fake_data = {"dublin": "12C, raining", "madrid": "28C, sunny"}
    return fake_data(city.lower(), "No data for that city")

def calculate(expression: str) -> str:
    """Evaluate a simple arithmetic expression.
    
    Args:
        expression: A maths expression, e.g. "23 * 47
    """
    try:
        # eval() executes the input as Python code, it's not restricted to arithmetic
        # it's fine for this sandbox but never put it in something real
        return str(eval(expression))
    except Exception as e:
        return f"Could not calculate: {e}"
    


