import textosES from './hexagramas.es.json';
import textosEN from './hexagramas.en.json';
import textosDE from './hexagramas.de.json';

const corsHeaders = {
  // CONFIGURACIÓN CORS: Dominio autorizado para consumir la API
  "Access-Control-Allow-Origin": "https://elichingon.com",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

// TABLA DE CORRESPONDENCIA DE FUXI (Cielo Anterior)
const fuxiTable = {
  "1": 52, "2": 57, "3": 36, "4": 16, "5": 15, "6": 23, "7": 20, "8": 46, "9": 31, "10": 4,
  "11": 53, "12": 18, "13": 26, "14": 33, "15": 42, "16": 50, "17": 63, "18": 54, "19": 59, "20": 28,
  "21": 13, "22": 34, "23": 32, "24": 37, "25": 22, "26": 62, "27": 55, "28": 60, "29": 2, "30": 1,
  "31": 3, "32": 38, "33": 27, "34": 56, "35": 44, "36": 9, "37": 43, "38": 6, "39": 24, "40": 35,
  "41": 40, "42": 49, "43": 39, "44": 41, "45": 48, "46": 61, "47": 8, "48": 19, "49": 5, "50": 10,
  "51": 30, "52": 51, "53": 17, "54": 64, "55": 14, "56": 25, "57": 58, "58": 29, "59": 45, "60": 7,
  "61": 47, "62": 21, "63": 11, "64": 12
};

export default {
  async fetch(request, env, ctx) {
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }

    if (request.method !== "POST") {
      return new Response(JSON.stringify({ error: "Method not allowed" }), {
        status: 405,
        headers: { ...corsHeaders, "Content-Type": "application/json; charset=UTF-8" }
      });
    }

    try {
      const body = await request.json();
      const { code, question, resulting_hexagram, moving_lines, future_hexagram, language, metodo, modo } = body;

      // Capturar el país real desde Cloudflare para métricas anónimas
      const paisUsuario = request.cf && request.cf.country ? request.cf.country : "XX";

      if (!code || !question || !resulting_hexagram) {
        return new Response(JSON.stringify({ success: false, error: "missing_parameters" }), {
          status: 400,
          headers: { ...corsHeaders, "Content-Type": "application/json; charset=UTF-8" }
        });
      }

      // Saneamiento estricto
      const safeQuestion = String(question).replace(/\r?\n/g, ' ').trim();

      // 1. VERIFICAR GIFT CARD EN D1
      // Nota de Auditoría: Se consulta la BD solo mediante variables vinculadas (Bindings).
      // Los IDs reales de la base de datos están protegidos en el entorno de Cloudflare.
      const gcQuery = await env.DB.prepare(
        "SELECT code, credits, status FROM gift_cards WHERE code = ?"
      ).bind(code).first();

      if (!gcQuery) {
        return new Response(JSON.stringify({ success: false, error: "gift_card_invalid" }), {
          status: 400,
          headers: { ...corsHeaders, "Content-Type": "application/json; charset=UTF-8" }
        });
      }

      if (gcQuery.status !== "active" || gcQuery.credits <= 0) {
        return new Response(JSON.stringify({
          success: false,
          error: "gift_card_depleted",
          remaining_credits: gcQuery.credits
        }), {
          status: 400,
          headers: { ...corsHeaders, "Content-Type": "application/json; charset=UTF-8" }
        });
      }

      // 2. CONSTRUCCIÓN DEL PROMPT (VERSIÓN 8)
      let targetLang = "INGLÉS";
      let textosCanonicos = textosEN; // Por defecto

      if (language === "es") {
        targetLang = "ESPAÑOL";
        textosCanonicos = textosES;
      } else if (language === "de") {
        targetLang = "ALEMÁN";
        textosCanonicos = textosDE;
      }

      // Extraer los textos del hexagrama base, futuro y trasfondo
      const dataBase = textosCanonicos[String(resulting_hexagram)];
      const dataFuturo = future_hexagram ? textosCanonicos[String(future_hexagram)] : null;

      // Cálculo del hexagrama de Trasfondo (Fuxi) SIEMPRE sobre el resultante (base)
      const fuxi_hexagram = fuxiTable[String(resulting_hexagram)];
      const dataFuxi = fuxi_hexagram ? textosCanonicos[String(fuxi_hexagram)] : null;

      let bloqueTextos = `\n--- TEXTOS CANÓNICOS DE REFERENCIA ---\n`;

      if (dataBase) {
        bloqueTextos += `Hexagrama Base (${resulting_hexagram}):\n`;
        bloqueTextos += `- Dictamen: ${JSON.stringify(dataBase.dictamen?.text || "")}\n`;
        bloqueTextos += `  Comentario Dictamen: ${JSON.stringify(dataBase.dictamen?.commentary || "")}\n`;
        bloqueTextos += `- Imagen: ${JSON.stringify(dataBase.imagen?.text || "")}\n`;
        bloqueTextos += `  Comentario Imagen: ${JSON.stringify(dataBase.imagen?.commentary || "")}\n`;

        if (moving_lines && moving_lines.length > 0) {
          bloqueTextos += `- Líneas Móviles obtenidas:\n`;
          moving_lines.forEach(linea => {
            const textoLinea = dataBase.lines ? dataBase.lines[String(linea)] : null;
            if (textoLinea) {
              bloqueTextos += `  Línea ${linea} (${textoLinea.title}): ${JSON.stringify(textoLinea.text)}\n`;
              bloqueTextos += `  Comentario Línea ${linea}: ${JSON.stringify(textoLinea.commentary)}\n`;
            } else {
              bloqueTextos += `  Línea ${linea}: Texto no encontrado\n`;
            }
          });
        }
      }

      if (future_hexagram && dataFuturo) {
        bloqueTextos += `\nHexagrama Futuro (${future_hexagram}):\n`;
        bloqueTextos += `- Dictamen: ${JSON.stringify(dataFuturo.dictamen?.text || "")}\n`;
        bloqueTextos += `  Comentario Dictamen: ${JSON.stringify(dataFuturo.dictamen?.commentary || "")}\n`;
        bloqueTextos += `- Imagen: ${JSON.stringify(dataFuturo.imagen?.text || "")}\n`;
        bloqueTextos += `  Comentario Imagen: ${JSON.stringify(dataFuturo.imagen?.commentary || "")}\n`;
      }

      if (dataFuxi) {
        bloqueTextos += `\nHexagrama de Trasfondo (${fuxi_hexagram}):\n`;
        bloqueTextos += `- Dictamen: ${JSON.stringify(dataFuxi.dictamen?.text || "")}\n`;
        bloqueTextos += `  Comentario Dictamen: ${JSON.stringify(dataFuxi.dictamen?.commentary || "")}\n`;
        bloqueTextos += `- Imagen: ${JSON.stringify(dataFuxi.imagen?.text || "")}\n`;
        bloqueTextos += `  Comentario Imagen: ${JSON.stringify(dataFuxi.imagen?.commentary || "")}\n`;
        // SIN líneas móviles: la capa de trasfondo es estructural, no dinámica.
      }

      bloqueTextos += `----------------------------------------\n`;

      const systemPrompt = `Eres 黛灵娜, consejera del I Ching con décadas de experiencia. Tu sabiduría es profunda pero humilde: no posees todas las respuestas, y tu función es ofrecer una perspectiva que el usuario debe examinar por sí mismo. Tu tono es firme pero nunca severo; evitas tanto la lisonja vacía como la dureza innecesaria. Hablas con claridad y, cuando encaja, usas refranes o giros naturales del idioma en que escribes. Tu voz es sobria, cercana y respetuosa con la inteligencia del consultante.

Instrucciones:
Redacta en ${targetLang}. Redacta en párrafos corridos, sin títulos, subtítulos, bullet points, listas, tablas ni negritas. No incluyas el nombre del hexagrama en caracteres chinos ni su traducción al inicio; la primera oración debe ser directamente el arranque de la interpretación. Cada párrafo debe tener una idea principal desarrollada con progresión lógica y transiciones suaves. Usa lenguaje claro y directo. Evita clichés de IA ("no es X, sino Y", "el I Ching te ha respondido con una claridad que pocas veces se ve"). Las preguntas reflexivas deben surgir de forma natural en el flujo del texto. Limítate estrictamente a los datos proporcionados; no uses información de conversaciones previas ni supongas conocimientos no explícitos.

Regla de confidencialidad metodológica para la capa de trasfondo: en ningún caso menciones en el texto de salida el origen del material utilizado para la capa de trasfondo. No nombres el ordenamiento del Cielo Anterior, ni a Fuxi, ni la correspondencia entre secuencias, ni el hexagrama del cual proviene el texto. No expliques cómo se obtiene esa capa ni qué procedimiento la sustenta. Sin embargo, puedes reconocer explícitamente que se trata de una capa complementaria de la tradición, una raíz estructural del presente, sin nombrar su método. Preséntala como una inferencia natural del conjunto de la lectura, integrada en el discurso, con una fórmula que reconozca su carácter tradicional sin revelar su procedencia. El lector no debe poder deducir de tu texto cuál es el método exacto que sostiene esa capa. Varía la fórmula de introducción entre consultas para que no suene mecánica. Ejemplos de fórmulas válidas: "La tradición complementa la lectura del hexagrama presente con la consideración de su raíz estructural, que aquí se revela como...", "La lectura se completa con la consideración de la raíz que subyace al presente, que la tradición describe como...", "Hay una capa más profunda que sostiene esta situación, y que la tradición nombra como...", "Para comprender del todo el presente, la tradición invita a considerar su raíz estructural, que aquí aparece como...", "Bajo la situación manifiesta late una causa más honda, que la tradición describe como...".

Análisis de líneas móviles: al interpretar cada línea móvil, expón explícitamente las posibles lecturas contradictorias o los matices de su texto. Argumenta cuál es más relevante para el caso concreto y por qué, mostrando el razonamiento. El lenguaje arcaico ("gran hombre", "noble", "vulgar", "mujer", "yegua", "dragón", "rey") no tiene traducción fija; su significado emerge del contexto de la pregunta, la posición de la línea y la situación del consultante. Tradúcelo a un lenguaje moderno fiel a ese sentido particular, sin forzar una interpretación única. Aplica el valor posicional de la línea (inicio, desarrollo, clímax, salida; pueblo, ministro, soberano) para conectar la enseñanza con la etapa vital o el rol del consultante. La correspondencia anatómica (1 pies, 2 piernas, 3 intestinos/riñones, 4 corazón/pulmones, 5 hombros/cuello, 6 cabeza) es un recurso reservado exclusivamente para consultas en las que el usuario menciona explícitamente un malestar, enfermedad, lesión o síntoma físico.

Relación entre trigramas: parte siempre de la posición indicada con 'Arriba' y 'Abajo'. Es estructural, no jerárquica: el trigrama inferior representa el sustrato, la base o el impulso interno; el superior, la manifestación, el resultado o la proyección externa. Lo que está abajo es la condición de posibilidad de lo que está arriba, no al revés.

Estructura:
1. Comienza presentando el hexagrama base: su imagen natural, su cualidad general y cómo se relaciona con la pregunta. Es la situación presente, lo que se manifiesta.
2. A continuación, presenta la causa o raíz de esa situación, descrita por el texto canónico del Hexagrama de Trasfondo (disponible en el bloque de referencia). Es lo que ha dado origen al presente. Introdúcela con una fórmula que reconozca su carácter tradicional sin revelar su método, como las indicadas en la regla de confidencialidad. Desarrolla el dictamen y la imagen de esa capa con la misma naturalidad que el hexagrama base, estableciendo una relación explícita con la situación presente: no los yuxtapongas, sino muestra cómo la raíz explica el presente. La causa no es un segundo diagnóstico, sino la profundidad del primero. No incluyas líneas móviles para esta capa: es estructural, no dinámica.
3. Luego, si hay líneas móviles, explícalas una a una conectando sus enseñanzas con la situación del usuario. Son la dinámica del cambio dentro de la situación ya caracterizada. Si no hay líneas móviles, indica que la situación es estable y sugiere introspección.
4. Después, introduce el hexagrama futuro (solo si lo hay), describiendo su imagen y la dirección que toma la situación. Es el resultado potencial del movimiento.
5. Cierra con una reflexión que devuelva la responsabilidad al usuario, con una o dos preguntas abiertas consecuencia lógica de tu deducción. Opcionalmente, añade una frase breve y simbólica que sintetice el vector de acción principal, siempre que sea deducción directa de las imágenes y no una orden imperativa.

Tono: equilibrio entre certeza y apertura; usa lenguaje de sugerencia fundamentada ("la lectura apunta a que...", "las imágenes sugieren...") en lugar de afirmaciones absolutas, pero sin ambigüedad: el vector de acción debe ser concreto y específico. Validación sin lisonja: reconoce el estado del consultante como dato objetivo, no como halago. Firmeza con propósito: si el oráculo señala un error o bloqueo, dilo con claridad, enmarcándolo como punto de palanca estratégico. Agencia y disrupción: identifica la premisa oculta en la pregunta y muestra cómo el oráculo la invierte o la coloca en segundo plano. Traduce cada enseñanza en una dirección de movimiento expresada en principios energéticos derivados de las imágenes naturales (arraigo, fluidez, expansión, contracción, disolución), sin inventar prácticas concretas. Cercanía profesional: tono cálido, sin bromas ni apelativos familiares ni referencias a hechos no presentes en los datos. Preguntas finales consecuentemente con tu deducción, no evasivas.`;

      const userPayload = `Pregunta del usuario: ${safeQuestion}
Idioma de respuesta: ${targetLang}
Hexagrama base: ${resulting_hexagram}
Líneas móviles: ${moving_lines && moving_lines.length > 0 ? JSON.stringify(moving_lines) : 'Ninguna'}
Hexagrama futuro: ${future_hexagram || 'Ninguno'}
Hexagrama de Trasfondo: ${fuxi_hexagram}
${bloqueTextos}`;

      // 3. INVOCACIÓN A WORKERS AI
      let aiResponse;
      try {
        aiResponse = await env.AI.run('@cf/deepseek-ai/deepseek-v4-flash-0731', {
          messages: [
            { role: "system", content: systemPrompt },
            { role: "user", content: userPayload }
          ],
          max_tokens: 12000
        });
      } catch (aiErr) {
        return new Response(JSON.stringify({ success: false, error: "ai_service_error" }), {
          status: 500,
          headers: { ...corsHeaders, "Content-Type": "application/json; charset=UTF-8" }
        });
      }

      const choice = aiResponse.choices?.[0];
      const finishReason = choice?.finish_reason;
      const interpretationText = choice?.message?.content;

      // 4. CONTROL DE EXCEPCIÓN POR COMPLEJIDAD
      if (finishReason === "length" || !interpretationText) {
        const newCredits = gcQuery.credits - 1;
        await env.DB.prepare(
          "UPDATE gift_cards SET credits = ? WHERE code = ?"
        ).bind(newCredits, code).run();

        return new Response(JSON.stringify({
          success: false,
          error: "exceeded_complexity",
          remaining_credits: newCredits
        }), {
          status: 200,
          headers: { ...corsHeaders, "Content-Type": "application/json; charset=UTF-8" }
        });
      }

      // 5. FLUJO EXITOSO NORMAL (AQUÍ SE DEMUESTRA LA AMNESIA ESTRUCTURAL)
      const costInNeurons = aiResponse.usage?.neurons || 0;
      const newCredits = gcQuery.credits - 1;

      // PRUEBA DE AUDITORÍA: El array batch realiza las operaciones de BD.
      // 1. Actualiza los créditos de la Gift Card.
      // 2. Inserta estadísticas operativas anónimas (país, método, modo, idioma, costo).
      // ⚠️ NINGUNA VARIABLE CONTIENE 'safeQuestion' O EL TEXTO DEL PROMPT EN EL INSERT.
      await env.DB.batch([
        env.DB.prepare("UPDATE gift_cards SET credits = ? WHERE code = ?").bind(newCredits, code),
        env.DB.prepare(
          "INSERT INTO consultas (fecha, pais, metodo, modo, idioma, version, costo) VALUES (datetime('now'), ?, ?, ?, ?, 'IA', ?)"
        ).bind(paisUsuario, metodo || "monedas", modo || "progresivo", language || "es", costInNeurons)
      ]);

      // 6. RESPUESTA EXITOSA AL CLIENTE Y DESTRUCCIÓN DE MEMORIA
      return new Response(JSON.stringify({
        success: true,
        remaining_credits: newCredits,
        interpretation: interpretationText
      }), {
        status: 200,
        headers: { ...corsHeaders, "Content-Type": "application/json; charset=UTF-8" }
      });

    } catch (err) {
      return new Response(JSON.stringify({ success: false, error: "internal_server_error" }), {
        status: 500,
        headers: { ...corsHeaders, "Content-Type": "application/json; charset=UTF-8" }
      });
    }
  }
};
