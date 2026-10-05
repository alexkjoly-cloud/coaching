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

📣 **Depuis le 05/10, le client doit envoyer un message quand son bilan est rempli.**
Bandeau rouge en tête de l'onglet Bilan (Jean, Alexia) : *« N'oublie pas de m'envoyer
un message quand tu as fait ton bilan. Sans ça, je ne le fais pas. »* C'est la règle
d'Alexandre, pas une menace en l'air : pas de message, pas de bilan.

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

✅ **Mensurations de départ reçues le 21/09** : poitrine 107 · **taille 86** · hanches
106 · bras 34 / 34 · cuisses 64 / 63 · mollet G 38. **Poids 73,7 kg** (départ annoncé
73). La taille à 86 cm est le repère qui pilotera tout le reste.

**Ce qui manque encore :** ses **photos de départ**.

🔴 **État au 27/09 : elle s'est arrêtée.** Deux séances seulement, Lower A le 20/09 et
Upper A le 21/09, puis **plus rien pendant six jours**. Aucun bilan rempli. C'est le
point à traiter avant toute question de diète ou de charges.

---

## JEAN ESCLAPEZ

| | |
|---|---|
| Formule | **Un mois réglé** → appli calée sur **4 semaines** |
| Contact | 06 46 60 57 77 · esclapez2007@gmail.com |
| Profil | 19 ans, 171 cm, **74,9 kg** sur sa balance au 27/09 (le formulaire disait 71), On Air, 5 séances |
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
| Milieu du dos | 6 | 6 |
| Abdominaux | 2 | **9** |
| Ischios | 9 | 6 |
| Mollets | 4 | 3 |
| Triceps (direct) | 5 | 4 |
| Biceps (direct) | 5 | 2 |

Ce qui a payé la hausse : adducteurs supprimés, leg curl allongé supprimé, curl
marteau supprimé, et les séries de biceps, triceps, mollets et deltoïdes rabotées.
Biceps et triceps restent autour de 8 à 9 séries **effectives** une fois l'indirect
compté pour une demi-série, donc ils ne sont pas abandonnés.

⚠️ **Le milieu du dos plafonne à 6 séries, et c'est structurel.** Il n'y a que deux
séances qui tirent, Pull et Upper, donc deux créneaux, donc 6 séries au maximum sans
répéter le même mouvement.
🔴🔴 **23/09 — SA CORRECTION : J'AVAIS MIS DEUX FOIS LE MÊME EXERCICE DANS PULL.**
« Tirage horizontal coudes ouverts » et « Rowing machine assis, coudes ouverts » sont
le même tirage horizontal coudes ouverts sur le milieu du dos, à l'outil près. Je les
avais mis pour afficher 9 séries de milieu du dos. Ses mots : *« il faut virer l'un
des deux parce que c'est la même chose, la grosse erreur »*.
📐 **23/09 — LE REPÈRE : 5 EXERCICES PAR SÉANCE.** Sa validation après la correction
du doublon : *« normalement ça donne 5 exercices sur le push et 5 sur le pull, c'est
exactement ce qu'on veut »*. Push, Pull, Legs et Lower sont à 5. **Upper reste à 6**,
parce qu'elle reprend tout le haut du corps ; exception assumée, à lui reproposer si
elle devient un problème.

🔑 **Changer d'outil ne fait pas un exercice différent.** Avant d'ajouter un exercice
pour remplir un compteur, vérifier qu'il attaque le muscle sous un autre angle, pas
avec une autre machine. Un compteur qu'on gonfle avec un doublon ment sur le
programme.
✅ Le doublon a été retiré, les 3 séries sont parties sur les abdominaux en Lower
(crunch à la poulie), qui sont une de ses priorités déclarées et étaient les plus bas.

📌 Ajouts : **fente bulgare** en Lower (le quadriceps a perdu le hack squat),
**écarté à la poulie** en Upper, **crunch machine** et **relevé de jambes** en Legs,
**crunch à la poulie** en Lower.

**Diète.** 2 500 kcal · 146 g de protéines · 303 de glucides · 67 de lipides.
Maintenance estimée 2 500 (Mifflin 1 689), donc **au maintien, en recomposition**.
⚠️ **Sa maintenance est incertaine entre 2 320 et 2 700** : il a coché 10 000 pas ET
« légèrement actif ». Le chiffre est un pari au milieu, ce sont ses pesées qui
trancheront.

**Règle d'ajustement** :
- tour de taille +0,5 cm ou plus → **−150 kcal** en glucides
- ni le poids ni la taille ne bougent → **+150 kcal** (il doit finir par prendre)
- poids stable et taille qui descend → **on ne touche à rien**, c'est le but
- 🆕 05/10 : **poids qui descend de 0,5 kg ou plus** → on ne touche pas aux calories la
  première semaine, il mange la diète en entier ; **si ça recommence la semaine
  suivante → +150 kcal**. Il ne doit pas maigrir, l'objectif est le « sec » à poids égal.
- 🆕 05/10 : **sans tour de taille, pas de +150.** Un poids stable ne dit rien tout
  seul en recomposition. L'appli affiche « il manque ton tour de taille » et ne bouge pas.
- **les protéines ne bougent jamais**

📌 **Lui redire que la balance ne bougera presque pas.** En recomposition c'est le
tour de taille qui parle. Sans ça il croira qu'il ne se passe rien.

**Ce qui manque encore :** ses **mensurations** (promises pour le week-end du 26/09,
toujours rien au 27), ses **photos de départ**, et **son bilan**.

✅ **État au 27/09 : il s'entraîne.** Push A le 22, Pull A le 23, Legs et Upper le 26,
Lower entamé le 27. Il tient le rythme.
📌 **Il saisit en différé.** Le 26/09 entre 13 h 37 et 13 h 39 il a rentré d'un coup
des séries de quatre séances différentes, puis il a fait son Upper de 13 h 46 à
14 h 04. **Ça casse l'analyse des temps de repos** sur les lignes rattrapées, qui
sont filtrées, et ça décale les dates de séance. À lui redire.
🔎 **À traiter au premier bilan :**
- **Relevé de jambes 15, 15, 15** : haut de fourchette sur les trois séries, **il
  monte en charge** au prochain passage (lest).
- **Développé couché machine 40 kg × 12, 12, 10** : deux séries en haut de fourchette,
  pas la troisième, donc on ne touche pas encore.
- ⚠️ **Deux saisies aberrantes** : leg curl assis 57 kg × **2** au milieu de deux
  séries à 12, et écarté à la poulie **1,5 kg** après deux séries à 12,5. Des fautes
  de frappe, à confirmer avant de les lire comme des perfs.
- ⚠️ **Presse à cuisses : seule la série 3 est saisie**, à 200 kg × 7, sous la
  fourchette de 8-12. Les deux premières manquent.

---

## LES TEMPS DE REPOS (23/09)

Sa demande : *« ça serait bien à rajouter une analyse avec les temps de repos dans
les bilans »*.

🔴🔴 **SA CORRECTION, ET ELLE EST MEILLEURE QUE MA PREMIÈRE VERSION.** J'avais fait
enregistrer le chronomètre de l'appli. Ses mots : *« on s'en fiche du chronomètre,
parce qu'en fait tu sais quel temps de repos on a pris entre chaque série puisque tu
sais quand est-ce qu'on note les séries »*.
🔑 **Le repos ne se mesure pas, il se déduit de l'écart entre deux séries saisies.**
Aucun bouton à toucher, aucune donnée nouvelle à capturer, et **ça marche
rétroactivement sur tout l'historique**. Vérifié sur ses propres séances : **222
écarts exploitables** sortis de la Sheet sans rien avoir instrumenté.
⚠️ **Avant d'ajouter une capture, chercher si la donnée n'est pas déjà déductible de
ce qu'on enregistre.** Un horodatage vaut souvent un capteur.

**Comment on le calcule, côté Sheet (pour les bilans) :**
- colonne **MAJ**, à la minute près, sur chaque ligne `perf` ;
- on groupe par (jour, séance, exercice), on trie par numéro de série, on prend
  l'écart entre séries **consécutives** ;
- on jette **≤ 20 s** (saisie groupée après coup) et **> 15 min** (téléphone reposé,
  séance finie) ;
- ⚠️ **l'écart contient la série elle-même**, donc le repos réel est plus court de
  30 à 60 s. Ne jamais présenter l'écart brut comme du repos.

**Côté appli**, même logique en local : chaque saisie écrit
`ts-{séance}-e{index}-s{série}-w{semaine}`, et l'onglet **Bilan** affiche le réel
médian face au prescrit, avec un verdict (écourté sous 70 %, trop long au-delà de
150 %). La prescription se lit dans `exo.repos` chez Alexia, `exo.target` chez Jean.
📌 Seule condition : que le client remplisse **au moment de la série**, pas toute la
séance d'un coup à la fin. Les saisies groupées sont filtrées, elles ne faussent rien,
elles disparaissent.

📊 **Repère mesuré sur Alexandre, 222 écarts :** médiane **300 s** entre deux séries,
soit environ 4 min de repos réel.

---

## JOURNAL DES BILANS

### Jean · semaine 1 · bilan rempli le 27/09 à 20 h 16

5 séances sur 5. Sommeil 8 · énergie 7 · fatigue 1 · nutrition tenue 7.
*« Splendide très fort aucun crash »* · *« Fentes bulgares durs »* · aucune modif demandée.

**Poids 74,9 kg, pas 71.** Pris comme référence : c'est sa balance, c'est elle qu'on
suivra chaque semaine. Maintenance recalculée à 74,9 kg (Mifflin 1 728 × 1,48 ≈
2 557) : **+57 kcal, dans le bruit, la cible reste à 2 500.** Il est déjà à 75 sur le
poids, donc l'objectif devient 100 % tour de taille à poids égal. `PLAN.depart`
passé à 74,9 dans l'appli, texte de la cible corrigé.
**Calories déclarées 2 200 au lieu de 2 500** : pas d'ajustement, on lui demande de
manger la diète écrite. Pas de décision calorique avant deux semaines de données.
**Tour de taille non rempli** : réclamé. Mensurations toujours pas faites.

Double progression, au prochain passage :
- ⬆️ **tirage vertical prise large** 90 × 12, 12, 12
- ⬆️ **curl pupitre** 30 × 12, 12
- ⬆️ **relevé de jambes** 15, 15, 15 → haltère entre les pieds (consigne ajoutée
  dans l'appli)
- **écarté machine** : parti à 57,5 × 7 puis redescendu à 50 × 10, 10 → tout à 50
  la semaine 2
- **incliné 60 × 9, 9, 7** et **épaules 70 × 8, 7** : une série sous 8, on garde la
  charge, à surveiller semaine 2
- ⚠️ fautes de frappe à confirmer : leg curl série 2 à « 2 », écarté poulie série 3
  à « 1,5 kg »
- incomplets : presse quad (seule la série 3), tirage vertical neutre en Upper
  (seule la série 1)

Fente bulgare 20 × 11, 11, 10 : dure mais dans la fourchette, on garde. Consigne
ajoutée : se tenir d'une main si l'équilibre lâche avant les jambes.

### Jean · semaine 2 · bilan rempli le 05/10 à 9 h 27

4 séances sur 5 (Push 28/09, Pull 29-30/09, Legs 30/09, Upper 01-02/10), **pas de
Lower**. Sommeil 8 → **6** · énergie 7 · fatigue 1 · nutrition 7. *« Top encore une
fois »*, aucune difficulté, aucune modif, aucune question.
**Poids 74,9 → 74,0 (−0,9).** Calories déclarées **2 600** (semaine 1 : 2 200, ce qui
explique sans doute une partie de la baisse). **Toujours pas de tour de taille, ni
de mensurations.** Décision : calories inchangées à 2 500, nouvelle règle « poids qui
descend » ajoutée (voir plus haut), branche ajoutée dans l'appli.

⚠️ **Il a noté des séries sur la semaine 1 par erreur** (29/09 tirage vertical large,
02/10 tirage vertical neutre) : le 90 × 12-12-12 de la semaine 1 au tirage vertical
large est écrasé dans la Sheet. Lui dire de vérifier la semaine affichée avant de noter.
⚠️ **Charges en forte baisse sans explication le 28 et le 30/09** : développé épaules
70 → 40, écarté machine 50 → 42,5, leg curl 57 → 15, crunch machine 47 → 36,5,
élévations poulie 10 → 7,5, triceps poulie 47 → 40. Hypothèse : autre salle ou autre
machine. **Question posée, réponse à noter ici** avant de lire ces exos comme des
régressions.
⚠️ Les 3 montées de la semaine 1 n'ont pas été faites (tirage vertical large resté à
90, curl à 30, relevé sans lest), et ne sont plus déclenchées en semaine 2.

Montées au prochain passage :
- ⬆️ **tirage vertical prise neutre** (Upper) 75 × 12-13-12
- ⬆️ **extension triceps** (Upper) 47 × 15-15
- ⬆️ **développé épaules** 40 × 15-14, au-dessus de la fourchette 8-12 : charge trop
  légère, remonter franchement
- ⬆️ **écarté machine** 42,5 × 15-14-18 : retour à 50
- presse quad **200 × 12-11-11** (7 reps en semaine 1) : gros progrès, on garde 200
- ⚠️ rowing appui poitrine série 3 à « 2 » : faute de frappe probable

### Alexia · semaine 1

Rien. Deux séances (20 et 21/09), aucune depuis, aucun bilan. Relance à faire.

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

## VEILLE MÉTHODE — À REPORTER DANS LE SKILL

⚠️ Le dossier `methode-alex` vit sur claude.ai, la copie d'ici se remet à zéro. Ce qui
est écrit là doit être **recollé à la main par Alexandre** dans
`references/entrainement.md`.

### Les étirements, vérifié le 24/09/2026

Le dossier du skill date du 15/08. Il tient, sauf **une ligne à corriger**.

🔴 **À retirer : « preuve préliminaire sur les blessures musculo-tendineuses ».**
Une revue de 2025 a screené **plus de 300 000 références**, retenu 19 études pour
**plus de 9 000 participants**, et ne trouve **aucun effet protecteur** :
**OR = 0,945, p = 0,396**. La première moitié de la ligne, elle, se renforce.
⚠️ **La prise du contradicteur : les protocoles type FIFA 11+ réduisent bien les
blessures de 30 à 46 %.** Mais c'est du renforcement et du neuromusculaire, pas de
l'étirement. Le distinguer soi-même.

📐 **Le chiffre qui tue l'argument hypertrophie.** Méta 2024, 42 études, 1 318
participants : effet réel mais petit (**d = 0,20**), obtenu avec **15 minutes par
séance, 3 fois par semaine** sur le même muscle. Presque une heure par semaine et par
muscle. ✅ La formule : *ce n'est pas que ça ne marche pas, c'est le pire rapport
temps/résultat de la salle.*

**En fin de séance**, ajout du 24/09 :
- la perte de force aiguë ne s'applique plus, **c'est donc le bon moment** ;
- ❌ **aucun effet sur la récupération**. Méta 2021 sur les étirements post-séance :
  rien sur la force, rien sur les courbatures à 24, 48 et 72 h. Méta d'octobre 2025,
  15 études et 465 personnes : rien sur les courbatures, la force, la performance ni
  le seuil de douleur. Revue parapluie 2024 : arrêter de le présenter comme un outil
  de récupération ;
- 🔑 **Piège de lecture dans la méta 2025** : elle annonce aussi « aucun effet sur la
  souplesse ». Elle mesure la souplesse **comme marqueur de récupération** dans les
  jours qui suivent, pas les gains d'un programme sur des semaines, qui eux sont
  solides. Ne jamais laisser citer cette phrase hors contexte ;
- ✅ Le seul argument à garder est **l'adhérence** : en fin de séance on est déjà sur
  place, c'est le créneau où une habitude d'amplitude tient sans rien réorganiser.

**Position tenable :** *« si tu t'étires parce que ça te fait du bien, continue. Si tu
t'étires pour grossir ou pour ne pas te blesser, tu t'es trompé de raison. »*
⛔ On ne dit pas « ça sert à rien » : c'est faux sur l'amplitude, et ça ouvre un flanc.

---

## CLIENTS INACTIFS

- **Max** — suivi terminé. Ne plus le traiter. Son appli porte encore un onglet
  Macros avec des chiffres jamais validés par Alexandre : à retirer si son appli
  reste en ligne.
- **Léo** — **classé inactif le 29/09/2026 par Alexandre.** Mois 2 terminé le
  3 septembre, pas de renouvellement. Dernier bilan le 4 août (semaine 4, à moitié
  rempli), dernière séance notée le 18 septembre. Ne plus le traiter, ni dans les
  bilans ni dans la routine du lundi.
- **Julie, Romain, Théo** — voir l'onglet `Formules` de la Sheet, plusieurs dates de
  fin y sont fausses.

---

## L'ONGLET FORMULES EST À CORRIGER

Connu et pas encore fait : Alexia n'y a **aucune ligne**, Jean y figure encore sur
son ancien cycle (23 juin au 3 août), Léo est noté « 1 mois », Max a une fin au
29 juillet, et `alexandre_test` porte une durée parasite.
