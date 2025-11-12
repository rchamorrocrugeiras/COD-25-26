# Hundir la flota

#### Aquí voy a realizar un juego de hundir la flota

---

## `Diagrama de flujo` 
### - Tablero

```mermaid
flowchart TD
    A(["Inicio"]) --> B["contador_total = 0"]
    B --> C["Para cada fila en tablero"]
    C --> D["llamar recorrerFila fila"]
    D --> E["sumar resultado al contador_total"]
    E --> F{"¿Quedan filas?"}
    F -- Sí --> C
    F -- No --> G["Devolver contador_total"]
    G --> H(["Fin"])
     A:::Sky
     H:::Sky
    classDef Sky stroke-width:1px, stroke-dasharray:none, stroke:#374D7C, fill:#E2EBFF, color:#374D7C
```