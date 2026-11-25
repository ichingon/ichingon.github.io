## Privacy and Backend Architecture (El I Chingón) - English

This directory contains the **reference implementation** of the server code (Backend) that powers the AI-assisted oracular consultations under the **CSHC (Constrained Stochastic Hermeneutical Computing)** protocol on [elichingon.com/en/](https://elichingon.com/en/).

We make this code public as an exercise in transparency (*Proof of Transparency*) so any developer can audit how privacy, deterministic canonical text injection, and ephemeral execution work in practice.

### Structural Amnesia (Why you are safe)

Unlike centralized AI applications ("Plastic Oracles") that require accounts and store intimate queries in databases to profile users or train models, the backend of *El I Chingón* is built around **Structural Amnesia** and stateless edge execution on **Cloudflare Workers**.

By reviewing `worker.js` in this folder alongside the CSHC whitepaper, the data flow works as follows:

1. **Reception:** The Worker receives the payload (including the user's question, cast hexagram, moving lines, and voucher code) over TLS.
2. **Blind validation:** It checks the prepaid *Gift Card* balance in Cloudflare D1 (`gift_cards`) without tying it to any personal identity, login, or email address.
3. **RAM & Edge Processing:** It deterministically resolves the hexagram, moving lines, and Earlier Heaven (*Fuxi*) antecedent mapping, injects the canonical Richard Wilhelm texts, and calls the constrained model on Cloudflare Workers AI (`@cf/deepseek-ai/deepseek-v4.1-flash-1017`, subject to change as documented in `worker.js`).
4. **Ephemeral Cleanup & Minimal Operational State:** Once the response is returned to the client, the V8 isolate session state is torn down in memory. Only non-personal voucher credit updates (`gift_cards`) and anonymous aggregate operational metrics (`consultas`: timestamp, country code, casting method, interface mode, language, version, and neuron cost) are written to D1. **User questions, cast hexagrams, moving lines, IP addresses, and generated interpretations are never stored in any database.**

### Institutional Guarantee (Cloudflare Terms)

Processing inference payloads through Cloudflare Workers AI inherits Cloudflare's enterprise data-usage terms, which prohibit using customer inference payloads to train AI models. Combined with stateless execution and open-source auditability, privacy is enforced architecturally and contractually rather than through user profiling.

> *"Cloudflare does not use Customer Content processed by Workers AI to train AI models."*
> — [Cloudflare Workers AI Data Usage Policy](https://developers.cloudflare.com/workers-ai/platform/data-usage/)

### Files and Documentation
- `worker.js`: Reference logic of the Cloudflare Worker (sanitized of environment variables and secrets).
- Repository path: `https://github.com/ichingon/ichingon.github.io/blob/main/backend-reference/worker.js`
- CSHC Whitepaper & Permanent DOI: `10.5281/zenodo.24483432` ([https://doi.org/10.5281/zenodo.24483432](https://doi.org/10.5281/zenodo.24483432))

---

## Arquitectura de Privacidad y Backend (El I Chingón) - Español

Este directorio contiene la **implementación de referencia** del código de servidor (Backend) que impulsa las consultas oraculares asistidas por IA bajo el **protocolo CSHC (Constrained Stochastic Hermeneutical Computing)** en [elichingon.com](https://elichingon.com/).

Hacemos este código público como un ejercicio de transparencia (*Proof of Transparency*) para que cualquier desarrollador pueda auditar cómo operan en la práctica la privacidad, la inyección determinista de textos canónicos y la ejecución efímera.

### Amnesia Estructural (Por qué estás a salvo)

A diferencia de las aplicaciones de IA centralizadas ("Oráculos de Plástico") que exigen cuentas y guardan preguntas íntimas en bases de datos para perfilar usuarios o entrenar modelos, el *backend* de *El I Chingón* se apoya en la **Amnesia Estructural** y la ejecución sin estado en el borde mediante **Cloudflare Workers**.

Al revisar `worker.js` en esta carpeta junto con el *whitepaper* de CSHC, el ciclo de procesamiento funciona así:

1. **Recepción:** El Worker recibe el *payload* (pregunta del consultante, hexagrama obtenido, líneas móviles y código de vale) cifrado en tránsito mediante TLS.
2. **Validación ciega:** Verifica el saldo de la *Gift Card* prepagada en Cloudflare D1 (`gift_cards`) sin vincularlo a ninguna identidad personal, cuenta ni correo electrónico.
3. **Procesamiento en RAM y en el borde:** Resuelve de forma determinista el hexagrama, las líneas móviles y la correspondencia del Cielo Anterior (*Fuxi*), inyecta los textos canónicos de Richard Wilhelm y ejecuta el modelo constreñido en Cloudflare Workers AI (`@cf/deepseek-ai/deepseek-v4.1-flash-1017`, sujeto a cambios según se documente en `worker.js`).
4. **Limpieza efímera y registro operativo mínimo:** Una vez devuelta la respuesta al cliente, el estado de sesión del aislado V8 se destruye en memoria. En D1 solo se actualizan los créditos de los vales (`gift_cards`) y se registran métricas operativas agregadas y anónimas (`consultas`: marca temporal, código de país, método de tirada, modo de interfaz, idioma, versión y costo en neuronas). **Las preguntas de los usuarios, los hexagramas obtenidos, las líneas móviles, las direcciones IP y las interpretaciones generadas nunca se guardan en ninguna base de datos.**

### Garantía Institucional (Términos de Cloudflare)

Al procesar las cargas de inferencia mediante Cloudflare Workers AI, el sistema hereda los términos empresariales de uso de datos de Cloudflare, que prohíben emplear las cargas útiles de inferencia de los clientes para entrenar modelos de IA. Junto con la ejecución sin estado y la auditabilidad del código, la privacidad queda respaldada a nivel arquitectónico y contractual.

> *"Cloudflare does not use Customer Content processed by Workers AI to train AI models."*
> — [Cloudflare Workers AI Data Usage Policy](https://developers.cloudflare.com/workers-ai/platform/data-usage/)

### Archivos y Documentación
* `worker.js`: Lógica de referencia del Cloudflare Worker (sanitizada de variables de entorno y secretos).
* Ruta en el repositorio: `https://github.com/ichingon/ichingon.github.io/blob/main/backend-reference/worker.js`
* Whitepaper CSHC y DOI permanente: `10.5281/zenodo.24483432` ([https://doi.org/10.5281/zenodo.24483432](https://doi.org/10.5281/zenodo.24483432))