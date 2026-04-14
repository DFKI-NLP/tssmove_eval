# Live E2E Run Report

## Run Context
- Scenario ID: `v2x_definition_rolle`
- Query: Was versteht man unter Vehicle-To-X-Kommunikation und welche Rolle erfüllt sie?
- Trace JSON: `C:\Users\d93666\Desktop\TSS-MoVe\tss-move-platform\backend\apps\rag\agents\logs\agent_trace-20260409T224503Z-6f02ecd7b1ef0aef.json`
- Report Markdown: `C:\Users\d93666\Desktop\TSS-MoVe\tss-move-platform\backend\apps\rag\agents\logs\agent_trace-20260409T224503Z-6f02ecd7b1ef0aef.md`

## Pipeline Outcome
- Current phase: `ExecutionPhase.COMPLETE`
- Outcome status: `partial`
- Hypothesis mode: `False`
- Retrieved docs: `36`
- Claims: `7`
- Missing information entries: `3`
- Trace nodes: `[]`

## Cost Summary
- Pricing reference: azure_openai/gpt-5.2 | Data Zone | Germany West Central | 2026-03-31
- Run LLM total: EUR 0.308063
- Input tokens: `106828`
- Cached input tokens: `2688`
- Output tokens: `10484`
- Priced events: `6`

### Step Costs
- research_plan_agent: EUR 0.011637 (in=1080, cached=0, out=756)
- hypothesis_gate_agent: EUR 0.005051 (in=1528, cached=0, out=195)
- database_retrieval_agent: n/a (in=0, cached=0, out=0)
- reranker_agent: EUR 0.068142 (in=32001, cached=0, out=1200)
- hypothesis_agent: EUR 0.048243 (in=20401, cached=0, out=1133)
- challenge_agent: EUR 0.059403 (in=19487, cached=0, out=2103)
- knowledge_synthesis_agent (iteration=1): EUR 0.115587 (in=32331, cached=2688, out=5097)

## Claims
- V2X („Vehicle-to-Everything“) umfasst die Kommunikationsarten V2V, V2I, V2P und V2N.
- V2V ist überwiegend broadcast-basiert und überträgt u.a. Positions- und Dynamikinformationen.
- V2N ist Kommunikation zwischen UE und Serving Entity über das Mobilfunknetz (LTE/5G).
- CAM sind periodische Nachrichten mit Position/Bewegung/Fahrzeugeigenschaften; DENM sind ereignisgetriebene Warnmeldungen zu sicherheitskritischen Situationen.
- ETSI-standardisierte Nachrichtentypen, die in einem V2X-Projekt genutzt wurden, umfassen u.a. DENM, CAM, MAP, SPAT, IVI und CPM.
- 3GPP Release 14 Use-Cases umfassen u.a. Traffic flow optimization und Vulnerable road user safety; Enhanced V2X umfasst u.a. Vehicle platooning und Collective perception.
- ETSI ITS Security Architecture basiert auf Public-Key-Zertifikaten und einer PKI zur Verwaltung von Security Credentials für V2X-Kommunikation.

## Missing Information
- Direkte, normative Definitionen aus ETSI/3GPP/SAE-Standards (z.B. formale Begriffsdefinition von V2X in TS/EN-Dokumenten) liegen in den Auszügen nur indirekt bzw. über Projektberichte vor (exakte Standardzitate fehlen).
- Eine belastbare, quantitative Wirkungsbewertung (z.B. Unfallreduktion, Stau-/Emissionseffekte) wird in den vorliegenden Auszügen nicht ausgewiesen.
- Explizite Interoperabilitäts-/Deployment-Profile (z.B. C-ITS Deployment Profile, C-Roads Vorgaben) zur Frage, ob PKI „zwingend“ für Interoperabilität ist, sind nicht enthalten.

## Source Quality Profile
- Corpus total sources: `17`
- Selection total sources: `13`
- Selection peer-reviewed share: `0.0%`
- Selection open-access share: `0.0%`
- Selection median year: `2020.0`
- Selection high date confidence share: `7.69%`
- Significant deltas: none
- Selected source cards:
  - KoMoDnext - Automatisiertes Fahren im digitalen Testfeld Düsseldorf : Schlussbericht des Verbundes : Laufzeit des Vorhabens: von: 01.01.2020 bis: 31.03.2022 | grey_literature | editorial/curated | unknown
  - SMART - Simulation von Mobilfunk und Automobilverhalten in Realzeit : Abschlussbericht : Berichtszeitraum: 01.09.2017-31.01.2021 | grey_literature | editorial/curated | unknown
  - ConVeX ; deliverable D4.1: Deliverable D4.1: Roadside ITS station specification | grey_literature | editorial/curated | unknown
  - ConVeX ; deliverable D2.2: Deliverable D2.2: Final ConVeX system architecture description | grey_literature | editorial/curated | unknown
- Enrichment metrics:
  - corpus_sources_attempted: `17`
  - corpus_sources_resolved: `17`
  - corpus_source_resolution_rate: `100.0`
  - corpus_crawl_sources_matched: `0`
  - corpus_crawl_match_rate: `0.0`
  - corpus_crawl_states_found: `0`
  - corpus_crawl_state_coverage_rate: `0.0`
  - selection_sources_attempted: `13`
  - selection_sources_resolved: `13`
  - selection_source_resolution_rate: `100.0`
  - selection_crawl_sources_matched: `0`
  - selection_crawl_match_rate: `0.0`
  - selection_crawl_states_found: `0`
  - selection_crawl_state_coverage_rate: `0.0`

## Potential Issues
- none

## Final Answer
## Kurzdefinition und Rolle
Vehicle-to-X-Kommunikation (V2X, „Vehicle-to-Everything“) ist ein Sammelbegriff für den Informationsaustausch von Fahrzeugen mit anderen Fahrzeugen (V2V), mit Verkehrsinfrastruktur wie Roadside Units (V2I), mit vulnerablen Verkehrsteilnehmenden bzw. deren Endgeräten (V2P) sowie mit Netzdiensten/„Serving Entities“ über Mobilfunknetze (V2N). [1][2][3] Ihre Rolle im Straßenverkehr ist, kooperative sicherheits-, komfort- und effizienzrelevante Anwendungen zu ermöglichen, indem Fahrzeuge (und ggf. Infrastruktur/VRU-Geräte) Zustände, Ereignisse und Infrastrukturinformationen standardisiert austauschen (z. B. CAM/DENM sowie SPaT/MAP/IVI/CPM), sodass Warnungen, Assistenzfunktionen und Verkehrsflussoptimierung unterstützt werden. [4][5][6]

## Begriffsverständnis: Was umfasst V2X?
V2X wird in der ConVeX-Architektur explizit als „Vehicle-to-Everything“ mit vier Kommunikationsarten beschrieben: V2V, V2I, V2P und V2N. [1] Diese Taxonomie wird auch in einer Spezifikation der Roadside-ITS-Stationen als „V2X Service“-Arten über die beteiligten Endpunkte (UE, RSU, Serving Entity) definiert. [3]

## Abgrenzung der vier V2X-Teilarten
### Vehicle-to-Vehicle (V2V)
V2V ist direkte Fahrzeug-zu-Fahrzeug-Kommunikation (im ConVeX-Kontext über LTE-PC5 „Sidelink“) und dient dem Austausch von Applikationsinformationen wie Position, Dynamik und Fahrzeugattributen. [1] V2V wird dabei als „predominantly broadcast-based“ (überwiegend broadcast-basiert) beschrieben, was für Sicherheits- und Awareness-Anwendungen zentral ist. [1]

### Vehicle-to-Infrastructure (V2I)
V2I beschreibt den Austausch zwischen Fahrzeug/UE und Roadside Unit (RSU) bzw. lokal relevanten Applikationsservern, die ein geografisches Gebiet bedienen und ggf. überlappende Bereiche abdecken können. [2] In der ConVeX-Netzarchitektur wird V2I – wie V2V und V2P – als direkte Kommunikation über PC5 eingeordnet (wobei RSUs ähnlich wie UEs agieren). [1][2]

### Vehicle-to-Pedestrian (V2P)
V2P ist funktional „sehr ähnlich zu V2V“ (direkt, PC5-basiert) und ermöglicht Warnungen zwischen Fahrzeugen und VRU-Endgeräten (z. B. Warnung an Fußgänger oder Warnung an Fahrzeuge durch VRU-Geräte). [2] Ein exemplarischer Ablauf für VRU-Szenarien zeigt, wie Fahrzeuge CAM empfangen, eine potenziell gefährliche Situation (VRU in Nähe) erkennen und daraufhin eine Warnung ausgeben bzw. wieder zurücknehmen. [7]

### Vehicle-to-Network (V2N)
V2N verbindet ein Fahrzeug/UE mit einer „serving entity“ (Netz-/Backenddienst) über Mobilfunk (z. B. LTE oder 5G) und nutzt dazu (im LTE-Fall) die Uu-Schnittstelle; Kommunikation kann unicast oder multicast sein. [2][3]

## Kommunikationsmodelle und technische Einordnung (direkt vs. Wide-Area)
In den betrachteten Architekturen werden zwei komplementäre Kommunikationswege herausgestellt:
- Direkte Kommunikation für V2V/V2I/V2P: über PC5 (3GPP, C‑V2X) bzw. in ETSI-Kontext über ITS‑G5 auf IEEE 802.11p. [8]
- Netzbasierte Kommunikation für V2N: über LTE/5G Uu als Wide-Area-Link; ETSI stellt dafür keine eigene Funk-Schnittstelle bereit und stützt sich hierfür hybrid auf 3GPP-Interfaces. [8]
Damit wird V2X in der Praxis als Kombination aus direkter Nahbereichskommunikation und zellularer Netzkommunikation beschrieben. [8][5]

## Welche Informationen werden über V2X ausgetauscht?
### Basis-Sicherheitskommunikation: CAM und DENM
Für die Koordination autonom fahrender Fahrzeuge sieht ein ITS-Standard einen periodischen Nachrichtenaustausch vor und unterscheidet dabei prinzipiell zwei zentrale Nachrichtentypen: [4]
- Cooperative Awareness Message (CAM): periodische Nachrichten mit Informationen über Position, Bewegung und Fahrzeugeigenschaften. [4]
- Decentralized Environmental Notification Message (DENM): ereignisgetriebene Nachrichten, ausgelöst durch sicherheitskritische Situationen (z. B. Notbremsung), die solange die Situation besteht periodisch wiederholt werden. [4]

### Erweiterte Inhalte: Infrastruktur-, Karten- und Wahrnehmungsdaten
Weitere V2X-Nachrichteninhalte umfassen u. a. Wahrnehmungsdaten zur Erweiterung des Wahrnehmungsbereichs (von abstrakten Objektinformationen bis zu hochauflösenden Sensordaten), Fahrabsichten zur Koordination von Fahrmanövern sowie (hochauflösende) Kartendaten. [4]
In einem Praxisprojekt wurden darüber hinaus ETSI-standardisierte Nachrichtentypen als Grundlage einer generischen V2X-Schnittstelle genannt, insbesondere DENM, CAM, MAP, SPAT, IVI und CPM. [6]

## Funktionale Rolle im Verkehrssystem: Safety, Efficiency, Comfort und kooperative Funktionen
### Rollenbild anhand standardisierter Use-Cases
Use-Cases, die 3GPP zur Ableitung von Serviceanforderungen (Release 14) verwendet, umfassen u. a. Control loss warning, Emergency vehicle warning, Emergency stop, Cooperative adaptive cruise control, Queue warning, Automated parking system, Wrong way driver warning, Pre-crash sensing warning, Traffic flow optimization und Vulnerable road user safety. [9] Diese Use-Cases werden Kategorien wie Safety, Efficiency und Comfort zugeordnet. [9]
Für „enhanced V2X“ (Release 15 und darüber hinaus) werden anspruchsvollere kooperative Szenarien wie Vehicle platooning, Sensor and state map sharing, Remote driving und Collective perception of the environment genannt. [9]

### Rolle bei VRU-Schutz und kooperativer Wahrnehmung
Für VRU-Use-Cases wird als erwartetes Ergebnis explizit ein Sicherheitsnutzen beschrieben, wenn VRUs (z. B. Straßenarbeiter, Fußgänger, Radfahrende) portable V2X-fähige Geräte mitführen, wodurch Warnungen und Kollisionsvermeidung unterstützt werden können. [7] Eine breitere Einordnung beschreibt zudem, dass Fahrzeug-Sensorik (Kamera/Radar/LiDAR) mit V2X-Daten fusioniert wird, um kooperative Wahrnehmung und Kollisionsvermeidung zu verbessern; gleichzeitig werden Day-2/Day-3-Anwendungsfälle wie kooperative ACC und V2P-Kommunikation hervorgehoben. [10]

### Rolle für Infrastruktur-gestützte Assistenz und Verkehrsmanagement
In Testfeld- und Demonstrationskontexten wird V2X als Mittel zur Vernetzung von Fahrzeugen „über Daten und Informationen mit der Infrastruktur“ beschrieben, mit Ziel der Bewertung von Auswirkungen auf Verkehrseffizienz, Verkehrssicherheit und Umwelteinträge. [11] Ein konkretes Beispiel ist GLOSA: Über V2X wird an Ampeln die nächste Signalphase angekündigt („Green Light Optimal Speed Advice“). [12]

## Sicherheit und Vertrauenswürdigkeit als Teil der Rolle (Security Framework)
V2X ist im ITS-Kontext eng mit Sicherheitsmechanismen verbunden: Die ETSI ITS-Sicherheitsarchitektur umfasst Sicherheitsmechanismen und Managementfunktionen für Nachrichten (z. B. CAM/DENM) zwischen vehikulären ITS-Stationen, Roadside-ITS-Stationen und dem Netz über V2X-Interfaces (PC5 und Uu) und basiert auf Public-Key-Zertifikaten sowie einer Public Key Infrastructure (PKI), die zur Verwaltung der Security Credentials erforderlich ist. [13] In einem praktischen Projekt wurde außerdem eine PKI-Integration zur Signierung von V2X-Nachrichten in einer ITS‑G5 OBU beschrieben. [6]

## Einordnung: Stärken und Grenzen (aus den vorliegenden Quellen)
- Direkte Kommunikation kann durch begrenzte Reichweite eingeschränkt sein; dann kann der Austausch V2V-bezogener Applikationsinformationen alternativ über andere V2X-Services bzw. unter Nutzung zusätzlicher Infrastruktur (RSU, Applikationsserver) und verschiedener Kommunikationspfade (V2I, V2N) erfolgen – auch kombiniert. [2]
- Als offene Herausforderungen werden Kosten und Durchdringung (Marktpenetration) benannt. [10]

Missing information:
- Direkte, normative Definitionen aus ETSI/3GPP/SAE-Standards (z.B. formale Begriffsdefinition von V2X in TS/EN-Dokumenten) liegen in den Auszügen nur indirekt bzw. über Projektberichte vor (exakte Standardzitate fehlen).
- Eine belastbare, quantitative Wirkungsbewertung (z.B. Unfallreduktion, Stau-/Emissionseffekte) wird in den vorliegenden Auszügen nicht ausgewiesen.
- Explizite Interoperabilitäts-/Deployment-Profile (z.B. C-ITS Deployment Profile, C-Roads Vorgaben) zur Frage, ob PKI „zwingend“ für Interoperabilität ist, sind nicht enthalten.

Aufgestellte Hypothesen:
Hypothese 1: Vehicle-to-Everything (V2X) bezeichnet im Straßenverkehr einen Oberbegriff für vier Kommunikationsarten—Vehicle-to-Vehicle (V2V), Vehicle-to-Infrastructure (V2I), Vehicle-to-Pedestrian (V2P) und Vehicle-to-Network (V2N)—wobei V2V/V2I/V2P typischerweise direkte, überwiegend broadcast-basierte Nahbereichskommunikation sind und V2N eine zellulare (Wide-Area) Verbindung zu Netzdiensten/Serving Entities nutzt.
Reasoning: fit=0.71, semantic=inferential, sources=3, diversity=0.67, contradiction=False
Supporting evidence document IDs: [1], [2], [3]

Hypothese 2: Die funktionale Rolle von V2X im Straßenverkehr besteht darin, kooperative sicherheits- und effizienzrelevante Funktionen zu ermöglichen, indem Fahrzeuge periodische Statusinformationen (z.B. CAM: Position/Bewegung) und ereignisgetriebene Gefahrenmeldungen (z.B. DENM: sicherheitskritische Situationen) sowie Infrastrukturinformationen (z.B. SPAT/MAP/IVI) austauschen, um Warnungen, kooperative Manöver und Verkehrsflussoptimierung zu unterstützen.
Reasoning: fit=0.68, semantic=tangential, sources=3, diversity=0.67, contradiction=False
Supporting evidence document IDs: [4], [5], [9]

Hypothese 3: Technologisch wird V2X in der Praxis häufig als Hybrid aus direkter Funkkommunikation und zellularer Netzkommunikation realisiert: Direkte Links für V2V/V2I/V2P erfolgen entweder über ITS-G5/802.11p (ETSI C-ITS) oder über 3GPP C‑V2X PC5 („sidelink“), während V2N typischerweise über LTE/5G Uu läuft; ETSI stellt dabei für Wide-Area-V2N keine eigene Funk-Schnittstelle bereit, sondern nutzt 3GPP-Interfaces.
Reasoning: fit=0.74, semantic=inferential, sources=3, diversity=0.67, contradiction=False
Supporting evidence document IDs: [8], [6], [5]

Hypothese 4: Für interoperablen Einsatz von V2X (insbesondere für CAM/DENM) ist ein PKI-basiertes Security- und Credential-Management gemäß ETSI ITS Security Framework (u.a. TS 102 940/941/942/943, TS 103 097) erforderlich; ohne Zertifikate/Signaturmechanismen sind Authentizität und Integrität von V2X-Sicherheitsnachrichten nicht zuverlässig gewährleistbar.
Reasoning: fit=0.41, semantic=inferential, sources=3, diversity=0.67, contradiction=True
Supporting evidence document IDs: [13], [5]
Counter evidence document IDs: oA_6bJ0BQrw2ISf_Xh_a

Quellen:
[1] ConVeX ; deliverable D1.1: Deliverable D1.1: Use cases, requirements, performance evaluation criteria – https://www.tib.eu/de/suchen/id/TIBKAT%3A1729095240 (Document-ID: qxMzcZ0BQrw2ISf_SzRK; Chunk-ID: qxMzcZ0BQrw2ISf_SzRK; Chunk-Index: 11)
[2] ConVeX ; deliverable D1.1: Deliverable D1.1: Use cases, requirements, performance evaluation criteria – https://www.tib.eu/de/suchen/id/TIBKAT%3A1729095240 (Document-ID: rBMzcZ0BQrw2ISf_SzRY; Chunk-ID: rBMzcZ0BQrw2ISf_SzRY; Chunk-Index: 12)
[3] ConVeX ; deliverable D4.1: Deliverable D4.1: Roadside ITS station specification – https://www.tib.eu/de/suchen/id/TIBKAT%3A1729100252 (Document-ID: Lw_6bJ0BQrw2ISf_nSCT; Chunk-ID: Lw_6bJ0BQrw2ISf_nSCT; Chunk-Index: 2)
[4] SMART - Simulation von Mobilfunk und Automobilverhalten in Realzeit : Abschlussbericht : Berichtszeitraum: 01.09.2017-31.01.2021 – https://www.tib.eu/de/suchen/id/TIBKAT%3A185610351X (Document-ID: yBURcp0BQrw2ISf_yAHG; Chunk-ID: yBURcp0BQrw2ISf_yAHG; Chunk-Index: 34)
[5] KoMoDnext - Automatisiertes Fahren im digitalen Testfeld Düsseldorf : Schlussbericht des Verbundes : Laufzeit des Vorhabens: von: 01.01.2020 bis: 31.03.2022 – https://www.tib.eu/de/suchen/id/TIBKAT%3A1858811937 (Document-ID: qhCzbZ0BQrw2ISf_T_On; Chunk-ID: qhCzbZ0BQrw2ISf_T_On; Chunk-Index: 123)
[6] ConVeX ; deliverable D3.1: Deliverable D3.1: Comparative analysis of candidate V2X radio technologies – https://www.tib.eu/de/suchen/id/TIBKAT%3A1729097596 (Document-ID: UhMzcZ0BQrw2ISf_ozXh; Chunk-ID: UhMzcZ0BQrw2ISf_ozXh; Chunk-Index: 17)
[7] ConVeX ; deliverable D1.1: Deliverable D1.1: Use cases, requirements, performance evaluation criteria – https://www.tib.eu/de/suchen/id/TIBKAT%3A1729095240 (Document-ID: 4xMzcZ0BQrw2ISf_TzST; Chunk-ID: 4xMzcZ0BQrw2ISf_TzST; Chunk-Index: 67)
[8] ConVeX ; deliverable D3.1: Deliverable D3.1: Comparative analysis of candidate V2X radio technologies – https://www.tib.eu/de/suchen/id/TIBKAT%3A1729097596 (Document-ID: uw_6bJ0BQrw2ISf_dR_l; Chunk-ID: uw_6bJ0BQrw2ISf_dR_l; Chunk-Index: 16)
[9] ConVeX ; deliverable D1.1: Deliverable D1.1: Use cases, requirements, performance evaluation criteria – https://www.tib.eu/de/suchen/id/TIBKAT%3A1729095240 (Document-ID: sRMzcZ0BQrw2ISf_SzTS; Chunk-ID: sRMzcZ0BQrw2ISf_SzTS; Chunk-Index: 17)
[10] Schlussbericht GAIA-X 4 AMS - Advanced mobility services – https://www.tib.eu/de/suchen/id/renate-dtf%3A40b28f25992bb81ef2b12ddd6872535fb748566a (Document-ID: CxFXbp0BQrw2ISf__JQB; Chunk-ID: CxFXbp0BQrw2ISf__JQB; Chunk-Index: 29)
[11] KoMoD Schlussbericht : digitales Testfeld  Düsseldorf : 01.06.2017-31.08.2019 – https://www.tib.eu/de/suchen/id/TIBKAT%3A1713961873 (Document-ID: _w_ybJ0BQrw2ISf_LAjl; Chunk-ID: _w_ybJ0BQrw2ISf_LAjl; Chunk-Index: 85)
[12] iKoPA - Integrierte Kommunikationsplattform für automatisierte Elektrofahrzeuge : Schlussbericht 2015-12-01 bis 2018-12-31 – https://www.tib.eu/de/suchen/id/TIBKAT%3A1678869864 (Document-ID: 0RLybp0BQrw2ISf_taqk; Chunk-ID: 0RLybp0BQrw2ISf_taqk; Chunk-Index: 38)
[13] ConVeX ; deliverable D2.2: Deliverable D2.2: Final ConVeX system architecture description – https://www.tib.eu/de/suchen/id/TIBKAT%3A1729096387 (Document-ID: mg_6bJ0BQrw2ISf_Xh-T; Chunk-ID: mg_6bJ0BQrw2ISf_Xh-T; Chunk-Index: 56)

Hinweis zur Evidenzsicherheit:
- Für interoperablen Einsatz von V2X (insbesondere für CAM/DENM) ist ein PKI-basiertes Secur: begrenzte direkte Evidenz, teilweise widersprüchliche Quellenlage
