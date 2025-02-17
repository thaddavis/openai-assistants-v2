def add(a: int, b: int) -> str:
    try:
        print(f"Calling the 'add' tool...")
        print(f"Received params: {a} {b}")
        sum = a + b
        return str(sum)
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred while processing your request."