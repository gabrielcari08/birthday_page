# spec.md - Birthday Page para mi novia

## Objetivo
Página web interactiva móvil para regalo de cumpleaños.

## Diseño y Estética
- Colores: Principlamente Rosado y tonos rojizos.
- Temática romántica con animaciones de corazones al hacer clic.

## Flujo de Usuario (Pantallas)
1. **Pantalla de Bienvenida:** Botón gigante de "Ingresar".
2. **Pantalla del Carrusel:** - Botones "Anterior" y "Siguiente".
   - Cada carta muestra: Foto + Texto tierno.

## Requerimientos Técnicos (Backend Django)
- Una tabla `Card` en base de datos para que yo pueda cargar las cartas desde el panel de Admin de Django sin tocar código HTML.

## Modelo de datos

El modelo de datos no sera tan complejo

**User:** Username, Password (Autenticacion nativa de Django)
**Card** User_id (Quien la crea), Text(contenido del carta), Image, Created_at(fecha en la que fue creada)

## URLs requeridas.

- '/' -> Pantalla de bienvenida / Login
- '/home/' -> Lugar donde se mostraran todas las cartas (necesita login previo para verse)
- '/admin/' -> El panel de control nativo de Django para cargar las fotos y cartas.