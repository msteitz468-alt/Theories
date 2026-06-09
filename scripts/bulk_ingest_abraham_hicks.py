#!/usr/bin/env python3
"""Bulk-create wiki pages for Esther & Jerry Hicks — *The Essential Law of
Attraction Collection* (Hay House, 2013): the omnibus of *The Law of Attraction*
(2006), *Money, and the Law of Attraction* (2008), and *The Vortex* (2009).

Strict-extraction ingest. Everything below is drawn from the provided text; the
"Teachings of Abraham" are presented as the source presents them (Abraham being,
per the book, a Non-Physical "group consciousness" translated by Esther Hicks).
No external commentary or rebuttal is added.

Topic folder: law-of-attraction.
"""
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
TOPIC = "law-of-attraction"
TODAY = "2026-06-08"
SRC_TITLE = "The Essential Law of Attraction Collection (Hicks, 2013)"
SRC = f"[[{SRC_TITLE}]]"

# ---- Title registry (keep cross-links exact) -------------------------------
P_ESTHER = "Esther Hicks"
P_JERRY = "Jerry Hicks (d. 2011)"
P_ABRAHAM = "Abraham (Non-Physical Group Consciousness)"
P_JANE = "Jane Roberts (Seth)"
P_RHONDA = "Rhonda Byrne"
G_TOA = "The Teachings of Abraham (Abraham-Hicks)"

C_LOA = "Law of Attraction (Abraham-Hicks)"
C_THREELAWS = "The Three Universal Laws (Abraham)"
C_SDC = "The Science of Deliberate Creation"
C_AOA = "The Art of Allowing"
C_SEGINT = "Segment Intending"
C_WORKSHOP = "The Creative Workshop Process"
C_INNERBEING = "Inner Being (Source Energy)"
C_EGS = "Emotional Guidance System"
C_VIBRATION = "Vibration and Vibrational Match (Abraham)"
C_VORTEX = "The Vortex (Vortex of Creation)"
C_ESCROW = "Vibrational Escrow (Vibrational Reality)"
C_THREESTEP = "The Three-Step Process of Creation (Ask, Answer, Allow)"
C_PIVOTING = "The Process of Pivoting"
C_BOPA = "The Book of Positive Aspects"
C_NEWSTORY = "Telling a New Story"
C_CONTRAST = "Contrast (Abraham)"
C_EGSCALE = "The Emotional Guidance Scale"
C_WELLBEING = "Well-Being and the Stream of Well-Being"
C_SETPOINT = "Vibrational Set-Point"
C_DEFAULT = "Creating by Default"
C_SELFISH = "Selfishness as Alignment (Abraham)"
C_APPREC = "Appreciation, the Key to the Vortex"
C_RAMPAGE = "The Rampage of Appreciation"
C_FOCUSWHEEL = "The Focus-Wheel Process"
C_FLAWED = "The Twenty-Two Flawed Premises"
C_PREPAVE = "Prepaving"
C_ETERNAL = "The Eternal Nature of Being (Abraham)"
C_LEADINGEDGE = "Leading Edge and Co-creation"
C_RESISTANCE = "Resistance (Abraham)"
C_BUFFER = "The Buffer of Time"

# ---- Builders --------------------------------------------------------------

def write_page(slug_dir: str, slug: str, content: str):
    path = WIKI / slug_dir / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return path


def related(items):
    return "\n".join(f"- [[{r}]]" for r in items)


def source_page():
    body = f"""---
title: "{SRC_TITLE}"
type: source
source_type: secondary_scholarly
author_or_origin:
  - Esther Hicks
  - Jerry Hicks
  - "Abraham (channeled group consciousness)"
date_composed: "2013 omnibus (collecting works of 2006, 2008, 2009); teachings first recorded 1985–1988"
language_original: English
last_updated: {TODAY}
tags: [source, type/esoteric-selfhelp, topic/law-of-attraction]
---

## Source Description

*The Essential Law of Attraction Collection* (Hay House, 2013; hardcover ISBN
978-1-4019-4420-9) is a single-volume omnibus of three works by Esther and Jerry
Hicks presenting the channeled "Teachings of Abraham": **Book 1 — *The Law of
Attraction: The Basics of the Teachings of Abraham®*** (2006), **Book 2 —
*Money, and the Law of Attraction*** (2008), and **Book 3 — *The Vortex: Where
the Law of Attraction Assembles All Cooperative Relationships*** (2009). The
foreword is by Neale Donald Walsch.

Per the prefaces, Esther Hicks "translates" the vibration of **Abraham**, said
to be "a group of loving entities" (referred to in the plural) — "Non-Physical
teachers." The material was first received in 1985–86 and published in 1988 as
"Special Subjects" cassette albums; this collection presents those original
teachings in book form. The work is framed throughout as a "joy-based philosophy
of practical spirituality," and Book 1's tenet — *the Law of Attraction* —
became the basis of the 2006 film/book *The Secret* (produced by
[[{P_RHONDA}]]).

## What the Source Contributes

- The foundational metaphysics: [[{C_LOA}]], [[{C_THREELAWS}]], [[{C_INNERBEING}]], [[{C_VIBRATION}]], [[{C_WELLBEING}]]
- The creative method: [[{C_SDC}]], [[{C_THREESTEP}]], [[{C_WORKSHOP}]], [[{C_PREPAVE}]], [[{C_DEFAULT}]]
- The allowing/relationship doctrine: [[{C_AOA}]], [[{C_SELFISH}]], [[{C_LEADINGEDGE}]]
- The guidance model: [[{C_EGS}]], [[{C_EGSCALE}]], [[{C_RESISTANCE}]], [[{C_CONTRAST}]]
- The Vortex model (Book 3): [[{C_VORTEX}]], [[{C_ESCROW}]], [[{C_APPREC}]], [[{C_FLAWED}]]
- The practical processes: [[{C_SEGINT}]], [[{C_PIVOTING}]], [[{C_BOPA}]], [[{C_NEWSTORY}]], [[{C_FOCUSWHEEL}]], [[{C_RAMPAGE}]]
- The cast: [[{P_ESTHER}]], [[{P_JERRY}]], [[{P_ABRAHAM}]], [[{G_TOA}]]

## Chapter Summaries

### Book 1 — The Law of Attraction (Parts I–V)
Front matter narrates the origin: Jerry's lifelong search (Ouija board, Albert
Schweitzer, Napoleon Hill's *Think and Grow Rich*, [[{P_JANE}]]'s *Seth Speaks*),
Esther's first contact with Abraham during meditation (Nov 1985), and Abraham's
self-introduction as "Teachers." Part II defines [[{C_LOA}]] ("That which is like
unto itself, is drawn"); Part III, [[{C_SDC}]]; Part IV, [[{C_AOA}]]; Part V,
[[{C_SEGINT}]]. Establishes the [[{C_EGS}]], the [[{C_WORKSHOP}]], and the
[[{C_BUFFER}]].

### Book 2 — Money, and the Law of Attraction (Parts I–V)
Applies the model to money, health, weight, and careers. Introduces
[[{C_NEWSTORY}]] ("the story you tell"), [[{C_PIVOTING}]], the [[{C_BOPA}]],
[[{C_ESCROW}]], [[{C_SETPOINT}]], and [[{C_APPREC}]] (the "$100 process," the
emotional ladder from despair to appreciation). Health doctrine: "all illness is
separation between you and your Inner Being."

### Book 3 — The Vortex (Parts I–V)
Reframes all relationships around the [[{C_VORTEX}]] and the [[{C_THREESTEP}]].
Enumerates [[{C_FLAWED}]] underlying human suffering. Covers mating, sexuality,
parenting, and self-appreciation, culminating in [[{C_APPREC}]], the
[[{C_FOCUSWHEEL}]], and the [[{C_RAMPAGE}]].

## Key Claims Extracted

- [[That Which Is Like Unto Itself, Is Drawn]]
- [[You Get What You Think About, Whether You Want It or Not]]
- [[You Are the Sole Creator of Your Own Reality]]
- [[Nothing Enters Your Experience Without Your Vibrational Invitation]]
- [[There Are No Victims, Only Co-creators]]
- [[Emotions Reveal Your Vibrational Alignment With Source]]
- [[There Is No Such Thing as No in an Attraction-Based Universe]]
- [[Action Cannot Compensate for Misaligned Thought]]
- [[All Illness Is Vibrational Resistance and Separation From the Inner Being]]
- [[The Physical Body Responds Only to Thought]]
- [[Consciousness Is Eternal and All Death Is Self-Inflicted]]
- [[You Have Lived Thousands of Lifetimes]]
- [[Abraham Is a Non-Physical Group Consciousness Translated by Esther Hicks]]
- [[Money Flows in Response to Vibrational Alignment, Not Hard Work]]
- [[Pushing Against Unwanted Things Only Increases Them]]
- [[The Universe Does Not Distinguish Observed Reality From Imagined Reality]]
- [[Source Is Eternally Expanding and Has Reached No Final Conclusion]]
- [[Babies Think and Attract Vibrationally Before They Speak]]
- [[Animals Remain in Alignment With Source]]
- [[Appreciation and Love Are Identical Vibrations]]
- [[The Relationship Between You and Your Source Is the Primary Relationship]]
- [[Sexuality Is Guided by Innate Impulse, Not by Laws From Source]]
- [[A Belief Is Only a Thought You Continue to Think]]
- [[You Cannot Get to a Happy Ending Through an Unhappy Journey]]
- [[Pure Desire Is Always Accompanied by Positive Emotion]]
- [[Reaching for the Better-Feeling Thought Realigns You With Source]]
- [[Caring How You Feel Is the Basis of All Giving]]
- [[You Came Forth Already Worthy]]
- [[Abundance Is Created, Not Discovered, So There Is No Shortage]]
- [[Inspired Action Succeeds Where Effortful Action Fails]]
- [[Well-Being Is the Natural Default State of the Universe]]
- [[You Are on the Leading Edge, Adding to the Expansion of All-That-Is]]
- [[You Do Not Create While Dreaming Because Attraction Stops in Sleep]]

## Internal Tensions or Multiple Accounts

The source frames itself as non-dogmatic ("We come forth not to alter your
beliefs"; "there is nothing that you believe that we do not want you to
believe"), yet asserts its claims as "Law" and "absolute." Abraham concedes the
teaching is openly "selfish" (see [[{C_SELFISH}]]) and that "words do not teach"
— only life experience does — so it presents itself as a reminder of what the
reader "already knows" rather than new information. It explicitly rejects the
idea of a completed/judging God (see [[The Twenty-Two Flawed Premises]] #14).
"""
    write_page("sources", "the-essential-law-of-attraction-collection-hicks-2013", body)


# ---- Persons ---------------------------------------------------------------

def persons():
    write_page("persons", "esther-hicks", f"""---
title: "{P_ESTHER}"
type: person
also_known_as: ["the translator of Abraham"]
roles:
  - channel / "translator" of Abraham
  - co-author
  - workshop presenter
textual_sources:
  - "{SRC}"
last_updated: {TODAY}
tags: [person, topic/law-of-attraction]
---

## Biographical Details from Source

Esther Hicks is presented as the woman who "translates the vibration of
Abraham into the spoken or written word." Per her own account ("My Fears Were
Resolved"), she initially feared anything Non-Physical and disliked her husband
Jerry's [[{P_JANE}]] *Seth* books. After a session with a channel named Sheila
(speaking for an entity "Theo"), who told her "you, too, are channels" and
advised meditation, Esther meditated 15 minutes daily for roughly nine months.
Around Thanksgiving 1985 she began spelling letters with her nose ("I am
Abraham. I am your spiritual guide. I love you."), then typing, then speaking —
Abraham first spoke aloud ("Take the next exit") to avert a freeway accident.

She describes receiving Abraham's thoughts "like radio signals, at an
unconscious level," by relaxing and raising her own vibration to "harmonize"
with Abraham. In the "gate" story (Book 2) Abraham is "peeping through her eyes."
She quips: "I was so afraid of the idea of the Ouija board, and now I am one."

## Primary Source Appearances

Narrator of the origin account; the silent partner in early Q&A; the conduit for
all of Abraham's speech throughout the collection.

## Related Claims, Events, and Groups

- [[Abraham Is a Non-Physical Group Consciousness Translated by Esther Hicks]]
- {SRC}
{related([P_JERRY, P_ABRAHAM, G_TOA])}
""")

    write_page("persons", "jerry-hicks-d-2011", f"""---
title: "{P_JERRY}"
type: person
also_known_as: ["the questioner"]
roles:
  - co-author
  - questioner of Abraham
  - former entertainer / businessman
textual_sources:
  - "{SRC}"
last_updated: {TODAY}
tags: [person, topic/law-of-attraction]
---

## Biographical Details from Source

Jerry Hicks is the husband of [[{P_ESTHER}]] and the principal questioner whose
"long list of burning questions" structures the books. His biography is woven
through the text: a childhood of poverty ("chicken houses and tents and caves"),
a Ouija-board phase (1959, Spokane) that pointed him to Albert Schweitzer, a
transformative encounter with Napoleon Hill's *Think and Grow Rich* (1965) that
built a "multimillion-dollar" business, and a decade reading [[{P_JANE}]]'s
*Seth* books (whose terms "you create your own reality" and "your point of power
is in the present" he carried into the Abraham work). A former circus aerialist
and entertainer, he married Esther in 1980. Abraham says Jerry's "powerful
desire to find answers... summoned Abraham."

Per "About the Authors," **Jerry made his transition into Non-Physical in
November 2011**, after which Esther continued the workshops "with the
Non-Physical help of Abraham and Jerry."

## Primary Source Appearances

Interlocutor in nearly every dialogue; supplies the autobiographical
illustrations (fishing/catch-and-release, the Cadillac "bridging," the H.L. Hunt
story, the hidden-meadow appreciation story).

## Related Claims, Events, and Groups

- [[Consciousness Is Eternal and All Death Is Self-Inflicted]]
- {SRC}
{related([P_ESTHER, P_ABRAHAM, G_TOA, P_JANE])}
""")

    write_page("persons", "abraham-group-consciousness", f"""---
title: "{P_ABRAHAM}"
type: person
also_known_as: ["the Teachings of Abraham", "Non-Physical Teachers", "Source Energy"]
roles:
  - claimed Non-Physical group consciousness
  - "Teacher"
textual_sources:
  - "{SRC}"
last_updated: {TODAY}
tags: [person, topic/law-of-attraction, category/non-physical-entity]
---

## Biographical Details from Source

"Abraham" is presented not as one being but as "a group of loving entities" —
hence the plural — a "group consciousness" of Non-Physical "Teachers," "those
who are currently broader in understanding, who may lead others to that broader
understanding." Abraham states it is "not the biblical or presidential Abraham."
Abraham describes itself as remaining "focused in the broader, clearer... Non-
Physical perspective" while [[{P_ESTHER}]] and [[{P_JERRY}]]
agreed to go "into your magnificent physical bodies and into the Leading Edge of
thought." Abraham is also identified with "[[{C_INNERBEING}]]," "Source," and
the [[{C_VORTEX}]] from which it speaks: "we have the benefit of existing inside
this Vortex that you are creating."

Abraham professes no wish to alter beliefs ("there is nothing that you believe
that we do not want you to believe") and insists "words do not teach... only
life experience teaches."

## Primary Source Appearances

The speaker of all teaching content; answers Jerry's questions and audience
questions across all three books.

## Related Claims, Events, and Groups

- [[Abraham Is a Non-Physical Group Consciousness Translated by Esther Hicks]]
- [[{C_THREELAWS}]]
- {SRC}
{related([P_ESTHER, P_JERRY, G_TOA, C_VORTEX, C_INNERBEING])}
""")

    write_page("persons", "jane-roberts-seth", f"""---
title: "{P_JANE}"
type: person
also_known_as: ["channel of Seth"]
roles:
  - channel / author (acknowledged influence)
textual_sources:
  - "{SRC}"
last_updated: {TODAY}
tags: [person, topic/law-of-attraction, role/influence]
---

## Biographical Details from Source

Jane Roberts is named as a direct precursor influence. She would "go into a sort
of trance and allow Seth, a Non-Physical personality, to speak through her" to
dictate the *Seth* books (co-noted with her husband Robert F. Butts). Jerry read
*Seth Speaks* repeatedly; he credits Seth with two formative terms he never
fully understood but trusted — "You Create Your Own Reality" and "Your Point of
Power Is in the Present." Esther initially feared the Seth material. The Hickses
learned of Roberts's death just before being introduced to channeling, shortly
before Abraham emerged — presented as the lineage into which Abraham arrived.

## Primary Source Appearances

Cited in the Introduction and prefaces as the model of trance channeling that
prepared Jerry and Esther for Abraham.

## Related Claims, Events, and Groups

- {SRC}
{related([P_JERRY, P_ESTHER, P_ABRAHAM])}
""")

    write_page("persons", "rhonda-byrne", f"""---
title: "{P_RHONDA}"
type: person
also_known_as: ["producer of The Secret"]
roles:
  - Australian television producer
textual_sources:
  - "{SRC}"
last_updated: {TODAY}
tags: [person, topic/law-of-attraction, role/popularizer]
---

## Biographical Details from Source

Rhonda Byrne is the Australian television producer who approached the Hickses in
2005 aboard a Law of Attraction cruise seminar, brought a film crew on the 2005
Alaskan cruise, and filmed ~14 hours of Abraham material. The result (2006) was
the DVD movie and book *The Secret*, whose "basic tenet" the source identifies
as the Teachings of Abraham's [[{C_LOA}]]. Esther and Jerry appear only in the
original edition. The source credits *The Secret* with spreading Law of
Attraction "to many more millions" and thereby prompting their "asking."

## Primary Source Appearances

Named in the prefaces to Books 2 and 3.

## Related Claims, Events, and Groups

- {SRC}
{related([C_LOA, P_ESTHER, P_JERRY])}
""")


# ---- Group -----------------------------------------------------------------

def group():
    write_page("groups", "teachings-of-abraham", f"""---
title: "{G_TOA}"
type: group
category: ideological_movement
also_known_as: ["Abraham-Hicks", "the Teachings of Abraham®"]
periods_active: ["1986–present (per source)"]
textual_sources:
  - "{SRC}"
roles_significance:
  - originating modern "Law of Attraction" / New Thought self-help movement
  - source material behind the film/book *The Secret*
last_updated: {TODAY}
tags: [group, topic/law-of-attraction, category/movement]
---

## Identity and Nomenclature

"The Teachings of Abraham®" is the body of channeled material delivered through
[[{P_ESTHER}]], with [[{P_JERRY}]] as questioner. "The Law of Attraction," "The
Teachings of Abraham," "The Art of Allowing," "Segment Intending," and "The
Science of Deliberate Creation" are noted in the copyright page as registered
trademarks of Esther and Jerry Hicks.

## Primary Textual Appearances

The movement's history is given in the prefaces: first disclosed to "a handful
of close business associates in 1986"; recordings published 1988 as two
"Special Subjects" albums; ~50 cities/year of interactive workshops since 1989
from a San Antonio, Texas, base. Other best-selling authors are said to have
incorporated the teachings, and the producer [[{P_RHONDA}]] built *The Secret*
around them.

## Source-Specific Portraits

The movement presents itself as "a joy-based philosophy of practical
spirituality" centered on feeling good, aligning with [[{C_INNERBEING}]], and
the deliberate use of the [[{C_EGS}]]. Its publishing home is Hay House (founded
by Louise Hay, to whom the books are dedicated).

## Related Claims and Events

- [[Abraham Is a Non-Physical Group Consciousness Translated by Esther Hicks]]
- {SRC}

## Related Entities

{related([P_ESTHER, P_JERRY, P_ABRAHAM, C_LOA, P_RHONDA])}
""")


# ---- Concept builder -------------------------------------------------------

def concept(slug, title, body, rel, also=None, extra_tags=None):
    also_yaml = ("[" + ", ".join(f'"{a}"' for a in also) + "]") if also else "[]"
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
    concept("law-of-attraction-abraham", C_LOA, f"""
## Definition from Source

The Law of Attraction is "the most powerful Law in the Universe," stated as:
**"That which is like unto itself, is drawn."** It "affects all things at all
times. Nothing exists that is unaffected by this powerful Law." The book likens
it to "Birds of a feather flock together" and to a radio receiver matching a
transmitting frequency: "the radio signals between the transmitting tower and
your receiver must match."

## Key Properties (from source)

- **Inclusion-based**: there is "no such thing as exclusion" — attention to a
  thing (even shouting "No!") includes it in your vibration. See
  [[There Is No Such Thing as No in an Attraction-Based Universe]].
- **Responds to vibration, not words or action**: it answers "the vibration that
  is at the basis of those words and actions."
- **Amplifying**: "like a giant magnifying glass amplifying whatever is"; small
  thoughts grow "larger and larger, and more and more powerful."
- **Operates with or without belief**: "They do, indeed... You cannot turn your
  Creative Mechanism off."
- **Symmetrical**: "you get what you think about, whether you want it or not."

## Related Concepts

- [[{C_THREELAWS}]] — the first of the three
- [[{C_VIBRATION}]] — what the Law acts upon
- [[{C_SDC}]], [[{C_AOA}]]
""", [C_THREELAWS, C_VIBRATION, C_SDC, C_AOA, "That Which Is Like Unto Itself, Is Drawn"],
        also=["That which is like unto itself, is drawn"])

    concept("three-universal-laws-abraham", C_THREELAWS, f"""
## Definition from Source

Abraham names "three Eternal Universal Laws," to be understood in strict order
because each depends on the prior:

1. **[[{C_LOA}]]** — "That which is like unto itself, is drawn."
2. **[[{C_SDC}]]** — "That which I give thought to and that which I believe or
   expect—is."
3. **[[{C_AOA}]]** — "I am that which I am, and I am willing to allow all others
   to be that which they are."

"You must first understand and effectively utilize the first Law in order to
understand and utilize the second... before you will be able to understand and
utilize the third."

## Key Properties (from source)

- These are "absolute... Eternal... and omnipresent." Other so-called laws (time,
  gravity, space) are merely "agreements" of the physical dimension, not Laws:
  "There are no other Universal Laws that we are waiting to divulge to you."

## Related Concepts

- [[{C_LOA}]], [[{C_SDC}]], [[{C_AOA}]], [[{C_INNERBEING}]]
""", [C_LOA, C_SDC, C_AOA, P_ABRAHAM])

    concept("science-of-deliberate-creation", C_SDC, f"""
## Definition from Source

The second Universal Law (also called "the Law of Creation"): **"That which I
give thought to and that which I believe or expect—is."** It has "two parts: On
the one hand, there is the thought of what you want. On the other hand, there is
the expectation or belief—or the allowing." Creation = **desire + allowing**;
"the launching of the thought and the expectation of the thought."

## Key Properties (from source)

- **Not created through action**: "You did not come into this environment to
  create through action... your action is meant to be a way in which you enjoy
  what you have created through thought." Hospitals are "filled... with those who
  are now taking action to compensate for inappropriate thoughts."
- **Emotion launches it**: thoughts that "evoke great emotion manifest quickly";
  a thought without emotion merely "maintains."
- **The horror-movie example**: a vivid film creates the thought, but "It was
  only a movie" withholds the expectation, so it is not allowed.
- The deliberate process = being clear about desire + sensitive to feeling
  (see [[{C_EGS}]]) + allowing.

## Related Concepts

- [[{C_WORKSHOP}]], [[{C_PREPAVE}]], [[{C_DEFAULT}]], [[{C_THREESTEP}]]
""", [C_THREELAWS, C_WORKSHOP, C_PREPAVE, C_DEFAULT, C_EGS, "Action Cannot Compensate for Misaligned Thought"])

    concept("art-of-allowing", C_AOA, f"""
## Definition from Source

The third Universal Law: **"I am that which I am, and I am willing to allow all
others to be that which they are."** In Book 3 it is restated as "allowing
yourself... to keep up with the expansion of yourself." It is "the most glorious
state of Being you will ever achieve."

## Key Properties (from source)

- **Allowing ≠ tolerating**: "One who tolerates is feeling negative emotion. One
  who is an Allower does not feel negative emotion." Freedom is the absence of
  negative emotion.
- **Achieved by selective focus**, not by changing the world: "finding a way of
  looking at things that still allows your connection to your [[{C_INNERBEING}]]."
- Requires understanding that "another cannot be a part of your experience unless
  you invite them in through your thoughts," removing any need for "walls,
  barricades, armies, wars, or jails."
- The standard of achievement: to "allow another, even in their not allowing of
  you" and "feel joy all of the time."

## Related Concepts

- [[{C_THREELAWS}]], [[{C_SELFISH}]], [[{C_RESISTANCE}]], [[{C_LEADINGEDGE}]]
""", [C_THREELAWS, C_SELFISH, C_RESISTANCE, C_LEADINGEDGE, C_INNERBEING])

    concept("segment-intending", C_SEGINT, f"""
## Definition from Source

Segment Intending is "the process of deliberate identification of what is
specifically wanted for this moment in time." The day is divided into "segments"
(waking, dressing, getting in the vehicle, a phone call, going to sleep), and at
the start of each you "stop and identify what is most important to you."

## Key Properties (from source)

- It eliminates "the predominant hindrances to your Deliberate Creation:
  influence of others... or the influence of your own old habits."
- It is a form of [[{C_PREPAVE}]]: intentions "set forth in advance... begin to
  prepave your future."
- "Clarity brings the speed" — it can speed manifestation and surface inspired
  action.
- Distinguished from a "Workshop" and from "Meditation," each a different
  intention.

## Related Concepts

- [[{C_PREPAVE}]], [[{C_WORKSHOP}]], [[{C_SDC}]]
""", [C_PREPAVE, C_WORKSHOP, C_SDC, C_LOA])

    concept("creative-workshop-process", C_WORKSHOP, f"""
## Definition from Source

The Creative Workshop is a daily 15–20 minute period of "giving thought to what
you want with such clarity that your [[{C_INNERBEING}]] responds by offering
confirming emotion." It is "not a meditative state."

## Key Properties (from source)

- **Be happy first**: enter only when "uplifted, lighthearted"; otherwise "your
  attracting power will not be there."
- **Collect data** through the day "like a shopping spree" — gather wanted
  traits, "leave out" the unwanted ("bring the example of prosperity, and...
  leave out the example of sickness").
- Assemble the data into "a sort of picture of yourself... that satisfies and
  pleases you," from which you attract.
- A "negative Workshop" is any sustained negative focus (e.g. a horror movie, or
  sitting with a stack of bills in fear).

## Related Concepts

- [[{C_SDC}]], [[{C_SEGINT}]], [[{C_BOPA}]]
""", [C_SDC, C_SEGINT, C_BOPA, C_INNERBEING])

    concept("inner-being-source-energy", C_INNERBEING, f"""
## Definition from Source

The "Inner Being" is the "Non-Physical part of you" — "an extension of
Non-Physical Source Energy" — "that broader, older, wiser Non-Physical you...
now also focused into the physical Being that you know as you." Other names
allowed: "Higher Self," "Soul," "Source," "Total You," "who-you-really-are." The
Non-Physical part "remains currently, powerfully, and predominantly focused in
the Non-Physical realm while a part of that perspective flows into this physical
perspective."

## Key Properties (from source)

- It is "the culmination of all that you have lived" (see
  [[You Have Lived Thousands of Lifetimes]]).
- It "always offers a perspective that is to your greatest advantage" and
  "only... focuses upon love" / value / success.
- It "expanded because of the existence and experience of your physical aspect."
- The relationship between you and It generates your emotions (see [[{C_EGS}]]).
  "Source never turns away from you."

## Related Concepts

- [[{C_EGS}]], [[{C_VORTEX}]], [[{C_WELLBEING}]], [[{C_ETERNAL}]]
""", [C_EGS, C_VORTEX, C_WELLBEING, C_ETERNAL, P_ABRAHAM])

    concept("emotional-guidance-system", C_EGS, f"""
## Definition from Source

The Emotional Guidance System is the felt indicator of "the match or mismatch"
between your current thought and the perspective of your [[{C_INNERBEING}]].
"There are only two emotions: One of them feels good, and the other feels bad."
Positive emotion = alignment; negative emotion = "you are, in the moment...
miscreating."

## Key Properties (from source)

- Agreed upon before birth as a feeling "that could not be missed" rather than a
  thought "that could be missed."
- Replaces the impossible task of monitoring thoughts: "rather than trying to
  monitor your thoughts... simply pay attention to how you are feeling."
- Inspiration = "a perfect vibrational match to the broader perspective of your
  Inner Being."
- Negative emotion is a "guiding bell," not merely a "warning bell"; it always
  means "your life has caused expansion which... you are disallowing."

## Related Concepts

- [[{C_EGSCALE}]], [[{C_INNERBEING}]], [[{C_RESISTANCE}]]
""", [C_EGSCALE, C_INNERBEING, C_RESISTANCE, "Emotions Reveal Your Vibrational Alignment With Source"])

    concept("vibration-vibrational-match", C_VIBRATION, f"""
## Definition from Source

"Everything is actually vibrationally based"; "Energy" is used as a synonym. The
five physical senses plus emotion are "six physical vibrational interpreters" —
"what you hear is your interpretation of vibration." At "the very core of your
Being you are vibrating at... perfection in vibrational balance."

## Key Properties (from source)

- The Law of Attraction "matches things that are like, not things that are
  unlike," so "when you feel poor—only things that feel like poverty can come to
  you."
- A "Vibrational Match" is the requirement for any manifestation: "you must
  consistently be a Vibrational Match to what you want."
- Words alone "do not attract"; the emotion behind them reveals the true
  vibration.
- A "thought continues to think" becomes a belief (see
  [[A Belief Is Only a Thought You Continue to Think]]).

## Related Concepts

- [[{C_LOA}]], [[{C_SETPOINT}]], [[{C_RESISTANCE}]]
""", [C_LOA, C_SETPOINT, C_RESISTANCE, C_EGS])

    concept("the-vortex", C_VORTEX, f"""
## Definition from Source

The Vortex (or "Vortex of Creation") is the central concept of Book 3. Each time
life causes you to ask, "a Vibrational, rocketlike request shoots forward and is
received by your [[{C_INNERBEING}]] and becomes the Vibrational, expanded version
of your request." When the Law of Attraction responds to that pure, expanded
desire, "the result is a powerful swirling Vortex of attraction," drawing in
"all cooperative components."

## Key Properties (from source)

- It "holds only your positive requests... holds no thoughts that contradict
  improvement and expansion." Before birth "you were in the Vortex (no resistant
  thought resides there)."
- **You are the missing component**: "You are one of the components of your
  creation. In fact, you are the creation." The only question is whether you are
  "right now, a Vibrational Match" — answered by how you feel.
- Getting "into the Vortex" = the absence of resistance = alignment with all you
  desire. "One person consistently inside the Vortex is more powerful than
  millions who are not."
- The key that opens it is [[{C_APPREC}]], especially appreciation of self.

## Related Concepts

- [[{C_ESCROW}]], [[{C_THREESTEP}]], [[{C_APPREC}]], [[{C_FOCUSWHEEL}]]
""", [C_ESCROW, C_THREESTEP, C_APPREC, C_FOCUSWHEEL, C_INNERBEING])

    concept("vibrational-escrow", C_ESCROW, f"""
## Definition from Source

The "Vibrational Escrow" (also "Vibrational Reality") is "the furthermost,
expanded version of you" — the stored sum of every desire your living has
launched, held by the Inner Being "until you become a close enough Vibrational
Match to them." "Through your process of living life and noticing things wanted
and unwanted, you have created a sort of Vibrational Escrow."

## Key Properties (from source)

- Every contrasting experience "launches a rocket of desire" into it; the Inner
  Being "not only answers your request... but becomes it."
- Your "perfect mate," your improved career, your wellness "is all queued up for
  you" there; your only work is to stop offering "an opposing Vibration."
- It feeds the [[{C_VORTEX}]]: the escrowed desires are what the Vortex assembles
  "cooperative components" for.

## Related Concepts

- [[{C_VORTEX}]], [[{C_CONTRAST}]], [[{C_INNERBEING}]]
""", [C_VORTEX, C_CONTRAST, C_INNERBEING])

    concept("three-step-process-of-creation", C_THREESTEP, f"""
## Definition from Source

The Three-Step Process of Creation:

1. **Ask** — "the contrast of life experience causes you to do that."
2. **Answer** — "not the work of you... but the work of Non-Physical Source
   Energy." The answer forms "in the moment of its launch."
3. **Allow** — "You must find a way to be a Vibrational Match to what you are
   asking for or you will not allow it into your experience."

## Key Properties (from source)

- "Humans are more naturally involved in Step One" (asking/creating); "Animals
  are more naturally involved in Step Three" (allowing). "Humans are more
  creative, and animals are more allowing." See [[Animals Remain in Alignment With Source]].
- Competition/contrast is "a tremendous impetus to Step One" but "a tremendous
  hindrance to Step Three."
- The whole gap between asking and receiving "is only the amount of time that it
  takes you to get into" the [[{C_VORTEX}]].

## Related Concepts

- [[{C_VORTEX}]], [[{C_CONTRAST}]], [[{C_ESCROW}]]
""", [C_VORTEX, C_CONTRAST, C_ESCROW])

    concept("process-of-pivoting", C_PIVOTING, f"""
## Definition from Source

Pivoting is "a conscious recognition that every subject is really two subjects"
— what is wanted and the lack of it — "and then a deliberate speaking or thinking
about the desired aspect." The trigger phrase: **"I know what I don't want; what
is it that I do want?"** In that moment "the answer... is summoned from within
you, and... the beginning of a vibrational shift occurs."

## Key Properties (from source)

- It is **not** pretending the unwanted is wanted: "you are never in a position
  where you can kid yourself into feeling better."
- Esther's drought story: asking "Why do you want the rain?" pivots from lack to
  desire — and "that afternoon it rained."
- Pivoting underlies "[[{C_NEWSTORY}]]" and the [[{C_BOPA}]].

## Related Concepts

- [[{C_NEWSTORY}]], [[{C_BOPA}]], [[{C_EGS}]]
""", [C_NEWSTORY, C_BOPA, C_EGS])

    concept("book-of-positive-aspects", C_BOPA, f"""
## Definition from Source

A literal notebook titled "MY BOOK OF POSITIVE ASPECTS" in which you list what
is good about a person, place, or situation. Origin story: a hotel in Austin
"always seemed to forget" the Hickses were coming; Abraham advised, "you will
take yourselves with you," and had Esther write the hotel's positive aspects —
after which "the hotel never forgot they were coming again."

## Key Properties (from source)

- Writing positive aspects shifts your vibration and therefore your point of
  attraction; the staff "could not buck the current of Esther's negative
  thought."
- Recommended for subjects already mostly positive too, "for the pleasure of
  good-feeling thoughts."
- A close relative of the [[{C_RAMPAGE}]] and the [[{C_FOCUSWHEEL}]].

## Related Concepts

- [[{C_PIVOTING}]], [[{C_RAMPAGE}]], [[{C_APPREC}]]
""", [C_PIVOTING, C_RAMPAGE, C_APPREC])

    concept("telling-a-new-story", C_NEWSTORY, f"""
## Definition from Source

The dominant practical instruction of Book 2: **"You have to tell the story of
your life as you now want it to be and discontinue the tales of how it has been
or of how it is."** "Each and every component that makes up your life experience
is drawn to you by the powerful Law of Attraction's response to the thoughts you
think and the story you tell about your life."

## Key Properties (from source)

- Resistance to it comes from the urge to "tell it like it is"; but "the Law of
  Attraction is responding to you while you are telling your story of 'how it
  is'—and therefore is perpetuating more of whatever story you are telling."
- The book supplies paired "Old Story / New Story" examples for money, body, and
  career.
- "What-is has no bearing on what is coming unless you are continually
  regurgitating the story of what-is."

## Related Concepts

- [[{C_PIVOTING}]], [[{C_SETPOINT}]], [[Money Flows in Response to Vibrational Alignment, Not Hard Work]]
""", [C_PIVOTING, C_SETPOINT, "Money Flows in Response to Vibrational Alignment, Not Hard Work"])

    concept("contrast-abraham", C_CONTRAST, f"""
## Definition from Source

"Contrast" is the variety of wanted and unwanted in physical experience, which
"causes you to do" Step One (asking). "You came forth into this physical life
experience with the intention of experiencing the variety and contrast for the
very purpose of determining your own personal preferences and desires."

## Key Properties (from source)

- "Every subject is really two subjects: what you want and the lack... of what
  you want."
- Contrast "is the basis of expansion" — it "puts the Eternalness into Eternity."
- "Whenever you know what you do not want, you always know more clearly what you
  do want," launching a rocket into your [[{C_ESCROW}]].
- Diversity/contrast is therefore to be valued, not eliminated: "in sameness, in
  conformity, there is not the diversity that stimulates creativity."

## Related Concepts

- [[{C_ESCROW}]], [[{C_THREESTEP}]], [[{C_LEADINGEDGE}]]
""", [C_ESCROW, C_THREESTEP, C_LEADINGEDGE])

    concept("emotional-guidance-scale", C_EGSCALE, f"""
## Definition from Source

The emotional "scale" or ladder from misalignment to alignment, used to climb
toward the [[{C_VORTEX}]] one reachable thought at a time. As stated in Book 3:
"a feeling of powerlessness is the emotion that indicates the greatest distance
from the Vortex... Revenge is closer, anger is closer still, overwhelment is
closer..., and frustration is much closer... Hope is a great deal closer..., and
now you are almost there."

## Key Properties (from source)

- The Book 2 "downstream" formulation (after Joseph Campbell's "follow your
  bliss"): "If you are in despair, follow your revenge; it is downstream. If you
  are in revenge, follow your hatred... hatred → anger → frustration → hope →
  appreciation."
- You cannot leap from despair to joy; "reach for the best-feeling thought you
  can find" from where you are.
- "Belief in Well-Being and knowledge of Well-Being are inside the Vortex, along
  with appreciation and love and passion and eagerness."

## Related Concepts

- [[{C_EGS}]], [[{C_VORTEX}]], [[Reaching for the Better-Feeling Thought Realigns You With Source]]
""", [C_EGS, C_VORTEX, "Reaching for the Better-Feeling Thought Realigns You With Source"])

    concept("well-being-stream", C_WELLBEING, f"""
## Definition from Source

Well-Being is described as "your natural state" and the default condition of the
universe; Source "offers a steady vibration of Well-Being," the "Stream of
Well-Being," ever flowing toward you. "At the core of that which you are is
wellness and Well-Being."

## Key Properties (from source)

- Lack of Well-Being is never an absence of the Stream but a "disallowing" of it
  through resistance: "sickness... occurs when you vibrationally disallow your
  alignment with Well-Being."
- Negative emotion "means that you are preventing your vibrational access to
  Source and to the Stream of Well-Being."
- "Sleep Time Is Realignment-of-Energies Time": during sleep "attraction stops"
  and the Inner Being "realigns your Energies."

## Related Concepts

- [[{C_INNERBEING}]], [[{C_RESISTANCE}]], [[Well-Being Is the Natural Default State of the Universe]]
""", [C_INNERBEING, C_RESISTANCE, "Well-Being Is the Natural Default State of the Universe"])

    concept("vibrational-set-point", C_SETPOINT, f"""
## Definition from Source

The "set-point" is your habitual vibrational baseline on a subject, which
"sets the general tone of your thoughts for the rest of the day." Each morning
"you have an opportunity to establish another vibrational basis (a sort of
set-point)."

## Key Properties (from source)

- Morning is "your most positive vibrational state" (after sleep detaches you
  from resistance); beginning the day looking for positive aspects sets a higher
  set-point.
- "Your vibration is right where you last left it" — bedtime thought carries into
  morning unless deliberately reset.
- A belief is a chronic set-point: "a thought you continue to think."

## Related Concepts

- [[{C_VIBRATION}]], [[{C_NEWSTORY}]], [[A Belief Is Only a Thought You Continue to Think]]
""", [C_VIBRATION, C_NEWSTORY, "A Belief Is Only a Thought You Continue to Think"])

    concept("creating-by-default", C_DEFAULT, f"""
## Definition from Source

"Creating by default" is attracting "without being deliberate about it" —
"giving thought to something without being deliberate about it... thinking about
it, and thereby attracting it—whether you want it or not." Most people "are
creating almost everything in their lives by default because they do not
understand the rules of the game."

## Key Properties (from source)

- Watching television "by default" opens you to "being influenced by whatever is
  thrown at you."
- Two cars colliding are "two Beings who have not intended safety... living life
  by default."
- The remedy is deliberate intent — [[{C_SEGINT}]], the [[{C_WORKSHOP}]], and
  attention to the [[{C_EGS}]].

## Related Concepts

- [[{C_SDC}]], [[{C_SEGINT}]], [[{C_PREPAVE}]]
""", [C_SDC, C_SEGINT, C_PREPAVE])

    concept("selfishness-as-alignment", C_SELFISH, f"""
## Definition from Source

Abraham openly "teaches selfishness": "Selfishness is the sense of self... you
cannot perceive life from any perspective other than from that of yourself."
"Alignment with Source—being inside your [[{C_VORTEX}]]... — is the ultimate
selfishness."

## Key Properties (from source)

- It is the precondition of all giving: "unless you are selfish enough to care
  about how you feel... you have nothing to give another anyway." "You cannot get
  poor enough to help poor people thrive or sick enough to help sick people get
  well."
- "The greatest gift that you could ever give another is the gift of your
  expectation of their success."
- Charge of selfishness from others "without realizing the hypocrisy of their
  demand" (they ask you to please them instead of yourself).

## Related Concepts

- [[{C_AOA}]], [[{C_APPREC}]], [[Caring How You Feel Is the Basis of All Giving]]
""", [C_AOA, C_APPREC, "Caring How You Feel Is the Basis of All Giving"])

    concept("appreciation-key-to-vortex", C_APPREC, f"""
## Definition from Source

Appreciation is "the vibration of alignment with who-you-are... the absence of
resistance... the absence of everything that feels bad and the presence of
everything that feels good." "Love and appreciation are identical vibrations." A
"state of appreciation is a state of Godliness." It is named "the key to getting
inside your [[{C_VORTEX}]]."

## Key Properties (from source)

- Distinguished from **gratitude**, which "often" still carries a "struggle"
  vibration (like motivation vs. inspiration).
- "There is no more important object of attention to which you must flow your
  appreciation than that of self"; "the lack of appreciation of self" holds most
  people outside the Vortex "more than all other thoughts put together."
- Jerry's "hidden meadow" and "Esther" stories illustrate manifestation by
  appreciation: "We never said that we wanted that piece of land—we purely
  appreciated it."

## Related Concepts

- [[{C_RAMPAGE}]], [[{C_VORTEX}]], [[Appreciation and Love Are Identical Vibrations]]
""", [C_RAMPAGE, C_VORTEX, "Appreciation and Love Are Identical Vibrations", C_SELFISH])

    concept("rampage-of-appreciation", C_RAMPAGE, f"""
## Definition from Source

A process of writing/speaking a flowing, escalating list beginning "I
appreciate..." to "firmly stake your claim on your newly acquired higher
Vibration." Presented in Book 3 as the culminating process after the
[[{C_FOCUSWHEEL}]] and the List-of-Positive-Aspects.

## Key Properties (from source)

- Done "from inside the Vortex," where "you are seeing... through the eyes of
  Source," the words "flow easily onto your page."
- Builds momentum like a swirling vortex; used to "milk" and extend a
  resistance-free state.

## Related Concepts

- [[{C_APPREC}]], [[{C_BOPA}]], [[{C_FOCUSWHEEL}]]
""", [C_APPREC, C_BOPA, C_FOCUSWHEEL])

    concept("focus-wheel-process", C_FOCUSWHEEL, f"""
## Definition from Source

A worksheet process to "release resistance and focus you into your
[[{C_VORTEX}]]." Draw a large circle with a small center circle and 12 circles
around the rim "like the numbers on a clock." Write the desired statement in the
center, then fill the 12 positions with progressively better-feeling thoughts you
already believe — like climbing onto a moving "merry-go-round" without being
"tossed... off in the bushes."

## Key Properties (from source)

- Each rim statement must be a thought you currently believe and that "somehow
  makes you feel better," building momentum toward the center desire.
- Worked example: moving from "My employer doesn't appreciate me" to "I know my
  boss sees my value."
- "In this one short process, you have released resistance... and you have
  entered your Vortex."

## Related Concepts

- [[{C_EGSCALE}]], [[{C_PIVOTING}]], [[{C_VORTEX}]]
""", [C_EGSCALE, C_PIVOTING, C_VORTEX])

    concept("twenty-two-flawed-premises", C_FLAWED, f"""
## Definition from Source

Book 3 enumerates **22 "Flawed Premises"** — beliefs "false relative to the
natural Laws of the Universe" that "are at the heart of the confusion and
distortion of your physical reality." They are summarized in a closing list.

## The Premises (verbatim/abridged from source)

1. I am either physical or Non-Physical, either dead or alive.
2. My parents... know better than I do what is right or wrong for me.
3. If I push hard enough against unwanted things, they will go away.
4. I have come here to live the right way of life and to influence others to the same.
5. Because I am older than you, I am wiser than you; therefore you should allow me to guide you.
6. Who I am began the day I was born... [as] an unworthy Being... to achieve greater worthiness.
7. With enough effort, or hard work, I can accomplish anything.
8. To be in harmony with another, we have to want and believe the same things.
9. The path to my joy is through my action... I can get to what I want by leaving what I don't want.
10. I cannot have everything I desire, so I have to give up some things to get others.
11. If I leave an unwanted situation, I will find what I am looking for.
12. There is a finite container of resources... [satisfying mine] deprives others.
13. There are right ways and wrong ways to live, and all should agree and enforce them.
14. **There is a God Who, having considered all things, has come to a final and correct conclusion about everything** ("the most important flawed premise of all").
15. You cannot know, while in your physical body, the true reward or punishment for your actions; it is shown after death.
16. By gathering data... we can sort people into absolute piles of right and wrong, then enforce them.
17. Only very special people, like the founder of our group, can receive the right message from God.
18. By ferreting out the undesirable elements in our society, we can eliminate them and be freer.
19. A good relationship is one whose dominant intention is to find agreement and harmony with the other.
20. When I focus upon things of a physical nature, I am less Spiritual.
21. It is my job as a parent to have all the answers so that I can teach those answers to my children.
22. I can criticize successful people and still achieve my own success.

## Related Concepts

- [[{C_AOA}]], [[{C_VORTEX}]], [[Source Is Eternally Expanding and Has Reached No Final Conclusion]]
""", [C_AOA, C_VORTEX, "Source Is Eternally Expanding and Has Reached No Final Conclusion"])

    concept("prepaving", C_PREPAVE, f"""
## Definition from Source

Prepaving is "In your present, you give thought to your future so that when you
get to that future time, your future has been prepaved, or prepared, for you by
you." "Much that you are experiencing today is as a result of your thoughts about
today that you thought yesterday."

## Key Properties (from source)

- Intending "safety on this journey" before driving "will literally attract the
  circumstances that will bring that about."
- It is the future-facing face of [[{C_SEGINT}]]: "the subjects of your thoughts
  are prepaving your future experiences."
- Past, present, and future are "all one... tied together with the continuum of
  thought."

## Related Concepts

- [[{C_SEGINT}]], [[{C_SDC}]], [[{C_DEFAULT}]]
""", [C_SEGINT, C_SDC, C_DEFAULT])

    concept("eternal-nature-of-being", C_ETERNAL, f"""
## Definition from Source

You are "Eternal Consciousness, with an Eternal history of becoming." Before
birth "you were Source" — "Vibrationally intertwined with... God" with "no
discernible separation." Physical death is "an end to the time that your
Consciousness will flow through this particular physical body," never an end to
Consciousness: "there is never an ending to the Consciousness of You, so really
there is no 'death.'"

## Key Properties (from source)

- "You have lived thousands of lifetimes"; the [[{C_INNERBEING}]] is their
  "culmination." Memory is withheld to avoid "distraction from the power of your
  now."
- "All deaths are a form of 'suicide'" — self-inflicted by withdrawal of Source
  Energy: "Most do not decide to die—they just do not decide to continue to
  live." "Get happy and live long."
- After transition, the Being "looks back... only with love and appreciation."

## Related Concepts

- [[{C_INNERBEING}]], [[Consciousness Is Eternal and All Death Is Self-Inflicted]], [[You Have Lived Thousands of Lifetimes]]
""", [C_INNERBEING, "Consciousness Is Eternal and All Death Is Self-Inflicted", "You Have Lived Thousands of Lifetimes"])

    concept("leading-edge-co-creation", C_LEADINGEDGE, f"""
## Definition from Source

Physical humans are "on the Leading Edge of thought and creation," "Leading-Edge
creators with all of the resources of the Universe at your disposal," "adding
unto the Universe with your every thought, word, and deed." Co-creation is the
intended purpose of sharing the planet with others.

## Key Properties (from source)

- "You are not inferior Beings here trying to catch up, but... Leading-Edge
  creators."
- Your living "equals the expansion of the Universe" / "the expansion of
  All-That-Is" — "you are creating an expanded you," not only an expanded world.
- Relationships are "the basis of the majority of the expansion that you
  achieve" — both the source of "your greatest joys and your greatest sorrows."
- "There is no relationship of greater importance... than the relationship
  between you... and the Soul/Source/God from which you have come."

## Related Concepts

- [[{C_CONTRAST}]], [[{C_ESCROW}]], [[The Relationship Between You and Your Source Is the Primary Relationship]]
""", [C_CONTRAST, C_ESCROW, "The Relationship Between You and Your Source Is the Primary Relationship", "You Are on the Leading Edge, Adding to the Expansion of All-That-Is"])

    concept("resistance-abraham", C_RESISTANCE, f"""
## Definition from Source

Resistance is "caused by focusing upon the lack of what is wanted" — "thought
that does not match the perspective of your Source." It is "the only thing that
ever thwarts joyous creation." "Every dis-ease is caused by vibrational discord
or resistance, without exception."

## Key Properties (from source)

- Felt as negative emotion; if ignored it escalates: "First there is negative
  emotion, then more... then sensation, then pain."
- "True freedom is the absence of resistance."
- The cork analogy: release resistance and "you will take the most direct route
  back to the surface" — your natural Well-Being.

## Related Concepts

- [[{C_EGS}]], [[{C_WELLBEING}]], [[All Illness Is Vibrational Resistance and Separation From the Inner Being]]
""", [C_EGS, C_WELLBEING, "All Illness Is Vibrational Resistance and Separation From the Inner Being"])

    concept("buffer-of-time", C_BUFFER, f"""
## Definition from Source

In physical "time-space reality," manifestation is not instantaneous: "There is
a wonderful buffer of time between when you begin to think about something and
the time it manifests." This buffer "gives you the opportunity to redirect your
attention."

## Key Properties (from source)

- It lets you tell, "by the way you feel," whether a developing thought is wanted
  before it manifests.
- Without it "you would be spending more of your time trying to get rid of your
  mistakes... than... creating the things you want."
- It is why deliberate, sustained thought (not a single thought) is required to
  manifest: "Nothing ever manifests from your first, subtle attention to it."

## Related Concepts

- [[{C_SDC}]], [[{C_EGS}]], [[The Universe Does Not Distinguish Observed Reality From Imagined Reality]]
""", [C_SDC, C_EGS, "The Universe Does Not Distinguish Observed Reality From Imagined Reality"])


# ---- Claim builder ---------------------------------------------------------

def claim(slug, title, contexts, prevalence, statement, evidence, contexts_note,
          rel, actors=None, opposing=None):
    # Quoted YAML scalars must not contain bare double quotes.
    prevalence = prevalence.replace('"', "'")
    contexts = contexts.replace('\\"', "'").replace('"', "'")
    actors = actors or [{"type": "person", "link": P_ABRAHAM}]
    actors_yaml = "\n".join(
        f'  - type: {a["type"]}\n    link: "[[{a["link"]}]]"' for a in actors)
    opp = ""
    if opposing:
        opp = f"\n## Opposing Information Within the Source\n\n{opposing}\n"
    content = f"""---
title: "{title}"
type: claim
date_or_period: "Teachings of Abraham (recorded 1985–2009; collected 2013)"
involved_actors:
{actors_yaml}
source_attribution: "{SRC}"
contexts: {contexts}
prevalence_in_source: "{prevalence}"
status: extracted
last_updated: {TODAY}
tags: [claim, topic/law-of-attraction]
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
    write_page("claims/law-of-attraction", slug, content)


def claims():
    claim("that-which-is-like-unto-itself-is-drawn",
          "That Which Is Like Unto Itself, Is Drawn",
          '["Book 1, Part II — The Law of Attraction"]',
          "the foundational axiom of the entire teaching; restated dozens of times",
          'The single Law underlying all experience is "That which is like unto itself, is drawn" — like vibration attracts like vibration, without exception.',
          'Book 1: "The Law of Attraction says: That which is like unto itself, is drawn... it defines the most powerful Law in the Universe—a Law that affects all things at all times. Nothing exists that is unaffected by this powerful Law." Illustrated with "Birds of a feather flock together," magnetized iron, and matched radio frequencies (630AM). "There is no vibrational evidence, anywhere in the Universe, that supports the idea that opposites attract. They do not."',
          'Presented as Law #1 of the [[{0}]], the prerequisite for understanding the other two. The book insists the reader will find "not a shred of evidence that is contrary."'.format(C_THREELAWS),
          [C_LOA, C_THREELAWS, C_VIBRATION])

    claim("you-get-what-you-think-about",
          "You Get What You Think About, Whether You Want It or Not",
          '["Book 1, Part III", "Book 2 — Money"]',
          "the most-repeated operative slogan in the collection",
          'Whatever you give sustained, emotionalized thought to — wanted or unwanted — you attract the essence of into your experience.',
          '"In short, you get what you are thinking about, whether you want it or not." "Without exception, that which you give thought to is that which you begin to invite into your experience." A thought held long enough "will eventually become powerful enough to attract the essence of itself."',
          'Used to explain why fearing illness attracts illness and why "those who speak most of prosperity have more of it." Tempered by the [[{0}]]: a single thought does not instantly manifest.'.format(C_BUFFER),
          [C_LOA, C_SDC, C_BUFFER, "There Is No Such Thing as No in an Attraction-Based Universe"])

    claim("you-are-the-sole-creator-of-your-reality",
          "You Are the Sole Creator of Your Own Reality",
          '["Book 1, Part III"]',
          "central, asserted repeatedly and defended against objections",
          'No one else can attract into your experience; you alone create your reality through the vibration of your thought. "There is not another who attracts into your experience that which you are getting—you are doing it all."',
          '"No other creates in your experience. You are doing it all; you get all of the credit." Even unwanted things: "only you could have caused it, for no one else has the power to attract what comes to you but you." Borrowed from Seth via [[{0}]]: "You Create Your Own Reality."'.format(P_JANE),
          'Acknowledges the objection ("I wouldn\'t have invited this") and answers that the creating was done "by default," not on purpose.',
          [C_DEFAULT, P_JANE, "Nothing Enters Your Experience Without Your Vibrational Invitation"])

    claim("nothing-enters-without-vibrational-invitation",
          "Nothing Enters Your Experience Without Your Vibrational Invitation",
          '["Book 1, Part IV — The Art of Allowing", "Book 3"]',
          "the basis of the Art of Allowing and of personal safety claims",
          'Nothing — no person, circumstance, or aggressor — can enter your experience uninvited; every rendezvous is a vibrational match you have offered.',
          '"Nothing can come into your life without your attention to it." "Unless you invite them through your thought, aggressors will not be part of your experience. That is Law." Therefore "you no longer feel a need for walls, barricades, armies, wars, or jails."',
          'The claim underwrites the [[{0}]]: because the unwanted cannot "seep or jump into your experience," there is no need to control others.'.format(C_AOA),
          [C_AOA, "There Are No Victims, Only Co-creators"])

    claim("there-are-no-victims-only-co-creators",
          "There Are No Victims, Only Co-creators",
          '["Book 1, Part IV", "Book 3 — parenting/abuse"]',
          "a recurring, deliberately provocative claim applied even to assault and abuse",
          'There are no victims; "the assaulted and the assaulter are co-creators of the event," each a vibrational match. One who "gives much thought to, or... speaks much about, rape" is, by Law, likely to attract such an experience.',
          '"No matter what the subject is, it is important to understand that there are no victims. There are only co-creators." On the abused child: "you do not choose something by looking at it and shouting Yes... You make your choices by your attention to things."',
          'Applied to robbery, prejudice ("the one who feels discriminated against is the most powerful creator"), and child abuse. The book holds that the abuser is also "suffering their own disconnection from Source."',
          ["Nothing Enters Your Experience Without Your Vibrational Invitation", C_LOA],
          opposing='The book concedes "none of us feel joy in watching another being raped or... murdered," and recommends physical separation from abuse "as quickly as possible," while maintaining the vibrational analysis.')

    claim("emotions-reveal-vibrational-alignment",
          "Emotions Reveal Your Vibrational Alignment With Source",
          '["Book 1, Part II", "Book 2"]',
          "the practical core of the entire method",
          'Emotions are the readout of the match or mismatch between your current thought and your Inner Being. Positive emotion = alignment; negative emotion = miscreation. "There are only two emotions: One feels good, and the other feels bad."',
          '"Your emotions are your physical indication of your relationship with your Inner Being." "Whenever there is negative emotion present within you, you are, in that moment, miscreating." The system was "agreed" before birth as a feeling "that could not be missed."',
          'Replaces thought-monitoring ("simply pay attention to how you are feeling") and grounds every process in the book.',
          [C_EGS, C_INNERBEING, C_EGSCALE])

    claim("no-such-thing-as-no",
          "There Is No Such Thing as No in an Attraction-Based Universe",
          '["Book 1, Part II", "Book 2"]',
          "repeatedly asserted to explain why resistance backfires",
          'The universe is "inclusion-based"; attention to a thing includes it in your vibration regardless of whether you say yes or no. "There is no such thing as no."',
          '"When you shout No! at those things you do not want, you are actually inviting those unwanted things into your experience." "The Universe does not hear no. When you are saying, No, I do not want illness, your attention to the subject of illness is saying, Yes, come unto me."',
          'The conceptual root of [[Pushing Against Unwanted Things Only Increases Them]] and the rejection of "Resist ye not evil."',
          [C_LOA, "Pushing Against Unwanted Things Only Increases Them"])

    claim("action-cannot-compensate-for-misaligned-thought",
          "Action Cannot Compensate for Misaligned Thought",
          '["Book 1, Part III", "Book 2 — careers"]',
          "central economic/practical claim, repeated in many forms",
          'Creation is by thought, not action; "there is not enough action in the world to compensate for that misalignment." Action is meant only "to enjoy what you have created through thought."',
          '"You did not come into this environment to create through action." "Your hospitals are filled to the brim with those who are now taking action to compensate for inappropriate thoughts." Action from alignment is "joyful action"; action from contradiction "is hard work that... does not yield good results."',
          'Explains the recurring observation that those who "work hardest have least" — see [[Inspired Action Succeeds Where Effortful Action Fails]].',
          [C_SDC, "Inspired Action Succeeds Where Effortful Action Fails", "Money Flows in Response to Vibrational Alignment, Not Hard Work"])

    claim("all-illness-is-resistance-and-separation",
          "All Illness Is Vibrational Resistance and Separation From the Inner Being",
          '["Book 2, Part III — Physical Well-Being"]',
          "the foundational health claim, asserted without exception",
          'All sickness is the vibrational separation between you and your Inner Being, caused by chronic resistant thought. "Every dis-ease is caused by vibrational discord or resistance, without exception."',
          '"That is what all illness is: separation (caused by your choice of thoughts) between you and your Inner Being." "Illness is nothing more than a physical indicator of Energy out of balance." Negative thought, sustained, becomes "physical sensation—then physical deterioration." "Illness is about resistance, not about age."',
          'Leads to claims that any disease, including "incurable" ones, congenital conditions, and inherited tendencies, can be reversed by thought; that doctors who find what they look for can perpetuate illness; and that "your natural state is one of wellness."',
          [C_RESISTANCE, C_WELLBEING, "The Physical Body Responds Only to Thought"],
          opposing='Abraham says medicine and doctors are "neither good nor bad," and that action "accompanied by joy or love" (e.g. a doctor visit) "is always valuable" — it is action from fear that is not.')

    claim("body-responds-only-to-thought",
          "The Physical Body Responds Only to Thought",
          '["Book 2, Part IV — Health, Weight, and Mind"]',
          "stated emphatically and absolutely",
          'The body is "absolutely a pure reflection of the way you think" and responds to nothing else. "There is nothing else that is affecting your body other than your thoughts."',
          '"There is nothing in the Universe that responds faster to your thoughts than your own physical body." On weight: "When you feel fat, you cannot attract slender"; the body "will respond to the image of self—always." On food: "People respond differently to the food because the food is not the constant—the thought is." Churchill (smoked, lived to 90) cited as evidence behavior matters less than thought.',
          'Drives the weight doctrine (diets fail because they focus on the unwanted fat) and the claim that exercise/nutrition are "far less important than the thoughts you think."',
          ["All Illness Is Vibrational Resistance and Separation From the Inner Being", C_VIBRATION])

    claim("consciousness-is-eternal-death-self-inflicted",
          "Consciousness Is Eternal and All Death Is Self-Inflicted",
          '["Book 2, Part IV"]',
          "core metaphysical claim about death",
          'Consciousness never ends ("there is no death"); the timing of leaving the body is self-determined. "All deaths are a form of suicide" — self-inflicted through withdrawal of Source Energy. "Most do not decide to die—they just do not decide to continue to live."',
          '"There is never an ending to the Consciousness of You." Negative emotion "is a signal that you are cutting off the Source Energy replenishment." "Get happy and live long." After transition the Eternal Being "looks back... only with love and appreciation."',
          'Consistent with [[You Have Lived Thousands of Lifetimes]]. Jerry Hicks is later said (in About the Authors) to have "made his transition into Non-Physical" in November 2011.',
          [C_ETERNAL, "You Have Lived Thousands of Lifetimes", P_JERRY])

    claim("you-have-lived-thousands-of-lifetimes",
          "You Have Lived Thousands of Lifetimes",
          '["Book 1, Part IV"]',
          "stated plainly to explain the Inner Being and zest for life",
          'You are an old Being who has "lived thousands of lifetimes"; the Inner Being is "the culmination of all of those lifetimes of experience," which is why "your zest for life is so great."',
          '"You have lost your physical life on many occasions. You have lived thousands of lifetimes." Memory is withheld because "you do not want the distraction of all that memory." Past-life details "do not affect you in this physical experience" unless you give them attention.',
          'Grounds the Inner Being concept and the rejection of past-life determinism ("I\'m fat because I starved to death in the last [life]" is rejected).',
          [C_ETERNAL, C_INNERBEING, "Consciousness Is Eternal and All Death Is Self-Inflicted"])

    claim("abraham-is-non-physical-group-consciousness",
          "Abraham Is a Non-Physical Group Consciousness Translated by Esther Hicks",
          '["Front matter; About the Authors"]',
          "the framing claim about the source of all the teaching",
          'The teachings are delivered by "Abraham," presented as a Non-Physical "group of loving entities" / "group consciousness" of Teachers, whose vibration Esther Hicks "translates" into words.',
          '"The singular name Abraham is a group of loving entities, which is why they\'re referred to in the plural." "Esther receives our thoughts, like radio signals, at an unconscious level... and then translates them." The phenomenon began in 1985 with nose-spelling, then typing, then speech. "Abraham—a group of uplifting Non-Physical teachers—present their Broader Perspective through Esther Hicks."',
          'The provenance narrative (Ouija board, Schweitzer, Napoleon Hill, [[{0}]]/Seth) frames Abraham as the culmination of Jerry\'s lifelong "asking."'.format(P_JANE),
          [P_ABRAHAM, P_ESTHER, G_TOA, P_JANE])

    claim("money-flows-by-alignment-not-hard-work",
          "Money Flows in Response to Vibrational Alignment, Not Hard Work",
          '["Book 2 — Money, and the Law of Attraction"]',
          "the thesis of Book 2",
          'Financial abundance comes through vibrational alignment, not effort. "The money that comes in response to physical action is very small in comparison with what comes through alignment of thought." "You do not have to have money to attract money, but you cannot feel poor and attract money."',
          'The "$100 process": carry a bill and mentally spend it many times ("if you mentally spend that $100 one thousand times today, you have vibrationally spent $100,000"). The ex-husband who "inherited over a million dollars" by "refusing to feel guilty" while the hardworking wife "focused upon lack" illustrates that "the Universe matched those feelings precisely." "You cannot find a happy ending to an unhappy journey."',
          'Money is "two subjects" — money vs. its absence. Saving from fear "slows the process." Money is framed as Spiritual: "All of the magnificent things of a physical nature... are Spiritual in nature."',
          [C_NEWSTORY, "Action Cannot Compensate for Misaligned Thought", "You Cannot Get to a Happy Ending Through an Unhappy Journey"])

    claim("pushing-against-unwanted-increases-it",
          "Pushing Against Unwanted Things Only Increases Them",
          '["Book 2", "Book 3"]',
          "repeated as a refrain (\"A War Against War Is War\")",
          'Fighting against an unwanted condition focuses on it and therefore enlarges it. Wars against poverty, drugs, AIDS, crime, terror, and cancer "are all getting bigger."',
          '"A War Against War Is War." "Attention to the lack of what is wanted causes it to increase and come closer to you." "You simply cannot get to where you want to be by controlling or eliminating the unwanted." This underlies Flawed Premise #3 and #18.',
          'The constructive alternative is to "relax into your natural Well-Being" and give attention to the wanted. See the [[{0}]] (premises 3, 18).'.format(C_FLAWED),
          ["There Is No Such Thing as No in an Attraction-Based Universe", C_FLAWED, C_AOA])

    claim("universe-does-not-distinguish-observed-from-imagined",
          "The Universe Does Not Distinguish Observed Reality From Imagined Reality",
          '["Book 1, Part III", "Book 2"]',
          "the justification for visualization and \"telling a new story\"",
          'The Law of Attraction responds identically to a thought from observation and a thought from imagination. "The Universe... does not distinguish between a thought brought about by your observation of some reality... and a thought brought about by your imagination."',
          '"Whether you are remembering the past, observing the present, or imagining the future... whatever you are focusing upon is causing an activation of a vibration that the Law of Attraction is responding to." "If you are able to imagine it, it is not unrealistic."',
          'Justifies visualizing the wanted end-result and "telling a new story" before any evidence exists; "you have to offer the vibration before the manifestation."',
          [C_NEWSTORY, C_WORKSHOP, C_BUFFER])

    claim("source-is-eternally-expanding-no-final-conclusion",
          "Source Is Eternally Expanding and Has Reached No Final Conclusion",
          '["Book 3, Part III — Sexuality"]',
          "called \"the most important flawed premise of all\" to refute (Flawed Premise #14)",
          'There is no completed, judging God who has "come to a final and correct conclusion about everything." Source is "Eternally expanding"; therefore "there cannot be a static list of right and wrong or good and evil."',
          'Flawed Premise #14: "There is a God Who, having considered all things, has come to a final and correct conclusion about everything" — "at the root of man\'s continual assault on humanity... your wars, your prejudices, your hatred, and your feelings of unworthiness." "There is no ending to the expansion of God." Guidance is individual and felt, not a handed-down list: "What feels like love, is—and what feels like hate is not love."',
          'Bundled with rejected premises #15 (deferred reward/punishment), #16 (sorting right/wrong), and #17 ("only... the founder of our group can receive the right message from God"). Abraham equates anger/condemnation with "misalignment with that which you call God."',
          [C_FLAWED, "Sexuality Is Guided by Innate Impulse, Not by Laws From Source", C_INNERBEING])

    claim("babies-think-and-attract-before-they-speak",
          "Babies Think and Attract Vibrationally Before They Speak",
          '["Book 1, Part IV", "Book 2", "Book 3"]',
          "the standard answer to the \"innocent child\" objection",
          'Infants think and emit vibration "from their time of birth," absorbing the beliefs and fears of surrounding adults telepathically; thus a baby can attract unwanted conditions.',
          '"The child is thinking, and receiving vibrational thought from you on the day that he enters your environment. That is the reason that beliefs are transmitted so easily from parent to child." Some Beings "deliberately intend to vary from what is normal," choosing "physical disability" or differences (autism framed as resistance to "an epidemic of conformity"). "All Non-Physical Beings coming forth... never come from a position of lack."',
          'Answers the recurring "but what about the innocent child?" challenge while maintaining that no one else creates one\'s reality.',
          ["You Are the Sole Creator of Your Own Reality", C_VIBRATION])

    claim("animals-remain-in-alignment",
          "Animals Remain in Alignment With Source",
          '["Book 3, Part I — animals"]',
          "explains the three-step division between humans and animals",
          'Animals are "extensions of Source Energy" who "primarily remain in a state of Connection or alignment with their Broader Perspective." What humans call "instinct" is "an animal\'s state of alignment with Broader Perspective."',
          '"Humans are more naturally involved in Step One" (asking); "Animals are more naturally involved in Step Three" (allowing). "Humans are more creative, and animals are more allowing." Their "greatest value... is the Vibrational balance they provide."',
          'Part of the [[{0}]] doctrine; control of animals (or people) is "unnatural to man and beast."'.format(C_THREESTEP),
          [C_THREESTEP, C_INNERBEING])

    claim("appreciation-and-love-are-identical-vibrations",
          "Appreciation and Love Are Identical Vibrations",
          '["Book 2 — careers", "Book 3 — self-appreciation"]',
          "the climactic emotional claim of the collection",
          'Appreciation and love are "identical vibrations" — "alignment with who-you-are... the absence of resistance." Appreciation is "the key to getting inside your Vortex," and the most important object of appreciation is the self.',
          '"Love and appreciation are identical vibrations." "A state of appreciation is a state of Godliness." Distinguished from gratitude, which still carries a "struggle" vibration. Jerry\'s "hidden meadow" story: "We never said that we wanted that piece of land—we purely appreciated it" — and it became their office.',
          'The lack of self-appreciation is named the single biggest thing holding people outside the [[{0}]].'.format(C_VORTEX),
          [C_APPREC, C_VORTEX, C_RAMPAGE])

    claim("relationship-with-source-is-primary",
          "The Relationship Between You and Your Source Is the Primary Relationship",
          '["Book 3 — relationships throughout"]',
          "the organizing thesis of Book 3",
          'Of all relationships, the one between the physical you and your Non-Physical Source is primary; no other relationship can be satisfying until it is in alignment. "Alignment first—then anything else."',
          '"There is no relationship of greater importance to achieve than the relationship between you, in your physical body... and the Soul/Source/God from which you have come." A "Soul Mate" is reframed as "mating, or consciously Connecting, with your own Soul." Two secure people make a stable couple; "two who are feeling inadequate" do not. "Fix misalignment and then find a mate."',
          'Reframes mating, parenting, governance, and even sexuality as secondary to self-Source alignment; "you must be selfish enough to be in alignment with your true self before you have anything to give."',
          [C_LEADINGEDGE, C_SELFISH, C_AOA])

    claim("sexuality-guided-by-impulse-not-law",
          "Sexuality Is Guided by Innate Impulse, Not by Laws From Source",
          '["Book 3, Part III — Sexuality"]',
          "the central claim of the sexuality section",
          'No sexual taboos or rules come from Source or the Inner Being; sexuality is governed by natural impulse (like hunger and thirst) for the perpetuation of the species. All sexual laws "come from a perspective of lack."',
          '"No taboos or rules are coming from your Inner Being... they are the product of your physical vulnerability." Negative emotion about sex is never about the act\'s rightness but about "condemning something that your Source does not condemn." "We have never seen a physical human who was in alignment with Source who was repulsed by physical interaction. Repulsion is an indication of disconnection." "Being physical does not separate you from Source, and having sex does not diminish your Spiritual connection" (vs. Flawed Premise #20).',
          'Tied to the rejection of a judging God (Flawed Premise #14) and to the principle that one\'s own felt emotion, not others\' approval, is the only valid guide.',
          ["Source Is Eternally Expanding and Has Reached No Final Conclusion", C_FLAWED, C_EGS])

    claim("a-belief-is-only-a-thought-you-continue-to-think",
          "A Belief Is Only a Thought You Continue to Think",
          '["Book 2", "Book 3"]',
          "a defining formula repeated across the collection",
          'A belief has no special status; it is merely "a thought you continue to think" — "nothing more than a chronic pattern of thought" — and can therefore be changed by changing the thought.',
          '"A belief is only a thought you continue to think. A belief is nothing more than a chronic pattern of thought, and you have the ability... to begin a new pattern, to tell a new story." This means past programming "many years ago" only affects you because "you have been continuing the negative train of thoughts."',
          'Underwrites the changeability of set-points, the rejection of childhood/past-life determinism, and the practicality of "telling a new story."',
          [C_SETPOINT, C_NEWSTORY, C_VIBRATION])

    claim("no-happy-ending-through-unhappy-journey",
          "You Cannot Get to a Happy Ending Through an Unhappy Journey",
          '["Book 2 — Money"]',
          "stated as Law against the \"struggle then success\" mindset",
          'The emotional quality of the path determines the outcome; struggle cannot yield joy. "You cannot find a happy ending to an unhappy journey." "The end absolutely does not justify the means."',
          '"Struggle, struggle, struggle never leads to a happy ending. It defies Law." "When I get there, then I\'ll be happy is not a productive mind-set because unless you are happy, you cannot get there. When you decide to first be happy—then you will get there." "The means... always brings about the essence of an identical ending."',
          'Reframes success as a present-tense alignment ("continual, joyful becoming") rather than a future reward, and undercuts the value of "patience."',
          ["Money Flows in Response to Vibrational Alignment, Not Hard Work", C_WELLBEING])

    claim("pure-desire-is-always-accompanied-by-positive-emotion",
          "Pure Desire Is Always Accompanied by Positive Emotion",
          '["Book 1, Part II"]',
          "a definitional claim distinguishing wanting from needing",
          'To "want" or "desire" in the productive sense is "to focus attention... toward a subject, while at the same time experiencing positive emotion." Desire mixed with doubt is not pure desire but "need," which feels bad.',
          '"Pure desire is always accompanied by positive emotion." "From our point of view, it is not possible to purely desire something while feeling negative emotion." Wanting from lack ("needing") "always feels bad because you are a Vibrational Match to the absence of your desire."',
          'Explains why "wanting someone pushes them away" when the dominant thought is the lack of them; and the subtle but crucial difference between "wanting to feel good" and "not wanting to feel bad."',
          [C_EGS, C_RESISTANCE])

    claim("reaching-for-the-better-feeling-thought",
          "Reaching for the Better-Feeling Thought Realigns You With Source",
          '["Book 1", "Book 2", "Book 3"]',
          "the universally prescribed micro-practice",
          'From wherever you stand you have access only to "two emotions: one that feels better and one that feels worse"; deliberately and repeatedly reaching for the better-feeling thought gradually restores alignment and shifts your point of attraction.',
          '"By reaching for the best-feeling thought you can find, you reconnect with that perspective." You cannot leap from a strongly negative thought to a delightful one ("too much vibrational disparity"); you "build a bridge" thought by thought (the flu-bridging example). In extreme negativity, "distraction" (sleep, music, a movie) is advised over trying to change the thought.',
          'The operational form of the [[{0}]]; underlies the [[{1}]] and the [[{2}]].'.format(C_EGSCALE, C_FOCUSWHEEL, C_PIVOTING),
          [C_EGSCALE, C_FOCUSWHEEL, C_PIVOTING])

    claim("caring-how-you-feel-is-basis-of-all-giving",
          "Caring How You Feel Is the Basis of All Giving",
          '["Book 1, Part II", "Book 3"]',
          "the ethical core of the \"selfishness\" teaching",
          'Unless you are "selfish" enough to maintain your own alignment, you have nothing of value to give anyone; aligned attention, not action, is the only real help. "You only ever uplift from your position of strength and clarity and alignment."',
          '"Unless you are selfish enough to care about how you feel... you have nothing to give another anyway." "You never help others when you allow yourself to be a sounding board for their complaints." "The greatest gift that you could ever give another is the gift of your expectation of their success."',
          'Reverses conventional altruism: giving "from your place of sadness" while "focused on their lack" actually "perpetuat[es] their lack."',
          [C_SELFISH, "The Relationship Between You and Your Source Is the Primary Relationship"])

    claim("you-came-forth-already-worthy",
          "You Came Forth Already Worthy",
          '["Book 1, Part III"]',
          "a doctrinal rejection of original unworthiness",
          'You are not here to prove or earn worthiness; you are already worthy, and your very existence is the proof. Belief in unworthiness is a major source of disallowed Well-Being.',
          '"You are not here to prove your worthiness. You are worthy!" "Your very existence is justification enough." The thought of unworthiness "feels so bad because that thought is in utter disagreement with the way your Inner Being feels." Rejects Flawed Premise #6 (born "unworthy... to achieve greater worthiness").',
          'Tied to the triad of inborn intentions — "freedom, growth, and joy" — and to the claim that struggle is never required to deserve well-being.',
          [C_FLAWED, C_WELLBEING, C_SELFISH])

    claim("abundance-is-created-not-discovered",
          "Abundance Is Created, Not Discovered, So There Is No Shortage",
          '["Book 3, Part I"]',
          "the refutation of scarcity/competition (Flawed Premise #12)",
          'Resources are not a finite pile to be discovered and divided; they are continually created by desire. "You are not merely discovering improved benefits. You are creating them." Therefore satisfying your desire deprives no one.',
          'Flawed Premise #12 rejected: "There is a finite container of resources... when I satisfy my request... I deprive others." "If your time-space reality has the wherewithal to inspire a desire within you... it has the ability to deliver" it. "The feeling of competition or shortage... means you are out of alignment with your own desire." "There is enough of everything for all of you."',
          'Resolves the "what if everyone got everything they want?" objection: a "well-balanced place," not a "mess." Underlies the instruction to "praise abundance wherever you see it."',
          [C_FLAWED, "Money Flows in Response to Vibrational Alignment, Not Hard Work"])

    claim("inspired-action-succeeds-where-effortful-action-fails",
          "Inspired Action Succeeds Where Effortful Action Fails",
          '["Book 1, Part III", "Book 2 — careers"]',
          "the resolution of the \"where does work fit in?\" question",
          'Action taken from alignment (inspired action) is "effortless" and productive; action taken from misaligned thought is "hard work that... does not yield good results." Alignment must precede action.',
          '"Action that is inspired from aligned thought is joyful action." The "2,000 doors" image: in alignment "the door is opened for you," so action is "the way you enjoy the benefit of the alignment." "Get happy, then eat. But do not try to eat your way to happiness."',
          'Explains why some "offer very little action for an enormous return"; the disparity is "only in the comparison of the action... not... the alignment of Energies."',
          ["Action Cannot Compensate for Misaligned Thought", C_SEGINT, C_WELLBEING])

    claim("well-being-is-the-natural-default-state",
          "Well-Being Is the Natural Default State of the Universe",
          '["Book 2, Part III", "Book 3"]',
          "the cosmological optimism underpinning the health and abundance claims",
          'Well-Being is "the basis of everything" and your natural state; the Stream of Well-Being flows constantly and is only ever "disallowed," never withheld. "Your natural state is one of wellness, one of absolute health."',
          '"At the core of that which you are is wellness and Well-Being." Source "offers a steady vibration of Well-Being." Every "awful or abhorrent thing... exists only because someone is disallowing the Well-Being that would be there otherwise." The Dr. Livingstone/lion "euphoria" is explained as the Inner Being\'s flow of Energy once "struggle" (not the desire to live) is released.',
          'The premise that makes resistance — not any opposing force — the sole obstacle: "It is your resistance that causes an illness in the first place."',
          [C_WELLBEING, C_RESISTANCE, "All Illness Is Vibrational Resistance and Separation From the Inner Being"])

    claim("you-are-on-the-leading-edge-of-expansion",
          "You Are on the Leading Edge, Adding to the Expansion of All-That-Is",
          '["Book 1, Part I", "Book 3 — self-appreciation"]',
          "the cosmic-purpose claim, emphasized in the closing chapters",
          'Physical humans are "Leading-Edge creators" whose every desire launches a "rocket" that expands not only their own reality but "All-That-Is." Creation is ongoing: "not a story of something that happened—but a story of something that is happening."',
          '"You are truly on the Leading Edge of thought, adding unto the Universe with your every thought, word, and deed." "It is not only an expanded world you are creating—it is an expanded you." "The expansion of the Universe is the inevitable consequence of life."',
          'Frames human contrast and even suffering as the engine of universal expansion ("puts the Eternalness into Eternity"); humility that refuses this role is why the book was written.',
          [C_LEADINGEDGE, C_CONTRAST, C_ESCROW])

    claim("you-do-not-create-while-dreaming",
          "You Do Not Create While Dreaming Because Attraction Stops in Sleep",
          '["Book 1, Part II"]',
          "a specific, narrower claim about the dream state",
          'You are not attracting or creating while you sleep; consciousness withdraws from physical time-space reality. Dreams instead "give you a glimpse into what you have created or... are in the process of creating."',
          '"While you sleep, you have withdrawn your consciousness from your physical time-space reality, and you are temporarily not attracting." Sleep is therefore "Realignment-of-Energies Time," when the Inner Being "realigns your Energies" and the body is refreshed; "awaking in the morning is not so different from being born."',
          'Makes sleep a deliberate tool: bedtime appreciation + morning basking resets the [[{0}]] for a higher-vibration day.'.format(C_SETPOINT),
          [C_SETPOINT, C_WELLBEING, C_EGS])


if __name__ == "__main__":
    source_page()
    persons()
    group()
    concepts()
    claims()
    print("Abraham-Hicks ingest complete.")
