# El I Chingón — Cuartel General

Este repositorio contiene el código fuente y los contenidos de **El I Chingón** (`https://elichingon.com/`), una plataforma de consulta del I Ching con privacidad estricta y un repositorio de estudio y ensayos.

## Propósito del Proyecto
Reunir la consulta oracular bajo el protocolo **CSHC** (*Constrained Stochastic Hermeneutical Computing*) - diseñado para mitigar la complacencia y las alucinaciones de los LLM comerciales mediante entropía física, textos canónicos de Richard Wilhelm y ejecución sin estado en el borde - junto con el estudio directo de las fuentes clásicas y ensayos originales en español, inglés y alemán.

## Arquitectura y Recursos Clave
* **Sitio y generación:** Sitio estático generado con Hugo (tema Blowfish) y desplegado en GitHub Pages, con soporte multilingüe (`es`, `en`, `de`).
* **Privacidad y ejecución:** Sin inicio de sesión, sin cookies ni rastreo invasivo, con telemetría anónima en Umami y procesamiento efímero en el borde mediante Cloudflare Workers.
* **Referencia de Backend (`backend-reference/`):** Implementación de referencia (`worker.js`) y documentación de privacidad/arquitectura auditables públicamente.
* **Whitepaper y DOI:** El protocolo CSHC está formalizado en el whitepaper con DOI permanente `10.5281/zenodo.24483432` (versiones en español, inglés y alemán archivadas en Zenodo).