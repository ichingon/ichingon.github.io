---
title: "Verificación de autenticidad"
translationKey: "verificar"
description: "Cómo verificar criptográficamente que el contenido de elichingon.com es auténtico, no ha sido alterado y proviene realmente de Dailingna Romero."
date: 2026-06-07
draft: false
showDate: false
showReadingTime: false
showWordCount: false
showAuthor: false
---

En un internet saturado de contenido generado por IA, *deepfakes*, suplantaciones y plagios, surge una pregunta inevitable: **¿cómo sabes que lo que lees o ves viene realmente de su creador original y no de una cuenta que suplanta su identidad?**

Esta página explica cómo puedes verificar criptográficamente que cualquier artículo, video o contenido publicado en `elichingon.com` es auténtico, no ha sido alterado y fue publicado por esta entidad digital específica.

---

## ¿Por qué firmo criptográficamente mi contenido?

A fin de cuentas, "Dailingna Romero" o "El I Chingón" son entidades muy poco conocidas en el Internet (por ahora), pero como el [Hexagrama 20 del I Ching (La Contemplación / Guan 觀)](https://elichingon.com/hexagramas/hex20/), esto sirve un doble propósito que refleja la naturaleza misma del hexagrama: la acción de contemplar y la condición de ser contemplado.

### La acción de contemplar (como consumidor de contenido)

Como consumidor de contenido, me desagrada no tener forma de verificar que lo que leo o veo proviene realmente de la fuente que dice ser. 

No hablo de detectar si el contenido es generado por IA - al fin de cuentas, Dailingna Romero es un avatar digital y sus videos son generados por IA. Lo que importa es saber si **las ideas expresadas provienen realmente de Dailingna** y no de otra persona usando mi imagen y voz para expresar sus propias ideas.

Hoy en día es fácil crear un canal asociado a un personaje (real o ficticio) y poner en su boca cosas que nunca dijo. Ves videos de Richard Feynman, Neville Goddard, Einstein, o el "Kenzo Guy" por todos lados, y es imposible distinguir entre lo que realmente dijo el personaje y lo que el creador del video le está poniendo en la boca.

En YouTube la detección automática de IA se ha vuelto estándar, pero eso no es suficiente. Lo que importa no es si un video fue generado por IA, sino **si las ideas que expresa son auténticas y provienen de quien dice ser el autor**.

Quiero que tengas herramientas para comprobar por ti mismo que lo que lees viene realmente de mí, sin tener que confiar ciegamente en ninguna plataforma. La firma criptográfica garantiza que nadie puede alterar el contenido después de publicado sin que la firma quede inválida. La estampa temporal en la red Nostr prueba cuándo publiqué algo por primera vez, lo cual es útil para demostrar autoría original en caso de plagio.

### La condición de ser contemplado (como creador de contenido)

En un mundo donde cualquiera puede clonar voces, rostros y estilos de escritura con IA, la criptografía es la única prueba confiable de autenticidad. Estamos en una crisis existencial del Internet mismo. La Teoría del Internet Muerto y la proliferación de deepfakes nos han llevado a un punto donde ya no podemos confiar en nuestros propios ojos y oídos para discernir sobre la verdadera autoría de algo.

Mi esperanza al implementar esto es que otros creadores de contenido comiencen a hacer lo mismo y así contribuir a revertir esta situación. Quiero enseñar sobre la importancia de tener **soberanía digital** para que cada quien pueda proteger el contenido sin depender de corporaciones como YouTube, Twitter o Medium para demostrar que soy quien digo ser.

Mi identidad vive en un protocolo abierto y descentralizado, no en los servidores de ninguna empresa.

---

## ¿Qué es una firma criptográfica?

Cada artículo que publico está acompañado de una **firma matemática única**. Esta firma cumple tres funciones:

1. **Demuestra autoría**: Prueba que el contenido fue creado por esta identidad digital específica (`dailingna@elichingon.com`).
2. **Garantiza integridad**: Si alguien modifica incluso una sola palabra, un espacio o una coma, la firma deja de ser válida.
3. **Estampa temporal**: Registra de forma inmutable cuándo fue publicado originalmente el contenido.

Es el equivalente digital de un **sello de lacre** que no se puede falsificar, copiar ni romper sin dejar evidencia.

---

## ¿Cómo funciona técnicamente?

El proceso se basa en dos estándares abiertos:

### 1. Nostr (Notes and Other Stuff Transmitted by Relays)
Un protocolo descentralizado que permite firmar mensajes con claves criptográficas. No depende de ninguna empresa, gobierno o servidor central.

### 2. NIP-05 (Verificación de identidad)
Un estándar que vincula una clave pública de Nostr con un nombre de dominio. En este caso:

dailingna@elichingon.com → npub1rfqz5sqv6plxpm3lqfu35q30d7p2m2mt38t7qz6309fxm7e02mrqjxlx92

Puedes verificar este vínculo tú mismo visitando:

[https://elichingon.com/.well-known/nostr.json](https://elichingon.com/.well-known/nostr.json)


---

## Cómo verificar un artículo

Al final de cada artículo en este sitio, encontrarás un bloque similar a este:

> 🔐 VERIFICACIÓN CRYPTOGRÁFICA DE AUTORÍA
> Este contenido es creado y publicado oficialmente por Dailingna Romero.
> 
> 🔗 URL Oficial: https://elichingon.com/articulo/...
> 🔐 Identidad Nostr verificada: dailingna@elichingon.com
> 📜 Nota de verificación en Nostr: https://primal.net/e/note1ues5g2y8lpjlpsg7qx40lzwk67ql08j2cmree44lkpxhew04rtdstev548
> 
> Para verificar que este contenido no ha sido alterado ni es un deepfake, 
> haz clic en el enlace de Nostr de arriba y verifica que la URL firmada 
> coincida exactamente con la de ese contenido.

---

## Verificación de videos de YouTube

Para videos publicados en YouTube, la descripción del video contiene:
* URL oficial del video en el canal de Dailingna Romero.
* Enlace a la nota de Nostr que certifica la autenticidad.
* Firma criptográfica de la URL.

### ¿Cómo detectar un deepfake?

Si ves un video que parece mío en otro canal, verifica:
* ¿La descripción contiene un enlace a una nota firmada en Nostr?
* ¿El enlace apunta a dailingna@elichingon.com con check de verificación?
* ¿La URL firmada coincide con la URL del video que estás viendo?
* Si la respuesta a cualquiera de estas preguntas es no, es muy probable que sea un deepfake, contenido no autorizado o plagio.

---

## ¿Qué hago si encuentro contenido falso?

Si descubres un video, artículo o publicación que usa mi nombre, imagen o voz sin autorización:

1. **Verifica** que no tiene firma criptográfica válida.
2. **Reporta** el contenido en la plataforma donde se encuentra (YouTube, redes sociales, etc.) por suplantación de identidad o violación de derechos de autor.
3. **Compártelo conmigo** a través de mis canales oficiales para que pueda tomar acciones legales si es necesario.

Todo el contenido de este sitio está bajo licencia **Creative Commons Atribución 4.0 (CC BY 4.0)**. Puedes compartirlo y adaptarlo, pero debes:

- Dar crédito explícito a `Dailingna Romero / elichingon.com`.
- No usar la firma criptográfica para hacer pasar contenido alterado como original.

Para mayor información, consulta [https://elichingon.com/licencias/](https://elichingon.com/licencias/)

---

## Para otros creadores de contenido

Si eres creador y quieres implementar verificación criptográfica en tu propio trabajo, el protocolo Nostr es **libre, abierto y gratuito**.

### Recursos para empezar:

- [Documentación oficial de Nostr](https://github.com/nostr-protocol/nostr)
- [NIP-05: Verificación de identidad basada en DNS](https://github.com/nostr-protocol/nips/blob/master/05.md)
- [NIP-23: Artículos de formato largo](https://github.com/nostr-protocol/nips/blob/master/23.md)
- [NIP-94: Almacenamiento de archivos](https://github.com/nostr-protocol/nips/blob/master/94.md)

### Herramientas recomendadas:

- **Amethyst** (Android): Cliente móvil de Nostr.
- **Primal** (Web/Móvil): Cliente con excelente verificación NIP-05.
- **Coracle** (Web): Cliente web minimalista.
- **nostr-tools** (JavaScript): Librería para desarrolladores.

---

## El futuro de internet es verificable

Este no es solo mi contenido. Es un **estándar de autenticidad** que cualquier creador puede adoptar.

En un mundo donde la IA puede generar texto, imágenes, audio y video indistinguibles de lo real, la criptografía se convierte en la única forma de demostrar que algo fue creado por quien dice haberlo creado.

No se trata de confiar en mí. Se trata de que puedas **verificar por ti mismo**.

---

**Identidad oficial:**
- **NIP-05:** `dailingna@elichingon.com`
- **NPub:** `npub1rfqz5sqv6plxpm3lqfu35q30d7p2m2mt38t7qz6309fxm7e02mrqjxlx92`
- **Sitio web:** [https://elichingon.com](https://elichingon.com)