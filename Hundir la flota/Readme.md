# Hundir la flota

#### Aquí voy a realizar un juego de hundir la flota

---

## `Diagrama de flujo` 
### - Tablero

```mermaid
flowchart TD
    A(["Inicio<br>recorrerTablero()"]) --> n1["Tablero = lista de listas (5x5)"]
    n1 --> n2["i = 0"]
    n2 --> n3["Recorrer lista"]
    n3 --> n4["i &lt; 6"]
    n4 -- No --> n5["mostrar i"]
    n4 -- Si --> n2
    n1@{ shape: rect}
    n2@{ shape: rect}
    n3@{ shape: rect}
    n4@{ shape: diam}
    n5@{ shape: lean-r}
     A:::Sky
    classDef Aqua stroke-width:1px, stroke-dasharray:none, stroke:#46EDC8, fill:#DEFFF8, color:#378E7A
    classDef Ash stroke-width:1px, stroke-dasharray:none, stroke:#999999, fill:#EEEEEE, color:#000000
    classDef Sky stroke-width:1px, stroke-dasharray:none, stroke:#374D7C, fill:#E2EBFF, color:#374D7C
```