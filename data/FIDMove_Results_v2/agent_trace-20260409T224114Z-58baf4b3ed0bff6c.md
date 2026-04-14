# Live E2E Run Report

## Run Context
- Scenario ID: `datenaustausch_luftfahrt_ansätze`
- Query: Was sind die aktuelle Ansätze zum Datenaustausch in der Luftfahrt?
- Trace JSON: `C:\Users\d93666\Desktop\TSS-MoVe\tss-move-platform\backend\apps\rag\agents\logs\agent_trace-20260409T224114Z-58baf4b3ed0bff6c.json`
- Report Markdown: `C:\Users\d93666\Desktop\TSS-MoVe\tss-move-platform\backend\apps\rag\agents\logs\agent_trace-20260409T224114Z-58baf4b3ed0bff6c.md`

## Pipeline Outcome
- Current phase: `ExecutionPhase.COMPLETE`
- Outcome status: `partial`
- Hypothesis mode: `True`
- Retrieved docs: `25`
- Claims: `9`
- Missing information entries: `7`
- Trace nodes: `[]`

## Cost Summary
- Pricing reference: azure_openai/gpt-5.2 | Data Zone | Germany West Central | 2026-03-31
- Run LLM total: EUR 0.312423
- Input tokens: `99333`
- Cached input tokens: `2688`
- Output tokens: `11760`
- Priced events: `6`

### Step Costs
- research_plan_agent: EUR 0.012446 (in=1080, cached=0, out=818)
- hypothesis_gate_agent: EUR 0.005128 (in=1599, cached=0, out=192)
- database_retrieval_agent: n/a (in=0, cached=0, out=0)
- reranker_agent: EUR 0.089610 (in=41789, cached=0, out=1615)
- hypothesis_agent: EUR 0.040248 (in=14969, cached=0, out=1203)
- challenge_agent: EUR 0.048284 (in=15548, cached=0, out=1746)
- knowledge_synthesis_agent (iteration=1): EUR 0.116707 (in=24348, cached=2688, out=6186)

## Claims
- SWIM wurde im SESAR-Programm entwickelt und implementiert, um u. a. Situationsbewusstsein und Datenqualität zu verbessern sowie durch lose Kopplung die Interoperabilität zu erhöhen.
- In OPs‑TIMAl sollen zur internen Kommunikation SWIM-Services genutzt, definiert und eine SWIM-Infrastruktur implementiert werden; es werden IP/Mobilfunk, ACARS und SATCOM IP-Broadband für Boden–Bord-Transport genannt.
- OPs‑TIMAl beschreibt Datenaustausch in SWIM/XML sowie ein aus AIXM abgeleitetes XSD als SWIM-konformes Format.
- A‑CDM in Frankfurt teilt aktuelle flugereignisbezogene Daten zwischen Airline, Flughafen und Flugsicherung und nutzt transparente Regeln, um Staus zu vermeiden; Pushback wird idealerweise erst bei verfügbarer Rollkapazität freigegeben.
- IWXXM (ICAO-standardisiertes XML) wurde als Datenaustauschformat für flugmeteorologische Produkte erprobt; für manche Produkte war es nicht direkt nutzbar, daher wurden standardnahe Formate vorgeschlagen und Software entwickelt.
- Im FALKE-Projekt wurden Softwareschnittstellen zum DFS‑UTM implementiert; geplante Flugbahnen werden vor dem Flug aufbereitet und ans UTM gesendet, das u. a. Regularien prüft und perspektivisch Kollisionsvermeidungsempfehlungen unterstützt.
- Für ATM-Schnittstellen im UAV-Kontext werden Datenflüsse für Echtzeitentscheidungen bei verfügbarer Bandbreite adressiert; externe Dienste (z. B. Wetter, regulatorische Infos) fließen in die Trajektorienplanung, und UAV-Performanz/Zustand kann ans ATM geliefert werden.
- FLUIT stellt fest, dass IT-Sicherheit in der Flugsicherung historisch keine große Rolle spielte und es an konkreten Betreiber-Handlungsempfehlungen mangelt; als relevante Normen/Guidelines werden ISO/IEC 27000, IEC 62443, BSI IT‑Grundschutz und EUROCAE ED‑201/202A/203/204 genannt.
- CANSO ED‑205 wird als wesentliche industriespezifische Richtlinie für organisatorische IT‑Sicherheitsaspekte im ATM beschrieben; zusätzlich wird ein mehrstufiges Cybersecurity-Maturitätsmodell (Standard of Excellence) zur Reifebewertung genannt.

## Missing Information
- Aktuelle, explizite Referenzen zu ATM/SWIM-Architekturen außerhalb der exemplarischen SESAR-/OPs‑TIMAl-Nennungen (z. B. konkrete europäische/US‑Implementierungen, SWIM-Profile, Produktivbetrieb) fehlen in den vorliegenden Quellen.
- Konkrete Evidenz zu Luftfahrt-Datenmodellen/Standards wie AIXM/FIXM/WXXM (Versionen, Scopes, Governance) ist in den bereitgestellten Textstellen nur indirekt (AIXM als Schemaquelle; IWXXM als Wetterformat) enthalten.
- Standardisierte Spezifikationen/APIs für U‑Space/UTM-Datenaustausch (z. B. europaweite Schnittstellenstandards) werden nicht genannt; die Evidenz bleibt auf Projekt-/Prototypkontexte beschränkt.
- Detaillierte, operativ umsetzbare IT‑Security-Kontrollmaßnahmen speziell für Datenaustausch/SWIM/ATM-Schnittstellen werden in den Snippets nicht ausgeführt (nur Normen-/Guidelines-Referenzen und Gap-Feststellung).
- Aussagen zur Verbreitung und Reife von A‑CDM über den Flughafen Frankfurt hinaus (Deutschland/Europa/global) sind nicht belegt.
- Ansätze/Standards zum Airline–Airport-Datenaustausch wie AIDX/AEIDX werden in den bereitgestellten Quellen nicht adressiert.
- Ansätze zu FF‑ICE/TBO oder digitaler Flugfreigabe werden in den bereitgestellten Quellen nicht adressiert.

## Source Quality Profile
- Corpus total sources: `29`
- Selection total sources: `10`
- Selection peer-reviewed share: `0.0%`
- Selection open-access share: `0.0%`
- Selection median year: `2021.5`
- Selection high date confidence share: `0.0%`
- Significant deltas:
  - The selected sources span 2017-2023, while the broader retrieval set spans 2010-2024.
- Selected source cards:
  - Real-time analytics, prognostics and health management (RTAPHM) - Entwicklung leistungsbasierter Diensterbringung durch Digitalisierung und Optimierung der Plattformverfügbarkeit durch Datenanalytik und Prognose : Schlussbericht der TU Darmstadt : Projektlaufzeit: 01.07.2019 bis 31.03.2023, Berichtszeitraum: 01.07.2019 bis 31.03.2023 | grey_literature | editorial/curated | unknown
  - Schlussbericht - Kurzbericht (Teil 1), Eingehende Darstellung (Teil 2) zum Teilvorhaben "FLUIT" der Frequentis Comsoft GmbH im Verbund "Sicherheit für vernetztes Flugverkehrsmanagement" zum Thema Bedrohungsanalyse, Standardisierungsvorbereitung und Abgrenzung zur funktionalen Sicherheit in der Flugsicherung | grey_literature | editorial/curated | unknown
  - Verbundvorhaben LuFo OPs-TIMAl - Taktische Flugprofiloptimierung auf Basis von Echtzeitdaten mit dem Ziel der Optimierung von Kraftstoffeffizienz und Pünktlichkeit : Schlussbericht : Luftfahrtforschungsprogramm (LuFo V - 3. Aufruf) | grey_literature | editorial/curated | unknown
  - Teilvorhaben: "Entwicklung und Optimierung einer adaptiven, automatisierten Flugführung für ein unbemanntes Kippflügel Fluggerät" : Schlussbericht : FALKE: Flugsystem-assistierte Leitung komplexer Einsatzlagen : Berichtszeitraum: 01.08.2018-28.02.2022 | grey_literature | editorial/curated | unknown
  - MISSION Schlussbericht | grey_literature | editorial/curated | unknown
  - Abschlussbericht zum Vorhaben "Entwicklung einer Software zur Bereitstellung speziell aufbereiteter flugmeteorologischer Informationen für die interpretationsfreie, prozessorientierte und ergonomische Visualisierung in ATC-Anwendungen" im Verbundvorhaben WxVis4ATC im Luftfahrtforschungsprogramm LuFo, 5. Call : Laufzeit des Vorhabens: 01.07.2016-31.03.2020 | grey_literature | editorial/curated | unknown
  - Airport eMove FKZ 03EM0510C - eSchlepper & TaxiBot : Abschlussbericht | grey_literature | editorial/curated | unknown
- Enrichment metrics:
  - corpus_sources_attempted: `29`
  - corpus_sources_resolved: `29`
  - corpus_source_resolution_rate: `100.0`
  - corpus_crawl_sources_matched: `0`
  - corpus_crawl_match_rate: `0.0`
  - corpus_crawl_states_found: `0`
  - corpus_crawl_state_coverage_rate: `0.0`
  - selection_sources_attempted: `10`
  - selection_sources_resolved: `10`
  - selection_source_resolution_rate: `100.0`
  - selection_crawl_sources_matched: `0`
  - selection_crawl_match_rate: `0.0`
  - selection_crawl_states_found: `0`
  - selection_crawl_state_coverage_rate: `0.0`

## Potential Issues
- none

## Final Answer
## Direktantwort
Aktuelle Ansätze zum Datenaustausch in der Luftfahrt lassen sich in vier, heute parallel genutzte Stoßrichtungen bündeln: (1) SWIM als systemweite, serviceorientierte Informationsmanagement-Infrastruktur im ATM/Flugsicherungsumfeld, (2) operative Kollaboration am Flughafen über A‑CDM mit geteilten ereignisbezogenen Flugdaten und gemeinsamen Regeln, (3) standardisierte digitale Datenformate für konkrete Domänen (z. B. flugmeteorologische Produkte über ICAO‑IWXXM) sowie (4) Schnittstellen und Datenaustausch für die Integration unbemannter Luftfahrzeuge über UTM/U‑Space. Flankierend werden Governance- und Normenrahmen zur IT‑Sicherheit (u. a. ISO/IEC 27000, IEC 62443, BSI IT‑Grundschutz, EUROCAE ED‑201/202A/203/204, CANSO ED‑205) als Voraussetzung für vertrauenswürdigen Datenaustausch herangezogen. [1][3][4][5][7]

## SWIM als serviceorientierte Infrastruktur für ATM-übergreifenden Datenaustausch
SWIM (System Wide Information Management) wurde im Rahmen von SESAR entwickelt und implementiert, um einen systemweiten Informationsaustausch im Flugverkehrsmanagement zu ermöglichen und dabei u. a. Situationsbewusstsein und Datenqualität zu verbessern, Systemperformance und Flexibilität zu erhöhen, den Informationsaustausch kostengünstiger zu machen sowie durch lose Kopplung die Interoperabilität zu steigern. [1]

Wie SWIM in konkreten IT‑Architekturen angewendet wird, zeigt ein deutsches LuFo-Projekt zur taktischen Trajektorienoptimierung: Dort wird eine auf Microservices basierende, cloudbasierte Systemarchitektur definiert, die Datenquellen wie Flugplan-, Wetter- und ATM-Daten sowie Flugzeugparameter integriert; für die interne Kommunikation werden explizit „SWIM Services“ genutzt, die mit Unterstützung des DLR definiert werden, einschließlich Implementierung einer SWIM‑Infrastruktur. [2]

Auch die technische Ausprägung des Datenaustauschs wird in diesem Projekt konkret: Daten werden u. a. im „ARINC 633 und SWIM/XML Format“ aus einem Flugplanungssystem übergeben; zudem wird der Datenaustausch mit einem Conflict-Detection-System in „einem SWIM konformen XML Format“ beschrieben. [3] Als weiteres Beispiel für semantische Harmonisierung wird „ein HAP-interner XSD aus AIXM als SWIM konformes Format“ erstellt und ATC‑Daten werden einbezogen. [3]

## Datenflüsse Boden–Bord und heterogene Transportnetze
Aktuelle Datenaustauschansätze sind nicht nur datenmodell- und serviceorientiert, sondern berücksichtigen auch die Transportwege und ihre Randbedingungen. In der beschriebenen Trajektorienoptimierungs-Architektur werden für den Datentransport zwischen Server (Boden) und Flugzeug (Client) bodenseitig IP- und Mobilfunkverbindungen sowie im Flug ACARS und SATCOM IP‑Broadband‑Verbindungen als zu unterstützende Übertragungswege genannt; zudem sollen Datenvolumina, Latenzzeiten und Übertragungskosten abgeschätzt und optimiert werden. [2]

## Operativer Datenaustausch im Flughafenbetrieb über A‑CDM
Ein praxisnaher organisatorisch-technischer Ansatz ist Airport Collaborative Decision Making (A‑CDM), wie er am Flughafen Frankfurt praktiziert wird. Dort wird durch das Teilen „aktueller flugereignisbezogener Daten“ zwischen Fluggesellschaft, Flughafen und Flugsicherung sowie durch „einheitliche, für alle transparenten Regeln“ erreicht, dass größere Staus am Flughafen vermieden werden und unnötige Triebwerkslaufzeiten sinken. [4]

Der Bericht konkretisiert auch den operativen Mechanismus: Push‑Back-Freigaben werden idealerweise erst erteilt, wenn Flugzeuge weitgehend ungehindert Richtung Startbahn rollen können. [4] Gleichzeitig wird A‑CDM im internationalen Vergleich als „eher eine Ausnahme denn die Regel“ eingeordnet, was auf heterogene Umsetzungsstände hinweist. [4]

## Standardisierte Austauschformate für flugmeteorologische Produkte (IWXXM)
Ein weiterer Ansatz ist die Verwendung standardisierter, domänenspezifischer Austauschformate. Für flugmeteorologische Produkte wurde die Erprobung des ICAO‑standardisierten XML‑Formats IWXXM als Datenaustauschformat für verschiedene Produkte (u. a. zu Sommer-/Winterwetter-gefährdeten Flugbereichen sowie Turbulenzen und Vulkanasche) berichtet. [5]

Dabei zeigt sich auch eine typische Praxis im Übergang von Standard zu Anwendung: Die Nutzbarkeit der IWXXM‑Formate wurde für die genannten Produkte geprüft, und es wurde festgestellt, dass einige Produkte „noch nicht direkt verwendet werden konnten“; daraufhin wurden Vorschläge für Datenaustauschformate erarbeitet, die sich „möglichst eng an die standardisierten Formate anlehnen“, und eine Java‑Software zur Bereitstellung dieser Informationen entwickelt und später weiterentwickelt. [5]

## UTM/U‑Space: Datenaustausch zur Integration unbemannter Luftfahrzeuge
Mit der zunehmenden Integration von UAS entsteht ein eigener Datenaustauschstrang über UTM-Interfaces. In einem deutschen Forschungsprojekt wurden „Schnittstellen zum UTM (UAS Traffic Management) System der Deutschen Flugsicherung (DFS) implementiert“. [6]

Das UTM-System wird dabei als mehr als reine Positionsveröffentlichung beschrieben: Es soll Funktionen bereitstellen, die die sichere Integration in den Luftraum unterstützen und insbesondere in zukünftigen U‑Spaces für die Verkehrsflusssteuerung relevant sind; als Beispiele werden die „Überprüfung auf Einhaltung der Regularien“ und perspektivisch „Empfehlungen zur Kollisionsvermeidung“ genannt. [6]

Operativ relevant ist zudem, dass Softwareschnittstellen in eine Bodenstation integriert wurden, über die Informationen zur Flugmission bereitgestellt werden können: Vor dem Flug kann eine geplante Flugbahn geladen, automatisiert aufbereitet und an das UTM-System gesendet werden. [6]

Eine weitere Quelle strukturiert den Datenaustausch zwischen UAV-Betriebsarchitekturen und ATM/ATC als Designproblem: Für eine ATM‑Schnittstelle werden u. a. Anforderungen wie Bereitstellung wichtiger Daten für ATM zum Betrieb vieler UAVs und „angemessener Datenfluss zur Realisierung von Echtzeitentscheidungen bei verfügbarer Bandbreite“ genannt. [7] In der skizzierten Architektur sind externe Dienstinformationen (z. B. Wetter, regulatorische Informationen, Missionsabsichten benachbarter UAV) für die Trajektorienplanung relevant; umgekehrt kann der Operations Manager dem ATM „UAV Performanz und Zustandsdaten“ zur Verfügung stellen. [7]

## IT‑Security- und Governance-Rahmen als Voraussetzung für vertrauenswürdigen Datenaustausch
Mehr Austausch und Vernetzung erhöht den Bedarf an Sicherheits- und Governance-Leitplanken. Eine Stand-der-Technik-Analyse für den Kontext Flugsicherung hebt hervor, dass IT‑Sicherheit historisch (im Gegensatz zu Functional Safety) „keine signifikante Rolle gespielt hat“ und dass es zwar Risikoanalysen gibt, aber an konkreten Anhaltspunkten zur Risikobeurteilung sowie an Handlungsempfehlungen für Betreiber zum Betrieb eines IT‑sicheren Systems mangelt. [8]

Als relevante Vorarbeiten und Referenzrahmen werden ISO/IEC 27000, IEC 62443 sowie der IT‑Grundschutz des BSI genannt; außerdem werden domänenspezifische Dokumente wie EUROCAE ED‑201 (AISS Framework Guidance), ED‑202A, ED‑203 und ED‑204 berücksichtigt. [8]

Für das Flugverkehrsmanagement werden zudem industriespezifische organisatorische Leitlinien beschrieben: CANSO ED‑205 liefert Grundlagen für organisatorische Aspekte der IT‑Sicherheit und dient als Vorlage für den organisatorischen Aufbau bei Betreibern und Lieferanten; zusätzlich nennt die Quelle einen von CANSO eingeführten „Standard of Excellence in Cybersecurity“ als mehrstufiges Maturitätsmodell zur Bewertung der eigenen IT‑Sicherheitsreife und des Handlungsbedarfs (auch gegenüber Lieferanten). [9]

## Einordnung: Was „aktuell“ in der Praxis bedeutet
Über die Quellen hinweg zeigt sich, dass „aktuelle Ansätze“ typischerweise eine Kombination aus (a) Architektur-/Integrationskonzepten (SWIM, Microservices/Cloud, UTM‑Interfaces), (b) standardisierten Datenrepräsentationen (z. B. SWIM/XML, IWXXM; projektspezifische Schemata nahe an Standards) und (c) kollaborativen Betriebsverfahren (A‑CDM) sind, die durch IT‑Security‑ und Governance-Rahmenbedingungen abgesichert werden sollen. [1][2][3][4][5][8][9]

Gleichzeitig wird die Heterogenität des Reifegrades sichtbar: A‑CDM wird als Ausnahme im internationalen Vergleich bezeichnet [4], IWXXM ist für bestimmte Produkte nicht direkt nutzbar und erfordert standardnahe Erweiterungen [5], und für Flugsicherungsbetreiber werden fehlende konkrete IT‑Security‑Handlungsempfehlungen konstatiert. [8]

## Hypothesenbewertung
Hypothese 7a00c8f8-a57b-4191-bb9c-0ce67ed0ab0c (SWIM in deutschen ATM-/Airline-IT-Projekten)
Die inhaltlichen Kernelemente (SWIM-Services, SWIM/XML, AIXM-abgeleitete XSD) sind im OPs‑TIMAl-Projekt klar belegt; die Verallgemeinerung auf „aktuelle ATM/Flugsicherungs- und Airline-IT-Projekte in Deutschland“ ist mit den vorliegenden Quellen jedoch nur exemplarisch abgedeckt. [2][3]

Hypothese 9e8f640b-1f24-4d2d-9464-b4dbc844a80b (A‑CDM als Datenteilungs- und Regelansatz)
Die Beschreibung (Teilen aktueller ereignisbezogener Daten zwischen Airline/Flughafen/Flugsicherung; transparente Regeln; Pushback-Synchronisation) ist für Frankfurt direkt belegt; zur Breite der Nutzung über diesen Kontext hinaus liefern die Quellen keine belastbare Abdeckung. [4]

Hypothese 9d108123-9b42-4e87-8363-ee62aa06f6c7 (Security-Governance- und Normenrahmen)
Die genannten Normen- und Leitliniensets sowie die Einschätzung eines Mangels an konkreten Betreiberempfehlungen werden direkt gestützt; Details zu konkreten Kontrollen/Operationalisierung sind in den vorliegenden Textstellen nicht ausgeführt. [8][9]

Hypothese 499b4f2f-4e46-406a-9701-afcc1cc3c28e (UTM/U‑Space-Integration über Schnittstellen)
Die Kernaussage (UTM‑Schnittstellen, Missions-/Trajektoriendatenübermittlung, Prüfung gegen Restriktionen/Regularien, perspektivische Kollisionsvermeidung) ist im FALKE-Kontext gut belegt; Aussagen zur Standardisierung oder europaweiten Spezifikationen bleiben offen. [6]

Missing information:
- Aktuelle, explizite Referenzen zu ATM/SWIM-Architekturen außerhalb der exemplarischen SESAR-/OPs‑TIMAl-Nennungen (z. B. konkrete europäische/US‑Implementierungen, SWIM-Profile, Produktivbetrieb) fehlen in den vorliegenden Quellen.
- Konkrete Evidenz zu Luftfahrt-Datenmodellen/Standards wie AIXM/FIXM/WXXM (Versionen, Scopes, Governance) ist in den bereitgestellten Textstellen nur indirekt (AIXM als Schemaquelle; IWXXM als Wetterformat) enthalten.
- Standardisierte Spezifikationen/APIs für U‑Space/UTM-Datenaustausch (z. B. europaweite Schnittstellenstandards) werden nicht genannt; die Evidenz bleibt auf Projekt-/Prototypkontexte beschränkt.
- Detaillierte, operativ umsetzbare IT‑Security-Kontrollmaßnahmen speziell für Datenaustausch/SWIM/ATM-Schnittstellen werden in den Snippets nicht ausgeführt (nur Normen-/Guidelines-Referenzen und Gap-Feststellung).
- Aussagen zur Verbreitung und Reife von A‑CDM über den Flughafen Frankfurt hinaus (Deutschland/Europa/global) sind nicht belegt.
- Ansätze/Standards zum Airline–Airport-Datenaustausch wie AIDX/AEIDX werden in den bereitgestellten Quellen nicht adressiert.
- Ansätze zu FF‑ICE/TBO oder digitaler Flugfreigabe werden in den bereitgestellten Quellen nicht adressiert.

Aufgestellte Hypothesen:
Hypothese 1: In aktuellen ATM/Flugsicherungs- und Airline-IT-Projekten in Deutschland wird SWIM als serviceorientierte Infrastruktur für HAP-interne (und teils HAP-übergreifende) Kommunikation genutzt; Daten werden dabei in SWIM-konformen XML-Formaten bereitgestellt und u. a. aus AIXM abgeleitete XSD-Schemata eingesetzt, um interoperablen Austausch zwischen Backend-Diensten und luftfahrzeugseitigen Clients zu ermöglichen.
Reasoning: fit=0.56, semantic=inferential, sources=3, diversity=0.67, contradiction=False
Supporting evidence document IDs: [2], [3], KBUrcp0BQrw2ISf_NEfz

Hypothese 2: Im operativen Flughafenbetrieb wird Airport Collaborative Decision Making (A‑CDM) als organisatorisch-technischer Ansatz genutzt, bei dem Airline, Flughafen und Flugsicherung aktuelle ereignisbezogene Flugdaten teilen und einheitliche, transparente Regeln anwenden, um Bodenstaus zu vermeiden und Abläufe (z. B. Pushback-Freigaben) zu synchronisieren.
Reasoning: fit=0.61, semantic=inferential, sources=2, diversity=0.50, contradiction=False
Supporting evidence document IDs: [4], aRLZbp0BQrw2ISf_iIm3

Hypothese 3: Für vertrauenswürdigen Datenaustausch im Flugverkehrsmanagement (ATM) werden IT‑Security-Governance- und Normenrahmen (u. a. ISO/IEC 27000, IEC 62443, BSI IT‑Grundschutz) sowie domänenspezifische Leitlinien (EUROCAE ED‑201/202A/203/204 und CANSO ED‑205 inkl. Cybersecurity-Maturity-Modell) herangezogen; zugleich besteht laut Stand-der-Technik-Analyse ein Mangel an konkreten, betriebsorientierten Handlungsempfehlungen speziell für Flugsicherungsbetreiber.
Reasoning: fit=0.78, semantic=inferential, sources=4, diversity=0.67, contradiction=False
Supporting evidence document IDs: [8], VRUwcp0BQrw2ISf_Mlcv, [9], AhHRbZ0BQrw2ISf_g0Kt

Hypothese 4: Die Integration unbemannter Luftfahrzeuge in zukünftigen U‑Space‑Umgebungen erfolgt über UTM-Schnittstellen, über die UAS-Bodenstationen u. a. Missions-/Trajektoriendaten (geplante Flugbahnen) an ein UTM-System übermitteln, das diese Daten gegen Restriktionsgebiete/Regularien prüft und perspektivisch Funktionen wie Empfehlungen zur Kollisionsvermeidung unterstützt.
Reasoning: fit=0.72, semantic=inferential, sources=2, diversity=0.50, contradiction=False
Supporting evidence document IDs: [6], VxC0bZ0BQrw2ISf_0fhK

Quellen:
[1] MISSION Schlussbericht – https://www.tib.eu/de/suchen/id/TIBKAT%3A1799935035 (Document-ID: hRBybZ0BQrw2ISf_Oj96; Chunk-ID: hRBybZ0BQrw2ISf_Oj96; Chunk-Index: 8)
[2] Verbundvorhaben LuFo OPs-TIMAl - Taktische Flugprofiloptimierung auf Basis von Echtzeitdaten mit dem Ziel der Optimierung von Kraftstoffeffizienz und Pünktlichkeit : Schlussbericht : Luftfahrtforschungsprogramm (LuFo V - 3. Aufruf) – https://www.tib.eu/de/suchen/id/TIBKAT%3A1881571580 (Document-ID: HhUrcp0BQrw2ISf_NEeK; Chunk-ID: HhUrcp0BQrw2ISf_NEeK; Chunk-Index: 18)
[3] Verbundvorhaben LuFo OPs-TIMAl - Taktische Flugprofiloptimierung auf Basis von Echtzeitdaten mit dem Ziel der Optimierung von Kraftstoffeffizienz und Pünktlichkeit : Schlussbericht : Luftfahrtforschungsprogramm (LuFo V - 3. Aufruf) – https://www.tib.eu/de/suchen/id/TIBKAT%3A1881571580 (Document-ID: 2xHKbZ0BQrw2ISf_1zF2; Chunk-ID: 2xHKbZ0BQrw2ISf_1zF2; Chunk-Index: 28)
[4] Airport eMove FKZ 03EM0510C - eSchlepper & TaxiBot : Abschlussbericht – https://www.tib.eu/de/suchen/id/TIBKAT%3A1666141399 (Document-ID: 6w6wbJ0BQrw2ISf_IaNA; Chunk-ID: 6w6wbJ0BQrw2ISf_IaNA; Chunk-Index: 48)
[5] Abschlussbericht zum Vorhaben "Entwicklung einer Software zur Bereitstellung speziell aufbereiteter flugmeteorologischer Informationen für die interpretationsfreie, prozessorientierte und ergonomische Visualisierung in ATC-Anwendungen" im Verbundvorhaben WxVis4ATC im Luftfahrtforschungsprogramm LuFo, 5. Call : Laufzeit des Vorhabens: 01.07.2016-31.03.2020 – https://www.tib.eu/de/suchen/id/TIBKAT%3A1748100726 (Document-ID: pQ8ObZ0BQrw2ISf_gFMM; Chunk-ID: pQ8ObZ0BQrw2ISf_gFMM; Chunk-Index: 16)
[6] Teilvorhaben: "Entwicklung und Optimierung einer adaptiven, automatisierten Flugführung für ein unbemanntes Kippflügel Fluggerät" : Schlussbericht : FALKE: Flugsystem-assistierte Leitung komplexer Einsatzlagen : Berichtszeitraum: 01.08.2018-28.02.2022 – https://www.tib.eu/de/suchen/id/TIBKAT%3A1860108679 (Document-ID: dxUVcp0BQrw2ISf_EQw3; Chunk-ID: dxUVcp0BQrw2ISf_EQw3; Chunk-Index: 29)
[7] Real-time analytics, prognostics and health management (RTAPHM) - Entwicklung leistungsbasierter Diensterbringung durch Digitalisierung und Optimierung der Plattformverfügbarkeit durch Datenanalytik und Prognose : Schlussbericht der TU Darmstadt : Projektlaufzeit: 01.07.2019 bis 31.03.2023, Berichtszeitraum: 01.07.2019 bis 31.03.2023 – https://www.tib.eu/de/suchen/id/TIBKAT%3A1897715218 (Document-ID: QhU4cp0BQrw2ISf_4mhT; Chunk-ID: QhU4cp0BQrw2ISf_4mhT; Chunk-Index: 40)
[8] Schlussbericht - Kurzbericht (Teil 1), Eingehende Darstellung (Teil 2) zum Teilvorhaben "FLUIT" der Frequentis Comsoft GmbH im Verbund "Sicherheit für vernetztes Flugverkehrsmanagement" zum Thema Bedrohungsanalyse, Standardisierungsvorbereitung und Abgrenzung zur funktionalen Sicherheit in der Flugsicherung – https://www.tib.eu/de/suchen/id/TIBKAT%3A1887449884 (Document-ID: 7hHRbZ0BQrw2ISf_g0E3; Chunk-ID: 7hHRbZ0BQrw2ISf_g0E3; Chunk-Index: 1)
[9] Schlussbericht - Kurzbericht (Teil 1), Eingehende Darstellung (Teil 2) zum Teilvorhaben "FLUIT" der Frequentis Comsoft GmbH im Verbund "Sicherheit für vernetztes Flugverkehrsmanagement" zum Thema Bedrohungsanalyse, Standardisierungsvorbereitung und Abgrenzung zur funktionalen Sicherheit in der Flugsicherung – https://www.tib.eu/de/suchen/id/TIBKAT%3A1887449884 (Document-ID: aRUwcp0BQrw2ISf_Mle9; Chunk-ID: aRUwcp0BQrw2ISf_Mle9; Chunk-Index: 21)

Hinweis zur Evidenzsicherheit:
- In aktuellen ATM/Flugsicherungs- und Airline-IT-Projekten in Deutschland wird SWIM als ser: mittlere Evidenzabdeckung
- Im operativen Flughafenbetrieb wird Airport Collaborative Decision Making (A‑CDM) als orga: mittlere Evidenzabdeckung
