def get_FUV_email_class_code(email):
  if not isinstance(email, str):
    raise ValueError('The provided input is not a string.')
  elif '@student.fulbright.edu.vn' in email:
    return 1
  elif not email.endswith('@fulbright.edu.vn') or email.count('@') != 1:
    return 4
  elif '@fulbright.edu.vn' in email and email.split('@')[0].count('.') == 1:
    return 2
  else:
    return 3
  
def get_vnd(money):
  exchange_rates = {
    'CAD': 18063.0,
    'USD': 24372.0,
    'VND': 1.0
  }
  money = money.strip().upper()
  amount = ''.join([c for c in money if c.isdigit() or c == '.'])
  currency = ''.join([c for c in money if c.isalpha()])
  if amount + currency != money or currency not in exchange_rates:
    return 0
  try:
    amount = float(amount)
  except ValueError:
    return 0
  if currency in exchange_rates:
    return round(amount * exchange_rates[currency], 1)
  else:
    return 0
  