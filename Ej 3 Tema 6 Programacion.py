def check_input_for_es_primo (n):
    if not ( type (n) == int or type (n) == float ):
        raise ValueError (" Wrong Type ")
    elif (int(n) != n) or (n <= 0):
        raise ValueError (" Wrong Value ")