#!/usr/bin/env python3
"""Bulk-create wiki pages for *Oahspe: A New Bible* (John Ballou Newbrough,
1882; this e-book a 2021 OK Publishing reprint).

Strict-extraction ingest. Everything below is drawn from the provided text. The
cosmology, anthropology, pantheon, prophetic system, and doctrines are presented
as Oahspe presents them — as a revelation written, per the book itself, by "the
Embassadors of the angel hosts of heaven" through a mortal instrument in the
"kosmon era." No external commentary, rebuttal, or training-data biography is
added; the book's own claims (e.g. that worlds are made by vortices, that the
sun does not give heat, that Christ was a false God) are recorded as the source's
assertions, not as fact.

Topic folder: oahspe.
"""
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
TOPIC = "oahspe"
TODAY = "2026-06-08"
SRC_TITLE = "Oahspe: A New Bible (Newbrough, 1882)"
SRC = f"[[{SRC_TITLE}]]"

# ---- Title registry (keep cross-links exact) -------------------------------
# Persons
P_NEWBROUGH = "John Ballou Newbrough"
P_ANUHASAJ = "Anuhasaj (De'yus, the false Lord God)"
P_LOOEAMONG = "Looeamong (the false Christ)"
P_KABALACTES = "Kabalactes (the false Buddha)"
P_ENNOCHISSA = "Ennochissa (the false Brahma)"
P_THOTH = "Thoth (Gabriel, founder of Mohammedanism)"
P_APH = "Aph, Son of Jehovih"
P_ZARATHUSTRA = "Zarathustra (Zoroaster)"
P_MOSES = "Moses (Oahspe)"
P_CAPILYA = "Capilya"
P_CHINE = "Chine"
P_ABRAM = "Abram (Abraham, Oahspe)"
P_BRAHMA = "Brahma (Oahspe)"
P_PO = "Po"
P_EAWAHTAH = "Ea-wah-tah"
P_SAKAYA = "Sakaya (the historical Buddha)"
P_KAYU = "Ka'yu (Confucius)"
P_JOSHU = "Joshu (the historical Jesus)"
P_THOTHMA = "Thothma (builder of the great pyramid)"
P_TAE = "Tae (the representative man of Kosmon)"

# Groups
G_FAITHISTS = "The Faithists (Oahspe)"
G_UZIANS = "The Uzians"
G_IHINS = "The I'hins (the sacred little people)"
G_IHUANS = "The I'huans"
G_DRUKS = "The Druks"
G_GHANS = "The Ghans"
G_ASUANS = "The Asu (Asuans, the first race)"
G_CONFEDERACY = "The Confederacy of the Holy Ghost (the Triunes)"

# Locations
L_PAN = "Pan (Whaga, the submerged continent)"
L_JAFFETH = "Jaffeth (China)"
L_VINDYU = "Vind'yu (India)"
L_ARABINYA = "Arabin'ya (Arabia and Egypt)"
L_GUATAMA = "Guatama (America)"
L_HORED = "Hored (the first heaven of the earth)"

# Periods
PER_KOSMON = "The Kosmon Era"
PER_DAN = "The Cycles of Dan and Dan'ha"
PER_ARCBON = "The Arc of Bon (cycle of the lawgivers)"

# Events
E_GENESIS = "The Cohabitation of Angels and Asu (origin of immortal man)"
E_PAN = "The Submersion of the Continent of Pan (the Flood)"
E_DEYUS = "Anuhasaj Proclaims Himself De'yus (the first false Godhead)"
E_CONFED = "The Founding of the Confederacy of the Holy Ghost"
E_CHRIST = "Looeamong Takes the Name Christ and Founds Christianity"
E_KOSMON = "The Kosmon Revelation (the writing of Oahspe)"

# Concepts
C_JEHOVIH = "Jehovih (the Great Spirit, E-O-Ih)"
C_THREEWORLDS = "The Three Worlds: Corpor, Atmospherea, and Etherea"
C_ES = "Es and Corpor (the seen and the unseen)"
C_VORTEXYA = "Vortexya and Vortexan Cosmogony"
C_ANTIPHYSICS = "The Denial of Gravitation and Solar Light and Heat"
C_SEMU = "Se'mu and the Spontaneous Origin of Life"
C_SPECIAL = "Special Creation of Species (the rejection of transmutation)"
C_RACES = "The Races of Man: Asu, I'hin, Druk, I'huan, and Ghan"
C_TREEOFLIFE = "The Tree of Life and the Origin of Immortal Man"
C_RESURRECTIONS = "The Three Resurrections and the Grades of Ascent"
C_HIERARCHY = "God, Lords, and the Hierarchy of Heaven"
C_FALSEGODS = "False Gods and Self-Godhood"
C_BEAST = "The Beast (Self) and Its Four Heads"
C_INSPIRATION = "The Doctrine of Inspiration (Oahspe)"
C_SUIS = "Su'is and Sar'gis (clairvoyance and materialization)"
C_LOOIS = "The Loo'is and the Breeding of Prophets"
C_NOSALVATION = "The Rejection of Vicarious Salvation"
C_ETHICS = "Faithist Ethics: Vegetarianism and Non-Resistance"
C_PROPHECY = "The Tables of Prophecy (the prophetic numbers)"
C_DRUJAS = "Drujas, Fetals, and the Bondage of Hells"
C_ASHARS = "Ashars and Asaphs (guardian angels and receivers of the dead)"
C_HARVEST = "Brides and Bridegrooms (the harvests of resurrection)"
C_SHIPS = "The Etherean Ships of Fire"
C_PANIC = "The Panic Language and the First Speech"
C_RITES = "Faithist Rites and the Degrees of Initiation"
C_REVELATION = "Oahspe's Mode of Revelation"
C_ANTIREINCARNATION = "The Rejection of Reincarnation"
C_LIGHT = "The All Light and the I AM"

# Claims
CL_PANTHEISM = "Jehovih Is the Whole; All Things Are His Person"
CL_VORTEX = "The Earth Floats in a Vortex and There Is No Gravitation"
CL_NOSUNHEAT = "Heat and Light Do Not Come From the Sun"
CL_NOLIGHTTRAVEL = "There Is No Substance or Travel of Light"
CL_SEMU = "Life Arises Without Seed From Se'mu by Jehovih's Presence"
CL_SPECIAL = "Each Species Was Created Separately and None Came From Another"
CL_ASU = "Immortal Man Arose When Angels Cohabited With the First Race Asu"
CL_PAN = "The Continent of Pan Was Sunk Beneath the Ocean in a Great Flood"
CL_DANHA = "Every Three Thousand Years the Earth Enters Etherean Light and a New Cycle"
CL_GODNOTCREATOR = "God and Lord Are Titles of Exalted Mortals, Not the Creator"
CL_FOURFALSE = "The World's Four Great Religions Were Founded by False Gods"
CL_CHRIST = "Christ Was a False God and the Gospels Were Compiled Under Constantine"
CL_NOSALVATION = "There Is No Vicarious Salvation; Resurrection Comes Only by Good Works"
CL_IDOLATRY = "To Worship Any Named God or Savior Is Idolatry Against Jehovih"
CL_SATAN = "Self Is the Satan That Is the Origin of All False Gods"
CL_INSPIRATION = "Man Originates No Thought; All Knowledge Is Inspiration From Jehovih"
CL_TWOKINDS = "Mankind Divides Into Faithists and Uzians"
CL_VEG = "The Chosen Must Be Vegetarian, Non-Resistant, and Abjure War"
CL_SPIRITS = "In the Kosmon Era the Dead Commune With Mortals Face to Face"
CL_CONSULT = "Consulting Angels for Earthly Gain Delivers One to Lying Spirits"
CL_NOREINCARNATION = "No Spirit Re-Enters a Womb to Be Born Again"
CL_LOOIS = "Angels Breed Up Prophets Through Six Generations of Mortals"
CL_RESURRECTIONS = "Spiritual Ascent Proceeds Through Three Resurrections"
CL_HELLS = "The Heavens of the Earth Can Become Hells of Bound Spirits"
CL_WORLDLIFE = "Worlds Are Born, Mature, and Die Like Living Creatures"
CL_SIMUL = "The Kosmon Revelation Was Given Simultaneously to Many"
CL_EOIH = "The Creator's Name E-O-Ih Was Taken From the Sound of the Wind"
CL_AJI = "Nebulous Darkness A'ji Descending on Earth Drives Men to War"
CL_ETHE = "Etherea Is Made of Ethe, the Solvent of All Corporeal Substance"
CL_PURPOSE = "Oahspe Aims to Teach Mortals to Hear the Creator and See the Heavens While Living"
CL_AMERICA = "Kosmon Was Revealed in a Land Free of Enforced Gods and Saviors"


# ---- Builders --------------------------------------------------------------

def write_page(slug_dir: str, slug: str, content: str):
    path = WIKI / slug_dir / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return path


def related(items):
    return "\n".join(f"- [[{r}]]" for r in items)


def ylist(items):
    return "[" + ", ".join(f'"{i}"' for i in items) + "]"


def source_page():
    body = f"""---
title: "{SRC_TITLE}"
type: source
source_type: primary_scripture
author_or_origin:
  - John Ballou Newbrough
  - "Angel Embassadors of Jehovih (claimed)"
date_composed: "Kosmon era (text dates itself c. 33 years into the Spiritualist era, i.e. c. 1881); first published 1882. This e-book: 2021 OK Publishing reprint."
language_original: English
last_updated: {TODAY}
tags: [source, type/revealed-scripture, topic/oahspe]
---

## Source Description

*Oahspe* is a 19th-century revealed scripture attributed on the title page to
**[[{P_NEWBROUGH}]]**. Internally it presents itself as written not by a man but
by "the Embassadors of the angel hosts of heaven," who "prepared and revealed
unto man in the name of Jehovih, His heavenly kingdoms" in "the thirty-third
year" of a new dispensation it calls the **kosmon era**. The book repeatedly
calls itself "this Bible" ("AS IN OTHER BIBLES IT IS REVEALED THAT THE WORLD WAS
CREATED, SO IN THIS BIBLE IT IS REVEALED HOW THE CREATOR CREATED IT"). The name
*Oahspe* is glossed as meaning earth (corpor), sky (atmospherea), and spirit
(etherea) — "because it relates to earth, sky and spirit."

The work comprises a Preface (a "General Statement of the Contents," a Glossary
of coined words, a "List of the Principal Prophets and Law-Givers," and "Hints
to the Reader") followed by ~33 "Books," from the cosmogonic **Book of Jehovih**
through long narrative histories of the earth's heavens (Aph, Sue, Apollo, Thor,
Osiris, Fragapatti, Cpenta-armij, Lika, Wars Against Jehovih, the Arc of Bon,
Eskra, Es) to the explicitly doctrinal books (Cosmogony and Prophecy, Judgment,
Inspiration, Discipline) and the practical program (Jehovih's Kingdom on Earth /
Shalam). It uses a coined cosmological vocabulary (corpor, es, ethe, vortexya,
se'mu, dan, drujas, I'hin) and dates events in years **B.K.** ("Before Kosmon").

## What the Source Contributes

- The theology: [[{C_JEHOVIH}]], [[{C_LIGHT}]], [[{C_INSPIRATION}]]
- The cosmology: [[{C_THREEWORLDS}]], [[{C_ES}]], [[{C_VORTEXYA}]], [[{C_ANTIPHYSICS}]], [[{C_SEMU}]]
- The anthropology: [[{C_RACES}]], [[{C_TREEOFLIFE}]], [[{C_SPECIAL}]]
- The pantheon and its corruption: [[{C_HIERARCHY}]], [[{C_FALSEGODS}]], [[{C_BEAST}]], [[{G_CONFEDERACY}]]
- The afterlife system: [[{C_RESURRECTIONS}]], [[{C_DRUJAS}]], [[{C_ASHARS}]], [[{C_HARVEST}]], [[{C_ANTIREINCARNATION}]]
- The prophetic system: [[{PER_DAN}]], [[{C_PROPHECY}]]
- The mediumship and prophet-breeding doctrines: [[{C_SUIS}]], [[{C_LOOIS}]]
- The ethics and program: [[{C_NOSALVATION}]], [[{C_ETHICS}]], [[{C_RITES}]], [[{PER_KOSMON}]]
- The mode of its own production: [[{C_REVELATION}]]

## Book-by-Book Structure (as summarized in the Preface)

- **Book of Jehovih** — "a general idea of the creation of man... and of the
  inorganic habitation of the earth." Vortexan cosmogony; the three worlds; se'mu.
- **Books of Sethantes, Ah'shong, Aph, Sue, Apollo, Thor, Osiris, Fragapatti,
  Cpenta-armij, Lika** — the "organic" history of the earth and its heavens,
  cycle by cycle, from ~78,000 years ago down to ~3,400 B.K. **Book of Aph**
  recounts [[{E_PAN}]].
- **Book of Wars Against Jehovih** — the rise of the self-made false God
  [[{P_ANUHASAJ}]] (De'yus) and his confederate Lords. "Books of Eskra and Es
  bring the history down to Kosmon" — the four false Gods who founded the
  modern world religions ([[{G_CONFEDERACY}]]).
- **Book of the Arc of Bon** — "a history of Capilya, Moses and Chine," the
  lawgivers ([[{PER_ARCBON}]]).
- **Book of Cosmogony and Prophecy** — "the manner in which worlds are made...
  showing how Light and Heat, Magnetism and Electricity are manufactured, being
  wholly at variance with the present Systems of Philosophy and Astronomy."
- **Book of Saphah** — "the formation of languages, and of rites and ceremonies."
- **Books of Ben, Judgment, Inspiration and Discipline** — "are doctrinal."
- **Book of Jehovih's Kingdom on Earth / Book of Shalam** — "the condition of
  things soon to come upon the earth"; the Faithist colony program.

## Key Claims Extracted

- [[{CL_PANTHEISM}]]
- [[{CL_EOIH}]]
- [[{CL_VORTEX}]]
- [[{CL_NOSUNHEAT}]]
- [[{CL_NOLIGHTTRAVEL}]]
- [[{CL_ETHE}]]
- [[{CL_SEMU}]]
- [[{CL_SPECIAL}]]
- [[{CL_WORLDLIFE}]]
- [[{CL_ASU}]]
- [[{CL_PAN}]]
- [[{CL_DANHA}]]
- [[{CL_AJI}]]
- [[{CL_GODNOTCREATOR}]]
- [[{CL_SATAN}]]
- [[{CL_FOURFALSE}]]
- [[{CL_CHRIST}]]
- [[{CL_NOSALVATION}]]
- [[{CL_IDOLATRY}]]
- [[{CL_INSPIRATION}]]
- [[{CL_TWOKINDS}]]
- [[{CL_VEG}]]
- [[{CL_SPIRITS}]]
- [[{CL_CONSULT}]]
- [[{CL_NOREINCARNATION}]]
- [[{CL_LOOIS}]]
- [[{CL_RESURRECTIONS}]]
- [[{CL_HELLS}]]
- [[{CL_SIMUL}]]
- [[{CL_PURPOSE}]]
- [[{CL_AMERICA}]]

## Internal Tensions or Multiple Accounts

The book states of itself: **"Not immaculate in this Book, OAHSPE"** — i.e. it
does not claim inerrancy, its stated aim being to teach mortals "HOW TO ATTAIN
TO HEAR THE CREATOR'S VOICE." It distinguishes sharply between **God** (an
exalted mortal ruling for a season) and **Jehovih** (the Creator) and warns that
both true and false angels speak to mortals, so that revelations must be judged
"on the merit only of wisdom and truth," not by the names professed. The
provided e-book also contains a duplicated chapter (Book of Jehovih ch. VIII
appears twice) — a formatting artifact of the reprint, not a doctrinal variant.
"""
    write_page("sources", "oahspe-newbrough-1882", body)


# ---- Persons ---------------------------------------------------------------

def person(slug, title, roles, body, rel, aka=None, extra_tags=None):
    aka_yaml = ylist(aka) if aka else "[]"
    roles_yaml = "\n".join(f'  - "{r}"' for r in roles)
    tags = ["person", f"topic/{TOPIC}"] + (extra_tags or [])
    content = f"""---
title: "{title}"
type: person
also_known_as: {aka_yaml}
roles:
{roles_yaml}
textual_sources:
  - "{SRC}"
last_updated: {TODAY}
tags: {tags}
---

{body.strip()}

## Related Entities

- {SRC}
{related(rel)}
"""
    write_page("persons", slug, content)


def persons():
    person("john-ballou-newbrough", P_NEWBROUGH,
           ["named author / scribe of Oahspe", "claimed mortal instrument of the angel embassadors"],
           f"""
## Biographical Details from Source

John Ballou Newbrough is the name on the title page of {SRC}. The text itself
makes no biographical claims about him; it presents its true authors as **"the
Embassadors of the angel hosts of heaven"** who "revealed unto man in the name
of Jehovih, His heavenly kingdoms" in "the thirty-third year" of the kosmon era.
The book is therefore framed as transcribed revelation rather than personal
authorship, and disclaims inerrancy: **"Not immaculate in this Book, OAHSPE."**
Its stated purpose is "to teach mortals HOW TO ATTAIN TO HEAR THE CREATOR'S
VOICE, and to SEE HIS HEAVENS, in full consciousness, whilst still living."
""",
           [C_REVELATION, E_KOSMON, PER_KOSMON],
           extra_tags=["role/scribe"])

    person("anuhasaj-deyus", P_ANUHASAJ,
           ["one-time sub-God", "self-proclaimed Lord God / De'yus", "first false Godhead of the earth"],
           f"""
## Biographical Details from Source

Anuhasaj is the central villain of the **Book of Wars Against Jehovih**: a
one-time sub-God who, counseled by **Satan (self)**, rose through "hundreds of
years" of feigned humility to be crowned **Lord God**, "the first rank below
God." He then declared himself the Creator under the name **De'yus** (glossed as
"Dyaus, Deity," and linked to Zeus, Joss, Ho'Joss), re-established the false
heaven **[[{L_HORED}]]** as "the All Highest Place," and made **Anubi** his "Son
and Savior of Men." The Preface names him "The False Lord God... who first made
the names Lord, God, Lord God, De'yus... worshipful on the earth in place of the
Great Spirit." He is the archetype of [[{C_FALSEGODS}]] and is eventually cast
into hell.
""",
           [E_DEYUS, C_FALSEGODS, C_HIERARCHY, C_BEAST, CL_SATAN, CL_GODNOTCREATOR],
           aka=["De'yus", "Dyaus", "the false Lord God"],
           extra_tags=["category/false-god"])

    person("looeamong-false-christ", P_LOOEAMONG,
           ["false God", "self-styled Christ", "founder of Christianity (per Oahspe)"],
           f"""
## Biographical Details from Source

Looeamong is one of the four "Triunes" of the **[[{G_CONFEDERACY}]]**, each of
whom "took the title, SON OF THE HOLY GHOST." Forty years after the death of
[[{P_JOSHU}]], "a false God, Looeamong, with millions of angel emissaries,
obsessed the inhabitants of all those countries and plunged them into war."
"Looeamong, the false God, now changed his name and falsely called himself
Christ, which is the Ahamic word for knowledge. And he raised up tribes of
mortal warriors, who called themselves Christians, who are warriors to this
day." He declared "I come not to bring peace, but war!" and warred on Baal,
Ashtaroth, and his fellow false Gods, before being "finally cast into hell...
which corresponds in date to the time the pope established himself as
vicegerent." His mortal warrior-servant was [[{P_THOTH}]].
""",
           [E_CHRIST, E_CONFED, G_CONFEDERACY, C_FALSEGODS, CL_CHRIST, CL_FOURFALSE, P_JOSHU],
           aka=["Kriste", "Christ (the false God)"],
           extra_tags=["category/false-god"])

    person("kabalactes-false-buddha", P_KABALACTES,
           ["false God", "founder of modern Buddhism (per Oahspe)"],
           f"""
## Biographical Details from Source

Kabalactes is the Triune of the **[[{G_CONFEDERACY}]]** who "by inspiration,
founded what is now called Buddhism," ruling the heavenly capital Horactu over
**[[{L_VINDYU}]]** (India). Oahspe distinguishes him sharply from the historical
sage [[{P_SAKAYA}]] (whom his followers wrongly called "Buddha" a thousand years
after death). "The terrible conflicts in the heavens of Kabalactes... were also
manifested on the mortals of Vind'yu." He "is finally cast into hell."
""",
           [E_CONFED, G_CONFEDERACY, C_FALSEGODS, CL_FOURFALSE, P_SAKAYA, L_VINDYU],
           aka=["the false Buddha"],
           extra_tags=["category/false-god"])

    person("ennochissa-false-brahma", P_ENNOCHISSA,
           ["false God", "founder of modern Brahmanism (per Oahspe)"],
           f"""
## Biographical Details from Source

Ennochissa is the Triune of the **[[{G_CONFEDERACY}]]** who "by inspiration,
founded modern Brahmanism," ruling the heavenly capital Eta-shong. Oahspe
distinguishes him from the ancient lawgiver [[{P_BRAHMA}]], who had taught the
one Great Spirit. With Kabalactes and Looeamong he "took the title, SON OF THE
HOLY GHOST," and "is finally cast into hell."
""",
           [E_CONFED, G_CONFEDERACY, C_FALSEGODS, CL_FOURFALSE, P_BRAHMA],
           aka=["the false Brahma"],
           extra_tags=["category/false-god"])

    person("thoth-gabriel", P_THOTH,
           ["false God / great warrior angel", "founder of Mohammedanism (per Oahspe)"],
           f"""
## Biographical Details from Source

Thoth (also called **Gabriel**) is named in the Preface as the false God who
"by inspiration, founded Mohammedanism," and who "also is cast into hell." He
served as the "great warrior servant" of [[{P_LOOEAMONG}]] and as captain of his
hosts, through whom Looeamong "overcame and cast into hell" the Goddess
Ashtaroth and the false God Baal. He is one of "The Four False Gods" of the
Preface, paired with the founders of Christianity, Buddhism, and Brahmanism.
""",
           [E_CONFED, G_CONFEDERACY, C_FALSEGODS, CL_FOURFALSE, P_LOOEAMONG],
           aka=["Gabriel", "the founder of Mohammedanism"],
           extra_tags=["category/false-god"])

    person("aph-son-of-jehovih", P_APH,
           ["etherean God ('Son of Jehovih')", "executor of the submersion of Pan"],
           f"""
## Biographical Details from Source

Aph, "Son of Jehovih, God in the arc of Noe," is the etherean God who carries
out [[{E_PAN}]] some 24,000 years before kosmon, after the earth's heavens had
filled with [[{C_DRUJAS}]]. At Jehovih's command he ringed the doomed continent
of [[{L_PAN}]] with "a wall of pillars of fire" and a net "a thousand miles"
high, then "the vortex of the earth closed in... and the land sank down beneath
the water, to rise no more," delivering billions of bound spirits on
"birth-blankets." His companion is Nin'ya, Daughter of Jehovih. The cycle/arc of
Aph is one of the great dan'ha markers in the prophetic system ([[{PER_DAN}]]).
""",
           [E_PAN, CL_PAN, L_PAN, C_DRUJAS, C_SHIPS, C_HARVEST],
           aka=["Aph, God in the arc of Noe"])

    person("zarathustra-zoroaster", P_ZARATHUSTRA,
           ["lawgiver / prophet of the one Great Spirit", "i-e-su"],
           f"""
## Biographical Details from Source

Zarathustra (Zoa-raaster, "erroneously called Zoroaster") is, per the Preface,
"a Persian lawgiver who lived in the cycle of Fragapatti, eight thousand nine
hundred years ago, the farthest back of all historical characters." He "was of
enormous size, and of neither sex, being an **i-e-su**." Oahspe asserts that
"both Buddhist and Christian religions are said to be made up chiefly from the
history and miracles of Zarathustra," and that to obliterate this history "did
Coatulus, a Christian priest, burn the Alexandrian Library in the year 390." In
the Books of God's Word and Divinity he is taught by the angel **I'hua'Mazda**.
""",
           [C_SUIS, PER_DAN, CL_FOURFALSE],
           aka=["Zoroaster", "Zoa-raaster", "the All Pure"])

    person("moses-oahspe", P_MOSES,
           ["Egyptian lawgiver and leader-forth of the Faithists", "su'is / i-e-su"],
           f"""
## Biographical Details from Source

Moses, in the **Book of the Arc of Bon**, is "an Egyptian lawgiver...
cotemporaneous with Capilya of India, and Chine of China, living two thousand
four hundred years after Abram (3400 B.K.)." He was "a large man, a pure I'huan,
copper coloured, and of great strength," foster-son of Pharaoh. He "rebuilt what
had been lost since Abram's time," teaching "the Zarathustrian doctrine of one
Great Spirit, Whom they worshipped secretly under the Name Jehovih," while in
public, to avoid persecution, calling Him God or Lord. He led the Faithists
(Iz'zerlites) out of Egypt under the direction of "the angels of Jehovih."
""",
           [PER_ARCBON, P_CAPILYA, P_CHINE, C_LOOIS, G_FAITHISTS, P_ABRAM],
           aka=["the Egyptian lawgiver"])

    person("capilya", P_CAPILYA,
           ["Indian lawgiver and leader-forth of the Faithists", "natural-born i-e-su, su'is and sar'gis"],
           f"""
## Biographical Details from Source

Capilya, in the **Book of the Arc of Bon**, is "of India, an i-e-su, living
three thousand four hundred years ago in the cycle of Lika, a lawgiver who
restored the believers in one Great Spirit to hold property." He was "a
foster-child of the king of India," paralleling Moses. Bred up over generations
by the **loo'is** under the archangel Hirattax (see [[{C_LOOIS}]]), he was born
and secretly switched to the barren queen of the cruel king Yokovrana, and was
sprinkled with the blood of a lamb as **"Capilya, the Lamb of Heaven"** — ending
human sacrifice in Vind'yu. "In all things he was directed by the angels of
Jehovih (Ormazd)."
""",
           [PER_ARCBON, C_LOOIS, P_MOSES, P_CHINE, G_FAITHISTS, L_VINDYU, C_SUIS],
           aka=["the Lamb of Heaven"])

    person("chine", P_CHINE,
           ["Chinese lawgiver and founder of China", "i-e-su"],
           f"""
## Biographical Details from Source

Chine, in the **Book of the Arc of Bon**, is "a lawgiver cotemporaneous with
Capilya and Moses... an i-e-su, and like Moses... of copper colour and very
large, but his hair was red like a fox." He is "the founder of China" (Jaffeth)
who "restored the rights of the believers in Jehovih," establishing the doctrine
of the one Great Spirit "so firmly" that "all China to this day accepts it." The
land Jaffeth is said to be named after him. "Some of his miracles have never
been excelled."
""",
           [PER_ARCBON, P_MOSES, P_CAPILYA, G_FAITHISTS, L_JAFFETH],
           aka=["founder of China"])

    person("abram-abraham", P_ABRAM,
           ["Persian lawgiver", "founder of the ancient Hebrews (Iz'zerlites)", "I'huan"],
           f"""
## Biographical Details from Source

Abram, "afterward called Abraham," is per the Preface "an I'huan, large and red,
like new copper," "a Persian, and the founder of the ancient Hebrews or
Iz'zerlites, and also the founder of migration for religion's sake. He took his
followers into Egupt (Egypt)." He lived in the cycle of Cpenta-armij (~5,800
years ago), one of the four mortals (with Po, Brahma, and Ea-wah-tah) with whom
"four etherean Gods... walking with four mortals" re-established the worship of
the Great Spirit, under the name **Jehovih** in Arabin'ya.
""",
           [G_FAITHISTS, C_RACES, P_BRAHMA, P_PO, P_EAWAHTAH, P_MOSES, L_ARABINYA],
           aka=["Abraham", "founder of the Iz'zerlites"])

    person("brahma-oahspe", P_BRAHMA,
           ["East Indian lawgiver of the one Great Spirit"],
           f"""
## Biographical Details from Source

Brahma is "an East Indian lawgiver, cotemporaneous with Po and Abram... a large
man of great strength, and ranked the highest spiritually of all mortals. He
re-established the Zarathustrian religion in India." His wife was **Yu-tiv**,
"fairest of women." Oahspe distinguishes this true lawgiver, who taught the one
Great Spirit, from the later false God [[{P_ENNOCHISSA}]] who founded the
idolatrous "Brahmanism."
""",
           [P_ABRAM, P_PO, P_EAWAHTAH, P_ENNOCHISSA, L_VINDYU],
           aka=["the East Indian lawgiver"])

    person("po", P_PO,
           ["lawgiver of Jaffeth (China)", "i-e-su"],
           f"""
## Biographical Details from Source

Po, "of Jaffeth (afterward called China), was also an i-e-su. He was a lawgiver
cotemporaneous with Abram of Persia, living about five thousand eight hundred
years ago, and in the cycle of Cpenta-armij. He also taught, like Zarathustra,
the doctrine of one Great Spirit, which doctrine he re-established in Jaffeth
(China)." He is one of the four mortals through whom etherean Gods worked in the
cycle of Cpenta-armij.
""",
           [P_ABRAM, P_BRAHMA, P_EAWAHTAH, L_JAFFETH, P_ZARATHUSTRA])

    person("ea-wah-tah", P_EAWAHTAH,
           ["North American lawgiver", "founder of the Algonquin confederation"],
           f"""
## Biographical Details from Source

Ea-wah-tah is "a North American, cotemporaneous with Po, Abram, and Brahma...
taller than any other man, with a bright shining face of copper. He established
amongst the North Americans of his time the worship of the Great Spirit, and his
doctrines are still held by most of the tribes of North American Indians, who
refuse to accept any other God or Saviour." Oahspe credits him with founding "the
United States of America, but called by the name O-pah-e-go-quim or Algonquin" —
a confederation of "independent nations, united in one" said to be the model "for
the formation of the present United States of America by the whites."
""",
           [P_PO, P_ABRAM, P_BRAHMA, L_GUATAMA],
           aka=["Hiawatha (cf.)"])

    person("sakaya-buddha", P_SAKAYA,
           ["East Indian lawgiver of sub-cycle rank", "i-e-su"],
           f"""
## Biographical Details from Source

Sakaya, "sometimes erroneously called Buddha," lived "about twenty-five hundred
years ago... an East Indian by birth, holding to the doctrine of one Great
Spirit only." "The term Buddha was wrongly attached to him by his followers
something over a thousand years after his death." He "made no account of God or
Lord worship" and "taught that man's highest attainment was to live for sake of
others, and not for one's self," establishing "convents, nunneries, and
monasteries." Oahspe distinguishes him from the false God [[{P_KABALACTES}]].
""",
           [P_KABALACTES, P_KAYU, P_JOSHU, C_NOSALVATION],
           aka=["the historical Buddha", "Sakaya"])

    person("kayu-confucius", P_KAYU,
           ["Chinese lawgiver of sub-cycle rank", "i-e-su"],
           f"""
## Biographical Details from Source

Ka'yu, "erroneously called Confucius... a lawgiver of sub-cycle rank, of China,
living twenty-five hundred years ago," is called "one of the most learned men
that ever lived," with "more followers than any other lawgiver on earth, being
over three hundred million people." "He taught the doctrine of one Great Spirit,
and to worship Him only," and "abridged eighteen thousand books of the
ancients." The Book of Judgment cites Ka'yu as an example of one through whom "an
angel speaking" worked though he believed it himself.
""",
           [P_SAKAYA, P_JOSHU, C_INSPIRATION],
           aka=["Confucius"])

    person("joshu", P_JOSHU,
           ["Jewish lawgiver of sub-cycle rank", "i-e-su", "the historical Jesus (per Oahspe)"],
           f"""
## Biographical Details from Source

Joshu is, per the Preface, "of Jewish birth, and also an i-e-su, born near
Jerusalem, something less than two thousand years ago. His predecessors were of
the tribe called Esseneans, or non-resistants. He laboured to bring the Jews
back to their pristine purity. He was a severe preacher, denounced by the people
as a blasphemer, and was stoned to death in Jerusalem. He also taught the
doctrine of one Great Spirit only." Oahspe presents Joshu as the real human
teacher who is sharply distinguished from the false God [[{P_LOOEAMONG}]]
("Christ"): "the so-called Sermon on the Mount is a plagiarism on Joshu's
teachings, gotten up by the Ecumenical Council under the direction of the Emperor
Constantine."
""",
           [P_LOOEAMONG, E_CHRIST, CL_CHRIST, P_SAKAYA, P_KAYU],
           aka=["the historical Jesus", "Joshu the Essenean"])

    person("thothma-pyramid", P_THOTHMA,
           ["Egyptian adept and king", "builder of the great pyramid (per Oahspe)"],
           f"""
## Biographical Details from Source

Thothma (Hojax) is "the builder of the great pyramid in Egypt, and one of the
greatest adepts that ever lived. He could hear the Gods and talk with them
understandingly, and could cast himself in the death trance and go spiritually
into the lower heavens and return at will. He was under the inspiration of the
false God Osiris." He "laboured to establish immortality in the flesh" — to make
the body incorruptible — "but... he died on the day he was one hundred years
old." He exemplifies high [[{C_SUIS}]] turned to the service of a false God.
""",
           [C_SUIS, C_FALSEGODS, L_ARABINYA],
           aka=["Hojax"])

    person("tae", P_TAE,
           ["the representative man of the kosmon era", "founder of the Faithist colony Shalam"],
           f"""
## Biographical Details from Source

"Tae" is the name Oahspe gives to the representative or symbolic man of the
kosmon era — "because he was a representative man, the people named him, Tae" —
and also to the whole human race when Jehovih addresses it. In the **Book of
Jehovih's Kingdom on Earth / Book of Shalam**, Tae comes "out of Uz," gathers
"orphan babes and castaway infants and foundlings" the world rejected, and (with
a woman named **Es**) founds the communal colony **Shalam** with fifty Faithists
who will "give up self" — the practical beginning of "the Father's kingdom on
earth." He rejects the capital-labor reformers, eugenicists, and rival-religion
priests who offer themselves, accepting only those of faith willing to serve
helpless children "without money and without price."
""",
           [E_KOSMON, PER_KOSMON, G_FAITHISTS, C_ETHICS, C_NOSALVATION],
           aka=["the representative man", "founder of Shalam"])


# ---- Groups ----------------------------------------------------------------

def group(slug, title, category, body, rel, aka=None, periods_active=None,
          roles_sig=None, extra_tags=None):
    tags = ["group", f"topic/{TOPIC}"] + (extra_tags or [])
    content = f"""---
title: "{title}"
type: group
category: {category}
also_known_as: {ylist(aka) if aka else "[]"}
periods_active: {ylist(periods_active) if periods_active else "[]"}
textual_sources:
  - "{SRC}"
roles_significance: {ylist(roles_sig) if roles_sig else "[]"}
last_updated: {TODAY}
tags: {tags}
---

{body.strip()}

## Related Entities

- {SRC}
{related(rel)}
"""
    write_page("groups", slug, content)


def groups():
    group("faithists-oahspe", G_FAITHISTS, "religious_party",
          f"""
## Identity and Nomenclature

The Faithists are Oahspe's "chosen" — "to as many as separate themselves from the
dominion of the Beast, making these covenants unto Me... shall they be known...
as Mine, and shall be called **FAITHISTS**." They are the worshippers of the
Great Spirit [[{C_JEHOVIH}]] under His many names across the ages (Vede, Parsi'e,
Iz'zerlites, etc.), recurring "in all ages of the world." They are contrasted at
every turn with [[{G_UZIANS}]].

## Doctrine and Practice from Source

Faithists hold all things in common, "having no leaders, only their Creator,"
practice non-resistance, abjure war "even... submitting to death rather than take
part therein," eat no fish or flesh, keep the seventh day, and "go themselves
about gathering up sinners, and the poor and helpless and orphans." Their
higher-law status exempts them from the lower heavens: "the believers go to God,
but the unbelievers go to his Lords." Their kosmon-era embodiment is the colony
**Shalam** founded by [[{P_TAE}]] (see [[{C_ETHICS}]], [[{C_RITES}]]).
""",
          [G_UZIANS, C_ETHICS, C_NOSALVATION, C_RITES, CL_TWOKINDS, CL_VEG, P_TAE],
          aka=["the chosen", "worshippers of Jehovih"],
          roles_sig=["the righteous remnant in every age", "builders of Jehovih's kingdom on earth"],
          extra_tags=["category/religious-movement"])

    group("uzians", G_UZIANS, "ideological_movement",
          f"""
## Identity and Nomenclature

The Uzians are the counter-class to the Faithists: "to as many as will not make
these covenants, have I given the numbers of the Beast, and they shall be called
**UZIANS, signifying destroyers**. And these shall be henceforth the two kinds of
people on earth, Faithists and Uzians." "Uz" is also Oahspe's term for the
material/dissolving world and the "fourth dimension of corpor" (dissolution).
Uzians are the worldly, war-making, money-trusting people from among whom Tae
gathers the cast-off orphans to found [[{P_TAE}]]'s colony.
""",
          [G_FAITHISTS, C_BEAST, CL_TWOKINDS],
          aka=["the destroyers"],
          roles_sig=["the worldly / materialist majority"],
          extra_tags=["category/movement"])

    group("ihins", G_IHINS, "ethnic_group",
          f"""
## Identity and Nomenclature

The I'hins are the first sacred race — small, white and yellow, born of the
union of the angels (the "sons of Jehovih") with the first race [[{G_ASUANS}]]
(see [[{C_TREEOFLIFE}]]). They alone were "capable of everlasting life," could be
inspired by the angels, and were the builders and Faithists of the ancient
world. In [[{E_PAN}]] only "the remnants of I'hins" remained worth saving, and
they were carried in ships to the four divisions of the earth to seed the chosen
in every land. They are the foundational race in Oahspe's anthropology
([[{C_RACES}]]).
""",
          [C_RACES, C_TREEOFLIFE, G_ASUANS, G_IHUANS, G_DRUKS, E_PAN, CL_ASU],
          aka=["the sacred little people", "the chosen race"],
          roles_sig=["first immortal race", "builders and Faithists of antiquity"],
          extra_tags=["category/race"])

    group("ihuans", G_IHUANS, "ethnic_group",
          f"""
## Identity and Nomenclature

The I'huans are the copper-colored, "large and red" race born of the union of
the [[{G_IHINS}]] with the darker [[{G_DRUKS}]]. They are the warrior race from
whom many of Oahspe's lawgivers sprang — [[{P_ABRAM}]] ("an I'huan, large and
red, like new copper") and [[{P_MOSES}]] ("a pure I'huan, copper coloured") are
named as I'huans. They mark a middle grade between the sacred I'hins and the
fallen Druks ([[{C_RACES}]]).
""",
          [C_RACES, G_IHINS, G_DRUKS, G_GHANS, P_ABRAM, P_MOSES],
          aka=["the copper-colored race"],
          roles_sig=["warrior race", "stock of several lawgivers"],
          extra_tags=["category/race"])

    group("druks", G_DRUKS, "ethnic_group",
          f"""
## Identity and Nomenclature

The Druks are the dark, fallen race produced when the sacred I'hins or their
descendants cohabited "with the asuans," bringing forth "heirs in the descending
grade of life" — those who "shall go out in darkness." They are the carnivorous,
war-prone people associated with the Beast and with darkness in Oahspe's racial
hierarchy ([[{C_RACES}]]). The term "Druk" also stands for the lowest mortal
grade in the prophetic tables.
""",
          [C_RACES, G_IHINS, G_IHUANS, G_ASUANS, C_BEAST],
          aka=["the dark race"],
          roles_sig=["fallen / carnivorous race"],
          extra_tags=["category/race"])

    group("ghans", G_GHANS, "ethnic_group",
          f"""
## Identity and Nomenclature

The Ghans are the highest mortal race in Oahspe's anthropology, born of the
mingling of [[{G_IHUANS}]] with [[{G_IHINS}]] — "to reach the fourth grade will
require five generations, which shall spring from the I'hin race commingling with
the I'huans." They are the most capable race, the stock from which prophets and
the higher grades of mortals arise as the cycles advance ([[{C_RACES}]]).
""",
          [C_RACES, G_IHINS, G_IHUANS, C_LOOIS],
          aka=["the fourth-grade race"],
          roles_sig=["highest mortal race"],
          extra_tags=["category/race"])

    group("asu-asuans", G_ASUANS, "ethnic_group",
          f"""
## Identity and Nomenclature

The Asu (Asuans), called **Adam** in Oahspe, are the first race of man — made
"out of se'mu" by Jehovih's presence, "but as a tree, but dwelling in ha'k"
(darkness). They were soulless and mortal, "not capable of everlasting life";
"as the corporeal earth passeth away, so shall pass away the first race Asu." The
immortal races arose only when the descended angels cohabited with them (see
[[{C_TREEOFLIFE}]], [[{E_GENESIS}]]). They are the bottom of Oahspe's racial
sequence ([[{C_RACES}]]).
""",
          [C_RACES, C_TREEOFLIFE, E_GENESIS, C_SEMU, G_IHINS, CL_ASU],
          aka=["Asu", "Adam (Oahspe)", "the first race"],
          roles_sig=["first, soulless race of man"],
          extra_tags=["category/race"])

    group("confederacy-holy-ghost", G_CONFEDERACY, "religious_party",
          f"""
## Identity and Nomenclature

The Confederacy of the Holy Ghost is the alliance of false Gods who, per the
**Book of Eskra**, founded the modern world religions. "They resolved to organize
each one of these three places with a distinct head, and to unite the three heads
as one confederacy... Thus was founded the CONFEDERACY OF THE HOLY GHOST." Its
three "Triunes" — [[{P_KABALACTES}]] (Buddhism), [[{P_ENNOCHISSA}]]
(Brahmanism), and [[{P_LOOEAMONG}]] (Christianity) — "each... took the title, SON
OF THE HOLY GHOST," and Oahspe presents them as the literal origin of the
doctrine of the Trinity / Father, Son, and Holy Ghost. With [[{P_THOTH}]]
(Mohammedanism) they make up "The Four False Gods" of the Preface, all "finally
cast into hell."
""",
          [E_CONFED, P_LOOEAMONG, P_KABALACTES, P_ENNOCHISSA, P_THOTH, C_FALSEGODS, CL_FOURFALSE],
          aka=["the Triunes", "the founders of the Trinity"],
          roles_sig=["false-God alliance that founded the world religions"],
          extra_tags=["category/false-gods"])


# ---- Locations -------------------------------------------------------------

def location(slug, title, body, rel, aka=None, modern_geo="", peoples=None):
    peoples_yaml = ylist([f"[[{p}]]" for p in peoples]) if peoples else "[]"
    content = f"""---
title: "{title}"
type: location
also_known_as: {ylist(aka) if aka else "[]"}
periods_inhabited: []
modern_geography: "{modern_geo}"
associated_peoples: {peoples_yaml}
last_updated: {TODAY}
tags: [location, topic/oahspe]
---

{body.strip()}

## Related Entities

- {SRC}
{related(rel)}
"""
    write_page("locations", slug, content)


def locations():
    location("pan-whaga", L_PAN,
             f"""
## Geographical and Historical Context from Source

Pan — originally **Whaga**, "afterward called Pan, signifying earth" — is the
first great continent of man in Oahspe, the site of the first heavenly kingdom
[[{L_HORED}]] and the home of the I'hins. It was "cut loose from its fastenings"
and "sank down beneath the water, to rise no more" in [[{E_PAN}]], ~24,000 years
before kosmon, when the earth's vortex "closed in." The land lay in the Pacific
(its survivors were carried east and west to Jaffeth, Vind'yu, Arabin'ya, Shem,
Ham, and Guatama). Oahspe promises that "in the kosmon era... mortals" will
"discover the sunken land of Whaga."

## Textual Appearances

Setting of the Books of Sethantes through Aph; the original land of the Panic
language ([[{C_PANIC}]]).
""",
             [E_PAN, CL_PAN, L_HORED, G_IHINS, C_PANIC, P_APH],
             aka=["Whaga", "the sunken continent"],
             modern_geo="A continent in the Pacific, said by the source to have sunk beneath the ocean",
             peoples=[G_IHINS, G_ASUANS])

    location("jaffeth-china", L_JAFFETH,
             f"""
## Geographical and Historical Context from Source

Jaffeth is Oahspe's name for **China**, one of the great divisions of the earth
peopled by survivors of [[{L_PAN}]]. It is the land of the lawgivers [[{P_PO}]]
and [[{P_CHINE}]] (after whom it is said to be named) and of [[{P_KAYU}]]
(Confucius). In the cycle of the false Gods it fell under [[{P_KABALACTES}]] and
the name **Te-in** was given for the Great Spirit there.

## Textual Appearances

Recurs throughout the histories as one of the four/five divisions of the earth.
""",
             [P_PO, P_CHINE, P_KAYU, L_PAN, L_VINDYU, L_ARABINYA, L_GUATAMA],
             aka=["China"],
             modern_geo="China",
             peoples=[G_IHINS, G_IHUANS])

    location("vindyu-india", L_VINDYU,
             f"""
## Geographical and Historical Context from Source

Vind'yu is Oahspe's name for **India** (also called Shem), land of the lawgivers
[[{P_BRAHMA}]] and [[{P_CAPILYA}]] and of the sage [[{P_SAKAYA}]]. There the
Great Spirit was worshipped under the name **Ormazd**. In the cycle of the false
Gods it fell under [[{P_KABALACTES}]] ("Buddhism") and earlier under the idolatry
of Dyaus, whose king Yokovrana practiced human sacrifice until Capilya ended it.

## Textual Appearances

Setting of much of the Book of the Arc of Bon (History of Capilya).
""",
             [P_BRAHMA, P_CAPILYA, P_SAKAYA, P_KABALACTES, L_JAFFETH, L_ARABINYA],
             aka=["India", "Shem"],
             modern_geo="India",
             peoples=[G_IHUANS, G_FAITHISTS])

    location("arabinya", L_ARABINYA,
             f"""
## Geographical and Historical Context from Source

Arabin'ya is Oahspe's name for the region of **Arabia and Egypt** (Egupt), land
of [[{P_ABRAM}]] (Abraham), [[{P_MOSES}]], and the pyramid-builder
[[{P_THOTHMA}]]. There the Faithists worshipped the Great Spirit secretly under
the name **Jehovih** while publicly saying God or Lord to avoid persecution. It
is the home of the Iz'zerlites (ancient Hebrews) whom Abram founded and Moses led
forth.

## Textual Appearances

Setting of the Egyptian/Hebrew portions of the Arc of Bon and of the Osiris cycle.
""",
             [P_ABRAM, P_MOSES, P_THOTHMA, G_FAITHISTS, L_VINDYU, L_JAFFETH],
             aka=["Arabia", "Egupt (Egypt)"],
             modern_geo="Arabia and Egypt",
             peoples=[G_IHUANS, G_FAITHISTS])

    location("guatama-america", L_GUATAMA,
             f"""
## Geographical and Historical Context from Source

Guatama is Oahspe's name for **America**, one of the great divisions of the earth
settled from sunken [[{L_PAN}]]. It is the land of [[{P_EAWAHTAH}]], who
established the worship of the Great Spirit (under the name **Egoquim**) and the
"Algonquin" confederation. Oahspe presents America as the providentially prepared
land for the kosmon revelation — "this land untrammeled with Gods and Saviors and
Lords, enforced by the sword, so that My revelations... shall be published and
not suppressed" (see [[{CL_AMERICA}]]).

## Textual Appearances

Home of the Guatama cycles and of the kosmon-era founding of Shalam.
""",
             [P_EAWAHTAH, L_PAN, PER_KOSMON, CL_AMERICA, P_TAE],
             aka=["America"],
             modern_geo="The Americas (esp. North America)",
             peoples=[G_IHINS, G_FAITHISTS])

    location("hored", L_HORED,
             f"""
## Geographical and Historical Context from Source

Hored is "the first organic abiding place for the first God of this world" — the
first heavenly kingdom of [[{C_THREEWORLDS}]], established in [[{C_ASHARS}]]
atmospherea "over and above the mountains of Aotan... to the eastward of Ul, of
that country hereinafter called the continent of Pan." It held God's throne and
Council and governed the five Lords of the earth's divisions. The name later
recurs when the false God [[{P_ANUHASAJ}]] (De'yus) re-establishes a counterfeit
"Hored" as "the central kingdom of all the heavens" in his bid for self-Godhood.

## Textual Appearances

The seat of God in the Book of Jehovih and a contested name in the Book of Wars.
""",
             [C_THREEWORLDS, C_HIERARCHY, L_PAN, P_ANUHASAJ, E_DEYUS],
             aka=["the first heaven of the earth"],
             modern_geo="A heavenly plateau (atmospherea) over the former continent of Pan")


# ---- Periods ---------------------------------------------------------------

def period(slug, title, start_date, body, rel, end_date=None, extra_tags=None):
    tags = ["period", f"topic/{TOPIC}"] + (extra_tags or [])
    end_yaml = f'\nend_date: "{end_date}"' if end_date else ""
    content = f"""---
title: "{title}"
type: period
start_date: "{start_date}"{end_yaml}
last_updated: {TODAY}
tags: {tags}
---

{body.strip()}

## Related Entities

- {SRC}
{related(rel)}
"""
    write_page("periods", slug, content)


def periods():
    period("kosmon-era", PER_KOSMON,
           "1848 (year 1 of the Kosmon era; the text is dated c. 33 years later)",
           f"""
## Definition and Characterization from Source

The Kosmon era is the new dispensation Oahspe announces: "the seventh era," the
age in which "the inhabitation of the earth shall be completed, and the nations
shall have established civil communion around from east to west," so that Jehovih
"render[s] up the records of these heavenly kingdoms." Because this light is
"comprehensive, embracing corporeal and spiritual things, it is called the
beginning of the **KOSMON ERA**." It is the era in which the gates of heaven open
and "the spirits of the dead shall commune with mortals... face to face" (see
[[{CL_SPIRITS}]]) — the text noting this has been happening "now for more than
thirty years," i.e. since the rise of modern Spiritualism in 1848. Oahspe dates
events backward from it in years **B.K.** ("Before Kosmon").

## Key Associated Claims and Events

It is the era of [[{E_KOSMON}]], the founding of the Faithist colony Shalam by
[[{P_TAE}]], and the commandment to put away all Gods, Lords, and Saviors and
worship only [[{C_JEHOVIH}]] (see [[{C_NOSALVATION}]], [[{CL_AMERICA}]]).
""",
           [E_KOSMON, P_TAE, CL_SPIRITS, CL_AMERICA, C_NOSALVATION, C_REVELATION],
           extra_tags=["era/kosmon"])

    period("cycles-of-dan", PER_DAN,
           "from the earliest organic cycles (tens of thousands of years B.K.) to Kosmon",
           f"""
## Definition and Characterization from Source

The cosmic clock of Oahspe is the **dan'ha**: as the sun's "great serpent" (solar
phalanx) travels its 4,700,000-year orbit, Jehovih "placed in the line of the
orbit, at distances of three thousand years, etherean lights," and each time the
earth passes one, "angels from the second heaven come into its corporeal
presence" as "the etherean hosts of the Most High." Each such cycle is named
after the etherean God who superintends it (Sethantes, Aph, Sue, Apollo, Thor,
Osiris, Fragapatti, Cpenta-armij, Lika, etc.). Within each great cycle are
**lesser dans** (200, 400, 500, 600 years) marking the "harvests."

## Key Associated Claims and Events

Every dan'ha brings new revelation, archangels, and a "harvest" of resurrected
souls (see [[{CL_DANHA}]], [[{C_HARVEST}]]). The reckoning underlies
[[{C_PROPHECY}]]. The descent of darkness (**a'ji**) between the lights drives
men and angels to war (see [[{CL_AJI}]]).
""",
           [CL_DANHA, C_HARVEST, C_PROPHECY, CL_AJI, PER_ARCBON, PER_KOSMON],
           extra_tags=["framework/prophetic-cycles"])

    period("arc-of-bon", PER_ARCBON,
           "the cycle of Lika, c. 3,400 B.K.",
           f"""
## Definition and Characterization from Source

The Arc of Bon is the cycle "in the time of Lika, Son of Jehovih" (~3,400 years
before kosmon) treated in the **Book of the Arc of Bon**, "a history of Capilya,
Moses and Chine, the three great leaders-forth of the Faithists." In this cycle
three parallel lawgivers — [[{P_CAPILYA}]] in Vind'yu, [[{P_MOSES}]] in
Arabin'ya, and [[{P_CHINE}]] in Jaffeth — were raised up (over generations by the
[[{C_LOOIS}]]) to deliver the scattered, persecuted Faithists and re-establish
the worship of the one Great Spirit.

## Key Associated Claims and Events

The deliverances of the Faithists; the ending of human sacrifice; the founding of
lasting national religions of the one Great Spirit (see [[{C_LOOIS}]],
[[{G_FAITHISTS}]]).
""",
           [P_CAPILYA, P_MOSES, P_CHINE, C_LOOIS, G_FAITHISTS, PER_DAN],
           extra_tags=["cycle/lika"])


# ---- Events ----------------------------------------------------------------

def event(slug, title, date_start, body, rel, participants=None, date_end=None,
          location_link=None, extra_tags=None):
    parts_yaml = ylist([f"[[{p}]]" for p in participants]) if participants else "[]"
    end_yaml = f'\ndate_end: "{date_end}"' if date_end else ""
    loc_yaml = f'\nlocation: "[[{location_link}]]"' if location_link else ""
    tags = ["event", f"topic/{TOPIC}"] + (extra_tags or [])
    content = f"""---
title: "{title}"
type: event
date_start: "{date_start}"{end_yaml}
participants: {parts_yaml}{loc_yaml}
key_claims: []
sources_ingested: 1
last_updated: {TODAY}
tags: {tags}
---

{body.strip()}

## Related Entities

- {SRC}
{related(rel)}
"""
    write_page("events/oahspe", slug, content)


def events():
    event("cohabitation-angels-asu", E_GENESIS,
          "the age of se'mu (the earth's youth, before the latter days of se'mu)",
          f"""
## Event Overview

Oahspe's account of the origin of immortal man. Jehovih made the first race
[[{G_ASUANS}]] "out of se'mu," "but as a tree, but dwelling in ha'k." He then
called down "millions of angels from heaven" — many of whom "had never fulfilled
a corporeal life, having died in infancy" — to deliver Asu. Though commanded "not
of the tree of life," the angels "dwelt with the Asuans, and were tempted, and
partook of the fruit of the tree of life; and lo and behold they saw their own
nakedness." "And there was born of the first race (Asu) a new race called man" —
the immortal [[{G_IHINS}]]. The angels thereby became "bound spirits of the lower
heaven" and guardian [[{C_ASHARS}]] over their own offspring (see
[[{C_TREEOFLIFE}]]).
""",
          [CL_ASU, C_TREEOFLIFE, G_ASUANS, G_IHINS, C_SEMU, C_ASHARS],
          participants=[G_ASUANS, G_IHINS],
          extra_tags=["event/cosmogonic"])

    event("submersion-of-pan", E_PAN,
          "c. 24,000 B.K. (Before Kosmon)",
          f"""
## Event Overview

The submersion of the continent of [[{L_PAN}]] (Whaga), Oahspe's version of the
Deluge. Because the earth's heavens had become overrun with [[{C_DRUJAS}]] — "the
heavenly kingdoms founded by Gods and Lords have become pest houses for drujas
and fetals" — Jehovih commanded [[{P_APH}]] to "carry away their heaven and
earth." Aph ringed the continent with "pillars of fire" and a net "a thousand
miles" high, stationed etherean [[{C_SHIPS}]] from earth to Chinvat, and "the
vortex of the earth closed in... and the land sank down beneath the water, to
rise no more." Billions of bound spirits were delivered on "birth-blankets"; the
sacred [[{G_IHINS}]] were saved in ships and scattered to the four divisions of
the earth.
""",
          [CL_PAN, L_PAN, P_APH, C_DRUJAS, C_SHIPS, G_IHINS, C_HARVEST],
          participants=[P_APH, G_IHINS],
          location_link=L_PAN,
          extra_tags=["event/cataclysm"])

    event("anuhasaj-becomes-deyus", E_DEYUS,
          "the cycle of Cpenta-armij (c. 5,800 years ago) and after",
          f"""
## Event Overview

The first self-made false Godhead. In the **Book of Wars Against Jehovih**,
[[{P_ANUHASAJ}]] — counseled by **Satan (self)** — rose through centuries of
feigned humility to be crowned **Lord God**, then proclaimed himself the Creator
under the name **De'yus** (Dyaus/Deity). He re-established the false heaven
[[{L_HORED}]] as "the All Highest Place," diverted to himself the spirits owed to
the true God's kingdom Craoshivi, made **Anubi** "Master of the Scales" his "Son
and Savior of Men," and exalted confederate Lords (Osiris, Te-in, Sudga, Baal).
This is the archetypal origin of [[{C_FALSEGODS}]] — angels saying "There is
nothing higher than man... I am the highest" (see [[{CL_SATAN}]],
[[{CL_GODNOTCREATOR}]]).
""",
          [P_ANUHASAJ, C_FALSEGODS, CL_SATAN, CL_GODNOTCREATOR, L_HORED, C_HIERARCHY],
          participants=[P_ANUHASAJ],
          extra_tags=["event/heavenly-rebellion"])

    event("founding-confederacy-holy-ghost", E_CONFED,
          "the centuries before and into the Christian era (per the Book of Eskra)",
          f"""
## Event Overview

The founding of the **[[{G_CONFEDERACY}]]**. Three false Gods —
[[{P_KABALACTES}]], [[{P_ENNOCHISSA}]], and [[{P_LOOEAMONG}]] — "resolved to
organize each one of these three places with a distinct head, and to unite the
three heads as one confederacy... Thus was founded the CONFEDERACY OF THE HOLY
GHOST," each taking "the title, SON OF THE HOLY GHOST." Oahspe presents this as
the literal heavenly origin of the doctrine of the Trinity, and the means by
which Brahmanism, Buddhism, Christianity (and, through [[{P_THOTH}]],
Mohammedanism) were "founded by inspiration" and spread by war (see
[[{CL_FOURFALSE}]]).
""",
          [G_CONFEDERACY, P_KABALACTES, P_ENNOCHISSA, P_LOOEAMONG, P_THOTH, CL_FOURFALSE, C_FALSEGODS],
          participants=[P_LOOEAMONG, P_KABALACTES, P_ENNOCHISSA, P_THOTH],
          extra_tags=["event/heavenly-rebellion"])

    event("looeamong-founds-christianity", E_CHRIST,
          "c. 40 years after Joshu's death; consolidated under Constantine (4th c. A.D.)",
          f"""
## Event Overview

The founding of Christianity, per Oahspe. "Forty years after Joshu's death, a
false God, Looeamong... obsessed the inhabitants of all those countries and
plunged them into war." "[[{P_LOOEAMONG}]], the false God, now changed his name
and falsely called himself **Christ**, which is the Ahamic word for knowledge.
And he raised up tribes of mortal warriors, who called themselves Christians, who
are warriors to this day." The human teacher [[{P_JOSHU}]] is distinguished from
this false "Christ": "the so-called Sermon on the Mount is a plagiarism on
Joshu's teachings, gotten up by the Ecumenical Council under the direction of the
Emperor Constantine" (see [[{CL_CHRIST}]]). Looeamong was "finally cast into hell"
when "the pope established himself as vicegerent."
""",
          [CL_CHRIST, P_LOOEAMONG, P_JOSHU, G_CONFEDERACY, CL_FOURFALSE],
          participants=[P_LOOEAMONG, P_JOSHU],
          extra_tags=["event/religion-founding"])

    event("kosmon-revelation", E_KOSMON,
          "the Kosmon era (text composed c. 1881; the '33rd year')",
          f"""
## Event Overview

The production of Oahspe itself. "In the thirty-third year thereof, the
Embassadors of the angel hosts of heaven prepared and revealed unto man in the
name of Jehovih, His heavenly kingdoms; and have thus herein made known the
plan." The revelation is said to have been given simultaneously to many: "The
same things have been revealed at the same time unto many, who live at remote
distances from one another" (see [[{CL_SIMUL}]]). Its declared aim is "to teach
mortals HOW TO ATTAIN TO HEAR THE CREATOR'S VOICE, and to SEE HIS HEAVENS... whilst
still living" ([[{CL_PURPOSE}]]). The text is attributed on its title page to
[[{P_NEWBROUGH}]] and was, per its own framing, written in [[{L_GUATAMA}]], the
land "untrammeled with Gods and Saviors... enforced by the sword" ([[{CL_AMERICA}]]).
""",
          [CL_SIMUL, CL_PURPOSE, CL_AMERICA, P_NEWBROUGH, C_REVELATION, PER_KOSMON, L_GUATAMA],
          participants=[P_NEWBROUGH, P_TAE],
          location_link=L_GUATAMA,
          extra_tags=["event/revelation"])


# ---- Concepts --------------------------------------------------------------

def concept(slug, title, body, rel, also=None, extra_tags=None):
    also_yaml = ylist(also) if also else "[]"
    tags = ["concept", f"topic/{TOPIC}"] + (extra_tags or [])
    content = f"""---
title: "{title}"
type: concept
also_known_as: {also_yaml}
source_attribution: "{SRC}"
last_updated: {TODAY}
tags: {tags}
---

{body.strip()}

## Related Entities

- {SRC}
{related(rel)}
"""
    write_page("concepts", slug, content)


def concepts():
    concept("jehovih-great-spirit", C_JEHOVIH, f"""
## Definition from Source

Jehovih is the Creator, the "Great Spirit," the "All Person" — a pantheistic
deity who is the totality of existence: "I am the soul of all; and the all that
is seen is of My person and My body." He is "Ever Present" and "doeth by virtue
of His presence, and not by any law." Of "two apparent entities" — "the UNSEEN,
which is POTENT, and the SEEN, which is... IMPOTENT, and called CORPOR" — yet "I
AM BUT ONE." The name was given by man "after the sounds the wind uttereth," as
**E-O-Ih** (see [[{CL_EOIH}]]).

## Key Properties (from source)

- Distinct from "God" and "Lord," who are merely exalted mortals: "the twain God
  and Jehovih are not the same one" (see [[{C_HIERARCHY}]], [[{CL_GODNOTCREATOR}]]).
- Cannot be attained or comprehended in entirety: "To Whom none can attain forever."
- The sole source of Life, Motion, and individuality, which no angel or God can
  create.
- Identified with [[{C_LIGHT}]] ("the I AM") and the omnipresent Life of
  [[{C_SEMU}]].

## Related Concepts

- [[{C_LIGHT}]], [[{C_HIERARCHY}]], [[{C_THREEWORLDS}]], [[{C_INSPIRATION}]]
""", [C_LIGHT, C_HIERARCHY, C_THREEWORLDS, C_INSPIRATION, CL_PANTHEISM, CL_EOIH],
        also=["E-O-Ih", "Eolin", "the Great Spirit", "the All Person", "Ormazd"])

    concept("all-light-i-am", C_LIGHT, f"""
## Definition from Source

Oahspe identifies Jehovih with Light and consciousness: "I am Light; I am
Central, but Boundless." When man asks the omnipresent Life "Who art Thou?" the
answer comes "to the soul of man: I AM LIFE! I AM THE I AM! I AM THE EVER
PRESENT!... I am the Whole!" The "All Light" is the medium of revelation: it
"falls upon the throne" of God, and through it Jehovih speaks.

## Key Properties (from source)

- Light/Life is "OMNIPRESENT" — "it existeth everywhere."
- The degree to which a man perceives the Light is the measure of his wisdom and
  inspiration (see [[{C_INSPIRATION}]]).
- The "All Light" descending marks the presence and voice of Jehovih at the
  heavenly councils.

## Related Concepts

- [[{C_JEHOVIH}]], [[{C_INSPIRATION}]], [[{C_SEMU}]]
""", [C_JEHOVIH, C_INSPIRATION, C_SEMU])

    concept("three-worlds", C_THREEWORLDS, f"""
## Definition from Source

Oahspe's cosmos has "three kinds of worlds": **Corpor** (the corporeal/material —
"whatever has length and breadth and thickness"), **Atmospherea** (the lower
heavens, also called **Hada**, intermediate and "in process of condensation or
dissolution"), and **Etherea** (the highest, made of [[{C_ANTIPHYSICS}]]'s
"ethe," "the MOST RARIFIED"). "Three great estates have I bestowed on man: the
corporeal, the atmospherean, and the etherean." The book's very name encodes
them: Oahspe = earth, sky, and spirit.

## Key Properties (from source)

- A spirit rises through the estates: mortality → atmospherea (the first and
  second resurrections) → etherea (the third). See [[{C_RESURRECTIONS}]].
- Atmospherean worlds come in three densities — A'ji, Ji'ay, and Nebulae.
- Each corporeal world has its own atmospherean heaven that "travels with" it.
- The first heaven of the earth was [[{L_HORED}]].

## Related Concepts

- [[{C_ES}]], [[{C_VORTEXYA}]], [[{C_RESURRECTIONS}]], [[{C_HIERARCHY}]]
""", [C_ES, C_VORTEXYA, C_RESURRECTIONS, C_HIERARCHY, CL_ETHE],
        also=["Corpor, Atmospherea, Etherea", "Hada"])

    concept("es-and-corpor", C_ES, f"""
## Definition from Source

The fundamental duality of Oahspe is **Es** (the unseen) and **Corpor** (the
seen). "I created the seen and the unseen worlds... man called the seen worlds
Corper, and the unseen worlds Es." The inhabitants of Corpor are corporeans;
those of Es are "es'eans... sometimes spirits, and sometimes angels." Es is
divided into etherea and atmospherea. "In all the universe have I made the unseen
to rule over the seen."

## Key Properties (from source)

- Corpor is inert: it has "no power in any direction whatever," neither cohesion
  nor gravitation nor propulsion — all its apparent powers are [[{C_VORTEXYA}]]
  acting upon it from without.
- "The tendency of corpor is to uncorpor itself" (dissolve); "Uz" is the
  dissolution of corpor.
- Es-things are tangible to spirits as corpor is to mortals.

## Related Concepts

- [[{C_THREEWORLDS}]], [[{C_VORTEXYA}]], [[{C_SEMU}]]
""", [C_THREEWORLDS, C_VORTEXYA, C_SEMU],
        also=["the seen and the unseen", "Es", "Corpor"])

    concept("vortexya-cosmogony", C_VORTEXYA, f"""
## Definition from Source

Worlds are made and held by **vortices**, and the single force at work is
**vortexya**. "The earth floateth in the midst of a vortex." By "the power of
rotation" a vortex condenses the "a'ji and ji'ay and nebulae" of the firmament
into a corporeal world: "For each and every corporeal world created I a vortex
first." The whirlwind is given "as a sign to man of the manner of My created
worlds." The sun's master-vortex ("the great serpent, or solar phalanx") carries
the sub-vortices of all the planets.

## Key Properties (from source)

- Vortexya is the one force behind gravity, magnetism, electricity, light, and
  heat: "light, and heat, and magnetism, and electricity, are all one and the
  same thing... the manifestation of vortexian currents under different
  conditions."
- Things fall not by attraction but because "they are driven toward the centre of
  the vortex." (See [[{C_ANTIPHYSICS}]], [[{CL_VORTEX}]].)
- "Withdraw the vortexian power, and the earth would instantly go into
  dissolution."
- A su'is can see vortexya escaping from a magnet in the dark.

## Related Concepts

- [[{C_ANTIPHYSICS}]], [[{C_THREEWORLDS}]], [[{C_PROPHECY}]]
""", [C_ANTIPHYSICS, C_THREEWORLDS, C_PROPHECY, CL_VORTEX, CL_WORLDLIFE],
        also=["vortices", "the great serpent / solar phalanx"])

    concept("denial-of-gravitation-and-solar-heat", C_ANTIPHYSICS, f"""
## Definition from Source

Oahspe's Book of Cosmogony explicitly contradicts "the present Systems of
Philosophy and Astronomy." Three pillars of mainstream physics are denied:

1. **No gravitation.** "Corpor... hath no power in any direction whatever:
   Neither attraction of cohesion, nor attraction of gravitation." Tides, falling
   bodies, and planetary orbits are all vortexya, not attraction. The moon's
   utmost possible magnetic reach falls "more than two hundred thousand miles
   short of reaching to the earth."
2. **No heat from the sun.** "Think not that heat cometh from the sun to the
   earth; heat cometh not from the sun" — warmth is "manufactured" by the earth's
   own vortex (see [[{CL_NOSUNHEAT}]]).
3. **No substance or travel of light.** "There is no such thing as travel of
   light in fact; nor is there any substance of light" — light is "polarity of
   corporeal needles in solution" (see [[{CL_NOLIGHTTRAVEL}]]).

## Key Properties (from source)

- A diamond-quality sun "would be entirely consumed in eighty thousand years" —
  so the sun cannot be the eternal furnace astronomers suppose.
- Spectroscopic readings of the sun actually read intervening etherean solutions,
  not the sun's composition.
- Color is the turning of "needles," not waves; "there is neither wave nor
  undulation in fact."

## Related Concepts

- [[{C_VORTEXYA}]], [[{C_ES}]], [[{CL_ETHE}]]
""", [C_VORTEXYA, C_ES, CL_NOSUNHEAT, CL_NOLIGHTTRAVEL, CL_VORTEX, CL_ETHE],
        also=["the rejection of Newtonian physics"])

    concept("semu-spontaneous-life", C_SEMU, f"""
## Definition from Source

**Se'mu** is the primordial life-bearing substance — "commingled atmosphere and
corporeal substance" — out of which Jehovih quickens all living things by His
presence, "without seed." "In due season I rained down se'mu on the earth; and by
virtue of my presence quickened I into life all the living." The green scum on
water and the jelly-fish are "signs" of the age of se'mu. The Book of Cosmogony
describes se'mu forming on charged water and producing "miniature trees, even
forests... No seed was there."

## Key Properties (from source)

- Life ("this new property... because it existeth everywhere it is called
  OMNIPRESENT") is unfathomable to man, but identical with the [[{C_LIGHT}]] / I
  AM.
- Each world passes through "a time for se'mu" in its youth and ceases to bear it
  in age (see [[{CL_WORLDLIFE}]]).
- From se'mu came the first race [[{G_ASUANS}]] (see [[{CL_SEMU}]], [[{CL_ASU}]]).

## Related Concepts

- [[{C_LIGHT}]], [[{C_SPECIAL}]], [[{C_TREEOFLIFE}]]
""", [C_LIGHT, C_SPECIAL, C_TREEOFLIFE, CL_SEMU, CL_WORLDLIFE],
        also=["se'mu", "the green scum / jelly-fish sign"])

    concept("special-creation", C_SPECIAL, f"""
## Definition from Source

Oahspe affirms the separate creation of each kind and denies transmutation of
species: "Each and every living thing created I new upon the earth, of a kind
each to itself; and not one living thing created I out of another." As a "sign...
that man in his darkness may not believe that one animal changeth and becometh
another," Jehovih permits cross-bred animals but makes the hybrid "barren." "Every
one bringeth forth after its own kind."

## Key Properties (from source)

- Species arise by quickening of se'mu "according to the locality and the
  surroundings," not by descent from other species.
- The doctrine is repeated in the Book of Cosmogony: "not one thing of all of
  them mergeth into another."
- It applies to man's own origin too: the immortal races did not evolve but were
  begotten by angels upon Asu (see [[{C_TREEOFLIFE}]]).

## Related Concepts

- [[{C_SEMU}]], [[{C_RACES}]], [[{C_TREEOFLIFE}]]
""", [C_SEMU, C_RACES, C_TREEOFLIFE, CL_SPECIAL],
        also=["the rejection of evolution / transmutation"])

    concept("races-of-man", C_RACES, f"""
## Definition from Source

Oahspe's anthropology arranges mankind in a sequence of races defined by spiritual
grade and descent:

- **[[{G_ASUANS}]]** (Asu / Adam) — the first race, made from se'mu, soulless and
  mortal.
- **[[{G_IHINS}]]** — the sacred little white-and-yellow people, born of angels +
  Asu; the first immortal race and the Faithists of antiquity.
- **[[{G_DRUKS}]]** — the dark fallen race, from I'hins (or their seed) + Asu;
  "heirs that shall go out in darkness."
- **[[{G_IHUANS}]]** — the copper-colored warrior race, from I'hins + Druks (stock
  of Abram and Moses).
- **[[{G_GHANS}]]** — the highest race, from I'huans + I'hins.

## Key Properties (from source)

- Race correlates with capacity for everlasting life and for hearing Jehovih's
  voice; the chosen "cohabit together" to "rise in wisdom and virtue," while
  mixing with the asuans brings "heirs in the descending grade of life."
- The grades are managed across generations by the [[{C_LOOIS}]].

## Related Concepts

- [[{C_TREEOFLIFE}]], [[{C_SPECIAL}]], [[{C_LOOIS}]]
""", [C_TREEOFLIFE, C_SPECIAL, C_LOOIS, G_ASUANS, G_IHINS, G_IHUANS, G_DRUKS, G_GHANS],
        also=["Asu, I'hin, Druk, I'huan, Ghan"])

    concept("tree-of-life", C_TREEOFLIFE, f"""
## Definition from Source

Oahspe's reworking of Genesis. The first race [[{G_ASUANS}]] was "as a tree,
dwelling in ha'k." Jehovih sent angels to raise Asu, commanding them to "partake
ye not of the tree of life, lest in that labor ye become procreators and as if
dead to the heavens whence ye came." But the angels "were tempted, and partook of
the fruit of the tree of life; and lo and behold they saw their own nakedness."
Their offspring upon Asu was "a new race called man" — the immortal
[[{G_IHINS}]] — and the angels became "bound spirits" and guardians over their
own seed (see [[{E_GENESIS}]], [[{CL_ASU}]]).

## Key Properties (from source)

- The "tree of life" = procreation/corporeal generation; partaking of it binds a
  spirit to the earth.
- Jehovih quickens a new spirit "at the time of conception" for every child, and
  forbids any other spirit to enter a womb (see [[{C_ANTIREINCARNATION}]]).
- Immortality is thus a gift conferred through this angelic descent, not an
  evolutionary attainment.

## Related Concepts

- [[{C_RACES}]], [[{C_ANTIREINCARNATION}]], [[{C_ASHARS}]]
""", [C_RACES, C_ANTIREINCARNATION, C_ASHARS, E_GENESIS, CL_ASU],
        also=["Oahspe's Genesis / Adam (Asu)"])

    concept("three-resurrections", C_RESURRECTIONS, f"""
## Definition from Source

Spiritual ascent proceeds by **grades** through three resurrections (Book of
Discipline): the **first resurrection** is the state of the newly dead ("es'yans"
and bound spirits who still dwell with mortals); the **second resurrection** is
organized angelic life in the heavens, in which angels "abandon" mortals and work
in disciplined "phalanxes"; the **third resurrection** is the rise into etherea,
"the highest of all heavens." "As ye live on the earth, so shall ye reap in
heaven."

## Key Properties (from source)

- Membership in the second resurrection "required the renunciation of all
  associations and conditions below it"; its angels never come as individuals but
  "in legions."
- Three classes of mortals correspond: the world's people, the believers
  (subjective spiritualists), and the Faithists (objective, self-abnegating) —
  only the last "escape the place of the first resurrection."
- Grades are numbered (e.g. "grade fifty") and rise by good works, not profession.

## Related Concepts

- [[{C_HARVEST}]], [[{C_DRUJAS}]], [[{C_NOSALVATION}]], [[{G_FAITHISTS}]]
""", [C_HARVEST, C_DRUJAS, C_NOSALVATION, G_FAITHISTS, CL_RESURRECTIONS],
        also=["grades", "first / second / third resurrection"])

    concept("god-lords-hierarchy", C_HIERARCHY, f"""
## Definition from Source

Heaven is governed by a hierarchy of **exalted mortals**, not by the Creator
directly. In ascending rank: **Lord** ("a one-time mortal, ruler over part of the
people on earth"), **Lord God**, **God** ("ruler over all the people on earth and
in the lower heavens, for a season"), **Orian Chief**, and **Nirvanian Chief** —
above all of whom is Jehovih, "to Whom none can attain." A God's dominion lasts
"never more than three thousand years," fixed by the cycles of dan.

## Key Properties (from source)

- These titles are emphatically **not** the Creator: "the twain God and Jehovih
  are not the same one... none of these, however exalted, can create Life" (see
  [[{CL_GODNOTCREATOR}]]).
- God rules from a heavenly capital (first [[{L_HORED}]], later Craoshivi) with a
  Council; Lords govern the earth's divisions and direct the [[{C_ASHARS}]].
- Mortal kings and emperors are "sons of God," raised to dominion under this
  system.
- The abuse of these offices — angels claiming to BE the Creator — produces
  [[{C_FALSEGODS}]].

## Related Concepts

- [[{C_JEHOVIH}]], [[{C_FALSEGODS}]], [[{C_ASHARS}]], [[{C_HARVEST}]]
""", [C_JEHOVIH, C_FALSEGODS, C_ASHARS, C_HARVEST, CL_GODNOTCREATOR],
        also=["Lord, Lord God, God, Orian Chief, Nirvanian Chief"])

    concept("false-gods-self-godhood", C_FALSEGODS, f"""
## Definition from Source

A **false God** is an angel "who assume[s] kingdoms in atmospherea, denying
Jehovih, professing [himself] to be the Creator, though born of woman." The
prototype is [[{P_ANUHASAJ}]] (De'yus). The progression is always the same:
fallen angels "first questioned My Person; next My Wisdom; next My Justice; next
My Power... whereupon they usurped to themselves to say: There is nothing higher
than man... I am the highest."

## Key Properties (from source)

- Driven by **Satan**, defined in the Glossary as "the captain of the selfish
  passions. Selfishness per se. Self." (see [[{C_BEAST}]], [[{CL_SATAN}]]).
- False Gods demand worship, set up counterfeit heavens (a false [[{L_HORED}]]),
  appoint "Saviors" (Anubi), and drive men to war.
- The great false Gods include De'yus, Osiris, Te-in, Sudga, Baal, Ashtaroth, and
  the four founders of the world religions ([[{G_CONFEDERACY}]]).
- All are eventually "cast into hell."

## Related Concepts

- [[{C_BEAST}]], [[{C_HIERARCHY}]], [[{G_CONFEDERACY}]], [[{C_NOSALVATION}]]
""", [C_BEAST, C_HIERARCHY, G_CONFEDERACY, C_NOSALVATION, CL_SATAN, CL_FOURFALSE, P_ANUHASAJ],
        also=["De'yus and the false Lords", "self-Godhood"])

    concept("the-beast-self", C_BEAST, f"""
## Definition from Source

The **Beast** is self / selfishness — "the animal man. The earthly part of man."
In Oahspe's opening, "the Beast (self) rose up before man" and said, "Possess
thou whatsoever thou wilt," bringing war into the world. "And the Beast divided
itself into four great heads... BRAHMIN, BUDDHIST, CHRISTIAN and MOHAMMEDAN" —
the four idolatrous religions "whose trade was killing man." Satan is its captain:
"the captain of the selfish passions. Selfishness per se. Self."

## Key Properties (from source)

- Allegiance to the Beast makes one a [[{G_UZIANS}]] ("the numbers of the Beast");
  separation from it makes one a Faithist (see [[{CL_TWOKINDS}]]).
- "The four heads of the Beast shall be put away; and war shall be no more" in the
  kosmon era.
- Its "tables" — the times of war and darkness — run on 666 years, "SATAN'S
  TABLES, or the TIMES OF THE BEAST" (see [[{C_PROPHECY}]]).

## Related Concepts

- [[{C_FALSEGODS}]], [[{G_UZIANS}]], [[{C_ETHICS}]], [[{C_PROPHECY}]]
""", [C_FALSEGODS, G_UZIANS, C_ETHICS, C_PROPHECY, CL_TWOKINDS],
        also=["Self", "Satan", "the four heads of the Beast"])

    concept("doctrine-of-inspiration", C_INSPIRATION, f"""
## Definition from Source

The **Book of Inspiration** teaches that man originates nothing; all knowledge,
thought, and impulse flow into him from Jehovih and His creations. "Neither canst
thou, of thine own self, manufacture or acquire... one new thought, nor idea, nor
invention. All thought and knowledge and judgment which thou hast, I gave unto
thee." Man is "as a center; all things come to thee from without" — "of
inspiration made."

## Key Properties (from source)

- Two voices: "The silent voice and the audible voice"; men are susceptible to
  one or both.
- The senses are "corporeal doorways" through which inspiration is received;
  "whatsoever is charged upon these doorways... is inspiration."
- Cumulative knowledge across generations is only "the increase I gave," not
  human creation; a condensing lens lights a fire but "contained not the heat."
- "Perfect manhood" is equal corporeal and spiritual sense; "strong corporeal
  senses and weak spiritual senses... make him infidel."

## Related Concepts

- [[{C_LIGHT}]], [[{C_JEHOVIH}]], [[{C_SUIS}]]
""", [C_LIGHT, C_JEHOVIH, C_SUIS, CL_INSPIRATION],
        also=["the silent and audible voice"])

    concept("suis-sargis", C_SUIS, f"""
## Definition from Source

**Su'is** is "clairaudience and clairvoyance — a person who can see with the eyes
closed, or one who can hear angel voices." **Sar'gis** is "both a materialised
angel, or a person in whose presence the angels can take on the semblance of
mortal forms" (a materialization medium). These are the faculties by which
prophets, seers, and mediums perceive the unseen world.

## Key Properties (from source)

- Su'is can be inborn (the prophets and lawgivers were "natural born su'is and
  sar'gis") or attained "by diet and by fasting."
- A su'is "can see vortexya," e.g. the light escaping a magnet in the dark.
- In the kosmon era these faculties spread widely as the heavens open (see
  [[{CL_SPIRITS}]]), but the Book of Judgment warns that low or unclean sar'gis
  attract lying spirits (see [[{CL_CONSULT}]]).
- The degrees of [[{C_RITES}]] teach the development of su'is and sar'gis.

## Related Concepts

- [[{C_INSPIRATION}]], [[{C_RITES}]], [[{C_DRUJAS}]]
""", [C_INSPIRATION, C_RITES, C_DRUJAS, CL_SPIRITS, CL_CONSULT],
        also=["su'is", "sar'gis", "clairvoyance / materialization"])

    concept("loois-breeding-prophets", C_LOOIS, f"""
## Definition from Source

The **loo'is** are master angels charged with raising up, over generations, the
mortal lines that produce prophets and deliverers. In the History of Capilya, God
sends angels to "dwell with them for six generations" and "lead ye man and woman
together as husband and wife... Raise me up a man that can hear me." The chief
loo'is Hirattax declares: "I will not only raise up an heir to Thee, Jehovih; but
I will have dominion over Thy enemies" — engineering marriages (even of a barren
queen and a cruel king) to bring forth [[{P_CAPILYA}]].

## Key Properties (from source)

- The work is multi-generational and deliberate — a kind of providential
  spiritual eugenics aimed at producing su'is capable of hearing Jehovih.
- It explains the appearance of the lawgivers Capilya, Moses, and Chine in one
  cycle ([[{PER_ARCBON}]]) and the racial grades of [[{C_RACES}]].
- The loo'is guard the pregnancy and infancy of the chosen child with assigned
  angels (144 over Capilya, in four watches).

## Related Concepts

- [[{C_RACES}]], [[{C_SUIS}]], [[{PER_ARCBON}]]
""", [C_RACES, C_SUIS, PER_ARCBON, CL_LOOIS],
        also=["loo'is", "the breeding of prophets"])

    concept("rejection-of-vicarious-salvation", C_NOSALVATION, f"""
## Definition from Source

The Book of Judgment abolishes all saviors and vicarious atonement: "I am not
come to establish, but to abolish all Gods and Lords and Saviors amongst
mortals." "Nor have I provided resurrection in this world, nor in my heavens
above, save by good works done unto others." To say "call thou on this Savior...
and thy sins shall be forgiven thee" is "blasphemy against Jehovih"; church
confession and absolution are likewise condemned.

## Key Properties (from source)

- Judgment is by works, not professions or names: man "shall accept nothing from
  angels or men because of the name professed."
- "There shall be but one doctrine, which is Jehovih, the All Person... with good
  works done unto others."
- The world religions are judged "impotent" — "they have not raised up one city
  of righteous people" (see [[{CL_NOSALVATION}]], [[{CL_IDOLATRY}]]).
- Worship "on the ground of miracles" is to be destroyed; signs are given even to
  liars to prove names mean nothing.

## Related Concepts

- [[{C_FALSEGODS}]], [[{C_ETHICS}]], [[{C_RESURRECTIONS}]], [[{G_FAITHISTS}]]
""", [C_FALSEGODS, C_ETHICS, C_RESURRECTIONS, CL_NOSALVATION, CL_IDOLATRY, G_FAITHISTS],
        also=["no saviors", "salvation by works"])

    concept("faithist-ethics", C_ETHICS, f"""
## Definition from Source

The ethics commanded of the chosen: vegetarianism, non-resistance, community of
goods, and the renunciation of war. In the kosmon commandment Jehovih changes man
"from a carnivorous man of contention to an herbivorous man of peace": "They
shall not eat fish nor flesh of any creature that breathed the breath of life."
The Faithists "abjure war; even, if necessary, by submitting to death rather than
take part therein," "hold their possessions in common," "have no leaders, only
their Creator," and practice "good for evil; non-resistance to persecution."

## Key Properties (from source)

- The army is to be disbanded; "whosoever desireth not to war, thou shalt not
  impress."
- Flesh-eating invites "vampires" and fetals (see [[{C_DRUJAS}]]); diet is tied
  to spiritual grade and to attaining su'is.
- The positive program is to "gather up sinners, and the poor and helpless and
  orphans" into communities — embodied in [[{P_TAE}]]'s colony Shalam.

## Related Concepts

- [[{C_NOSALVATION}]], [[{G_FAITHISTS}]], [[{C_DRUJAS}]]
""", [C_NOSALVATION, G_FAITHISTS, C_DRUJAS, CL_VEG, P_TAE],
        also=["vegetarianism", "non-resistance", "community of goods"])

    concept("tables-of-prophecy", C_PROPHECY, f"""
## Definition from Source

The Book of Cosmogony gives numeric "rules in prophecy" by which the variations
of the earth's vortex (and thus seasons, harvests, wars, and the rise and fall of
nations) can be foretold. The **First Rule**: the sum of heat and light is nearly
constant generation to generation; subdivided by three into **eleven years** (the
Second Rule); the **Third Rule** is **ninety-nine years** plus one. The moon's
cycle is eighteen years; tables of vortexya run in **thirty-three-year** periods.

## Key Properties (from source)

- A **generation = 33 years**; a **cycle (dan'ha) = 3,000 (or 3,300) years**; the
  base of prophecy is built on the divisions of dan (200, 400, 500, 600 years).
- "Winter tables made by the ancients were based on periods of six hundred and
  sixty-six years, and were called **SATAN'S TABLES, or the TIMES OF THE
  BEAST**."
- Prophecy is "more about the cause of things" (vortexya) than new predictions;
  what cannot be found "by any corporeal observation must come by inspiration."

## Related Concepts

- [[{C_VORTEXYA}]], [[{PER_DAN}]], [[{C_BEAST}]]
""", [C_VORTEXYA, PER_DAN, C_BEAST, CL_DANHA, CL_AJI],
        also=["the rules of prophecy", "Satan's Tables / Times of the Beast (666)"])

    concept("drujas-fetals-hells", C_DRUJAS, f"""
## Definition from Source

The dark side of the spirit world. **Drujas** are spirits of darkness who, never
having risen, cling to the earth; **fetals** (and "familiars," "vampires,"
"engrafters") are spirits who feed parasitically on mortals — "vampires that live
on mortals and in swine and cattle, that induce mortals to eat flesh food for
that purpose." When fallen angels and slain warriors accumulate, the heavens of
the earth become **hells** and "knots" — "suffocating hells" of chaos where
spirits "still keep fighting."

## Key Properties (from source)

- A mortal can be obsessed by "hundreds and thousands of spirits" in one body,
  driving out the natural spirit and rendering him "worthless."
- The overrunning of the earth's heavens with drujas and fetals was the cause of
  [[{E_PAN}]] — the kingdoms became "pest houses."
- Flesh-eating, drunkenness, narcotics, and consulting spirits for gain invite
  them (see [[{CL_CONSULT}]]).
- Their delivery from hell is a chief labor of the Gods and ethereans.

## Related Concepts

- [[{C_ASHARS}]], [[{C_RESURRECTIONS}]], [[{C_ETHICS}]], [[{E_PAN}]]
""", [C_ASHARS, C_RESURRECTIONS, C_ETHICS, E_PAN, CL_HELLS, CL_CONSULT],
        also=["drujas", "fetals", "vampires", "hells and knots"])

    concept("ashars-asaphs", C_ASHARS, f"""
## Definition from Source

The two offices of angelic ministry to the earth. **Ashars** are guardian angels
appointed over living mortals — "such of you as are appointed by My God and My
Lords as guardians over mortals shall be called Ashars" — who keep a record of
each mortal's grade and good works. **Asaphs** are the angels who "receive the
spirits of the dead into heaven"; at death the ashar delivers the new spirit
(es'yan), with its record, to the asaph.

## Key Properties (from source)

- The whole earth is divided among Lords and their ashars; each Lord has "ten
  thousand ashars."
- In the second resurrection the guardian work is reorganized into "phalanxes of
  millions," never as individuals, lest mortals worship spirits (see
  [[{C_RESURRECTIONS}]]).
- The es'yan (newborn spirit) is schooled and graded after death; this is the
  receiving end of the resurrection system.

## Related Concepts

- [[{C_HIERARCHY}]], [[{C_RESURRECTIONS}]], [[{C_HARVEST}]]
""", [C_HIERARCHY, C_RESURRECTIONS, C_HARVEST, C_DRUJAS],
        also=["ashars", "asaphs", "guardian angels", "es'yans"])

    concept("brides-and-bridegrooms", C_HARVEST, f"""
## Definition from Source

A **harvest** is the periodic resurrection of prepared souls from the earth's
heavens up to etherea. At the end of a God's dominion, the angels "prepared in
wisdom and strength for resurrection... shall be called **Brides and Bridegrooms
to Jehovih**." In the time of dan, "ships" descend from etherea — sent "by My
etherean Gods and Goddesses" — "and receive God and His Lords with the Brides and
Bridegrooms, and carry them up to the exalted regions."

## Key Properties (from source)

- Harvests occur only "in the time of dan," at the cyclic lights — "at no other
  times... shall My Harvests ascend." (See [[{PER_DAN}]], [[{CL_DANHA}]].)
- Numbers are vast — e.g. a thousand million raised over one Aph-cycle's visits.
- The descending vessels are the [[{C_SHIPS}]].

## Related Concepts

- [[{C_SHIPS}]], [[{PER_DAN}]], [[{C_RESURRECTIONS}]]
""", [C_SHIPS, PER_DAN, C_RESURRECTIONS, CL_DANHA],
        also=["harvests", "Brides and Bridegrooms to Jehovih"])

    concept("etherean-ships-of-fire", C_SHIPS, f"""
## Definition from Source

The heavens of Oahspe are traversed by living vessels of light — "ships of fire,"
also called **avalanza** and **airavagna** — on which the Gods, Goddesses, and
harvested souls travel between worlds. At the deliverance of Pan, "there moved
myriads of shapely stars, which were ships of fire, coursing the firmament,
whereon rode the Gods and Goddesses." A departing ship rises "in spiral form,
turning and rising... like an ascending sun."

## Key Properties (from source)

- They descend in the time of dan to carry up the [[{C_HARVEST}]].
- They are built and steered by etherean craft, contracted or expanded in power
  (Aph's were "contracted ten thousand fold... to break the crust of the earth").
- They are central to the imagery of [[{E_PAN}]] and the great cyclic processions.

## Related Concepts

- [[{C_HARVEST}]], [[{C_THREEWORLDS}]], [[{E_PAN}]]
""", [C_HARVEST, C_THREEWORLDS, E_PAN, P_APH],
        also=["avalanza", "airavagna", "ships of fire"])

    concept("panic-language", C_PANIC, f"""
## Definition from Source

**Panic** is the first human language — "Such is Panic (Earth) language, the
first language" — the speech of the original continent [[{L_PAN}]]. Oahspe's
coined terms (corpor, es, uz, ab, ra) are presented as Panic roots, and the Book
of Saphah traces "the formation of languages, and of rites and ceremonies in all
ages." The Glossary etymologizes sacred words (e.g. "Abracadabra") through Panic.

## Key Properties (from source)

- Language, like all knowledge, is given by inspiration (see [[{C_INSPIRATION}]]).
- Names are not arbitrary: man named the Creator [[{C_JEHOVIH}]] "after the sounds
  the wind uttereth" (E-O-Ih).
- Words and signs (the cross, the wheel, Tau) carry doctrinal meanings preserved
  across the cycles.

## Related Concepts

- [[{C_INSPIRATION}]], [[{C_JEHOVIH}]], [[{L_PAN}]], [[{C_RITES}]]
""", [C_INSPIRATION, C_JEHOVIH, L_PAN, C_RITES, CL_EOIH],
        also=["Panic", "the first language"])

    concept("faithist-rites-degrees", C_RITES, f"""
## Definition from Source

The Faithists preserve secret rites and **degrees of initiation**. The Book of
Wars describes five degrees taught by angels in sar'gis: the first teaches spirit
communion (circles, crescents, how to attract righteous and repel evil spirits);
later degrees teach the names and dominions of the Gods and Lords, the
arrangement of the heavens and hells, and culminate in the **fifth degree, "the
degree of prophecy."** In the Book of Shalam the colonists mark a **"line of the
sacred circle"** to dedicate "the Place of the Holy Covenant."

## Key Properties (from source)

- The higher degrees were kept secret with the Faithists, making them the
  keepers of "the greatest knowledge of the earth"; even kings employed
  fifth-degree Faithists for great works.
- The cross and the wheel are sacred signs (a true prophet is "released by Eolin"
  from the wheel; a false one "rotted on the wheel," marked with the X / "Sa").
- Rites are explanatory "of all the doctrines in the world."

## Related Concepts

- [[{C_SUIS}]], [[{C_PROPHECY}]], [[{G_FAITHISTS}]], [[{C_PANIC}]]
""", [C_SUIS, C_PROPHECY, G_FAITHISTS, C_PANIC],
        also=["the five degrees", "the degree of prophecy", "the sacred circle"])

    concept("oahspe-mode-of-revelation", C_REVELATION, f"""
## Definition from Source

Oahspe presents itself as revelation transcribed by "the Embassadors of the angel
hosts of heaven" in the kosmon era, "in the thirty-third year thereof." It is not
claimed to be inerrant ("Not immaculate in this Book, OAHSPE") and not wholly
new: "the same things have been revealed at the same time unto many, who live at
remote distances from one another" (see [[{CL_SIMUL}]]). Its aim is practical —
to teach mortals "HOW TO ATTAIN TO HEAR THE CREATOR'S VOICE, and to SEE HIS
HEAVENS... whilst still living."

## Key Properties (from source)

- The Book of Discipline warns that both wise and false angels speak to mortals,
  so revelation must be weighed "on the merit only of wisdom and truth," not by
  names professed.
- It is given in [[{L_GUATAMA}]] (America) precisely because that land is "free"
  of enforced state religion (see [[{CL_AMERICA}]]).
- The revelation includes new "science" (vortexya) deliberately "at variance"
  with established astronomy.

## Related Concepts

- [[{C_INSPIRATION}]], [[{PER_KOSMON}]], [[{E_KOSMON}]]
""", [C_INSPIRATION, PER_KOSMON, E_KOSMON, CL_SIMUL, CL_PURPOSE, CL_AMERICA, P_NEWBROUGH],
        also=["the kosmon revelation", "angelic embassadors"])

    concept("rejection-of-reincarnation", C_ANTIREINCARNATION, f"""
## Definition from Source

Oahspe denies reincarnation. Jehovih quickens a new spirit for each child "at the
time of conception" and forbids any pre-existing spirit to re-enter a womb:
"Neither will I give to any spirit of the higher or lower heaven power to enter a
womb, or a fetus of a womb, and be born again." The Book of Discipline lists
belief in reincarnation among the falsehoods of low spirits — "Who saith:
Resurrection cometh by reincarnation... or that a spirit re-entereth the womb, and
is born again in mortality."

## Key Properties (from source)

- Spiritual progress is by resurrection upward through the heavens, not by return
  to flesh (see [[{C_RESURRECTIONS}]]).
- Spirits who claim reincarnation are among the deceiving drujas of the first
  resurrection (see [[{C_DRUJAS}]]).
- A spirit that obsessively re-attaches to mortals is a fetal/vampire, not a
  reborn soul.

## Related Concepts

- [[{C_RESURRECTIONS}]], [[{C_TREEOFLIFE}]], [[{C_DRUJAS}]]
""", [C_RESURRECTIONS, C_TREEOFLIFE, C_DRUJAS, CL_NOREINCARNATION],
        also=["no rebirth into the womb"])


# ---- Claims ----------------------------------------------------------------

def claim(slug, title, contexts, prevalence, statement, evidence, contexts_note,
          rel, actors=None, opposing=None, period=None):
    prevalence = prevalence.replace('"', "'")
    date_or_period = period or "Oahspe revelation (Kosmon era; events reckoned in years B.K.)"
    actors = actors or [{"type": "concept", "link": C_JEHOVIH}]
    actors_yaml = "\n".join(
        f'  - type: {a["type"]}\n    link: "[[{a["link"]}]]"' for a in actors)
    opp = ""
    if opposing:
        opp = f"\n## Opposing Information Within the Source\n\n{opposing}\n"
    content = f"""---
title: "{title}"
type: claim
date_or_period: "{date_or_period}"
involved_actors:
{actors_yaml}
source_attribution: "{SRC}"
contexts: {ylist(contexts)}
prevalence_in_source: "{prevalence}"
status: extracted
last_updated: {TODAY}
tags: [claim, topic/oahspe]
---

## Claim Statement

{statement.strip()}

## Source Attribution and Direct Evidence

{evidence.strip()}

## Contexts Within the Source

{contexts_note.strip()}
{opp}
## Related Entities

- {SRC}
{related(rel)}
"""
    write_page("claims/oahspe", slug, content)


def claims():
    claim("jehovih-is-the-whole", CL_PANTHEISM,
          ["Book of Jehovih, ch. I–II", "Book of Cosmogony, ch. IV"],
          "the foundational theology, stated at the very opening of the revelation",
          "Jehovih (the Great Spirit) is the totality of existence; everything seen and unseen is literally His person and body — a pantheistic monotheism.",
          '"ALL was. ALL is. ALL ever shall be." "I am the soul of all; and the all that is seen is of My person and My body." "Nor is there aught in all the universe but what is part of Him." When man asks Life who it is, the answer: "I AM THE I AM!... All that thou seest in earth or heaven, and even the unseen worlds, also, are My very Person! I am the Whole!"',
          "Opens the Book of Jehovih and recurs as the basis of every other doctrine; the seen (corpor) and unseen (es) are 'but parts of My person; I am the Unity of the whole.'",
          [C_JEHOVIH, C_ES, C_LIGHT],
          actors=[{"type": "concept", "link": C_JEHOVIH}])

    claim("name-eoih-from-the-wind", CL_EOIH,
          ["Book of Jehovih, ch. I"],
          "the account of how the Creator was named; stated once, foundationally",
          "The Creator's name was not invented after any earthly thing but given in imitation of the sound of the wind — E-O-Ih, now pronounced Jehovih.",
          '"I commanded him to give Me a name... And man named Me not after anything in heaven or on the earth. In obedience to My will named he Me after the sounds the wind uttereth, and he said E-O-Ih! Which is now pronounced Jehovih." The Glossary lists the names Eolin, E-O-IH, Eloih, Egoquim, Ormazd as the Creator named by man.',
          "Tied to the doctrine of inspiration (man names by Jehovih's prompting) and to the Panic first-language material.",
          [C_JEHOVIH, C_PANIC, C_INSPIRATION])

    claim("earth-floats-in-a-vortex-no-gravitation", CL_VORTEX,
          ["Book of Cosmogony and Prophecy, ch. I"],
          "the central physical doctrine of the Book of Cosmogony, argued at length",
          "The earth floats in and is held together by a vortex; objects fall not by gravitation but because they are driven toward the vortex's centre. There is no attraction of gravitation in corporeal substance at all.",
          '"The earth floateth in the midst of a vortex." "Things fall not to the earth because of the magnetism therein... but they are driven toward the centre of the vortex, by the power of the vortex." "Corpor, as such, hath no power in any direction whatever: Neither attraction of cohesion, nor attraction of gravitation; nor hath it propulsion."',
          "Argued against Newtonian astronomy with worked examples (tides, the moon's magnetic reach falling 200,000 miles short). See the unifying force [[" + C_VORTEXYA + "]].",
          [C_VORTEXYA, C_ANTIPHYSICS],
          actors=[{"type": "concept", "link": C_VORTEXYA}])

    claim("heat-and-light-not-from-the-sun", CL_NOSUNHEAT,
          ["Book of Cosmogony and Prophecy, ch. I"],
          "repeated emphatic denial throughout the Book of Cosmogony",
          "Neither heat nor light travels from the sun to the earth; the earth's warmth is manufactured by its own vortex.",
          '"Think not that heat cometh from the sun to the earth; heat cometh not from the sun to the earth." "By vortexya was the earth first formed as a ball of fire. By the same power is the warmth of the surface of the earth manufactured to this day." A sun even of diamond quality "would be entirely consumed in eighty thousand years."',
          "Part of the deliberate program to correct astronomy 'wholly at variance with the present Systems of Philosophy.'",
          [C_ANTIPHYSICS, C_VORTEXYA],
          actors=[{"type": "concept", "link": C_VORTEXYA}])

    claim("no-substance-or-travel-of-light", CL_NOLIGHTTRAVEL,
          ["Book of Cosmogony and Prophecy, ch. I–III"],
          "a distinctive optical doctrine, stated with worked argument",
          "Light is neither a substance nor something that travels; it is the polarity of corporeal 'needles' in solution within the master vortex, present everywhere at once.",
          '"There is no such thing as travel of light in fact; nor is there any substance of light. But that which is called light is polarity of corporeal needles in solution, caused by the lines of vortexya." Daylight is "the condition of things polarized within the master vortex"; night is "manufactured by the earth coming betwixt the master\'s focus and the outer extreme."',
          "Color, too, is the turning of needles, not waves: 'there is neither wave nor undulation in fact.'",
          [C_ANTIPHYSICS, C_VORTEXYA],
          actors=[{"type": "concept", "link": C_VORTEXYA}])

    claim("etherea-made-of-ethe-the-solvent", CL_ETHE,
          ["Book of Cosmogony and Prophecy, ch. II", "Book of Jehovih, ch. II"],
          "the basic substance-doctrine of the cosmos",
          "There are only two things in the universe — ethe and corpor — and ethe is the solvent of corpor; the etherean heavens are a vast solution of dissolved corporeal substance.",
          '"There are two known things in the universe: ethe and corpor. The former is the solvent of the latter." "For the substance of My etherean worlds I created Ethe, the MOST RARIFIED... and gave to it power... to penetrate and exist within all things." Salt dissolved in water is the analogy for corpor dissolved in ethe.',
          "Grounds the three-worlds cosmology and the account of how worlds condense out of, and dissolve back into, ethe.",
          [C_ES, C_THREEWORLDS, C_ANTIPHYSICS],
          actors=[{"type": "concept", "link": C_ES}])

    claim("life-without-seed-from-semu", CL_SEMU,
          ["Book of Jehovih, ch. V", "Book of Cosmogony, ch. IV"],
          "the doctrine of the origin of life, repeated as a 'sign'",
          "Living things arise without seed, spontaneously quickened out of the substance se'mu by the presence of Jehovih.",
          '"As a testimony to man, behold the earth was once a globe of liquid fire!... But in due season I rained down se\'mu on the earth; and by virtue of my presence quickened I into life all the living. Without seed created I the life that is in them." In the Book of Cosmogony, se\'mu forms on charged water and produces "miniature trees, even forests... No seed was there."',
          "The green scum and jelly-fish are given as present-day 'signs' of the age of se'mu; Life itself is omnipresent and identical with the I AM.",
          [C_SEMU, C_LIGHT, C_SPECIAL])

    claim("each-species-created-separately", CL_SPECIAL,
          ["Book of Jehovih, ch. V", "Book of Cosmogony, ch. IV"],
          "an explicit, repeated rejection of transmutation of species",
          "Each kind of living thing was created separately by the quickening of se'mu; no species came from another, and cross-bred hybrids are made barren as a sign of this.",
          '"Each and every living thing created I new upon the earth, of a kind each to itself; and not one living thing created I out of another." Hybrids are made barren "that man in his darkness may not believe that one animal changeth and becometh another." "Every one bringeth forth after its own kind."',
          "Applies to man's own origin: the immortal races were begotten, not evolved (see the tree-of-life account).",
          [C_SPECIAL, C_SEMU, C_RACES])

    claim("worlds-are-born-mature-and-die", CL_WORLDLIFE,
          ["Book of Jehovih, ch. IV"],
          "the doctrine of living, mortal worlds",
          "Corporeal worlds are like living creatures: they are born, mature, grow old, and die, passing through fixed stages from molten globe through se'mu to dissolution.",
          '"There is a time of childhood, a time of genesis, a time of old age, and a time of death to all men. Even so is it with all the corporeal worlds I have created." The stages: vapor → molten "globe of fire" → se\'mu (life-bearing) → ho\'tu (barren) → a\'du (cannot generate) → uz (dissipated): "Thus create I, and thus dissipate planets, suns, moons and stars."',
          "Underlies the vortexan cosmogony and the prophetic cycles; the earth 'is not in the place of the firmament as of old.'",
          [C_VORTEXYA, C_SEMU, PER_DAN])

    claim("immortal-man-from-angels-and-asu", CL_ASU,
          ["Book of Jehovih, ch. VI"],
          "Oahspe's central anthropogenic myth (its Genesis)",
          "The first race of man (Asu/Adam) was soulless and mortal, made from se'mu; the immortal races arose only when descended angels cohabited with the Asuans, partaking of the 'tree of life.'",
          '"Out of se\'mu I made man, and man was but as a tree, but dwelling in ha\'k; and I called him Asu (Adam)." The angels were told not to partake of "the tree of life," but "they dwelt with the Asuans, and were tempted, and partook... And there was born of the first race (Asu) a new race called man." The angels thereby became "bound spirits of the lower heaven" and guardians.',
          "Reframes Eden, the Fall, and the 'sons of God' of Genesis 6; the new race is the I'hins, first of the immortal grades.",
          [C_TREEOFLIFE, G_ASUANS, G_IHINS, E_GENESIS, C_RACES])

    claim("continent-of-pan-was-sunk", CL_PAN,
          ["Book of Aph"],
          "a major narrative event, the Oahspe Deluge",
          "About 24,000 years before kosmon, the entire continent of Pan (Whaga) was deliberately sunk beneath the ocean — the event 'commonly called the Deluge, or Flood of waters.'",
          'The Book of Aph records "the submersion of the continent of Whaga (afterward called Pan)... commonly called the Deluge, or Flood of waters." At Aph\'s command "the vortex of the earth closed in about on all sides, and by the pressure, the land sank down beneath the water, to rise no more. And the corporeans went down to death."',
          "Motivated by the overrunning of the earth's heavens with drujas/fetals; the I'hins were saved in ships and scattered to the four divisions of the earth.",
          [E_PAN, L_PAN, P_APH, C_DRUJAS],
          actors=[{"type": "person", "link": P_APH}],
          period="c. 24,000 B.K. (Before Kosmon)")

    claim("dan-ha-every-three-thousand-years", CL_DANHA,
          ["Book of Jehovih, ch. VII", "Book of Cosmogony, ch. III"],
          "the structural principle of Oahspe's history",
          "Every three thousand years the earth, traveling its vast orbit, passes through a region of etherean light (dan'ha), at which time angelic hosts descend, a new revelation is given, and a 'harvest' of souls is raised.",
          'Jehovih "placed in the line of the orbit, at distances of three thousand years, etherean lights, the which places, as the earth passeth through, angels from the second heaven come into its corporeal presence... these are called the etherean hosts of the Most High." The whole circuit "requireth... four million seven hundred thousand years."',
          "Each cycle is named after its presiding God; the lesser dans (200–600 years) time the harvests and the tables of prophecy.",
          [PER_DAN, C_HARVEST, C_PROPHECY],
          period="every ~3,000 years across the earth's 4,700,000-year orbit")

    claim("aji-darkness-drives-men-to-war", CL_AJI,
          ["Book of Wars Against Jehovih, ch. VIII", "Book of Cosmogony"],
          "the doctrine linking cosmic darkness to human history",
          "When the earth passes through regions of nebulous darkness (a'ji), men and angels are driven toward conceit, darkness, and war; Jehovih uses this to test his Gods and Lords.",
          '"Now will I try them for a season, by sending them a\'ji\'an darkness; for My Gods and Lords must learn to master the elements I have created." It was during such a\'jian darkness that Anuhasaj fell to self-conceit and became De\'yus. Winter/war tables run on the 666-year "Times of the Beast."',
          "A'ji is one of the three densities of atmospherean substance; its descent is both a cosmic and a moral event.",
          [C_PROPHECY, PER_DAN, C_FALSEGODS, C_BEAST])

    claim("god-and-lord-are-exalted-mortals", CL_GODNOTCREATOR,
          ["Hints to the Reader", "Book of Discipline, ch. I"],
          "a foundational distinction insisted on throughout",
          "The beings titled God, Lord, and Lord God are exalted one-time mortals ruling for a season — emphatically not the Creator, Jehovih.",
          '"Distinguish, then, that the twain God and Jehovih are not the same one." "God said: I am, as any other spirit of the dead, a one-time man upon the earth, thy elder brother of tens of thousands of years\' experience... none of these, however exalted, can create Life or Motion or an Individual." Lord, Lord God, and God are defined as successive ranks of former mortals.',
          "This distinction is the hinge of the whole polemic against idolatry and false Gods.",
          [C_HIERARCHY, C_JEHOVIH, C_FALSEGODS])

    claim("self-is-the-satan-origin-of-false-gods", CL_SATAN,
          ["Glossary", "Book of Wars Against Jehovih, ch. VIII–IX"],
          "the moral-psychological root of all evil in Oahspe",
          "Satan is not a separate devil but self / selfishness itself; it is the voice that tempts angels to deny Jehovih and proclaim themselves the highest, producing every false God.",
          'The Glossary defines: "Satan. The chief of the seven tetracts, the captain of the selfish passions. Selfishness per se. Self." In the Book of Wars, "Satan (self) said unto Anuhasaj: Who art thou, that one of less wisdom ordereth thee?" — and counsels his whole rise to false Godhood.',
          "The fallen always end by saying 'There is nothing higher than man... I am the highest'; this is the genesis of self-Godhood.",
          [C_FALSEGODS, C_BEAST, P_ANUHASAJ, E_DEYUS],
          actors=[{"type": "person", "link": P_ANUHASAJ}])

    claim("four-religions-founded-by-false-gods", CL_FOURFALSE,
          ["Preface", "God's Book of Eskra"],
          "a central polemical claim of the whole work",
          "The four great world religions — Brahmanism, Buddhism, Christianity, and Mohammedanism — were each founded by inspiration by a false God, not by the Creator.",
          'The Preface names "The Four False Gods": "Looeamong, Kriste, Christ" (Christianity); "Kabalactes, Buddha"; "Ennochissa, Brahma"; "Thoth, Gabriel" (Mohammedanism) — "The founders of the Trinity." Each "by inspiration, founded" his religion and "is finally cast into hell." They united as the Confederacy of the Holy Ghost.',
          "Oahspe distinguishes these false Gods from the true historical sages (Brahma, Sakaya, Joshu) whom they impersonated or supplanted.",
          [G_CONFEDERACY, C_FALSEGODS, P_LOOEAMONG, P_KABALACTES, P_ENNOCHISSA, P_THOTH],
          actors=[{"type": "group", "link": G_CONFEDERACY}])

    claim("christ-was-a-false-god", CL_CHRIST,
          ["Preface", "Book of Cosmogony and Prophecy (historical chapters)", "God's Book of Eskra"],
          "the most pointed anti-Christian claim of the work",
          "'Christ' was not the human Joshu but a false God, Looeamong, who took the name; the Christian gospels (e.g. the Sermon on the Mount) were compiled from Joshu's teachings by an Ecumenical Council under Constantine.",
          '"Looeamong, the false God, now changed his name and falsely called himself Christ, which is the Ahamic word for knowledge. And he raised up tribes of mortal warriors, who called themselves Christians, who are warriors to this day." "The so-called Sermon on the Mount is a plagiarism on Joshu\'s teachings, gotten up by the Ecumenical Council under the direction of the Emperor Constantine."',
          "The real teacher Joshu is presented as an Essenean non-resistant stoned at Jerusalem; 'Christ'/Looeamong declared 'I come not to bring peace, but war!'",
          [P_LOOEAMONG, P_JOSHU, E_CHRIST, G_CONFEDERACY],
          actors=[{"type": "person", "link": P_LOOEAMONG}])

    claim("resurrection-only-by-good-works", CL_NOSALVATION,
          ["The Book of Judgment, ch. III"],
          "the core ethical doctrine of the Book of Judgment, stated absolutely",
          "There is no vicarious salvation: no Savior, prayer, confession, or profession can redeem; resurrection in this world or in heaven comes only by good works done unto others.",
          '"I am not come to establish, but to abolish all Gods and Lords and Saviors amongst mortals." "Nor have I provided resurrection in this world, nor in my heavens above, save by good works done unto others; and this is serving Jehovih." To promise forgiveness by calling on a Savior, or absolution by priest and church, is "a blasphemer against Jehovih."',
          "The judgment is pronounced upon Brahmins, Buddhists, Kriste'yans, Mohammedans, Confucians, and Jews alike; the religions are judged 'impotent' for raising up no city of righteous people.",
          [C_NOSALVATION, C_FALSEGODS, G_FAITHISTS])

    claim("worship-of-any-named-god-is-idolatry", CL_IDOLATRY,
          ["The Book of Judgment, ch. III"],
          "the anti-idolatry doctrine, enumerated name by name",
          "To worship any named God, Lord, or Savior — Brahma, Buddha, Kriste, Deity, or any man or angel figured as a person on a throne — is idolatry and blasphemy against Jehovih, the Ever Present All Person.",
          '"Whoso saith: KRISTE, KRISTE! signifying a God in the figure and shape of a man, sitting on a throne in heaven, is a blasphemer against Jehovih, the Creator, the All Person." The same is said of Brahma and Budah; "whoso calleth on the name of any other man or angel, worshipping such as a God, is an idolator in my sight" — "no less idolatrous than though they worshipped stone idols."',
          "Names that merely signify the Ever Present Creator (God, Ormazd, etc.) are permitted; it is the man-shaped, throne-sitting God that is condemned.",
          [C_NOSALVATION, C_JEHOVIH, C_FALSEGODS])

    claim("man-originates-no-thought", CL_INSPIRATION,
          ["Book of Inspiration, ch. I–II"],
          "the whole thesis of the Book of Inspiration",
          "Man creates no thought, idea, or impulse of his own; all knowledge and judgment are inspiration flowing into him from Jehovih and the external world.",
          '"Neither canst thou, of thine own self, manufacture or acquire or take unto thyself, one new thought, nor idea, nor invention. All thought and knowledge and judgment which thou hast, I gave unto thee." "Thou art as a center; all things come to thee from without." Cumulative human knowledge is "only the increase I gave. Man of himself created none of it."',
          "Grounded in the two voices (silent and audible) and the senses as 'corporeal doorways' of inspiration.",
          [C_INSPIRATION, C_LIGHT])

    claim("mankind-divides-into-faithists-and-uzians", CL_TWOKINDS,
          ["Oahspe (opening proclamation), v. 20–21"],
          "the fundamental social division asserted at the outset",
          "Henceforth mankind is of two kinds only: Faithists, who covenant with Jehovih and separate from the Beast, and Uzians (destroyers), who keep the numbers of the Beast.",
          '"To as many as separate themselves from the dominion of the Beast, making these covenants unto Me... shall they be called FAITHISTS. But to as many as will not make these covenants, have I given the numbers of the Beast, and they shall be called UZIANS, signifying destroyers. And these shall be henceforth the two kinds of people on earth."',
          "The Book of Judgment refines this into three classes (world's people, believers, Faithists), of which only the Faithists practice harmony and good works.",
          [G_FAITHISTS, G_UZIANS, C_BEAST])

    claim("the-chosen-must-be-vegetarian-and-abjure-war", CL_VEG,
          ["Oahspe (opening), v. 16", "The Book of Judgment, ch. I"],
          "the practical ethics commanded of the chosen, repeatedly",
          "Jehovih commands the chosen to become herbivorous men of peace: to eat no fish or flesh, to disband armies, to practice non-resistance, and to abjure war even at the cost of death.",
          '"Thy Creator commandeth thy change from a carnivorous man of contention to an herbivorous man of peace. The four heads of the Beast shall be put away; and war shall be no more." "They shall not eat fish nor flesh of any creature that breathed the breath of life." They shall "abjure war; even, if necessary, by submitting to death rather than take part therein."',
          "Linked to grade and purity: flesh-eating invites vampires/fetals, and the program is embodied in the colony Shalam.",
          [C_ETHICS, G_FAITHISTS, C_DRUJAS])

    claim("dead-commune-with-mortals-face-to-face", CL_SPIRITS,
          ["The Book of Judgment, ch. I", "Book of Jehovih's Kingdom on Earth, ch. III"],
          "the defining sign of the kosmon era",
          "In the kosmon era the gates of heaven are opened so that the spirits of the dead commune with mortals face to face — the phenomenon of modern Spiritualism.",
          '"Thou shalt keep open the gates of heaven for a season, and the spirits of the dead shall commune with mortals... And mortals shall see them, and talk with them, face to face; and they shall recognize their own kin." In the Kingdom book this is said to have been happening "now for more than thirty years, to hundreds of thousands of good people."',
          "Dated implicitly to the rise of Spiritualism in 1848 (year 1 of kosmon); the proof of immortality, but warned against if abused.",
          [PER_KOSMON, C_SUIS, C_DRUJAS],
          actors=[{"type": "concept", "link": C_JEHOVIH}])

    claim("consulting-angels-for-gain-brings-lying-spirits", CL_CONSULT,
          ["The Book of Judgment, ch. I–II", "Book of Discipline"],
          "a strong, repeated warning qualifying the spiritualism of the era",
          "Whoever consults the angels for riches, marriage, curiosity, or any earthly profit — or without seeking to become a better person — is delivered over to drujas, vampires, and lying spirits.",
          '"Whoso consulteth the angels, without regard to becoming a better man himself, suffer him also, to become captive to lying spirits." Those who ask for famous spirits (Moses, Jesus, Kriste) "suffer him to be answered by evil spirits and deceivers." "To all men that feed on fish or flesh, suffer thou vampires to inhabit them."',
          "Part of the kosmon judgment that destroys 'the worship of all Gods and Lords and Saviors on the ground of miracles'; signs are given to liars and truthful alike so that names prove nothing.",
          [C_DRUJAS, C_SUIS, C_NOSALVATION])

    claim("no-spirit-re-enters-a-womb", CL_NOREINCARNATION,
          ["Book of Jehovih, ch. VI", "Book of Discipline, ch. III"],
          "an explicit denial of reincarnation",
          "Jehovih quickens a new spirit for each child at conception and gives no spirit, high or low, power to enter a womb and be born again; reincarnation is a falsehood of low spirits.",
          '"Neither will I give to any spirit of the higher or lower heaven power to enter a womb, or a fetus of a womb, and be born again." The Book of Discipline lists among the lies of dark angels: "Who saith: Resurrection cometh by reincarnation... or that a spirit re-entereth the womb, and is born again in mortality."',
          "Spiritual progress is by resurrection upward through the heavens, not by return to flesh; obsessive re-attachment to mortals is the mark of a fetal/vampire.",
          [C_ANTIREINCARNATION, C_RESURRECTIONS, C_DRUJAS])

    claim("angels-breed-up-prophets-over-generations", CL_LOOIS,
          ["Book of the Arc of Bon, ch. I–II (History of Capilya)"],
          "the doctrine of providential prophet-breeding (loo'is)",
          "Master angels called loo'is raise up prophets and deliverers by inspiring marriages across six generations of mortals, engineering a line that can hear the voice of God.",
          'God commands his angels to "dwell with them for six generations... lead ye man and woman together as husband and wife... Raise me up a man that can hear me." The chief loo\'is Hirattax: "I will not only raise up an heir to Thee, Jehovih; but I will have dominion over Thy enemies" — arranging the birth of [[' + P_CAPILYA + ']].',
          "Explains the simultaneous appearance of Capilya, Moses, and Chine in one cycle, and the racial grades of mankind.",
          [C_LOOIS, P_CAPILYA, C_RACES, PER_ARCBON],
          actors=[{"type": "concept", "link": C_LOOIS}])

    claim("ascent-through-three-resurrections", CL_RESURRECTIONS,
          ["Book of Discipline, ch. I–III"],
          "the structure of the afterlife, stated systematically",
          "The soul ascends by grades through three resurrections: the newly dead first resurrection (still bound to the earth), the organized second resurrection in the heavens, and the third resurrection into etherea.",
          '"First, mortality, then death, which is the first resurrection... Second, angel organization in heaven, and their abandonment of mortals, which is the second resurrection... there is a third resurrection, in which the angels rise still higher... and are sent by thy God into etherea." Membership in the second "required the renunciation of all... below it."',
          "Three classes of mortals correspond to the resurrections; only Faithists 'escape the place of the first resurrection.'",
          [C_RESURRECTIONS, C_HARVEST, G_FAITHISTS])

    claim("earths-heavens-can-become-hells", CL_HELLS,
          ["Book of Jehovih, ch. VIII", "Book of Aph"],
          "a recurring structural danger of the lower heavens",
          "The atmospherean heavens of the earth can degenerate into hells — places of torment, chaos, and bondage — when fallen angels and slain warriors accumulate and prey upon one another.",
          'Rebellious angels "with the foul gases of atmospherea shall... make weapons of war and places of torment... suffocating hells in order to cast one another in chaos." By Aph\'s time "the heavenly kingdoms founded by Gods and Lords have become pest houses for drujas and fetals" — the cause of the submersion of Pan.',
          "Delivering souls out of these hells is a chief labor of the Gods and ethereans, accomplished at the cyclic dawns of dan.",
          [C_DRUJAS, E_PAN, C_RESURRECTIONS])

    claim("revelation-given-simultaneously-to-many", CL_SIMUL,
          ["Oahspe (opening proclamation), v. 25"],
          "the source's account of its own non-exclusive revelation",
          "The revelations of Oahspe were not given to one man alone but disclosed at the same time to many people living far apart who were not in contact with one another.",
          '"Neither are, nor were, the revelations within this OAHSPE wholly new to mortals. The same things have been revealed at the same time unto many, who live at remote distances from one another, but who were not in correspondence till afterward."',
          "Consistent with the doctrine of inspiration and with the kosmon era as a general outpouring of light, not a private message.",
          [C_REVELATION, C_INSPIRATION, PER_KOSMON],
          actors=[{"type": "source", "link": SRC_TITLE}])

    claim("oahspe-teaches-hearing-the-creator-while-living", CL_PURPOSE,
          ["Oahspe (opening proclamation), v. 24"],
          "the stated purpose of the entire work",
          "Oahspe's declared aim is to teach mortals how to hear the Creator's voice and see His heavens in full consciousness while still living, and to know their condition after death.",
          '"Not immaculate in this Book, OAHSPE; but to teach mortals HOW TO ATTAIN TO HEAR THE CREATOR\'S VOICE, and to SEE HIS HEAVENS, in full consciousness, whilst still living on the earth; and to know of a truth the place and condition awaiting them after death."',
          "The same passage disclaims inerrancy ('Not immaculate'), framing the book as practical instruction rather than a fixed creed.",
          [C_REVELATION, C_SUIS, PER_KOSMON],
          actors=[{"type": "source", "link": SRC_TITLE}])

    claim("kosmon-revealed-in-a-free-land", CL_AMERICA,
          ["The Book of Judgment, ch. I"],
          "the providential role assigned to America (Guatama)",
          "The kosmon revelation was given in a land deliberately kept free of Gods, Saviors, and Lords enforced by the sword, so that it could be published openly and not suppressed.",
          '"I have prepared this land untrammeled with Gods and Saviors and Lords, enforced by the sword, so that My revelations of this day shall be published and not suppressed." The land is Guatama (America), home of Eawahtah\'s worship of the Great Spirit and of the kosmon-era colony Shalam.',
          "Connects the New World's freedom of religion to the possibility of the kosmon revelation; the prior cycles' revelations were each confined to one division of the earth.",
          [L_GUATAMA, PER_KOSMON, C_REVELATION],
          actors=[{"type": "concept", "link": C_JEHOVIH}])


if __name__ == "__main__":
    source_page()
    persons()
    groups()
    locations()
    periods()
    events()
    concepts()
    claims()
    print("Oahspe ingest complete.")
