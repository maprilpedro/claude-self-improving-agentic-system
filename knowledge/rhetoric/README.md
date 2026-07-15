# Rhetoric — routeur du check à la demande

> **Ce dossier n'est pas à lire en entier.** C'est un routeur pour un usage précis : quand Pedro rédige une réponse et demande explicitement « une règle de rhéto s'applique ici ? », on lit cette table, on sélectionne 3-5 règles candidates, et on rend un verdict par règle. Retrieval piloté par la demande, jamais automatique.

## Comment l'utiliser (l'invocation)

Déclencheurs explicites, sur un draft ou un échange : **« check rhéto »**, **« une règle s'applique ? »**, **« passe ce draft au filtre rhéto »**, **« quelle figure/tactique ici ? »**.

Sortie attendue, par règle candidate :
- ✅ **s'applique** → comment l'utiliser sur CE draft
- ⚠️ **se retourne contre toi ici** → pourquoi, dans ce contexte précis
- — **pas pertinente**

**Garde-fou voix.** Chaque fiche porte un champ `Compatible voix Pedro : charpente | ornement(⚠️)`. On ne propose à l'usage que la **charpente** (ce qu'on dit, l'ordre, le cadrage). L'**ornement** (période, figures de son, style littéraire) entre en conflit avec ses règles de voix (plain English, pas d'aphorismes, pas de tirets) → à signaler mais rarement à appliquer. Voir [[feedback_draft_in_pedros_voice]].

## Table de routage — situation → règles à checker

| Situation dans le draft | Règles candidates (fichier) |
|---|---|
| **Répondre à une objection / un désaccord** | Homme de fer · Dissociation de notions · Désaccord de valeurs · Recadrage en 4 temps · Prolepse · Face au procès d'intention · Réponds à une image par une image · Fermeture (opposer du même niveau) — `ferry.md`, `classical-scaffold.md` |
| **Poser / établir un problème** | Partir du problème · Montrer avant de dire · Quantitatif ET qualitatif · Montre un cas n'argumente pas · Structure en 3 temps — `ferry.md` |
| **Demander une action** | Finir par une action concrète · Un seul appel à l'action mesurable · Convaincre n'est pas persuader · Choisis ton levier d'influence · Choisir le registre (vendeur) — `ferry.md` |
| **Structurer / ordonner / couper** | Règle de trois · Chaque partie milite pour la suivante · Fusil de Tchekhov · Antithèse d'idées · Test de vérité / validité · Scanner les 6 sophismes — `ferry.md` |
| **Émotion / ethos / prise de parole publique** | Concéder l'émotion attendue · De l'ombre à la lumière · Empathie = somme nulle · Débat public = ethos pas logos · Vraie bienveillance · Amplification épidictique · Étiquette positive — `ferry.md` |
| **Cadrage / pouvoir des mots** | Dissociation de notions · Qualification / dénomination · Présupposition · Question oratoire · Transfert (choisir le lieu) · Paradoxe — `ferry.md`, `classical-scaffold.md` |
| **Choisir le type d'argument / de discours** | Les 3 genres (délibératif / judiciaire / épidictique) · Exemple · Précédent · Argument d'autorité (+ retourner celle de l'adversaire) · Analogie · Enthymème · Alternative / dilemme — `classical-scaffold.md` |

## Fichiers

- **`ferry.md`** — Victor Ferry, *12 leçons de rhétorique pour prendre le pouvoir*. 37 règles de charpente, une par tiroir, testables contre un draft. La source la plus opérationnelle des trois.
- **`classical-scaffold.md`** — ossature classique (digest de notes sur Aristote / Cicéron / Quintilien / Perelman) : les 3 genres, les 4 parties, les types d'arguments, l'enthymème, les figures à fonction argumentative, les 3 principes (non-paraphrase, fermeture, transfert).
- **`viktorovitch.md`** — Clément Viktorovitch, *Le pouvoir rhétorique*. **Cadrage + définition seulement** : le fichier source est un aperçu de 49 pages (intro + table des matières), pas le corps du livre. À compléter si Pedro fournit le PDF complet.

## Sources ingérées (2026-07-15)

| Source | État du fichier | Portée ingérée |
|---|---|---|
| Ferry, *12 leçons de rhétorique pour prendre le pouvoir* | **Complet** (70K mots) | Intégrale, 12 leçons → 37 fiches |
| Viktorovitch, *Le pouvoir rhétorique* (Seuil, 2021) | **Aperçu 49 p** (intro + TOC) | Définition + cadrage seulement, corps absent |
| Aristote, *La Rhétorique* (fichier `.doc`) | **Digest de notes de cours**, pas le texte primaire | Ossature classique (genres, parties, arguments, principes) |

## Chevauchements connus (pour ne pas dupliquer)

Beaucoup de ces règles recoupent des entrées existantes. On cite l'entrée existante plutôt que de la refaire : [[feedback_bertrand_concrete_first]] (montrer avant de dire), [[feedback_separate_facts_from_proposals]] (test de vérité/validité), [[The Game Itself — Position Over Merit]] (cessez de citer / procès d'intention), la pyramide de Minto / [[pyramid-principle]] (en tension avec « partir du problème » et « structure en 3 temps » — arbitrer selon l'audience), Greene / `interpersonal/` (homme de fer, cadre, ethos public). Le net-nouveau de la rhéto = la **granularité tactique** (la figure précise à dégainer sur une phrase précise), pas les grands principes déjà en base.
