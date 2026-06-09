#!/usr/bin/env python3
"""Bulk-create wiki pages for Jacobsen Area 51 chapters 2-21."""
from pathlib import Path
from textwrap import dedent

WIKI = Path(__file__).resolve().parent.parent / "wiki"
SOURCE = "[[Area 51 — An Uncensored History of America's Top Secret Military Base (Jacobsen 2010)]]"
TODAY = "2026-06-07"


def write_if_new(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return True


def claim_page(title, slug, date_or_period, actors, location, contexts, statement, evidence, opposing=None, tags=None):
    tags = tags or ["claim", "topic/area-51"]
    actors_yaml = "\n".join(f'  - type: {a["type"]}\n    link: "[[{a["link"]}]]"' for a in actors)
    opp = ""
    if opposing:
        opp = f"\n## Opposing Information Within the Source\n\n{opposing}\n"
    return dedent(f"""\
        ---
        title: {title}
        type: claim
        date_or_period: "{date_or_period}"
        involved_actors:
        {actors_yaml}
        location: "{location}"
        source_attribution: "{SOURCE}"
        contexts: {contexts}
        prevalence_in_source: extracted from Jacobsen source
        status: extracted
        last_updated: {TODAY}
        tags: {tags}
        ---

        ## Claim Statement

        {statement}

        ## Source Attribution and Direct Evidence

        {evidence}
        {opp}
        ## Related Entities

        - {SOURCE}
    """)


def person_page(title, slug, roles, body, tags=None):
    tags = tags or ["person", "topic/area-51"]
    roles_yaml = "\n".join(f"  - {r}" for r in roles)
    return dedent(f"""\
        ---
        title: {title}
        type: person
        also_known_as: []
        roles:
        {roles_yaml}
        textual_sources:
          - "{SOURCE}"
        last_updated: {TODAY}
        tags: {tags}
        ---

        {body}

        ## Related Entities

        - {SOURCE}
    """)


def event_page(title, slug, date_start, date_end, participants, location, overview, tags=None):
    tags = tags or ["event", "topic/area-51"]
    parts = "\n".join(f'  - "[[{p}]]"' for p in participants)
    return dedent(f"""\
        ---
        title: {title}
        type: event
        date_start: "{date_start}"
        date_end: "{date_end}"
        participants:
        {parts}
        location: "{location}"
        key_claims: []
        sources_ingested: 1
        last_updated: {TODAY}
        tags: {tags}
        ---

        ## Event Overview

        {overview}

        ## Related Entities

        - {SOURCE}
    """)


def group_page(title, slug, category, body, tags=None):
    tags = tags or ["group", "topic/area-51"]
    return dedent(f"""\
        ---
        title: {title}
        type: group
        category: {category}
        also_known_as: []
        periods_active: []
        textual_sources:
          - "{SOURCE}"
        roles_significance: []
        last_updated: {TODAY}
        tags: {tags}
        ---

        {body}

        ## Related Entities

        - {SOURCE}
    """)


def location_page(title, slug, body, tags=None):
    tags = tags or ["location", "topic/area-51"]
    return dedent(f"""\
        ---
        title: {title}
        type: location
        also_known_as: []
        periods_inhabited: []
        modern_geography: []
        associated_peoples: []
        last_updated: {TODAY}
        tags: {tags}
        ---

        {body}

        ## Related Entities

        - {SOURCE}
    """)


def concept_page(title, slug, body, tags=None):
    tags = tags or ["concept", "topic/area-51"]
    return dedent(f"""\
        ---
        title: {title}
        type: concept
        also_known_as: []
        last_updated: {TODAY}
        tags: {tags}
        ---

        {body}

        ## Related Entities

        - {SOURCE}
    """)


def controversy_page(title, slug, locus, positions, body, tags=None):
    tags = tags or ["controversy", "topic/area-51"]
    pos = "\n".join(f"  - \"{p}\"" for p in positions)
    return dedent(f"""\
        ---
        title: {title}
        type: controversy
        text_locus: "{locus}"
        positions_presented:
        {pos}
        last_updated: {TODAY}
        tags: {tags}
        ---

        {body}

        ## Related Entities

        - {SOURCE}
    """)


def chapter_page(num, title, summary, claims, events, persons, groups, locations):
    slug = f"jacobsen-area-51-chapter-{num:02d}-{title.lower().replace(' ', '-').replace(chr(39), '')[:40]}"
    claims_links = "\n".join(f"- [[{c}]]" for c in claims)
    events_links = "\n".join(f"- [[{e}]]" for e in events)
    persons_links = "\n".join(f"- [[{p}]]" for p in persons)
    groups_links = "\n".join(f"- [[{g}]]" for g in groups)
    locations_links = "\n".join(f"- [[{l}]]" for l in locations)
    return dedent(f"""\
        ---
        title: "Jacobsen Area 51 — Chapter {num}: {title}"
        type: source
        source_type: secondary_scholarly
        author_or_origin:
          - Annie Jacobsen
        date_composed:
          - "2010"
        language_original:
          - English
        last_updated: {TODAY}
        tags: [source, chapter-ingest, topic/area-51]
        ---

        ## Chapter Summary

        {summary}

        Parent source: {SOURCE}

        ## Claims Extracted

        {claims_links or "- (see chapter text)"}

        ## Events

        {events_links or "- (see chapter text)"}

        ## Persons

        {persons_links or "- (see chapter text)"}

        ## Groups

        {groups_links or "- (see chapter text)"}

        ## Locations

        {locations_links or "- (see chapter text)"}
    """), slug


# --- DATA ---

CHAPTERS = [
    (2, "Imagine a War of the Worlds",
     "War of the Worlds broadcast panic; Operation Crossroads; V-2 Juárez crash; Roswell 1947; Operation Harass for Horten brothers.",
     ["Roswell craft had Cyrillic writing per Jacobsen source", "JCS replaced flying disc press release with weather balloon story",
      "Operation Harass sought Horten brothers for Roswell disc explanation"],
     ["War of the Worlds broadcast (October 1938)", "Operation Crossroads Baker shot (July 1946)", "Roswell crash (July 1947)"],
     ["Richard Leghorn (overhead espionage)", "Curtis LeMay (Cold War)", "Wernher Von Braun (Paperclip)"],
     ["Office of Policy Coordination (CIA)", "Operation Paperclip"],
     ["Bikini Atoll", "White Sands Proving Ground", "Roswell Army Air Field (1947)"]),
    (3, "The Secret Base",
     "Bissell diverts Marshall Plan funds; Groom Lake selected for U-2; Eisenhower gives CIA control; Mount Charleston crash.",
     ["Bissell diverted Marshall Plan funds to CIA covert ops", "Eisenhower chose CIA for U-2 plausible deniability",
      "Goudey first sustained flight above 65000 ft kept secret until 1998"],
     ["Mount Charleston C-54 crash (November 16, 1955)", "CIA selects Groom Lake for U-2 (1955)"],
     ["Richard Bissell (CIA)", "Kelly Johnson (Lockheed)", "Frank Wisner (CIA OPC)"],
     ["Lockheed Skunk Works", "Office of Policy Coordination (CIA)"],
     ["Groom Lake (Nevada)", "Mount Charleston (Nevada)"]),
    (4, "The Seeds of a Conspiracy",
     "U-2/Oxcart mistaken for UFOs; CIA debunking; Robertson Panel; Project Blue Book covert investigations.",
     ["Silver U-2s at 70000 ft mistaken for UFOs per Jacobsen", "By 1957 U-2s caused over 50 percent continental UFO reports per CIA monograph",
      "Air Force told Congress no UFO files existed while running covert programs"],
     ["Kenneth Arnold sighting (June 24, 1947)"],
     ["Walter Bedell Smith (CIA director)", "Todos Odarenko (CIA UFO office)"],
     ["Project Blue Book (US Air Force)", "Robertson Panel (1953)"],
     ["Area 51 (Groom Lake, Nevada)"]),
    (5, "The Need-to-Know",
     "Stockman first Soviet overflight; NII-88; Operation Home Run; dirty-bird paint crash; Sputnik.",
     ["Stockman U-2 flight proved bomber gap false July 1956", "Operation Home Run flew into Siberia not 12 miles offshore per Pizzo",
      "Dirty-bird radar paint caused Sieker fatal crash 1957"],
     ["First U-2 over Soviet Union (July 4, 1956)", "Sputnik launch (October 4, 1957)"],
     ["Hervey Stockman (U-2 pilot)", "Sergei Korolev (Soviet)"],
     ["National Reconnaissance Office", "Boston Group (MIT stealth paint)"],
     ["NII-88 Podlipki (Soviet analogue)"]),
    (6, "Atomic Accidents",
     "Project 57 dirty bomb at Area 13; Operation Plumbbob; Hood thermonuclear test evacuates Area 51.",
     ["Project 57 spread plutonium over 895 acres adjacent to Groom Lake April 1957",
      "Hood was largest continental US detonation at 74 kt July 1957", "Area 51 uninhabitable after Hood per Jacobsen"],
     ["Project 57 detonation (April 24, 1957)", "Hood thermonuclear test (July 5, 1957)"],
     ["Richard Mingus (Area 51 security)", "James Shreve Jr (Project 57 director)"],
     ["Armed Forces Special Weapons Project"],
     ["Area 13 (Project 57 site)", "Indian Springs (Nevada)"]),
    (7, "From Ghost Town to Boomtown",
     "Area 51 abandoned 1957-59; A-12 stealth development; cesium ionization; Eisenhower authorizes twelve Oxcarts.",
     ["Area 51 sat largely abandoned 1957-1959 with caretakers only", "Chines reduced A-12 radar cross section 90 percent",
      "Soviets inferred A-12 shape via infrared satellite heat signature"],
     ["CIA authorizes twelve A-12 Oxcarts (January 26, 1960)"],
     ["Edward Lovick (stealth physicist)", "Kelly Johnson (Lockheed)"],
     ["Lockheed Skunk Works"],
     ["Area 51 (Groom Lake, Nevada)"]),
    (8, "Cat and Mouse Becomes Downfall",
     "Gary Powers shootdown; Bay of Pigs; Project Palladium; Area 51 runway expansion.",
     ["Powers shot down at Kyshtym 40 May 1 1960", "Eisenhower admitted authorized espionage after cover collapsed",
      "Bay of Pigs hundreds killed 1189 imprisoned per Jacobsen"],
     ["Gary Powers U-2 shootdown (May 1, 1960)", "Bay of Pigs invasion (1961)"],
     ["Francis Gary Powers (U-2 pilot)", "Richard Bissell (CIA)", "Frank Wisner (CIA)"],
     ["Project Palladium (CIA ELINT)"],
     ["Peshawar Pakistan CIA U-2 base", "Kyshtym 40 (Soviet nuclear facility)"]),
    (9, "The Base Builds Back Up",
     "Freedman at Area 51; Kirkpatrick inspection; NRO creation; Teak Orange Argus nuclear tests in space.",
     ["NRO created September 1961 public did not know until 1992", "Teak detonated directly above Johnston Island due to rocket failure",
      "Howard Hughes had own hangar at Area 51 activity classified as of 2011"],
     ["National Reconnaissance Office creation (September 6, 1961)", "Operation Teak (August 1, 1958)", "Tsar Bomba (October 30, 1961)"],
     ["Jim Freedman (Area 51 property control)", "Lyman Kirkpatrick Jr (CIA IG)"],
     ["National Reconnaissance Office"],
     ["Johnston Atoll", "Groom Mountain"]),
    (10, "Wizards of Science Technology and Diplomacy",
     "First Oxcart flights; Wheelon Mayor of Area 51; Cuban missile crisis U-2 photography.",
     ["Wheelon became Mayor of Area 51 summer 1962", "Oct 14 1962 U-2 photos showed Soviet nuclear missiles in Cuba",
      "Ledford assessed 1 in 6 chance U-2 shootdown over Cuba"],
     ["First official Oxcart flight (1962)", "Cuban missile crisis U-2 photography (October 14, 1962)"],
     ["Bud Wheelon (CIA DS&T)", "Louis Schalk (Lockheed test pilot)", "John McCone (CIA director)"],
     ["CIA Directorate of Science and Technology"],
     ["Area 51 (Groom Lake, Nevada)", "Cuba (missile sites 1962)"]),
    (11, "What Airplane?",
     "Ken Collins crash; F-105 cover story; SR-71 designation; LBJ unaware of Area 51 as VP.",
     ["Collins Oxcart crash Wendover May 24 1963 pitot tube cause", "Press told F-105 crash still listed that way as of 2011",
      "LBJ as VP entirely unaware of A-12 and Area 51 until after JFK death"],
     ["Ken Collins Oxcart crash Wendover (May 24, 1963)", "JFK assassination notification at Area 51 (November 22, 1963)"],
     ["Kenneth Collins (Oxcart pilot)", "Robert Holbury (Area 51 commander)", "Lyndon B Johnson (president)"],
     ["1129th Special Activities Squadron"],
     ["Wendover Utah (Oxcart crash site 1963)"]),
    (12, "Covering Up the Cover-Up",
     "Oxcart UFO reports; Cronkite exposé; gorilla-mask XP-59 deception; Hillenkoetter NICAP.",
     ["A-12 generated massive UFO reports like U-2", "1942 gorilla-mask jet deception at Muroc per Jacobsen",
      "Hillenkoetter knew Roswell disc sent by Stalin per Jacobsen source"],
     ["Cronkite CBS UFO special (May 10, 1966)"],
     ["Hugh Slater (Area 51 commander)", "Roscoe Hillenkoetter (CIA/NICAP)"],
     ["NICAP (ufology organization)"],
     ["Area 51 (Groom Lake, Nevada)"]),
    (13, "Dull Dirty and Dangerous Requires Drones",
     "Black Cat U-2 losses; D-21 drone; M-21 crash; atomic cloud sampling; Ivy Mike.",
     ["Yeh Changti tortured 19 years CIA unaware he survived", "D-21 was worlds first Mach 3 stealth drone per Lovick",
      "Ivy Mike vaporized Elugelab 10.4 megaton yield"],
     ["M-21 D-21 crash Ray Torick drowned (July 30, 1966)", "Yeh Changti U-2 shootdown (November 1, 1963)"],
     ["Yeh Changti (Black Cat pilot)", "Ed Lovick (Lockheed)", "Ray Torick (M-21 flight engineer)"],
     ["Thirty-Fifth Black Cat U-2 Squadron"],
     ["Taoyuan Air Base Taiwan", "Lake Mead (Nevada)"]),
    (14, "Drama in the Desert",
     "Johnson Sputnik reaction; A-11 cover; Gulf of Tonkin; Oxcart sonic boom deaths.",
     ["Johnson vowed anti-Communist response to Sputnik Red Moon quote", "NSA admitted Gulf of Tonkin intelligence skewed 2005",
      "286 nuclear bombs exploded near Area 51 by 1964 per Jacobsen"],
     ["Johnson A-11 press conference (February 29, 1964)", "Gulf of Tonkin incident (August 1964)"],
     ["Lyndon B Johnson (president)", "Robert McNamara (SECDEF)"],
     ["303 Committee (covert action review)"],
     ["Kadena Air Base Okinawa"]),
    (15, "The Ultimate Boys Club",
     "Slater command; Walt Ray crash; Helms saves Oxcart; presidential reversal May 1967.",
     ["Walt Ray ejection seat parachute tangled faulty fuel gauge January 1967",
      "Helms only sin in espionage is getting caught quote", "President reversed Oxcart termination May 1967"],
     ["Walt Ray Oxcart crash (January 5, 1967)", "303 Committee Oxcart termination order (February 1967)"],
     ["Hugh Slater (Area 51 commander)", "Walt Ray (Oxcart pilot)", "Richard Helms (CIA director)"],
     ["303 Committee (covert action review)"],
     ["Slater Lake (Groom Lake Nevada)"]),
    (16, "Operation Black Shield and USS Pueblo",
     "Black Shield Kadena deployment; 29 Oxcart missions; Pueblo seizure; Oxcart located ship prevented war.",
     ["Oxcart located USS Pueblo prevented air attack per Rostow 1994", "29 total Oxcart missions 24 Vietnam 3 North Korea per Jacobsen",
      "SR-71 arrival ended CIA Mach 3 missions at Kadena"],
     ["Operation Black Shield begins (May 1967)", "USS Pueblo seized (January 23, 1968)", "Jack Weeks Oxcart disappearance (June 5, 1968)"],
     ["Jack Weeks (Oxcart pilot)", "Frank Murray (Oxcart pilot)", "Lloyd Bucher (USS Pueblo captain)"],
     ["1129th Special Activities Squadron"],
     ["Kadena Air Base Okinawa", "Wonsan Harbor North Korea"]),
    (17, "The MiGs of Area 51",
     "Redfa MiG-21 defection; Have Doughnut; Top Gun origin.",
     ["Redfa defected for 1 million dollars and safe haven", "Have Doughnut 102 missions six weeks per Barnes",
      "Top Gun born from MiG program established March 1969"],
     ["Munir Redfa MiG-21 defection (August 1966)", "MiG-21 arrival at Area 51 (March 1968)", "Top Gun establishment (March 1969)"],
     ["Munir Redfa (Iraqi defector)", "T D Barnes (Area 51 radar)", "Mordechai Hod (Israeli Air Force)"],
     ["Have Doughnut program (MiG evaluation)", "US Air Force Foreign Technology Division"],
     ["Tel Aviv", "Beatty Nevada"]),
    (18, "Meltdown",
     "Palomares Thule accidents; NERVA meltdowns; Cosmos 954; Clinton denied EG&G records.",
     ["Palomares 650 acres aerosolized plutonium January 1966", "Clinton denied EG&G records need-to-know 1994",
      "Cosmos 954 CIA decided not to inform public per Weiss"],
     ["Palomares nuclear accident (January 17, 1966)", "Thule B-52 crash (January 21, 1968)", "Cosmos 954 crash (January 24, 1978)"],
     ["Larry Messinger (Chrome Dome pilot)", "Mahlon E Gates (NEST founder)", "Gus Weiss (CIA analyst)"],
     ["Nuclear Emergency Search Team (NEST)"],
     ["Palomares Spain", "Area 25 Jackass Flats (NERVA)", "Thule Greenland"]),
    (19, "The Lunar-Landing Conspiracy and Other Legends",
     "Apollo 11; Kaysing hoax; tunnel conspiracies; Derry Memo; Rainier Mesa tunnels.",
     ["Armstrong landed Apollo 11 with 20 seconds fuel remaining", "Kaysing father of lunar hoax three questions",
      "Derry Memo classify to avoid embarrassment to AEC"],
     ["Apollo 11 lunar landing (July 20, 1969)", "Buzz Aldrin punches Bart Sibrel (September 2002)"],
     ["Neil Armstrong (astronaut)", "William Kaysing (lunar hoax author)", "Buzz Aldrin (astronaut)"],
     ["Atomic Energy Commission (US)"],
     ["Rainier Mesa (Nevada Test Site)", "Schooner crater Area 20"]),
    (20, "From Camera Bays to Weapons Bays Air Force Takes Control",
     "1982 Wackenhut mock attack; F-117; Area 52; Bond MiG-23 death; CIA ceded Area 51.",
     ["Wackenhut mock attack 1982 without DOE notice nuclear subs alerted", "Have Blue radar signature ball bearing size per Lovick",
      "CIA ceded Area 51 control by 1974 per Jacobsen"],
     ["Wackenhut mock helicopter attack Area 51 (c. 1982)", "General Bond MiG-23 crash (April 26, 1984)", "F-117 public reveal (November 1988)"],
     ["Richard Mingus (Area 51 security)", "Edward Lovick (stealth physicist)", "Robert M Bond (USAF general)"],
     ["Wackenhut Security", "Lockheed Skunk Works"],
     ["Area 52 Tonopah Test Range", "Rainier Mesa (Nevada Test Site)"]),
    (21, "Revelation",
     "Predator bin Laden mock-up; Yemen drone strike; Roswell EG&G engineer testimony; S-4 human experiments claim.",
     ["Predator assassination tests at Area 51 January 2001 classified", "Full-scale Tarnak Farm mock-up built at Area 51 2001",
      "Roswell disc child bodies Stalin Mengele hoax per EG&G engineer Jacobsen source",
      "US parallel medical experiments on handicapped at S-4 per EG&G engineer"],
     ["Bin Laden compound mock-up at Area 51 (2001)", "Yemen Predator strike al-Harethi (November 2, 2002)", "Roswell crash (July 1947)"],
     ["Cofer Black (CIA Counterterrorism)", "George Tenet (CIA director)", "EG&G engineer Roswell source (anonymous)"],
     ["General Atomics (Predator drone)"],
     ["Tarnak Farm (Afghanistan mock-up)", "Creech Air Force Base (Indian Springs)", "S-4 facility (per Lazar and engineer)"]),
]

CLAIMS = [
    ("Roswell craft had Cyrillic writing per Jacobsen source", "roswell-craft-cyrillic-writing-jacobsen",
     "July 1947", [], "[[Roswell Army Air Field (1947)]]", '["Chapter 2"]',
     "The Roswell crashed craft had a round fuselage, dome, no tail or wings, and Cyrillic writing inside—kept secret until Jacobsen's book per source.",
     '> "flying disc"; Russian writing "kept secret until now." (Chapter 2)'),
    ("JCS replaced flying disc press release with weather balloon story", "jcs-roswell-weather-balloon-cover",
     "July 1947", [], "[[Roswell Army Air Field (1947)]]", '["Chapter 2"]',
     "Joint Chiefs withdrew the flying-disc press release and replaced it with a weather balloon story—the official cover story ever since per Jacobsen.",
     '> "official cover story… ever since." (Chapter 2)'),
    ("Bissell diverted Marshall Plan funds to CIA covert ops", "bissell-marshall-plan-fund-diversion",
     "1951", [{"type": "person", "link": "Richard Bissell (CIA)"}], "Washington DC", '["Chapter 3"]',
     "Richard Bissell diverted Marshall Plan funds to CIA covert operations—largely unknown until Jacobsen's account.",
     '> "Largely unknown until now… hidden hand." (Chapter 3)'),
    ("Eisenhower chose CIA for U-2 plausible deniability", "eisenhower-cia-u2-plausible-deniability",
     "October 1955", [{"type": "person", "link": "Dwight D Eisenhower (president)"}], "[[Area 51 (Groom Lake, Nevada)]]", '["Chapter 3"]',
     "President Eisenhower chose the CIA over the Air Force for U-2 operations to maintain plausible deniability if a plane were shot down.",
     "Eisenhower intervened in Bissell-LeMay dispute and gave CIA control of Area 51 and U-2 (Chapter 3)."),
    ("By 1957 U-2s caused over 50 percent continental UFO reports per CIA monograph", "u2-caused-majority-ufo-reports-1957",
     "By 1957", [{"type": "group", "link": "Central Intelligence Agency"}], "United States", '["Chapter 4"]',
     "By 1957 U-2 flights accounted for more than 50% of continental UFO sightings per a CIA monograph cited by Jacobsen.",
     "Odarenko policy segregated explainable U-2 sightings from inexplicable reports (Chapter 4)."),
    ("Stockman U-2 flight proved bomber gap false July 1956", "stockman-flight-bomber-gap-false-1956",
     "July 4, 1956", [{"type": "person", "link": "Hervey Stockman (U-2 pilot)"}], "Soviet Union", '["Chapter 5"]',
     "Hervey Stockman's July 4, 1956 U-2 overflight showed orderly Soviet fighter rows and proved the bomber gap false per Miller memos.",
     "8.5-hour flight; 400,000 sq mi coverage (Chapter 5)."),
    ("Project 57 spread plutonium over 895 acres adjacent to Groom Lake April 1957", "project-57-plutonium-895-acres-1957",
     "April 24, 1957", [{"type": "group", "link": "Atomic Energy Commission (US)"}], "[[Area 13 (Project 57 site)]]", '["Chapter 6"]',
     "Project 57 detonation spread plutonium over 895 acres adjacent to Groom Lake; Mingus guarded without radiation gear.",
     "6:27 a.m. detonation; extreme radiation per source (Chapter 6)."),
    ("Hood was largest continental US detonation at 74 kt July 1957", "hood-largest-continental-detonation-74kt-1957",
     "July 5, 1957", [], "[[Nevada Test Site]]", '["Chapter 6"]',
     "Hood was the largest thermonuclear detonation on continental U.S. soil at 74 kt; flash visible from Canada to Mexico.",
     "Area 51 evacuated but not secured; Mingus sent back alone (Chapter 6)."),
    ("Gary Powers shot down at Kyshtym 40 May 1 1960", "powers-shootdown-kyshtym-1960",
     "May 1, 1960", [{"type": "person", "link": "Francis Gary Powers (U-2 pilot)"}], "[[Kyshtym 40 (Soviet nuclear facility)]]", '["Chapter 8"]',
     "Francis Gary Powers was shot down at Kyshtym 40 at 8:53 local time; Bissell had assured Eisenhower pilot would not survive SA-2 hit.",
     "Powers escaped without ejection seat; canopy manual release (Chapter 8)."),
    ("Wheelon became Mayor of Area 51 summer 1962", "wheelon-mayor-area-51-1962",
     "Summer 1962", [{"type": "person", "link": "Bud Wheelon (CIA DS&T)"}], "[[Area 51 (Groom Lake, Nevada)]]", '["Chapter 10"]',
     "Bud Wheelon became the new 'Mayor of Area 51' as first head of CIA Directorate of Science and Technology.",
     '> "in this way, I became the new \\"Mayor of Area 51,\\"" (Chapter 10)'),
    ("Collins Oxcart crash Wendover May 24 1963 pitot tube cause", "collins-oxcart-crash-pitot-tube-1963",
     "May 24, 1963", [{"type": "person", "link": "Kenneth Collins (Oxcart pilot)"}], "[[Wendover Utah (Oxcart crash site 1963)]]", '["Chapter 11"]',
     "Ken Collins crashed Article #123 at Wendover due to pitot tube freezing in cloud moisture causing false airspeed and stall.",
     "F-105 nuclear-weapon cover story given to ranchers; press still listed F-105 as of 2011 (Chapter 11)."),
    ("Hillenkoetter knew Roswell disc sent by Stalin per Jacobsen source", "hillenkoetter-knew-roswell-stalin-disc",
     "1947–1960", [{"type": "person", "link": "Roscoe Hillenkoetter (CIA/NICAP)"}], "[[Roswell Army Air Field (1947)]]", '["Chapter 12"]',
     "In his position as CIA director, Roscoe Hillenkoetter knew the flying disc at Roswell had been sent by Joseph Stalin per Jacobsen.",
     "Hillenkoetter testified Air Force silenced personnel on UFOs (Chapter 12)."),
    ("Have Doughnut 102 missions six weeks per Barnes", "have-doughnut-102-missions-1968",
     "Spring 1968", [{"type": "person", "link": "T D Barnes (Area 51 radar)"}], "[[Area 51 (Groom Lake, Nevada)]]", '["Chapter 17"]',
     "Have Doughnut MiG-21 evaluation: test pilots flew 102 MiG missions over six weeks per T.D. Barnes.",
     "MiG nicknamed 'the doughnut'; gave birth to Top Gun (Chapter 17)."),
    ("Oxcart located USS Pueblo prevented air attack per Rostow 1994", "oxcart-located-pueblo-prevented-war-1968",
     "January 26, 1968", [{"type": "person", "link": "Jack Weeks (Oxcart pilot)"}], "[[Wonsan Harbor North Korea]]", '["Chapter 16"]',
     "Jack Weeks's Oxcart mission located USS Pueblo in Changjinwan Bay; Walt Rostow (1994) said this prevented a planned air attack that would have killed Americans including POWs.",
     "Pentagon had planned 15,000-ton air attack on North Korea (Chapter 16)."),
    ("Predator assassination tests at Area 51 January 2001 classified", "predator-assassination-tests-area-51-2001",
     "January 2001", [{"type": "person", "link": "Cofer Black (CIA Counterterrorism)"}], "[[Area 51 (Groom Lake, Nevada)]]", '["Chapter 21"]',
     "Weaponized Predator drone technology merging Hellfire missiles was tested at Area 51; development program remains classified per Jacobsen.",
     "Cofer Black faced hurdle that targeted assassination by CIA was illegal under Reagan EO 12333 (Chapter 21)."),
    ("Full-scale Tarnak Farm mock-up built at Area 51 2001", "tarnak-farm-mock-up-area-51-2001",
     "2001", [], "[[Area 51 (Groom Lake, Nevada)]]", '["Chapter 21"]',
     "CIA and Air Force built a full-scale mock-up of Osama bin Laden's Tarnak Farm compound on outer reaches of Area 51 to test drone strike collateral damage.",
     "State Department needed casualty estimates for bin Laden family members and guests (Chapter 21)."),
    ("Roswell disc child bodies Stalin Mengele hoax per EG&G engineer Jacobsen source", "roswell-stalin-mengele-child-aviators-jacobsen",
     "July 1947", [{"type": "person", "link": "EG&G engineer Roswell source (anonymous)"}], "[[Roswell Army Air Field (1947)]]", '["Chapter 21"]',
     "Per anonymous EG&G engineer interviewed by Jacobsen: Roswell crash was not aliens but human guinea pigs under five feet tall; craft sent by Stalin with Russian writing; children created by Josef Mengele for a War of the Worlds-style hoax.",
     "Engineer: 'not aliens… human guinea pigs… under five feet tall'; Stalin goal was public panic like War of the Worlds (Chapter 21).",
     "Walter Haut posthumous affidavit claimed aliens; Air Force weather balloon retractions also in source—Jacobsen does not adjudicate."),
    ("US parallel medical experiments on handicapped at S-4 per EG&G engineer", "s4-human-experiments-handicapped-jacobsen-engineer",
     "Through 1980s", [{"type": "person", "link": "EG&G engineer Roswell source (anonymous)"}], "[[S-4 facility (per Lazar and engineer)]]", '["Chapter 21"]',
     "EG&G engineer told Jacobsen the U.S. performed medical experiments on handicapped children and prisoners at S-4 because 'we were doing the same thing' as alleged Soviet program; continued at least through the 1980s.",
     "Engineer refused full disclosure: 'You don't know half of it.' (Chapter 21)."),
]

PERSONS = [
    ("Richard Leghorn (overhead espionage)", "richard-leghorn-overhead-espionage", ["MIT physicist", "overhead reconnaissance advocate"],
     "Formulated overhead espionage concept at Operation Crossroads Baker detonation; presented spy-plane papers 1946 and 1948."),
    ("Curtis LeMay (Cold War)", "curtis-lemay-cold-war", ["Air Force general", "SAC commander"],
     "Advocated bomber fleet and first-strike policy; opposed spy planes; incendiary bombing of Japan; Crossroads procedures officer."),
    ("Richard Bissell (CIA)", "richard-bissell-cia", ["CIA officer", "U-2 and A-12 program lead"],
     "Led Project Aquatone; diverted Marshall Plan funds; resigned after Bay of Pigs February 1962."),
    ("Kelly Johnson (Lockheed)", "kelly-johnson-lockheed", ["Lockheed Skunk Works head", "U-2 and A-12 designer"],
     "Designed U-2 and A-12; opposed radar-absorbing paint; 'What in Hell, Lou?' to Schalk."),
    ("Francis Gary Powers (U-2 pilot)", "francis-gary-powers-u2-pilot", ["U-2 pilot"],
     "Shot down May 1, 1960; offered suicide pin; sentenced ten years; exchanged 1962."),
    ("Hervey Stockman (U-2 pilot)", "hervey-stockman-u2-pilot", ["CIA Detachment A pilot"],
     "First U-2 over Soviet Union July 4, 1956; shot down June 11, 1967; POW."),
    ("Richard Mingus (Area 51 security)", "richard-mingus-area-51-security", ["security guard", "EG&G employee"],
     "Guarded Project 57 and Area 51; Hood test witness; 1982 mock-attack coordinator."),
    ("Bud Wheelon (CIA DS&T)", "bud-wheelon-cia-dst", ["CIA Director of Science and Technology", "Mayor of Area 51"],
     "First DS&T head; 'Mayor of Area 51' summer 1962; Cuba missile warning dismissed by Sherman Kent."),
    ("Kenneth Collins (Oxcart pilot)", "kenneth-collins-oxcart-pilot", ["CIA Oxcart pilot", "code name Ken Colmar"],
     "Crashed Article #123 May 24, 1963; Black Shield pilot; truth serum debrief."),
    ("Hugh Slater (Area 51 commander)", "hugh-slater-area-51-commander", ["Area 51 base commander"],
     "Handled UFO disclosure forms; Black Shield commander; House-Six flying rules."),
    ("Richard Helms (CIA director)", "richard-helms-cia-director", ["CIA director"],
     "'Only sin in espionage is getting caught'; saved Oxcart from mothballing 1967."),
    ("Jack Weeks (Oxcart pilot)", "jack-weeks-oxcart-pilot", ["Oxcart pilot"],
     "Located USS Pueblo Jan 26, 1968; vanished South China Sea June 5, 1968."),
    ("T D Barnes (Area 51 radar)", "td-barnes-area-51-radar", ["EG&G radar specialist", "Have Doughnut participant"],
     "Fixed X-15 radar; 102 Have Doughnut MiG missions; NERVA witness."),
    ("Munir Redfa (Iraqi defector)", "munir-redfa-iraqi-defector", ["Iraqi Air Force colonel"],
     "Defected with MiG-21 to Israel August 1966 for $1 million per source."),
    ("Cofer Black (CIA Counterterrorism)", "cofer-black-cia-counterterrorism", ["CIA Counterterrorism Center director"],
     "January 2001 Predator-Hellfire bin Laden planning; Area 51 tests."),
    ("EG&G engineer Roswell source (anonymous)", "egg-engineer-roswell-source-anonymous", ["EG&G engineer", "Jacobsen source"],
     "Anonymous source; 18 months of interviews; Stalin/Mengele Roswell account; S-4 human experiments claim."),
    ("Wernher Von Braun (Paperclip)", "wernher-von-braun-paperclip", ["rocket scientist", "Operation Paperclip"],
     "German rocket scientist at White Sands; fled Johnston Island before Orange test."),
    ("Dwight D Eisenhower (president)", "dwight-d-eisenhower-president", ["U.S. president"],
     "Gave CIA control of Area 51; authorized U-2 overflights with caution after Stockman flight."),
    ("Lyndon B Johnson (president)", "lyndon-b-johnson-president", ["U.S. president", "vice president"],
     "Sputnik 'Red Moon' reaction; outed YF-12 as A-11; unaware of Area 51 as VP."),
    ("Roscoe Hillenkoetter (CIA/NICAP)", "roscoe-hillenkoetter-cia-nicap", ["first CIA director", "NICAP board"],
     "Knew Roswell disc from Stalin per Jacobsen; testified on Air Force UFO secrecy."),
]

GROUPS = [
    ("Lockheed Skunk Works", "lockheed-skunk-works", "military_alliance",
     "Lockheed Advanced Development Projects; built U-2, A-12, SR-71, Have Blue, F-117; Burbank facility."),
    ("Office of Policy Coordination (CIA)", "office-of-policy-coordination-cia", "polity",
     "CIA covert operations arm; Frank Wisner chief; funded via Marshall Plan diversion per Bissell."),
    ("National Reconnaissance Office", "national-reconnaissance-office", "polity",
     "Founded September 6, 1961; name classified until 1992; overhead reconnaissance partner at Area 51."),
    ("Project Blue Book (US Air Force)", "project-blue-book-us-air-force", "polity",
     "Public UFO investigation; covert Sign/Grudge/Twinkle programs; 74,000 pages classified files per source."),
    ("Thirty-Fifth Black Cat U-2 Squadron", "thirty-fifth-black-cat-u2-squadron", "military_alliance",
     "Taiwanese Nationalist CIA U-2 pilots; Taoyuan base; Yeh Changti shot down 1963."),
    ("Have Doughnut program (MiG evaluation)", "have-doughnut-mig-evaluation-program", "military_alliance",
     "1968 MiG-21 reverse engineering at Area 51; 102 missions; origin of Top Gun per Barnes."),
    ("303 Committee (covert action review)", "303-committee-covert-action-review", "polity",
     "Review board for covert actions; denied then authorized Oxcart missions 1966–1967."),
    ("1129th Special Activities Squadron", "1129th-special-activities-squadron", "military_alliance",
     "Oxcart/Black Shield unit at Groom Lake and Kadena."),
    ("Wackenhut Security", "wackenhut-security", "military_alliance",
     "Conducted unannounced mock helicopter attack on Area 51 c. 1982."),
    ("General Atomics (Predator drone)", "general-atomics-predator-drone", "military_alliance",
     "Predator drone manufacturer; Hellfire integration tested at Area 51."),
]

LOCATIONS = [
    ("Roswell Army Air Field (1947)", "roswell-army-air-field-1947",
     "Site of July 1947 crash(es); 509th Bomb Group; weather balloon cover story per source."),
    ("Bikini Atoll", "bikini-atoll",
     "Operation Crossroads 1946; Baker 23-kiloton underwater shot."),
    ("White Sands Proving Ground", "white-sands-proving-ground",
     "V-2/Hermes tests; May 29, 1947 errant launch toward Juárez."),
    ("Area 13 (Project 57 site)", "area-13-project-57-site",
     "16 sq mi NW of Groom Lake; Project 57 dirty bomb April 1957; excluded from official NTS maps as of 2011."),
    ("Kadena Air Base Okinawa", "kadena-air-base-okinawa",
     "Operation Black Shield deployment May 1967; 29 Oxcart missions."),
    ("Area 25 Jackass Flats (NERVA)", "area-25-jackass-flats-nerva",
     "Nuclear rocket testing; Kiwi and Phoebus meltdowns; General Bond MiG-23 crash 1984."),
    ("Area 52 Tonopah Test Range", "area-52-tonopah-test-range",
     "Secondary black site for F-117 bombing tests; never officially acknowledged per Jacobsen."),
    ("Palomares Spain", "palomares-spain",
     "January 17, 1966 B-52 collision; 650 acres aerosolized plutonium."),
    ("S-4 facility (per Lazar and engineer)", "s-4-facility-area-51",
     "Outpost facility per Bob Lazar and EG&G engineer; hangars in mountainside near Groom Lake."),
    ("Creech Air Force Base (Indian Springs)", "creech-air-force-base-indian-springs",
     "Drone pilot operations ~30 miles south of Area 51; Indian Springs rebranded."),
]

EVENTS = [
    ("War of the Worlds broadcast (October 1938)", "war-of-the-worlds-broadcast-1938", "1938-10", "1938-10",
     ["Vannevar Bush (Manhattan Project context)"], "Grover's Mill New Jersey (fictional in broadcast)",
     "CBS broadcast caused mass panic; cited by Bush as example of public manipulation risk."),
    ("Operation Crossroads Baker shot (July 1946)", "operation-crossroads-baker-1946", "1946-07", "1946-07",
     ["Richard Leghorn (overhead espionage)", "Alfred O'Donnell (EG&G)"], "[[Bikini Atoll]]",
     "23-kiloton underwater detonation; Leghorn's overhead epiphany; 1M+ tons steel armada."),
    ("Roswell crash (July 1947)", "roswell-crash-july-1947", "1947-07", "1947-07",
     [], "[[Roswell Army Air Field (1947)]]",
     "First week of July 1947; flying disc then weather balloon cover; Cyrillic writing per Jacobsen Ch.2; Stalin/Mengele account Ch.21."),
    ("Mount Charleston C-54 crash (November 16, 1955)", "mount-charleston-c54-crash-1955", "1955-11-16", "1955-11-16",
     ["Richard Bissell (CIA)"], "Mount Charleston Nevada",
     "11 Project Aquatone personnel killed; CIA acknowledged 2002."),
    ("Gary Powers U-2 shootdown (May 1, 1960)", "gary-powers-u2-shootdown-1960", "1960-05-01", "1960-05-01",
     ["Francis Gary Powers (U-2 pilot)", "Richard Bissell (CIA)"], "[[Kyshtym 40 (Soviet nuclear facility)]]",
     "SA-2 shootdown; five-day weather-plane cover collapsed when Khrushchev revealed Powers alive."),
    ("Operation Black Shield begins (May 1967)", "operation-black-shield-begins-1967", "1967-05", "1967-05",
     ["Richard Helms (CIA director)", "Hugh Slater (Area 51 commander)"], "[[Kadena Air Base Okinawa]]",
     "Oxcart deployment; 1M lbs matériel; 260 crew; first mission photographed 70 of 190 SAM sites."),
    ("USS Pueblo seized (January 23, 1968)", "uss-pueblo-seized-1968", "1968-01-23", "1968-01-23",
     [], "[[Wonsan Harbor North Korea]]",
     "North Korea seized SIGINT ship; 90% documents survived destruction; Pentagon war plan abandoned after Oxcart located vessel."),
    ("Munir Redfa MiG-21 defection (August 1966)", "munir-redfa-mig-21-defection-1966", "1966-08", "1966-08",
     ["Munir Redfa (Iraqi defector)"], "Israel",
     "Iraqi colonel flew MiG-21 to Israel; later shipped to Area 51."),
    ("Palomares nuclear accident (January 17, 1966)", "palomares-nuclear-accident-1966", "1966-01-17", "1966-01-17",
     [], "[[Palomares Spain]]",
     "B-52 collision; plutonium dispersion; Pentagon denied lost bomb 44 days."),
    ("Bin Laden compound mock-up at Area 51 (2001)", "bin-laden-compound-mock-up-area-51-2001", "2001", "2001",
     ["Cofer Black (CIA Counterterrorism)"], "[[Area 51 (Groom Lake, Nevada)]]",
     "Full-scale Tarnak Farm replica for Predator strike collateral-damage testing."),
]

CONCEPTS = [
    ("Overhead espionage", "overhead-espionage",
     "Aerial reconnaissance above denied territory; Leghorn's post-Crossroads concept; U-2, Oxcart, satellites."),
    ("Plausible deniability", "plausible-deniability",
     "Eisenhower chose CIA for U-2 so U.S. could deny military involvement if shot down."),
    ("Project 57 dirty bomb test", "project-57-dirty-bomb-test",
     "1957 AEC simulation of airplane crash dispersing plutonium at Area 13; called 'safety test' in press."),
    ("Operation Black Shield", "operation-black-shield",
     "1967–1968 Oxcart deployment from Kadena; 29 missions over Vietnam, Korea, Cambodia/Laos."),
    ("Have Doughnut MiG reverse engineering", "have-doughnut-mig-reverse-engineering",
     "1968 evaluation of Soviet MiG-21 at Area 51; led to Top Gun."),
    ("Stealth antiradar technology", "stealth-antiradar-technology",
     "Ed Lovick radar cross-section work; chines, cesium ionization, Have Blue faceted panels."),
]

CONTROVERSIES = [
    ("Roswell crash explanation within Jacobsen source", "roswell-crash-explanation-jacobsen-source",
     "Chapters 2, 12, 21",
     ["Weather balloon cover (JCS/Air Force)", "Hillenkoetter: Stalin sent disc", "EG&G engineer: Stalin/Mengele child aviators hoax", "Haut affidavit: aliens", "Lazar: extraterrestrial saucers"],
     "## Positions in Source\n\nJacobsen presents multiple incompatible accounts without adjudicating: JCS weather balloon cover (Ch.2), Hillenkoetter knew Stalin sent disc (Ch.12), anonymous EG&G engineer's Stalin/Mengele hoax with U.S. parallel S-4 experiments (Ch.21), plus prior Lazar extraterrestrial claims (Ch.1) and Walter Haut's alien affidavit mentioned in Ch.21."),
    ("CIA vs Air Force UFO cover-up blame", "cia-air-force-ufo-coverup-blame-1966",
     "Chapter 12",
     ["Air Force Secretary Brown blamed CIA", "CIA refused Robertson Panel publicity (Weber)", "Cronkite: CIA lied to Congress"],
     "Air Force and CIA each blamed the other for UFO cover-up; CIA tracked UFOs while denying congressional knowledge."),
    ("Gulf of Tonkin attack validity per Jacobsen", "gulf-of-tonkin-attack-validity-jacobsen",
     "Chapter 14",
     ["Johnson/McNamara 1964 justification for escalation", "NSA 2005 admission intelligence deliberately skewed"],
     "Jacobsen cites NSA 2005 admission that Gulf of Tonkin intelligence was skewed to support attack narrative."),
    ("Bob Lazar vs EG&G engineer on S-4", "bob-lazar-vs-egg-engineer-s4-jacobsen",
     "Chapters 1 and 21",
     ["Lazar: nine extraterrestrial saucers", "EG&G engineer: S-4 timeline fits; human experiments; hover tech solved 1950s", "Most interviewees skeptical of Lazar"],
     "Jacobsen notes engineer said Lazar's S-4 timeline 'fits' but most sources skeptical; engineer offers terrestrial explanation vs Lazar's extraterrestrial account."),
]

def main():
    created = 0
    for num, title, summary, claims, events, persons, groups, locations in CHAPTERS:
        content, slug = chapter_page(num, title, summary, claims, events, persons, groups, locations)
        if write_if_new(WIKI / "sources" / f"{slug}.md", content):
            created += 1

    for title, slug, date, actors, loc, ctx, stmt, ev, *rest in CLAIMS:
        opp = rest[0] if rest else None
        content = claim_page(title, slug, date, actors, loc, ctx, stmt, ev, opp)
        if write_if_new(WIKI / "claims" / f"{slug}.md", content):
            created += 1

    for title, slug, roles, body in PERSONS:
        if write_if_new(WIKI / "persons" / f"{slug}.md", person_page(title, slug, roles, body)):
            created += 1

    for title, slug, cat, body in GROUPS:
        if write_if_new(WIKI / "groups" / f"{slug}.md", group_page(title, slug, cat, body)):
            created += 1

    for title, slug, body in LOCATIONS:
        if write_if_new(WIKI / "locations" / f"{slug}.md", location_page(title, slug, body)):
            created += 1

    for title, slug, ds, de, parts, loc, overview in EVENTS:
        if write_if_new(WIKI / "events" / f"{slug}.md", event_page(title, slug, ds, de, parts, loc, overview)):
            created += 1

    for title, slug, body in CONCEPTS:
        if write_if_new(WIKI / "concepts" / f"{slug}.md", concept_page(title, slug, body)):
            created += 1

    for title, slug, locus, positions, body in CONTROVERSIES:
        if write_if_new(WIKI / "controversies" / f"{slug}.md", controversy_page(title, slug, locus, positions, body)):
            created += 1

    print(f"Created {created} new wiki pages")


if __name__ == "__main__":
    main()
