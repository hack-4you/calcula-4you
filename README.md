# calcula-4you

calcula-4you permite calcular la nota necesaria en el examen final para aprobar. Incluye opciones para ejercicios, cátedra y taller, si aplica. Según las notas ingresadas y los pesos de cada componente, calcula y muestra la nota mínima requerida para alcanzar una nota deseada.

## Cómo usar en Debian / Linux

### 1) Verifica que Python esté instalado

```bash
python3 --version
```

Si no aparece la versión, instala Python:

```bash
sudo apt update
sudo apt install python3 python3-venv -y
```

### 2) Accede al repositorio

```bash
cd /ruta/donde/guardaste/calcula-4you
```

### 3) Ejecuta la calculadora

```bash
python3 calculadora_nota.py
```

### 4) Ingresa los datos

Ejemplo de interacción:

```text
¿El ramo incluye taller de acompañamiento? (s/n): s
Ingrese la nota del Ejercicio 1 (0-70): 55
Ingrese la nota del Ejercicio 2 (0-70): 60
Ingrese la nota de Cátedra (0-70): 50
Ingrese la nota del Taller (0-70): 65
```

El programa mostrará la nota mínima necesaria en el examen final para aprobar.

## Seguridad y validación

- Consulta la política de seguridad en [SECURITY.md](SECURITY.md)
- Consulta la guía de validación en [VALIDACION.md](VALIDACION.md)
- El repositorio incluye una validación automática con GitHub Actions.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE).
