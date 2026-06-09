# Material para a Formación Profesional Inicial

**A04. Personalizacións para programación eficiente con IA**

---

## 1. Ficha Técnica

**Datos de Identificación**
* **Familia profesional:** Informática e Comunicacións
* **Ciclo formativo / Curso de especialización:** CE3IFC005200 - Curso de especialización en Intelixencia artificial e big data
* **Módulo profesional:** MP5073 - Programación de intelixencia artificial
* **Unidade didáctica:** UD01 - Ecosistema de programación para IA
* **Actividade:** A04 - Personalizacións para programación eficiente con IA
* **Licenza:** © 2026 Xunta de Galicia. Creative Commons BY-NC-SA 3.0 ES

**Contexto da Actividade e Duración**
* **Módulo:** MP5073. Programación con IA (Duración: 200h)
* **Unidade Didáctica:** UD01. Ecosistema de programación para IA (Duración total: 37 sesións de 50')
* **Actividades previas da UD:** A01 (9 sesións), A02 (9 sesións), A03 (9 sesións)
* **Esta Actividade (A04):** Personalizacións para programación eficiente con IA (Duración: 18 sesións)
* **Descrición da A04:** Configuraranse exemplos de personalizacións de Copilot nun repositorio de proxectos de IA: instrucións, prompts, skills, axentes e hooks.

---

## 2. Resultados de Aprendizaxe e Obxectivos

**Resultados de aprendizaxe do currículo**
* **RA1 (Parcial):** Caracteriza linguaxes de programación valorando a súa idoneidade no desenvolvemento de Intelixencia Artificial.
* **RA3 (Parcial):** Avalía as melloras nos negocios integrando converxencia tecnolóxica.

**Obxectivos didácticos específicos**
* **O4.1:** Configurar GitHub Copilot mediante instrucións globais e específicas por tipo de arquivo.
* **O4.2:** Crear prompts reutilizables para tarefas frecuentes de desenvolvemento.
* **O4.3:** Implementar un axente docente socrático con restrición de ferramentas.
* **O4.4:** Desenvolver skills con activos empaquetados para fluxos de traballo de datos.
* **O4.5:** Implementar un hook determinista que aplique políticas do repositorio.
* **O4.6:** Reflexionar sobre a elección de primitivas e os seus trade-offs.

---

## 3. Avaliación, Contidos e Recursos

| Criterios de avaliación | Instrumentos de avaliación |
| :--- | :--- |
| **subCA1.4.1:** Deseñáronse personalizacións para facilitar a programación facendo uso de modelos de IA. | Rúbrica sobre o repositorio entregado: as personalizacións cárganse correctamente en VS Code; as skills son invocables con /. |
| **CA1.6:** Caracterizáronse linguaxes de marcaxe destacando a información que conteñen as súas etiquetas. | Rúbrica sobre o repositorio: os ficheiros están correctamente definidos e seguen os estándares. |
| **subCA3.1.1:** Avaliación da mellora de produtividade. | Rúbrica sobre o documento de reflexión: as catro preguntas están respondidas con argumentos baseados en evidencias do repositorio. |
| **subCA4.1.1:** Identificáronse as novas estratexias e modelos no desenvolvemento de software. | Rúbrica sobre o documento de reflexión: o alumnado distingue entre primitivas deterministas (hooks) e non deterministas (instrucións), e entre primitivas pasivas e activas. |

**Contidos a tratar**
* Arquitectura de personalización de GitHub Copilot: as cinco capas (Instructions, Prompts, Skills, Agents, Hooks).
* Instrucións globais (copilot-instructions.md) e específicas por tipo de arquivo (applyTo).
* Prompts almacenados (.prompt.md): macros de texto reutilizables.
* Skills (.github/skills/): paquetes de fluxo de traballo con activos empaquetados.
* Axentes personalizados (.agent.md): restrición de ferramentas e definición de persona.
* Hooks (.github/hooks/): interceptores deterministas de eventos do ciclo de vida do axente.
* Frontmatter YAML: campos obrigatorios e erros comúns.
* Primitivas para fluxo de traballo de datos: EDA, dataset cards, debugging Python.

**Resultados ou produtos agardados**
* Repositorio GitHub con personalizacións: dous prompts invocables almacenados; un axente titor con restrición de ferramentas verificada; dúas skills con activos empaquetados; un hook.
* Documento de xustificación sobre elección de primitivas.

**Recursos e Documentación Base**
* Documentación oficial de VSCode Agents: https://code.visualstudio.com/docs/agents/overview
* Documentación oficial de GitHub Copilot Agents: https://docs.github.com/en/copilot/concepts/agents
* VSCode instalado con acceso a personalizacións integradas (built-in).
* Conta de GitHub con licenza educativa.
* Repositorio proporcionado coas ramas "asigment" (enunciado) e "solution" (solución proposta).

---

## 4. Desenvolvemento da Actividade (A04)

### Introdución e Contexto
A introdución de asistentes e axentes de IA no desenvolvemento de software está a transformar de maneira clara os fluxos de traballo profesionais. Visual Studio Code xunto con GitHub Copilot constitúe unha opción especialmente axeitada para a aula grazas á súa extensión no desenvolvemento actual e as súas capacidades de asistencia e personalización contextual. A licenza educativa elimina barreiras económicas, permitindo o acceso a modelos premium e autocompletados ilimitados.

Pedagoxicamente, despraza o foco da memorización sintáctica cara á arquitectura de solucións, a organización do repositorio e a revisión crítica do código. Isto permite acelerar o avance cara aos contidos nucleares da materia: deseño de pipelines, selección de modelos e avaliación de resultados de Machine Learning.

O repositorio de partida inclúe un clasificador sinxelo sobre o dataset Iris en PyTorch (`src/train_model.py`), un notebook de análise exploratoria (`notebooks/01_eda_example.ipynb`) e un CSV de apoio (`data/sample.csv`). As personalizacións organízanse en cinco capas.

### As Cinco Capas de Personalización
* **1. Instrucións (Instructions):** Contexto persistente cargado automaticamente de xeito global ou específico por ficheiro. Serve para fixar políticas transversais (idioma, sementes) ou regras de estilo específicas (PEP 8, type hints).
* **2. Prompts almacenados (Prompt Files):** Plantillas reutilizables invocadas manualmente no chat para estandarizar peticións frecuentes sen reescribilas.
* **3. Axentes personalizados (Custom Agents):** Versións especializadas con instrucións e restricións de ferramentas (tools), permitindo roles diferenciados (ex. un axente de só lectura).
* **4. Skills:** Paquetes de instrucións, scripts e recursos empaquetados aplicables a tarefas especializadas complexas.
* **5. Hooks:** Mecanismos deterministas que executan comandos de shell en eventos do axente para impoñer políticas ou bloqueos de seguridade ineludibles.

---

## 5. Descrición das Tarefas Prácticas

### Tarefa 1. Instrucións globais e específicas por tipo de arquivo
Crea un arquivo `.github/copilot-instructions.md` no repositorio que inclúa:
* Unha descrición do contexto do proxecto.
* Polo menos dúas políticas transversais (idioma da documentación, política de sementes).
* Unha referencia aos arquivos de instrucións específicos.

A continuación, crea instrucións específicas usando o campo `applyTo` do frontmatter YAML:
* `.github/instructions/python.instructions.md`: normas de estilo para Python (PEP 8, type hints, docstrings NumPy).
* `.github/instructions/notebooks.instructions.md`: normas para notebooks (estrutura narrativa, limpeza de outputs).

**Autoavaliación:**
* [ ] Arquivos creados con frontmatter YAML válido (entre `---`).
* [ ] O ficheiro de Python ten `applyTo: "**/*.py"`.
* [ ] O ficheiro de notebooks ten `applyTo: "**/*.ipynb"`.
* [ ] `applyTo` está ben configurado e as regras cárganse ao editar eses ficheiros en VS Code.

### Tarefa 2. Prompts almacenados
Crea polo menos dous ficheiros de prompt en `.github/prompts/`:
* Un prompt que analice a arquitectura do proxecto e produza un informe de puntos fortes e debilidades.
* Un prompt que escanee comentarios TODO e xere unha lista priorizada de tarefas.

**Pistas:** Un prompt é só texto expandido, non contén lóxica. O campo `description` do frontmatter aparece no autocompletado do chat.

**Autoavaliación:**
* [ ] Frontmatter YAML válido.
* [ ] O campo `description` é claro.
* [ ] Invocables con `/` no chat.
* [ ] Non inclúen plantillas embebidas longas (iso sería unha skill).

### Tarefa 3. Axente personalizado socrático
Crea un axente en `.github/agents/tutor.agent.md` que actúe como docente socrático:
* Responde con preguntas, non escribe código e só pode ler a base de código (non editala).

**Pistas:** A restrición defínese na lista de ferramentas (tools) do frontmatter. Omitir `editFiles` fai que a IA sexa estruturalmente incapaz de editar código.

**Autoavaliación:**
* [ ] Arquivo `tutor.agent.md` creado.
* [ ] O frontmatter inclúe `codebase` e `search` en tools, pero omite `editFiles`.
* [ ] O axente aparece no selector e non produce código funcional directo.

### Tarefa 4. Skills con activos empaquetados
Crea as seguintes skills en `.github/skills/`:
* **Skill A (csv-eda-basica):** Ficheiro `SKILL.md` con pasos de EDA, unha checklist en `references/eda-checklist.md` e unha plantilla en `assets/notebook-template.md`.
* **Skill B (conventional-commit):** Ficheiro `SKILL.md` para propoñer mensaxes de commit, con exemplos en `references/commit-examples.md`.

**Autoavaliación:**
* [ ] O campo `name` do frontmatter coincide exactamente co nome do cartafol correspondente.
* [ ] Inclúen activos válidos (plantillas ou checklists).
* [ ] A execución manual xera análises estruturadas correctas.

### Tarefa 5. Hook de políticas
Crea un hook determinista para rexeitar lecturas de ficheiros Jupyter Notebook excesivamente pesados:
* **Definición:** Crea `.github/hooks/notebook-guardian.json` co evento `PreToolUse`.
* **Script:** Crea `.github/hooks/scripts/notebook-guardian.py`.
* O script debe ler de `stdin`. Se a ferramenta é `read_file` e o input é un `.ipynb`, devolver `{"action": "deny"}` e saír con código 2. Noutro caso, devolver `{"action": "allow"}` e saír con código 0.

Para testear o script (debe ser estritamente executado na terminal local para verificar o comportamento):
```bash
echo '{"tool":"read_file","input":{"file":"test.ipynb"}}' | python3 .github/hooks/scripts/notebook-guardian.py
# Expected output: {"action": "deny", "message": "..."}

echo '{"tool":"read_file","input":{"file":"README.md"}}' | python3 .github/hooks/scripts/notebook-guardian.py
# Expected output: {"action": "allow"}
```

**Autoavaliación:**
* [ ] O JSON configúrase sobre o evento `PreToolUse`.
* [ ] O script utiliza `json.loads(sys.stdin.read())` e non xera falsos positivos en terminal.
* [ ] O código de saída diferénciase estritamente (2 para bloqueo, 0 para validación).

### Tarefa 6. Reflexión sobre primitivas
Responde en inglés no ficheiro `doc/reflexion.md`:
1. Por que as instrucións con `applyTo` son superiores a unha soa instrución global para proxectos heteroxéneos?
2. Cal é a diferenza estrutural entre un prompt e un skill? (Engade exemplos do repositorio).
3. Por que o axente titor non pode editar código a pesar das peticións directas?
4. Pode implementarse un hook coma unha instrución? Razoa a resposta baseándote no determinismo.

**Autoavaliación:**
* [ ] As catro preguntas responden citando evidencias e ficheiros concretos do repositorio.
* [ ] O documento está integramente redactado en inglés.

---

## 6. Rúbrica de Avaliación

**Pesos da avaliación:**
* Implementación Técnica: 70%
* Reflexión Crítica: 30%

| Categoría / Tarefa | Puntuación (Excelente) | Puntuación (Bo/Competente) | Puntuación (Insuficiente) |
| :--- | :--- | :--- | :--- |
| **Implementación Técnica** (Tarefas 1-5) | As customizacións funcionan perfectamente. YAML válido, Markdown correcto e obxectivos cumpridos. | Funcionan na súa maioría, con pequenos erros en rutas `applyTo` ou detalles menores. | Non cargan ou teñen fallos graves. O código non segue os estándares. |
| **Restricións e Determinismo** (Tarefas 3 e 5) | O axente cumpre estritamente (non edita). O hook bloquea lecturas de forma ineludible. | Segue a maioría das regras, pero o hook ten problemas menores de integración ou control de erros. | O axente edita código (falla de restrición). O hook non bloquea as accións non autorizadas. |
| **Empaquetado e Estrutura** (Tarefa 4) | Skills correctamente estruturadas (nomes e cartafoles coincidentes) con activos reutilizables. | Falta algún activo ou a nomenclatura non é perfecta, pero as skills son invocables. | Erros estruturais críticos (nomes non coincidentes) xerando fallos silenciosos no sistema. |
| **Análise e Reflexión** (Tarefa 6) | Respostas fundamentadas en evidencias do repositorio. Argumenta os trade-offs entre primitivas. | Argumentación feble ou vinculación superficial co traballo técnico realizado. | Respostas vagas, sen base teórica nin conexión co traballo entregado. |