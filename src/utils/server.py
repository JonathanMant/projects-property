from http.server import HTTPServer
import os

from src.apps.property.domain.views import MiManejador

env_path = '.env'

with open(env_path) as f:
    for line in f:
        key, value = line.strip().split('=')
        os.environ[key] = value

puerto = 8080
servidor = HTTPServer(('localhost', puerto), MiManejador)

print(f"Servidor activo en http://localhost:{puerto}")

servidor.serve_forever()
