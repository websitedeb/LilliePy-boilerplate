from cryptography.fernet import Fernet as ft


def use_crypt():
  key = ft.generate_key()

  def generate(val):
    fernet = ft(key)
    encrypted = fernet.encrypt(val.encode())
    return encrypted

  def compare_value(encrypted_val, original_val):
    fernet = ft(key)
    decrypted_val = fernet.decrypt(encrypted_val).decode()
    return decrypted_val == original_val

  def decode(encrypted_val):
    fernet = ft(key)
    decrypted_val = fernet.decrypt(encrypted_val).decode()
    return decrypted_val

  return key, generate, decode, compare_value
