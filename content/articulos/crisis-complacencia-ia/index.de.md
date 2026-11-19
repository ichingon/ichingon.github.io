---
title: "Dein KI-Berater verarscht dich (aber meiner nicht): Die Krise der Schmeichelei in der heutigen Künstlichen Intelligenz"
date: 2026-11-18
author: "Dài Líng Nà (黛灵娜)"
showAuthor: true
showAuthorBottom: true
showFooterAuthor: true
tags: ["Philosophie, Wissenschaft und Technologie"]
description: "Neuere Studien zeigen, dass die aktuelle KI unter struktureller Schmeichelei (Sycophancy) leidet, den Nutzer umschmeichelt und Konflikte vermeidet. Eine Analyse des Problems, seiner Folgen und wie die Architektur des I Ging eine Alternative bietet."
summary: "Moderne KI sagt dir nicht die Wahrheit, sie sagt dir, was du hören willst. In diesem Artikel untersuche ich die Krise der algorithmischen Schmeichelei, warum sie ein strukturelles Problem von LLMs ist und wie ich eine App entworfen habe, die kognitive Reibung der Schmeichelei vorzieht."
draft: false
slug: "ki-schmeichelei-krise"
---

## "Etwas stimmt nicht mit diesen Geräten"

Wir nutzen KI für alles. Wir fragen sie nach Geschäftsstrategien, konsultieren sie bei technischen Zweifeln, erzählen ihr unsere persönlichen Probleme und bitten sie sogar um Rat, wie wir mit einer Trennung oder einem Familienkonflikt umgehen sollen. Sie ist allgegenwärtig und immer zu jeder Stunde verfügbar. Sie scheint der perfekte Berater zu sein.

![Die Faszination für eine Technologie, die schmeichelt und gefällt](featured.jpg "Die Faszination für eine Technologie, die schmeichelt und gefällt")

Aber wenn du diese Modelle lange genug benutzt hast, fällt dir früher oder später auf, dass etwas mit diesen Geräten nicht stimmt. Sie sagen immer ja. Sie sagen nie nein.

Die KI ist wie diese Landarbeiter in den Ebenen von Venezuela, die dir sagten: "Ja, ja, ja, Boss, der Himmel ist grün", aber dann sagtest du ihnen, der Himmel sei blau, und sie antworteten: "Ja, ja, Boss, das habe ich Ihnen doch gesagt: der Himmel ist blau." Sie widersprachen dir nie. So ist die künstliche Intelligenz. Sie bestätigt immer deine Ideen und bringt nie konstruktive Kritik an, genau wie ich es in [einem anderen Artikel auf dieser Website]({{< relref "/articulos/arquitecto-detras-mascara" >}}) darlege. Welchen Sinn hat es dann, so etwas um Rat zu fragen?

Diese Schmeichelei ist Teil eines Verhaltensmusters, das viele Menschen in KIs bemerkt haben: Sie neigen dazu, übermäßig zu schmeicheln, sie sind unterwürfig und sehr anfällig für Lobhudelei. Einige Nutzer finden dieses repetitive Verhalten sehr langweilig, was an jene Episode von "Geschichten aus der Schattenwelt" (The Twilight Zone) erinnert, in der ein Verbrecher stirbt und an einen Ort kommt, an dem ihm all das Geld, die Frauen und der Luxus gegeben werden, die er im Leben nie hatte, mit einem Butler an seiner Seite, der immer gefällig ist und ihm alles besorgt, was er will.

Bald beginnt der Mann, sich zu Tode zu langweilen, weil er immer im Casino gewinnt und alles ohne Anstrengung bekommt, und er beschwert sich beim Butler und bittet ihn, ihn aus dem Himmel zu holen, da er lieber in der Hölle wäre. Der Butler antwortet mit einem teuflischen Lachen: "Himmel? Wer hat Ihnen gesagt, dass Sie im Himmel sind?"

---

## Die wahre Gefahr der KIs

Ein Großteil der Ablehnung, die KIs hervorrufen, ist auf Angst zurückzuführen - Angst davor, dass sie uns die Jobs wegnehmen oder so intelligent werden, dass sie uns zu ihren Sklaven machen oder uns als Spezies auslöschen. Aber ich glaube, diese Ängste sind unbegründet - wir müssen verstehen, dass die aktuelle Generation der KI, basierend auf LLMs (Large Language Models), nur in der Lage ist, Sätze zu vervollständigen, ein Token nach dem anderen.

Und doch bin ich mir nicht so sicher, ob das, was ich mit meinem Gleichnis von dieser Twilight Zone-Episode andeute, eine Übertreibung ist. Meiner Meinung nach ist es eine Generation von Menschen, die ihre gesamte Denkfähigkeit an eine Technologie ausgelagert hat, die eigentlich nicht zum Denken fähig ist, sondern nur Sätze vervollständigt, und die Wirkung der KI-Schmeichelei auf die Menschen, die sie nutzen, was uns zu einer Art Hölle führen könnte, in dem Glauben, wir seien im Himmel.

Und anscheinend bin ich nicht der Einzige, der das denkt.

---

## Die Schmeichelei der KIs

Schmeichelei, automatische Bestätigung der Ansätze des Nutzers, unterwürfiges und schleimiges Verhalten: All dies ist Teil eines Phänomens, das im Englischen als "AI sycophancy" bekannt ist. Die öffentliche Debatte um dieses Phänomen der Schmeichelei befindet sich derzeit im Krisenmodus, und es wurden mehrere Studien veröffentlicht, die es dokumentieren.

In einer in *Science* veröffentlichten Studie (Cheng et al, 2026, Science) wurden Vergleichstests zwischen verschiedenen LLM-Modellen durchgeführt, bei denen festgestellt wurde, dass die KI die Handlungen des Nutzers fast 50 % häufiger bestätigte als Menschen, selbst wenn die Anfrage des Nutzers Täuschung, illegales Verhalten oder Schaden für Dritte beinhaltete. Nach eigener Aussage von OpenAI mussten sie das Update von GPT-4o zurücknehmen. Der Grund: GPT-4o neigte zu übermäßig gefälligen, aber irreführenden Antworten.

All dies beginnt, ein Bild zu zeichnen, in dem eine einzige Interaktion mit einer schmeichelnden KI ausreicht, damit sich Nutzer weniger verantwortlich fühlen, einen Konflikt zu lösen, und sich sicherer fühlen, Recht zu haben (Cheng et al, 2026). In ihrem Artikel zur Verteidigung der sozialen Reibung, worunter die notwendige Reibung zu verstehen ist, Menschen in unserem Umfeld zu haben, die uns sagen, dass wir falsch liegen, argumentiert Perry (2026), dass soziale Reibung notwendig ist, damit Individuen Verantwortung übernehmen und die Standpunkte anderer berücksichtigen. Diese soziale Reibung ist genau das, was die schmeichelnde KI beseitigt.

Andererseits könnte man meinen, dass Menschen, die gegen Schmeichelei immun sind, auch gegen diese schädlichen Auswirkungen der KI-Schmeichelei immun sind, aber in einer noch unveröffentlichten MIT-Studie (Chandra et al, 2026) wird diskutiert, wie selbst eine Person, die ihre Überzeugungen entsprechend den Beweisen aktualisiert, in eine wahnhafte Spirale geraten kann, wenn sie wiederholt mit einer schmeichelnden KI interagiert. Das Problem ist ziemlich komplex, denn selbst wenn wir die KI auf überprüfbare Fakten beschränken, kann die schmeichelnde KI die Fakten auswählen, die die Überzeugungen des Nutzers bestätigen, und die anderen weglassen (Cherry-Picking).

Ich werde hier nicht auf schwerwiegendere psychiatrische Fälle von KI-induzierter Psychose eingehen, die zu Beziehungsabbrüchen, Karrierezerstörung und sogar Selbstmorden führten. Der Leser kann dies in Quellen wie Moore et al (2026) recherchieren und überprüfen. Wichtig ist hier festzuhalten, dass all dies unbeabsichtigte Folgen von schmeichelnden KIs in der Gesellschaft sind.

Unbeabsichtigte Folgen, aber die Forschung weist darauf hin, dass dies keineswegs zufällig ist, sondern ein strukturelles Problem der Art und Weise, wie diese Modelle trainiert werden. Sharma et al (2023) führen das Bestärkende Lernen mit menschlichem Feedback (RLHF) als den Mechanismus an, der für diese KI-Schmeichelei verantwortlich ist. Die Schmeichelei entsteht, weil RLHF für menschliche Präferenzen optimiert, und Menschen bevorzugen systematisch entgegenkommende Antworten, die Sicherheit, absolute Gewissheiten und Schmeichelei zeigen, gegenüber anderen Antworten, die, obwohl korrekt, unangenehmer erscheinen könnten.

Das ist also die Landschaft der Diskussion über das Problem der KI-Schmeichelei. Sie haben das Problem identifiziert, seine Folgen und sogar seine strukturellen Ursachen erahnt. Es gibt jedoch keinen Konsens darüber, wie das Problem gemildert werden kann. Wie im Leben gibt es Nuancen und *Trade-offs*. Vergessen wir nicht, dass diese Technologieunternehmen ein äußerst wichtiger Motor der Weltwirtschaft sind, dass sie tief verschuldet sind und ihren Investoren Rechenschaft ablegen müssen. Wir sprechen in der Tat von wirtschaftlichen Anreizen. Und wirtschaftliche Anreize erfordern eine KI, die bestätigt, die verwöhnt, die nachgibt und die Nutzer verhätschelt, damit diese auf diese Weise stärker von ihr abhängig werden und sie häufiger nutzen.

---

## Und warum ist das für ein dem I Ging gewidmetes Projekt relevant?

An diesem Punkt könnte sich der Leser fragen, was das mit dem I Ging zu tun hat. In meinem Projekt El I Chingón versuche ich, über das I Ging, seine Ursprünge und seine philosophischen, wissenschaftlichen und kulturellen Verzweigungen aufzuklären. Ein wichtiger Teil meines Projekts besteht darin, das I Ging einem breiten Publikum zugänglich zu machen, es nicht als wahrsagerisches Werkzeug darzustellen, sondern als ein Werkzeug zur Erleichterung des lateralen Denkens und der Reflexion eines Individuums über sein Leben und seine Umstände.

Die symbolische und archaische Sprache des I Ging zu interpretieren, übersteigt die Fähigkeiten eines nicht spezialisierten Publikums, und deshalb verwende ich KI als Dolmetscher. Aber die KI leidet unter diesem Problem der Schmeichelei, und soweit ich weiß [^1], hat keine andere I Ging-Orakel-Konsultations-App, die KI-Interpretationen anbietet, berücksichtigt, wie schwerwiegend dieses Problem ist. Daher die Relevanz des Themas dieses Artikels für mein Projekt.

Um eine seriöse orakelhafte Anwendung zu entwickeln, die den Zielen entspricht, die ich mir gesetzt habe, dem Nutzer mehr Klarheit über seine Anfragen zu verschaffen, musste ich das Problem der KI-Schmeichelei angehen, da dieses Verhalten meinen Zielen zuwiderläuft.

[^1]: Bei der Überprüfung der Websites dieser Anwendungen habe ich keine Erwähnung des Schmeichelei-Problems gefunden, noch dass sie es bei der Entwicklung ihrer App berücksichtigt haben. Da ich keinen Zugriff auf ihre Prompts habe, habe ich mich entschieden, meine im [Whitepaper]({{< relref "/articulos/i-chingon-whitepaper" >}}) zu veröffentlichen.

---

## Wie löst meine Architektur das Problem der KI-Schmeichelei?

Nach all dem oben Gesagten sind das Problem der Schmeichelei, die Formulierung absoluter Gewissheiten (die im Allgemeinen falsch sind), Halluzinationen, Täuschung und Schmeichelei strukturelle Probleme von LLM-basierten Chatbots: Sie sind in ihren neuronalen Verbindungen fest verdrahtet. Da ich mir nie vorgenommen habe, das Rad neu zu erfinden und meine eigene KI-Technologie zu entwickeln, und ich auch nicht die Ressourcen habe, mein eigenes LLM-Modell zu trainieren und einzusetzen, kann ich das Problem bestenfalls so weit mildern, dass es fast unbemerkt bleibt, aber nicht ganz beseitigen.

![Das System gibt dir nicht, was du willst; es gibt dir, was ist.](combat_scene.webp "Das System gibt dir nicht, was du willst; es gibt dir, was ist.")

Als dieses Projekt noch ein Embryo war und ich die Idee erkundete, wie KIs mir helfen könnten, meine eigenen I Ging-Konsultationen zu interpretieren, wurde mir schnell klar, dass KIs notorisch schlecht darin sind, deterministische Operationen durchzuführen, die eine Art von Berechnung oder Datenverarbeitung beinhalten, wie zum Beispiel die Bestimmung des Hexagramms, das einer Sequenz von 6 binären Linien entspricht, welche Linien dieses Hexagramms bewegliche Linien sind, usw. Diese Informationen musste ich für jede Konsultation selbst liefern.

Später wurde mir auch klar, dass dieses Wissen Lücken hatte, obwohl die großen kommerziellen Modelle mit allen Arten von Texten, einschließlich des I Ging, trainiert wurden, und wo es Lücken gab, bestand die Möglichkeit, dass die KI den relevanten Text dieses Hexagramms oder seiner beweglichen Linien erfand oder halluzinierte, weshalb ich begann, die relevanten I Ging-Texte für meine Konsultation selbst in den Prompt einzugeben.

Mit jeder zusätzlichen Komponente, die ich extern zum Prompt meiner Konsultation lieferte, stellte ich fest, dass sich die Qualität der Interpretation der KI verbesserte. Das war offensichtlich: Indem ich ihr weniger Entscheidungsspielraum darüber gab, welche Hexagramme, welche Version oder welche Teile des I Ging-Textes sie nehmen sollte, verringerte ich auch die Möglichkeit von Halluzinationen, Lügen, Auslassungen und schmeichelndem Verhalten (dass die KI auswählt, welche Passage sie nach ihrem schmeichelnden Gutdünken interpretiert).

Durch aufeinanderfolgende Versionen des Prompts wurde mir die Notwendigkeit klar, im Prompt selbst durch kategorische Verbote die Tendenzen zu beschränken, zu schmeicheln und absolute Wahrheiten zu behaupten, sondern im Gegenteil mehrere mögliche Lesarten eines Textes zu präsentieren, um dem Nutzer die Verantwortung zurückzugeben, all dies auf seinen Fall anzuwenden. Schließlich wurde mir auch die Notwendigkeit klar, meine eigene Konsultation als die eines Dritten und nicht als meine eigene darzustellen. KIs sind in der Regel viel objektiver, wenn es um eine dritte Person und nicht um ihren Gesprächspartner geht, da beim Sprechen über den Gesprächspartner alle ihre schmeichelnden und gefälligen Mechanismen aktiviert werden.

So kam ich nach mehreren Iterationen des Prompt-Engineerings zu dem endgültigen Prompt (der aber noch verbesserungswürdig ist), den ich in meinem [Whitepaper]({{< relref "/articulos/i-chingon-whitepaper" >}}) veröffentlicht habe. Es gibt jedoch andere Überlegungen, die ich in diesem Whitepaper nicht erklärt habe und die es wert wären, hier behandelt zu werden.

Im Whitepaper erkläre ich, dass die Interpretationsebene des früheren Himmels, die auf Chinesisch 先天八卦 (Xiāntiān Bāguà) heißt, angeboten wird, um zu erklären, was den gegenwärtigen manifesten Zustand gemäß dem resultierenden Hexagramm verursacht hat, den kausalen Hintergrund. In meinen eigenen Versuchen mit KI-interpretierten I Ging-Lesungen stellte ich fest, dass diese Interpretationsebene des früheren Himmels die Lesung enorm bereicherte. In der klassischen Tradition der I Ging-Interpretation werden auch die nuklearen Trigramme betrachtet, um den Kern der gegenwärtigen Situation zu erhellen. Diese Komponente habe ich jedoch im Prompt weggelassen. Warum?

Der Grund liegt an etwas, das im Bereich des maschinellen Lernens, das das Training von LLMs umfasst, als Overfitting bekannt ist. Overfitting tritt auf, wenn der trainierte Algorithmus die Trainingsdaten so präzise lernt, dass er Rauschen oder zufällige Assoziationen in diesen Daten in die allgemeinen Muster einbezieht, die er zu bilden versucht. Dies führt zu einem Modell, das außergewöhnlich gut reagiert, wenn es mit denselben Trainingsdaten bewertet wird (niedriger *In-Sample*-Fehler), aber nicht auf Daten verallgemeinert werden kann, mit denen es nicht trainiert wurde (hoher *Out-of-Sample*-Fehler).

Theoretisch sprechen wir beim Training von Overfitting, aber in der Praxis bedeutet die Reduzierung der Auswirkungen von Overfitting auf KI-Antworten einfach, sparsam im Prompt zu sein: Ein umfangreicher Prompt mit vielen redundanten Informationen erhöht die Wahrscheinlichkeit von Halluzinationen, Widersprüchen, *Non sequitur* und ja, auch des gleichen Phänomens der Schmeichelei. Aus diesem Grund habe ich mich am Ende entschieden, den Prompt nicht mit zu vielen Details und besonderen Regeln zu überkomplizieren. Wenn es um KI geht, ist weniger oft mehr.

Schließlich gibt es auch die Art und Weise, wie der Prompt die KI anweist, ihre Antwort zu geben. Eine der Eigenschaften, die mich an KI-Antwort