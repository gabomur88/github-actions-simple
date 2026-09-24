import json
import os
import subprocess
import sys
import time
import urllib.request

URL = "http://127.0.0.1:8000/health"


def main():

    # Comprobar que existe nuestra variable secreta
    if not os.getenv("DEMO_SECRET"):
        raise RuntimeError("DEMO_SECRET no esta definido")

    print("Iniciando aplicacion...")

    # Arrancar el artefacto en segundo plano
    process = subprocess.Popen(
        [sys.executable, "dist/simpleapp.pyz"],
        env=os.environ.copy()
    )

    try:

        print("Esperando que la aplicacion responda...")

        app_ready = False

        # Intentamos durante un maximo de 30 segundos
        for intento in range(1, 31):

            try:

                print(f"Intento {intento}/30")

                with urllib.request.urlopen(URL, timeout=2) as response:

                    data = json.loads(
                        response.read().decode()
                    )

                    if data.get("status") == "UP":

                        print("Aplicacion saludable")
                        print(data)

                        app_ready = True
                        break

            except Exception:
                time.sleep(1)

        if not app_ready:
            raise RuntimeError(
                "La aplicacion nunca llego a estar saludable"
            )

    finally:

        print("Deteniendo aplicacion...")

        process.terminate()

        try:
            process.wait(timeout=5)

        except subprocess.TimeoutExpired:
            print("Forzando cierre...")
            process.kill()

        print("Aplicacion detenida correctamente")


if __name__ == "__main__":
    main()
