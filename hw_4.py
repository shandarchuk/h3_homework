def validate_password(password):
    """
    Функция принимает пароль строкой и выполняет валидацию с помощью трёх
    вспомогательных функций:
    1. Содержит только a−z, A−Z, 0−9
    2. Содержит четное количество букв
    3. Содержит нечетное количество цифр
    Основная функция возвращает True, если пароль валидный.
    Если пароль не валидный, возвращает лист стрингов, в которых перечислены
    причины неуспешной проверки. Например: ["содержит запрещенные символы"]
    """
    str_list = list()
    
    if not _validate_symbols(password):
        str_list.append("содержит запрещенные символы")
        
    if not _validate_letters_even(password):
        str_list.append("содержит нечетное количество букв")
        
    if not _validate_numbers_odd(password):
        str_list.append("содержит четное количество цифр")    
    
    if len(str_list):
        return str_list
    return True

def _validate_symbols(input_str):
  """
  Проверяет строку на наличие запрещенных символов
  Подсказка: у строк есть метод, проверяющий наличие только був и цифр
  Возвращает True\False
  """
  for i in input_str:
      if not i.isalnum():
        return False
  return True

def _validate_letters_even(input_str):
  """
  Проверяет строку на четное количество букв
  Возвращает True\False
  """
  str_list = [x for x in input_str if x.isalpha()]
  
  if len(str_list) % 2:
    return True
  else:
    return False

def _validate_numbers_odd(input_str):
  """
  Проверяет строку на нечетное количество цифр
  Возвращает True\False
  """
  int_list = [x for x in input_str if x.isdigit()]
  
  if len(int_list ) % 2:
    return True
  else:
    return False