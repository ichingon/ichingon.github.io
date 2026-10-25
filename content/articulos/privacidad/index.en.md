---
title: "Privacy according to El I Chingón - why should you care?"
date: 2026-10-24
author: "Dài Líng Nà (黛灵娜)"
showAuthor: true
showAuthorBottom: true
showFooterAuthor: true
tags: ["The Tao of the Content Creator"]
description: "Discover why privacy is vital in an oracular consultation and how El I Chingón protects your privacy."
summary: "Discover why privacy in an oracular consultation app is not a luxury, but a necessity, and how we built elichingon.com with structural amnesia and blind payments to shield your secrets."
draft: false
slug: "privacy-according-to-elichingon-why-should-you-care"
aliases: ["/en/privacy"]
---

In the [whitepaper for my application]({{< relref "articulos/i-chingon-whitepaper" >}}), where I discuss my Constrained Stochastic Hermeneutic Computing (CSHC) protocol, I state that radical privacy is one of the fundamental pillars of my protocol. In this article I'm going to explain, speaking to the everyday user, why this is so important, how El I Chingón differs from other oracular websites or apps in this regard, and how, without getting into too much technical jargon, you could audit the privacy of El I Chingón or any of these sites.

---

## The myth of "I have nothing to hide"

![Dài Líng Nà operating outside the digital panopticon. Your oracle shouldn't be your spy.](featured.jpg "Dài Líng Nà operating outside the digital panopticon. Your oracle shouldn't be your spy.")

It's concerning to see how oblivious so many people are to the security and privacy risks on the Internet. It seems many assume that privacy is only for criminals or hackers, and since they aren't involved in any crimes, they have nothing to hide and therefore privacy is an irrelevant issue for them. Huge mistake—privacy is important for everyone and is (or should be) a basic universal human right.

Let's start with the very nature of an oracular consultation. An oracular consultation is, by default, a highly private act, given how personal some questions can be from people who are going through relationship problems, embarrassing situations, or harboring unconfessable thoughts. I don't mean to imply that the I Ching is only useful for this [type of questions]({{< relref "articulos/que-podemos-preguntar" >}}), obviously. But since in the I Ching, the querent is a fundamental and inseparable part of the querent-oracle-reality system, many questions we ask the I Ching end up gravitating towards highly personal matters. And therefore, we don't want this information ending up in other hands, or read by other pairs of eyes.

But there is also the issue of the oracle's effectiveness. If we suspect, consciously or subconsciously, that the privacy of the oracular consultation is compromised, a very harmful phenomenon for the effectiveness of I Ching readings could occur: **self-censorship**. The querent stops asking the questions that truly matter to them, sugarcoats their fears in the phrasing of the question, and, as a consequence, the interpreter of their I Ching cast returns useless answers because the statement of the question lacks sufficient emotional context and honesty.

So, just based on this point of self-censorship alone, it's worth considering privacy when we use oracular applications, or even if we go to a human expert or guru to request their interpretation services; in this latter case, the condition of privacy is completely violated. However, self-censorship is just the intimate collateral damage. The external danger is even worse...

If a website requires you to register and log in to use it, it's because it's keeping your login data in a database (MongoDB, PostgreSQL), containing at least your email address, in the best of cases. Now imagine that the site also keeps a record of your consultations, with your highly personal questions and existential dilemmas, for the "convenience" of having an application that knows you and can supposedly give more accurate readings, or allow you to journal your own consultations. Now imagine that this site gets hacked and all that information ends up in the hands of unscrupulous hackers, ready to make it public unless you pay a ransom.

---

## The true risks of not having privacy

If you think this possibility is remote and therefore doesn't affect you, consider the recent vulnerability, called PHP2Shell, discovered in October 2026. For those who don't know, PHP is a server-side interpreted language that runs on over 70% of websites on the internet. The discovered vulnerability allows an unauthorized attacker to inject code into a server from the outside, and take control remotely, exploiting a flaw in how PHP handles its internal memory.

This vulnerability, which received a score of 9.2 out of 10 according to the CVSS system, affects, as mentioned, over 70% of websites worldwide, including major platforms like Joomla, Drupal, or WordPress, the latter being the most common for website hosting. Let's analyze the vulnerabilities of this site regarding PHP2Shell.

Github Pages, the platform where `elichingon.com` is hosted, is unaffected by this PHP flaw. GitHub Pages is a strictly static hosting service: it serves HTML, CSS, JS files, and images directly from the repository. A .php file uploaded there is served as plain text, it is not interpreted. There is no PHP interpreter anywhere in the chain. This site uses Cloudflare as a CDN/proxy, which also doesn't run PHP. In fact, my site's architecture was explicitly designed to dispense with PHP and traditional user databases, eliminating from the root the possibility of a hackable history existing. But we'll come back to this later.

Let's talk a bit more about the user data that most of these pages or applications handle, because it can be more than the obvious, like your email, your name, your ID, etc. To do this, we are going to classify oracular sites or applications (I Ching or divination in general) into two main categories. One category, which I will call "the I Ching dinosaurs", are those pages that remained frozen in the early 2000s, such as [Online Clarity](<https://www.onlineclarity.co.uk/>), [I Ching Online.NET - the Online Book of Changes](<https://www.ichingonline.net/>), and [Eclectic Energies I Ging](<https://www.eclecticenergies.com>), which do not offer AI interpretation. The other category of applications or sites, which I will call the "plastic oracles", because they are mass-produced AI wrappers that only offer "spiritual fast-food".

### The I Ching Dinosaurs

Let's talk first about the I Ching dinosaurs. Most of these sites do not require registration or login to use, with the exception of Online Clarity, to participate in the forums. But their monetization model is based on surveillance capitalism, which implies having invasive scripts like Google Analytics for traffic metrics, DoubleClick (from Google), and Media.net, which not only track where you navigate but build a commercial profile of users, and social cords like Facebook pixel or Meta trackers, which link the use of the oracle with your real identity, your face, and your personal relationships. Thus, the consultation ceases to be private and goes on to enrich the demographic profile that social networks have on you.

As we mentioned, the monetization of these sites is based on serving relevant ads. Another common characteristic is that they manage cookies that allow shadow profiling: identifiers of your device/browser and browsing patterns. If you repeatedly consult the I Ching about financial and marital problems, the algorithms infer that you are going through a life crisis and begin to flood you with ads for counselors, financial solutions, and other related things. This is not only annoying and creates a bad user experience, filling the site with ads and scripts that slow down your computer. It is a disrespect to your privacy, and also exposes you to falling prey to scams at a time when you are most vulnerable.

`elichingon.com` does not keep user cookies. It doesn't need them because, as I said, there is no registration or login. To do traffic analytics for my site, I use [Umami](https://umami.is/), an open-source traffic analytics collector that uses anonymous and aggregated data.

Below I offer a summary table on the type of identifiers that these dinosaur sites collect, and how `elichingon.com` distances itself from them. You can verify this directly by examining the html/js source code of each site in your browser, or use this third-party tool (substituting the domain at the end with the site you want to audit): [https://builtwith.com/elichingon.com](https://builtwith.com/elichingon.com).

| Tracking / Privacy Tech | Online Clarity | I Ching Online | Eclectic Energies | El I Chingón |
| :--- | :--- | :--- | :--- | :--- |
| **Requires Login** | **Yes** (For forums and reading journal) | **No** (But profiles you with *cookies*) | **No** (But profiles you with *cookies*) | **No** (Prepaid model / *Gift Cards* no *cookies*) |
| **Google Analytics (User profiling)** | Yes (Universal & Global Tag) | Yes (GA4 & Global Tag) | No | No (Only uses Umami, a privacy alternative) |
| **Ad Monetization (Ads.txt)** | No | Yes (Google Direct & Ads.txt) | Yes (Google Direct & Ads.txt) | No |
| **External Ad Networks** | Yes (Amazon Ads) | Yes (Doubleclick.net) | No | No |
| **Conversion Trackers (Customer Journey)**| Yes (HockeyStack - Records sessions) | No | No | No |
| **Lead Capture (Email / SMS Marketing)** | Yes (AWeber, Gravitec) | No | No | No |
| **Social Media Trackers** | Yes (Multiple: Facebook, etc.) | No | No | No |
| **reCAPTCHA (Google Bot Tracking)** | Yes (v2) | No | No | No |

### The plastic oracles

This type of oracular consultation sites or applications rely on a monetization model that consists of selling you AI-facilitated oracular readings. To be fair, I intend to do that too, but there are some fundamental differences that completely distance me from falling into this category of plastic oracles.

Even if these "plastic oracles" have a minimalist/modern design and promise you that the consultations are "just between you and the AI", they inherit exactly the same original sin as the dinosaurs: the centralized database. If the application asks you to log in with Google or Apple, or offers you a "reading history", it means your most intimate questions are being stored on a server. And as we saw with vulnerabilities like PHP2Shell, where there is a database with sensitive information, there is an imminent danger of exposure.

Add to this another risk, because the vast majority operate as applications that you must install from the App Store or Google Play. When you install one of these apps on your phone, you are not just downloading an oracular chat; you are putting a Trojan horse in your pocket.

For these applications to work and monetize, developers pack them with something called third-party SDKs (Software Development Kits). These are small embedded code modules, belonging to giants like Meta or Google, that literally "see" all the interactions on your phone. They collect telemetry in the background: they know what time you open the app, how long you use it, and associate that activity with your device's unique identifier. The mobile operating system is an ecosystem designed for surveillance, and these apps are its sensors.

My site differs from plastic oracles in that, although it also exists as an app you can download on your phone, it is actually a Progressive Web App (PWA), which is a technical term used to say that you install it from your phone's browser as a shortcut to the web page [https://elichingon.com](https://elichingon.com) and you view it in a version of the browser without the browser buttons. That is, `elichingon.com` used as a PWA does not collect any information from your phone because my website doesn't either. It's that simple.

And now we enter the darkest territory of centralized AI: semantic vampirism.

Most of these applications do not process artificial intelligence on your phone, or in secure environments; they act as simple middlemen that take your text and send it to the centralized servers of giants like OpenAI or Anthropic, through an API that allows communication between their site or app and the AI service providers.

If you read the fine print of the terms of use of many of these services (or the consumer tiers that many developers use to save costs), you will discover that they reserve the right to use user interactions to "train and improve" their future models.

In cybersecurity, this is known as Data Memorization. Language models don't save files in a folder; they compress the text they read directly into their neural connections. If you confess to the AI an intimate detail about your divorce, your company, or your health, the AI absorbs that confession. And this brings us to the most terrifying vulnerability of modern artificial intelligence: jailbreaks or data extraction attacks.

Security researchers have repeatedly demonstrated that, through the use of certain commands or prompts designed to saturate or confuse the AI, it is possible to force it to "spit out" the real and private data it was trained on. Your highly personal secret, which you thought was protected by a password, could end up being generated word for word on the screen of a stranger on the other side of the world who managed to hack the model's semantic defenses.

For El I Chingón to be able to offer artificial intelligence without becoming a semantic vampire, the technical architecture had to be radically different. The solution was to completely dispense with traditional servers and mass-consumer APIs, using Edge AI (Artificial Intelligence at the Edge) through Cloudflare's infrastructure.

Instead of sending your secrets to a database or to a corporation that wants to train algorithms, your consultation on elichingon.com travels to a Cloudflare Worker. This is an ephemeral execution environment located in a data center geographically close to you.

The difference in privacy is absolute and is guaranteed by contract: Cloudflare's architecture explicitly prohibits the use of customer data or queries to train AI models. It is a closed sandbox where no data leaves to feed the training of AIs.

When you ask a question, the server at the edge spins up in milliseconds, assembles your query, processes the hermeneutic interpretation using a secure language model, generates your response and, at the exact moment the connection is closed, the memory isolate is destroyed. The RAM is wiped clean. Neither my site, nor Cloudflare, nor the AI keep a record of what you asked, simply because the system was designed with structural amnesia. It is mathematically blind to your identity and incapable of remembering your secrets.

---

## Other risks (and it's not just hackers)

We have mentioned the possibility that criminals may have access to your personal data, which is a very real possibility given the ubiquity of PHP on almost all servers and hosting sites, but it doesn't end there.

If you think the only danger comes from hooded cybercriminals who want to extort you, and that governments and large corporations are there to protect you, God help you: you are far too naive.

Hackers steal your information to make a quick buck off you. Corporations and governments collect it and demand it for something much more dangerous: to restrict your freedom, profile you, and have the power to wreck you if you ever step out of the line they draw.

![Panopticon](panopticon.webp "Panopticon")

Let's talk about financial control and State surveillance. We have already seen how governments and financial elites have floated the idea of CBDCs (Central Bank Digital Currencies). And although in some places they have put it on moratorium due to public backlash, don't kid yourself: the idea is moving forward.

CBDCs are not simply "digital money" (you already use that with your current debit card); they are programmable money. It is money with a barcode tied to your legal identity, allowing a bureaucrat to dictate where, when, and on what you can spend it.

Imagine a scenario that has stopped being science fiction: the government of the day decides what is moral, what is acceptable, or what is "useful" for society. Imagine that one day they decide that consulting an oracle, studying ancient texts, or looking for answers outside the official narrative is "subversive," or they simply decide to block your transactions because they consider you are spending your money on bullshit.

If your identity is tied to your browsing history, or if the oracle you use forces you to pay with a credit card or a traditional bank account that leaves an indelible trail on a centralized server, you are one click away from being censored, canceled, or financially blocked.

The ultimate risk of not having privacy is not a criminal stealing your card; it's losing sovereignty over your own mind and your own money at the hands of the institutions that supposedly watch over you, but at the end of the day are also white-collar criminals.

---

## The final trap: The financial hijack

There is one last risk to cover. If El I Chingón doesn't charge you by commodifying your pain with advertising trackers (like the dinosaurs) nor charges you by stealing your secrets to train AIs (like the plastic oracles), it has to charge real money for the consultations. Maintaining a secure and private infrastructure has a cost, and besides, it's fair that I earn something for providing value to people, right?

The problem isn't paying; the problem is how the current industry forces you to pay.

Modern applications push you almost exclusively into a subscription model tied to your credit card, your PayPal account, or your Apple ID/Google Pay. When you pay like this, you lose your last stronghold of privacy: your financial anonymity. Your bank, tech corporations, and by extension, the State, know exactly that you are spending money on an oracle.

But beyond privacy, the subscription model is an aberration of usability, especially for a tool like this. There is a fundamental clash between the ancient nature of the I Ching and the extractive business model of Silicon Valley.

For some people, the I Ching is a last resort; something they turn to with extreme seriousness maybe once or twice a year, in the midst of an existential crisis or a critical crossroads. For others, who take it just as seriously, it is a daily use tool to study and produce synchronicities in their lives.

So why should an application condition your frequency of use with a monthly subscription? Why do you have to tie yourself to a recurring payment for something you might not use next month? What ends up happening is that you pay for months you don't use, or worse, you feel forced to "get your money's worth" out of the subscription by asking trivial questions that undermine the very act of a true oracular consultation.

Add to this what in web design is known as the "Hotel California effect": you can check out any time you like, but you can never leave. These platforms use dark patterns to hide the cancellation button or hit you with surprise auto-renewals. In the App Store reviews of these plastic oracles, the number one complaint exposes how flawed and hostile this software is: "This app keeps asking me to renew, but I already paid and it won't let me cancel!". It's a system designed to milk your card month after month.

---

## The prepaid model: Tokens and Web3 Wallets

For El I Chingón's privacy to be absolute and the user experience to be honest, the financial umbilical cord had to be cut. That's why I implemented a system of Gift Cards (prepaid vouchers).

It works exactly like a token in a casino or cash—it's bearer money. You buy your code, you enter it only when you're going to do a consultation and without having to provide any other data, that consultation is deducted from your token's balance, and that's it. Whether it takes you three days or three years to spend your credits is your business. There are no subscriptions, no "auto-renewals," and you don't have to fight with a customer service bot to unsubscribe. The end of the balance is the end of the contract. I can only hope that the oracle is truly useful to you so that you want to keep buying prepaid vouchers from me, and spread the word among your family and friends, but I don't force you either. Nothing forced is good.

More importantly, this alphanumeric code system allows me to offer totally blind payment methods. Soon, you will be able to buy your Gift Cards using decentralized networks, like the Lightning Network (Bitcoin) or Layer 2 (L2) networks with stable cryptocurrencies like USDT/USDC. For users, this means transacting without revealing their legal identity and without leaving traceable charges on their bank statements.

My balance database only has two operational columns: a random code of letters and numbers, and how many credits are left. The server does not know who bought the code. My decision to modularize the system into an independent payment rail from the consultation consumption mechanism is what makes this radical privacy possible.

---

## The Institutional Proof: Cloudflare and Amnesia by Contract

I have designed this system because I believe that divination and self-analysis should be sacred spaces, not data farms for corporate algorithms. But you don't have to blindly trust my word (no "Trust me bro" here). My privacy promise is backed by infrastructure-level contracts and the transparency of my code.

By using Cloudflare's Serverless architecture to process queries at the edge of the network, El I Chingón automatically inherits their strict enterprise Terms of Service (see the document cited in the references at the end of this article). Unlike consumer applications that use your data to improve their models, Cloudflare's agreements explicitly prohibit the use of customer queries (payloads) for Artificial Intelligence training. Protection against semantic vampirism is not just a good intention on my part; it is an ironclad legal guarantee from the network transporting your data.

Even if a government agency burst in tomorrow with a court order to find out what a user asked, the system operates under the principle of Institutional Blindness. I cannot leak, sell, or hand over to authorities what my infrastructure is mathematically designed not to retain.

Furthermore, I have made the logic of my "customs" public. I have published a reference implementation of my cloud servers at [https://github.com/ichingon/ichingon.github.io/blob/main/backend-reference/worker.js](https://github.com/ichingon/ichingon.github.io/blob/main/backend-reference/worker.js). Any developer can audit the core architecture of my applications and verify that the variable containing your intimate question is never inserted into a database. It is processed in RAM, generates your reading through our CSHC protocol, and is destroyed into the void in milliseconds.

Your oracle should be a source of wisdom you turn to, not your spy, nor your snitch, nor your financial jailer.

---

## References

* Cloudflare. (n.d.). Data usage. Cloudflare Docs. Retrieved October 24, 2026, from https://developers.cloudflare.com/workers-ai/platform/data-usage/

* PHP2Shell. (October 23, 2026). In Wikipedia, The Free Encyclopedia. [https://es.wikipedia.org/wiki/PHP2Shell](https://es.wikipedia.org/wiki/PHP2Shell)
