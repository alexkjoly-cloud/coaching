# SUIVI CLIENTS — fiche de pilotage

**Ce fichier est la mémoire du suivi.** Une conversation qui démarre sans contexte
lit ce fichier et sait quoi faire. Il se met à jour à chaque décision.

Dernière mise à jour : **21/09/2026**
Méthode appliquée : skill `methode-alex`.

🔴🔴 **LE SKILL SE REMET À ZÉRO, PAS CE FICHIER.** Le 20/09 j'ai écrit trois règles
dans `SKILL.md` (mot-témoin passé à `suivi-20`). Le 21/09 le skill était revenu à
`contraintes-13` : le dossier `~/.claude/skills/synced/` est **resynchronisé depuis
le serveur à chaque session**, donc tout ce qu'on y écrit depuis une session Claude
Code disparaît. 🔑 **Une règle client ne se note que dans `SUIVI.md`, qui est versionné
dans le dépôt.** Pour modifier le skill pour de vrai, c'est Alexandre qui l'édite
depuis claude.ai.

---

## LA ROUTINE DU LUNDI (armée le 21/09/2026)

`trig_01Wea6LLpGp8HinUDRFUKL1t` — « Bilan hebdo coaching — Alexia & Jean (lundi) ».
Cron `0 6 * * 1` en UTC, soit **8 h à Lyon l'été, 7 h l'hiver**. Elle ouvre une
session neuve à chaque fois, avec notification push et mail.

Ce qu'elle fait : charge le skill, lit ce fichier, lit la Sheet, fait les deux bilans,
pousse les modifs, et rend à Alexandre **les deux messages prêts à envoyer** plus un
point en bullet points. ⛔ **Elle ne contacte jamais un client directement.**

🔴 **Limite connue : la routine n'embarque aucun connecteur.** Les sessions qu'elle
ouvre n'ont donc ni Google Drive ni Gmail, et **ne peuvent pas lire la Sheet**. Tant
que ce n'est pas réglé, la routine sert de rappel et le bilan se fait dans une session
normale. Pour la réparer, Alexandre la recrée depuis **claude.ai → Routines**, qui
permet d'y attacher les connecteurs.

---

## LA DIÈTE VIT DANS L'APPLI, PAS DANS UN MESSAGE

Sa demande du 20/09 : les clients doivent retrouver leur diète **dans l'onglet Diète
de leur appli**, au même endroit que leurs séances. Jamais en PDF, jamais en artifact,
jamais dans un message WhatsApp.

Le niveau de détail dépend de la formule :

| Client | Ce que l'onglet contient |
|---|---|
| **Alexia** (suivi + nutrition) | macros · **7 journées différentes** bâties sur sa liste de courses · les recettes · la liste de courses · la cible de poids |
| **Jean** (suivi) | macros · **7 journées** en version simple · la cible de poids |

📌 **Sept journées différentes, jamais trois ou quatre qui tournent.** Sa correction :
répéter les menus tue l'adhérence d'un client qui paie pour de la nutrition.
📌 Le bloc **objectif de la semaine** est en haut de l'onglet, il recalcule la cible
tout seul à partir du bilan.

---

## LA PROCÉDURE HEBDOMADAIRE

À faire le **lundi**, pour chaque client actif.

1. **Lire la Sheet.** `SUIVI FINAL !`, id `1KVVjEU4onfNoesgMpgqpj7ZghiggfGJ9j_MreO7CbDQ`.
   ⚠️ `read_file_content` tronque vers 226 lignes par onglet : passer par
   `download_file_content` en `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`,
   décoder le base64, lire avec openpyxl.
   Format des clés : `perf|WW|séance|exo|série` · `bilan|WW|OO-champ` · `note|séance|WW`
   · `corp|WW` · `poids|WW` · `mens|ZZ|col`.
   📌 **Le tour de taille de certains clients est une ligne `perf` sur la séance `corps`**,
   exercice « Tour de taille (cm) ». Ne pas le filtrer par erreur.

2. **Lire les perfs exercice par exercice.** On cherche une seule chose :
   **qui a touché le haut de la fourchette sur toutes ses séries.** Ceux-là montent
   d'un cran au prochain passage. Ceux qui stagnent trois semaines sur la même charge
   sans atteindre le haut, on regarde la récupération avant de toucher au volume.

3. **Lire le bilan.** Poids, tour de taille, sommeil, énergie, fatigue, ressenti.
   Le poids se lit en **moyenne de la semaine**, jamais sur un chiffre isolé.

4. **Décider la diète** avec la règle d'ajustement du client (plus bas). Si la cible
   change, **réécrire les journées** de l'onglet Diète, pas seulement le chiffre.

5. **Écrire la réponse au bilan.** Ton d'Alex, tutoiement, concis, zéro marqueur IA.
   Alexandre veut **le message final prêt à envoyer**, pas un rapport.

6. **Pousser.** Branche `claude/weekly-coaching-reviews-ecbvwm` puis `main` en
   `--ff-only`, et vérifier que les quatre SHAs concordent.

⚠️ **Ne jamais écrire dans l'appli d'un client pour tester** : la saisie part dans la
Sheet à son nom et pollue son suivi.

---

## ALEXIA M

| | |
|---|---|
| Formule | Suivi 3 mois + nutrition, **300 € payés**, mais **un seul mois réglé** → appli calée sur **4 semaines** |
| Contact | Instagram `vanuzzaaa` · ravanuzzaa@gmail.com · pas de numéro |
| Profil | 26 ans, 166 cm, **73 kg au départ**, bureau, 7 000 pas, 4 séances |
| Objectif | Perte de gras, « un beau physique ». Priorité déclarée au **fessier**. |
| Bilan | **Lundi** |
| Appli | `suivi_alexia.html` |

**Entraînement.** 4 séances, 64 séries. 3 Lower + 1 Upper, parce que 3 de ses 5
priorités sont en bas. Chaque séance fait 16 séries et 6 séries lourdes, pour que
l'effort soit le même d'une séance à l'autre : elle l'a demandé explicitement.
Grand fessier 14 séries la semaine sur quatre angles, moyen fessier 8, ischios 9,
quadriceps 8, dos 12.

**Diète.** 1 700 kcal · 147 g de protéines · 140 de glucides · 57 de lipides.
Maintenance estimée 2 150 (Mifflin 1 477 × 1,45), donc **−450 kcal**, soit 0,5 kg
par semaine. 7 journées différentes construites sur **sa liste** (voir plus bas).

**Règle d'ajustement** (appliquée automatiquement par l'appli, à confirmer à la main) :
- perte < 0,3 kg/semaine → **−150 kcal** en glucides
- perte > 0,8 kg/semaine → **+150 kcal**
- entre les deux → on ne touche à rien
- **les protéines ne bougent jamais**

**Sa liste d'aliments, donnée le 19/09.** Adore : tomates, courgettes, épinards,
champignons, concombre, flageolets, pommes de terre, riz, pâtes, tous les fromages,
viande rouge, poulet, abats, tous les poissons et fruits de mer (gros kiff saumon et
saumon fumé), fruits rouges, kiwi, raisin, banane, mangue, kaki, flocons d'avoine,
muesli, beurre de cacahuète. **Elle mange du skyr** (confirmé le 20/09).
Plats préférés : pâtes carbo, lasagnes, **banana bread qu'elle aime préparer**.
⛔ **Déteste le brocoli.** Ouverte à tout le reste.

**Ce qui manque encore :** ses **mensurations et ses photos de départ**. Relancer
tant qu'on ne les a pas, sans ça il n'y aura rien à montrer à la fin.

---

## JEAN ESCLAPEZ

| | |
|---|---|
| Formule | **Un mois réglé** → appli calée sur **4 semaines** |
| Contact | 06 46 60 57 77 · esclapez2007@gmail.com |
| Profil | 19 ans, 171 cm, **71 kg**, On Air, 5 séances |
| Objectif | **« 75 kg sec »** → recomposition, puis prise de masse propre |
| Bilan | **Dimanche** |
| Appli | `suivi_jean.html` |

**Entraînement.** 5 séances, 70 séries. Push / Pull / Legs / Upper / Lower.
Il stagne depuis des mois avec beaucoup de volume et peu d'intensité : **on a baissé
le volume et monté la proximité de l'échec.** Plusieurs muscles sont sous le plancher
de 12 séries, **c'est volontaire** et ça vaudra jusqu'à ce qu'il choisisse ses
priorités.
⛔ **Interdits, version du 22/09** : **squat barre libre et hack squat**, et rien
d'autre. Ses mots : *« j'ai aucun exo que j'aime pas sauf squat et hack squat »*.
✅ **Le développé militaire barre n'est donc plus interdit** (il le détestait en juin,
plus en septembre).
✅ **Le soulevé de terre roumain est confirmé OK.** La question ouverte depuis juin
est fermée, il reste au programme.
⚠️ Le hack squat qui saute coûte cher maintenant que le quadriceps est sa priorité :
il ne reste que la presse et le leg extension comme gros moteurs.

📅 **Il démarre officiellement la semaine du 22/09/2026.** Semaine 1 = cette
semaine-là, les 4 semaines payées courent jusqu'au 19/10.

🎯 **Ses muscles prioritaires, donnés le 22/09** : **pectoraux, sangle abdominale,
cuisses (« surtout ») et dos.** Quatre, donc, alors qu'on en demandait deux ou trois,
et « surtout » met le quadriceps devant.
⚠️ **Ça ne rentrait pas dans 70 séries.** Monter les quatre au plancher de 12
demandait +26 séries, soit un programme à 96. **Arbitrage tranché par Alexandre le
22/09 : cuisses et pectoraux au plancher, le dos aussi haut que le budget le permet,
les abdominaux restent secondaires.** Son « surtout » sur les cuisses a fait la
hiérarchie, et la sangle abdominale se verra par le tour de taille, pas par le volume.

**Programme v2, poussé le 22/09 — 72 séries.** Séries directes par semaine :

| Muscle | Avant | Maintenant |
|---|---|---|
| Pectoraux | 9 | **12** ✅ |
| Quadriceps | 9 | **12** ✅ |
| Grand dorsal | 8 | 9 |
| Milieu du dos | 6 | 9 |
| Abdominaux | 2 | 6 |
| Ischios | 9 | 6 |
| Mollets | 4 | 3 |
| Triceps (direct) | 5 | 4 |
| Biceps (direct) | 5 | 2 |

Ce qui a payé la hausse : adducteurs supprimés, leg curl allongé supprimé, curl
marteau supprimé, et les séries de biceps, triceps, mollets et deltoïdes rabotées.
Biceps et triceps restent autour de 8 à 9 séries **effectives** une fois l'indirect
compté pour une demi-série, donc ils ne sont pas abandonnés.

⚠️ **Le dos ne peut pas atteindre 12 par tissu sur 5 séances** sans casser autre
chose. Grand dorsal et milieu du dos sont à 9 chacun, au maximum finançable.
📌 Ajouts : **fente bulgare** en Lower (le quadriceps a perdu le hack squat),
**écarté à la poulie** en Upper, **rowing machine assis** en Pull, **crunch machine**
et **relevé de jambes** en Legs.

**Diète.** 2 500 kcal · 146 g de protéines · 303 de glucides · 67 de lipides.
Maintenance estimée 2 500 (Mifflin 1 689), donc **au maintien, en recomposition**.
⚠️ **Sa maintenance est incertaine entre 2 320 et 2 700** : il a coché 10 000 pas ET
« légèrement actif ». Le chiffre est un pari au milieu, ce sont ses pesées qui
trancheront.

**Règle d'ajustement** :
- tour de taille +0,5 cm ou plus → **−150 kcal** en glucides
- ni le poids ni la taille ne bougent → **+150 kcal** (il doit finir par prendre)
- poids stable et taille qui descend → **on ne touche à rien**, c'est le but
- **les protéines ne bougent jamais**

📌 **Lui redire que la balance ne bougera presque pas.** En recomposition c'est le
tour de taille qui parle. Sans ça il croira qu'il ne se passe rien.

**Ce qui manque encore :** ses **mensurations**, qu'il fait ce week-end (annoncé le
22/09), et ses **photos de départ**.

---

## CE QUE L'APPLI FAIT TOUTE SEULE

Depuis le 20/09, l'onglet **Diète** des deux applis porte un bloc **objectif de la
semaine** qui suit le sélecteur de semaine. Il lit le **poids** et le **tour de
taille** saisis dans le bilan (ou à défaut dans l'onglet Corps), compare les deux
dernières semaines renseignées et **recalcule les calories** avec la règle du client.

⚠️ **Il recalcule la cible, il ne réécrit pas les sept menus.** Quand la cible bouge,
c'est à nous de refaire les journées et de pousser.

⚠️ Le stockage local est partagé entre toutes les applis (même domaine, clés sans
nom de client). Sans conséquence pour les clients, qui n'ouvrent que la leur.
**La Sheet reste la source de vérité.**

---

## LA TABLE CIQUAL

Les diètes sont calculées sur la **table CIQUAL 2025 officielle** fournie par
Alexandre le 20/09 (`Table_Ciqual_2025_FR_2025_11_03.xls`, 3 485 aliments).
Colonnes utilisées : énergie règlement UE 1169/2011 (kcal), protéines N × Jones,
glucides, lipides.

🔴 **Tout se pèse cru et se calcule sur la ligne CRU.** La mention va **sur chaque
ligne** de la diète, pas en note de bas de page. Rien à mentionner sur ce qui n'a pas
d'état cru : conserves égouttées, laitages, pain, fruits, huile.

📌 **Le skyr n'est pas dans CIQUAL.** Valeur d'étiquette donnée par Alexandre :
**60 kcal · 10 g de protéines · 4,9 de glucides · 0,3 de lipides.**

⚠️ **ciqual.anses.fr et data.gouv.fr sont bloqués par le proxy** depuis
l'environnement d'exécution. Pour revérifier une valeur, il faut qu'Alexandre
renvoie le fichier.

---

## CLIENTS INACTIFS

- **Max** — suivi terminé. Ne plus le traiter. Son appli porte encore un onglet
  Macros avec des chiffres jamais validés par Alexandre : à retirer si son appli
  reste en ligne.
- **Léo** — mois 2 terminé le 3 septembre. Il s'entraînait encore seul mi-septembre.
  Statut à clarifier avec Alexandre.
- **Julie, Romain, Théo** — voir l'onglet `Formules` de la Sheet, plusieurs dates de
  fin y sont fausses.

---

## L'ONGLET FORMULES EST À CORRIGER

Connu et pas encore fait : Alexia n'y a **aucune ligne**, Jean y figure encore sur
son ancien cycle (23 juin au 3 août), Léo est noté « 1 mois », Max a une fin au
29 juillet, et `alexandre_test` porte une durée parasite.
