def first(param: str) -> str:
    print(f'numero 1 : {param}')
    f_value = second(param)
    return f_value

def second(param: str) -> str:
    print(f"Segunda recebeu: {param}")
    s_value = third(param)
    return s_value

def third(param : str) -> str:
    print(f"Terceirta recebeu {param}")
    t_value = "Fim!!"
    return t_value

if __name__ == "__main__":
    result = first("Trybe")
    print(f"Resultado final: {result}")

