# PokeBot

PokeBot es un bot de Discord que permite buscar y mostrar imágenes de Pokémon usando la PokéAPI.

## Características

- Comando `$poke <nombre_pokemon>`: Muestra la imagen del Pokémon solicitado.
- Comando `$clear`: Limpia el chat (requiere permisos de moderador).
- Mensajes de error amigables si el Pokémon no existe o falta el argumento.

## Requisitos

- Python 3.8+
- Paquetes: `discord.py`, `requests`, `python-dotenv`

## Instalación

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias:
   ```pwsh
   pip install discord.py requests python-dotenv
   ```
3. Crea un archivo `.env` y agrega tu token de Discord:
   ```env
   DSTOKEN=tu_token_aqui
   ```
4. Ejecuta el bot:
   ```pwsh
   python main.py
   ```

## Uso

- En Discord, escribe:
  - `$poke "nombre del pokemon"` para ver la imagen de Pikachu.
  - `$clear` para limpiar el chat (solo moderadores).

## Créditos

- Imágenes y datos de Pokémon por [PokéAPI](https://pokeapi.co/).
- Bot desarrollado con [discord.py](https://discordpy.readthedocs.io/).
