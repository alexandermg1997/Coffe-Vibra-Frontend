import base64
import hashlib

# El bloque base64 que el usuario obtuvo con ssh-keyscan
key_wire_format_b64 = "AAAAC3NzaC1lZDI1NTE5AAAAIIq469TOEGo4ODaWjlH4Iyh7V1Xe/URUy5hCJ8Pzi23g"
key_bytes = base64.b64decode(key_wire_format_b64)

# Calculamos el SHA256 (formato estándar de OpenSSH)
sha256_hash = hashlib.sha256(key_bytes).digest()
# OpenSSH quita los '=' al final del base64
fingerprint = base64.b64encode(sha256_hash).decode('utf-8').rstrip('=')

print(f"SHA256:{fingerprint}")
