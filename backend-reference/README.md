## Privacy and Backend Architecture (El I Chingón) - English

This directory contains the **reference implementation** of the server code (Backend) that powers the Artificial Intelligence oracular consultations on [elichingon.com/en/](https://elichingon.com/en/). 

We are making this code public as an exercise in radical transparency (Proof of Transparency) to structurally demonstrate our commitment to user privacy.

### Structural Amnesia (Why you are safe)

Unlike "Plastic Oracles" (centralized AI applications) that require a login and store your intimate questions in databases to profile you or train models, the architecture of *El I Chingón* operates under the principle of **Structural Amnesia**.

Our backend is built on **Cloudflare Workers** (Edge Computing). By reviewing the attached `worker.js` file in this folder, any developer can audit and verify the following data lifecycle:

1. **Reception:** The Worker receives your oracular question (payload) encrypted in transit.
2. **Blind validation:** It verifies the balance of your prepaid *Gift Card* without linking it to any personal identity.
3. **RAM Processing:** It assembles the hermeneutic query and communicates securely with the language model.
4. **Absolute destruction:** Once the response is returned, the memory isolate (V8 Isolate) spins down. The variable containing your question is destroyed in the RAM in milliseconds. **There are no `INSERT` statements to any database to save consultation histories.**

### Institutional Guarantee (Cloudflare ToS)

Our promise not to use your crises or vulnerabilities to feed algorithms (Semantic Vampirism) is backed by infrastructure-level contracts. 

By processing queries through Cloudflare, we automatically inherit their strict enterprise Service Level Agreement (SLA), which explicitly prohibits the use of customer data and queries for Artificial Intelligence training.

> *"Cloudflare does not use Customer Content processed by Workers AI to train AI models."*
> — [Cloudflare Workers AI Data Usage Policy](https://developers.cloudflare.com/workers-ai/platform/data-usage/)

### Files in this directory
- `worker.js`: Core logic of the Cloudflare Worker (sanitized of environment variables and API keys).

---

## Arquitectura de Privacidad y Backend (El I Chingón) - Español

Este directorio contiene la **implementación de referencia** del código de servidor (Backend) que impulsa las consultas oraculares de Inteligencia Artificial en [elichingon.com](https://elichingon.com). 

Hacemos este código público como un ejercicio de transparencia radical (Proof of Transparency) para demostrar estructuralmente nuestro compromiso con la privacidad del usuario.

### Amnesia Estructural (Por qué estás a salvo)

A diferencia de los "Oráculos de Plástico" (aplicaciones de IA centralizadas) que exigen un inicio de sesión y guardan tus preguntas íntimas en bases de datos para perfilarte o entrenar modelos, la arquitectura de *El I Chingón* opera bajo el principio de **Amnesia Estructural**.

Nuestro backend está construido sobre **Cloudflare Workers** (Edge Computing). Al revisar el archivo `worker.js` adjunto en esta carpeta, cualquier desarrollador puede auditar y verificar el siguiente ciclo de vida de los datos:

1. **Recepción:** El Worker recibe tu pregunta oracular (payload) cifrada en tránsito.
2. **Validación ciega:** Verifica el saldo de tu *Gift Card* prepagada sin vincularla a ninguna identidad personal.
3. **Procesamiento en RAM:** Ensambla la consulta hermenéutica y se comunica con el modelo de lenguaje de forma segura.
4. **Destrucción absoluta:** Una vez devuelta la respuesta, el aislado de memoria (V8 Isolate) se apaga. La variable que contenía tu pregunta se destruye en la memoria RAM en milisegundos. **No existen sentencias `INSERT` hacia ninguna base de datos para guardar historiales de consultas.**

### Garantía Institucional (Cloudflare ToS)

Nuestra promesa de no utilizar tus crisis o vulnerabilidades para alimentar algoritmos (Vampirismo Semántico) está respaldada por contratos a nivel de infraestructura. 

Al procesar las consultas mediante Cloudflare, heredamos automáticamente su estricto Acuerdo de Nivel de Servicio (SLA) empresarial, el cual prohíbe explícitamente el uso de los datos y consultas de los clientes para el entrenamiento de Inteligencia Artificial.

> *"Cloudflare does not use Customer Content processed by Workers AI to train AI models."*
> — [Cloudflare Workers AI Data Usage Policy](https://developers.cloudflare.com/workers-ai/platform/data-usage/)

### Archivos en este directorio
* `worker.js`: Lógica base del Cloudflare Worker (sanitizada de variables de entorno y claves de API).
