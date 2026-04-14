# Live E2E Run Report

## Run Context
- Scenario ID: `cbm_vs_klassische_instandhaltung`
- Query: Wie unterscheidet sich die zustandsorientierte Instandhaltung (CBM)  von herkömmlichen Methoden?
- Trace JSON: `C:\Users\d93666\Desktop\TSS-MoVe\tss-move-platform\backend\apps\rag\agents\logs\agent_trace-20260409T222046Z-ab9eda0ac6aae08c.json`
- Report Markdown: `C:\Users\d93666\Desktop\TSS-MoVe\tss-move-platform\backend\apps\rag\agents\logs\agent_trace-20260409T222046Z-ab9eda0ac6aae08c.md`

## Pipeline Outcome
- Current phase: `ExecutionPhase.COMPLETE`
- Outcome status: `partial`
- Hypothesis mode: `True`
- Retrieved docs: `22`
- Claims: `5`
- Missing information entries: `3`
- Trace nodes: `[]`

## Cost Summary
- Pricing reference: azure_openai/gpt-5.2 | Data Zone | Germany West Central | 2026-03-31
- Run LLM total: EUR 0.349358
- Input tokens: `114011`
- Cached input tokens: `0`
- Output tokens: `12443`
- Priced events: `9`

### Step Costs
- research_plan_agent: EUR 0.012709 (in=1089, cached=0, out=837)
- hypothesis_gate_agent: EUR 0.005498 (in=1626, cached=0, out=217)
- database_retrieval_agent: n/a (in=0, cached=0, out=0)
- reranker_agent: EUR 0.065521 (in=30825, cached=0, out=1147)
- hypothesis_agent: EUR 0.025770 (in=8154, cached=0, out=950)
- challenge_agent: EUR 0.036142 (in=8813, cached=0, out=1662)
- database_retrieval_agent (iteration=1): n/a (in=0, cached=0, out=0)
- reranker_agent (iteration=1): EUR 0.029313 (in=13410, cached=0, out=561)
- hypothesis_agent (iteration=1): EUR 0.035521 (in=13256, cached=0, out=1056)
- challenge_agent (iteration=1): EUR 0.045411 (in=13621, cached=0, out=1768)
- knowledge_synthesis_agent (iteration=2): EUR 0.093473 (in=23217, cached=0, out=4245)

## Claims
- CBM terminiert Instandhaltungsmaßnahmen auf Basis gesammelter Zustandsinformationen/Messdaten.
- In schiffstechnischen Anlagen gibt es regelmäßige Inspektionsintervalle durch Klassifikationsgesellschaften; Kostensenkung erfordert regelmäßige zustandsrelevante Messdaten.
- Im maritimen Antriebsstrang werden CBM-Potenziale u.a. über permanente Temperatur-/Verschleißüberwachung adressiert; CoMoGear zielt auf ein drahtloses, energieautarkes Sensornetzwerk und nennt Messgrößen wie Drehmoment, Drehzahl, Temperatur und Verschleißzustand.
- PdM nutzt Vorhersagealgorithmen, um Fehlerrisiko zu zukünftigen Zeitpunkten abzuschätzen, und verwendet dafür Sensordaten/Zustandsindikatoren sowie statistische und ingenieurtechnische Ansätze.
- In einem Prognosekonzept werden Reduktion ungeplanter Ausfälle und die Verlagerung von präventiver zu zustandsorientierter Instandhaltung (CBM) als Effekte genannt; präventive Inspektionen können bei wirksamer ISHM-Überwachung entfallen; RUL ist zentrale Eingangsgröße für Maintenance Planner.

## Missing Information
- Direkte, normative Definitionen/Taxonomien (z.B. ISO 17359/ISO 13374 oder vergleichbare Standards) zur sauberen begrifflichen Abgrenzung von CBM gegenüber präventiver/korrektiver Instandhaltung sowie zur Trennung CBM vs. PdM sind in den vorliegenden Quellen nicht enthalten.
- Quantitative maritime Vergleichsstudien (CBM vs. intervall-/reaktiv) mit Kennzahlen wie Downtime, Kosten oder Verfügbarkeit sind in den bereitgestellten Ausschnitten nicht belegt (nur qualitative Aussagen wie „signifikante Verbesserungen“ bzw. Kostenargumentation).
- Regelwerks-/Klassifikationsanforderungen speziell für den Einsatz von Condition Monitoring/CBM als Ersatz für Inspektionsintervalle im maritimen Bereich (z.B. „class notations“, anerkannte Nachweisprozesse) sind in den vorliegenden Quellen nicht konkret beschrieben.

## Source Quality Profile
- Corpus total sources: `11`
- Selection total sources: `10`
- Selection peer-reviewed share: `0.0%`
- Selection open-access share: `0.0%`
- Selection median year: `2019.5`
- Selection high date confidence share: `10.0%`
- Significant deltas: none
- Selected source cards:
  - WIR! - Verbundprojekt: Digitale Zwillinge für Prozessoptimierung und vorausschauende Instandhaltung (DIZPROVI); Teilvorhaben: Vorausschauende Instandhaltung für industrielle Mahlanlagen | grey_literature | editorial/curated | unknown
  - Schlussbericht zum BMWi-Projekt "CoMoGear" im Rahmen des Forschungsprogramms "Maritime Technologien der nächsten Generation" des BMWi mit dem Titel "Condition Monitoring of Marine Gearboxes based on Wireless, Energy-Autonomous Sensor Nodes" : Einzelvorhabenbezeichnung: Drahtlose energieautarke Datenübertragung von Sensorsignalen in Metallumgebung - DraSeMe : Berichtszeitraum: 01.08.2016 bis 31.12.2019 | grey_literature | editorial/curated | unknown
  - OMAHA - Overall management architecture for health analysis : Abschlussbericht OMAHA | grey_literature | editorial/curated | unknown
  - Einsatz drahtloser Kommunikationstechnologie zur wirtschaftlichen Zustandsüberwachung von Schiffsgetrieben - DriveCoM : Schlussbericht | grey_literature | editorial/curated | unknown
- Enrichment metrics:
  - corpus_sources_attempted: `11`
  - corpus_sources_resolved: `11`
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
## Direkte Abgrenzung: CBM vs. herkömmliche Instandhaltung
Zustandsorientierte Instandhaltung (Condition-Based Maintenance, CBM) unterscheidet sich von herkömmlichen Instandhaltungsansätzen dadurch, dass Instandhaltungsmaßnahmen nicht primär nach festen Inspektions- oder Wartungsintervallen geplant werden, sondern aus regelmäßig erfassten zustandsrelevanten Informationen/Messdaten abgeleitet und terminiert werden. [3]

## Begriffs- und Strategieabgrenzung
### CBM als datenbasierte Strategie zur Maßnahmenableitung
CBM wird als Strategie beschrieben, bei der „auf Basis von gesammelten Informationen“ Instandhaltungsmaßnahmen abgeleitet und terminiert werden. [3]

### Unterschied zur intervall-/inspektionsbasierten Instandhaltung (präventiv)
Im maritimen Umfeld unterliegen hoch belastete Anlagen (z. B. Getriebe) regelmäßigen Inspektionsintervallen durch Klassifikationsgesellschaften. [3]
Eine Reduzierung der Kosten, die durch Stillstand des Schiffes und die Inspektion selbst verursacht werden, wird daran geknüpft, dass regelmäßig zustandsrelevante Messdaten an den Maschinen erfasst werden (also nicht ausschließlich kalender-/intervallgetrieben geplant wird). [3]

### Unterschied zur reaktiven/korrektiven Instandhaltung
Ein zentraler Nutzen von Prognose- und Health-Management-Konzepten ist die Erkennung bevorstehender Ausfälle; als resultierender Effekt wird u. a. die Reduktion ungeplanter Ereignisse aufgrund von Ausfällen sowie die Ermöglichung von CBM (Verlagerung von präventiver zu zustandsorientierter Instandhaltung) genannt. [6]
Darüber hinaus können präventive Inspektionen entfallen, wenn das entsprechende Bauteil wirksam durch ein ISHM-System überwacht wird. [6]

## Maritime Spezifika: warum CBM anders „funktioniert“
### Messdatenerfassung als Voraussetzung für wirtschaftliche Effekte
Für schiffstechnische Anlagen wird explizit herausgestellt, dass eine Kostensenkung im Zusammenhang mit Stillstand und Inspektion nur erreicht werden kann, wenn regelmäßig zustandsrelevante Messdaten erfasst werden. [3]

### Condition-Monitoring-Infrastruktur und typische Messgrößen im Antriebsstrang
Im Projekt „CoMoGear“ wird CBM im Umfeld des Schiffsantriebsstrangs adressiert; genannt wird u. a., dass eine permanente messtechnische Überwachung (z. B. Temperaturen in der Lamellenkupplung und Verschleiß) zu signifikanten Verbesserungen von Dynamic Positioning und Betriebssicherheit führen würde. [2]
Als Ziel wird die Entwicklung und prototypische Implementierung eines energieautarken, drahtlosen Sensornetzwerks zur Zustandsdiagnose von hoch belasteten, rotierenden Bauteilen im Schiffsgetriebe beschrieben; hierfür sollen Messdaten zu Drehmoment, Drehzahl, Temperatur und Verschleißzustand im Öl umspülten Getriebe ermöglicht werden. [2]

### Verbreitungs-/Adoptionsaspekt (Hürde gegenüber herkömmlichen Verfahren)
Für klassifizierte Schiffe wird berichtet, dass nur ca. 2 % die Möglichkeiten von CBM im Umfeld des Schiffsantriebsstrangs nutzen, da die Investitionsvolumina als zu hoch angesehen werden. [2]

## Entscheidungslogik: Diagnose vs. Prognose und die Rolle von PdM
Predictive Maintenance (PdM) wird als vorausschauende Instandhaltung beschrieben, die auf präziser Analyse und Modellierung des Schadens-/Verschleißzustands basiert und mittels Vorhersagealgorithmen das Fehlerrisiko zu unterschiedlichen Zeitpunkten abschätzt; diese Algorithmen nutzen u. a. Sensordaten, Zustandsindikatoren und statistische sowie ingenieurtechnische Ansätze. [5]
In dieser Quelle werden Vorteile von PdM gegenüber „einfacheren Instandhaltungsstrategien“ explizit auch gegenüber zustandsbasierter Instandhaltung genannt. [5]
Gleichzeitig wird in einem Health-Management-/Prognosekonzept die Vorhersage der Remaining Useful Life (RUL) als wesentlicher Nutzen und als entscheidende Eingangsgröße für einen Maintenance Planner beschrieben, wobei damit sowohl eine Reduktion ungeplanter Ereignisse durch Ausfälle als auch die Ermöglichung von CBM (Verlagerung von präventiver zu zustandsorientierter Instandhaltung) verbunden wird. [6]
Damit zeigen die Quellen eine in der Praxis relevante Überlappung: CBM kann (je nach Ausgestaltung) eng mit prognosebasierten Größen wie RUL gekoppelt sein, während PdM definitorisch über Vorhersagealgorithmen und Risikoschätzung zu zukünftigen Zeitpunkten abgegrenzt wird. [5][6]

## Kompakte Gegenüberstellung
- Auslöser/Trigger
  - Herkömmlich präventiv: feste Inspektionsintervalle (im maritimen Kontext u. a. durch Klassifikationsgesellschaften geprägt). [3]
  - CBM: abgeleitet/terminiert aus gesammelten Zustandsinformationen; wirtschaftliche Effekte sind an regelmäßige Messdatenerfassung gekoppelt. [3]
- Zielwirkung
  - Herkömmlich (ohne wirksame Zustandsüberwachung): Inspektionen verursachen Stillstand und Kosten. [3]
  - CBM (mit wirksamer Überwachung/Health-Management): Reduktion ungeplanter Ausfallereignisse; potenziell Entfall präventiver Inspektionen bei wirksamer ISHM-Überwachung. [6]
- Technische Grundlage
  - CBM im maritimen Antriebsstrang: Sensorik/Monitoring (z. B. Temperatur, Drehmoment, Drehzahl, Verschleißzustand im Öl) und Systeme wie drahtlose, energieautarke Sensornetzwerke. [2]

## Einordnung der Evidenz und Grenzen
Die maritime Abgrenzung zwischen CBM und intervallbasierter Inspektion/Wartung ist direkt durch Quellen zu schiffstechnischen Anlagen (Getriebe/Antriebsstrang) belegt. [2][3]
Die Abgrenzung zu PdM ist nur teilweise definitorisch abgesichert, weil PdM zwar klar über Vorhersagealgorithmen und zukünftige Risikoschätzung beschrieben wird, CBM aber in anderen Quellen zugleich mit RUL-getriebenen Planungsansätzen verknüpft wird; eine harte Trennlinie „CBM ohne Prognose“ wird dadurch nicht eindeutig gestützt. [5][6]

Missing information:
- Direkte, normative Definitionen/Taxonomien (z.B. ISO 17359/ISO 13374 oder vergleichbare Standards) zur sauberen begrifflichen Abgrenzung von CBM gegenüber präventiver/korrektiver Instandhaltung sowie zur Trennung CBM vs. PdM sind in den vorliegenden Quellen nicht enthalten.
- Quantitative maritime Vergleichsstudien (CBM vs. intervall-/reaktiv) mit Kennzahlen wie Downtime, Kosten oder Verfügbarkeit sind in den bereitgestellten Ausschnitten nicht belegt (nur qualitative Aussagen wie „signifikante Verbesserungen“ bzw. Kostenargumentation).
- Regelwerks-/Klassifikationsanforderungen speziell für den Einsatz von Condition Monitoring/CBM als Ersatz für Inspektionsintervalle im maritimen Bereich (z.B. „class notations“, anerkannte Nachweisprozesse) sind in den vorliegenden Quellen nicht konkret beschrieben.

Aufgestellte Hypothesen:
Hypothese 1: CBM unterscheidet sich von zeit-/nutzungsbasierter präventiver Instandhaltung dadurch, dass Instandhaltungsmaßnahmen nicht nach festen Intervallen, sondern auf Basis regelmäßig erfasster zustandsrelevanter Messdaten abgeleitet und terminiert werden; dadurch können (im maritimen Kontext) Inspektions- und Stillstandskosten sinken, sofern kontinuierliche Zustandsdaten verfügbar sind.
Reasoning: fit=0.53, semantic=tangential, sources=3, diversity=0.67, contradiction=False
Supporting evidence document IDs: [3]

Hypothese 2: CBM unterscheidet sich von reaktiver/korrektiver Instandhaltung dadurch, dass technische Zustandsüberwachung (z.B. ISHM/HUMS/CMS) die Substitution geplanter bzw. ausfallgetriebener Eingriffe ermöglicht und ungeplante Ausfälle reduzieren kann; im Extremfall können präventive Inspektionen entfallen, wenn die Komponente wirksam überwacht wird.
Reasoning: fit=0.66, semantic=inferential, sources=2, diversity=0.50, contradiction=False
Supporting evidence document IDs: [6]

Hypothese 3: CBM erfordert typischerweise eine Condition-Monitoring-Infrastruktur, die zustandsrelevante Messgrößen (z.B. Drehmoment, Drehzahl, Temperatur, Öl-/Verschleißzustand) kontinuierlich/regelmäßig erfasst; ohne diese Datengrundlage ist eine kostenwirksame Ablösung von Inspektionsintervallen (z.B. im Schiffsantriebsstrang) nur begrenzt möglich.
Reasoning: fit=0.50, semantic=inferential, sources=2, diversity=0.50, contradiction=False
Supporting evidence document IDs: [2], [3]

Hypothese 4: Predictive Maintenance (PdM) grenzt sich von CBM dadurch ab, dass PdM zusätzlich Vorhersagealgorithmen auf Sensordaten/Zustandsindikatoren anwendet, um das Fehlerrisiko zu zukünftigen Zeitpunkten bzw. eine RUL abzuschätzen; CBM kann dagegen auf aktueller Zustandsdiagnose zur Maßnahmenableitung/Terminierung beruhen, ohne zwingend eine Zeit-prognostische Komponente zu benötigen.
Reasoning: fit=0.47, semantic=inferential, sources=2, diversity=0.50, contradiction=True
Supporting evidence document IDs: [5]
Counter evidence document IDs: [6]

Quellen:
[1] Statustagung Schifffahrt und Meerestechnik : Tagungsband der Statustagung 2011 – https://www.tib.eu/de/suchen/id/TIBKAT%3A689495544 (Document-ID: nBU5c50BQrw2ISf_VP1H; Chunk-ID: nBU5c50BQrw2ISf_VP1H; Chunk-Index: 199)
[2] Schlussbericht zum BMWi-Projekt "CoMoGear" im Rahmen des Forschungsprogramms "Maritime Technologien der nächsten Generation" des BMWi mit dem Titel "Condition Monitoring of Marine Gearboxes based on Wireless, Energy-Autonomous Sensor Nodes" : Einzelvorhabenbezeichnung: Drahtlose energieautarke Datenübertragung von Sensorsignalen in Metallumgebung - DraSeMe : Berichtszeitraum: 01.08.2016 bis 31.12.2019 – https://www.tib.eu/de/suchen/id/TIBKAT%3A1741721903 (Document-ID: 2g8FbZ0BQrw2ISf_Zjz9; Chunk-ID: 2g8FbZ0BQrw2ISf_Zjz9; Chunk-Index: 2)
[3] Einsatz drahtloser Kommunikationstechnologie zur wirtschaftlichen Zustandsüberwachung von Schiffsgetrieben - DriveCoM : Schlussbericht – https://www.tib.eu/de/suchen/id/TIBKAT%3A1004951493 (Document-ID: _hF0bp0BQrw2ISf_HeSq; Chunk-ID: _hF0bp0BQrw2ISf_HeSq; Chunk-Index: 4)
[4] Sicheres Fliegen senkrechtstartender elektrischer RPAs (SiFliegeR) : Schlussbericht der TU Darmstadt : Berichtszeitraum: 01.01.2016 bis 31.05.2019 – https://www.tib.eu/de/suchen/id/TIBKAT%3A1688535675 (Document-ID: zg7lbJ0BQrw2ISf_ruTd; Chunk-ID: zg7lbJ0BQrw2ISf_ruTd; Chunk-Index: 32)
[5] WIR! - Verbundprojekt: Digitale Zwillinge für Prozessoptimierung und vorausschauende Instandhaltung (DIZPROVI); Teilvorhaben: Vorausschauende Instandhaltung für industrielle Mahlanlagen – https://www.tib.eu/de/suchen/id/renate-dtf%3A06ebbc631d38d218e1ee483b2bdc54531d74e45c (Document-ID: YhaWc50BQrw2ISf_r3_g; Chunk-ID: YhaWc50BQrw2ISf_r3_g; Chunk-Index: 2)
[6] OMAHA - Overall management architecture for health analysis : Abschlussbericht OMAHA – https://www.tib.eu/de/suchen/id/TIBKAT%3A1027486762 (Document-ID: ghKlbp0BQrw2ISf_NTaA; Chunk-ID: ghKlbp0BQrw2ISf_NTaA; Chunk-Index: 109)
[7] OMAHA - Overall management architecture for health analysis – https://www.tib.eu/de/suchen/id/TIBKAT%3A1027483321 (Document-ID: _BKkbp0BQrw2ISf__jVX; Chunk-ID: _BKkbp0BQrw2ISf__jVX; Chunk-Index: 83)
[8] Entwicklung intelligenter, KI-basierter HUMS Systeme für Hubschraubergetriebe und e-Aktuatoren zur Rotorsteuerung - smartHUMS – https://www.tib.eu/de/suchen/id/renate-dtf%3A4c9546ab052f4735384b67bc6ca46400e0dcba95 (Document-ID: RA1HbJ0BQrw2ISf_PK6f; Chunk-ID: RA1HbJ0BQrw2ISf_PK6f; Chunk-Index: 74)
[9] "Sensorik, digitale Interaktion, Maintenance und Augmented Reality in Straßenbahnen" : gemeinsamer Schlussbericht zum Verbundprojekt: SensoDIMARiS – https://www.tib.eu/de/suchen/id/TIBKAT%3A1854444867 (Document-ID: VhCvbZ0BQrw2ISf_5-uH; Chunk-ID: VhCvbZ0BQrw2ISf_5-uH; Chunk-Index: 25)

Hinweis zur Evidenzsicherheit:
- CBM unterscheidet sich von zeit-/nutzungsbasierter präventiver Instandhaltung dadurch, das: mittlere Evidenzabdeckung
- CBM erfordert typischerweise eine Condition-Monitoring-Infrastruktur, die zustandsrelevant: mittlere Evidenzabdeckung
- Predictive Maintenance (PdM) grenzt sich von CBM dadurch ab, dass PdM zusätzlich Vorhersag: begrenzte direkte Evidenz, teilweise widersprüchliche Quellenlage
