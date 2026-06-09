# Actividad A01 — Customización de GitHub Copilot para Programación de IA

**Módulo:** MP5073 Programación de Inteligencia Artificial  
**Unidad Didáctica:** UD01 — Herramientas de generación de código para IA

---

## Introducción

GitHub Copilot no es solo un asistente de autocompletado: es un sistema de IA configurable que puede adaptarse al contexto de tu proyecto, a tu estilo de código y a tu flujo de trabajo. Esta adaptación se hace mediante **primitivas de customización** — archivos especiales en la carpeta `.github/` de tu repositorio.

En esta actividad vas a construir tu propio conjunto de customizaciones para un repositorio de proyectos de IA, siguiendo el modelo en `solucion/`. Al final comprenderás cuándo usar cada primitiva y por qué.

**Referencia:** La solución completa está en `solucion/`. Úsala como modelo de respuesta, pero desarrolla tu propia versión desde cero.

---

## Tareas

### Tarea 1. Instrucciones globales (Layer 1 — Instructions)

**Objetivo:** Configurar reglas que se apliquen a todo el repositorio sin necesidad de invocarlas explícitamente.

**Enunciado:**

Crea un archivo `.github/copilot-instructions.md` en tu repositorio con:
1. Una descripción del contexto del proyecto (para qué sirve el repositorio).
2. Al menos dos políticas transversales (por ejemplo: idioma de los comentarios, política de seeds para reproducibilidad).
3. Una referencia a otros archivos de instrucciones específicos que crearás en los siguientes pasos.

A continuación, crea instrucciones específicas para al menos **dos tipos de archivo** usando `applyTo`:
- `.github/instructions/python.instructions.md` — normas de estilo para Python (PEP 8, type hints, docstrings).
- `.github/instructions/notebooks.instructions.md` — normas para notebooks (estructura narrativa, limpieza de outputs).

**Pistas:**
- Compara tu `copilot-instructions.md` con el de la solución: ¿qué pone en el archivo global y qué en los archivos con `applyTo`? ¿Por qué?
- ¿Qué pasaría si pusieras todas las reglas en el archivo global?

**Autoavaliación:**
- [ ] `copilot-instructions.md` existe y contiene al menos dos políticas transversales.
- [ ] `python.instructions.md` tiene `applyTo: "**/*.py"` en el frontmatter YAML.
- [ ] `notebooks.instructions.md` tiene `applyTo: "**/*.ipynb"` en el frontmatter YAML.
- [ ] Los tres archivos están en inglés.
- [ ] Abre un archivo `.py` en VS Code y verifica en el chat de Copilot que las reglas de Python se cargaron (aparece la instrucción en el contexto).

---

### Tarea 2. Prompts almacenados (Layer 2 — Prompts)

**Objetivo:** Crear macros de texto reutilizables para tareas frecuentes.

**Enunciado:**

Crea al menos **dos prompt files** en `.github/prompts/`:

1. **`arch-review.prompt.md`** — Un prompt que analice la arquitectura del proyecto (estructura de carpetas, separación de responsabilidades, portabilidad) y produzca un informe con puntos fuertes y debilidades.

2. **`todo-to-plan.prompt.md`** — Un prompt que escanee todos los comentarios `TODO` del proyecto y genere una lista de tareas priorizadas con estimaciones de esfuerzo.

**Pistas:**
- Un prompt es una expansión de texto: no contiene lógica propia ni archivos adjuntos.
- Usa `$input` si quieres que el prompt acepte un argumento del usuario.
- Compara con los prompts de la solución: ¿en qué se diferencian de un skill?

**Autoavaliación:**
- [ ] Ambos archivos tienen frontmatter YAML válido (entre `---` markers).
- [ ] El campo `description` de cada prompt describe claramente cuándo usarlo.
- [ ] Invoca el prompt con `/arch-review` en el chat de Copilot y verifica que se ejecuta.
- [ ] El prompt no incluye plantillas ni checklists embebidos de más de 5 líneas (si los necesita, es candidato a ser un skill).

---

### Tarea 3. Agente personalizado (Layer 4 — Custom Agents)

**Objetivo:** Crear un agente con una persona y restricciones de herramientas específicas.

**Enunciado:**

Crea un agente en `.github/agents/tutor.agent.md` que actúe como asistente docente socrático:
- Responde preguntas con preguntas de vuelta cuando sea apropiado.
- **Nunca escribe código directamente** — solo explica, guía y señala pistas.
- Puede leer código y la base de código, pero NO puede editarla.

El frontmatter debe listar **solo** las herramientas necesarias para un asistente de solo lectura. Omitir `editFiles` es suficiente para hacerlo constitutivamente incapaz de modificar código.

**Pistas:**
- La diferencia entre un agente personalizado y el modo Ask no es solo el prompt del sistema — es la lista de herramientas (`tools`).
- Abre el agente `tutor` desde el selector de agentes de Copilot y pídele que "revise la función `train()` en `train_model.py`". ¿Escribe código? ¿Formula preguntas?
- ¿Qué pasaría si añadieras `editFiles` a la lista de herramientas? ¿Sigue siendo socrático?

**Autoavaliación:**
- [ ] `tutor.agent.md` existe en `.github/agents/`.
- [ ] El frontmatter incluye `tools` con al menos `codebase` y `search`, pero **sin** `editFiles`.
- [ ] La `description` contiene palabras clave que permiten encontrarlo: "tutor", "review", "explain", "guide".
- [ ] Al probarlo, el agente responde con preguntas y no produce bloques de código directos.

---

### Tarea 4. Skills (Layer 3 — Skills)

**Objetivo:** Crear al menos dos skills con activos empaquetados.

**Enunciado:**

Crea las siguientes skills en `.github/skills/`:

**Skill A: `csv-eda-basica`**
- `SKILL.md` con los pasos del procedimiento EDA (carga, calidad, estadísticas, distribuciones, preguntas iniciales).
- Un checklist de calidad en `references/eda-checklist.md`.
- Una plantilla de notebook en `assets/notebook-template.md`.

**Skill B: `conventional-commit`**
- `SKILL.md` que, a partir de un diff de git, proponga un mensaje de commit siguiendo la especificación [Conventional Commits](https://www.conventionalcommits.org/).
- Ejemplos de commits correctos en `references/commit-examples.md`.

**Pistas:**
- El `name` del frontmatter de `SKILL.md` debe coincidir **exactamente** con el nombre de la carpeta. Un error aquí causa fallo silencioso.
- ¿Por qué `csv-eda-basica` es un skill y no un prompt? Piensa en: ¿necesita plantillas? ¿tiene pasos secuenciales que deben ser consistentes?
- Verifica que `/csv-eda-basica` aparece como comando slash en el chat de Copilot.

**Autoavaliación:**
- [ ] `csv-eda-basica/SKILL.md` tiene `name: csv-eda-basica` en el frontmatter (coincide con la carpeta).
- [ ] `conventional-commit/SKILL.md` tiene `name: conventional-commit` en el frontmatter.
- [ ] Ambas skills incluyen al menos un archivo de activos (checklist, plantilla o ejemplos).
- [ ] Invocar `/csv-eda-basica data/sample.csv` produce un análisis estructurado o una propuesta de notebook.
- [ ] La `description` de cada skill incluye frases que el usuario usaría naturalmente para invocarla.

> **Going further (optional):** La solución incluye skills adicionales fuera del mínimo obligatorio. Prueba `/debug-python-basico`, `/spec-a-tareas` y `/dataset-card` para explorar casos de uso complementarios. Como ejercicio extra, diseña una skill nueva apoyándote en `/frontmatter-designer` y `/comparar-primitivas`.

---

### Tarea 5. Hook de políticas (Layer 5 — Hooks)

**Objetivo:** Implementar un interceptor determinista para una política de proyecto.

**Enunciado:**

Crea un hook en `.github/hooks/` que intercepte las llamadas `read_file` sobre archivos `.ipynb` y proteja el contexto del agente de outputs embebidos:

1. **`notebook-guardian.json`** — Configura el evento `PreToolUse` para ejecutar el script Python.
2. **`hooks/scripts/notebook-guardian.py`** — Script Python que:
   - Lee un JSON de stdin con el nombre de la herramienta y su argumento de archivo.
   - Si la herramienta es `read_file` y el archivo es `.ipynb`: devuelve `{"action": "deny", "message": "..."}` con código de salida 2.
   - En cualquier otro caso: devuelve `{"action": "allow"}` con código de salida 0.

Puedes ampliar el script para que limpie los outputs realmente (como en la solución) o dejarlo como stub que simplemente bloquea.

**Prueba el script** antes de integrarlo:
```bash
echo '{"tool":"read_file","input":{"file":"test.ipynb"}}' | python3 hooks/scripts/notebook-guardian.py
# Debe mostrar: {"action": "deny", "message": "..."}

echo '{"tool":"read_file","input":{"file":"README.md"}}' | python3 hooks/scripts/notebook-guardian.py
# Debe mostrar: {"action": "allow"}
```

**Pistas:**
- Los hooks son lo único **determinista** en el sistema. Un script con `sys.exit(2)` siempre bloquea — no hay forma de que el modelo lo ignore.
- ¿Por qué este requisito no se puede resolver con una instrucción que diga "no leas notebooks sucios"?

**Autoavaliación:**
- [ ] `notebook-guardian.json` tiene el formato correcto con `"hooks": {"PreToolUse": [...]}`.
- [ ] El script Python pasa las dos pruebas de terminal anteriores.
- [ ] El script usa `json.loads(sys.stdin.read())` para leer el payload (no argumentos de línea de comandos).
- [ ] La respuesta de deny tiene `sys.exit(2)` (blocking) y la de allow tiene `sys.exit(0)`.

---

### Tarea 6. Reflexión sobre primitivas (skill meta)

**Objetivo:** Consolidar la comprensión de cuándo usar cada primitiva.

**Enunciado:**

Usando la skill `comparar-primitivas` de la solución (o la que hayas creado), responde por escrito a las siguientes preguntas en un archivo `doc/reflexion.md` en tu repositorio:

1. ¿Por qué las instrucciones con `applyTo` son superiores a una sola instrucción global para proyectos con múltiples tipos de archivo?
2. ¿Cuál es la diferencia clave entre un prompt y un skill? Da un ejemplo de caso de uso para cada uno.
3. ¿Por qué el agente `tutor` es incapaz de editar código incluso si el usuario se lo pide explícitamente?
4. ¿Podría el hook `notebook-guardian` implementarse como una instrucción? ¿Por qué sí o no?

**Autoavaliación:**
- [ ] `doc/reflexion.md` tiene respuestas a las cuatro preguntas.
- [ ] Cada respuesta cita al menos un archivo concreto del proyecto como evidencia.
- [ ] Las respuestas están escritas en inglés (consistente con el idioma del proyecto).

---

## Entrega

El repositorio debe contener, como mínimo:
- `.github/copilot-instructions.md`
- `.github/instructions/python.instructions.md` y `notebooks.instructions.md`
- `.github/prompts/arch-review.prompt.md` y `todo-to-plan.prompt.md`
- `.github/agents/tutor.agent.md`
- `.github/skills/csv-eda-basica/` y `conventional-commit/`
- `.github/hooks/notebook-guardian.json` y `hooks/scripts/notebook-guardian.py`
- `doc/reflexion.md`

Comparte el enlace al repositorio de GitHub en el entregable de la plataforma.

## Recursos

- Solución de referencia: `solucion/`
- Arquitectura de capas: [solucion/doc/capas.md](solucion/doc/capas.md)
- Justificación de decisiones: [solucion/doc/justificacion.md](solucion/doc/justificacion.md)
- Documentación oficial de Copilot customizations: <https://code.visualstudio.com/docs/copilot/copilot-customization>
