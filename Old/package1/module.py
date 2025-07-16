# module.py
# Публичная ф-ция - можно обращаться в любом месте программы
def greet(name) :
    return (f'Привет,{name}!')

# Скрытая ф-ция, для внутр.пользования (
def _hidden_function() :
    return ('ДВП')