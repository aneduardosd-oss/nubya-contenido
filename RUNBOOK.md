# NuByA · Sistema de publicación de carruseles

Repo **público**: Instagram descarga las slides desde `raw.githubusercontent.com`. No subas aquí nada privado.

## Estructura
- `sistema/calendario.json`: las 10 piezas con fecha y hora (CDMX, UTC−6) y su estado.
- `sistema/specs/pNN.json`: el diseño de cada carrusel (texto por card, doodles, manchas).
- `sistema/specs/pNN.package.json`: copy out, hashtags y alt text.
- `posts/AAAA-MM-DD-pNN/`: las slides JPG (1080×1350) y `package.json` con `image_urls`.
- `assets/`: logo, avatar de Annie y doodles SVG oficiales (brandbook v1.4).

## Cuenta de Instagram
- Conexión Composio `instagram`, usuario **@nutritionbyannie**, `ig_user_id = 28611547095121922`.

## Flujo de cada pieza
1. **El día anterior**, una tarea programada abre sesión, lee `posts/<carpeta>/package.json` y manda al usuario las slides y el copy para aprobar.
2. **El usuario responde en esa sesión**:
   - "aprobado" (o similar): la sesión programa con `send_later` un mensaje para sí misma a la hora de `publish_at_utc`.
   - Pide cambios: editar `sistema/specs/pNN.json` o el `caption` y el `alt_text` del paquete, volver a renderizar (ver abajo), subir con push, reenviar las slides y volver a pedir aprobación.
   - Sin respuesta: **no se publica**. Nunca publiques sin un "sí" explícito.
3. **A la hora programada**, publicar:
   1. Por cada `image_urls[i]`, llamar `INSTAGRAM_POST_IG_USER_MEDIA` con `is_carousel_item=true`, `image_url` y `alt_text[i]`.
   2. `INSTAGRAM_CREATE_CAROUSEL_CONTAINER` con `children` en orden y `caption`.
   3. `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH` con el `creation_id`.
   4. `INSTAGRAM_GET_IG_MEDIA` para obtener el permalink; confirmar `CAROUSEL_ALBUM` con N hijos.
   5. En `package.json` y `sistema/calendario.json`: poner `status: "published"`, `media_id` y `permalink`; hacer commit y push.
   6. Avisar al usuario con el link.
   7. Programar con `send_later` una revisión de comentarios 60 minutos después: leer comentarios y sugerir respuestas en la voz de Annie, sin publicar ninguna sin OK.

## Volver a renderizar
```bash
cd sistema && npm i --silent && pip install playwright --break-system-packages -q
python3 build_specs.py        # si editaste textos en build_specs.py
python3 render.py specs/pNN.json ../posts/<carpeta>/   # genera pNN-...-01.jpg etc.
```
Después revisa visualmente cada JPG: nada tapado, sin palabras sueltas en una línea, doodles fuera del texto. Luego commit y push.

## Reglas de contenido
Siempre aplican el cerebro NuByA, el Agente 4 de cumplimiento y el brandbook v1.4:
- Tú, nunca usted.
- Sin cifras de peso ni promesas.
- Sin "garantizado", "cura", "milagroso", "el mejor".
- Sin fotos de cuerpos.
- **Nunca presentar un caso inventado como paciente real.** Las piezas 4, 7 y 8 están escritas en segunda persona, como situaciones con las que la gente se identifica.


## Reels
- Carpeta `posts/AAAA-MM-DD-rNN/` con el MP4 (1080×1920, 30 fps, H.264 + AAC), la portada JPG y `package.json` (`video_url`, `cover_url`, `caption`).
- Publicar: `INSTAGRAM_POST_IG_USER_MEDIA` con `media_type: REELS`, `video_url`, `cover_url`, `caption`, `share_to_feed: true` → `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH` con `max_wait_seconds: 300` (el video tarda en procesar) → `INSTAGRAM_GET_IG_MEDIA` para el permalink. Luego status/media_id/permalink en el paquete y el calendario, commit, push y aviso al usuario.
- La música va mezclada dentro del MP4; la API no permite agregar audio de la biblioteca de Instagram.
