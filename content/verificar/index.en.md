---
title: "Authenticity Verification"
translationKey: "verificar"
description: "How to cryptographically verify that content from elichingon.com is authentic, unaltered, and authored by Dailingna Romero."
date: 2026-06-07
draft: false
showDate: false
showReadingTime: false
showWordCount: false
showAuthor: false
---

In an internet saturated with AI-generated content, *deepfakes*, impersonation, and plagiarism, an inevitable question arises: **how do you know that what you read or see truly comes from its original creator and not from an account impersonating them?**

This page explains how you can cryptographically verify that any article, video, or content published on `elichingon.com` or any of its platforms is authentic, unaltered, and was first published by Dailingna.

---

## Why do I cryptographically sign my content?

After all, "Dailingna Romero" or "El I Chingón" are unknown and relatively obscure entities on the internet (for now), but like [Hexagram 20 of the I Ching (Contemplation / Guan 觀)](https://elichingon.com/hexagramas/hex20/), this serves a dual purpose that reflects the very nature of the hexagram: the act of contemplating and the condition of being contemplated.

### The act of contemplating (as a content consumer)

As a content consumer, I dislike having no way to verify that what I read or see truly comes from the source it claims to be.

I'm not talking about detecting whether content is AI-generated - after all, Dailingna Romero is a digital avatar and her videos are AI-generated. What matters is knowing whether **the ideas expressed truly come from Dailingna** and not from someone else using my image and voice to express their own ideas.

Today it's easy to create a channel associated with a character (real or fictional) and put words into their mouth that they never said. You see videos of Richard Feynman, Neville Goddard, Einstein, or the "Kenzo Guy" everywhere, and it's becoming increasingly difficult to distinguish between what the character actually said and what the video creator is putting into their mouth.

On YouTube, automatic AI detection has become standard, but that's not enough. What matters is not whether a video was AI-generated, but **whether the ideas it expresses are authentic and come from the alleged author**.

I want you to have tools to verify for yourself that what you read truly comes from me, without having to blindly trust any platform. The cryptographic signature guarantees that no one can alter the content after publication without invalidating the signature. The timestamp on the Nostr network proves when I first published something, which is useful for proving original authorship in case of plagiarism.

### The condition of being contemplated (as a content creator)

In a world where anyone can clone voices, faces, and writing styles with AI, cryptography is the only reliable proof of authenticity. We are in an existential crisis of the internet itself. Dead Internet Theory and the proliferation of deepfakes have brought us to a point where we can no longer trust our own eyes and ears to discern true authorship.

My hope in implementing this is that other content creators will start doing the same and thus help reverse this situation. I want to teach about the importance of having **digital sovereignty** so that everyone can protect their content without relying on corporations like YouTube, Twitter, or Medium to prove that I am who I say I am.

My identity lives on an open, decentralized protocol, not on any company's servers.

---

## What is a cryptographic signature?

Every article I publish is accompanied by a **unique mathematical signature**. This signature serves three functions:

1. **Proves authorship**: Shows that the content was created by this specific digital identity (`dailingna@elichingon.com`).
2. **Guarantees integrity**: If someone modifies even a single word, space, or comma, the signature becomes invalid.
3. **Timestamps**: Immutably records when the content was originally published.

It is the digital equivalent of a **wax seal** that cannot be forged, copied, or broken without leaving evidence.

---

## How does it work technically?

The process is based on two open standards:

### 1. Nostr (Notes and Other Stuff Transmitted by Relays)
A decentralized protocol that allows signing messages with cryptographic keys. It does not depend on any company, government, or central server.

### 2. NIP-05 (Identity Verification)
A standard that links a Nostr public key to a domain name. In this case:

dailingna@elichingon.com → npub1rfqz5sqv6plxpm3lqfu35q30d7p2m2mt38t7qz6309fxm7e02mrqjxlx92

You can verify this link yourself by visiting:

[https://elichingon.com/.well-known/nostr.json](https://elichingon.com/.well-known/nostr.json)

---

## How to verify an article

At the end of each article on this site, you will find a block similar to this:

> 🔐 CRYPTOGRAPHIC PROOF OF AUTHORSHIP
> This content is created and officially published by Dailingna Romero.
> 
> 🔗 Official URL: https://elichingon.com/article/...
> 🔐 Verified Nostr identity: dailingna@elichingon.com
> 📜 Nostr verification note: https://primal.net/e/note1ues5g2y8lpjlpsg7qx40lzwk67ql08j2cmree44lkpxhew04rtdstev548
> 
> To verify that this content has not been altered nor is a deepfake,
> click the Nostr link above and verify that the signed URL
> exactly matches the URL of this content.
---

## YouTube video verification

For videos published on YouTube, the video description contains:

- Official video URL on Dailingna Romero's channel.
- Link to the Nostr note certifying authenticity.
- Cryptographic signature of the URL.

## How to spot a deepfake?

If you see a video that looks like me on another channel, verify:

- Does the description contain a link to a signed note on Nostr?
- Does the link point to dailingna@elichingon.com with a verification check?
- Does the signed URL match the URL of the video you are watching?

If the answer to any of these questions is no, it is very likely a deepfake, unauthorized content, or plagiarism.

## What do I do if I find fake content?

If you discover a video, article, or post that uses my name, image, or voice without authorization:

1. Verify that it does not have a valid cryptographic signature.
2. Report the content on the platform where it is found (YouTube, social media, etc.) for impersonation or copyright infringement.
3. Share it with me through my official channels so I can take legal action if necessary.

All content on this site is under a **Creative Commons Attribution 4.0 (CC BY 4.0)** license. You may share and adapt it, but you must:

- Give explicit credit to `Dailingna Romero / elichingon.com`.
- Not use the cryptographic signature to pass off altered content as original.

For more information, see [https://elichingon.com/en/licenses/](https://elichingon.com/en/licenses/)

## For other content creators

If you are a creator and want to implement cryptographic verification in your own work, the Nostr protocol is **free, open, and no-cost**.

### Resources to get started:

- [Official Nostr documentation](https://github.com/nostr-protocol/nostr)
- [NIP-05: DNS-based identity verification](https://github.com/nostr-protocol/nips/blob/master/05.md)
- [NIP-23: Long-form articles](https://github.com/nostr-protocol/nips/blob/master/23.md)
- [NIP-94: File storage](https://github.com/nostr-protocol/nips/blob/master/94.md)

### Recommended tools:

- **Amethyst** (Android): Mobile Nostr client.
- **Primal** (Web/Mobile): Client with excellent NIP-05 verification.
- **Coracle** (Web): Minimalist web client.
- **nostr-tools** (JavaScript): Library for developers.

## The future of the internet is verifiable

This is not just my content. It is an **authenticity standard** that any creator can adopt.

In a world where AI can generate text, images, audio, and video indistinguishable from reality, cryptography becomes the only way to prove that something was created by whom it claims to have been created.

It's not about trusting me. It's about being able to **verify for yourself**.

---

**Official identity:**

- **NIP-05:** `dailingna@elichingon.com`
- **NPub:** `npub1rfqz5sqv6plxpm3lqfu35q30d7p2m2mt38t7qz6309fxm7e02mrqjxlx92`
- **Website:** [https://elichingon.com](https://elichingon.com)