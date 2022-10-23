def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    u = s.upper()
    l = s.lower()
    i = 0
    if u[0]==l[0]:
        i+=1
    if u[1]==l[1]:
        i+=1
    if u[2]==l[2]:
        i+=1
    if u[3]==l[3]:
        i+=1
    if u[4]==l[4]:
        i+=1
    return i 
