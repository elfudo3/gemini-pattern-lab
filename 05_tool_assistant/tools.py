# The SDK reads the docstrings, along with type hints, to build the description
# it sends the model

def get_weather(city:str) -> str:
    """Get the current weather for a city

    Args:
        city: Name of city, e.g. "Dublin"
    """
    print(f">>> get weather actually ran with city={city}")
    fake_data = {"dublin": "12C, raining", "madrid": "28C, sunny"}
    result = fake_data.get(city.lower(), "No data for that city")
    print(f">>> get_weather({city!r}) -> {result!r}")
    return result

def calculate(expression: str) -> str:
    """Evaluate a simple arithmetic expression.
    
    Args:
        expression: A maths expression, e.g. "23 * 47
    """
    print(f">>> get answer for expression=({expression})")
    try:
        # eval() executes the input as Python code, it's not restricted to arithmetic
        # it's fine for this sandbox but never put it in something real
        return str(eval(expression))
    except Exception as e:
        return f"Could not calculate: {e}"
    


