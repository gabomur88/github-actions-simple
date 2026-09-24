from pathlib import Path
import zipapp

Path("dist").mkdir(exist_ok=True)

zipapp.create_archive(
    source="src",
    target="dist/simpleapp.pyz",
    main="app:main"
)

print("Artefacto creado:")
print("dist/simpleapp.pyz")
