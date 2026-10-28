# SUIVI CLIENTS — fiche de pilotage

🔴🔴 **CE DÉPÔT EST PUBLIC** (vérifié le 12/10/2026) : tout ce qui est écrit ici est
lisible par n'importe qui. **Jamais de nom de famille, de téléphone, d'email ni de
pseudo Instagram.** Les données de santé des clients (poids, mensurations, cycle)
n'ont rien à faire ici non plus : voir la section « Confidentialité » plus bas.

**Ce fichier est la mémoire du suivi.** Une conversation qui démarre sans contexte
lit ce fichier et sait quoi faire. Il se met à jour à chaque décision.

Dernière mise à jour : **23/10/2026**
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

## ALEXIA

| | |
|---|---|
| Formule | Suivi 3 mois + nutrition, **300 € payés**, mais **un seul mois réglé** → appli calée sur **4 semaines** |
| Contact | WhatsApp (coordonnées dans le téléphone d'Alexandre, jamais ici) |
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
- perte < 0,3 kg/semaine **deux semaines de suite** → **−150 kcal** en glucides
- perte > 0,8 kg/semaine **deux semaines de suite** → **+150 kcal**
- 🆕 12/10 : **une seule semaine hors fourchette ne déclenche rien**, l'appli affiche
  « on ne touche à rien, si ça se répète on ajuste ». Son poids bouge avec l'eau et le
  cycle, une pesée isolée ne suffit pas.
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

🔒 **Accès à l'appli : verrouillage automatique le mardi 20/10/2026 à 0 h**, le lendemain
de son dernier bilan (mois réglé terminé). Pour rouvrir, repousser `FIN_ACCES` dans
`suivi_alexia.html`. Verrou côté navigateur seulement : pour couper vraiment l'accès,
retirer le fichier du site.
📌 **19/10 au matin : bilan S4 pas encore rempli.** Bilans reçus : S1 (rempli le 05/10)
et S3 (le 12/10), jamais de S2. Elle remplit le lundi vers 11 h, dernière séance notée
le 18/10. **Verrou laissé à ce soir minuit** pour qu'elle puisse envoyer ce dernier
bilan : le couper le matin l'aurait empêchée de le faire. **Rempli à 10 h 03**, voir
le journal des bilans.

🔴 **État au 27/09 : elle s'est arrêtée.** Deux séances seulement, Lower A le 20/09 et
Upper A le 21/09, puis **plus rien pendant six jours**. Aucun bilan rempli. C'est le
point à traiter avant toute question de diète ou de charges.

---

## JEAN

| | |
|---|---|
| Formule | **Un mois réglé** → appli calée sur **4 semaines** |
| Contact | WhatsApp (coordonnées dans le téléphone d'Alexandre, jamais ici) |
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

🔒 **18/10 : mois réglé terminé. Semaine 5 ajoutée mais verrouillée** : floutée, avec un
message « j'attends ton paiement pour la débloquer ». Les semaines 1 à 4 restent
ouvertes. **Après paiement, passer `SEMAINES_PAYEES` au nombre de semaines payées**
dans `suivi_jean.html`. Bilan : S1 et S2 remplis, rien en S3 et S4, dernière séance
notée le 13/10.
🔒 **19/10 : l'appli entière se verrouille d'elle-même le mardi 20/10 à 0 h**, à la fin
des 4 semaines payées, avec le même mécanisme qu'Alexia (`FIN_ACCES`). Toujours rien en
S3 ni en S4 ce matin-là : la journée du 19 lui reste pour envoyer son dernier bilan.
Message affiché : « Mois de suivi terminé · La suite t'attend », semaine 5 prête,
débloquée au paiement. L'ancien texte « Suivi en pause », écrit pour un programme
jamais réglé, ne collait plus : il a payé son premier mois. **Pour rouvrir après
paiement : repousser `FIN_ACCES` et passer `SEMAINES_PAYEES`.** Verrou côté navigateur
seulement : pour couper vraiment l'accès, retirer le fichier du site.
🔓 **28/10 : appli rouverte pour le mois 2, à la demande d'Alexandre.** Semaines 5 à 8,
**du lundi 26/10 au dimanche 22/11** (la semaine du 19/10, verrouillée, ne compte pas).
`NB_SEMAINES` et `SEMAINES_PAYEES` à 8, `FIN_ACCES` au **mardi 24/11 à 0 h** : le lundi 23
lui reste pour son dernier bilan, comme au mois 1. À sa première ouverture, l'appli
l'envoie **une seule fois** sur la semaine 5 (sinon il rouvrait sur la 4 et notait
par-dessus sa séance du 13/10). Les textes du verrou ne citent plus de numéro de
semaine, l'en-tête dit « Mois 2 · semaines 5 à 8 ». **Supposé : un mois payé.** S'il a
payé plus, monter les deux chiffres et repousser la date. Testé hors réseau : ouvert
le 23/11 à 23 h 59, verrouillé le 24/11 à 0 h 01.

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

Rien. Deux séances (20 et 21/09), aucune depuis, aucun bilan. Relance faite le 28/09.

### Alexia · semaine 2 · premier bilan rempli le 05/10 à 11 h 33 (étiqueté S1)

**Repartie après la relance : 4 séances sur 4** (Lower A 28/09, Upper A 30/09,
Lower B 03/10, Lower C 04/10). Sommeil 8 · énergie 8 · fatigue 4 · nutrition 7.
*« J'aime toutes les séances, super programme »*, *« j'y prends du plaisir et c'est
naturel de m'y tenir »*.
**Poids 73,3** (73,7 le 21/09, soit −0,4 en deux semaines). **Calories déclarées
1 800** au lieu de 1 700. Pas de nouveau tour de taille.

**Décision diète : on ne touche pas aux calories**, alors que la règle (< 0,3 kg/sem →
−150) le demanderait. Trois raisons : elle mange 100 kcal au-dessus de la cible, donc
la règle n'est pas testée ; les deux poids sont des pesées isolées et pas des
moyennes ; et la semaine 1 était blanche. On refait le point dans deux semaines sur
des moyennes, en comparant au même moment de son cycle.

Ses trois remarques et ce qui a été fait :
- **RDL : sa prise lâche à la 7e répétition à 30 kg** → sangles, consigne ajoutée.
- **Presse réglage quadriceps : elle sent surtout les fessiers** → consigne ajoutée
  (pieds plus bas, pousser avec tout le pied). Pas un vrai problème, ses fessiers sont
  sa priorité.
- **Sa question : les sorties et le cycle lui font redouter une stagnation** → bloc
  « Les sorties et ton cycle » ajouté dans l'onglet Diète : raisonner à la semaine,
  ne pas compenser le lendemain, comparer le poids au même moment du cycle.

📌 **Elle remplit la colonne RPE à sa façon** : 9-10 la plupart du temps, ce qui veut
dire proche de l'échec. Mais elle met **6 quand elle ne sent pas le bon muscle**
(abducteurs du Lower C). Lui expliquer que la colonne mesure l'effort, et que le
ressenti va dans la note de séance.
📌 **Elle monte la charge avant d'avoir le haut de la fourchette**, et mélange les
charges dans un même exercice (hip thrust 110 → 120 à 8-8-7, kickback 35 → 40 à
10-10, leg curl 35 puis 42,5). À recadrer : même charge sur toutes les séries, on
monte quand toutes touchent le haut.
⬆️ **Seule vraie montée : rowing appui poitrine** 8 kg × 15-15-15 à RPE 4-5, beaucoup
trop léger.

### Alexia · semaine 3 · bilan rempli le 12/10 à 11 h 13 (bien étiqueté S3)

4 séances sur 4, **mais du jeudi au dimanche d'affilée**. Sommeil 7 · énergie 8 ·
**fatigue 7** (4 la semaine d'avant) · **nutrition 9/10** (7 avant) · **1 650 kcal**.
**Poids 71,6** (73,7 le 21/09, 73,3 le 05/10) : −2,1 kg en 3 semaines, soit
**0,7 kg/sem, dans la fourchette**, malgré le −1,7 de la dernière semaine (eau et cycle
probables). **Décision : on ne touche à rien.** Règle de l'appli passée à « deux
semaines de suite » pour qu'elle n'affiche pas +150 kcal sur une seule pesée.
**Mensurations semaine 3** : taille **86 → 84**, poitrine 107 → 105, hanches 106 → 105,
cuisses 64/63 → 64/64, mollet 38 = 38. Elle perd du gras sans perdre ses jambes.

Ses notes :
- **RDL** : bas du dos sur la 2e série à 50 kg ; à 40 kg elle ferait 15 reps proprement
  → **45 kg**, et la série s'arrête dès que le dos prend le relais (consigne ajoutée).
- **Presse quadri faite « chez les filles »** (93 × 10-8-8) : autre machine, nouvelle
  référence, pas comparable aux 42,5-50 d'avant.
- **Rowing appui poitrine** : passé des haltères de 8 kg à la machine, **30 au total
  (15 par bras)**, 30 × 10-8-8. Nouvelle référence.
- **Peur de prendre des mollets si elle charge** → réponse : 2 séries par semaine ne
  feront pas de gros mollets ; proposition de retirer l'exercice si elle préfère.
  ✅ **12/10 : elle préfère, mollets retirés du Lower B** (14 séries au lieu de 16, et sa
  fatigue est à 7, donc on n'ajoute rien à la place).

⚠️ **RPE à 10 sur presque toutes les séries** + fatigue en hausse : on lui demande de
garder 1-2 reps en réserve sur hip thrust, presse et RDL (c'est sa prescription), et
d'espacer les séances plutôt que de les enchaîner.
⚠️ Jeudi 08/10, plusieurs charges ont nettement baissé (hip thrust 120 → 100,
kickback 40 → 20, curl poulie 30 → 16,5) : autre salle ou fatigue, à confirmer.
⬆️ **Abducteurs (Lower B) 110 × 15-15** : monte. **Tirage horizontal** 35 × 12-12 puis
32 × 12 : tout à 35, monte si 12 partout.

### Alexia · semaine 4 · bilan rempli le 19/10 à 10 h 03 (dernière semaine du mois réglé)

3 séances et demie : Lower A (12-13/10), Upper (16/10), puis le 18/10 le Lower C avec
le leg curl allongé et le RDL du Lower B, qu'elle avait raté (*« je fais les exos qui
ne sont pas doublons »*). Sommeil 9 · énergie 7 · **fatigue 4** (7 la semaine d'avant) :
les séances mieux espacées ont payé. Nutrition 8.
Poids et mensurations : dans la Sheet. Rythme de perte du mois dans la fourchette de la
règle → **diète inchangée**.
Ses mots : *« la fatigue au travail a un peu joué sur ma discipline, je suis un peu
déçue mais je vais rectifier ça »* · *« Merciii pour ton accompagnement ! »*

Si elle continue, au prochain passage :
- ⬆️ **abducteurs (Lower A)** 110 × 15-15-15
- ⬆️ **leg curl allongé** 35 × 15-15-15
- ⬇️ **rowing appui poitrine** 30 × 8-8-8, sous la fourchette 10-15 → **25**
- leg curl assis à 42,5 puis 35 sur une nouvelle machine : encore deux charges sur un
  même exercice, à recadrer
- ⚠️ presse fessiers, série 1 notée « 8 » : sans doute 85
- RDL refait à 50 au lieu des 45 conseillés, sans plainte de dos cette fois

🔒 L'appli se ferme ce soir à minuit. **Si elle renouvelle** : repousser `FIN_ACCES`,
passer `NB_SEMAINES` à 8 et appliquer la liste ci-dessus.

### Les deux applis rouvrent sur la dernière semaine consultée (05/10)

Elles repartaient toujours en semaine 1 : c'est ce qui a fait noter Jean et Alexia
dans la mauvaise semaine. Corrigé dans `suivi_jean.html` et `suivi_alexia.html`.


---

## FRANZ — appli en route depuis le 18/10/2026 (`suivi_franz.html`)

⚠️ **Dépôt public** : ses mensurations, son poids et ses photos ne vont **pas** ici tant
que le dépôt n'est pas privé. Ils iront dans la Sheet et dans son appli.

| | |
|---|---|
| Niveau | **Très bon niveau en musculation.** A ralenti récemment : a perdu un peu de masse et de sèche. S'il reprend sérieusement, la mémoire musculaire fera revenir vite |
| Objectif | **Compétition naturelle en amateur, NPC ou WNBF, courant 2027** (dates pas encore annoncées). « MPC » du 18/10 = NPC. En NPC, viser un show **« Natural »** (testé). **Catégorie : Classic ou Bodybuilding**, choix d'Alexandre : il n'a jamais travaillé ses jambes, elles se rattraperont vite. Alexandre le voit podium |
| Priorités | **Fessiers, ischios, épaules (surtout arrière d'épaule), haut du dos, bas du dos** (ajouté le 18/10). Plus les quadris (tout le bas est en retard) et, pour la scène, **mollets et abdos** |
| Fréquence | **5 séances par semaine** |
| Durée | Intense. **Le 1 h 30 n'est pas une limite** (précisé le 18/10) : il a le temps |
| Récupération | Encaisse beaucoup de volume, et sa vie est axée sur le repos en ce moment : **on peut monter le volume** |
| Méthode | La méthode d'Alexandre, **double progression stricte** |
| Photos (18/10) | Reçues, **gardées hors du dépôt**. Chez lui, mur violet, en pied, relâché : **c'est la base de comparaison**. Lecture : le haut est en avance, **le bas du corps entier est la priorité, quadris compris**. Encore sec. Prochaines photos : même heure, même lumière, regard droit |
| Photos (26/10) | Matin, relâché, même mur que le 18/10, **gardées hors du dépôt**. **Comparées au 18/10, alignées épaules-ceinture : ventre et taille identiques** (abdos du haut visibles relâché, bas du ventre plat, pas de poignées d'amour de dos). Rien qui ressemble à du gras après la S1 : la balance de la S1, c'est de l'eau et du glycogène. Le 26/10 paraît plus gros (épaules, dos, bras), mais le téléphone était bien plus près, ce qui grossit le buste : **pas de conclusion sur le volume**. Coupé à mi-cuisse : jambes non comparées. Prochaines : **téléphone posé au même endroit et à la même hauteur que le 18/10, retardateur, en pied**, même heure, même lumière, regard droit, une pose contractée par angle |
| Dossier photos | 🆕 **Page privée claude.ai « Photos de Franz »** (créée le 26/10, à sa demande) : séries par date, comparatif aligné épaules-ceinture, son ancien pic en référence. **Jamais dans le dépôt, jamais son lien ici** (dépôt public : si la page est un jour partagée, le lien suffirait). Mes fichiers peuvent disparaître d'un jour à l'autre, donc **chaque série reçue va d'abord dans la page** : la retrouver dans la liste des artefacts, la lire, ajouter la série dans `SERIES` avec ses repères (épaules, ceinture, centre, en % de la photo), publier les photos sous `photos/AAAA-MM-JJ/angle.jpg` avec la vignette `-min` |
| Format | **Validé le 18/10** : Upper A (lun) · Lower A (mar) · Upper B (mer) · Lower B (jeu) · off · **Postérieur** (sam) · off. Priorités à **3 passages**, 6 max par muscle et par séance ; en PPLUL elles plafonneraient à 12. Un seul gros hinge (RDL). Latérales 4 fois, dont une à 24 h (assumé) |
| Appli | **`suivi_franz.html`**, 10 semaines, sans verrou de paiement. Onglets : **Consignes** (ouvert par défaut), 5 séances, Diète, **Pesées** (Jour 1 à 7 dans chaque semaine ; la moyenne part toute seule dans le bilan sauf s'il tape son poids à la main, et pilote la diète dès 3 pesées), Bilan, Corps (mensurations seules). Repos : 4 à 5 min sur les gros, 3 à 4 min rowings et fente, 2 à 3 min isolation jambes et lombaires, 2 min le reste. Clés du stockage préfixées `franz-`. Colonne RIR (plus « RPE ») |
| Volume semaine | 103 séries. Fessiers 18 · ischios 13,5 · quadris 13,5 · arrière d'épaule 12 · latérales 12 · mollets 9 · biceps 9 · pecs 8 · dorsaux 8 · haut du dos 7,5 · abdos 6 · lombaires 6 · triceps 5 · adducteurs 3 en direct, plus la presse pieds écartés (indirect compté 0,5). Lower A à 8 exercices : abduction et adduction s'enchaînent sur la même machine. Corrections d'Alexandre du 18/10 : **pec fly** au lieu de l'écarté poulie (Upper B), **presse pieds hauts et écartés** au lieu du step-up (Postérieur, « je le vois mal faire du step-up »), **adducteurs** ajoutés. S1 = calibrage à RIR 2, RDL et lombaires légers |
| Changements | **19/10 : tractions à la place du tirage vertical prise large (Upper A)**, à la demande d'Alexandre, **à partir de la semaine 2**. La semaine 1 garde le tirage : il a fait son premier Upper A le 19/10 et y a noté ses 3 séries. Même fourchette 3 × 8-12, lest à la ceinture au-dessus de 12, noté dans la case kg (0 = poids du corps). L'Upper B garde le tirage vertical prise neutre. Volume inchangé |
| Prépa (19/10) | **Onglet « Prépa » dans l'appli.** Show visé : **WNBF France, Heroes Cup** (Pro Qualifier, Montargis ; le 26/09 en 2026). Date 2027 pas encore sortie : **base samedi 25/09/2027**, une seule ligne à changer (`PREPA.scene`) et toutes les dates suivent. **Catégorie : Classic Physique** (choix d'Alexandre). En WNBF, pas de grille poids-taille : la Classic se coupe par taille ou par poids selon le pays. Roadmap : mesure (19/10 → 01/11) · maintenance (→ 03/01/2027) · **prise +150 à +250 kcal, +0,4 à +0,7 kg par mois** (→ 11/04) · **sèche de 22 semaines, pauses comprises** (12/04 → 11/09, 0,5 à 1 %/sem, prêt à J-14) · **répétition de la peak week à J-5 semaines** (15 → 21/08) · marge · peak week (charge en glucides vers 8 g/kg à J-3 et J-2, eau et sel stables, pas de diurétiques) · après la scène. **`PREPA.maintenance` à remplir après la S2.** Sources : voir la veille du 19/10 |
| Calories (21/10) | **Onglet Pesées : une colonne Kcal à côté du poids**, à remplir chaque soir (journée type suivie = il tape sa cible du jour). Les jours vides ne comptent pas ; la moyenne de la semaine part toute seule dans le bilan, champ **« Calories moyennes »** (`calories`, comme le poids : il peut la forcer à la main). Les calories jour par jour restent dans l'appli, seule la moyenne arrive dans la Sheet, comme pour les pesées. **Onglet Diète : la cible du jour est dynamique** (kcal, P, G, L de la semaine, 3 990 dès la S3) avec le mode d'emploi pour manger autrement. Valeurs aliment par aliment ajoutées le 25/10 (étiquettes et valeurs courantes, voir la ligne Diète du 25/10) |
| Poids de scène | 🆕 **19/10 : photos de son poids max reçues** (lumière du dessus et pump, donc +1 à 2 points de gras par rapport à ce qu'elles montrent ; gardées hors du dépôt, chiffres dans la conversation). Lecture : haut du corps très avancé, taille fine, profil Classic ; jambes non visibles. **Estimation : s'il revient à ce niveau, il monte sur scène à peu près à son poids actuel ; plus haut seulement avec du muscle neuf, 1 à 2 kg réalistes en 5 mois.** Le poids habituel qu'Alexandre appelle « PDC » n'est pas tenable très sec en 2027 : il faudrait 3 à 5 kg de muscle de plus qu'à son meilleur. **Si fin mars il est revenu à ce niveau, la sèche peut partir 3 à 4 semaines plus tard que le 12/04** (16 à 18 semaines suffisent, 22 prévues) : décision fin mars sur photos et pesées |
| À venir | Ses mensurations (plus tard), dans l'onglet Corps. **Après la S2** : remplacer `PLAN.depart` par la moyenne de la S2, et choisir la suite selon la catégorie et la date |
| Activité | ~8 000 pas par jour (moyenne du mois). **À garder fixe** pendant la mesure de la maintenance |
| Diète (18/10) | Journée type calculée avec CIQUAL : **≈ 3 550 kcal** (3 150 à 3 800 selon l'huile et le haché), P 175 · G 410 · L 128. Matin : 2 tartines + pâte à tartiner, whey 39 g. Midi : riz 220 g cru, poulet 200 g cru, crème légère 18 % 20 cl, oignon, huile. Soir : pâtes 200-220 g crues, haché 200 g cru, coulis, huile |
| Diète (25/10) | **Refaite sur sa liste de courses du 25/10, 7 journées dans l'onglet Diète**, chacune avec son total et les macros de chaque repas (il peut tracker seul). **S2 calée sur sa moyenne réelle de la S1 : 3 440 kcal** (P 190 · G 438 · L 98, `PLAN` mis à jour), pour que les deux semaines de mesure se comparent ; S3 = +300 (riz +85 g). Pas de jours on/off pendant la mesure. Ses plats : riz + poulet au curry et crème légère, pâtes + bœuf (haché 15 %, rumsteck, bavette, steak) sauce tomate ou crème, petit-déj tartines Nocciolata + whey ou bol avoine + fromage blanc 7,6 % + whey, collation fromage blanc + kiwi jaune. Équivalences et Red Bull dans l'onglet. ⚠️ **Valeurs : étiquettes trouvées en ligne et valeurs courantes, pas CIQUAL** (fichier absent) : whey et fromage blanc à vérifier sur ses pots. Sources dans la conversation du 25/10 |
| Plan diète | 1) **2 semaines à l'identique mais pesé**, programme démarré, pesée chaque matin à jeun → moyenne = maintenance. 2) ~8 semaines à maintenance (mémoire musculaire). 3) Léger surplus jusqu'à la prépa, ~+200 g/semaine. 🔁 **19/10 : ramené à +0,4 à +0,7 kg par mois** (veille du 18/10 : la vitesse se règle sur le niveau ; +200 g/semaine, c'est un rythme de débutant ou d'intermédiaire). ⚠️ 20/10 : cette justification venait d'une confusion entre vitesse de poids et gain de muscle (corrigée dans la veille du 18/10). 🔁 **19/10 au soir, avec Alexandre : plus de maintien jusqu'en janvier. Prise dès la S3 (02/11) à maintenance + 300 kcal** (en glucides), visée +0,5 à 1 kg par mois ; +150 si pas de prise deux semaines de suite, −150 si prise > 0,3 kg/sem deux semaines de suite avec tour de taille +0,5 cm. Pourquoi : il est sous son poids max, ce qu'il reprend d'abord est surtout du muscle qu'il avait déjà, et commencer tôt donne plus de semaines de données avant la sèche. Ce qui reste prudent : pas de « très grosse prise », au-delà de la reprise un surplus plus gros ajoute surtout du gras (Helms 2023, Garthe 2013). Logique dans `majCible` (`PLAN.surplus`, `gainMin`, `gainMax`). 4) Prépa 16 à 20 semaines à ~0,7 %/semaine. Durées à caler sur la date. **Dans l'appli** : sa journée pesée + 1 fruit + 200 g de légumes = **3 690 kcal, P178 · G436 · L129**. Huile 20 g par repas, haché 15 %, whey dans l'eau. Ajustement auto à partir de S3 : ±150 kcal en glucides si la tendance se répète 2 semaines (baisse → +150 ; hausse avec tour de taille → −150). `PLAN.depart` = 73,3 non à jeun, à remplacer par la moyenne S2 |
| À lui demander | **La date** dès qu'elle sort. L'huile (2 c. à soupe par repas ou par jour ?), le % du haché, whey dans l'eau ou le lait, ce qui sort de la journée type (week-end, extras). Sa salle (Smith, leg curl assis, rear delt machine, hip thrust, extension lombaire ?), les exos qu'il déteste. Ses douleurs éventuelles : **hors du dépôt** |

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

### Prise de masse : la vitesse se règle sur le niveau, vérifié le 18/10/2026

🔴🔴 **20/10 : LA LIGNE DE REMPLACEMENT CI-DESSOUS EST ANNULÉE.** Le skill a été mis à
jour le 20/10 dans une autre conversation (mot-témoin `profil-20`, « LES VITESSES EN %
DU POIDS » en fin de `nutrition.md`), et **c'est lui qui a raison** : ma ligne prenait
le tableau d'Aragon (le **muscle** gagné par mois) pour une vitesse de **poids** de
corps. Les deux ne se confondent pas. Ce qui reste valable plus bas (Helms 2023, le
P-ratio reformulé) est intégré dans le zip `prepa-20` du 20/10.

À recoller dans **`references/nutrition.md`** (pas `entrainement.md`).

🔴 **Contradiction interne à corriger.** Section « Vitesses » : « Prise de masse :
surplus léger, **200-300 g/semaine** ». Or la table d'Aragon du même fichier donne,
pour un avancé, **0,25 à 0,5 % du poids par mois**, soit **200 à 400 g par mois** à
80 kg. 200-300 g par semaine, c'est 1 à 1,5 % par mois : le rythme d'un débutant.

✅ **Ligne de remplacement :** « Prise de masse : surplus léger, et la vitesse dépend
du niveau. Débutant 1 à 1,5 % du poids par mois (≈ 200-300 g/semaine à 80 kg),
intermédiaire 0,5 à 1 % (≈ 100-200 g/semaine), avancé 0,25 à 0,5 % (≈ 50-100
g/semaine). Au-delà, le surplus part surtout en gras. Prise rapide = sèche plus longue
derrière = temps perdu. »

📐 **Ce qui l'appuie.** Garthe 2013 (déjà dans le fichier) et **Helms et coll. 2023**
(*Sports Medicine – Open*) : pratiquants entraînés, 8 semaines, maintenance contre +5 %
contre +15 % de surplus. **Pas de différence sur l'épaisseur musculaire ni sur le
squat** ; le +15 % prend **plus de gras** (plis cutanés) et un peu plus au développé
couché. ⚠️ 17 sujets au bout, statistiques bayésiennes : cohérent avec Garthe, pas une
preuve à lui seul.

🔴 **Le plafond de gras en prise de masse : ne plus dire « au-delà de 15 % tu
construis moins bien ».** L'idée (le « P-ratio ») vient surtout de données sur des
**sédentaires** (Forbes 2000, reprise par Hall 2007). **Aucun essai contrôlé** ne
compare des pratiquants entraînés à des taux de gras différents, et le débat reste
ouvert (Henselmans pour, Trexler et Nuckols contre). ✅ La formule qui tient : « on
plafonne vers 15-16 % pour garder la sèche suivante courte ». La roadmap d'Alexandre du
04/08 l'écrivait sous l'autre forme : corrigée le 18/10.

### Les étirements, vérifié le 24/09/2026

✅ **Intégré dans le zip `prepa-20` du 20/10** (`entrainement.md`), à téléverser.

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


### Nutrition sans diplôme : ce que dit vraiment la loi, vérifié le 12/10/2026

✅ **Intégré dans le zip `prepa-20` du 20/10** (`legal.md`), à téléverser.

🔴 **`legal.md` du skill est incomplet.** Il dit : « le seul titre protégé de ce côté
est diététicien ». C'est vrai pour le **titre**, mais la loi protège aussi l'**activité** :
- **L4371-1 CSP** définit le diététicien comme toute personne qui « habituellement,
  dispense des conseils nutritionnels et, sur prescription médicale, participe à
  l'éducation et à la rééducation nutritionnelle des patients atteints de troubles du
  métabolisme ou de l'alimentation, par l'établissement d'un bilan diététique
  personnalisé et une éducation diététique adaptée ».
- **L4372-1** punit l'**exercice illégal** de la profession : 1 an et 15 000 €.
  **L4372-2** punit l'usage du **titre** sans diplôme (usurpation, art. 433-17 C. pénal).
- ⚠️ **Zone grise, non tranchée** : les diététiciens lisent « conseils nutritionnels »
  seul comme réservé ; les coachs lisent le « et, sur prescription médicale … patients »
  comme ce qui est réservé. **Aucune condamnation de coach nutrition trouvée**, contrôles
  très rares, et une question écrite (AN n° 9716, 2023) plus une pétition demandent
  justement d'encadrer les coachs, ce qui suggère qu'ils ne le sont pas clairement
  aujourd'hui. **Réponse ministérielle non lue** (site inaccessible depuis ici).
- « Nutritionniste » seul : **pas un titre protégé** d'après la plupart des sources ;
  « médecin nutritionniste » l'est. « Diététicien(ne) », « diététicien-nutritionniste »,
  « bilan diététique », « rééducation nutritionnelle », « patient » : **jamais**.
- **Exercice illégal de la médecine (L4161-1)** : aucune pathologie prise en charge
  (diabète, TCA, SOPK, thyroïde, grossesse, troubles digestifs, traitement en cours) →
  renvoi au médecin ou à un diététicien.

**Ce qui protège le plus** : public sain, objectif sportif ou de composition corporelle,
aucun diagnostic, aucun régime thérapeutique, filtre santé à l'inscription, mention
« ne remplace pas un avis médical ou diététique ». Pour une certitude : un avocat, ou un
diététicien diplômé en partenaire pour signer les plans.


### Peak week et prépa de compétition naturelle, vérifié le 19/10/2026

✅ **Intégré dans le zip `prepa-20` du 20/10** (`prepa-competition.md`), à téléverser.

**À reporter dans `references/nutrition.md`.** C'est la base de l'onglet Prépa de Franz.

| | Ce qui tient | Source |
|---|---|---|
| Vitesse de sèche | 0,5 à 1 % du poids par semaine. Les préps de pros naturels suivis durent environ 6 mois | Helms, Aragon & Fitschen 2014 (JISSN) ; cas Rossow 2013, Kistler 2014 |
| Macros en sèche | protéines 2,3 à 3,1 g/kg de masse maigre, lipides 15 à 30 % des kcal, glucides le reste | Helms 2014 |
| Pauses à maintenance | 1 semaine toutes les 3 : même perte de gras, même masse maigre, moins de faim et plus de satisfaction | Peos 2021, essai ICECAP (MSSE) |
| Prise hors saison | surplus de 10 à 20 % et +0,25 à 0,5 %/semaine pour débutant et intermédiaire, plus prudent pour l'avancé | Iraki 2019 (Sports) |
| Charge en glucides | seule technique de peak week avec un début de preuve : épaisseur musculaire et note photo en hausse chez 15 bodybuilders qui chargeaient, pas chez les 9 qui ne chargeaient pas ; +2,9 % d'épaisseur contre placebo à 9 g/kg | de Moraes 2019 (JSSM) ; essai contrôlé AUT/Abertay |
| Eau et sodium | les charger puis les couper : mécanismes supposés, aucun résultat mesuré, risques réels (hyponatrémie, intoxication à l'eau, rhabdomyolyse). Le sodium sert à absorber les glucides : le couper pendant la charge la freine | Escalante 2021 (BMC SSMR) ; Homer, Cross & Helms 2024 (Sports Med Open) |
| Tester avant | toute manipulation se répète avant la vraie compét ; sinon, on garde tout stable | Helms 2014 ; Escalante 2021 |
| Ce que font les athlètes | 93,8 % de 81 naturels britanniques manipulent glucides, eau ou sel la dernière semaine ; 6,2 % gardent leur diète | Chappell & Simper 2018 (Sports) |

⚠️ **Les chiffres de charge (8 à 12 g/kg) viennent de résumés** : les articles complets
n'ont pas pu être ouverts d'ici (sites bloqués par le réseau). À relire en entier avant
d'en faire une vidéo.
⛔ **Diurétiques** : liste de l'AMA, donc interdits en WNBF, dont le contrôle urinaire
suit le code AMA. Éligibilité WNBF : 10 ans sans stéroïdes, peptides ni GH, 2 ans sans
prohormones ni produit interdit en vente libre, polygraphe à l'inscription.

### Prépa de compétition : le fichier complet, 20/10/2026

**Fichier prêt à coller : `methode/prepa-competition.md`** (dans ce dépôt, envoyé à
Alexandre le 20/10). Il reprend le bloc peak week du 19/10 et ajoute ce qui a été décidé
depuis pour Franz, écrit sans aucune donnée de client :
- ✅ **Retour après une baisse : on prend tout de suite** (correction d'Alexandre du 19/10,
  contre mon plan de 9 semaines à maintenance) : surplus dès la fin de la mesure.
- ✅ **Le poids de scène se calcule** : masse maigre ÷ (1 − % de gras sur scène), avec 1 à
  2 points de gras en plus sur des photos flatteuses.
- ✅ **La durée de sèche se calcule depuis le gras à perdre** ; prêt à J-14 ; répétition de
  la peak week à J-5 semaines.
- Le cadre WNBF, les poses Classic, le posing, le protocole de peak week jour par jour, le
  rétro-planning.

✅ **20/10 : tout est intégré dans un skill complet prêt à téléverser, `methode-alex.zip`,
mot-témoin `prepa-20`**, construit sur la version `profil-20` du jour (envoyé à Alexandre,
gardé hors du dépôt public parce qu'il contient toute la méthode). Il suffit de supprimer
l'ancien skill sur claude.ai (Personnaliser → Skills) et de téléverser ce zip. Les étapes
manuelles ci-dessous ne servent que si le zip n'est pas utilisé.

**Pour l'intégrer à la main** (c'est Alexandre qui le fait, sur claude.ai) :
1. créer `references/prepa-competition.md` avec ce fichier ;
2. ajouter dans la liste des fichiers de `SKILL.md` : « **references/prepa-competition.md**
   — la prépa de compétition naturelle (WNBF, NPC Natural, Classic Physique) : poids de
   scène, hors-saison, sèche, peak week, posing, rétro-planning » ;
3. ~~appliquer la ligne de remplacement du 18/10~~ : annulée le 20/10, voir plus haut ;
4. changer le mot-témoin : proposition `prepa-20`, version du 20 octobre 2026.

### Collagène, articulations et tendons, vérifié le 22/10/2026

À reporter dans `complements.md` (proposition : **tier B, situationnel**, c'est à
Alexandre de trancher) et la glucosamine dans `mythes.md`. Rien n'existait dans le skill
sur ces sujets.

| Pour quoi | Ce que disent les études | Niveau |
|---|---|---|
| Douleur d'arthrose (genou) | méta 2024, 11 essais, 870 patients : moins de douleur et de raideur, la fonction bouge moins nettement. Essais hétérogènes, souvent sur des produits de marque, pas de preuve qu'il reconstruise le cartilage | 🟡 effet modeste |
| Douleur articulaire à l'effort | Clark 2008 (10 g/j, 24 semaines, 97 sportifs analysés) et Zdzieblik 2017 (5 g/j, 12 semaines, 139 sportifs) : moins de douleur | 🟡 deux essais, anciens |
| Tendon | Jerger 2022 (Achille) et 2023 (rotulien), 5 g/j + muscu 14 semaines : le tendon grossit plus (+11 % contre +4,7 % sur l'Achille). Balshaw 2023 (15 g/j, 15 semaines) : rien de plus que le placebo. Revue 2026 (8 essais, 257 personnes) : section plus grande dans 3 études sur 4, rigidité améliorée seulement à 15-30 g/j, aucun effet ajouté sur la force | 🟡 prometteur, contradictoire |
| Synthèse de collagène | Shaw 2017 : 15 g de gélatine + vitamine C, 1 h avant 6 min de corde à sauter, doublent un marqueur sanguin (PINP). 8 hommes | 🧪 un marqueur, pas un résultat |
| Muscle et force | protéine incomplète (pas de tryptophane, peu de leucine) : moins de synthèse musculaire que la whey (Oikawa 2020). Méta 2024 : pas d'effet utile sur la force. La méta en réseau de 2025 qui le classe premier est contestée (Phillips 2026 : un classement n'est pas une supériorité, et à leucine égale la whey fait plus de muscle) | ✅ pas un complément pour le muscle |
| Glucosamine (± chondroïtine) | ajoutée à l'exercice : aucun effet sur la douleur du genou (6 essais, 297 personnes, 2023). Chondroïtine seule : résultats partagés, les plus gros essais ne battent pas le placebo | 🔴 rien de solide |

🔑 **Ce qui adapte le tendon, c'est la charge** : la méthode le dit déjà (décalage
muscle/tendon, double progression). Le lien « tendon plus gros = moins de blessures »
n'est pas mesuré, comme pour la rotation d'exercices.
⚠️ Lu par résumés seulement (articles bloqués par le réseau) : à relire en entier
avant d'en faire une vidéo (règle du 29/08).

### « Déchirer les fibres » pour grossir, vérifié le 23/10/2026

À reporter dans `mythes.md`, en renfort de la ligne « Les courbatures mesurent le
travail », qui cite déjà Damas 2016.
- ✅ **Flann 2011** (*J Exp Biol*), le test direct : un groupe préparé pour ne pas avoir
  de dégâts, un autre qui en a (CK multipliée par plus de 5, courbatures), même travail
  pendant 8 semaines. **Même hypertrophie, même force (+25 % contre +26 %).** Les auteurs :
  la croissance peut démarrer sans aucun dégât détectable.
- ✅ **Damas 2016** (*J Physiol*, 10 hommes, 10 semaines) : les dégâts et la synthèse
  protéique sont au maximum la 1re semaine, et **ni l'un ni l'autre ne prédit la
  croissance**. La synthèse ne colle à l'hypertrophie qu'à partir de la 3e semaine, quand
  les dégâts ont baissé : au début, elle sert surtout à réparer.
- 🟡 Le débat n'est pas clos à 100 % (Schoenfeld 2012 : les dégâts pourraient aider, sans
  être nécessaires ; échange de lettres en 2018). ✅ Ce qui tient : **la tension mécanique
  est le moteur, les dégâts ne sont pas nécessaires, et trop de dégâts retardent.**
- 📌 « Déchirer » est une image : ce qu'on voit au microscope, c'est la structure des
  sarcomères désorganisée (lignes Z), pas des fibres coupées.

### Le nombre de séances se lit dans le carnet, 23/10/2026

À reporter dans `adherence.md`. **Observé sur un carnet de 10 semaines (le sien), pas
une étude** : à dire comme un constat de coach, jamais comme un résultat.
- 📌 **On construit le programme sur le nombre de séances faites, pas prévues.** À 5
  séances prévues, il en a fait 4, 4 puis 3, et c'est chaque fois la séance de jambes
  qui a sauté. Sur 4 prévues (depuis la semaine 4), il en fait 4.
- 📌 **Ce qui est en fin de séance saute en premier.** Jambes placées après le haut du
  corps : environ une série sur trois notée en 6 semaines, et jamais au deuxième Push.
  Le leg curl placé en milieu de Pull, lui, était fait.
- ✅ **La réponse : le muscle qu'on remonte va dans les séances réellement faites, en
  séance 1 de la rotation ou en milieu de séance, pas en dernier.** Appliqué à son
  bloc 11, après sa correction du 23/10 (**1 leg day, pas 2**) : Pull, Push, Legs,
  Upper, avec une leg extension et un leg curl en milieu de Pull.
- 🔁 **Récup, son idée du 23/10 : le leg day sépare les séances du haut.** Sur 4
  séances dont 3 du haut, deux séances du haut se touchent forcément quelque part du
  cycle : on choisit lesquelles. Chez lui, le Pull passe en tête pour que le Push et
  l'Upper (épaule et pec blessés) ne se suivent pas ; le seul enchaînement direct est
  Upper puis Pull, avec le jour off entre les deux. Les jambes réparties vont dans la
  séance la plus loin du leg day (le Pull), en 2e passage à 2 séries.
- ⚖️ **Même volume à chaque séance (14 séries), sa demande du 23/10** : la récup ne
  dépend plus du jour. Pour équilibrer, on déplace des exos peu coûteux (mollets du
  leg day vers le Push) plutôt que d'en ajouter.
- 📸 **Le volume suit la photo.** Un muscle point fort passe à 2 séries par passage et
  les séries libérées vont au point faible. Chez lui (photos du 23/10) : épaules en
  point fort, latérales de 3 à 2 séries, militaire au Push seulement (l'avant
  d'épaule travaille déjà dans tous les développés, déjà écrit dans
  `entrainement.md`).
- 🔴 **Ma lecture « jambes nettement en retard » était fausse (23/10 au soir).** Elle
  venait de photos relâchées, en lumière douce, cuisses coupées à mi-hauteur. Sa
  vidéo contractée du 18/10 montre des quadriceps développés et séparés. **Règle :
  on ne juge un muscle que vu en entier, contracté et relâché, et on compare dans la
  même image et la même lumière.** Ischios, fessiers et mollets : toujours pas vus
  correctement, le « point faible ischios » d'août n'est pas vérifié en photo.
  **Complément du 26/10 (Franz) : et à la même distance.** Un téléphone plus près
  grossit le buste : ses photos du 26/10, prises bien plus près que celles du 18/10,
  le faisaient paraître plus gros alors que le ventre et la taille n'avaient pas bougé.
  Les fichiers des photos peuvent disparaître de mon environnement : la série de
  référence se garde dans la page privée du client (voir sa fiche).
- 🔎 **Tirage vertical, omoplates qui montent en haut : vérifié le 24/10.** Aucune étude
  ne compare « omoplates libres en haut » et « épaules basses » sur la croissance du
  grand dorsal (seulement de l'EMG, et un essai enregistré sans résultat). Ce qu'on
  garde, comme **raisonnement** : en haut, le grand dorsal est à sa longueur maximale,
  et travailler long fait mieux que court (déjà dans `entrainement.md`). Laisser
  monter en contrôlant, sans rebond ; stop juste avant si l'épaule pince. ⛔ Jamais
  « c'est prouvé ».
- 🔁 **Rowing qui plafonne (24/10).** Poulie sans appui : le bas du dos lâche avant le
  dos. Hammer et haltères : trop légers pour lui. Réponse : **rowing à disques un
  bras (Meadows row, rang S dans `entrainement.md`)**, ou une machine à bras
  indépendants faite un bras à la fois. Sa proposition retenue au Pull : **pullover à
  la machine** (rang A), avant le vertical, isolation avant le poly comme aux pecs.
  Le Meadows row reste à l'Upper : sans aucun tirage horizontal, le milieu du dos ne
  garderait que le rear delt fly.
- 📌 **Chez lui, « l'épaule » d'une séance du haut, ce sont les latérales.** Une séance
  Upper avec le militaire mais sans latérales, pour lui, c'est « pas d'épaule ».
- 🔁 **Isolation avant le polyarticulaire aux jambes** (leg curl assis puis roumain, leg
  extension puis pendulum), à sa demande : même croissance (l'ordre ne
  change pas l'hypertrophie, déjà dans `entrainement.md`), charge plus basse sur le
  poly donc moins de stress genou et dos. Le prix : le poly progresse moins vite en
  charge. Même ordre chaque semaine.
- 🔑 **Sa consigne du 23/10 : la liste d'interdits n'est pas une règle de conception.**
  On choisit ce qui sert le mieux et il corrige. Le roumain revient, pré-fatigué ;
  squat barre libre, soulevé de terre et good morning restent dehors par choix (même
  travail avec moins de fatigue), le haut garde ses adaptations liées aux blessures.

---

## CONFIDENTIALITÉ — À RÉGLER (12/10/2026)

Le dépôt `alexkjoly-cloud/coaching` est **public**, et GitHub Pages publie aussi ses
fichiers. Ce fichier contenait jusqu'au 12/10 les noms de famille, un téléphone, des
emails et un pseudo Instagram : **retirés de la version actuelle, mais toujours
lisibles dans l'historique Git.** Il contient encore les poids, mensurations et notes
de santé des clients, qui sont des données de santé au sens du RGPD.

Ce qu'il faut faire, avec l'accord d'Alexandre :
1. **Sortir ce fichier dans un dépôt privé** (les applis, elles, restent publiques pour
   que GitHub Pages continue de les servir).
2. **Purger l'historique du dépôt public** (réécriture + push forcé), sinon les
   anciennes versions restent consultables.
3. Les applis clientes publiques ne doivent contenir ni nom de famille ni chiffre de
   santé dans leur texte (Jean : « ta balance dit 74,9 kg » est à reformuler).

---

## CLIENTS INACTIFS

- **Max** — suivi terminé. Ne plus le traiter. Son appli porte encore un onglet
  Macros avec des chiffres jamais validés par Alexandre : à retirer si son appli
  reste en ligne.
- **Léo** — **classé inactif le 29/09/2026 par Alexandre.** Mois 2 terminé le
  3 septembre, pas de renouvellement. Dernier bilan le 4 août (semaine 4, à moitié
  rempli), dernière séance notée le 18 septembre. Ne plus le traiter, ni dans les
  bilans ni dans la routine du lundi.
- **Julie** — **la copine d'Alexandre, pas une cliente** (précisé le 12/10/2026). Elle
  s'entraîne avec son appli (`suivi_julie.html`) mais n'est pas suivie comme une
  cliente : pas de bilan à réclamer, pas de relance, pas de place dans la routine du
  lundi. On ne la traite que si Alexandre le demande.
- **Romain, Théo** — voir l'onglet `Formules` de la Sheet, plusieurs dates de fin y
  sont fausses.

---

## L'ONGLET FORMULES EST À CORRIGER

Connu et pas encore fait : Alexia n'y a **aucune ligne**, Jean y figure encore sur
son ancien cycle (23 juin au 3 août), Léo est noté « 1 mois », Max a une fin au
29 juillet, et `alexandre_test` porte une durée parasite.
