---
title: "La privacidad según El I Chingón - ¿porqué debería importarte?"
date: 2026-10-22
author: "Dài Líng Nà (黛灵娜)"
showAuthor: true
showAuthorBottom: true
showFooterAuthor: true
tags: ["El Tao del Creador de Contenidos"]
description: "Descubre por qué la privacidad es vital en una consulta oracular y cómo El I Chingón protege tu privacidad."
summary: "Descubre por qué la privacidad en un app de consulta oracular no es un lujo, sino una necesidad, y cómo construimos elichingon.com con amnesia estructural y pagos ciegos para blindar tus secretos."
draft: false
slug: "privacidad-segun-elichingon-por-que-deberia-importarte"
---

En el [whitepaper de mi aplicación]({{< relref "articulos/i-chingon-whitepaper" >}}), donde hablo de mi protocolo de Computación Hermenéutica Estocástica Constreñida (CSHC, por sus siglas en inglés), expongo que la privacidad radical es uno de los pilares fundamentales de mi protocolo. En este artículo voy a explicar, hablandole al usuario común, porqué esto es tan importante, cómo se diferencia El I Chingón de otros sitios web o apps oraculares en este aspecto, y cómo, sin entrar en muchos tecnicismos, podrías auditar la privacidad de El I Chingón o cualquiera de estos sitios.

---

## El mito de "no tengo nada que ocultar"

![Dài Líng Nà operando fuera del panóptico digital. Tu oráculo no debería ser tu espía.](featured.jpg "Dài Líng Nà operando fuera del panóptico digital. Tu oráculo no debería ser tu espía.")

Es preocupante ver como tantas personas son ajenas a los riesgos de seguridad y privacidad en el Internet. Al parecer muchos asumen que la privacidad es sólo para criminales o hackers, y como no estan incursos en delitos, no tienen nada que ocultar y por lo tanto la privacidad es un tema irrelevante para ellos. Craso error- la privacidad es importante para todo el mundo y es (o debería ser) un derecho humano básico universal.

Comenzamos con la naturaleza misma de lo que es una consulta oracular. La consulta oracular es, por defecto, un acto muy privado, dado lo personal que podrían ser algunas preguntas de gente que esta pasando por problemas de relaciones, situaciones vergonzosas o albergando pensamientos inconfesables. Con esto no quiero decir que el I Ching solamente sirve para este [tipo de preguntas]({{< relref "articulos/que-podemos-preguntar" >}}), obviamente. Pero como en el I Ching, el consultante es una parte fundamental e inseparable del sistema consultante-oraculo-realidad, muchas preguntas que le hacemos al I Ching terminan gravitando hacia temas de índole muy personal. Y por lo tanto, no queremos que esta información termine en otras manos, o leidas por otros pares de ojos.

Pero además hay un tema de efectividad del oráculo. Si sospechamos, consciente o subconscientemente, que la privacidad de la consulta oracular esta comprometida, se podría producir un fenomeno muy nocivo para la efectividad de las lecturas del I Ching: la **auto-censura**. El consultante deja de hacer las preguntas que realmente le importan, maquilla sus miedos en la redacción de la pregunta y, en consecuencia, el interprete de la lectura de su tirada del I Ching le devuelve respuestas inútiles porque el enunciado de la pregunta carece de suficiente contexto emocional y honestidad.

Entonces, nada más por este punto de la auto-censura, conviene considerar la privacidad cuando hacemos uso de aplicaciones oraculares, o incluso si acudimos a un experto humano o guru para solicitar sus servicios de interpretación; en este último caso, la condición de privacidad es completamente violada. No obstante, la auto-censura es solo el daño colateral íntimo. El peligro exterior es aún peor...

Si un sitio de internet te exige registrarte y hacer login para usarlo, es porque esta manteniendo tus datos de login en una base de datos (MongoDB, PostgreSQL), con por lo menos tu correo electrónico, en el mejor de los casos. Imaginate ahora que además el sitio guarda un registro de tus consultas, con tus preguntas personalísimas y dilemas existenciales, por la "conveniencia" de tener una aplicación que te conozca y pueda hacer lecturas supuestamente más exactas, o permitirte hacer journaling de tus propias consultas. Ahora imagínate que ese sitio es hackeado y toda esa información termina en manos de hackers inescrupulosos, dispuestos a hacerla pública a menos de que pagues la extorsión.

---

## Los riesgos verdaderos de no tener privacidad

Si crees que esta posibilidad es remota y por lo tanto esto es un tema que no te afecta, piensa en la reciente vulnerabilidad, llamada PHP2Shell, que descubrieron en octubre del 2026. Para los que no saben, PHP es un lenguaje interpretado en servidores, que funciona en más del 70% de los sitios web en internet. La vulnerabilidad que descubrieron es que un atacante no autorizado puede inyectar codigo a un servidor desde afuera, y tomar el control remotamente, explotando una falla en el manejo que hace PHP en el manejo interno de su memoria. 

Esta vulnerabilidad, que ha recibido una puntuación de 9,2 de 10 según el sistema CVSS, afecta como se dijo a más del 70% de los sitios web en todo el mundo, incluida las grandes plataformas como Joomla, Drupal o WordPress, siendo esta la más común para el hospedaje de sitios web. Vamos a analizar las vulnerabilidades de este sitio respecto al PHP2Shell.

Github Pages, la plataforma sobre la cual se hospeda `elichingon.com`, no se ve afectada por este fallo de PHP. GitHub Pages es un servicio de hosting estrictamente estático: sirve archivos HTML, CSS, JS e imágenes directamente desde el repositorio.  Un archivo .php subido ahí se sirve como texto plano, no se interpreta. No hay intérprete PHP en ningún punto de la cadena. Este sitio utiliza Cloudflare como CDN/proxy, que tampoco ejecuta PHP. De hecho, la arquitectura de mi sitio fue diseñada explícitamente para prescindir de PHP y de bases de datos tradicionales de usuarios, eliminando de raíz la posibilidad de que exista un historial que hackear. Pero sobre esto volveremos más tarde.

Vamos a hablar un poquito más sobre los datos de los usuarios que la mayoria de estas páginas o aplicaciones manejan, porque puede ser más de lo que obvio, como el correo electronico, tu nombre, tu documento de identidad, etc. Para esto, vamos a clasificar los sitios o aplicaciones oraculares (del I Ching o de adivinación en general) en dos grandes categorias. Una categoría, que yo llamaré "los dinosaurios del I Ching", son aquellas páginas que se quedaron congeladas en los principios de los años 2000, como por ejemplo [Online Clarity](<https://www.onlineclarity.co.uk/>), [I Ching Online\.NET \- the Online Book of Changes](<https://www.ichingonline.net/>) y [Eclectic Energies I Ging](<https://www.eclecticenergies.com>), que no ofrecen interpretación por IA. La otra categoría de aplicaciones o sitios, a la cual llamaré los "oráculos de plástico", porque son envoltorios de IA (wrappers), producidos en serie que solo ofrecen "fast-food espiritual".

### Los dinosaurios del I Ching

Vamos a hablar primeramente de los dinosaurios del I Ching. La mayoría de estos sitios no requieren registrarse ni login para usar, con la excepción de Online Clarity, para participación en los foros. Pero su modelo de monetización se basa en el capitalismo de vigilancia, que implica tener scripts invasivos como Google Analytics para las metricas de tráfico, DoubleClick (de Google) y Media.net, que no solo rastrean por donde navegas, sino que construyen un perfil comercial de los usuarios, y los cordones sociales como Facebook pixel o los rastreadores de Meta, que vinculan el uso del oraculo con tu identidad real, tu rostro y tus relaciones personales. Así, la consulta deja de ser privada y pasa a enriquecer el perfil demográfico que las redes sociales tienen sobre ti. 

Como mencionamos, la monetización de estos sitios se basa en servir avisos publicitarios relevantes. Otra característica común es que manejan cookies que permiten hacer perfilado en las sombras (shadow profiling): identificadores de tu dispositivo/navegador y patrones de navegación. Si consultas repetidamente el I Ching sobre problemas financieros y maritales, los algorítmos infieren que estas atravesando una crisis vital y te comienzan a inundar con avisos publicitarios de consejeros, soluciones financieras, y démas cosas afines. Esto no solo es fastidioso y crea una mala experiencia de usuario, llenando el sitio de avisos publicitarios y scripts que ralentizan tu computadora. Son una falta de respeto a tu privacidad, y además te exponen a ser presa de estafas en un momento cuando estás más vulnerable.

`elichingon.com` no guarda cookies de usuarios. No las necesita porque como dije, no hay registro ni login. Para hacer analítica del trafico a mi sitio, utilizo [Umami](https://umami.is/), un recopilador open source de analitica de trafico que usa data anonima y agregada. 

A continuación les ofrezco una tabla resúmen sobre el tipo de identificadores que recolectan estos sitios dinosaurios, y cómo `elichingon.com` se desenmarca de estos. Puedes verificar esto directamente examinando el códido fuente html/js de cada sitio en tu navegador, o utilizar esta herramienta de terceros (sustituyendo el dominio al final por el del sitio que quieras auditar): [https://builtwith.com/elichingon.com](https://builtwith.com/elichingon.com).

| Tecnología de Rastreo / Privacidad | Online Clarity | I Ching Online | Eclectic Energies | El I Chingón |
| :--- | :--- | :--- | :--- | :--- |
| **Requiere Inicio de Sesión (Login)** | **Sí** (Para foros y diario de lecturas) | **No** (Pero te perfila con *cookies*) | **No** (Pero te perfila con *cookies*) | **No** (Modelo prepago / *Gift Cards* sin *cookies*) |
| **Google Analytics (Perfilado de usuarios)** | Sí (Universal & Global Tag) | Sí (GA4 & Global Tag) | No | No (Solo usa Umami, alternativa de privacidad) |
| **Monetización por Anuncios (Ads.txt)** | No | Sí (Google Direct & Ads.txt) | Sí (Google Direct & Ads.txt) | No |
| **Redes Publicitarias Externas** | Sí (Amazon Ads) | Sí (Doubleclick.net) | No | No |
| **Rastreadores de Conversión (Customer Journey)**| Sí (HockeyStack - Graba sesiones) | No | No | No |
| **Captura de Leads (Email / SMS Marketing)** | Sí (AWeber, Gravitec) | No | No | No |
| **Rastreadores de Redes Sociales** | Sí (Múltiples: Facebook, etc.) | No | No | No |
| **reCAPTCHA (Rastreo de Google Bot)** | Sí (v2) | No | No | No |


### Los oráculos de plástico

Este tipo de sitios o aplicaciones de consulta oracular se basan en un modelo de monetización que consiste en venderte lecturas oraculares facilitadas por IA. Para ser justos, yo también pretendo hacer eso, pero hay unas diferencias fundamentales que me desenmarcan completamente de entrar en esta categoría de oráculos de plástico.

Aunque estos "oráculos de plástico" tengan un diseño minimalista/moderno y te prometan que las consultas son "solo entre tú y la IA", heredan exactamente el mismo pecado original de los dinosaurios: la base de datos centralizada. Si la aplicación te pide iniciar sesión con Google o Apple, o te ofrece un "historial de lecturas", significa que tus preguntas más íntimas están siendo almacenadas en un servidor. Y como vimos con vulnerabilidades como PHP2Shell, donde hay una base de datos con información sensible, hay un peligro inminente de exposición.

A esto le agregamos otro riesgo, porque la inmensa mayoría operan como aplicaciones que debes instalar desde la App Store o Google Play. Cuando instalas una de estas apps en tu teléfono, no solo estás descargando un chat oracular; estás metiendo un caballo de Troya en tu bolsillo.

Para que estas aplicaciones funcionen y moneticen, los desarrolladores las empaquetan con algo llamado SDKs (Kits de Desarrollo de Software) de terceros. Son pequeños módulos de código incrustados, pertenecientes a gigantes como Meta o Google, que literalmente "ven" todas las interacciones en tu teléfono. Recopilan telemetría en segundo plano: saben a qué hora abres la app, cuánto tiempo la usas y asocian esa actividad al identificador único de tu dispositivo. El sistema operativo móvil es un ecosistema diseñado para la vigilancia, y estas apps son sus sensores.

Mi sitio se diferencia de los oráculos de plástico en que, aunque también existiendo como app que puedes descargar en tu teléfono, es en realidad un Progressive Web App (PWA), que es un tecnicismo que se usa para decir que lo instalas desde el navegador de tu teléfono como un acceso directo a la página web [https://elichingon.com](https://elichingon.com) y lo ves en una versión del navegador sin los botones del navegador. Es decir, `elichingon.com` usado como una PWA no recopila ninguna información de tu teléfono porque mi sitio web tampoco lo hace. Así de sencillo.

Y ahora entramos en el territorio más oscuro de la IA centralizada: el vampirismo semántico. 

La mayoría de estas aplicaciones no procesan la inteligencia artificial en tu teléfono, ni en entornos seguros; actúan como simples intermediarios que toman tu texto y lo envían a los servidores centralizados de gigantes como OpenAI o Anthropic, a través de un API que permite la comunicación entre su sitio o app y los proveedores de servicio de IA.

Si lees la letra pequeña de los términos de uso de muchos de estos servicios (o de las capas de consumidor que usan muchos desarrolladores para ahorrar costos), descubrirás que se reservan el derecho de utilizar las interacciones de los usuarios para "entrenar y mejorar" sus futuros modelos.

En ciberseguridad, esto se conoce como Memorización de Datos. Los modelos de lenguaje no guardan archivos en una carpeta; comprimen el texto que leen directamente en sus conexiones neuronales. Si le confiesas a la IA un detalle íntimo sobre tu divorcio, tu empresa o tu salud, la IA absorbe esa confesión. Y esto nos lleva a la vulnerabilidad más aterradora de la inteligencia artificial moderna: los jailbreaks o ataques de extracción de datos.

Los investigadores de seguridad han demostrado repetidamente que, mediante el uso de ciertos comandos o indicaciones diseñadas para saturar o confundir a la IA, es posible obligarla a "escupir" los datos reales y privados con los que fue entrenada. Tu secreto personalísimo, que creías resguardado por una contraseña, podría terminar siendo generado palabra por palabra en la pantalla de un extraño al otro lado del mundo que logró hackear las defensas semánticas del modelo.

Para que El I Chingón pudiera ofrecer inteligencia artificial sin convertirse en un vampiro semántico, la arquitectura técnica tenía que ser radicalmente diferente. La solución fue prescindir por completo de los servidores tradicionales y de las APIs de consumo masivo, utilizando Edge AI (Inteligencia Artificial en el Borde) a través de la infraestructura de Cloudflare.

En lugar de enviar tus secretos a una base de datos o a una corporación que quiere entrenar algoritmos, tu consulta en elichingon.com viaja hacia un Cloudflare Worker. Este es un entorno de ejecución efímero situado en un centro de datos geográficamente cercano a ti.

La diferencia en privacidad es absoluta y está garantizada por contrato: la arquitectura de Cloudflare prohíbe explícitamente el uso de los datos de los clientes o de los queries (consultas) para entrenar modelos de IA. Es un sandbox cerrado donde ningún dato sale y alimenta el entrenamiento de las IAs.

Cuando haces una pregunta, el servidor en el borde se enciende en milisegundos, ensambla tu consulta, procesa la interpretación hermenéutica usando un modelo de lenguaje seguro, genera tu respuesta y, en el mismo instante en que se cierra la conexión, el aislado de memoria se destruye. La memoria RAM se vacía. Ni mi sitio, ni Cloudflare, ni la IA guardamos un registro de lo que preguntaste, simplemente porque el sistema fue diseñado con amnesia estructural. Es matemáticamente ciego a tu identidad e incapaz de recordar tus secretos.

---

## Otros riesgos (y no son solo los hackers)

Hemos mencionado la posibilidad que los delincuentes tengan acceso a tus datos personales, que es una posibilidad muy real, dada la ubicuidad del PHP en casi todos los servidores y sitios de hospedaje, pero la cosa no termina ahi.

Si piensas que el único peligro proviene de cibercriminales encapuchados que quieren extorsionarte, y que los gobiernos y las grandes corporaciones están ahí para protegerte, que Dios te ampare: eres demasiado ingenuo.

Los hackers roban tu información para sacarte dinero rápido. Las corporaciones y los gobiernos la recolectan y la exigen para algo mucho más peligroso: restringir tu libertad, perfilarte y tener el poder de escoñetarte si en algún momento te sales de la línea que ellos marcan.

![Panóptico](panopticon.webp "Panóptico")

Hablemos del control financiero y la vigilancia de Estado. Ya hemos visto cómo los gobiernos y las élites financieras han asomado la idea de las CBDC (Monedas Digitales de Bancos Centrales, por sus siglas en inglés). Y aunque en algunos lugares lo han puesto en moratoria por el rechazo público, no te engañes: la idea va.

Las CBDC no son simplemente "dinero digital" (eso ya lo usas con tu tarjeta de débito actual); son dinero programable. Es dinero con un código de barras atado a tu identidad legal, que le permite a un burócrata dictar dónde, cuándo y en qué te lo puedes gastar.

Imagínate un escenario que ya dejó de ser ciencia ficción: el gobierno de turno decide qué es moral, qué es aceptable o qué es "útil" para la sociedad. Imagínate que un día decidan que consultar a un oráculo, estudiar textos antiguos o buscar respuestas fuera de la narrativa oficial es "subversivo", o simplemente decidan bloquearte las transacciones porque consideran que estás gastando tu dinero en mariqueras.

Si tu identidad está atada a tu historial de navegación, o si el oráculo que usas te obliga a pagar con una tarjeta de crédito o una cuenta bancaria tradicional que deja un rastro imborrable en un servidor centralizado, estás a un solo clic de ser censurado, cancelado o bloqueado financieramente.

El riesgo definitivo de no tener privacidad no es que un delincuente te robe la tarjeta; es perder la soberanía sobre tu propia mente y tu propio dinero a manos de las instituciones que supuestamente velan por ti, pero que al fín del día también son delincuentes de cuello blanco.

---

## La última trampa: El secuestro financiero

Queda un último riesgo por cubrir. Si El I Chingón no te cobra mercantilizando tu dolor con rastreadores publicitarios (como los dinosaurios) ni te cobra robando tus secretos para entrenar IAs (como los oráculos de plástico), tiene que cobrar dinero real por las consultas. Mantener una infraestructura segura y privada tiene un costo, y además, es justo que gane algo por aportar valor a la gente, ¿no?

El problema no es pagar; el problema es cómo la industria actual te obliga a pagar.

Las aplicaciones modernas te empujan casi exclusivamente a un modelo de suscripción atado a tu tarjeta de crédito, tu cuenta de PayPal o tu Apple ID/Google Pay. Cuando pagas así, pierdes el último reducto de privacidad: tu anonimato financiero. Tu banco, las corporaciones tecnológicas y, por extensión, el Estado, saben exactamente que estás gastando dinero en un oráculo.

Pero más allá de la privacidad, el modelo de suscripciones es una aberración de usabilidad, especialmente para una herramienta como esta. Hay un choque fundamental entre la naturaleza milenaria del I Ching y el modelo de negocio extractivo de Silicon Valley.

Para algunas personas, el I Ching es una instancia de último recurso; algo a lo que acuden con extrema seriedad quizás una o dos veces al año, en medio de una crisis existencial o una encrucijada crítica. Para otras, que se lo toman con la misma seriedad, es una herramienta de uso diario para estudiar y producir sincronicidades en su vida.

Entonces, ¿por qué una aplicación tendría que condicionar tu frecuencia de uso con una suscripción mensual? ¿Por qué tienes que atarte a un pago recurrente por algo que quizás no vas a usar el mes que viene? Lo que termina ocurriendo es que pagas por meses que no usas, o peor aún, te sientes obligado a "sacarle el jugo" a la suscripción haciendo preguntas triviales que socavan el mismo acto de una verdadera consulta oracular.

A esto le sumamos lo que en diseño web se conoce como el "efecto Hotel California": puedes entrar cuando quieras, pero nunca puedes salir. Estas plataformas utilizan patrones oscuros para esconder el botón de cancelación o te aplican renovaciones automáticas sorpresa. En las reseñas de la App Store de estos oráculos de plástico, la queja número uno expone lo defectuoso y hostil que es este software: "Esta aplicación me sigue pidiendo que renueve, ¡pero ya pagué y no me deja cancelar!". Es un sistema diseñado para exprimir tu tarjeta mes a mes.

---

## El modelo prepago: Tokens y Billeteras Web3

Para que la privacidad de El I Chingón sea absoluta y la experiencia de usuario sea honesta, el cordón umbilical financiero tenía que cortarse. Por eso implementé un sistema de Gift Cards (vouchers de prepago).

Funciona exactamente igual que una ficha en un casino o el dinero en efectivo- es dinero al portador. Tú compras tu código, lo introduces sólo cuando vas a hacer una consulta y sin necesidad de suministrar ningún otro dato, se te descuenta esa consulta del saldo de tu token, y se acabó. Si te toma tres días o tres años gastar tus créditos, es asunto tuyo. No hay suscripciones, no hay "renovaciones automáticas" y no tienes que pelear con un bot de atención al cliente para darte de baja. El fin del saldo es el fin del contrato. Yo solo puedo esperar que el oráculo te sea verdaderamente útil para que me quieras seguir comprando vouchers de prepago, y corriendo la voz entre tus familiares y amigos, pero tampoco te obligo. Nada obligado es bueno.

Más importante aún, este sistema de códigos alfanuméricos me permite ofrecer métodos de pago totalmente ciegos. Próximamente, podrás comprar tus Gift Cards utilizando redes descentralizadas, como la Lightning Network (Bitcoin) o redes de capa 2 (L2) con criptomonedas estables como USDT/USDC. Para los usuarios, esto significa transar sin revelar su identidad legal y sin dejar cargos rastreables en sus estados de cuenta bancarios. 

Mi base de datos de saldos solo tiene dos columnas operativas: un código de letras y números al azar, y cuántos créditos le quedan. El servidor no sabe quién compró el código. Mi decisión de modularizar el sistema en un riel de pagos independiente del mecanismo de consumo por consultas hace que esta privacidad radical sea posible.

---

## La Prueba Institucional: Cloudflare y la Amnesia por Contrato

He diseñado este sistema porque creo que la adivinación y el autoanálisis deben ser espacios sagrados, no granjas de datos para algoritmos de corporaciones. Pero no tienes que confiar ciegamente en mi palabra (nada de "Trust me bro").  Mi promesa de privacidad está respaldada por contratos a nivel de infraestructura y por la transparencia de mi código.

Al utilizar la arquitectura Serverless (sin servidor) de Cloudflare para procesar las consultas en el borde de la red, El I Chingón hereda automáticamente sus estrictos Términos de Servicio empresariales (ver el documento citado en las referencias al final de este artículo). A diferencia de las aplicaciones de consumidor que usan tus datos para mejorar sus modelos, los acuerdos de Cloudflare prohíben explícitamente el uso de las consultas de los usuarios (payloads) para el entrenamiento de Inteligencia Artificial. La protección contra el vampirismo semántico no es solo una buena intención mía; es una garantía legal blindada de la red que transporta tus datos.

Incluso si una agencia gubernamental irrumpiera mañana con una orden judicial para averiguar qué preguntó un usuario, el sistema opera bajo el principio de Ceguera Institucional. No puedo filtrar, vender ni entregar a las autoridades aquello que mi infraestructura está matemáticamente diseñada para no retener.

Además, he hecho pública la lógica de mi "aduana". He publicado una implementación de referencia de mis servidores en la nube en [https://github.com/ichingon/ichingon.github.io/blob/main/backend-reference/worker.js](https://github.com/ichingon/ichingon.github.io/blob/main/backend-reference/worker.js). Cualquier desarrollador puede auditar la arquitectura central de mis aplicaciones y verificar que la variable que contiene tu pregunta íntima jamás se inserta en una base de datos. Se procesa en la memoria RAM, genera tu lectura a través de nuestro protocolo CSHC, y se destruye en el vacío en milisegundos.

Tu oráculo debería ser una fuente de sabiduría a la que acudes, no tu espía, ni tu delator, ni tu carcelero financiero.

---

## Referencias

* Cloudflare. (s.f.). Data usage. Cloudflare Docs. Recuperado el 24 de octubre de 2026, de https://developers.cloudflare.com/workers-ai/platform/data-usage/

* PHP2Shell. (23 de octubre de 2026). En Wikipedia, la enciclopedia libre. [https://es.wikipedia.org/wiki/PHP2Shell](https://es.wikipedia.org/wiki/PHP2Shell)