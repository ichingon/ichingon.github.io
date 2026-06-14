---
title: "Echtheitsprüfung"
translationKey: "verificar"
description: "Wie Sie kryptografisch überprüfen können, dass die Inhalte auf elichingon.com authentisch sind, nicht verändert wurden und wirklich von Dailingna Romero stammen."
date: 2026-06-13
draft: false
showDate: false
showReadingTime: false
showWordCount: false
showAuthor: false
---

In einem Internet, das von KI-generierten Inhalten, Deepfakes, Identitätsdiebstahl und Plagiaten überschwemmt wird, stellt sich eine unumgängliche Frage: **Wie wissen Sie, ob das, was Sie lesen oder sehen, wirklich vom ursprünglichen Schöpfer stammt und nicht von einem Account, der dessen Identität vortäuscht?**

Diese Seite erklärt, wie Sie kryptografisch überprüfen können, dass jeder auf `elichingon.com` veröffentlichte Artikel, jedes Video oder jeder Inhalt authentisch ist, nicht manipuliert wurde und von dieser spezifischen digitalen Entität veröffentlicht wurde.

---

## Warum ich meine Inhalte kryptografisch signiere

Letztendlich sind „Dailingna Romero“ oder „El I Chingón“ (noch) sehr unbekannte Entitäten im Internet, aber genau wie das **Hexagramm 20 des I Ging (Die Betrachtung / Guān 觀)** erfüllt dies einen doppelten Zweck, der die Natur des Hexagramms selbst widerspiegelt: den Akt des Betrachtens und den Zustand, betrachtet zu werden.

### Der Akt des Betrachtens (als Medienkonsument)

Als Konsument von Inhalten missfällt es mir, keine Möglichkeit zu haben, zu überprüfen, ob das, was ich lese oder sehe, wirklich aus der angegebenen Quelle stammt.

Dabei geht es mir nicht darum, zu erkennen, ob ein Inhalt von einer KI generiert wurde – schließlich ist Dailingna Romero selbst ein digitaler Avatar und ihre Videos werden von KI generiert. Was zählt, ist zu wissen, ob **die ausgedrückten Ideen wirklich von Dailingna stammen** und nicht von einer anderen Person, die mein Bild und meine Stimme nutzt, um ihre eigenen Ideen zu verbreiten.

Heutzutage ist es ein Leichtes, einen Kanal zu erstellen, der mit einer (realen oder fiktiven) Persönlichkeit verknüpft ist, und dieser Dinge in den Mund zu legen, die sie nie gesagt hat. Man sieht überall Videos von Richard Feynman, Neville Goddard, Einstein oder dem „Kenzo Guy“, und es ist unmöglich zu unterscheiden, was die Persönlichkeit tatsächlich gesagt hat und was der Videoersteller ihr in den Mund legt.

Auf YouTube ist die automatische KI-Erkennung mittlerweile Standard, aber das reicht nicht aus. Es kommt nicht darauf an, ob ein Video von einer KI generiert wurde, sondern **ob die ausgedrückten Ideen authentisch sind und von dem stammen, der sich als Autor ausgibt**.

Ich möchte, dass Sie Werkzeuge haben, um selbst zu überprüfen, ob das, was Sie lesen, wirklich von mir stammt, ohne blind auf irgendeine Plattform vertrauen zu müssen. Die kryptografische Signatur garantiert, dass niemand den Inhalt nach der Veröffentlichung ändern kann, ohne dass die Signatur ungültig wird. Der Zeitstempel im Nostr-Netzwerk beweist, wann ich etwas zum ersten Mal veröffentlicht habe, was nützlich ist, um im Falle eines Plagiats die Originalautorenschaft nachzuweisen.

### Der Zustand, betrachtet zu werden (als Inhaltsersteller)

In einer Welt, in der jeder Stimmen, Gesichter und Schreibstile mit KI klonen kann, ist Kryptografie der einzige verlässliche Beweis für Authentizität. Wir befinden uns in einer existenziellen Krise des Internets selbst. Die Theorie des toten Internets und die Verbreitung von Deepfakes haben uns an einen Punkt gebracht, an dem wir unseren eigenen Augen und Ohren nicht mehr trauen können, um die wahre Autorenschaft von etwas zu erkennen.

Meine Hoffnung bei der Implementierung dieses Systems ist, dass andere Inhaltsersteller beginnen, dasselbe zu tun, und so dazu beitragen, diese Situation umzukehren. Ich möchte vermitteln, wie wichtig **digitale Souveränität** ist, damit jeder seine Inhalte schützen kann, ohne von Konzernen wie YouTube, Twitter oder Medium abhängig zu sein, um zu beweisen, dass ich derjenige bin, der ich vorgebe zu sein.

Meine Identität lebt in einem offenen und dezentralisierten Protokoll, nicht auf den Servern irgendeines Unternehmens.

---

## Was ist eine kryptografische Signatur?

Jeder Artikel, den ich veröffentliche, ist von einer **einzigartigen mathematischen Signatur** begleitet. Diese Signatur erfüllt drei Funktionen:

1. **Beweist Autorenschaft**: Sie zeigt, dass der Inhalt von dieser spezifischen digitalen Identität erschaffen wurde (`dailingna@elichingon.com`).
2. **Garantiert Integrität**: Wenn jemand auch nur ein einziges Wort, ein Leerzeichen oder ein Komma ändert, verliert die Signatur ihre Gültigkeit.
3. **Zeitstempel**: Sie registriert unveränderlich, wann der Inhalt ursprünglich veröffentlicht wurde.

Es ist das digitale Äquivalent eines **Siegellacks**, der weder gefälscht, kopiert noch gebrochen werden kann, ohne Beweise zu hinterlassen.

---

## Wie funktioniert das technisch?

Der Prozess basiert auf zwei offenen Standards:

### 1. Nostr (Notes and Other Stuff Transmitted by Relays)
Ein dezentralisiertes Protokoll, das das Signieren von Nachrichten mit kryptografischen Schlüsseln ermöglicht. Es hängt von keinem Unternehmen, keiner Regierung und keinem zentralen Server ab.

### 2. NIP-05 (Identitätsverifizierung)
Ein Standard, der einen öffentlichen Nostr-Schlüssel mit einem Domainnamen verknüpft. In diesem Fall:

dailingna@elichingon.com → npub1rfqz5sqv6plxpm3lqfu35q30d7p2m2mt38t7qz6309fxm7e02mrqjxlx92

Sie können diese Verknüpfung selbst überprüfen, indem Sie folgende Seite aufrufen:

[https://elichingon.com/.well-known/nostr.json](https://elichingon.com/.well-known/nostr.json)

---

## Wie man einen Artikel verifiziert

Am Ende jedes Artikels auf dieser Website finden Sie einen Block wie diesen:

> 🔐 KRYPTOGRAFISCHE VERIFIZIERUNG DER AUTORENSCHAFT
> Dieser Inhalt wurde offiziell von Dailingna Romero erstellt und veröffentlicht.
> 
> 🔗 Offizielle URL: https://elichingon.com/articulo/...
> 🔐 Verifizierte Nostr-Identität: dailingna@elichingon.com
> 📜 Verifizierungsnotiz auf Nostr: https://primal.net/e/note1ues5g2y8lpjlpsg7qx40lzwk67ql08j2cmree44lkpxhew04rtdstev548
> 
> Um zu überprüfen, dass dieser Inhalt nicht verändert wurde und kein Deepfake ist, 
> klicken Sie auf den obigen Nostr-Link und prüfen Sie, ob die signierte URL 
> exakt mit der URL dieses Inhalts übereinstimmt.

---

## Verifizierung von YouTube-Videos

Bei Videos, die auf YouTube veröffentlicht werden, enthält die Videobeschreibung:
* Die offizielle URL des Videos auf dem Kanal von Dailingna Romero.
* Einen Link zur Nostr-Notiz, die die Authentizität zertifiziert.
* Die kryptografische Signatur der URL.

### Wie erkennt man ein Deepfake?

Wenn Sie ein Video, das anscheinend von mir stammt, auf einem anderen Kanal sehen, überprüfen Sie Folgendes:
* Enthält die Beschreibung einen Link zu einer signierten Notiz auf Nostr?
* Verweist der Link auf dailingna@elichingon.com mit einem Verifizierungs-Häkchen?
* Stimmt die signierte URL mit der URL des Videos überein, das Sie gerade sehen?
* Wenn die Antwort auf eine dieser Fragen „Nein“ lautet, handelt es sich höchstwahrscheinlich um ein Deepfake, nicht autorisierten Inhalt oder ein Plagiat.

---

## Was tue ich, wenn ich gefälschte Inhalte finde?

Wenn Sie ein Video, einen Artikel oder einen Beitrag entdecken, der meinen Namen, mein Bild oder meine Stimme ohne Erlaubnis verwendet:

1. **Verifizieren Sie**, dass keine gültige kryptografische Signatur vorhanden ist.
2. **Melden Sie** den Inhalt auf der jeweiligen Plattform (YouTube, soziale Netzwerke usw.) wegen Identitätsdiebstahls oder Urheberrechtsverletzung.
3. **Teilen Sie es mir** über meine offiziellen Kanäle mit, damit ich bei Bedarf rechtliche Schritte einleiten kann.

Alle Inhalte dieser Website stehen unter der Lizenz **Creative Commons Namensnennung 4.0 International (CC BY 4.0)**. Sie dürfen sie teilen und bearbeiten, aber Sie müssen:

- `Dailingna Romero / elichingon.com` ausdrücklich als Urheber nennen.
- Die kryptografische Signatur nicht dazu verwenden, veränderten Inhalt als Original auszugeben.

Weitere Informationen finden Sie unter [https://elichingon.com/licencias/](https://elichingon.com/licencias/)

---

## Für andere Inhaltsersteller

Wenn Sie selbst Inhalte erstellen und eine kryptografische Verifizierung für Ihre eigene Arbeit implementieren möchten: Das Nostr-Protokoll ist **frei, offen und kostenlos**.

### Ressourcen für den Einstieg:

- [Offizielle Nostr-Dokumentation](https://github.com/nostr-protocol/nostr)
- [NIP-05: DNS-basierte Identitätsverifizierung](https://github.com/nostr-protocol/nips/blob/master/05.md)
- [NIP-23: Langform-Inhalte (Artikel)](https://github.com/nostr-protocol/nips/blob/master/23.md)
- [NIP-94: Datei-Metadaten-Speicherung](https://github.com/nostr-protocol/nips/blob/master/94.md)

### Empfohlene Tools:

- **Amethyst** (Android): Mobiler Nostr-Client.
- **Primal** (Web/Mobil): Client mit exzellenter NIP-05-Visualisierung und Performance.
- **Coracle** (Web): Minimalistischer Webclient.
- **nostr-tools** (JavaScript): Entwickler-Bibliothek.

---

## Die Zukunft des Internets ist verifizierbar

Dies ist nicht nur mein Inhalt. Es ist ein **Standard für Authentizität**, den jeder Kreative adaptieren kann.

In einer Welt, in der KI Texte, Bilder, Audio und Videos erzeugen kann, die nicht mehr von der Realität zu unterscheiden sind, wird Kryptografie zur einzigen Möglichkeit, zu beweisen, dass etwas tatsächlich von der Person erschaffen wurde, die dies von sich behauptet.

Es geht nicht darum, mir zu vertrauen. Es geht darum, dass Sie **selbst nachprüfen können**.

---

**Offizielle Identität:**
- **NIP-05:** `dailingna@elichingon.com`
- **NPub:** `npub1rfqz5sqv6plxpm3lqfu35q30d7p2m2mt38t7qz6309fxm7e02mrqjxlx92`
- **Website:** [https://elichingon.com](https://elichingon.com)