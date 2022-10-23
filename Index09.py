def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    l = s.lower()
    u = s.upper()
    if l!=u:
        a = -1
    else:
        a = int(s)
    return a 