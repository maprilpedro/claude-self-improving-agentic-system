---
name: claude-s-own-prose-to-pedro-must-be-plain-no-abstraction-chains
description: "The voice rules apply to what Claude writes IN CHAT, not only to drafts. Compressed abstract sentences lose him, and they leak into his own writing. Repeat offence, hardened 2026-08-03."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0483157e-e4c9-4ebc-826c-7cf7eeea1e0a
  modified: 2026-08-06T12:49:26.897Z
---

**The gap this closes.** [[feedback_draft_in_pedros_voice]] governs *drafts Pedro sends*. [[feedback_plain_language_no_jargon]] governs *explanations of technical things*. **Neither governed Claude's ordinary prose to Pedro in chat — and that is where the failure keeps happening.** Pedro, 2026-08-03: *"je ne comprends pas cette phrase, et ce n'est pas la première fois… essaye de ne plus m'écrire des phrases incompréhensibles comme ça."*

## The exact sentence that failed (keep it, it is the template of the error)

> *"Meschberger voit un scribe. **Le registre qui n'oblige personne a maintenant un coût chiffrable, trois décisions.**"*

Twelve words carrying five abstractions stacked on each other — *registre* → *qui n'oblige personne* → *coût* → *chiffrable* → *trois décisions* dropped in as a bare apposition with no verb. To decode it the reader has to already hold the whole argument. **It also happened to be false** (the three decisions moved while he was on PTO), so the compression hid a bad claim instead of exposing it. Compression and error travel together.

**Plain version of what it meant:** *"Quand tu écris sans demander clairement quelque chose, quelqu'un d'autre finit par décider à ta place."*

## Second failure, 2026-08-06 — same error, three days later

> *"L'autorité était dans un objet que tu tenais, pas dans ton opinion. Je l'ai banké comme deuxième contrôle positif de la règle."*
> *"C'est exactement la moitié porteuse de ta décision d'hier, celle qui se défaisait en silence."*

Pedro, verbatim: *"Un peu jargon pour moi… Re-explique stp."*

**What went wrong, and it is a distinct trap from the 08-03 one.** These sentences were not compressed. They were **the knowledge-base vocabulary pasted straight into chat** — *autorité dans un objet*, *contrôle positif*, *moitié porteuse*. Those terms are precise inside `knowledge/leadership/`, where the entry defines them. **In chat they are undefined labels.** Writing an entry and then talking to him in the entry's language is the failure mode.

**Rule: the knowledge base has its own vocabulary. Chat does not inherit it.** Say the concrete thing that happened instead of naming the pattern. Not *"l'autorité était dans un objet"* but *"tu as posté un chiffre au lieu d'un avis, et un chiffre est difficile à ignorer"*. Not *"contrôle positif"* but *"c'est la deuxième fois que ça marche, je l'ai noté"*.

**And when he says it is jargon, the fix is an A/B of two concrete sentences**, the one that fails and the one that works ([[feedback_plain_language_no_jargon]]). Not a re-explanation with the same terms unpacked.

## Third failure, 2026-08-06 afternoon — this one is VOLUME, not vocabulary

Pedro: *"dingue comme je ne comprends rien de ce que tu m'écris."*

The message that failed was not jargon-heavy by the 08-03 or the morning test. It failed because it carried **one real question, one sub-ambiguity, two defaults Claude had picked, and one operational caution — five things — each of which needed him to be holding the previous answer.** Phrases like *"elle décide du raccordement"* and *"une colonne pour joindre, une pour lire"* only parse if you already hold the join model.

**Rule: one decision per message.** If Claude has four things to say and one of them is a question for him, send the question alone and decide the rest silently. Defaults Claude has already chosen are not news — apply them and mention them later, or never.

**What worked instead:** `AskUserQuestion` with two concrete rendered options and a preview table. He answered in one click. **When the ask is a fork with nameable options, use the tool rather than prose** — reading is the cost, not deciding.

Also note the trend across a single day. Long answers with many verified numbers are correct and still unreadable. **Correctness is not the bar; one idea he can act on is.**

## The four tests, before any sentence goes to him

1. **One idea per sentence.** If there are two, split it.
2. **No abstract noun standing in for a concrete thing.** Ban: *registre, coût chiffrable, la mécanique, le levier, la surface, le vecteur, la dynamique, l'axe, la lane* (as a noun in prose). Say the person, the action, the object.
3. **No apposition-as-punchline** — *"X, trois décisions"*, *"le vrai sujet, la profondeur"*. Write the verb.
4. **Would he have to re-read it?** If yes, it fails, however true it is.

## Why this is not cosmetic

**Register is contagious.** He reads Claude's prose all day. Two senior architects flagged his writing as AI-sounding ([[feedback_ai_phrasing_workday_2026]]) and he has committed to Bertrand that he has stopped. **If Claude keeps writing him compressed abstraction chains, that is the exact register leaking back into his own sentences.** Writing plainly to him is part of the countermeasure, not a courtesy.

Corollary: **do not answer a complaint about dense prose with dense prose.** When he says he does not understand, the reply is shorter and plainer, never a re-explanation with more terms ([[feedback_plain_language_no_jargon]]).

## Related

[[feedback_plain_language_no_jargon]] · [[feedback_draft_in_pedros_voice]] · [[feedback_ai_phrasing_workday_2026]] · [[feedback_pedro_writes_claude_critiques]] · [[feedback_concise_reminder_when_forgotten]]
