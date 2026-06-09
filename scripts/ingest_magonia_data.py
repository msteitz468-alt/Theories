#!/usr/bin/env python3
"""Content payload for the Vallée *Passport to Magonia* ingest."""
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
TODAY = "2026-06-07"
SOURCE = "[[Passport to Magonia: From Folklore to Flying Saucers (Vallée, 1969)]]"

SOURCE_PAGE = f"""---
title: "Passport to Magonia: From Folklore to Flying Saucers (Vallée, 1969)"
type: source
source_type: secondary_scholarly
author_or_origin:
- Jacques Vallée
date_composed:
- "1969"
language_original:
- English
last_updated: {TODAY}
tags: [source, source/vallee-1969, topic/ufo-folklore]
---

## Source Description

*Passport to Magonia: From Folklore to Flying Saucers* is a comparative study by
astronomer and computer scientist Jacques Vallée, first published in 1969 (Henry
Regnery; the ingested copy is the 2014 Daily Grail Publishing reprint). It is one
of the foundational works of UFO literature and the book that shifted serious
ufology away from the simple "nuts and bolts" extraterrestrial hypothesis.

Vallée's thesis is that modern UFO encounters and the worldwide folklore of
fairies, elves, demons, incubi and religious apparitions are manifestations of a
single, enduring phenomenon. He argues the phenomenon's *stable* features
(humanoid occupants, paralysis, abduction, time distortion, sample-taking,
absurd dialogue) recur across cultures and centuries, while its *secondary*
features (the shape of the craft, the occupants' claimed origin) are "chameleon-
like," adapting to the beliefs and technology of each era. He explicitly does
**not** assert the objects are physical, nor that they are extraterrestrial; his
interest is the mechanism by which such beliefs are generated and their effect on
human imagination — what he calls a possible "control system."

The book closes with "A Century of UFO Landings (1868–1968)," a catalogue of
close-encounter/landing cases compiled from international sources, which became a
model for later UFO databases.

## What the Source Contributes

- The Magonia thesis: the identity of the UFO phenomenon with the fairy-faith and
  with religious/demonological apparitions.
- The "control system" / "functioning lie" idea — that engineered apparitions can
  shape collective belief regardless of whether the objects are physical.
- The argument that a superior intelligence would necessarily appear *absurd*, and
  that this absurdity itself keeps science away and lends the myth religious tone.
- Close readings of folklore sources: Agobard of Lyons (Magonia), Facius Cardan's
  seven visitors (1491), Rev. Robert Kirk's *Secret Commonwealth* (1691), and
  Fr. Sinistrari's *De Daemonialitate* (incubi/succubi).
- Parallels drawn to modern cases: Eagle River/Simonton (1961), Valensole/Masse
  (1965), Socorro/Zamora (1964), the Tully "saucer nests" (1966), the
  Kelly–Hopkinsville "goblins" (1955), and the Hill abduction.
- The interpretation of Catholic apparitions (Knock 1879, Fatima, Guadalupe) as
  structurally identical to UFO events.
- "A Century of UFO Landings" catalogue and an explicit methodology for it.

## Key Claims Extracted

- [[Vallée argues the UFO phenomenon and the fairy-faith are the same phenomenon]]
- [[The name Magonia derives from Agobard of Lyons's account of cloud-ships]]
- [[Facius Cardan recorded seven aerial beings who said they were made of air in 1491]]
- [[Vallée proposes a control system that shapes belief through engineered apparitions]]
- [[The phenomenon's secondary features adapt to the witness's culture]]
- [[Vallée summarizes the UFO phenomenon in five facts]]
- [[Vallée concludes a superior intelligence would necessarily appear absurd]]
- [[Joe Simonton was given pancakes by saucer occupants echoing fairy food]]
- [[Vallée links UFO sightings to cattle theft and mutilation across centuries]]
- [[Saucer nests match the fairy rings of folklore]]
- [[UFO occupants gather plant and soil samples and claim to be from Mars]]
- [[Witnesses report paralysis and missing time near landed craft]]
- [[Daemonialitas records sexual and genetic contact between humans and nonhuman beings]]
- [[Sinistrari argued incubi are a separate aerial species not the devil]]
- [[Catholic apparitions such as Knock and Fatima are structurally UFO events]]
- [[Robert Kirk's Secret Commonwealth systematized fairy traits matching ufonauts]]
- [[Vallée argues the extraterrestrial hypothesis is an insufficient explanation]]
- [[The catalogue indexes a century of UFO landings from 1868 to 1968]]
- [[UFO reports keep pace with human technology across eras]]
- [[Religious scripture describes celestial chariots and sky-beings]]
- [[The absurd behavior of UFO entities keeps science away and gives the myth religious overtones]]
- [[Vallée argues fiction anticipated specific UFO report details]]
- [[Vallée recommends small informal investigation groups over large organizations]]

## Internal Tensions

- Vallée repeatedly stresses he is **not** claiming the objects are real physical
  craft, nor that they are extraterrestrial; he warns the reader not to read the
  book "too fast" and mistake his juxtapositions for assertions of fact.
- In "Conjectures" he offers several speculative theories (a dream-implementing
  medium; collectively-perceptible mental entities; a superior intelligence
  projecting art-like objects through time) and then states plainly that "none of
  these attractive theories has a scientific leg to stand upon."
- The catalogue's own warning notes that inclusion of a case implies no claim it
  describes a real physical event and that cases are not all equally reliable.
"""

CHAPTER_NOTES = f"""---
title: "Vallée Passport to Magonia — Chapter Notes"
type: source
source_type: secondary_scholarly
author_or_origin:
- Jacques Vallée
date_composed:
- "1969"
language_original:
- English
last_updated: {TODAY}
tags: [source, chapter-ingest, topic/ufo-folklore]
---

Parent source: {SOURCE}

---

## Chapter 1 — Visions of a Parallel World

Sets up the thesis with ancient and medieval "sky-being" material: the Palenque
sarcophagus and Jomon Dogu figurines (as cited by ancient-astronaut writers);
celestial chariots in the Bible and Ezekiel's cherubim; medieval Japanese and
European prodigies; St. Anthony's satyr; Agobard of Lyons and Magonia; Facius
Cardan's seven visitors (1491); Goethe's luminous creatures; and modern humanoid
landings (Niagara 1958, Socorro 1964, Hopkinsville 1955, Quarouble 1954,
Valensole 1965). Introduces Aimé Michel's idea that a superior race's behavior
would appear random or absurd.

**Concepts:** [[Magonia]], [[The control system (Vallée's functioning lie)]]
**Claims:** [[The name Magonia derives from Agobard of Lyons's account of cloud-ships]], [[Facius Cardan recorded seven aerial beings who said they were made of air in 1491]], [[Religious scripture describes celestial chariots and sky-beings]]

---

## Chapter 2 — The Good People

The fairy-faith parallels. Joe Simonton's Eagle River pancakes (1961) set against
Celtic "food from fairyland" (Evans-Wentz); the "Gentry"/"Good People"
(Sleagh Maith); fairy rings vs. saucer "nests" (Tully 1966, Ohio 1965, Charlton
crater 1963).

**Claims:** [[Joe Simonton was given pancakes by saucer occupants echoing fairy food]], [[Saucer nests match the fairy rings of folklore]]
**Events:** [[Eagle River incident (Simonton, 1961)]], [[Tully saucer nests (1966)]]

---

## Chapter 3 — Angels or Devils?

Sample-taking humanoids (Gary Wilcox, Tioga 1964, "from Mars"); theft of animals
and the cattle-mutilation theme (Hamilton's 1897 Kansas airship-cow affidavit;
Snippy the horse, 1967). "The Secret Commonwealth": Kirk's 1691 treatise and its
16-point description of the elves; aerial races; the argument that the
extraterrestrial hypothesis is insufficient.

**Claims:** [[UFO occupants gather plant and soil samples and claim to be from Mars]], [[Vallée links UFO sightings to cattle theft and mutilation across centuries]], [[Robert Kirk's Secret Commonwealth systematized fairy traits matching ufonauts]], [[Vallée argues the extraterrestrial hypothesis is an insufficient explanation]]
**Concepts:** [[The Secret Commonwealth]]

---

## Chapter (Folklore in the Making)

Changelings, human midwives, abductions and the relativity of time "in Magonia"
(mortals who spend hours with the fairies return to find years have passed).
Reinforces the paralysis/abduction/time-distortion parallels.

**Claims:** [[Witnesses report paralysis and missing time near landed craft]]
**Events:** [[Valensole encounter (Masse, 1965)]]

---

## Chapter — Daemonialitas

The sexual and genetic dimension censored out of modern fairy tales: incubi and
succubi, intermarriage with nonhumans, the Villas-Boas and Hill cases, and
Fr. Sinistrari's *De Daemonialitate* arguing incubi are a distinct aerial species
rather than the devil. "Nurslings of Immortality" and "A Great Sign in Heaven"
treat contactee claims and the Knock apparition (1879) as structurally identical
to UFO events.

**Claims:** [[Daemonialitas records sexual and genetic contact between humans and nonhuman beings]], [[Sinistrari argued incubi are a separate aerial species not the devil]], [[Catholic apparitions such as Knock and Fatima are structurally UFO events]]
**Events:** [[Knock apparition (1879)]]

---

## Chapter — The Functioning Lie (conclusion)

The thesis stated: the mechanisms generating these beliefs are identical across
ages; controlling imagination shapes collective destiny "provided the source of
this control is not identifiable by the public." The "perfect landing" cases
(Tripoli 1954, Abbiate Guazzone 1950) read as staged scenes. Summarized as Five
Facts and Three Propositions. The "Conjectures" speculations are offered and then
disowned as unscientific.

**Concepts:** [[The control system (Vallée's functioning lie)]], [[Vallée's Five Facts of the UFO phenomenon]], [[Vallée's Three Propositions on the UFO phenomenon]], [[Interdimensional hypothesis (UFOs as windows not objects)]]
**Claims:** [[Vallée proposes a control system that shapes belief through engineered apparitions]], [[Vallée summarizes the UFO phenomenon in five facts]], [[Vallée concludes a superior intelligence would necessarily appear absurd]], [[The phenomenon's secondary features adapt to the witness's culture]], [[UFO reports keep pace with human technology across eras]], [[Vallée argues fiction anticipated specific UFO report details]]

---

## Appendix — A Century of UFO Landings (1868–1968)

Vallée's catalogue of landing/close-encounter cases compiled from French,
Italian, Anglo-American and worldwide sources (building on Aimé Michel, Guy
Quincy, the *Flying Saucer Review* "Humanoids" issue, and ATIC files), with an
explicit methodology and a warning about reliability.

**Concepts:** [[A Century of UFO Landings (Vallée's catalogue)]]
**Claims:** [[The catalogue indexes a century of UFO landings from 1868 to 1968]], [[Vallée recommends small informal investigation groups over large organizations]]
"""

# ---------------------------------------------------------------------------
PERSONS = [
    ("Jacques Vallée", "jacques-vallee", ["Jacques Vallée"],
     ["astronomer", "computer scientist", "ufologist", "author"],
     "French-born astronomer and computer scientist, author of *Passport to "
     "Magonia* (1969) and a central figure in the shift of ufology toward the "
     "folklore / interdimensional interpretation of UFOs. In the book he combines "
     "scientific training, folklore scholarship and case files to argue that UFO "
     "encounters are the modern form of an ancient phenomenon, while carefully "
     "withholding any claim that the objects are physical or extraterrestrial.",
     ["Vallée argues the UFO phenomenon and the fairy-faith are the same phenomenon",
      "Aimé Michel"]),
    ("Agobard of Lyons", "agobard-of-lyons", ["Saint Agobard"],
     ["Archbishop of Lyons (9th century)", "theologian"],
     "Ninth-century Archbishop of Lyons (c.779–840) whose treatise records that "
     "people of his time believed in a sky-region called *Magonia* from which "
     "cloud-ships sailed to carry off crops; he describes four captives said to "
     "have fallen from these ships, whom he saved from stoning by declaring the "
     "belief false. Vallée takes the name Magonia from this account and notes that "
     "occultists later reinterpreted the same incident (the Comte de Gabalis story "
     "of the Sylphs and Zedechias).",
     ["The name Magonia derives from Agobard of Lyons's account of cloud-ships",
      "Magonia"]),
    ("Robert Kirk (minister)", "robert-kirk-minister", ["Reverend Robert Kirk"],
     ["Scottish minister", "folklorist"],
     "Scottish minister of Aberfoyle (d.1692) who in 1691 wrote *The Secret "
     "Commonwealth of Elves, Fauns and Fairies*, the first systematic description "
     "of the fairy races. Vallée reproduces a 16-point summary of Kirk's findings "
     "(intermediate nature between man and angels; fluid bodies; ability to carry "
     "things off; underground dwellings with self-lit lamps; whistling speech; "
     "tribal organization) and argues it matches the modern ufonauts.",
     ["Robert Kirk's Secret Commonwealth systematized fairy traits matching ufonauts",
      "The Secret Commonwealth"]),
    ("Ludovico Maria Sinistrari", "ludovico-maria-sinistrari", [],
     ["Franciscan theologian", "Inquisition councillor"],
     "Italian Franciscan theologian (1622–1701), councillor to the Supreme "
     "Tribunal of the Inquisition, author of the manuscript *De Daemonialitate, et "
     "Incubis, et Succubis*. Vallée uses Sinistrari's careful argument that incubi "
     "and succubi are a distinct, embodied aerial species — not the devil, since "
     "they ignore exorcism and relics — as a 17th-century parallel to the genetic "
     "/ sexual dimension of modern UFO contact.",
     ["Sinistrari argued incubi are a separate aerial species not the devil",
      "Daemonialitas"]),
    ("Aimé Michel", "aime-michel", [],
     ["French science writer", "ufologist"],
     "French science writer whose work on the 1954 French wave (and the "
     "'straight-line mystery') Vallée drew on heavily. Michel advanced the idea, "
     "which Vallée calls the most intriguing put forward, that a superior race's "
     "actions would appear random or absurd to us — and might be intended to "
     "change human destiny by confronting us with our limitations.",
     ["Vallée concludes a superior intelligence would necessarily appear absurd"]),
    ("W. Y. Evans-Wentz", "evans-wentz", ["Walter Evans-Wentz"],
     ["folklorist", "anthropologist"],
     "Scholar whose 1909 study *The Fairy-Faith in Celtic Countries* gathered "
     "first-hand Celtic accounts of the Gentry, fairy food, fairy rings and "
     "abductions. Vallée quotes Evans-Wentz extensively to establish the detailed "
     "correspondence between the fairy-faith and modern UFO reports.",
     ["Vallée argues the UFO phenomenon and the fairy-faith are the same phenomenon",
      "The Gentry (Good People / Sleagh Maith)"]),
    ("Joe Simonton", "joe-simonton", [],
     ["chicken farmer", "UFO witness"],
     "Sixty-year-old Wisconsin chicken farmer who, on 18 April 1961 at Eagle "
     "River, said he gave water to occupants of a landed saucer and received three "
     "pancakes in return; Air Force analysis (via J. Allen Hynek) found them an "
     "ordinary terrestrial buckwheat pancake. Vallée makes the case the centerpiece "
     "of his fairy-food parallel.",
     ["Joe Simonton was given pancakes by saucer occupants echoing fairy food",
      "Eagle River incident (Simonton, 1961)"]),
    ("Maurice Masse", "maurice-masse", [],
     ["lavender farmer", "UFO witness"],
     "Valensole (France) lavender farmer who on 1 July 1965 reported encountering "
     "two small beings beside a landed egg-shaped craft; one pointed a tube at him "
     "and he was paralyzed yet conscious for the encounter, afterwards suffering "
     "weeks of compulsive drowsiness. Vallée treats it as a model 'close-proximity' "
     "case (paralysis, benign impression, after-effects).",
     ["Witnesses report paralysis and missing time near landed craft",
      "Valensole encounter (Masse, 1965)"]),
]

GROUPS = [
    ("The Gentry (Good People / Sleagh Maith)", "the-gentry-good-people",
     "folkloric_collective", ["Good People", "Good Neighbors", "Sleagh Maith", "the Gentry"],
     "The Celtic fairy races as described by Evans-Wentz's informants: a tall, "
     "noble, 'military-aristocratic' people, neither human nor spirit, who live in "
     "mountains and the sea, travel in companies, take an interest in human "
     "affairs, can appear and vanish, and 'take' people body and soul. Vallée "
     "argues the Gentry are indistinguishable from the occupants of modern UFOs.",
     ["The Secret Commonwealth",
      "Vallée argues the UFO phenomenon and the fairy-faith are the same phenomenon"]),
    ("Flying Saucer Review (FSR)", "flying-saucer-review",
     "publication", ["FSR"],
     "London-based UFO journal (founded 1955) that Vallée repeatedly cites as the "
     "most reliable serious outlet for first-hand reports; its 1966 special issue "
     "'The Humanoids' (chaired by editor Charles Bowen) listed over three hundred "
     "landing reports with bibliographies and served as a key source for Vallée's "
     "catalogue.",
     ["A Century of UFO Landings (Vallée's catalogue)",
      "Vallée recommends small informal investigation groups over large organizations"]),
]

LOCATIONS = [
    ("Eagle River (Wisconsin)", "eagle-river-wisconsin", [],
     "Rural town in Wisconsin, USA, home of Joe Simonton and site of the 18 April "
     "1961 'pancake' encounter that Vallée uses as the bridge between ufology and "
     "the Celtic 'food from fairyland' tradition.",
     ["Eagle River incident (Simonton, 1961)", "Joe Simonton"]),
    ("Valensole (France)", "valensole-france", [],
     "Lavender-growing plateau in Alpes-de-Haute-Provence, France, where farmer "
     "Maurice Masse reported his 1 July 1965 close-proximity encounter and "
     "paralysis.",
     ["Valensole encounter (Masse, 1965)", "Maurice Masse"]),
    ("Knock (County Mayo, Ireland)", "knock-ireland", [],
     "Village in the west of Ireland where, on 21 August 1879, fifteen witnesses "
     "reported an apparition of figures (identified as the Virgin, St. Joseph and "
     "St. John) in a stationary golden light on the church gable in heavy rain — "
     "the ground beneath staying dry. Vallée presents it as structurally identical "
     "to a UFO event.",
     ["Knock apparition (1879)",
      "Catholic apparitions such as Knock and Fatima are structurally UFO events"]),
]

EVENTS = [
    ("Eagle River incident (Simonton, 1961)", "eagle-river-incident-1961",
     "1961-04-18", "1961-04-18",
     ["Joe Simonton"], "[[Eagle River (Wisconsin)]]",
     "On 18 April 1961 at about 11:00 a.m., Wisconsin farmer Joe Simonton said a "
     "silvery saucer hovered by his yard; an occupant held out a jug, Simonton "
     "filled it with water, and in return was handed three perforated pancakes "
     "while another occupant 'fried food on a flameless grill'. The encounter "
     "lasted about five minutes. Air Force analysis (J. Allen Hynek, Maj. Robert "
     "Friend) found the cake an ordinary terrestrial buckwheat pancake. Vallée "
     "links it to the Celtic tradition that fairy food contains no salt.",
     ["Joe Simonton was given pancakes by saucer occupants echoing fairy food"]),
    ("Valensole encounter (Masse, 1965)", "valensole-encounter-1965",
     "1965-07-01", "1965-07-01",
     ["Maurice Masse"], "[[Valensole (France)]]",
     "On 1 July 1965 at 6:00 a.m. lavender farmer Maurice Masse approached a "
     "landed egg-shaped craft and two small beings; one pointed a small tube at "
     "him and he became unable to move while remaining fully conscious. The beings "
     "left and the craft vanished. Masse suffered weeks of compulsive sleepiness "
     "afterward and reported a strong impression that the beings were 'good'.",
     ["Witnesses report paralysis and missing time near landed craft"]),
    ("Socorro encounter (Zamora, 1964)", "socorro-encounter-1964",
     "1964-04-24", "1964-04-24",
     ["Project Blue Book (US Air Force)"], "Socorro, New Mexico",
     "On 24 April 1964 police officer Lonnie Zamora reported a shiny egg-shaped "
     "object on landing pads with two small white-clad beings nearby; it took off "
     "with a roar then flew silently, leaving physical traces measured by police "
     "and an FBI man. Vallée notes Zamora asked to see a priest before releasing "
     "his report — an emotional pattern he calls reminiscent of medieval "
     "apparitions. Project Blue Book left the case 'still open'.",
     ["UFO occupants gather plant and soil samples and claim to be from Mars"]),
    ("Tully saucer nests (1966)", "tully-saucer-nests-1966",
     "1966-01-19", "1966-01-19",
     [], "Horseshoe Lagoon, Tully, Queensland, Australia",
     "On 19 January 1966 banana grower George Pedley reported a blue-grey craft "
     "rising from a swamp; investigators found several circular 'nests' of "
     "flattened and uprooted reeds (clockwise and counter-clockwise). Vallée sets "
     "these alongside the Ohio ring (1965) and the Charlton crater (1963) as "
     "modern instances of the folkloric 'fairy ring'.",
     ["Saucer nests match the fairy rings of folklore"]),
    ("Kelly–Hopkinsville goblins (1955)", "kelly-hopkinsville-goblins-1955",
     "1955-08-21", "1955-08-21",
     [], "near Kelly / Hopkinsville, Kentucky",
     "On the night of 21 August 1955 a Kentucky farm family reported a siege by "
     "several small 'little men' with oversized round heads, long taloned arms and "
     "large lidless eyes set on the sides of the head, who floated when shot and "
     "ran on all fours. Vallée notes the glowing aluminium-like appearance recalls "
     "the 'sylphs of 1491'.",
     ["Vallée argues the UFO phenomenon and the fairy-faith are the same phenomenon"]),
    ("Knock apparition (1879)", "knock-apparition-1879",
     "1879-08-21", "1879-08-21",
     [], "[[Knock (County Mayo, Ireland)]]",
     "On 21 August 1879 fifteen witnesses (aged 6 to 75) reported figures and an "
     "altar with a lamb in a brilliant, changing golden light on the gable of "
     "Knock church during heavy rain; one witness who tried to embrace the figures "
     "felt only the wall, and the ground beneath the light stayed dry. Cures were "
     "reported afterward. Vallée presents it as a religious 'UFO event' whose "
     "message was doctrinal rather than technological.",
     ["Catholic apparitions such as Knock and Fatima are structurally UFO events"]),
]

CONCEPTS = [
    ("Magonia", "magonia", [],
     "The sky-region named in Agobard of Lyons's 9th-century account, from which "
     "cloud-ships were believed to sail to steal crops. Vallée adopts it as the "
     "title-metaphor for the 'parallel world' from which the phenomenon's "
     "occupants — fairies, sylphs, demons, ufonauts — are reported to come, and "
     "for the relativity of time associated with it in folklore.",
     ["The name Magonia derives from Agobard of Lyons's account of cloud-ships",
      "Interdimensional hypothesis (UFOs as windows not objects)"]),
    ("The control system (Vallée's functioning lie)", "control-system-functioning-lie",
     ["the functioning lie"],
     "Vallée's central conjecture that human action is driven by imagination and "
     "belief rather than objective observation, and that 'to control human "
     "imagination is to shape mankind's collective destiny, provided the source of "
     "this control is not identifiable by the public.' He argues it is "
     "demonstrably possible to make populations believe in supernatural races by "
     "exposing them to a few carefully engineered scenes tailored to their culture "
     "— without committing to whether the UFO phenomenon is such a system or who "
     "(if anyone) runs it.",
     ["Vallée proposes a control system that shapes belief through engineered apparitions",
      "The phenomenon's secondary features adapt to the witness's culture"]),
    ("The Secret Commonwealth", "the-secret-commonwealth", [],
     "Title of Rev. Robert Kirk's 1691 treatise and Vallée's term for the ordered "
     "society of aerial/elemental beings it describes. Vallée's 16-point summary of "
     "Kirk (fluid bodies, ability to carry things off, underground self-lit "
     "dwellings, whistling speech, tribal structure, a philosophy of perpetual "
     "cyclical renewal) is offered as a near-exact template for the modern "
     "ufonauts.",
     ["Robert Kirk's Secret Commonwealth systematized fairy traits matching ufonauts",
      "The Gentry (Good People / Sleagh Maith)"]),
    ("Daemonialitas", "daemonialitas", ["demoniality"],
     "The category, named by Sinistrari, for carnal contact between humans and "
     "nonhuman beings (incubi/succubi), distinguished from bestiality. Vallée uses "
     "it to surface the sexual and genetic dimension of the phenomenon — "
     "changelings, human midwives, intermarriage, the biblical 'sons of God' and "
     "giants, and modern abduction cases (Villas-Boas, the Hills) — that modern "
     "fairy tales have censored out.",
     ["Daemonialitas records sexual and genetic contact between humans and nonhuman beings",
      "Sinistrari argued incubi are a separate aerial species not the devil"]),
    ("Interdimensional hypothesis (UFOs as windows not objects)", "interdimensional-hypothesis-windows",
     ["windows not objects"],
     "Vallée's speculative alternative to the extraterrestrial hypothesis: that "
     "UFOs may be 'windows' rather than 'objects' — manifestations from a parallel "
     "reality or from a manipulation of space-time — which could account for their "
     "ability to appear and vanish, leave physical traces, and distort time. He "
     "presents it among 'conjectures' and stresses it has no scientific footing.",
     ["Vallée argues the extraterrestrial hypothesis is an insufficient explanation",
      "Magonia"]),
    ("Vallée's Five Facts of the UFO phenomenon", "vallee-five-facts", [],
     "Vallée's summary of what stands clearly from the data: (1) since mid-1946 an "
     "active worldwide generation of close-to-the-ground sighting rumors with "
     "physical traces and effects; (2) the saucer myth coincides with the Celtic "
     "fairy-faith and older traditions; (3) reported entities fall into recurring "
     "biological types, chiefly two kinds of dwarf (dark/hairy gnome-like and "
     "human-complexioned sylph-like); (4) the entities' behavior is as absurd as "
     "their craft are ludicrous and their statements are systematically "
     "misleading; (5) the apparition mechanism follows the model of religious "
     "miracles (Fatima, Guadalupe).",
     ["Vallée summarizes the UFO phenomenon in five facts",
      "Vallée's Three Propositions on the UFO phenomenon"]),
    ("Vallée's Three Propositions on the UFO phenomenon", "vallee-three-propositions", [],
     "Vallée's deductions from the Five Facts: (1) the behavior of nonhuman "
     "visitors, or of a superior race coexisting with us, would not necessarily "
     "appear purposeful to humans; (2) since the nature of time remains a puzzle, "
     "no theory of possible visitors can ignore our ignorance of it; (3) the whole "
     "mystery contains all the elements of a myth usable for political or "
     "sociological purposes, evidenced by the link between report content and the "
     "progress of human technology.",
     ["Vallée concludes a superior intelligence would necessarily appear absurd",
      "Vallée's Five Facts of the UFO phenomenon"]),
    ("A Century of UFO Landings (Vallée's catalogue)", "century-of-ufo-landings-catalogue", [],
     "The book's appendix: an indexed catalogue of UFO landing / close-encounter "
     "cases for 1868–1968, compiled from cross-indexed international sources "
     "(Aimé Michel, Guy Quincy, the *Flying Saucer Review* 'Humanoids' issue, ATIC "
     "files). About 35% of entries include occupant descriptions. Vallée includes "
     "a methodology and a warning that inclusion implies no claim of physical "
     "reality and that cases differ in reliability.",
     ["The catalogue indexes a century of UFO landings from 1868 to 1968",
      "Flying Saucer Review (FSR)"]),
    ("Saucer nests and fairy rings", "saucer-nests-and-fairy-rings", [],
     "Vallée's grouping of ground-trace phenomena: circular flattened/uprooted "
     "vegetation (the Tully 'nests' 1966, the Ohio ring 1965, the Charlton crater "
     "1963) which he sets against the folkloric 'fairy rings' where grass grows "
     "differently and which tradition attributes to fairy dancing.",
     ["Saucer nests match the fairy rings of folklore"]),
    ("Fairy food and the rite of hospitality", "fairy-food-rite-of-hospitality", [],
     "The folklore motif that food links humans and the Other: one must not eat "
     "fairy food or be unable to return; fairy food is saltless; and the exchange "
     "of food (Simonton's water-for-pancakes, biblical hospitality to angels) "
     "constitutes a sacred bond. Vallée uses Hartland's analysis of the rite of "
     "hospitality to read the Eagle River exchange as a ceremony rather than a "
     "sample collection.",
     ["Joe Simonton was given pancakes by saucer occupants echoing fairy food"]),
]

CONTROVERSIES = [
    ("Extraterrestrial hypothesis versus the folklore/interdimensional hypothesis",
     "eth-versus-folklore-interdimensional-hypothesis",
     "Chapter 'Angels or Devils?' (The Secret Commonwealth) and the conclusion 'The Functioning Lie'",
     ["Extraterrestrial hypothesis: UFOs are material craft from another planet — a view Vallée says science fiction has made acceptable and which sample-taking, trace-leaving cases superficially support",
      "Folklore/interdimensional hypothesis (Vallée): the phenomenon is the modern form of the fairy-faith and religious apparitions, possibly 'windows' from a parallel reality, and the ETH is 'not a complete answer'",
      "Vallée's own position: agnostic on the physical nature of the objects; the deeper, answerable question is the mechanism and human effect, not the craft's origin"],
     "Vallée argues the ETH cannot be 'stronger than the Celtic faith in the elves' "
     "and that the historical continuity of the phenomenon makes a purely "
     "extraterrestrial, nuts-and-bolts reading insufficient — while explicitly "
     "refusing to assert the interdimensional alternative as fact.",
     ["Vallée argues the extraterrestrial hypothesis is an insufficient explanation",
      "Interdimensional hypothesis (UFOs as windows not objects)"]),
    ("Are religious apparitions UFO phenomena?", "are-religious-apparitions-ufo-phenomena",
     "Chapter 'Daemonialitas' ('A Great Sign in Heaven') and Fact 5 of the conclusion",
     ["Vallée: cases bearing the Catholic Church's stamp (Fatima, Guadalupe, Knock) are, if the definitions are applied strictly, UFO phenomena in which the entity delivered a religious rather than a technological message",
      "Traditional religious view: these are genuine divine apparitions of a wholly different character",
      "Skeptical view: reflections, hoaxes or mass suggestion (e.g. the magic-lantern tests at Knock)"],
     "Vallée presents the structural identity (stationary light, figures, "
     "physical anomalies, witnesses of all ages, subsequent cures) without "
     "adjudicating the theological question, treating the apparition mechanism as "
     "the same one underlying the fairy-faith and modern landings.",
     ["Catholic apparitions such as Knock and Fatima are structurally UFO events",
      "Knock apparition (1879)"]),
]

# ---------------------------------------------------------------------------
P = lambda link: {"type": "person", "link": link}
G = lambda link: {"type": "group", "link": link}

CLAIMS = [
    ("Vallée argues the UFO phenomenon and the fairy-faith are the same phenomenon",
     "ufo-phenomenon-and-fairy-faith-same", "1969 (argument); cases 1868–1968",
     [P("Jacques Vallée")], "Worldwide", '["Chapters 1–3", "Conclusion"]',
     "the book's central thesis",
     "Vallée argues that the modern, global belief in flying saucers and their "
     "occupants is identical to the earlier fairy-faith: the entities described as "
     "UFO pilots are indistinguishable from the elves, sylphs and lutins of the "
     "Middle Ages, and both belong to what folklore called the Secret Commonwealth.",
     "He writes that 'the modern, global belief in flying saucers and their "
     "occupants is identical to an earlier belief in the fairy-faith' and that the "
     "~20,000 post-WWII reports are 'nothing but a resurgence of a deep stream in "
     "human culture known in older times under various other names.'",
     "Stated explicitly as his 'basic contention,' while he cautions he is not "
     "thereby assuming the objects are physically real.",
     ["The Secret Commonwealth", "The Gentry (Good People / Sleagh Maith)",
      "W. Y. Evans-Wentz"]),

    ("The name Magonia derives from Agobard of Lyons's account of cloud-ships",
     "magonia-from-agobard", "c. 830 (Agobard); cited 1969",
     [P("Agobard of Lyons")], "Lyons, France", '["Chapter 1"]',
     "source of the book's title",
     "Vallée takes the title 'Magonia' from a treatise of Agobard, Archbishop of "
     "Lyons, who recorded a 9th-century belief in a sky-region called Magonia from "
     "which cloud-ships sailed to carry off crops; Agobard saved four people said "
     "to have fallen from such ships from being stoned.",
     "He quotes Agobard's text on the 'certain region, which they call Magonia, "
     "whence ships sail in the clouds' and notes occultists (the Comte de Gabalis) "
     "later reinterpreted the same Lyons incident as the Sylphs of Zedechias.",
     "Used to establish the deep historical pedigree of the 'cloud-ship/aerial "
     "people' motif.",
     ["Magonia", "Agobard of Lyons"]),

    ("Facius Cardan recorded seven aerial beings who said they were made of air in 1491",
     "facius-cardan-seven-aerial-beings-1491", "13 August 1491",
     [P("Jacques Vallée")], "Milan, Italy", '["Chapter 1"]',
     "key medieval contact case",
     "Vallée reproduces (via Jerome Cardan's *De Subtilitate*) Facius Cardan's "
     "account of seven men in shining silken garments who appeared to him in 1491, "
     "said they were 'men composed, as it were, of air, and subject to birth and "
     "death,' might live up to 300 years, and disagreed among themselves about "
     "whether God created the world from eternity or 'from moment to moment.'",
     "He quotes the 1491 record at length, highlighting the sylph's remark that "
     "God 'created [the universe] from moment to moment' as antedating quantum "
     "theory by four centuries.",
     "Offered as a Renaissance instance of the recurring 'aerial people' contact, "
     "linked to Paracelsus's theories of the Elementals.",
     ["Magonia", "The Secret Commonwealth"]),

    ("Vallée proposes a control system that shapes belief through engineered apparitions",
     "control-system-engineered-apparitions", "1969 (thesis)",
     [P("Jacques Vallée")], "Worldwide", '["Conclusion (The Functioning Lie)"]',
     "the book's interpretive conclusion",
     "Vallée proposes that human action rests on imagination and belief rather "
     "than objective observation, so that controlling imagination shapes "
     "collective destiny 'provided the source of this control is not identifiable "
     "by the public' — and that it is demonstrably possible to make populations "
     "believe in supernatural races via a few carefully engineered, culturally "
     "tailored scenes.",
     "He states it is possible 'to make large sections of any population believe "
     "in the existence of supernatural races ... by exposing them to a few "
     "carefully engineered scenes,' but stops short of claiming the UFO phenomenon "
     "is such a system or naming any controller.",
     "His central conjecture (the 'functioning lie'); he stresses it holds "
     "regardless of whether the objects are physical.",
     ["The control system (Vallée's functioning lie)",
      "The phenomenon's secondary features adapt to the witness's culture"]),

    ("The phenomenon's secondary features adapt to the witness's culture",
     "secondary-features-adapt-to-culture", "1969 (analysis)",
     [P("Jacques Vallée")], "Worldwide", '["Conclusion"]',
     "core structural observation",
     "Vallée distinguishes the phenomenon's stable, invariant features from its "
     "'chameleon-like' secondary attributes — craft shape, occupant appearance, "
     "and claimed origin — which vary as a function of the cultural environment "
     "into which they are projected.",
     "He notes the entities appear as 'science fiction monsters' in the US, "
     "'sanguinary' in South America, 'rational, Cartesian' tourists in France, and "
     "as an aristocratic order in Celtic lore, while the underlying pattern stays "
     "constant.",
     "Underpins both the fairy/UFO identity and the control-system argument.",
     ["The control system (Vallée's functioning lie)",
      "UFO reports keep pace with human technology across eras"]),

    ("Vallée summarizes the UFO phenomenon in five facts",
     "vallee-five-facts-summary", "1969",
     [P("Jacques Vallée")], "Worldwide", '["Conclusion"]',
     "explicit numbered summary",
     "Vallée distills the data into five 'facts': (1) since mid-1946 an active "
     "worldwide generation of close-to-the-ground sighting rumors with physical "
     "traces; (2) the saucer myth coincides with the Celtic fairy-faith; (3) "
     "entities fall into recurring types, chiefly two dwarf forms (gnome-like and "
     "sylph-like); (4) entity behavior is consistently absurd and their statements "
     "systematically misleading; (5) the apparition mechanism follows the model of "
     "religious miracles.",
     "Listed as 'Fact 1' through 'Fact 5' in the concluding chapter.",
     "The empirical base from which he draws his Three Propositions.",
     ["Vallée's Five Facts of the UFO phenomenon",
      "Vallée's Three Propositions on the UFO phenomenon"]),

    ("Vallée concludes a superior intelligence would necessarily appear absurd",
     "superior-intelligence-appears-absurd", "1969",
     [P("Aimé Michel")], "Worldwide", '["Chapter 1", "Conclusion (Proposition 1)"]',
     "key proposition (after Aimé Michel)",
     "Vallée argues, following Aimé Michel, that the organized action of a "
     "superior race must appear absurd or random to an inferior one, so scientists "
     "who dismiss UFO reports because 'intelligent visitors would not behave like "
     "that' have not thought seriously about nonhuman intelligence.",
     "He likens human attempts to find purpose in the behavior to a dog "
     "confronted with a mathematician writing on a blackboard, and states this "
     "absurdity 'has had the effect of keeping professional scientists away.'",
     "Proposition 1 of his conclusion; also explains Fact 4.",
     ["The absurd behavior of UFO entities keeps science away and gives the myth religious overtones",
      "Vallée's Three Propositions on the UFO phenomenon"]),

    ("Joe Simonton was given pancakes by saucer occupants echoing fairy food",
     "simonton-pancakes-fairy-food", "18 April 1961",
     [P("Joe Simonton")], "[[Eagle River (Wisconsin)]]", '["Chapter 2"]',
     "centerpiece of the fairy-food parallel",
     "Vallée recounts that Joe Simonton gave water to occupants of a landed saucer "
     "at Eagle River and received three pancakes, which Air Force analysis found to "
     "be an ordinary terrestrial buckwheat pancake — and notes the analysis found "
     "no salt, matching the Celtic tradition that fairy food is saltless and that "
     "the pure water the occupants took mirrors fairy custom.",
     "He sets the case against Evans-Wentz's 'food from fairyland' tales and "
     "Hartland's analysis of the rite of hospitality, reading the exchange as a "
     "ceremony rather than sample-collection. J. Allen Hynek confirmed Simonton "
     "believed the experience was real.",
     "The book's primary worked example of the fairy/UFO correspondence.",
     ["Eagle River incident (Simonton, 1961)",
      "Fairy food and the rite of hospitality", "Joe Simonton"]),

    ("Vallée links UFO sightings to cattle theft and mutilation across centuries",
     "ufo-cattle-theft-mutilation", "1897–1967 (cases)",
     [P("Jacques Vallée")], "United States and Europe", '["Chapter 3 (The Haunted Land)"]',
     "recurring theme across folklore and ufology",
     "Vallée connects modern animal theft and mutilation reports (Alexander "
     "Hamilton's 1897 sworn Kansas affidavit of an airship lifting a heifer; the "
     "1967 'Snippy' horse mutilation in Colorado) with the folkloric motif of "
     "fairies stealing cattle and produce.",
     "He quotes Hamilton's affidavit ('I don't know whether they are devils or "
     "angels ... but we all saw them') and the disputed Snippy case with its "
     "circular ground marks and missing organs.",
     "Part of the chapter showing the parallel 'verges on the ludicrous ... but to "
     "pursue the investigation further leads to horror.'",
     ["Vallée argues the UFO phenomenon and the fairy-faith are the same phenomenon"]),

    ("Saucer nests match the fairy rings of folklore",
     "saucer-nests-match-fairy-rings", "1963–1966 (cases)",
     [P("Jacques Vallée")], "Australia, Ohio, England", '["Chapter 2 (Rings in the Moonlight)"]',
     "ground-trace parallel",
     "Vallée argues that 'saucer nests' — circular patches of flattened or "
     "uprooted vegetation (the Tully nests 1966, the Ohio ring 1965, the Charlton "
     "crater 1963) — are the modern form of the folkloric 'fairy rings' that "
     "tradition attributes to fairy dancing.",
     "He catalogues common features (flattening force with stationary or rotating "
     "pattern, removed vegetation, central holes, occasional magnetism) and recalls "
     "'that celebrated habit of the fairies, to leave behind them strange rings in "
     "the fields.'",
     "One of several physical-trace categories he treats as 'borderline' yet "
     "significant.",
     ["Saucer nests and fairy rings", "Tully saucer nests (1966)"]),

    ("UFO occupants gather plant and soil samples and claim to be from Mars",
     "occupants-gather-samples-claim-mars", "1964 (cases)",
     [P("Jacques Vallée")], "United States and worldwide", '["Chapter 3 (Angels or Devils?)"]',
     "the 'sample-gathering' pattern",
     "Vallée notes many landing reports show occupants taking plants, soil and "
     "animals and even interviewing witnesses about agriculture — e.g. Gary Wilcox "
     "(Tioga, NY, 24 April 1964) who said two beings carrying soil trays told him "
     "'we are from what you people refer to as Planet Mars' and asked about "
     "fertilizer.",
     "He observes such behavior is 'well designed to make the investigators ... "
     "assume that the visitors are gathering samples with all the care and "
     "precision of seasoned exobiologists,' yet matches the folkloric theft of "
     "produce.",
     "Used to argue the 'Mars' framing is a culturally-tailored secondary feature, "
     "not evidence of literal Martian origin.",
     ["Socorro encounter (Zamora, 1964)",
      "The phenomenon's secondary features adapt to the witness's culture"]),

    ("Witnesses report paralysis and missing time near landed craft",
     "paralysis-and-missing-time", "1965 (Valensole) and others",
     [P("Maurice Masse")], "[[Valensole (France)]]", '["Chapter 1", "Folklore in the Making"]',
     "recurring close-proximity effect",
     "Vallée documents that witnesses near landed craft are frequently "
     "'paralyzed' — immobilized while remaining conscious — as with Maurice Masse "
     "at Valensole (1965) and Georges Gatay's eight-man crew at Nouâtre (1954); he "
     "links this to the fairy-faith motif of being struck immobile and to the "
     "relativity of time 'in Magonia.'",
     "He clarifies the word 'paralysis' is loose — Masse stayed conscious with "
     "normal heartbeat but could not move, then suffered weeks of compulsive "
     "drowsiness — and parallels the Hill abduction's account.",
     "A 'little-known characteristic of close-proximity cases' he uses to tie "
     "modern reports to abduction folklore.",
     ["Valensole encounter (Masse, 1965)", "Maurice Masse", "Magonia"]),

    ("Daemonialitas records sexual and genetic contact between humans and nonhuman beings",
     "daemonialitas-sexual-genetic-contact", "1969 (analysis); 17th c. sources",
     [P("Jacques Vallée")], "Europe", '["Chapter Daemonialitas"]',
     "the censored sexual/genetic dimension",
     "Vallée argues the sexual and genetic dimension — changelings, human "
     "midwives, intermarriage with the Gentry, incubi/succubi, and modern "
     "abduction cases (Villas-Boas, the Hills) — is the element censored out of "
     "modern fairy tales but central to the phenomenon, and that belief in "
     "human–nonhuman intermarriage is a corollary of apparitions in every "
     "historical context.",
     "He cites Kirk on succubi ('Leannain Sith'), Evans-Wentz's fairy-lover tales, "
     "and the biblical 'sons of God' begetting giants (Genesis 6:4) as evidence of "
     "a recurring 'genetic' theme.",
     "Framed as what gives the tradition its lasting impact and links witchcraft, "
     "fairy-faith and ufology.",
     ["Daemonialitas", "Sinistrari argued incubi are a separate aerial species not the devil"]),

    ("Sinistrari argued incubi are a separate aerial species not the devil",
     "sinistrari-incubi-separate-species", "later 17th century",
     [P("Ludovico Maria Sinistrari")], "Pavia / Milan, Italy", '["Chapter Daemonialitas"]',
     "key historical authority",
     "Vallée presents Fr. Sinistrari's *De Daemonialitate* argument that incubi "
     "and succubi are not the possessing devils of exorcism — since they ignore "
     "relics and holy objects — but a distinct, embodied aerial race, closely "
     "resembling the fairies and Elementals, capable of carnal contact with humans.",
     "He quotes Sinistrari's reasoning that demoniality differs from bestiality, "
     "and his and Maluenda's lists of figures said to be born of such unions, "
     "while noting Sinistrari doubted the devil could actually engender children.",
     "Vallée's 17th-century parallel for the 'genetic' reading of modern UFO "
     "contact.",
     ["Daemonialitas", "Ludovico Maria Sinistrari"]),

    ("Catholic apparitions such as Knock and Fatima are structurally UFO events",
     "catholic-apparitions-are-ufo-events", "1879 (Knock); 1917 (Fatima)",
     [P("Jacques Vallée")], "Ireland; Portugal", '["Chapter Daemonialitas (A Great Sign in Heaven)", "Conclusion (Fact 5)"]',
     "Fact 5 of the conclusion",
     "Vallée argues that apparition cases bearing the Catholic Church's stamp — "
     "Fatima, Guadalupe, and the 1879 Knock apparition — are, if the definitions "
     "are applied strictly, UFO phenomena in which the entity delivered a religious "
     "rather than a technological message.",
     "He details Knock (stationary changing golden light, figures and a lamb, a "
     "witness whose embrace met only the wall, dry ground under the light during "
     "heavy rain, subsequent cures) as structurally identical to a landing.",
     "Stated as Fact 5: the apparition mechanism 'is standard and follows the "
     "model of religious miracles.'",
     ["Knock apparition (1879)", "Are religious apparitions UFO phenomena?"]),

    ("Robert Kirk's Secret Commonwealth systematized fairy traits matching ufonauts",
     "kirk-secret-commonwealth-matches-ufonauts", "1691",
     [P("Robert Kirk (minister)")], "Aberfoyle, Scotland", '["Chapter 3 (The Secret Commonwealth)"]',
     "principal folklore authority",
     "Vallée summarizes Rev. Robert Kirk's 1691 *Secret Commonwealth* in sixteen "
     "points — beings intermediate between man and angels, with light 'fluid' "
     "bodies that appear and vanish, who carry things off, live underground with "
     "self-lit lamps, speak in whistling sounds, are organized into tribes, and "
     "hold a philosophy of perpetual cyclical renewal — and argues this matches "
     "the modern ufonauts.",
     "He notes the close similarity between Kirk's account and Facius Cardan's "
     "1491 visitors, and that both Kirk and Paracelsus say a pact can make these "
     "beings appear at will.",
     "The systematic 'template' for his fairy/UFO identification.",
     ["The Secret Commonwealth", "Robert Kirk (minister)",
      "The Gentry (Good People / Sleagh Maith)"]),

    ("Vallée argues the extraterrestrial hypothesis is an insufficient explanation",
     "eth-insufficient-explanation", "1969",
     [P("Jacques Vallée")], "Worldwide", '["Chapter 3", "Conclusion"]',
     "central critical stance",
     "Vallée argues the theory that flying saucers are material craft from another "
     "planet 'is not a complete answer': the belief cannot be stronger than the "
     "Celtic faith in elves or the medieval fear of demons, and the historical "
     "continuity of the phenomenon makes a purely nuts-and-bolts extraterrestrial "
     "reading inadequate.",
     "He notes the same ridicule covers both the fairy-faith and the UFO "
     "phenomenon, and that the controlling-intelligence question need not assume "
     "the objects are real or that the intelligence is extraterrestrial — it might "
     "even be human.",
     "Sets up his 'windows not objects' / control-system alternatives without "
     "asserting them as fact.",
     ["Interdimensional hypothesis (UFOs as windows not objects)",
      "Extraterrestrial hypothesis versus the folklore/interdimensional hypothesis"]),

    ("The catalogue indexes a century of UFO landings from 1868 to 1968",
     "catalogue-century-of-landings", "1868–1968",
     [G("Flying Saucer Review (FSR)")], "Worldwide", '["Appendix"]',
     "the book's reference appendix",
     "The appendix presents 'A Century of UFO Landings (1868–1968),' an indexed "
     "catalogue of landing / close-encounter cases compiled from cross-indexed "
     "international sources, of which about 35% include descriptions of occupants.",
     "Vallée describes building the index from 1961, drawing on Aimé Michel, Guy "
     "Quincy, the *Flying Saucer Review* 'Humanoids' special issue, and "
     "re-examined ATIC files (witness names deleted per official procedure), with "
     "the 1954 French/Italian wave the best-documented section.",
     "Offered as a research tool, with an explicit warning that inclusion implies "
     "no claim of physical reality.",
     ["A Century of UFO Landings (Vallée's catalogue)", "Flying Saucer Review (FSR)",
      "Aimé Michel"]),

    ("UFO reports keep pace with human technology across eras",
     "reports-keep-pace-with-technology", "1897–1968",
     [P("Jacques Vallée")], "Worldwide", '["Conclusion (Proposition 3)"]',
     "Proposition 3 of the conclusion",
     "Vallée observes a 'curious link' between report content and the progress of "
     "human technology — from aerial ships to dirigibles to ghost rockets to "
     "flying saucers — such that each era's craft are believable to that era's "
     "witnesses (the 1897 airship could not actually have flown) but not to later "
     "ones.",
     "He notes fiction even anticipated specific features and that the 1897 "
     "airship 'is no longer credible to us,' suggesting the appearance is 'designed "
     "to deceive potential witnesses.'",
     "Proposition 3, tying the phenomenon to a myth usable for sociological "
     "purposes.",
     ["The phenomenon's secondary features adapt to the witness's culture",
      "Vallée argues fiction anticipated specific UFO report details"]),

    ("Religious scripture describes celestial chariots and sky-beings",
     "scripture-celestial-chariots-sky-beings", "antiquity",
     [P("Jacques Vallée")], "Near East and worldwide", '["Chapter 1 (The Age of the Gods)"]',
     "ancient layer of the thesis",
     "Vallée notes that the foundational texts of religion describe contact with a "
     "'superior race' from the sky using luminous craft ('celestial chariots'), "
     "citing the Bible and Ezekiel's cherubim, and surveys ancient imagery (the "
     "Palenque sarcophagus, the Jomon Dogu figurines) that ancient-astronaut "
     "writers read as space visitors.",
     "He quotes Psalms ('The chariots of God are twenty thousand, even thousands "
     "of angels') and Ezekiel, while treating the ancient-astronaut readings as "
     "speculation he reports rather than endorses.",
     "Establishes the deepest historical layer of the recurring phenomenon.",
     ["Magonia"]),

    ("The absurd behavior of UFO entities keeps science away and gives the myth religious overtones",
     "absurdity-keeps-science-away", "1969",
     [P("Jacques Vallée")], "Worldwide", '["Conclusion (Fact 4)"]',
     "Fact 4 of the conclusion",
     "Vallée holds that the entities' behavior is 'as consistently absurd as the "
     "appearance of their craft is ludicrous' and their statements 'systematically "
     "misleading,' which has the dual effect of keeping professional scientists "
     "away and giving the saucer myth its religious and mystical overtones.",
     "He traces the misleading dialogue from the Gentry through the 1897 airship "
     "pilots to the alleged Martians, presenting it as an invariant feature.",
     "Fact 4; closely tied to Proposition 1 on nonhuman intelligence.",
     ["Vallée concludes a superior intelligence would necessarily appear absurd",
      "Vallée's Five Facts of the UFO phenomenon"]),

    ("Vallée argues fiction anticipated specific UFO report details",
     "fiction-anticipated-report-details", "1933; 1950",
     [P("Jacques Vallée")], "Worldwide", '["Conclusion"]',
     "supporting observation for Proposition 3",
     "Vallée points out that works of fiction anticipated specific later UFO "
     "report features: Arthur Koestler's 1933 play *Twilight Bar* contains the "
     "first UFO-caused blackout, and Bernard Newman's 1950 novel *The Flying "
     "Saucer* the first UFO car-ignition failure.",
     "He calls the coincidence between these imaginative works and the actual "
     "details later reported by the public 'remarkable,' opening 'the way to "
     "unlimited speculation' — then deliberately stops speculating.",
     "Cited as evidence the phenomenon's content tracks human imagination and "
     "technology.",
     ["UFO reports keep pace with human technology across eras",
      "The control system (Vallée's functioning lie)"]),

    ("Vallée recommends small informal investigation groups over large organizations",
     "small-informal-groups-recommendation", "1969",
     [P("Jacques Vallée")], "Worldwide", '["Conclusion"]',
     "methodological recommendation",
     "Vallée argues that large, formal UFO organizations waste energy on overhead "
     "and feuds and bury or bias their data, and that real progress would come "
     "instead from many small, informal circles gathering and rapidly publishing "
     "good first-hand reports.",
     "He states that only local residents can properly weigh a sighting, praises "
     "outlets such as the *Flying Saucer Review*, GEPA Bulletin and *Lumières dans "
     "la Nuit*, and insists 'neither a crash-program ... nor computer correlations "
     "... will easily dispose of' the problem.",
     "His prescription for turning the material into something studiable.",
     ["Flying Saucer Review (FSR)",
      "A Century of UFO Landings (Vallée's catalogue)"]),
]


# ---------------------------------------------------------------------------
def run(g):
    write = g["write_if_new"]
    n = 0
    n += write(WIKI / "sources" / "passport-to-magonia-vallee-1969.md", SOURCE_PAGE)
    n += write(WIKI / "sources" / "vallee-magonia-chapters.md", CHAPTER_NOTES)

    for (title, slug, also, roles, body, related) in PERSONS:
        n += write(WIKI / "persons" / f"{slug}.md",
                   g["person_page"](title, slug, also, roles, body, related))
    for (title, slug, category, also, body, related) in GROUPS:
        n += write(WIKI / "groups" / f"{slug}.md",
                   g["group_page"](title, slug, category, also, body, related))
    for (title, slug, also, body, related) in LOCATIONS:
        n += write(WIKI / "locations" / f"{slug}.md",
                   g["location_page"](title, slug, also, body, related))
    for (title, slug, ds, de, parts, loc, overview, kc) in EVENTS:
        n += write(WIKI / "events" / "ufo-folklore" / f"{slug}.md",
                   g["event_page"](title, slug, ds, de, parts, loc, overview, kc))
    for (title, slug, also, body, related) in CONCEPTS:
        n += write(WIKI / "concepts" / f"{slug}.md",
                   g["concept_page"](title, slug, also, body, related))
    for (title, slug, locus, positions, body, related) in CONTROVERSIES:
        n += write(WIKI / "controversies" / "ufo-folklore" / f"{slug}.md",
                   g["controversy_page"](title, slug, locus, positions, body, related))
    for c in CLAIMS:
        title, slug, dop, actors, loc, ctx, prev, stmt, evid, ctxnote, rel = c[:11]
        opposing = c[11] if len(c) > 11 else None
        n += write(WIKI / "claims" / "ufo-folklore" / f"{slug}.md",
                   g["claim_page"](title, slug, dop, actors, loc, ctx, prev,
                                   stmt, evid, ctxnote, rel, opposing))
    print(f"Magonia ingest: {n} new pages written.")
