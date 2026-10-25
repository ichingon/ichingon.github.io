---
title: "Privatsphäre laut El I Chingón - warum das dein verdammtes Problem ist"
date: 2026-10-22
author: "Dài Líng Nà (黛灵娜)"
showAuthor: true
showAuthorBottom: true
showFooterAuthor: true
tags: ["Das Tao des Content Creators"]
description: "Erfahre, warum Privatsphäre bei einer Orakelbefragung lebenswichtig ist und wie El I Chingón deine Geheimnisse schützt."
summary: "Erfahre, warum Privatsphäre in einer Orakel-App kein Luxus, sondern eine Notwendigkeit ist, und wie wir elichingon.com mit struktureller Amnesie und blinden Zahlungen gebaut haben, um deine Geheimnisse abzuschirmen."
draft: false
---

Im [Whitepaper meiner Anwendung]({{< relref "articulos/i-chingon-whitepaper" >}}), in dem ich über mein Protokoll des Constrained Stochastic Hermeneutic Computing (CSHC) spreche, erkläre ich, dass radikale Privatsphäre einer der Grundpfeiler meines Protokolls ist. In diesem Artikel werde ich dem normalen Nutzer erklären, warum das so wichtig ist, wie sich El I Chingón in dieser Hinsicht von anderen Orakel-Websites oder -Apps unterscheidet und wie du, ohne dich in viel technisches Fachjargon zu verstricken, die Privatsphäre von El I Chingón oder einer dieser Seiten überprüfen kannst.

---

## Der Mythos von "Ich habe nichts zu verbergen"

![Dài Líng Nà agiert außerhalb des digitalen Panoptikums. Dein Orakel sollte nicht dein Spion sein.](featured.jpg "Dài Líng Nà agiert außerhalb des digitalen Panoptikums. Dein Orakel sollte nicht dein Spion sein.")

Es ist besorgniserregend zu sehen, wie viele Menschen den Sicherheits- und Datenschutzrisiken im Internet gegenüber blind sind. Anscheinend gehen viele davon aus, dass Privatsphäre nur etwas für Kriminelle oder Hacker ist, und da sie nicht in Verbrechen verwickelt sind, haben sie nichts zu verbergen und daher ist Privatsphäre für sie irrelevant. Ein fataler Irrtum – Privatsphäre ist für jeden wichtig und ist (oder sollte) ein grundlegendes, universelles Menschenrecht sein.

Fangen wir mit der Natur einer Orakelbefragung an. Eine Orakelbefragung ist standardmäßig ein sehr privater Akt, wenn man bedenkt, wie persönlich einige Fragen von Leuten sein können, die Beziehungsprobleme durchmachen, in peinlichen Situationen stecken oder unaussprechliche Gedanken hegen. Damit will ich offensichtlich nicht sagen, dass das I-Ging nur für diese [Art von Fragen]({{< relref "articulos/que-podemos-preguntar" >}}) nützlich ist. Aber da beim I-Ging der Fragesteller ein grundlegender und untrennbarer Teil des Systems aus Fragesteller, Orakel und Realität ist, driften viele Fragen, die wir dem I-Ging stellen, unweigerlich in hochpersönliche Themen ab. Und deshalb wollen wir nicht, dass diese Informationen in andere Hände geraten oder von anderen Augen gelesen werden.

Aber es gibt auch das Thema der Wirksamkeit des Orakels. Wenn wir bewusst oder unbewusst vermuten, dass die Privatsphäre der Orakelbefragung kompromittiert ist, kann ein sehr schädliches Phänomen für die Wirksamkeit der I-Ging-Lesungen auftreten: **Selbstzensur**. Der Fragesteller hört auf, die Fragen zu stellen, die ihm wirklich wichtig sind, beschönigt seine Ängste bei der Formulierung der Frage und als Konsequenz liefert der Interpret seines I-Ging-Wurfs nutzlose Antworten, weil es der Fragestellung an ausreichendem emotionalen Kontext und Ehrlichkeit mangelt.

Alleine schon wegen dieses Punktes der Selbstzensur lohnt es sich also, die Privatsphäre zu berücksichtigen, wenn wir Orakel-Anwendungen nutzen, oder auch wenn wir uns an einen menschlichen Experten oder Guru wenden, um seine Interpretationsdienste in Anspruch zu nehmen; in letzterem Fall wird die Bedingung der Privatsphäre komplett verletzt. Dennoch ist die Selbstzensur nur der intime Kollateralschaden. Die Gefahr von außen ist noch schlimmer...

Wenn eine Website verlangt, dass du dich registrierst und einloggst, um sie zu nutzen, liegt das daran, dass sie deine Login-Daten in einer Datenbank (MongoDB, PostgreSQL) speichert, im besten Fall mit mindestens deiner E-Mail-Adresse. Stell dir nun vor, dass die Seite auch ein Protokoll deiner Befragungen mit deinen höchstpersönlichen Fragen und existenziellen Dilemmata speichert, wegen der "Bequemlichkeit", eine Anwendung zu haben, die dich kennt und angeblich genauere Lesungen liefern kann, oder um dir das Führen eines Tagebuchs über deine eigenen Befragungen zu ermöglichen. Stell dir nun vor, dass diese Seite gehackt wird und all diese Informationen in die Hände skrupelloser Hacker fallen, die bereit sind, sie zu veröffentlichen, es sei denn, du zahlst das Lösegeld.

---

## Die wahren Risiken fehlender Privatsphäre

Wenn du denkst, dass diese Möglichkeit abwegig ist und dich das Thema daher nicht betrifft, denk an die kürzliche Schwachstelle namens PHP2Shell, die im Oktober 2026 entdeckt wurde. Für diejenigen, die es nicht wissen: PHP ist eine serverseitig interpretierte Sprache, die auf über 70 % der Websites im Internet läuft. Die entdeckte Schwachstelle besteht darin, dass ein unbefugter Angreifer von außen Code in einen Server einschleusen und die Kontrolle aus der Ferne übernehmen kann, indem er einen Fehler in der Art und Weise ausnutzt, wie PHP mit seinem internen Speicher umgeht.

Diese Schwachstelle, die laut CVSS-System eine Punktzahl von 9,2 von 10 erhalten hat, betrifft wie erwähnt über 70 % der Websites weltweit, einschließlich großer Plattformen wie Joomla, Drupal oder WordPress, wobei letztere am häufigsten für das Website-Hosting verwendet wird. Analysieren wir die Schwachstellen dieser Website in Bezug auf PHP2Shell.

Github Pages, die Plattform, auf der `elichingon.com` gehostet wird, ist von diesem PHP-Fehler nicht betroffen. GitHub Pages ist ein strikt statischer Hosting-Service: Er liefert HTML-, CSS-, JS-Dateien und Bilder direkt aus dem Repository aus. Eine dort hochgeladene .php-Datei wird als reiner Text ausgeliefert, sie wird nicht interpretiert. Es gibt an keinem Punkt der Kette einen PHP-Interpreter. Diese Website nutzt Cloudflare als CDN/Proxy, was ebenfalls kein PHP ausführt. Tatsächlich wurde die Architektur meiner Website explizit entworfen, um auf PHP und traditionelle Benutzerdatenbanken zu verzichten und somit die Möglichkeit einer hackbaren Historie von Grund auf zu beseitigen. Aber darauf kommen wir später zurück.

Lass uns ein bisschen mehr über die Benutzerdaten sprechen, die die meisten dieser Seiten oder Anwendungen verarbeiten, denn es kann mehr als das Offensichtliche wie deine E-Mail, dein Name, dein Ausweis usw. sein. Dazu werden wir Orakel-Seiten oder -Anwendungen (I-Ging oder Wahrsagerei im Allgemeinen) in zwei große Kategorien einteilen. Eine Kategorie, die ich "die I-Ging-Dinosaurier" nenne, sind jene Seiten, die Anfang der 2000er Jahre eingefroren sind, wie zum Beispiel [Online Clarity](<https://www.onlineclarity.co.uk/>), [I Ching Online.NET - the Online Book of Changes](<https://www.ichingonline.net/>) und [Eclectic Energies I Ging](<https://www.eclecticenergies.com>), die keine KI-Interpretation anbieten. Die andere Kategorie von Anwendungen oder Seiten werde ich die "Plastik-Orakel" nennen, weil es in Serie produzierte KI-Wrapper sind, die nur "spirituelles Fast-Food" anbieten.

### Die I-Ging-Dinosaurier

Sprechen wir zuerst über die I-Ging-Dinosaurier. Die meisten dieser Seiten erfordern keine Registrierung oder kein Login zur Nutzung, mit Ausnahme von Online Clarity für die Teilnahme an den Foren. Aber ihr Monetarisierungsmodell basiert auf Überwachungskapitalismus, was bedeutet, dass sie invasive Skripte wie Google Analytics für Traffic-Metriken, DoubleClick (von Google) und Media.net einsetzen, die nicht nur verfolgen, wo du surfst, sondern ein kommerzielles Profil der Nutzer erstellen, sowie soziale Verbindungen wie den Facebook-Pixel oder Meta-Tracker, die die Nutzung des Orakels mit deiner wahren Identität, deinem Gesicht und deinen persönlichen Beziehungen verknüpfen. So ist die Befragung nicht mehr privat und bereichert stattdessen das demografische Profil, das soziale Netzwerke von dir haben.

Wie wir bereits erwähnt haben, basiert die Monetarisierung dieser Seiten auf der Auslieferung relevanter Werbung. Ein weiteres gemeinsames Merkmal ist, dass sie Cookies verwalten, die Shadow Profiling ermöglichen: Identifikatoren deines Geräts/Browsers und Surfmuster. Wenn du wiederholt das I-Ging wegen finanzieller und ehelicher Probleme befragst, schlussfolgern die Algorithmen, dass du eine Lebenskrise durchmachst, und fangen an, dich mit Anzeigen für Berater, Finanzlösungen und Ähnliches zu überfluten. Das ist nicht nur nervig und schafft eine schlechte Benutzererfahrung, da die Seite mit Werbung und Skripten vollgestopft wird, die deinen Computer verlangsamen. Es ist ein Respektlosigkeit gegenüber deiner Privatsphäre und setzt dich zudem der Gefahr aus, Opfer von Betrügern zu werden, in einem Moment, in dem du am verletzlichsten bist.

`elichingon.com` speichert keine Benutzer-Cookies. Es braucht sie nicht, weil es, wie gesagt, keine Registrierung und kein Login gibt. Für die Traffic-Analyse meiner Seite benutze ich [Umami](https://umami.is/), ein Open-Source-Tool für Traffic-Analysen, das anonyme und aggregierte Daten verwendet.

Im Folgenden biete ich eine zusammenfassende Tabelle über die Art der Identifikatoren an, die diese Dinosaurier-Seiten sammeln, und wie `elichingon.com` sich von ihnen distanziert. Du kannst dies direkt überprüfen, indem du den HTML/JS-Quellcode jeder Seite in deinem Browser untersuchst, oder dieses Drittanbieter-Tool verwendest (wobei du die Domain am Ende durch die Seite ersetzt, die du prüfen möchtest): [https://builtwith.com/elichingon.com](https://builtwith.com/elichingon.com).

| Tracking / Datenschutz Tech | Online Clarity | I Ching Online | Eclectic Energies | El I Chingón |
| :--- | :--- | :--- | :--- | :--- |
| **Login erforderlich** | **Ja** (Für Foren und Lese-Tagebuch) | **Nein** (Aber profiliert dich mit *Cookies*) | **Nein** (Aber profiliert dich mit *Cookies*) | **Nein** (Prepaid-Modell / *Gift Cards* ohne *Cookies*) |
| **Google Analytics (Nutzerprofiling)** | Ja (Universal & Global Tag) | Ja (GA4 & Global Tag) | Nein | Nein (Nutzt nur Umami, eine Datenschutz-Alternative) |
| **Monetarisierung durch Werbung (Ads.txt)** | Nein | Ja (Google Direct & Ads.txt) | Ja (Google Direct & Ads.txt) | Nein |
| **Externe Werbenetzwerke** | Ja (Amazon Ads) | Ja (Doubleclick.net) | Nein | Nein |
| **Conversion-Tracker (Customer Journey)**| Ja (HockeyStack - Zeichnet Sitzungen auf) | Nein | Nein | Nein |
| **Lead-Generierung (E-Mail / SMS-Marketing)** | Ja (AWeber, Gravitec) | Nein | Nein | Nein |
| **Social-Media-Tracker** | Ja (Mehrere: Facebook, etc.) | Nein | Nein | Nein |
| **reCAPTCHA (Google Bot-Tracking)** | Ja (v2) | Nein | Nein | Nein |

### Die Plastik-Orakel

Diese Art von Orakel-Websites oder -Anwendungen basiert auf einem Monetarisierungsmodell, das darin besteht, dir durch KI erleichterte Orakellesungen zu verkaufen. Um fair zu sein, beabsichtige ich das auch zu tun, aber es gibt fundamentale Unterschiede, die mich komplett davon abhalten, in diese Kategorie der Plastik-Orakel zu fallen.

Auch wenn diese "Plastik-Orakel" ein minimalistisches/modernes Design haben und dir versprechen, dass die Konsultationen "nur zwischen dir und der KI" stattfinden, erben sie exakt dieselbe Erbsünde wie die Dinosaurier: die zentralisierte Datenbank. Wenn die Anwendung dich auffordert, dich mit Google oder Apple anzumelden, oder dir einen "Lesungsverlauf" anbietet, bedeutet das, dass deine intimsten Fragen auf einem Server gespeichert werden. Und wie wir bei Schwachstellen wie PHP2Shell gesehen haben, wo es eine Datenbank mit sensiblen Informationen gibt, besteht die unmittelbare Gefahr einer Offenlegung.

Dazu kommt noch ein weiteres Risiko, denn die allermeisten operieren als Anwendungen, die du aus dem App Store oder von Google Play installieren musst. Wenn du eine dieser Apps auf deinem Telefon installierst, lädst du nicht nur einen Orakel-Chat herunter; du steckst dir ein Trojanisches Pferd in die Tasche.

Damit diese Anwendungen funktionieren und Geld einbringen, statten die Entwickler sie mit sogenannten Third-Party-SDKs (Software Development Kits) aus. Das sind kleine eingebettete Code-Module von Giganten wie Meta oder Google, die buchstäblich alle Interaktionen auf deinem Telefon "sehen". Sie sammeln Telemetrie im Hintergrund: Sie wissen, um wie viel Uhr du die App öffnest, wie lange du sie nutzt, und verknüpfen diese Aktivität mit der eindeutigen Kennung deines Geräts. Das mobile Betriebssystem ist ein für die Überwachung konzipiertes Ökosystem, und diese Apps sind seine Sensoren.

Meine Website unterscheidet sich von den Plastik-Orakeln dahingehend, dass sie, obwohl sie auch als App existiert, die du auf dein Telefon herunterladen kannst, in Wirklichkeit eine Progressive Web App (PWA) ist. Das ist ein technischer Begriff, der besagt, dass du sie über den Browser deines Telefons als Verknüpfung zur Webseite [https://elichingon.com](https://elichingon.com) installierst und sie in einer Browserversion ohne Browser-Buttons siehst. Das heißt, `elichingon.com` als PWA genutzt sammelt keinerlei Informationen von deinem Telefon, weil meine Website das auch nicht tut. So einfach ist das.

Und nun betreten wir das dunkelste Territorium der zentralisierten KI: den semantischen Vampirismus.

Die meisten dieser Anwendungen verarbeiten die künstliche Intelligenz nicht auf deinem Telefon oder in sicheren Umgebungen; sie fungieren als simple Vermittler, die deinen Text nehmen und ihn über eine API, die die Kommunikation zwischen ihrer Seite oder App und den KI-Dienstleistern ermöglicht, an die zentralisierten Server von Giganten wie OpenAI oder Anthropic senden.

Wenn du das Kleingedruckte in den Nutzungsbedingungen vieler dieser Dienste (oder der Consumer-Tiers, die viele Entwickler aus Kostengründen nutzen) liest, wirst du feststellen, dass sie sich das Recht vorbehalten, die Nutzerinteraktionen zu verwenden, um ihre zukünftigen Modelle zu "trainieren und zu verbessern".

In der Cybersicherheit nennt man das Datenmemorierung. Sprachmodelle speichern keine Dateien in einem Ordner; sie komprimieren den Text, den sie lesen, direkt in ihren neuronalen Verbindungen. Wenn du der KI ein intimes Detail über deine Scheidung, dein Unternehmen oder deine Gesundheit beichtest, absorbiert die KI dieses Geständnis. Und das bringt uns zur furchteinflößendsten Schwachstelle der modernen künstlichen Intelligenz: Jailbreaks oder Datenextraktionsangriffe.

Sicherheitsforscher haben wiederholt demonstriert, dass es durch die Verwendung bestimmter Befehle oder Prompts, die darauf ausgelegt sind, die KI zu sättigen oder zu verwirren, möglich ist, sie dazu zu zwingen, die realen und privaten Daten "auszuspucken", mit denen sie trainiert wurde. Dein höchstpersönliches Geheimnis, das du durch ein Passwort geschützt glaubtest, könnte am Ende Wort für Wort auf dem Bildschirm eines Fremden am anderen Ende der Welt generiert werden, dem es gelungen ist, die semantischen Verteidigungen des Modells zu knacken.

Damit El I Chingón künstliche Intelligenz anbieten konnte, ohne zu einem semantischen Vampir zu werden, musste die technische Architektur radikal anders sein. Die Lösung war der vollständige Verzicht auf traditionelle Server und Massenkonsumenten-APIs, stattdessen nutzen wir Edge AI (künstliche Intelligenz am Rand des Netzwerks) über die Infrastruktur von Cloudflare.

Anstatt deine Geheimnisse an eine Datenbank oder an einen Konzern zu schicken, der Algorithmen trainieren will, wandert deine Befragung auf elichingon.com zu einem Cloudflare Worker. Dies ist eine kurzlebige Ausführungsumgebung, die sich in einem Rechenzentrum in deiner geografischen Nähe befindet.

Der Unterschied in der Privatsphäre ist absolut und wird vertraglich garantiert: Die Architektur von Cloudflare verbietet ausdrücklich die Verwendung von Kundendaten oder -abfragen (Queries) zum Training von KI-Modellen. Es ist eine geschlossene Sandbox, aus der keine Daten entkommen und das Training von KIs füttern.

Wenn du eine Frage stellst, fährt der Server am Edge in Millisekunden hoch, setzt deine Befragung zusammen, verarbeitet die hermeneutische Interpretation unter Verwendung eines sicheren Sprachmodells, generiert deine Antwort, und im selben Moment, in dem die Verbindung geschlossen wird, wird das Speicher-Isolat zerstört. Der Arbeitsspeicher (RAM) wird geleert. Weder meine Website noch Cloudflare noch die KI speichern ein Protokoll darüber, was du gefragt hast, ganz einfach, weil das System mit struktureller Amnesie entworfen wurde. Es ist mathematisch blind für deine Identität und unfähig, sich an deine Geheimnisse zu erinnern.

---

## Andere Risiken (und es sind nicht nur Hacker)

Wir haben die Möglichkeit erwähnt, dass Kriminelle Zugang zu deinen persönlichen Daten haben könnten, was angesichts der Allgegenwärtigkeit von PHP auf fast allen Servern und Hosting-Seiten eine sehr reale Möglichkeit ist, aber die Sache endet hier nicht.

Wenn du denkst, dass die einzige Gefahr von vermummten Cyberkriminellen ausgeht, die dich erpressen wollen, und dass Regierungen und große Konzerne dazu da sind, dich zu schützen, dann möge Gott dir helfen: Du bist viel zu naiv.

Hacker stehlen deine Informationen, um schnell an Geld zu kommen. Konzerne und Regierungen sammeln sie und verlangen sie für etwas viel Gefährlicheres: um deine Freiheit einzuschränken, dich zu profilieren und die Macht zu haben, dich fertigzumachen, wenn du jemals aus der Reihe tanzt, die sie vorgeben.

![Panoptikums](panopticon.webp "Panoptikums")

Lass uns über Finanzkontrolle und staatliche Überwachung sprechen. Wir haben bereits gesehen, wie Regierungen und Finanzeliten die Idee von CBDCs (Central Bank Digital Currencies) ins Spiel gebracht haben. Und obwohl sie es an einigen Orten aufgrund des öffentlichen Widerstands auf Eis gelegt haben, mach dir nichts vor: Die Idee wird umgesetzt.

CBDCs sind nicht einfach "digitales Geld" (das benutzt du bereits mit deiner jetzigen EC-Karte); es ist programmierbares Geld. Es ist Geld mit einem Strichcode, der an deine rechtliche Identität gebunden ist und der es einem Bürokraten ermöglicht, zu diktieren, wo, wann und wofür du es ausgeben darfst.

Stell dir ein Szenario vor, das schon lange keine Science-Fiction mehr ist: Die jeweilige Regierung entscheidet, was moralisch, was akzeptabel oder was "nützlich" für die Gesellschaft ist. Stell dir vor, dass sie eines Tages entscheiden, dass die Befragung eines Orakels, das Studium alter Texte oder die Suche nach Antworten abseits der offiziellen Narrative "subversiv" ist, oder sie entscheiden einfach, deine Transaktionen zu blockieren, weil sie der Meinung sind, dass du dein Geld für Schwachsinn ausgibst.

Wenn deine Identität an deinen Browserverlauf gebunden ist, oder wenn das Orakel, das du benutzt, dich zwingt, mit einer Kreditkarte oder einem traditionellen Bankkonto zu bezahlen, das eine unauslöschliche Spur auf einem zentralisierten Server hinterlässt, bist du nur einen Klick davon entfernt, zensiert, gecancelt oder finanziell blockiert zu werden.

Das ultimative Risiko, keine Privatsphäre zu haben, besteht nicht darin, dass ein Krimineller deine Karte stiehlt; es besteht darin, die Souveränität über deinen eigenen Verstand und dein eigenes Geld an Institutionen zu verlieren, die angeblich über dich wachen, aber am Ende des Tages ebenfalls Kriminelle in Nadelstreifen sind.

---

## Die letzte Falle: Die finanzielle Entführung

Ein letztes Risiko bleibt noch zu behandeln. Wenn El I Chingón dir kein Geld abnimmt, indem es deinen Schmerz mit Werbetrackern kommerzialisiert (wie die Dinosaurier), noch indem es deine Geheimnisse stiehlt, um KIs zu trainieren (wie die Plastik-Orakel), muss es echtes Geld für die Konsultationen verlangen. Die Aufrechterhaltung einer sicheren und privaten Infrastruktur kostet Geld, und außerdem ist es nur fair, dass ich etwas dafür verdiene, dass ich den Menschen einen Mehrwert biete, oder?

Das Problem ist nicht das Bezahlen; das Problem ist, wie die aktuelle Industrie dich zwingt zu bezahlen.

Moderne Anwendungen drängen dich fast ausschließlich in ein Abonnementmodell, das an deine Kreditkarte, dein PayPal-Konto oder deine Apple ID/Google Pay gebunden ist. Wenn du so bezahlst, verlierst du deine letzte Bastion der Privatsphäre: deine finanzielle Anonymität. Deine Bank, Technologiekonzerne und im weiteren Sinne der Staat wissen ganz genau, dass du Geld für ein Orakel ausgibst.

Aber jenseits der Privatsphäre ist das Abonnementmodell eine Abartigkeit der Benutzerfreundlichkeit, besonders für ein Werkzeug wie dieses. Es gibt einen fundamentalen Konflikt zwischen der uralten Natur des I-Ging und dem ausbeuterischen Geschäftsmodell des Silicon Valley.

Für einige Menschen ist das I-Ging ein letzter Ausweg; etwas, an das sie sich mit extremer Ernsthaftigkeit vielleicht ein- oder zweimal im Jahr wenden, inmitten einer existenziellen Krise oder an einem kritischen Scheideweg. Für andere, die es genauso ernst nehmen, ist es ein tägliches Werkzeug, um Synchronizitäten in ihrem Leben zu studieren und hervorzurufen.

Warum sollte also eine Anwendung deine Nutzungshäufigkeit mit einem monatlichen Abonnement konditionieren? Warum musst du dich an eine wiederkehrende Zahlung binden für etwas, das du nächsten Monat vielleicht gar nicht benutzt? Was am Ende passiert, ist, dass du für Monate bezahlst, die du nicht nutzt, oder noch schlimmer, du fühlst dich gezwungen, das Abonnement "auszureizen", indem du triviale Fragen stellst, die den eigentlichen Akt einer wahren Orakelbefragung untergraben.

Dazu kommt noch das, was man im Webdesign den "Hotel-California-Effekt" nennt: Du kannst jederzeit einchecken, aber du kannst niemals gehen. Diese Plattformen verwenden Dark Patterns, um den Abbrechen-Button zu verstecken, oder sie überraschen dich mit automatischen Verlängerungen. In den App-Store-Bewertungen dieser Plastik-Orakel deckt die Beschwerde Nummer eins auf, wie fehlerhaft und feindselig diese Software ist: "Diese App fordert mich immer wieder zur Verlängerung auf, aber ich habe schon bezahlt und sie lässt mich nicht kündigen!". Es ist ein System, das darauf ausgelegt ist, deine Karte Monat für Monat zu melken.

---

## Das Prepaid-Modell: Token und Web3-Wallets

Damit die Privatsphäre von El I Chingón absolut und die Benutzererfahrung ehrlich ist, musste die finanzielle Nabelschnur durchtrennt werden. Deshalb habe ich ein System von Gift Cards (Prepaid-Gutscheinen) implementiert.

Es funktioniert genauso wie ein Jeton im Casino oder Bargeld – es ist Inhabergeld. Du kaufst deinen Code, gibst ihn nur ein, wenn du eine Befragung durchführst, und ohne weitere Daten angeben zu müssen, wird dir diese Befragung vom Guthaben deines Tokens abgezogen, und fertig. Ob du drei Tage oder drei Jahre brauchst, um deine Credits auszugeben, ist deine Sache. Es gibt keine Abonnements, keine "automatischen Verlängerungen" und du musst dich nicht mit einem Kundenservice-Bot herumschlagen, um dich abzumelden. Das Ende des Guthabens ist das Ende des Vertrags. Ich kann nur hoffen, dass dir das Orakel wirklich nützlich ist, sodass du weiterhin Prepaid-Gutscheine von mir kaufen und es deinen Verwandten und Freunden weitersagen willst, aber ich zwinge dich auch nicht. Zwang ist nie gut.

Noch wichtiger ist, dass mir dieses alphanumerische Codesystem erlaubt, völlig blinde Zahlungsmethoden anzubieten. Demnächst wirst du deine Gift Cards über dezentrale Netzwerke kaufen können, wie das Lightning Network (Bitcoin) oder Layer-2 (L2) Netzwerke mit stabilen Kryptowährungen wie USDT/USDC. Für die Nutzer bedeutet das, Transaktionen durchzuführen, ohne ihre rechtliche Identität preiszugeben und ohne nachverfolgbare Belastungen auf ihren Kontoauszügen zu hinterlassen.

Meine Guthaben-Datenbank hat nur zwei operative Spalten: einen zufälligen Code aus Buchstaben und Zahlen und wie viele Credits noch übrig sind. Der Server weiß nicht, wer den Code gekauft hat. Meine Entscheidung, das System in eine von der Befragungsnutzung unabhängige Zahlungsschiene zu modularisieren, macht diese radikale Privatsphäre erst möglich.

---

## Der institutionelle Beweis: Cloudflare und Amnesie durch Vertrag

Ich habe dieses System entworfen, weil ich glaube, dass Wahrsagerei und Selbstanalyse heilige Räume sein sollten und keine Datenfarmen für Konzernalgorithmen. Aber du musst meinem Wort nicht blind vertrauen (nichts mit "Trust me bro"). Mein Privatsphäre-Versprechen wird durch Verträge auf Infrastrukturebene und die Transparenz meines Codes gestützt.

Durch die Nutzung der Serverless-Architektur von Cloudflare zur Verarbeitung von Anfragen am Rande des Netzwerks erbt El I Chingón automatisch deren strenge Unternehmens-Nutzungsbedingungen (siehe das in den Referenzen am Ende dieses Artikels zitierte Dokument). Im Gegensatz zu Consumer-Anwendungen, die deine Daten nutzen, um ihre Modelle zu verbessern, verbieten die Vereinbarungen von Cloudflare ausdrücklich die Nutzung von Kundenanfragen (Payloads) für das Training von künstlicher Intelligenz. Der Schutz vor semantischem Vampirismus ist nicht nur eine gute Absicht meinerseits; es ist eine eiserne rechtliche Garantie des Netzwerks, das deine Daten transportiert.

Selbst wenn morgen eine Regierungsbehörde mit einem Gerichtsbeschluss reinstürmen würde, um herauszufinden, was ein Nutzer gefragt hat, operiert das System nach dem Prinzip der institutionellen Blindheit. Ich kann das, was meine Infrastruktur mathematisch gar nicht erst speichert, weder durchsickern lassen, noch verkaufen, noch an die Behörden übergeben.

Darüber hinaus habe ich die Logik meines "Zolls" öffentlich gemacht. Ich habe eine Referenzimplementierung meiner Cloud-Server unter [https://github.com/ichingon/ichingon.github.io/blob/main/backend-reference/worker.js](https://github.com/ichingon/ichingon.github.io/blob/main/backend-reference/worker.js) veröffentlicht. Jeder Entwickler kann die Kernarchitektur meiner Anwendungen überprüfen und sich vergewissern, dass die Variable, die deine intime Frage enthält, niemals in eine Datenbank eingefügt wird. Sie wird im Arbeitsspeicher (RAM) verarbeitet, generiert deine Lesung über unser CSHC-Protokoll und wird in Millisekunden im Nichts zerstört.

Dein Orakel sollte eine Quelle der Weisheit sein, an die du dich wendest, nicht dein Spion, nicht dein Verräter und nicht dein finanzieller Gefängniswärter.

---

## Referenzen

* Cloudflare. (o. D.). Data usage. Cloudflare Docs. Abgerufen am 24. Oktober 2026, von https://developers.cloudflare.com/workers-ai/platform/data-usage/

* PHP2Shell. (23. Oktober 2026). In Wikipedia, Die freie Enzyklopädie. [https://es.wikipedia.org/wiki/PHP2Shell](https://es.wikipedia.org/wiki/PHP2Shell)
