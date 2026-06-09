#!/usr/bin/env python3
"""Content payload for the Coulthart *In Plain Sight* ingest.

Kept separate from the template helpers (bulk_ingest_coulthart.py) so the
prose can be edited without touching the writer logic.
"""
from pathlib import Path
from textwrap import dedent

WIKI = Path(__file__).resolve().parent.parent / "wiki"
TODAY = "2026-06-07"
SOURCE = "[[In Plain Sight: An Investigation into UFOs and Impossible Science (Coulthart, 2021)]]"

# ---------------------------------------------------------------------------
# Source page + chapter notes (written verbatim)
# ---------------------------------------------------------------------------

SOURCE_PAGE = dedent(f"""\
---
title: "In Plain Sight: An Investigation into UFOs and Impossible Science (Coulthart, 2021)"
type: source
source_type: secondary_journalistic
author_or_origin:
- Ross Coulthart
date_composed:
- "2021"
language_original:
- English
last_updated: {TODAY}
tags: [source, source/coulthart-2021, topic/ufo-disclosure]
---

## Source Description

*In Plain Sight* (HarperCollins, 2021) is a book-length investigation by
Australian investigative journalist Ross Coulthart into Unidentified Aerial
Phenomena (UAP, the author's preferred term over "UFO"). Coulthart is a
veteran television reporter (ABC *Four Corners*, Seven and Nine Network
current affairs) who frames the book as the work of a professional sceptic
who set out to test, rather than promote, claims of a UAP cover-up.

The book combines: (1) declassified Australian, US, UK and Soviet government
files; (2) Coulthart's own interviews with named and anonymous military,
intelligence and aerospace insiders; and (3) close re-examination of
historically significant sighting cases. Throughout, Coulthart distinguishes
between firsthand witness evidence he finds credible and secondhand or
hearsay claims he flags as unproven — a distinction preserved in the extracted
pages.

A recurring thesis is that, while the US Air Force publicly debunked UAPs for
decades (Project Sign → Grudge → Blue Book → the Condon Report), the same
governments privately treated the phenomenon as a serious national-security
matter, and that some advanced craft of unknown origin operate "in plain
sight" in the world's skies, oceans and orbit.

## What the Source Contributes

- Detailed Australian and New Zealand UAP cases largely absent from US-centric
  accounts: North West Cape / Harold E. Holt station (1973, 1987, 1990, 1991),
  Woomera (1950s), the Westall mass sighting (1966), Tully (1966) and the
  Kaikoura radar-visual case (1978).
- The career of Australian defence scientist Harry Turner, who concluded
  internally that RAAF sighting data was "suggestive of extra-terrestrial
  origin" and alleged a deliberate US ridicule policy.
- Firsthand interviews on the 2004 USS *Nimitz* "Tic Tac" encounter (Kevin Day,
  Gary Voorhis) and the 2014–15 USS *Theodore Roosevelt* encounters.
- The Daniel Sheehan account of viewing a classified Project Blue Book photo of
  a crashed disc in 1977, and the claim that the CIA refused President Carter a
  UAP briefing.
- Reconstruction of the Tom DeLonge / To The Stars Academy story and the leaked
  John Podesta emails that corroborate DeLonge's meetings with US Air Force
  generals and a Lockheed Skunk Works executive.
- The "Admiral Wilson Memo" / "EWD Notes" recovered from the estate of
  astronaut Edgar Mitchell, and the competing on-record statements about it.
- Firsthand interviews with former US Navy science chief Nat Kobitz, who said
  he was "read into" a crash-retrieval program and shown anomalous metal at
  Wright-Patterson.
- Analysis of the Salvatore Pais US Navy patents (inertial mass reduction
  device, room-temperature superconductor, gravity-wave craft).
- The "Art's Parts" metamaterial samples and the TTSA / US Army CRADA.

## Key Claims Extracted

- [[Annie Farinaccio saw a triangular craft at North West Cape in 1991 and was interrogated by US personnel]]
- [[A black sphere was reported over North West Cape during the 1973 DEFCON-3 alert by two witnesses]]
- [[The 1946 Swedish ghost rockets were judged beyond any known earthly culture]]
- [[Nathan Twining's 1947 memo called the flying discs real and not visionary or fictitious]]
- [[Project Sign's 1948 Estimate of the Situation concluded UAPs were interplanetary]]
- [[The Wilbert Smith memo recorded flying saucers as more classified than the H-bomb]]
- [[A 1956 US Air Force cable reported a recovered flying saucer in Afghanistan]]
- [[Project Moon Dust was a covert US program to recover unidentified objects and space debris]]
- [[Bob Jacobs filmed a UFO disabling a dummy warhead over Big Sur in 1964]]
- [[The Westall school incident was witnessed by over 100 people and followed by an official cover-up]]
- [[Harry Turner concluded RAAF sighting data was suggestive of extra-terrestrial origin]]
- [[The Kaikoura objects were tracked on radar and filmed and remain officially unexplained]]
- [[Daniel Sheehan says he viewed a classified Blue Book photo of a crashed disc in 1977]]
- [[The CIA confiscated radar evidence after the JAL flight 1628 sighting in 1986]]
- [[The Belgian Wave involved triangular craft tracked by F-16 radar]]
- [[Ben Rich told associates Skunk Works had technology to take ET home]]
- [[US sensors track Fast Walkers entering the atmosphere from space]]
- [[Kevin Day says some Tic Tac objects came from orbit and the radio comms were wiped]]
- [[NIDS investigated paranormal phenomena and cattle mutilations at Skinwalker Ranch]]
- [[Harry Reid says he was told for decades that Lockheed held retrieved UAP materials]]
- [[Eric Davis briefed a Defence agency that the US holds off-world vehicles not made on this earth]]
- [[Tom DeLonge says senior officials told him the US found a lifeform during the Cold War]]
- [[The leaked Podesta emails corroborate DeLonge's meetings with generals and a Lockheed executive]]
- [[The Admiral Wilson Memo describes a reverse-engineering program working on craft not made by human hands]]
- [[At the 1997 Pentagon briefing Admiral Wilson was told he had no need to know about a UAP program]]
- [[Nat Kobitz said he was read into a crash-retrieval program and shown integral-cast metal at Wright-Patterson]]
- [[Salvatore Pais filed US Navy patents the Navy vouched were operable]]
- [[The Art's Parts metamaterial samples are being analysed by the US Army under a CRADA with TTSA]]
- [[Edgar Mitchell privately said he filmed anomalous blue lights on Apollo 14]]
- [[The US Navy formally declared the Tic Tac Gimbal and Go Fast videos unidentified in 2019]]

## Internal Tensions

- Coulthart is openly sceptical of many claims he reports (e.g. Steven Greer's
  "death ray" allegations, the "Art's Parts" provenance, Annie Jacobsen's
  Nazi-Roswell thesis, the Aztec crash) and labels them implausible or
  unproven even while documenting them. These authorial caveats are part of the
  source and are retained.
- Several central claims rest on single sources who are now dead (Nat Kobitz,
  Edgar Mitchell) or anonymous, which the author acknowledges he cannot
  independently verify.
- The book presents directly contradictory on-record statements (e.g. Admiral
  Thomas Wilson's denial vs. Davis/Puthoff's near-confirmations of the Wilson
  Memo); these are recorded separately on the relevant controversy pages
  without adjudication.
""")

CHAPTER_NOTES = dedent(f"""\
---
title: "Coulthart In Plain Sight — Chapter Notes (All Chapters)"
type: source
source_type: secondary_journalistic
author_or_origin:
- Ross Coulthart
date_composed:
- "2021"
language_original:
- English
last_updated: {TODAY}
tags: [source, chapter-ingest, topic/ufo-disclosure]
---

Parent source: {SOURCE}

---

## Prologue

Opens with Annie Farinaccio's late-1991 sighting of a diamond/triangular craft
near the US Naval Communication Station Harold E. Holt at North West Cape, WA,
and her subsequent interrogation by US personnel. Frames the book's thesis:
governments take UAPs seriously in private while ridiculing them in public.

**Claims:** [[Annie Farinaccio saw a triangular craft at North West Cape in 1991 and was interrogated by US personnel]]

---

## Chapter 1 — Let's Hope They're Friendly

Australian/NZ sighting history: Aboriginal Min Min lights and Wandjina imagery;
RAAF Squadron Leader (later Air Marshal Sir) George Jones investigating 1930
Warrnambool "mystery aircraft"; Francis Chichester's 1931 Tasman sighting;
Frederick Valentich's 1978 disappearance over Bass Strait; the Kaikoura case
(developed later). Coulthart's evolution from Asimov-quoting sceptic.

---

## Chapter 2 — Roswell: Implausible Denials

Foo Fighters; 1946 Swedish ghost rockets; February 1947 southern-Australia
"five egg-shaped craft" sightings; Kenneth Arnold (June 1947); the Roswell
crash and the US Air Force's four shifting explanations; Jesse Marcel; Walter
Haut's 2002 deathbed affidavit; Donald Menzel's secret NSA/CIA ties.

**Claims:** [[The 1946 Swedish ghost rockets were judged beyond any known earthly culture]]
**Events:** [[Roswell crash (July 1947)]]

---

## Chapter 3 — The Launch of Project Blue Book

Nathan Twining's 1947 memo; Project Sign's "Estimate of the Situation"
(Ruppelt); the Guy Hottel FBI memo (1950); the Wilbert Smith / Robert
Sarbacher memo (1950); 1952 Washington DC flap; the Robertson Panel; Project
Grudge → Blue Book; J. Allen Hynek's "it can't be, therefore it isn't".

**Claims:** [[Nathan Twining's 1947 memo called the flying discs real and not visionary or fictitious]], [[Project Sign's 1948 Estimate of the Situation concluded UAPs were interplanetary]], [[The Wilbert Smith memo recorded flying saucers as more classified than the H-bomb]]

---

## Chapter 4 — A Worldwide Phenomenon

Senator Richard Russell's 1955 Soviet train sighting; the 1956 RAF
Bentwaters–Lakenheath radar-visual case; the 1956 Kabul/Afghanistan US Air
Force "recovered flying saucer" cable; Woomera Rocket Range sightings; Harry
Turner's 1954 classified review for DAFI; NICAP and the disclosure activism of
former CIA Director Roscoe Hillenkoetter.

**Claims:** [[A 1956 US Air Force cable reported a recovered flying saucer in Afghanistan]], [[Harry Turner concluded RAAF sighting data was suggestive of extra-terrestrial origin]]

---

## Chapter 5 — Hard Evidence

The 4602d Air Intelligence Service Squadron, Project Moon Dust and Operation
Blue Fly; Bob Jacobs' 1964 Big Sur film of a UFO disabling a dummy warhead
(Major Mansmann's corroboration); Lonnie Zamora (Socorro 1964); Kecksburg
(1965); the Westall school mass sighting (1966); the Condon Report.

**Claims:** [[Project Moon Dust was a covert US program to recover unidentified objects and space debris]], [[Bob Jacobs filmed a UFO disabling a dummy warhead over Big Sur in 1964]], [[The Westall school incident was witnessed by over 100 people and followed by an official cover-up]]

---

## Chapter 6 — Cracking the Cover-up

Harry Turner's 1971 paper alleging a deliberate US ridicule policy; the October
1973 North West Cape black-sphere sighting during the DEFCON-3 alert (Bill Lynn
and Lt Cdr Moyer/Meyer); Daniel Sheehan's 1977 viewing of a classified Blue
Book crash photo and the claim the CIA refused President Carter a briefing.

**Claims:** [[A black sphere was reported over North West Cape during the 1973 DEFCON-3 alert by two witnesses]], [[Daniel Sheehan says he viewed a classified Blue Book photo of a crashed disc in 1977]]

---

## Chapter 7 — Confusion or Cover-up?

Kaikoura (1978) re-examined via air-traffic controller John Cordy and reporter
Dennis Grant; Rendlesham Forest (1980); the Cash-Landrum case (1980); JAL
flight 1628 (1986) and John Callahan's account of CIA confiscation of the radar
data; the 1987 Learmonth SAS sighting; Soviet UAP programs (Colonel Sokolov).

**Claims:** [[The Kaikoura objects were tracked on radar and filmed and remain officially unexplained]], [[The CIA confiscated radar evidence after the JAL flight 1628 sighting in 1986]]
**Events:** [[Rendlesham Forest UAP incident (December 1980)]]

---

## Chapter 8 — The Black Triangles

The Belgian Wave (1989–90) and Colonel Wilfried De Brouwer; UK triangle waves
(1993); Christopher Mellon's investigation finding no US triangular program;
Ben Rich's Skunk Works remarks; Bob Lazar; the 1991 Pine Gap "Fast Walker"
tracked via Bob Fish / Podesta emails; Dick D'Amato's cover-up suspicions.

**Claims:** [[The Belgian Wave involved triangular craft tracked by F-16 radar]], [[Ben Rich told associates Skunk Works had technology to take ET home]], [[US sensors track Fast Walkers entering the atmosphere from space]]

---

## Chapter 9 — The Disclosure Project

Clinton, Webster Hubbell and Laurance Rockefeller; Steven Greer, CSETI and the
Disclosure Project; the April 1997 Pentagon briefing of Admiral Thomas Wilson
with Edgar Mitchell; the leaked NRO codename document; the Phoenix Lights
(1997); John Podesta's public calls for disclosure.

**Claims:** [[At the 1997 Pentagon briefing Admiral Wilson was told he had no need to know about a UAP program]]
**Events:** [[Pentagon UAP briefing of Admiral Wilson (April 1997)]]

---

## Chapter 10 — Skinwalker Ranch

The Sherman family; Robert Bigelow's purchase and the NIDS investigation (Eric
Davis, Colm Kelleher, John Alexander); cattle mutilations across the US and
Australia (Cloverly Station); the Dulce, NM material and the Bennewitz/Doty
disinformation episode.

**Claims:** [[NIDS investigated paranormal phenomena and cattle mutilations at Skinwalker Ranch]]

---

## Chapter 11 — Tic Tacs from Space

The 2004 USS *Nimitz* encounter via Kevin Day, Gary Voorhis, David Fravor and
Chad Underwood; the claim some objects came from orbit; the wiped radio comms
and confiscated data drives.

**Claims:** [[Kevin Day says some Tic Tac objects came from orbit and the radio comms were wiped]]
**Events:** [[USS Nimitz Tic Tac encounter (November 2004)]]

---

## Chapter 12 — The Hunt for 'The Big Secret'

Harry Reid, Daniel Inouye and Ted Stevens fund AAWSAP/AATIP ($22M); Bigelow
and BAASS; Eric Davis's crash-retrieval claims (Roswell, Del Rio, Aztec); Reid
on Lockheed holding retrieved materials.

**Claims:** [[Harry Reid says he was told for decades that Lockheed held retrieved UAP materials]], [[Eric Davis briefed a Defence agency that the US holds off-world vehicles not made on this earth]]

---

## Chapter 13 — Would the President Know?

The 2011 Obama White House denial; Annie Jacobsen's Nazi-Roswell thesis;
Podesta's 2015 "biggest failure" tweet; Tom DeLonge's desert CE-5 experience
and his Skunk Works pitch; "It was the Cold War and we found a lifeform."

**Claims:** [[Tom DeLonge says senior officials told him the US found a lifeform during the Cold War]]

---

## Chapter 14 — We Can Handle the Truth

DeLonge's Joe Rogan and George Knapp interviews; claims of recovered craft and
aliens, anti-gravity, free energy, "The Others", and an international cover-up.
Coulthart repeatedly flags the claims as implausible while documenting them.

---

## Chapter 15 — Sharing the Guilty Secret

The GRU Fancy Bear hack of John Podesta; the leaked emails corroborating
DeLonge's contact with Major Generals Michael Carey and Neil McCasland,
Skunk Works' Rob Weiss and Podesta; the founding of TTSA.

**Claims:** [[The leaked Podesta emails corroborate DeLonge's meetings with generals and a Lockheed executive]]

---

## Chapter 16 — To The Stars Academy of Arts & Sciences

The October 2017 TTSA launch (Semivan, Puthoff, Justice, Mellon, Elizondo);
the December 2017 *New York Times* story; Elizondo's "we may not be alone";
TTSA's release of the Tic Tac, Gimbal and Go Fast videos.

---

## Chapter 17 — Verified Unidentified

The 2014–15 USS *Theodore Roosevelt* encounters (Ryan Graves, Danny Aucoin);
the "cube in a sphere"; the Navy's September 2019 admission the videos are
"unidentified"; the ONI FOIA refusal; the Five Observables.

**Claims:** [[The US Navy formally declared the Tic Tac Gimbal and Go Fast videos unidentified in 2019]]
**Events:** [[USS Roosevelt UAP encounters (2014–2015)]]

---

## Chapter 18 — Art's Parts

The "anonymous sergeant" letters to Art Bell (1996) and the bismuth/
magnesium-zinc samples; Linda Moulton Howe; sceptical objections (car-radiator
louvres, Betterton-Kroll slag); the 2019 TTSA / US Army CRADA.

**Claims:** [[The Art's Parts metamaterial samples are being analysed by the US Army under a CRADA with TTSA]]

---

## Chapter 19 — The New Science of Metamaterials

Sir John Pendry and real metamaterials; Puthoff's shifting assessments of the
Art's Parts samples; TTSA's CIA-heavy roster; the malachite stock-image
gaffe; Elizondo and Davis on recovered "off-world" hardware.

---

## Chapter 20 — The Astronaut and 'the Spaceman'

Edgar Mitchell via the anonymous "Spaceman"; Mitchell's private claim he filmed
anomalous blue lights on Apollo 14 and his one-word answer "Treason"; the
Mitchell archive; the AATIP "DoD Threat Scenario" briefing slides on Mellon's
website; Mitchell's 1997 fax to Senator Strom Thurmond backing Philip Corso.

**Claims:** [[Edgar Mitchell privately said he filmed anomalous blue lights on Apollo 14]]

---

## Chapter 21 — Not Made by Human Hands

The "Admiral Wilson Memo" / "EWD Notes" recovered from Mitchell's archive;
its claims of a contractor-held reverse-engineering program of craft "not made
by human hands"; Admiral Wilson's denial; the qualified statements of Davis,
Puthoff and Oke Shannon.

**Claims:** [[The Admiral Wilson Memo describes a reverse-engineering program working on craft not made by human hands]]

---

## Chapter 22 — Gordon Novel: Fact or Fiction

The Fluxliner / Alien Reproduction Vehicle (ARV) story; Gordon Novel; the
firsthand interviews with former US Navy science chief Nat Kobitz, who said he
was read into a crash-retrieval program and shown integral-cast metal at
Wright-Patterson; Barry Goldwater and General LeMay.

**Claims:** [[Nat Kobitz said he was read into a crash-retrieval program and shown integral-cast metal at Wright-Patterson]]

---

## Chapter 23 — Dr Salvatore Pais's Puzzling Patents

The Salvatore Pais US Navy patents (inertial mass reduction craft, room-
temperature superconductor, gravity-wave generator, plasma compression fusion);
Dr James Sheehy vouching they are "operable"; Mellon's scepticism that the
craft are US-made; Nick Cook's *Hunt for Zero Point*; closing assessment.

**Claims:** [[Salvatore Pais filed US Navy patents the Navy vouched were operable]]
""")

# ---------------------------------------------------------------------------
# Persons (new pages only; existing pages are linked, not recreated)
# ---------------------------------------------------------------------------

PERSONS = [
    ("Ross Coulthart (journalist)", "ross-coulthart-journalist", [],
     ["investigative journalist", "author"],
     "Australian investigative journalist and author of *In Plain Sight* (2021). "
     "A career television reporter (ABC *Four Corners*, Seven and Nine Network), "
     "Coulthart presents himself in the source as a professional sceptic who was "
     "encouraged by Australian Air Force contacts in the early 1990s to "
     "reconsider his dismissive attitude to UAPs. The book is built from "
     "declassified files and his own interviews with named and anonymous "
     "military, intelligence and aerospace insiders.",
     []),
    ("Tom DeLonge (musician)", "tom-delonge-musician", ["Blink-182"],
     ["musician", "UAP disclosure activist", "TTSA co-founder"],
     "Punk-pop musician (Blink-182) who left the band in 2015 to pursue UAP "
     "research and founded [[To The Stars Academy (TTSA)]]. Coulthart argues "
     "that, however implausible his account sounds, DeLonge demonstrably met "
     "very senior US Air Force generals, a Lockheed Skunk Works executive and "
     "John Podesta — meetings later corroborated by the leaked Podesta emails. "
     "DeLonge claims senior officials briefed him that the US recovered alien "
     "craft and a 'lifeform' during the Cold War.",
     ["To The Stars Academy (TTSA)", "John Podesta (political adviser)",
      "Steve Justice (aerospace engineer)"]),
    ("Edgar Mitchell (Apollo 14 astronaut)", "edgar-mitchell-astronaut",
     ["Ed Mitchell"],
     ["astronaut", "Apollo 14 lunar module pilot", "UAP researcher"],
     "Sixth man to walk on the Moon (Apollo 14, 1971) and later a proponent of "
     "UAP research who sat on the science advisory board of [[National Institute "
     "for Discovery Science (NIDS)]]. Coulthart's source 'the Spaceman' says "
     "Mitchell privately confided he filmed anomalous blue lights on Apollo 14 "
     "and answered 'Treason' when asked why astronauts stayed silent. Mitchell's "
     "estate is the provenance of the 'Admiral Wilson Memo'. He died February "
     "2016.",
     ["National Institute for Discovery Science (NIDS)",
      "Admiral Wilson Memo (EWD Notes)"]),
    ("Nat Kobitz (US Navy science chief)", "nat-kobitz-navy-science", [],
     ["Director of Science and Technology Development, US Navy", "engineer"],
     "Former Director of Science and Technology Development for the US Navy "
     "(retired 1994), interviewed by Coulthart in early 2020 shortly before his "
     "death in April 2020. Kobitz said he was 'read into' a program involving "
     "crashed UFOs, that the US had recovered alien spacecraft 'several times', "
     "and that he was shown an anomalous piece of metal at Wright-Patterson "
     "whose bond appeared integral/cast rather than welded. Coulthart treats him "
     "as a credible, named insider.",
     ["Nat Kobitz said he was read into a crash-retrieval program and shown integral-cast metal at Wright-Patterson",
      "Wright-Patterson Air Force Base"]),
    ("Thomas Wilson (Vice Admiral)", "thomas-wilson-admiral",
     ["Tom Wilson"],
     ["Vice Admiral, US Navy", "Deputy Director, Defence Intelligence Agency"],
     "Career US Navy intelligence officer who, as Deputy Director of the Defence "
     "Intelligence Agency, took the April 1997 Pentagon meeting with Steven "
     "Greer and Edgar Mitchell. The disclosure activists say Wilson admitted he "
     "was blocked from a contractor-run UAP program ('you don't have a need to "
     "know'); the 'Admiral Wilson Memo' attributes the same account to a 2002 "
     "meeting with Eric Davis. Wilson has categorically denied the 2002 meeting "
     "ever happened and called the memo 'pure fiction'.",
     ["At the 1997 Pentagon briefing Admiral Wilson was told he had no need to know about a UAP program",
      "Admiral Wilson Memo (EWD Notes)"]),
    ("Steven Greer (disclosure activist)", "steven-greer-disclosure", [],
     ["emergency physician", "CSETI founder", "Disclosure Project founder"],
     "Emergency physician who founded CSETI (1990) and the Disclosure Project "
     "(1992). Greer organised the April 1997 Pentagon briefing of Admiral Wilson "
     "and the 2001 National Press Club disclosure event. Coulthart credits his "
     "access but is openly sceptical of his more extreme claims (an electromagnetic "
     "'death ray' from Utah, assassination plots) and notes Greer's habit of "
     "publicly naming officials who spoke with him.",
     ["The Disclosure Project (CSETI)",
      "At the 1997 Pentagon briefing Admiral Wilson was told he had no need to know about a UAP program"]),
    ("Daniel Sheehan (attorney)", "daniel-sheehan-attorney", [],
     ["civil-rights attorney", "Jesuit general counsel"],
     "Prominent US civil-rights attorney (Pentagon Papers, Watergate, Karen "
     "Silkwood, Iran-Contra) who, as Jesuit general counsel in 1977, says he was "
     "permitted to view classified Project Blue Book microfiche and saw a "
     "photograph of a crashed domed disc in a snowy field with etched symbols. "
     "He alleges the CIA refused President Carter a UAP briefing. He later "
     "vetted witnesses for the Disclosure Project.",
     ["Daniel Sheehan says he viewed a classified Blue Book photo of a crashed disc in 1977"]),
    ("Salvatore Pais (US Navy engineer)", "salvatore-pais-engineer", [],
     ["aerospace engineer, Naval Air Warfare Center"],
     "US Navy aerospace engineer at the Naval Air Warfare Center Aircraft "
     "Division who filed a series of exotic patents (2016–2019) assigned to the "
     "Navy: an inertial-mass-reduction 'hybrid craft', a room-temperature "
     "superconductor, a high-frequency gravitational-wave generator and a plasma "
     "compression fusion device. The Navy's Dr James Sheehy vouched to the "
     "Patent Office that several were 'operable'. Coulthart and the physicists he "
     "consulted remain deeply sceptical.",
     ["Salvatore Pais filed US Navy patents the Navy vouched were operable"]),
    ("Charles Halt (USAF colonel)", "charles-halt-usaf-colonel", [],
     ["US Air Force colonel", "deputy base commander RAF Bentwaters"],
     "Deputy commander of RAF Bentwaters who led a patrol into Rendlesham Forest "
     "in December 1980 and audiotaped his commentary of a luminous object that "
     "'danced about' and shone beams into the nuclear weapons storage area. "
     "Interviewed by Coulthart in 2009, Halt remained adamant the object was "
     "intelligently controlled and probably non-human, and that there was an "
     "official cover-up.",
     ["Rendlesham Forest UAP incident (December 1980)"]),
    ("Harry Turner (Australian defence scientist)", "harry-turner-defence-scientist",
     ["Oliver Harry Turner"],
     ["nuclear physicist", "Australian defence/intelligence scientist"],
     "Melbourne nuclear physicist hired by Australia's Directorate of Air Force "
     "Intelligence (DAFI) in 1954 to review UAP sightings; he concluded the RAAF "
     "evidence was 'suggestive of extra-terrestrial origin'. As head of the "
     "nuclear-science section of the Joint Intelligence Bureau's DSTI, his 1971 "
     "paper alleged a deliberate US ridicule policy and proposed an Australian "
     "rapid-intervention team. He also investigated sightings at Maralinga while "
     "serving as a health physics officer on the British nuclear tests.",
     ["Harry Turner concluded RAAF sighting data was suggestive of extra-terrestrial origin",
      "Woomera Rocket Range"]),
    ("John Podesta (political adviser)", "john-podesta-adviser", [],
     ["White House Chief of Staff", "presidential counsellor"],
     "Senior US political adviser (Clinton White House Chief of Staff; Obama "
     "counsellor; Hillary Clinton 2016 campaign chairman) and a long-standing "
     "public advocate for UAP disclosure. His Gmail account was hacked by the GRU "
     "in 2016 and dumped by WikiLeaks; the leaked emails corroborate Tom "
     "DeLonge's meetings with US Air Force generals and a Lockheed executive, and "
     "include the 'Fast Walkers' correspondence from Bob Fish.",
     ["The leaked Podesta emails corroborate DeLonge's meetings with generals and a Lockheed executive",
      "US sensors track Fast Walkers entering the atmosphere from space"]),
    ("Bob Fish (defence intelligence insider)", "bob-fish-intelligence-insider", [],
     ["defence communications intelligence insider"],
     "Former highly-cleared US defence communications-intelligence specialist who "
     "emailed John Podesta about 'Fast Walkers' — objects detected entering "
     "Earth's atmosphere from space by Defense Support Program satellites — and "
     "who told Coulthart the US tracks high-Mach UAPs by their electromagnetic "
     "signature without attacking them. He described a 1991 controlled descent "
     "tracked during the run-up to the Iraq War.",
     ["US sensors track Fast Walkers entering the atmosphere from space",
      "Joint Defence Facility Pine Gap"]),
    ("Annie Farinaccio (Exmouth witness)", "annie-farinaccio-witness", [],
     ["UAP witness"],
     "Exmouth (WA) local who, in late 1991, says she and two Australian "
     "Federal Protective Service officers saw a low diamond/triangular craft near "
     "the US Naval Communication Station Harold E. Holt, and who was subsequently "
     "taken onto the base and interrogated by US personnel who tried to persuade "
     "her she had seen a weather balloon. The book's prologue.",
     ["Annie Farinaccio saw a triangular craft at North West Cape in 1991 and was interrogated by US personnel",
      "Harold E. Holt Naval Communication Station (North West Cape)"]),
    ("Kevin Day (US Navy senior chief)", "kevin-day-navy-senior-chief", [],
     ["Operations Specialist Senior Chief, USS Princeton"],
     "Senior radar operator aboard the USS *Princeton* who coordinated air "
     "defence for the *Nimitz* carrier group during the November 2004 Tic Tac "
     "encounter. He tracked clusters of objects descending from above 80,000 "
     "feet, told Coulthart some objects 'came from orbit', and said the radio "
     "comms recording was found wiped the next morning.",
     ["Kevin Day says some Tic Tac objects came from orbit and the radio comms were wiped",
      "USS Nimitz Tic Tac encounter (November 2004)"]),
    ("Wilbert Smith (Canadian engineer)", "wilbert-smith-engineer", [],
     ["radio engineer, Canadian Department of Transport"],
     "Senior Canadian government radio engineer who, in a November 1950 memo, "
     "recorded that US scientist Dr Robert Sarbacher told him flying saucers were "
     "'the most highly classified subject in the United States government, rating "
     "higher even than the H-bomb', and that a small group under Dr Vannevar Bush "
     "was studying them.",
     ["The Wilbert Smith memo recorded flying saucers as more classified than the H-bomb"]),
    ("Ben Rich (Skunk Works director)", "ben-rich-skunk-works", [],
     ["Director, Lockheed Skunk Works", "aerospace engineer"],
     "Former Director of [[Lockheed Skunk Works]] (died 1995) who repeatedly "
     "dropped remarks suggesting a major undisclosed technological breakthrough — "
     "'we have things out in the desert that are 50 years beyond what you can "
     "comprehend' and 'we now have the technology to take ET home'. Coulthart "
     "notes these may equally have been disinformation.",
     ["Ben Rich told associates Skunk Works had technology to take ET home",
      "Lockheed Skunk Works"]),
    ("Bob Jacobs (US Air Force officer)", "bob-jacobs-usaf-officer", [],
     ["1st Lieutenant, US Air Force photographic squadron"],
     "US Air Force lieutenant who in September 1964 directed telescopic filming "
     "of a dummy nuclear warhead launched from Vandenberg. The film, screened to "
     "him by Major Florenze Mansmann, showed an object circling the warhead and "
     "firing beams of light, after which the warhead tumbled. Mansmann later "
     "corroborated Jacobs' account in signed letters.",
     ["Bob Jacobs filmed a UFO disabling a dummy warhead over Big Sur in 1964",
      "Big Sur warhead film incident (September 1964)"]),
    ("Steve Justice (aerospace engineer)", "steve-justice-aerospace", [],
     ["former Director of Advanced Systems, Lockheed Skunk Works", "TTSA COO"],
     "Former director of advanced systems at Lockheed Skunk Works who became "
     "Chief Operating Officer of [[To The Stars Academy (TTSA)]], leading its "
     "aerospace division and its proposed 'Advanced Electromagnetic Vehicle'. His "
     "2021 departure from TTSA, Coulthart suggests, indicates the much-hyped "
     "metamaterials and anti-gravity propulsion claims had stalled.",
     ["To The Stars Academy (TTSA)"]),
    ("Ryan Graves (US Navy pilot)", "ryan-graves-navy-pilot", [],
     ["US Navy F/A-18 pilot, USS Theodore Roosevelt"],
     "F/A-18 Super Hornet pilot who publicly described the near-daily UAP "
     "encounters off the US east coast in 2014–15, including the 'cube inside a "
     "sphere' near-miss, and whose squadron's safety reports went unanswered. He "
     "later briefed members of Congress.",
     ["USS Roosevelt UAP encounters (2014–2015)",
      "The US Navy formally declared the Tic Tac Gimbal and Go Fast videos unidentified in 2019"]),
    ("Wilfried De Brouwer (Belgian Air Force general)", "wilfried-de-brouwer-general", [],
     ["Major General, Belgian Air Force", "Chief of Operations Division"],
     "Then chief of the Operations Division of the Belgian Air Staff (later "
     "Deputy Chief of Staff) who presented the Belgian Air Force's evidence on "
     "the 1989–90 'Belgian Wave' of triangular-craft sightings, including F-16 "
     "radar locks recording performance 'well outside the envelope of existing "
     "aircraft'.",
     ["The Belgian Wave involved triangular craft tracked by F-16 radar",
      "Belgian Wave (1989–1990)"]),
]

# ---------------------------------------------------------------------------
# Groups (new)
# ---------------------------------------------------------------------------

GROUPS = [
    ("National Institute for Discovery Science (NIDS)", "national-institute-for-discovery-science",
     "research_organisation", ["NIDS"],
     "Privately funded research organisation created by billionaire [[Robert "
     "Bigelow (aerospace entrepreneur)]] in 1995 to investigate UAPs, the "
     "paranormal and 'the physics of consciousness'. NIDS bought and ran "
     "full-time surveillance of [[Skinwalker Ranch]] from 1996 and investigated "
     "cattle mutilations across Utah, Nevada and New Mexico. Its scientists "
     "included [[Eric Davis (physicist)]], Dr Colm Kelleher and Colonel John "
     "Alexander; [[Edgar Mitchell (Apollo 14 astronaut)]] sat on its advisory "
     "board. Much of its research remains confidential.",
     ["Robert Bigelow (aerospace entrepreneur)", "Skinwalker Ranch",
      "NIDS investigated paranormal phenomena and cattle mutilations at Skinwalker Ranch"]),
    ("The Disclosure Project (CSETI)", "the-disclosure-project-cseti",
     "advocacy_organisation", ["CSETI", "Center for the Study of Extra-terrestrial Intelligence"],
     "UAP-disclosure advocacy effort founded by [[Steven Greer (disclosure "
     "activist)]] (CSETI 1990; Disclosure Project 1992) that gathered witness "
     "testimony from military and government insiders, culminating in a 2001 "
     "National Press Club event. Coulthart credits its access while doubting some "
     "of Greer's more extreme cover-up claims.",
     ["Steven Greer (disclosure activist)"]),
    ("Condon Committee (University of Colorado UFO study)", "condon-committee",
     "scientific_review_body", ["Condon Report"],
     "US Air Force–funded University of Colorado study of UFOs (1966–68) led by "
     "physicist Edward Condon, which concluded further study could not be "
     "justified. Coulthart cites Dr Robert Low's leaked memo — that 'the trick "
     "would be' to give the public the impression of a 'totally objective study' "
     "— and Harry Turner's view that the report was discredited. It nonetheless "
     "acknowledged the 1956 Bentwaters–Lakenheath case as a probable genuine UFO.",
     ["Project Blue Book (US Air Force)",
      "Harry Turner concluded RAAF sighting data was suggestive of extra-terrestrial origin"]),
    ("Robertson Panel (1953)", "robertson-panel-1953",
     "scientific_review_body", [],
     "CIA-convened panel of scientists (January 1953), chaired by physicist "
     "Howard Robertson, that recommended a public 'training and debunking' "
     "program to reduce UAP reporting. Coulthart notes the CIA Director had been "
     "privately advised that the reports indicated 'something going on that must "
     "have immediate attention', making the panel's no-threat conclusion a "
     "'cop-out'. J. Allen Hynek concluded the CIA feared UFO reports, not UFOs.",
     ["Project Blue Book (US Air Force)"]),
    ("GRU Fancy Bear (Unit 26165)", "gru-fancy-bear-unit-26165",
     "intelligence_unit", ["Fancy Bear", "APT28"],
     "Russian military-intelligence (GRU) cyber-hacking unit, led by Victor "
     "Netyksho, that spear-phished John Podesta's email in 2016. Coulthart's "
     "point is the unintended consequence: the leaked emails corroborated Tom "
     "DeLonge's claimed contacts with US generals and a Lockheed executive over "
     "UAP disclosure.",
     ["The leaked Podesta emails corroborate DeLonge's meetings with generals and a Lockheed executive",
      "John Podesta (political adviser)"]),
]

# ---------------------------------------------------------------------------
# Locations (new)
# ---------------------------------------------------------------------------

LOCATIONS = [
    ("Harold E. Holt Naval Communication Station (North West Cape)", "harold-e-holt-naval-communication-station",
     ["North West Cape", "US Naval Communication Station North West Cape", "Exmouth"],
     "US/Australian very-low-frequency naval communication station on the North "
     "West Cape near Exmouth, Western Australia, built in the mid-1960s with an "
     "original role of sending launch-code orders to US Polaris nuclear "
     "submarines. Coulthart documents repeated anomalous sightings here across "
     "decades — 1973 (black sphere during the DEFCON-3 alert), 1987 (Learmonth "
     "SAS), 1990 (massive triangle) and 1991 (Farinaccio) — arguing UAP "
     "incidents at this nuclear-linked site were consistently suppressed.",
     ["Annie Farinaccio saw a triangular craft at North West Cape in 1991 and was interrogated by US personnel",
      "A black sphere was reported over North West Cape during the 1973 DEFCON-3 alert by two witnesses"]),
    ("Joint Defence Facility Pine Gap", "joint-defence-facility-pine-gap",
     ["Pine Gap"],
     "Joint US/Australian satellite ground station 18 km south-west of Alice "
     "Springs, central Australia, that collects Defense Support Program early-"
     "warning satellite data. Coulthart reports that operators sometimes detect "
     "objects ('Fast Walkers') that are not missiles and appear to change course "
     "under intelligent control, and that military insiders described anomalous "
     "sightings over Pine Gap stretching across decades.",
     ["US sensors track Fast Walkers entering the atmosphere from space",
      "Bob Fish (defence intelligence insider)"]),
    ("Woomera Rocket Range", "woomera-rocket-range",
     ["Anglo-Australian Long Range Weapons Establishment", "RAAF Woomera Test Range"],
     "Vast (122,188 km²) remote test range in South Australia used from 1946 for "
     "British Cold War rocket and (at Maralinga) nuclear-weapon testing. "
     "Declassified RAAF files record numerous anomalous high-speed sightings here "
     "in the 1950s, including a May 1954 radar-tracked 'misty grey disc' at "
     "60,000 ft. Harry Turner cited Woomera data in support of his "
     "extra-terrestrial hypothesis.",
     ["Harry Turner concluded RAAF sighting data was suggestive of extra-terrestrial origin"]),
    ("Westall (Melbourne)", "westall-melbourne",
     ["Westall High School", "The Grange"],
     "Suburb of Melbourne, Australia, site of the 6 April 1966 Westall school "
     "incident in which more than 100 students and teachers reported silvery "
     "disc-shaped craft, one of which apparently landed in nearby bushland known "
     "as The Grange before a military presence arrived. Coulthart calls it one of "
     "the world's most-witnessed unexplained UAP sightings.",
     ["The Westall school incident was witnessed by over 100 people and followed by an official cover-up"]),
    ("Wright-Patterson Air Force Base", "wright-patterson-air-force-base",
     ["Wright Field", "Foreign Technology Division", "NASIC"],
     "US Air Force base near Dayton, Ohio, long home to the Foreign Technology "
     "Division (later folded into the National Air and Space Intelligence Center) "
     "and central to UAP lore as the alleged repository of Roswell wreckage. "
     "Coulthart's source Nat Kobitz said he was invited there as a private "
     "welding expert and shown a strange titanium-alloy fragment whose bond "
     "appeared integral/cast rather than welded.",
     ["Nat Kobitz said he was read into a crash-retrieval program and shown integral-cast metal at Wright-Patterson"]),
    ("Kaikoura (New Zealand)", "kaikoura-new-zealand",
     [],
     "Region off the north-east coast of New Zealand's South Island where, in "
     "late December 1978, glowing objects following an Argosy cargo aircraft were "
     "tracked simultaneously on Wellington radar and the aircraft's radar, seen "
     "by multiple witnesses and filmed by cameraman David Crockett. The Royal NZ "
     "Air Force attributed it to Venus and squid-boat lights; witnesses "
     "interviewed by Coulthart reject that and note key witnesses were never "
     "questioned.",
     ["The Kaikoura objects were tracked on radar and filmed and remain officially unexplained"]),
]

# ---------------------------------------------------------------------------
# Events (new)
# ---------------------------------------------------------------------------

EVENTS = [
    ("North West Cape triangular craft sighting (1991)", "north-west-cape-triangular-craft-1991",
     "late 1991", "late 1991",
     ["Annie Farinaccio (Exmouth witness)",
      "Harold E. Holt Naval Communication Station (North West Cape)"],
     "[[Harold E. Holt Naval Communication Station (North West Cape)]]",
     "About 2:30 am on the North West Cape, Annie Farinaccio and two Australian "
     "Federal Protective Service officers reported a low diamond/triangular craft "
     "with rows of lights that pursued their vehicle, shot up and down "
     "instantaneously, and appeared to land in scrub. Two days later US military "
     "police took Farinaccio onto the base where US officers and civilians "
     "pressed her to call it a weather balloon; the officers' confiscated "
     "photographs were never returned.",
     ["Annie Farinaccio saw a triangular craft at North West Cape in 1991 and was interrogated by US personnel"]),
    ("North West Cape black sphere sighting (October 1973)", "north-west-cape-black-sphere-1973",
     "1973-10-25", "1973-10-25",
     ["Harold E. Holt Naval Communication Station (North West Cape)"],
     "[[Harold E. Holt Naval Communication Station (North West Cape)]]",
     "On the evening of 25 October 1973 — hours after Kissinger raised US forces "
     "to DEFCON-3 during the Yom Kippur War — Australian fire captain Bill Lynn "
     "and a US Lt Cdr (Moyer/Meyer) independently filed RAAF 'Unusual Aerial "
     "Sighting' reports of a large black sphere hovering near the base that "
     "'accelerated beyond belief' and vanished northward. The original RAAF "
     "records later disappeared from the National Archives.",
     ["A black sphere was reported over North West Cape during the 1973 DEFCON-3 alert by two witnesses"]),
    ("Westall school incident (April 1966)", "westall-school-incident-1966",
     "1966-04-06", "1966-04-06",
     ["Westall (Melbourne)"],
     "[[Westall (Melbourne)]]",
     "On 6 April 1966 more than 100 students and teachers at Westall High School "
     "in Melbourne saw one or more silvery disc-shaped craft hover over power "
     "lines and apparently land in nearby bushland (The Grange), darting away "
     "when light aircraft approached. Military and unidentified men in suits "
     "arrived; students were warned at assembly not to talk. Researchers Shane "
     "Ryan and Bill Chalker documented well over 100 witnesses; no official "
     "explanation has ever been given.",
     ["The Westall school incident was witnessed by over 100 people and followed by an official cover-up"]),
    ("Kaikoura sightings (December 1978)", "kaikoura-sightings-1978",
     "1978-12-20", "1978-12-31",
     ["Kaikoura (New Zealand)"],
     "[[Kaikoura (New Zealand)]]",
     "On the nights of 20 and 30 December 1978, glowing objects accompanying an "
     "Argosy cargo aircraft off Kaikoura were tracked on both Wellington radar "
     "and the aircraft's radar, witnessed by crew and reporters and filmed by "
     "cameraman David Crockett. The Royal NZ Air Force quickly blamed Venus and "
     "squid-boat lights; air-traffic controller John Cordy and reporter Dennis "
     "Grant told Coulthart that explanation does not fit and that they were never "
     "interviewed.",
     ["The Kaikoura objects were tracked on radar and filmed and remain officially unexplained"]),
    ("Belgian Wave (1989–1990)", "belgian-wave-1989-1990",
     "1989-11", "1990-04",
     ["Wilfried De Brouwer (Belgian Air Force general)"],
     "Belgium",
     "From late November 1989 to April 1990, large numbers of witnesses across "
     "Belgium — including police and senior officers — reported large triangular "
     "craft with underside lights moving slowly and silently, then accelerating. "
     "F-16s scrambled and recorded radar contacts with changes in speed and "
     "altitude 'well outside the performance envelope of existing aircraft'. "
     "Officially unexplained; the US assured Belgium the craft were not American.",
     ["The Belgian Wave involved triangular craft tracked by F-16 radar"]),
    ("Phoenix Lights (March 1997)", "phoenix-lights-1997",
     "1997-03-13", "1997-03-13",
     ["Project Blue Book (US Air Force)"],
     "Phoenix, Arizona",
     "On the evening of 13 March 1997 thousands of witnesses reported a massive "
     "V-shaped formation of lights — perceived by many as a single mile-wide "
     "black craft — moving slowly and silently over Phoenix. The Air National "
     "Guard attributed it to flares; Arizona Governor Fife Symington, a former "
     "Air Force pilot, said the craft resembled no man-made object he had seen "
     "and that flares 'don't fly in formation'.",
     []),
    ("Big Sur warhead film incident (September 1964)", "big-sur-warhead-film-1964",
     "1964-09", "1964-09",
     ["Bob Jacobs (US Air Force officer)"],
     "Big Sur, California",
     "In September 1964, telescopic film directed by Lt Bob Jacobs of a dummy "
     "nuclear warhead launched from Vandenberg AFB captured an object circling "
     "the warhead at high speed and firing four beams of light, after which the "
     "warhead tumbled. Major Florenze Mansmann screened it, ordered Jacobs to "
     "say it never happened, and decades later confirmed the account in signed "
     "letters, calling the object an extra-terrestrial craft.",
     ["Bob Jacobs filmed a UFO disabling a dummy warhead over Big Sur in 1964"]),
    ("Cash-Landrum incident (December 1980)", "cash-landrum-incident-1980",
     "1980-12-29", "1980-12-29",
     [],
     "near Dayton, Texas",
     "On 29 December 1980 near Dayton, Texas, Betty Cash, Vickie Landrum and her "
     "grandson reported a huge diamond-shaped object radiating intense heat, "
     "escorted by some 23 helicopters including CH-47 Chinooks. The witnesses "
     "suffered burns and hair loss consistent with ionising radiation; their "
     "lawsuit was dismissed when the military denied the object was theirs. Eric "
     "Davis later cited the case in a paper on UAP 'mimicry'.",
     []),
    ("JAL flight 1628 sighting (November 1986)", "jal-flight-1628-sighting-1986",
     "1986-11-17", "1986-11-17",
     [],
     "near Anchorage, Alaska",
     "On 17 November 1986 the crew of Japan Airlines flight 1628 reported two "
     "glowing craft and a gigantic 'mothership' ('two times bigger than an "
     "aircraft carrier') near Anchorage. The FAA called the radar returns "
     "'clutter'; FAA division chief John Callahan said CIA agents later "
     "confiscated the radar and voice data at a Washington meeting and ordered "
     "its existence denied, but he kept copies.",
     ["The CIA confiscated radar evidence after the JAL flight 1628 sighting in 1986"]),
    ("Pentagon UAP briefing of Admiral Wilson (April 1997)", "pentagon-wilson-briefing-1997",
     "1997-04-10", "1997-04-10",
     ["Thomas Wilson (Vice Admiral)", "Steven Greer (disclosure activist)",
      "Edgar Mitchell (Apollo 14 astronaut)"],
     "The Pentagon, Washington DC",
     "On 10 April 1997 Steven Greer, Edgar Mitchell and Cmdr Willard Miller "
     "briefed Vice Admiral Thomas Wilson, then Deputy Director of the DIA. "
     "Greer's group says Wilson admitted that, after investigating codenames in a "
     "leaked NRO document, he traced a contractor-run program and was told 'you "
     "don't have a need to know'. Wilson, in a letter to Coulthart, confirmed the "
     "meeting but denied acknowledging any such program.",
     ["At the 1997 Pentagon briefing Admiral Wilson was told he had no need to know about a UAP program"]),
]

# ---------------------------------------------------------------------------
# Concepts (new)
# ---------------------------------------------------------------------------

CONCEPTS = [
    ("Metamaterials (UAP context)", "metamaterials-uap-context", [],
     "Engineered materials whose properties derive from designed nano-scale "
     "geometry rather than their base composition, pioneered by Sir John Pendry "
     "in the mid-1990s and capable of manipulating electromagnetic radiation "
     "(e.g. radar-frequency 'invisibility cloaks'). In the UAP debate the term is "
     "applied to samples such as the 'Art's Parts' bismuth/magnesium-zinc "
     "layers, with the speculative hypothesis that the right terahertz "
     "frequencies could produce anomalous effects (even levitation). Coulthart "
     "stresses no public evidence yet substantiates such claims.",
     ["Art's Parts (UAP metal samples)",
      "The Art's Parts metamaterial samples are being analysed by the US Army under a CRADA with TTSA"]),
    ("Special Access Programs (SAP, USAP, WUSAP)", "special-access-programs", [],
     "US Defence Department security framework for compartmented classified "
     "projects. A SAP is a codenamed, Sensitive Compartmented Information "
     "project; a USAP (Unacknowledged SAP) may have its very existence denied; a "
     "WUSAP (Waived USAP) has normal oversight waived and is overseen only by the "
     "Congressional 'Gang of Eight'. Coulthart uses these definitions to frame "
     "claims that a UAP reverse-engineering program could be hidden as a "
     "WUSAP beyond ordinary oversight.",
     ["The Big Secret",
      "At the 1997 Pentagon briefing Admiral Wilson was told he had no need to know about a UAP program"]),
    ("The Big Secret", "the-big-secret", [],
     "Coulthart's shorthand for the alleged, still-unproven secret that the US "
     "(and possibly Russia and China) has recovered non-human craft and is "
     "attempting to reverse-engineer them, concealed from Congress and presidents "
     "within contractor-held compartmented programs. The author repeatedly tests "
     "and qualifies the claim rather than asserting it as fact.",
     ["Special Access Programs (SAP, USAP, WUSAP)",
      "Eric Davis briefed a Defence agency that the US holds off-world vehicles not made on this earth",
      "Admiral Wilson Memo (EWD Notes)"]),
    ("Fast Walkers", "fast-walkers", [],
     "Term for objects detected passing through the field of view of Earth-"
     "observation sensors (notably Defense Support Program early-warning "
     "satellites feeding Pine Gap) that are suspected of being in orbit. The "
     "category includes ordinary debris, but Coulthart's source Bob Fish "
     "described a 1991 object that made a controlled 30-degree course correction "
     "before a controlled descent.",
     ["US sensors track Fast Walkers entering the atmosphere from space",
      "Joint Defence Facility Pine Gap"]),
    ("Project Moon Dust and Operation Blue Fly", "project-moon-dust-operation-blue-fly",
     ["Moon Dust", "Blue Fly", "4602d AISS"],
     "US Air Force programs for the covert worldwide recovery of 'descended "
     "foreign space vehicles' and unidentified objects, run via the 4602d Air "
     "Intelligence Service Squadron and tasked by the 1961 'Betz Memo'. "
     "Declassified files tie Moon Dust to sighting/recovery reports in Pakistan, "
     "Bolivia and Nepal. In 1987 the Air Force said the name 'no longer "
     "officially exists', having been replaced by a still-classified one.",
     ["Project Moon Dust was a covert US program to recover unidentified objects and space debris"]),
    ("Alien Reproduction Vehicle (Fluxliner)", "alien-reproduction-vehicle-fluxliner",
     ["ARV", "Fluxliner"],
     "Alleged US 'alien reproduction vehicle' — a back-engineered anti-gravity "
     "craft — described by illustrator Mark McCandlish at the 2001 Disclosure "
     "Project and promoted by CIA-linked operative Gordon Novel. Coulthart treats "
     "the Fluxliner story sceptically but notes that former US Navy science chief "
     "Nat Kobitz, shown McCandlish's drawing, called it a hoax while separately "
     "affirming he was read into a genuine crash-retrieval program.",
     ["Nat Kobitz said he was read into a crash-retrieval program and shown integral-cast metal at Wright-Patterson"]),
    ("Art's Parts (UAP metal samples)", "arts-parts-uap-metal-samples",
     ["Art's Parts"],
     "Layered bismuth/magnesium-zinc (and aluminium) metal samples sent "
     "anonymously to radio host Art Bell in 1996, accompanied by letters from a "
     "self-described US Army sergeant claiming they came from the 1947 Roswell "
     "craft. Coulthart finds the provenance story full of holes (a louvred piece "
     "resembling a 1925-era car-radiator fin; possible Betterton-Kroll slag) yet "
     "notes TTSA bought the samples and the US Army agreed to analyse them.",
     ["The Art's Parts metamaterial samples are being analysed by the US Army under a CRADA with TTSA",
      "Metamaterials (UAP context)"]),
    ("Admiral Wilson Memo (EWD Notes)", "admiral-wilson-memo-ewd-notes",
     ["EWD Notes", "Wilson-Davis Memo"],
     "A 15-page document (titled 'EWD Notes', for Eric W. Davis) recovered from "
     "Edgar Mitchell's estate, purporting to record an October 2002 meeting in "
     "which Admiral Thomas Wilson told Davis he had been blocked from a "
     "contractor-held program reverse-engineering technology 'not made by human "
     "hands'. Wilson denies the meeting ever happened; Davis and Puthoff have "
     "come close to confirming the document without doing so outright. Coulthart "
     "concludes it must be treated as a hoax until proven otherwise.",
     ["The Admiral Wilson Memo describes a reverse-engineering program working on craft not made by human hands",
      "Eric Davis (physicist)", "Thomas Wilson (Vice Admiral)"]),
]

# ---------------------------------------------------------------------------
# Controversies (new; ufo-disclosure topic folder)
# ---------------------------------------------------------------------------

CONTROVERSIES = [
    ("Authenticity of the Admiral Wilson Memo", "authenticity-of-the-admiral-wilson-memo",
     "Chapter 21 ('Not Made by Human Hands') and the 'EWD Notes' recovered from Edgar Mitchell's estate",
     ["Authentic: the document is a genuine record of a 2002 Wilson–Davis meeting (Eric Davis's near-confirmation; Hal Puthoff calling them 'the Wilson documents'; Oke Shannon's non-denial and apology; clear provenance through Mitchell's archive)",
      "Hoax/fiction: Admiral Thomas Wilson categorically denies the meeting ever occurred and calls the memo 'pure fiction', stating several named people in it are unknown to him",
      "Coulthart's position: must be treated as a hoax until corroborated on the record, while noting that no principal has flatly denied its authenticity except Wilson"],
     "Coulthart lays out competing on-record statements without adjudicating. He "
     "stresses that, even if authentic, the memo only records Davis's account and "
     "proves nothing on its own; and that the most credibility-straining element "
     "(a contractor volunteering program details to someone not on the 'Bigot "
     "list') is what his defence-intelligence sources flagged as least "
     "plausible.",
     ["Admiral Wilson Memo (EWD Notes)", "Thomas Wilson (Vice Admiral)",
      "Eric Davis (physicist)", "Harold Puthoff (physicist)"]),
    ("Provenance of the Art's Parts samples", "provenance-of-the-arts-parts-samples",
     "Chapters 18–19 ('Art's Parts' / 'The New Science of Metamaterials')",
     ["Authentic extra-terrestrial metamaterial: TTSA and some scientists treat the layered bismuth/magnesium-zinc as anomalous and possibly not manufacturable by known means; the US Army agreed to analyse it",
      "Mundane/hoax: a louvred sample resembles a 1925-era car-radiator fin; the layered metal may be Betterton-Kroll process slag; the anonymous 'sergeant' letters contain timeline impossibilities",
      "Coulthart's position: strongly doubts the grandfather/Roswell provenance while puzzled that the US Army gave the samples credibility via the CRADA"],
     "The dispute turns on a sample whose only origin story is anonymous letters "
     "to Art Bell, set against TTSA's later investment and the US Army CRADA. "
     "Coulthart records both the sceptical objections and the unfulfilled claims "
     "of anomalous properties (e.g. terahertz-induced levitation) for which no "
     "public evidence exists.",
     ["Art's Parts (UAP metal samples)", "Metamaterials (UAP context)",
      "The Art's Parts metamaterial samples are being analysed by the US Army under a CRADA with TTSA"]),
    ("Is TTSA a government disclosure front?", "is-ttsa-a-government-disclosure-front",
     "Chapters 16–21 (the To The Stars Academy story)",
     ["Independent advocacy: TTSA is a public-benefit company of former insiders genuinely campaigning for transparency, which flushed out the Tic Tac/Gimbal/Go Fast videos and official Navy admissions",
      "Government front / 'soft disclosure' vehicle: TTSA's CIA- and Defence-heavy roster and DeLonge's acknowledgement that it provides 'plausible deniability' suggest it may be a controlled channel to release information (or to launder back-engineered breakthroughs via the Army CRADA)",
      "Coulthart's position: undecided — notes the suspicious composition and unmet promises while crediting TTSA's concrete role in forcing official admissions"],
     "Coulthart presents the 'government front' theory as plausible speculation, "
     "not established fact, balancing TTSA's spy-heavy membership and DeLonge's "
     "own 'plausible deniability' remark against the organisation's genuine "
     "achievements in compelling the US Navy to declare the videos unidentified.",
     ["To The Stars Academy (TTSA)",
      "The US Navy formally declared the Tic Tac Gimbal and Go Fast videos unidentified in 2019",
      "The Art's Parts metamaterial samples are being analysed by the US Army under a CRADA with TTSA"]),
]


# ---------------------------------------------------------------------------
# Claims (title must match the links used elsewhere exactly)
# ---------------------------------------------------------------------------

P = lambda link: {"type": "person", "link": link}
G = lambda link: {"type": "group", "link": link}

CLAIMS = [
    ("Annie Farinaccio saw a triangular craft at North West Cape in 1991 and was interrogated by US personnel",
     "farinaccio-north-west-cape-triangular-craft-1991", "late 1991",
     [P("Annie Farinaccio (Exmouth witness)")],
     "[[Harold E. Holt Naval Communication Station (North West Cape)]]",
     '["Prologue"]', "opening case of the book",
     "Exmouth local Annie Farinaccio says she and two Australian Federal "
     "Protective Service officers saw a low diamond/triangular craft near the US "
     "naval station on the North West Cape in late 1991, and that she was later "
     "taken onto the base and pressured by US personnel to say it was a weather "
     "balloon.",
     "Coulthart records Farinaccio's account in detail, including the officer's "
     "warning 'Please shut up . . . Shut up before you get us all killed', the "
     "confiscation of the officers' photographs, and corroboration from her "
     "mother that military police came to the family home.",
     "Used in the prologue to introduce the thesis that UAP incidents at "
     "nuclear-linked sites are taken seriously in private but suppressed in "
     "public.",
     ["North West Cape triangular craft sighting (1991)",
      "Harold E. Holt Naval Communication Station (North West Cape)"]),

    ("A black sphere was reported over North West Cape during the 1973 DEFCON-3 alert by two witnesses",
     "north-west-cape-black-sphere-1973", "1973-10-25",
     [P("Harry Turner (Australian defence scientist)")],
     "[[Harold E. Holt Naval Communication Station (North West Cape)]]",
     '["Chapter 6"]', "central Australian case in Chapter 6",
     "On 25 October 1973, hours after the US went to DEFCON-3 during the Yom "
     "Kippur War, Australian fire captain Bill Lynn and a US Lt Cdr (Moyer/Meyer) "
     "independently filed RAAF sighting reports of a large stationary black sphere "
     "near the base that then accelerated 'beyond belief' and vanished northward.",
     "Coulthart quotes both reports — Lynn's ~30-ft sphere 'with a halo around "
     "the centre' and the officer's note that he could think of no conventional "
     "explanation ('Not a thing'). He notes the original 1973 records later "
     "disappeared from the National Archives, though their provenance via a "
     "1974–75 RAAF release is not in doubt.",
     "Presented as evidence of the recurring link between UAP sightings and "
     "sensitive nuclear-linked sites, and of records going missing.",
     ["North West Cape black sphere sighting (October 1973)",
      "Harold E. Holt Naval Communication Station (North West Cape)"]),

    ("The 1946 Swedish ghost rockets were judged beyond any known earthly culture",
     "swedish-ghost-rockets-1946", "February 1946",
     [G("Project Blue Book (US Air Force)")],
     "Sweden", '["Chapter 2"]', "historical context in Chapter 2",
     "Coulthart reports that in 1946 Sweden recorded more than 2,000 'ghost "
     "rocket' sightings, hundreds corroborated by radar, with objects that were "
     "silent, exhaustless and flew horizontally — leading Sweden's Air "
     "Intelligence Service to conclude they reflected technical skill beyond any "
     "known earthly culture.",
     "Quotes the Swedish assessment that 'these phenomena are obviously the "
     "result of a high technical skill which cannot be credited to any presently "
     "known culture on earth'.",
     "Part of the chapter's survey of pre-Roswell sightings establishing that "
     "anomalous objects were taken seriously by governments before 1947.",
     []),

    ("Nathan Twining's 1947 memo called the flying discs real and not visionary or fictitious",
     "twining-1947-memo-discs-real", "September 1947",
     [G("Project Blue Book (US Air Force)")],
     "United States", '["Chapter 3"]', "origin of Project Sign",
     "General Nathan Twining, head of US Air Materiel Command, wrote in September "
     "1947 that the flying-disc phenomenon was 'something real and not visionary "
     "or fictitious', describing metallic discs with extreme climb and "
     "manoeuvrability suggesting manual or remote control, and recommended a "
     "formal study — which became Project Sign.",
     "Coulthart quotes Twining's memo directly and traces its line to Project "
     "Sign (December 1947), the first formal US Air Force UAP study.",
     "Used to show that the US military privately treated the discs as real even "
     "as it prepared to debunk them publicly.",
     []),

    ("Project Sign's 1948 Estimate of the Situation concluded UAPs were interplanetary",
     "project-sign-estimate-interplanetary-1948", "1948",
     [G("Project Blue Book (US Air Force)")],
     "United States", '["Chapter 3"]', "early classified assessment",
     "Air Force officer Edward Ruppelt, later head of Project Blue Book, said he "
     "saw a classified 1948 Project Sign report — the 'Estimate of the Situation' "
     "— that concluded the best explanation for the flying-saucer sightings was "
     "that the craft were interplanetary.",
     "Coulthart quotes Ruppelt: 'The situation was the UFOs; the estimate was "
     "that they were interplanetary.' He notes any such finding was absent from "
     "the heavily redacted version released in 1987.",
     "Presented as an early instance of the gap between private assessments and "
     "the public debunking posture (Sign → Grudge → Blue Book).",
     ["Nathan Twining's 1947 memo called the flying discs real and not visionary or fictitious"]),

    ("The Wilbert Smith memo recorded flying saucers as more classified than the H-bomb",
     "wilbert-smith-memo-saucers-most-classified", "November 1950",
     [P("Wilbert Smith (Canadian engineer)")],
     "Washington DC", '["Chapter 3"]', "cited as a credible-source claim",
     "A November 1950 memo by senior Canadian government engineer Wilbert Smith "
     "recorded that US scientist Dr Robert Sarbacher told him flying saucers were "
     "'the most highly classified subject in the United States government, rating "
     "higher even than the H-bomb', that they exist, and that a small group under "
     "Dr Vannevar Bush was studying them.",
     "Coulthart quotes the memo and notes Sarbacher, before his death, wrote that "
     "recovered materials were 'extremely light and very tough' and that recovered "
     "'aliens' seemed 'constructed like certain insects'. He flags it as "
     "intriguing but ultimately hearsay.",
     "Offered as a credible-source claim that the author nonetheless classifies "
     "as unverified hearsay.",
     []),

    ("A 1956 US Air Force cable reported a recovered flying saucer in Afghanistan",
     "1956-afghanistan-recovered-saucer-cable", "January 1956",
     [G("Project Moon Dust and Operation Blue Fly")],
     "Takala, Kataghan Province, Afghanistan", '["Chapter 4"]',
     "described as an official document of undisputed provenance",
     "Coulthart reports a 1956 series of US Air Force air-attaché cables (to "
     "Wright-Patterson) stating the Governor of Kataghan Province reported a "
     "'flying saucer' — about 15 m in circumference, metal, with small thick glass "
     "windows — had landed near Takala, and that the Afghans planned to move it to "
     "Kabul.",
     "He stresses the cable's provenance 'is not in any doubt; it is an official "
     "US government document', while noting there is no record of what was "
     "ultimately found and speculating the USSR may have recovered it first.",
     "Cited among declassified files suggesting a worldwide pattern of "
     "recovered-object reports.",
     ["Project Moon Dust and Operation Blue Fly"]),

    ("Project Moon Dust was a covert US program to recover unidentified objects and space debris",
     "project-moon-dust-recovery-program", "1953–1987",
     [G("Project Moon Dust and Operation Blue Fly")],
     "United States (worldwide operations)", '["Chapter 5"]',
     "documented from declassified files",
     "Coulthart documents that the US Air Force ran the 4602d Air Intelligence "
     "Service Squadron and Project Moon Dust / Operation Blue Fly — quick-reaction "
     "teams tasked (per the 1961 'Betz Memo') to 'locate, recover and deliver "
     "descended foreign space vehicles' and unidentified objects to the Foreign "
     "Technology Division at Wright-Patterson.",
     "Declassified files tie Moon Dust to reports in Pakistan (1961), Bolivia "
     "(1979) and a disc-shaped object near Pokhara, Nepal (1968). In 1987 the Air "
     "Force said the name 'no longer officially exists', replaced by a still-"
     "classified one — which Coulthart reads as implying a successor continues.",
     "Used to argue official UAP recovery work continued after Blue Book's public "
     "closure.",
     []),

    ("Bob Jacobs filmed a UFO disabling a dummy warhead over Big Sur in 1964",
     "bob-jacobs-big-sur-warhead-film-1964", "September 1964",
     [P("Bob Jacobs (US Air Force officer)")],
     "Big Sur, California", '["Chapter 5"]', "firsthand interview case",
     "Former Air Force Lt Bob Jacobs told Coulthart that telescopic film he "
     "directed in 1964 of a dummy nuclear warhead launched from Vandenberg showed "
     "an object circle the warhead at high speed and fire four beams of light, "
     "after which the warhead tumbled and fell.",
     "Jacobs says his CO Major Mansmann ordered him never to repeat that it was a "
     "UFO and later confirmed the account in signed letters Jacobs provided to "
     "Coulthart, asserting the object was an extra-terrestrial craft using "
     "'directed energy'. Coulthart notes the viciousness of sceptics (Klass, "
     "Oberg) toward Jacobs.",
     "Presented as a firsthand, corroborated military case suggesting "
     "coordinated suppression of UAP-military interactions.",
     ["Big Sur warhead film incident (September 1964)"]),

    ("The Westall school incident was witnessed by over 100 people and followed by an official cover-up",
     "westall-school-incident-coverup-1966", "1966-04-06",
     [G("Project Blue Book (US Air Force)")],
     "[[Westall (Melbourne)]]", '["Chapter 5"]',
     "called one of the world's most-witnessed UAP cases",
     "Coulthart reports that on 6 April 1966 more than 100 students and teachers "
     "at Westall High School in Melbourne saw silvery disc-shaped craft, one of "
     "which apparently landed in nearby bushland, and that students were warned "
     "not to talk while a military presence removed soil from the site.",
     "He cites witnesses (Joy Clarke, Colin Kelly, Terry Peck, Andrew "
     "Greenwood), researcher Shane Ryan's 122 witnesses, and a former senior "
     "public servant whose Defence-scientist father wrote a secret report that "
     "'shocked and rattled him' — yet no government document on Westall has ever "
     "surfaced.",
     "Used as a strong daylight mass-witness case with evidence of an Australian "
     "official cover-up.",
     ["Westall school incident (April 1966)", "Westall (Melbourne)"]),

    ("Harry Turner concluded RAAF sighting data was suggestive of extra-terrestrial origin",
     "harry-turner-raaf-data-extraterrestrial", "1954; 1971",
     [P("Harry Turner (Australian defence scientist)")],
     "Australia", '["Chapter 4", "Chapter 6"]', "recurring Australian thread",
     "Australian defence scientist Harry Turner, hired by air-force intelligence "
     "(DAFI) in 1954 to review UAP reports, concluded the RAAF evidence 'tends to "
     "support the conclusion . . . that certain strange aircraft have been "
     "observed to behave in a manner suggestive of extra-terrestrial origin', and "
     "in a 1971 paper alleged a deliberate US ridicule policy.",
     "Coulthart quotes Turner's 1954 finding and his 1971 charge that the US "
     "'erected a façade of ridicule' partly to cover its own anti-gravity "
     "research, and that his RAAF file access and proposed rapid-intervention team "
     "were later shut down by DAFI.",
     "Anchors the book's argument that an allied government privately reached an "
     "extra-terrestrial assessment and was pressured to suppress it.",
     ["Woomera Rocket Range"]),

    ("The Kaikoura objects were tracked on radar and filmed and remain officially unexplained",
     "kaikoura-objects-radar-filmed-unexplained", "1978-12",
     [G("Project Blue Book (US Air Force)")],
     "[[Kaikoura (New Zealand)]]", '["Chapter 1", "Chapter 7"]',
     "re-examined case with new witness interviews",
     "Coulthart reports that the December 1978 Kaikoura objects were tracked "
     "simultaneously on Wellington radar and an Argosy aircraft's radar, seen by "
     "crew and reporters and filmed, and that the Royal NZ Air Force's Venus / "
     "squid-boat explanation does not fit the evidence.",
     "Air-traffic controller John Cordy ('there was nothing wrong with the "
     "radar') and reporter Dennis Grant told Coulthart the objects were solid "
     "radar targets that parallel-tracked the plane for 40 miles, and that key "
     "witnesses (including Cordy) were never interviewed by investigators.",
     "Used to show a rushed official explanation applied to a well-recorded "
     "radar-visual case.",
     ["Kaikoura sightings (December 1978)", "Kaikoura (New Zealand)"]),

    ("Daniel Sheehan says he viewed a classified Blue Book photo of a crashed disc in 1977",
     "sheehan-classified-blue-book-crash-photo-1977", "spring 1977",
     [P("Daniel Sheehan (attorney)")],
     "Library of Congress, Washington DC", '["Chapter 6"]',
     "extended firsthand interview",
     "Attorney Daniel Sheehan told Coulthart that in 1977, while assisting a "
     "Congressional Research Service inquiry for President Carter, he was allowed "
     "to view classified Project Blue Book microfiche and saw photographs of a "
     "crashed domed disc in a snowy field with etched symbols, one of which he "
     "traced onto his notepad.",
     "Sheehan recounts the cloak-and-dagger access, the ban on note-taking, and "
     "his claim that the CIA Director (George H. W. Bush) had earlier refused "
     "President-elect Carter a UAP briefing on 'need to know' grounds. Coulthart "
     "notes Sheehan has told this unchallenged for decades and that Carter/Marcia "
     "Smith never denied it.",
     "Central to the chapter's argument that even a US president was denied UAP "
     "information by the CIA.",
     []),

    ("The CIA confiscated radar evidence after the JAL flight 1628 sighting in 1986",
     "cia-confiscated-jal-1628-radar-1986", "1986-11-17",
     [G("Central Intelligence Agency")],
     "near Anchorage, Alaska", '["Chapter 7"]', "documented via Callahan",
     "Coulthart reports that after the November 1986 JAL flight 1628 sighting near "
     "Anchorage, FAA division chief John Callahan said CIA agents confiscated all "
     "the radar evidence at a Washington meeting and ordered that the meeting be "
     "denied — but that Callahan kept copies of the radar, voice and paper data.",
     "Quotes the CIA's stated rationale that revealing 'a UFO' would panic the "
     "public ('So therefore you can't talk about it'), and notes Callahan's "
     "account 'has never been challenged by any official'.",
     "Used as an explicit, on-record account of official suppression of UAP "
     "sensor evidence.",
     ["JAL flight 1628 sighting (November 1986)"]),

    ("The Belgian Wave involved triangular craft tracked by F-16 radar",
     "belgian-wave-triangular-craft-f16-radar", "1989–1990",
     [P("Wilfried De Brouwer (Belgian Air Force general)")],
     "Belgium", '["Chapter 8"]', "lead case of the 'Black Triangles' chapter",
     "Coulthart reports that during the 1989–90 Belgian Wave, large triangular "
     "craft seen by many witnesses (including police and officers) were tracked "
     "by F-16 radar showing changes in speed and altitude 'well outside the "
     "performance envelope of existing aircraft'; the case remains officially "
     "unexplained.",
     "Quotes Colonel (later Major General) Wilfried De Brouwer's Washington press "
     "account and Colonel André Almond's personal sighting, and notes the US "
     "assured Belgium the craft were not American.",
     "Anchors the chapter's question of whether some triangular craft are an "
     "undisclosed terrestrial technology or something else.",
     ["Belgian Wave (1989–1990)"]),

    ("Ben Rich told associates Skunk Works had technology to take ET home",
     "ben-rich-skunk-works-take-et-home", "c. 1993–1995",
     [P("Ben Rich (Skunk Works director)")],
     "United States", '["Chapter 8"]', "widely-cited insider remarks",
     "Coulthart reports that former Lockheed Skunk Works director Ben Rich made "
     "remarks to associates suggesting a major undisclosed breakthrough — 'we "
     "have things out in the desert that are 50 years beyond what you can "
     "comprehend' and, ending a 1993 lecture, 'we now have the technology to take "
     "ET home'.",
     "Sources include aviation writer Jim Goodall and lecture attendees Jan "
     "Harzan and T. L. Keller; Coulthart explicitly cautions the remarks may have "
     "been disinformation rather than literal truth.",
     "Used to weigh the possibility that a US contractor secretly cracked exotic "
     "propulsion, a hypothesis the author neither endorses nor dismisses.",
     ["Lockheed Skunk Works"]),

    ("US sensors track Fast Walkers entering the atmosphere from space",
     "fast-walkers-tracked-from-space", "1991 and ongoing",
     [P("Bob Fish (defence intelligence insider)")],
     "[[Joint Defence Facility Pine Gap]]", '["Chapter 8"]',
     "from the leaked Podesta emails and a direct interview",
     "Coulthart reports that US Defense Support Program satellites (feeding "
     "stations such as Pine Gap) detect objects called 'Fast Walkers', and that "
     "insider Bob Fish described a 1991 object that made a controlled 30-degree "
     "course correction before a controlled descent — implying intelligent "
     "control.",
     "Drawn from Fish's leaked emails to John Podesta and his interview with "
     "Coulthart, including a claim that a hypersonic object tracked alongside an "
     "SR-71 made a 90-degree turn at Mach 3+, and that the US tracks such craft by "
     "electromagnetic signature without attacking them.",
     "Used to argue the US quietly tracks UAPs from orbit while withholding the "
     "data.",
     ["Joint Defence Facility Pine Gap", "Fast Walkers",
      "John Podesta (political adviser)"]),

    ("Kevin Day says some Tic Tac objects came from orbit and the radio comms were wiped",
     "kevin-day-tic-tac-from-orbit-comms-wiped", "2004-11-14",
     [P("Kevin Day (US Navy senior chief)")],
     "Pacific Ocean off San Diego", '["Chapter 11"]', "firsthand interview",
     "USS *Princeton* senior radar chief Kevin Day told Coulthart that during the "
     "November 2004 Tic Tac encounter some of the objects were tracked coming "
     "'from orbit', and that the next morning the ship's stored radio "
     "communications for the encounter had been wiped while their date/time "
     "stamps remained.",
     "Day describes clusters dropping from above 80,000 ft to just above the "
     "ocean in under a second, corroboration across multiple radars, and data "
     "drives later handed to unidentified personnel who arrived by helicopter.",
     "Adds Coulthart's firsthand interviews to the well-known Tic Tac case, "
     "emphasising the orbital origin and post-event data suppression.",
     ["USS Nimitz Tic Tac encounter (November 2004)",
      "Dave Fravor (Navy pilot)"]),

    ("NIDS investigated paranormal phenomena and cattle mutilations at Skinwalker Ranch",
     "nids-skinwalker-paranormal-cattle-mutilations", "1996–2004",
     [G("National Institute for Discovery Science (NIDS)")],
     "[[Skinwalker Ranch]]", '["Chapter 10"]', "central case of Chapter 10",
     "Coulthart reports that Robert Bigelow's NIDS bought Skinwalker Ranch in "
     "1996 and ran years of surveillance, with scientists (Eric Davis, Colm "
     "Kelleher, John Alexander) reporting UAPs, a creature emerging from a glowing "
     "'tunnel of light', and surgically precise, bloodless cattle mutilations "
     "echoed across the US and Australia.",
     "He cites NIDS reports preserved in Edgar Mitchell's archive (Dulce, NM "
     "investigations; cow-pat displacement tests) and Australian rancher Mick "
     "Cook's Cloverly Station mutilations (2018–2021), while noting that the "
     "extensive camera data did not capture the most dramatic claims.",
     "Coulthart records both the witness testimony and the absence of supporting "
     "instrument data, leaving the phenomena unresolved.",
     ["Skinwalker Ranch", "National Institute for Discovery Science (NIDS)",
      "Eric Davis (physicist)", "Robert Bigelow (aerospace entrepreneur)"],
     "Coulthart notes that the large body of NIDS data (video, EM readings, soil "
     "and blood tests) 'did not support these extraordinary claims', and that "
     "sceptics attribute the events to credulous over-interpretation."),

    ("Harry Reid says he was told for decades that Lockheed held retrieved UAP materials",
     "harry-reid-lockheed-retrieved-materials", "2021 (statement)",
     [P("Harry Reid (Senator)")],
     "United States", '["Chapter 12"]', "headline admission of Chapter 12",
     "Coulthart quotes former Senator Harry Reid telling *The New Yorker* in 2021: "
     "'I was told for decades that Lockheed had some of these retrieved "
     "materials', and that the Pentagon refused to grant him the classified "
     "access he requested to examine them.",
     "Reid links this to his unsuccessful 2009 request to give AATIP Special "
     "Access Program status, and confirmed to George Knapp he knew of 'other "
     "programs . . . including different pieces of evidence'. Coulthart notes Reid, "
     "a former 'Gang of Eight' member, stopped just short of asserting the US "
     "holds alien technology.",
     "A key on-record statement from a senior senator suggesting retrieved "
     "materials are held by a contractor beyond his oversight.",
     ["Advanced Aerospace Threat Identification Program (AATIP)",
      "Special Access Programs (SAP, USAP, WUSAP)"]),

    ("Eric Davis briefed a Defence agency that the US holds off-world vehicles not made on this earth",
     "eric-davis-off-world-vehicles-briefing", "March 2020",
     [P("Eric Davis (physicist)")],
     "United States", '["Chapter 12", "Chapter 19"]',
     "repeated on-record insider claim",
     "Coulthart reports that physicist Eric Davis — a former NIDS/BAASS scientist "
     "now at the federally funded Aerospace Corporation — told *The New York "
     "Times* he gave a classified Defence Department briefing in March 2020 about "
     "retrievals from 'off-world vehicles not made on this earth', and has stated "
     "the US holds 'recovered, crashed and landed' UFO hardware it cannot "
     "replicate.",
     "Davis also told George Knapp the 2004 Tic Tac was 'a legitimate UFO . . . "
     "not a technology that is made on Earth', and endorsed the Roswell, Del Rio "
     "and (with caveats) Aztec crash-retrieval claims. Coulthart stresses Davis "
     "retains his clearances and job despite these statements.",
     "One of the book's strongest on-record insider assertions of recovered "
     "non-human technology.",
     ["Bigelow Aerospace Advanced Space Studies (BAASS)",
      "The Big Secret"]),

    ("Tom DeLonge says senior officials told him the US found a lifeform during the Cold War",
     "delonge-officials-found-a-lifeform", "c. 2015–2016",
     [P("Tom DeLonge (musician)")],
     "United States", '["Chapter 13", "Chapter 14"]',
     "the DeLonge narrative's core claim",
     "Coulthart recounts Tom DeLonge's claim that senior US officials ('The "
     "General' and others) briefed him that the US had recovered alien craft and, "
     "during the Cold War, 'found a lifeform' (which DeLonge says he was told was "
     "discovered in 1989), and that there is a secret effort to master the "
     "technology and prepare for a perceived threat.",
     "DeLonge's account (from Joe Rogan and George Knapp interviews) includes a "
     "recovered-craft origin for the 1947 creation of the US Air Force, anti-"
     "gravity and free-energy breakthroughs, and warnings about 'The Others'. "
     "Coulthart repeatedly flags the claims as implausible while arguing the "
     "briefings demonstrably happened.",
     "Coulthart separates the verified fact that DeLonge met senior officials "
     "from the unverified content of what they allegedly told him.",
     ["The leaked Podesta emails corroborate DeLonge's meetings with generals and a Lockheed executive",
      "To The Stars Academy (TTSA)"],
     "Coulthart writes that he believes the briefings happened but cannot verify "
     "their content, and that the claims may equally be a military disinformation "
     "exercise aimed at Cold War rivals."),

    ("The leaked Podesta emails corroborate DeLonge's meetings with generals and a Lockheed executive",
     "podesta-emails-corroborate-delonge-meetings", "2016",
     [P("John Podesta (political adviser)")],
     "United States", '["Chapter 15"]', "the chapter's pivotal evidence",
     "Coulthart reports that the GRU's 2016 hack of John Podesta's email, dumped "
     "by WikiLeaks, revealed exchanges proving Tom DeLonge was in contact with "
     "Podesta, two recently retired US Air Force major generals (Michael Carey "
     "and Neil McCasland) and Lockheed Skunk Works executive Rob Weiss to discuss "
     "UAP disclosure.",
     "The emails show DeLonge offering to bring 'A-level officials' to meet "
     "Podesta, McCasland's role over the Wright-Patterson laboratory, and "
     "DeLonge's claim that 'when Roswell crashed, they shipped it to . . . "
     "Wright-Patterson'. Coulthart stresses this proves the meetings, not the "
     "truth of what was said.",
     "The corroboration that elevates DeLonge's otherwise dismissible story into "
     "documented fact about who he met.",
     ["GRU Fancy Bear (Unit 26165)", "Tom DeLonge (musician)",
      "Lockheed Skunk Works"]),

    ("The Admiral Wilson Memo describes a reverse-engineering program working on craft not made by human hands",
     "admiral-wilson-memo-reverse-engineering-program", "dated October 2002",
     [P("Eric Davis (physicist)")],
     "Las Vegas, Nevada", '["Chapter 21"]', "the book's central document",
     "The 'Admiral Wilson Memo' / 'EWD Notes', recovered from Edgar Mitchell's "
     "estate, purports to record Vice Admiral Thomas Wilson telling Eric Davis in "
     "2002 that he traced a contractor-held program reverse-engineering recovered "
     "technology 'not of this Earth and not made by human hands', was refused "
     "access despite his clearances, and was threatened over his career.",
     "Coulthart summarises the 15-page document's claims (a 400–800-person 'Bigot "
     "list'; the program hidden across compartments outside normal oversight; "
     "the contractor's 'watch committee or gatekeepers') and quotes Davis and "
     "Puthoff's near-confirmations and Oke Shannon's non-denial.",
     "Coulthart concludes the memo must be treated as a hoax until corroborated "
     "on the record, and that even if authentic it only records Davis's account.",
     ["Admiral Wilson Memo (EWD Notes)", "Thomas Wilson (Vice Admiral)",
      "Authenticity of the Admiral Wilson Memo"],
     "Vice Admiral Thomas Wilson categorically denied to Coulthart that the 2002 "
     "meeting ever happened, calling the memo 'pure fiction' and stating that "
     "several people named in it are unknown to him."),

    ("At the 1997 Pentagon briefing Admiral Wilson was told he had no need to know about a UAP program",
     "1997-pentagon-wilson-no-need-to-know", "1997-04-10",
     [P("Thomas Wilson (Vice Admiral)")],
     "The Pentagon, Washington DC", '["Chapter 9"]',
     "foundational episode for the Wilson thread",
     "Coulthart reports the disclosure activists' account that, after the April "
     "1997 Pentagon briefing, DIA Deputy Director Admiral Thomas Wilson "
     "investigated codenames in a leaked NRO document, traced a contractor-run "
     "program and was told 'you don't have a need to know' — even though he was "
     "the second-most senior figure in Defence Intelligence.",
     "The account is attributed to Steven Greer and corroborated by Edgar "
     "Mitchell, Cmdr Willard Miller, Stephen Lovekin and Shari Adamiak; an aide "
     "allegedly confirmed Majestic-12 'exists'. Wilson confirmed the meeting to "
     "Coulthart but denied acknowledging any such program.",
     "Sets up the later 'Admiral Wilson Memo' controversy by establishing the "
     "1997 meeting as real.",
     ["Pentagon UAP briefing of Admiral Wilson (April 1997)",
      "Steven Greer (disclosure activist)", "Edgar Mitchell (Apollo 14 astronaut)"],
     "Admiral Wilson told Coulthart he accepted the meeting only out of courtesy "
     "to astronaut Edgar Mitchell, never acknowledged or sought access to any UAP "
     "program, and considered the rest 'poppycock'."),

    ("Nat Kobitz said he was read into a crash-retrieval program and shown integral-cast metal at Wright-Patterson",
     "nat-kobitz-crash-retrieval-wright-patterson-metal", "interviewed early 2020",
     [P("Nat Kobitz (US Navy science chief)")],
     "[[Wright-Patterson Air Force Base]]", '["Chapter 22"]',
     "the named-insider claim Coulthart found most persuasive",
     "Former US Navy Director of Science and Technology Development Nat Kobitz "
     "told Coulthart that he was 'read into' a program involving crashed UFOs, "
     "that the US had recovered alien spacecraft 'several times', and that at "
     "Wright-Patterson he was shown a ~3-by-4-ft titanium-alloy fragment whose "
     "bond to its skin appeared integral/cast rather than welded — beyond any "
     "industrial process he knew.",
     "Kobitz, terminally ill and speaking weeks before his April 2020 death, "
     "answered 'Yes, I was' when asked if he was read into a crashed-UFO program "
     "and confirmed an active back-engineering effort, while calling the "
     "Fluxliner drawing a hoax. He also put Coulthart on to a further anonymous "
     "source ('Sidewinder').",
     "Coulthart treats Kobitz as a credible, named insider and pre-empts the "
     "likely smear that he was a confused dying man.",
     ["Wright-Patterson Air Force Base",
      "Alien Reproduction Vehicle (Fluxliner)", "The Big Secret"]),

    ("Salvatore Pais filed US Navy patents the Navy vouched were operable",
     "salvatore-pais-navy-patents-operable", "2016–2019",
     [P("Salvatore Pais (US Navy engineer)")],
     "Naval Air Warfare Center, Patuxent River, Maryland", '["Chapter 23"]',
     "the closing case study",
     "Coulthart reports that US Navy engineer Dr Salvatore Pais filed patents "
     "(assigned to the Navy) for an inertial-mass-reduction 'hybrid craft', a "
     "room-temperature superconductor, a high-frequency gravitational-wave "
     "generator and a plasma compression fusion device, and that the Navy's Dr "
     "James Sheehy vouched to the Patent Office that several were 'operable'.",
     "He notes the craft patent resembles a Tic Tac/triangle, that Pais cites Hal "
     "Puthoff, and that Sheehy argued the patents should be held 'as opposed to "
     "paying forever more' if China developed the technology — while physicists "
     "Coulthart consulted, and Christopher Mellon, doubt the craft are US-made or "
     "the physics viable.",
     "Used to weigh whether the US has (or is bluffing about) anti-gravity "
     "technology; Coulthart remains sceptical.",
     ["Harold Puthoff (physicist)", "Christopher Mellon (intelligence official)"],
     "Coulthart and the scientists he consulted express grave doubts the patents "
     "describe working technology; some suggest they are filed mainly to deter "
     "Chinese or Russian claims."),

    ("The Art's Parts metamaterial samples are being analysed by the US Army under a CRADA with TTSA",
     "arts-parts-us-army-crada-ttsa", "October 2019",
     [G("To The Stars Academy (TTSA)")],
     "United States", '["Chapter 18", "Chapter 19"]',
     "the metamaterials thread",
     "Coulthart reports that in October 2019 To The Stars Academy announced a "
     "Cooperative Research and Development Agreement (CRADA) under which the US "
     "Army would analyse the 'Art's Parts' bismuth/magnesium-zinc samples and "
     "develop 'novel materials' for purposes including 'space-time metric "
     "engineering' and 'beamed energy propulsion'.",
     "TTSA's SEC filing shows DeLonge sold the samples to the company for "
     "$35,000 for Hal Puthoff to analyse; the Army's Dr Joseph Cannon called TTSA "
     "a 'non-traditional source for novel materials'. Coulthart questions why the "
     "Army would credibly analyse samples of such dubious provenance.",
     "Frames the puzzle of an official body lending credibility to samples whose "
     "extra-terrestrial origin the author doubts.",
     ["Art's Parts (UAP metal samples)", "Metamaterials (UAP context)",
      "Provenance of the Art's Parts samples"],
     "Coulthart details strong reasons to doubt the samples' provenance "
     "(resemblance to a 1925-era car-radiator fin; possible industrial slag) and "
     "notes no public evidence supports the claimed anomalous properties."),

    ("Edgar Mitchell privately said he filmed anomalous blue lights on Apollo 14",
     "edgar-mitchell-apollo-14-blue-lights", "1971 (disclosed c. 2015–2016)",
     [P("Edgar Mitchell (Apollo 14 astronaut)")],
     "Apollo 14 mission / cislunar space", '["Chapter 20"]',
     "from the 'Spaceman' source and Mitchell archive",
     "Coulthart reports that, via the anonymous 'Spaceman', astronaut Edgar "
     "Mitchell privately said in his final months that he saw and filmed "
     "anomalous well-defined blue lights during Apollo 14 — one behind him on the "
     "lunar surface and a triangular cluster beside the command module on two "
     "separate cameras — though he publicly always denied seeing a 'UFO'.",
     "Mitchell reportedly dismissed lens-flare explanations because he saw the "
     "lights with his own eyes and checked the film, and answered 'Treason' when "
     "asked why astronauts stayed silent. Coulthart stresses he could not verify "
     "this without hearing it from Mitchell directly.",
     "Presented as an unverifiable but striking deathbed account from a named "
     "astronaut, recorded with the author's caveats.",
     ["Admiral Wilson Memo (EWD Notes)",
      "National Institute for Discovery Science (NIDS)"]),

    ("The US Navy formally declared the Tic Tac Gimbal and Go Fast videos unidentified in 2019",
     "us-navy-declared-three-videos-unidentified-2019", "September 2019",
     [G("To The Stars Academy (TTSA)")],
     "United States", '["Chapter 17"]', "treated as a historic admission",
     "Coulthart reports that in September 2019 the US Navy formally stated it "
     "considers the phenomena in the three TTSA-released videos (Tic Tac/FLIR1, "
     "Gimbal and Go Fast) as 'unidentified', and that in April 2020 the Pentagon "
     "officially released them while confirming they remain unidentified.",
     "Quotes Navy spokesman Joseph Gradisher and notes the Office of Naval "
     "Intelligence later refused a FOIA request for Tic Tac records, claiming "
     "release 'would cause exceptionally grave damage to the National Security of "
     "the United States'.",
     "Marks, for Coulthart, the break with 75 years of public denial — the US "
     "military conceding on the record it cannot explain the objects.",
     ["USS Roosevelt UAP encounters (2014–2015)",
      "Five Observables (Elizondo UAP framework)",
      "Ryan Graves (US Navy pilot)"]),
]


# ---------------------------------------------------------------------------
# Writer
# ---------------------------------------------------------------------------

def run(g):
    """g is the globals() of bulk_ingest_coulthart, exposing the template fns."""
    write_if_new = g["write_if_new"]
    created = 0

    # Source pages
    created += write_if_new(WIKI / "sources" / "in-plain-sight-coulthart-2021.md", SOURCE_PAGE)
    created += write_if_new(WIKI / "sources" / "coulthart-in-plain-sight-chapters.md", CHAPTER_NOTES)

    for (title, slug, also, roles, body, related) in PERSONS:
        created += write_if_new(WIKI / "persons" / f"{slug}.md",
                                g["person_page"](title, slug, also, roles, body, related))

    for (title, slug, category, also, body, related) in GROUPS:
        created += write_if_new(WIKI / "groups" / f"{slug}.md",
                                g["group_page"](title, slug, category, also, body, related))

    for (title, slug, also, body, related) in LOCATIONS:
        created += write_if_new(WIKI / "locations" / f"{slug}.md",
                                g["location_page"](title, slug, also, body, related))

    for (title, slug, ds, de, parts, loc, overview, kc) in EVENTS:
        created += write_if_new(WIKI / "events" / "ufo-disclosure" / f"{slug}.md",
                                g["event_page"](title, slug, ds, de, parts, loc, overview, kc))

    for (title, slug, also, body, related) in CONCEPTS:
        created += write_if_new(WIKI / "concepts" / f"{slug}.md",
                                g["concept_page"](title, slug, also, body, related))

    for (title, slug, locus, positions, body, related) in CONTROVERSIES:
        created += write_if_new(WIKI / "controversies" / "ufo-disclosure" / f"{slug}.md",
                                g["controversy_page"](title, slug, locus, positions, body, related))

    for c in CLAIMS:
        title, slug, dop, actors, loc, ctx, prev, stmt, evid, ctxnote, rel = c[:11]
        opposing = c[11] if len(c) > 11 else None
        created += write_if_new(WIKI / "claims" / "ufo-disclosure" / f"{slug}.md",
                                g["claim_page"](title, slug, dop, actors, loc, ctx, prev,
                                                stmt, evid, ctxnote, rel, opposing))

    print(f"Coulthart ingest: {created} new pages written.")
