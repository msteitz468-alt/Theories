#!/usr/bin/env python3
"""Second batch: additional claims/events from Jacobsen ch 2-21."""
from pathlib import Path
import importlib.util

spec = importlib.util.spec_from_file_location("bulk", Path(__file__).parent / "bulk_ingest_jacobsen_ch2_21.py")
bulk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bulk)

WIKI = bulk.WIKI

EXTRA_CLAIMS = [
    ("Chines reduced A-12 radar cross section 90 percent", "a12-radar-cross-section-90-percent-reduction",
     "Fall 1959", [{"type": "person", "link": "Kelly Johnson (Lockheed)"}], "[[Area 51 (Groom Lake, Nevada)]]", '["Chapter 7"]',
     "Flat underbelly chines reduced A-12 radar cross section by approximately 90 percent per Jacobsen.",
     '> "With the plane\'s underbelly now flat, its radar cross section was reduced by an astonishing 90 percent."'),
    ("NRO created September 1961 public did not know until 1992", "nro-created-1961-secret-until-1992",
     "September 6, 1961", [{"type": "group", "link": "National Reconnaissance Office"}], "Washington DC", '["Chapter 9"]',
     "National Reconnaissance Office created September 6, 1961; existence unknown to public until 1992.",
     "Wayne Pendleton: 'where I'm going doesn't exist' (Chapter 9)."),
    ("Yeh Changti tortured 19 years CIA unaware he survived", "yeh-changti-tortured-19-years-black-cat",
     "November 1, 1963", [{"type": "person", "link": "Yeh Changti (Black Cat pilot)"}], "China", '["Chapter 13"]',
     "Black Cat U-2 pilot Yeh Changti shot down November 1, 1963; tortured 19 years; CIA unaware he survived until release 1982.",
     "Program fully classified as of 2011 per Hsichun Hua (Chapter 13)."),
    ("Johnson outed YF-12 as fictitious A-11 February 1964", "johnson-a11-yf12-disclosure-february-1964",
     "February 29, 1964", [{"type": "person", "link": "Lyndon B Johnson (president)"}], "Washington DC", '["Chapter 14"]',
     "Johnson publicly disclosed YF-12 as 'A-11' speed record; true A-12 remained secret until 2007.",
     "Schriever memo sought forced disclosure for Air Force takeover (Chapter 14)."),
    ("NSA admitted Gulf of Tonkin intelligence skewed 2005", "nsa-gulf-of-tonkin-intelligence-skewed-2005",
     "2005 (admission)", [{"type": "group", "link": "NSA (National Security Agency)"}], "Gulf of Tonkin", '["Chapter 14"]',
     "NSA admitted in 2005 that Gulf of Tonkin intelligence was deliberately skewed to support notion of an attack.",
     "Johnson used incident for Vietnam escalation August 1964 (Chapter 14)."),
    ("Top Gun born from MiG program established March 1969", "top-gun-born-from-have-doughnut-1969",
     "March 1969", [{"type": "group", "link": "Have Doughnut program (MiG evaluation)"}], "[[Area 51 (Groom Lake, Nevada)]]", '["Chapter 17"]',
     "Have Doughnut MiG-21 program gave birth to Navy Fighter Weapons School (Top Gun), established March 1969.",
     "Vietnam air combat ratio shifted from 9:1 to 13:1 per source (Chapter 17)."),
    ("Wackenhut mock attack 1982 without DOE notice nuclear subs alerted", "wackenhut-mock-attack-1982-nuclear-alert",
     "c. 1982", [{"type": "group", "link": "Wackenhut Security"}], "[[Area 51 (Groom Lake, Nevada)]]", '["Chapter 20"]',
     "Wackenhut mock helicopter attack on Area 51 conducted without informing DOE; nuclear submarines alerted; Tomahawks targeted NTS.",
     "Mingus ordered bomb test in shaft to continue: 'Keep the device going down' (Chapter 20)."),
    ("Area 51 named for Roswell remains sent 1951 per EG&G engineer", "area-51-named-roswell-remains-1951",
     "1951", [{"type": "person", "link": "EG&G engineer Roswell source (anonymous)"}], "[[Area 51 (Groom Lake, Nevada)]]", '["Chapter 21"]',
     "Per EG&G engineer: Area 51 named because 1947 Roswell crash remains were sent to Nevada in 1951.",
     "Engineer interviewed 18 months; program linked to S-4 (Chapter 21)."),
    ("Tenet halted pre-9/11 Predator strike on bin Laden", "tenet-halted-pre-911-bin-laden-predator-strike",
     "Early 2001", [{"type": "person", "link": "George Tenet (CIA director)"}], "[[Tarnak Farm (Afghanistan mock-up)]]", '["Chapter 21"]',
     "CIA Director George Tenet decided against Hellfire-equipped Predator strike on Osama bin Laden before 9/11—a decision the CIA would come to regret per Jacobsen.",
     "State Department approved assassination in February 2001 after FBI bounty avenue (Chapter 21)."),
    ("286 nuclear bombs exploded near Area 51 by 1964", "286-nuclear-bombs-near-area-51-by-1964",
     "By 1964", [{"type": "group", "link": "Atomic Energy Commission (US)"}], "[[Nevada Test Site]]", '["Chapter 14"]',
     "286 nuclear bombs exploded near Area 51 by 1964; 162 underground tests Sept 1961–Dec 1964, nearly half with accidental radioactivity release per Jacobsen.",
     "Oxcart sonic boom killed two factory workers in West Virginia (Chapter 14)."),
    ("Air Force told Congress no UFO files existed while running covert programs", "air-force-denied-ufo-files-congress",
     "1950s", [{"type": "group", "link": "Project Blue Book (US Air Force)"}], "United States", '["Chapter 4"]',
     "U.S. Air Force told Congress no UFO investigation files existed while running covert Project Sign/Blue Book/Twinkle programs with 74,000 pages classified.",
     "37 cubic feet of classified case files per source (Chapter 4)."),
    ("LBJ as VP entirely unaware of A-12 and Area 51 until after JFK death", "lbj-unaware-area-51-as-vice-president",
     "1963", [{"type": "person", "link": "Lyndon B Johnson (president)"}], "[[Area 51 (Groom Lake, Nevada)]]", '["Chapter 11"]',
     "Lyndon Johnson as vice president was entirely unaware of the A-12 program and had no clue about Area 51 until after Kennedy's assassination.",
     "Briefed on 8th day as president (Chapter 11)."),
]

EXTRA_PERSONS = [
    ("Yeh Changti (Black Cat pilot)", "yeh-changti-black-cat-pilot", ["Taiwanese U-2 pilot", "Black Cat squadron"],
     "Shot down November 1, 1963; tortured 19 years; released 1982; CIA unaware he survived."),
    ("George Tenet (CIA director)", "george-tenet-cia-director", ["CIA director"],
     "Halted pre-9/11 Predator strike on bin Laden; later drone war expansion."),
    ("Frank Murray (Oxcart pilot)", "frank-murray-oxcart-pilot", ["Oxcart pilot", "Black Shield"],
     "Black Shield missions; ECM jamming during Vietnam bombing raids; North Korea overflight February 1968."),
    ("Ed Lovick (stealth physicist)", "ed-lovick-stealth-physicist", ["Lockheed physicist", "grandfather of stealth"],
     "Radar cross-section work from 1957; D-21 drone; Have Blue ball-bearing signature."),
    ("Jim Freedman (Area 51 property control)", "jim-freedman-area-51-property", ["EG&G property control 1960-1974"],
     "Area 51 property manager; witnessed Vietnamese trainees; Kirkpatrick ramp modifications."),
    ("Louis Schalk (Lockheed test pilot)", "louis-schalk-lockheed-pilot", ["Lockheed test pilot"],
     "First Oxcart taxi lift-off April 25, 1962; first official flight 59 minutes."),
    ("Walt Ray (Oxcart pilot)", "walt-ray-oxcart-pilot", ["Oxcart pilot"],
     "Killed January 5, 1967; ejection seat parachute tangled; faulty fuel gauge."),
]

EXTRA_LOCATIONS = [
    ("Kyshtym 40 (Soviet nuclear facility)", "kyshtym-40-soviet-nuclear-facility",
     "Site where Gary Powers U-2 was shot down May 1, 1960."),
    ("Mount Charleston (Nevada)", "mount-charleston-nevada",
     "November 16, 1955 C-54 crash killed 11 Project Aquatone personnel."),
    ("Wonsan Harbor North Korea", "wonsan-harbor-north-korea",
     "USS Pueblo anchored near here; Oxcart located ship January 26, 1968."),
    ("Wendover Utah (Oxcart crash site 1963)", "wendover-utah-oxcart-crash-1963",
     "Ken Collins Article #123 crash May 24, 1963; F-105 cover story."),
    ("Tarnak Farm (Afghanistan mock-up)", "tarnak-farm-afghanistan-mock-up",
     "Bin Laden compound; full-scale replica built at Area 51 for drone testing 2001."),
]

EXTRA_EVENTS = [
    ("Project 57 detonation (April 24, 1957)", "project-57-detonation-april-1957", "1957-04-24", "1957-04-24",
     ["Richard Mingus (Area 51 security)", "James Shreve Jr (Project 57)"], "[[Area 13 (Project 57 site)]]",
     "Dirty bomb safety test; plutonium over 895 acres; Mingus unprotected guard."),
    ("Hood thermonuclear test (July 5, 1957)", "hood-thermonuclear-test-july-1957", "1957-07-05", "1957-07-05",
     ["Richard Mingus (Area 51 security)"], "[[Nevada Test Site]]",
     "74 kt largest continental U.S. detonation; Area 51 uninhabitable after."),
    ("Ken Collins Oxcart crash Wendover (May 24, 1963)", "ken-collins-oxcart-crash-wendover-1963", "1963-05-24", "1963-05-24",
     ["Kenneth Collins (Oxcart pilot)"], "[[Wendover Utah (Oxcart crash site 1963)]]",
     "Pitot tube freeze; F-105 cover story; truth serum debrief."),
    ("Cuban missile crisis U-2 photography (October 14, 1962)", "cuban-missile-crisis-u2-photography-1962", "1962-10-14", "1962-10-14",
     ["Bud Wheelon (CIA DS&T)", "John McCone (CIA director)"], "Cuba",
     "Air Force pilot in blue suit flew CIA U-2; photos showed Soviet nuclear missiles."),
    ("Yemen Predator strike al-Harethi (November 2, 2002)", "yemen-predator-strike-al-harethi-2002", "2002-11-02", "2002-11-02",
     ["Cofer Black (CIA Counterterrorism)"], "Marib Yemen",
     "First high-profile post-9/11 drone assassination; Wolfowitz broke secrecy agreement."),
    ("Jack Weeks Oxcart disappearance (June 5, 1968)", "jack-weeks-oxcart-disappearance-1968", "1968-06-05", "1968-06-05",
     ["Jack Weeks (Oxcart pilot)"], "South China Sea",
     "Lost at sea; no body or wreckage; Oxcart program ended."),
]

EXTRA_GROUPS = [
    ("NSA (National Security Agency)", "nsa-national-security-agency", "polity",
     "Gulf of Tonkin intelligence; USS Pueblo SIGINT; 2005 skewed-intelligence admission cited."),
    ("NICAP (ufology organization)", "nicap-ufology-organization", "ideological_movement",
     "National Investigations Committee on Aerial Phenomena; Hillenkoetter board; Bryan head 1969."),
]

def main():
    created = 0
    for title, slug, date, actors, loc, ctx, stmt, ev, *rest in EXTRA_CLAIMS:
        opp = rest[0] if rest else None
        if bulk.write_if_new(WIKI / "claims" / f"{slug}.md", bulk.claim_page(title, slug, date, actors, loc, ctx, stmt, ev, opp)):
            created += 1
    for title, slug, roles, body in EXTRA_PERSONS:
        if bulk.write_if_new(WIKI / "persons" / f"{slug}.md", bulk.person_page(title, slug, roles, body)):
            created += 1
    for title, slug, body in EXTRA_LOCATIONS:
        if bulk.write_if_new(WIKI / "locations" / f"{slug}.md", bulk.location_page(title, slug, body)):
            created += 1
    for title, slug, ds, de, parts, loc, overview in EXTRA_EVENTS:
        if bulk.write_if_new(WIKI / "events" / f"{slug}.md", bulk.event_page(title, slug, ds, de, parts, loc, overview)):
            created += 1
    for title, slug, cat, body in EXTRA_GROUPS:
        if bulk.write_if_new(WIKI / "groups" / f"{slug}.md", bulk.group_page(title, slug, cat, body)):
            created += 1
    print(f"Created {created} additional pages")

if __name__ == "__main__":
    main()
