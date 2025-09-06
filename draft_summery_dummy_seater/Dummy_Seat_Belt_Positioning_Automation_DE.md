# Crash-Lastfall — Knie-Mapping & Aufprallbewertung (Setup)

## Zweck
- Vorbereitung des FE-Modells für eine Euro NCAP-konforme Bewertung des unteren Körperbereichs  
- Sicherstellung einer realistischen Positionierung des Dummys und Konfiguration des Rückhaltesystems

## Dummy-, Sitz- & Sicherheitsgurt-Setup
- **Sitz:** Import und Ausrichtung der Sitzgeometrie mit korrektem H-Punkt und Sitzhaltung über ANSA/VE  
- **Virtueller Dummy:** Positionierung von ATD H395% auf der Fahrerseite & ATD H350/95% auf der Beifahrerseite gemäß EU NCAP über VE  
- **Sicherheitsgurt:** Modellierung von Aufroller, Gurtstraffer und Befestigungspunkten; Überprüfung der Führung über den Dummy | referenziert im Belt-Module  
- **Vorspannung:** Anwendung der anfänglichen Gurtspannung und Dummy-Setzung über VE, ProDSiG & Belt-Module-Tools

## Randbedingungen
- Fahrzeugmodell an globalen Befestigungen fixiert; umliegende Struktur für realistische Lastpfade enthalten  
- Definition der Anfangsgeschwindigkeit und entweder Standard- oder Testimpulsbelastung  
- Aktivierung von Airbag-Modulen für Knie-Mapping

## Vorabprüfungen
- Definition von Dummy-Kontakten (Haut-zu-Armaturenbrett, Knie-zu-unteres Armaturenbrett)  
- Verhalten des Sicherheitsgurts bei Rückzug und Vorspannung im ersten Lastschritt  
- Sicherstellung, dass alle Sensoren/Kanäle (Femurkraft, Beckenverschiebung) aktiv sind

<img src="https://github.com/Dummy-Seater/Dummy-Seater-Automation/blob/main/Docu/Images/Knee-impact-setup.png" alt="Knee-impact-setup" width="50%" />

---

# Automatisierung der Dummy-, Sitz- & Gurtpositionierung

## Ziel
- Automatisierung der realistischen Positionierung des Dummys und Einrichtung des Rückhaltesystems für Crashsimulationen  
- Sicherstellung der Reproduzierbarkeit und Einhaltung gesetzlicher Vorschriften (z. B. Euro NCAP)

## Schrittübersicht
- **🧍 Dummy-Positionierung:** Ausrichtung des H-Punkts und der Haltung des Dummys mit VE/ANSA. Anwendung anthropometrischer Regeln und Validierung der anatomischen Ausrichtung  
- **🪑 Sitzvorspannung:** Simulation der schwerkraftbasierten Setzung des Dummys auf dem Sitz über quasistatische Analyse. Erfassung von Sitzverformung und Kontaktkräften  
- **🔗 Gurt-Systemeinrichtung (Parametrisch):**  
  - Verwendung parameterbasierter Eingaben für Layout und Führung  
  - Anwendung der Anfangsspannung (20–50 N) und Definition von Kontakt/Reibung mit dem Dummy  
  - Automatisierte Geometrieerstellung und Vernetzung über Belt-Module, VE oder Python-Skripte

## Verwendete Tools
- VE, ProDSiG, Belt-Module, ANSA

<img src="https://github.com/Dummy-Seater/Dummy-Seater-Automation/blob/main/Docu/Images/Knee-impact-setup.png" alt="Knee-impact-setup" width="50%" />

---

## 🧍 Schritt 1: Dummy-Positionierung auf dem Sitz

**Ziel:**  
Positionierung des virtuellen Dummys auf dem Sitz mit anatomisch korrekter Haltung und regelkonformer Ausrichtung.

**Teilschritte:**
- **Sitzreferenzgeometrie extrahieren:** Bestimmung wichtiger Merkmale wie H-Punkt, Sitzflächenkontur und Rückenlehnenorientierung.
- **Dummy-Modell auswählen (z. B. ATD H395):** Laden eines LS-DYNA-kompatiblen virtuellen FEM-Dummys für Insassen-Simulationen.
- **Positionsdatei zur Einrichtung verwenden:** Einsatz einer strukturierten Textdatei zur Definition von Gelenkzielen, Bauteilgruppen und Haltungsvorgaben.
- **Becken und Oberkörper ausrichten:** Platzierung des Beckens am H-Punkt und Ausrichtung von Oberkörper und Gliedmaßen gemäß Sitzgeometrie und Haltungsvorgaben.
- **Anthropometrische Regeln anwenden:** Durchsetzung von Gelenkwinkeln und Gliedmaßenpositionen gemäß Euro NCAP oder internen Protokollen.
- **Haltung und Metriken validieren:** Überprüfung von Kopfhöhe, Kniewinkel und anatomischer Ausrichtung. Dokumentation relevanter Kennwerte zur Nachvollziehbarkeit.
- **Automatisierung über VE oder ANSA:** Anwendung der Positionsdatei zur Durchsetzung von Haltungsvorgaben und zur Vereinfachung des Positionierungsprozesses.

---

# 🪑 Schritt 2: Sitzvorspannung

## Ziel
- Simulation realistischer Sitzverformung und Dummy-Setzung mit Regal-Dummy  
- Sicherstellung korrekter Kontaktkräfte und Randbedingungen für nachgelagerte Crashanalysen

## Teilschritte
- **Import & Validierung der Sitzgeometrie:** Laden des Sitzmodells und Überprüfung der Netzqualität, Materialdefinition und Konnektivität  
- **Anwendung der Dummy-Position aus Schritt 1:** Übertragung der Gelenkpositionen und Erzwingung der Haltung über Gelenkzwänge oder vorgegebene Bewegung  
- **Aktivierung von Schwerkraft & Masse:** Einführung des Dummy-Gewichts und der Schwerkraft zur Simulation natürlicher Setzung  
- **Kontakt- & Zwangsdefinition:**  
  - Definition von Flächenkontakt mit Reibung  
  - Fixierung der Sitzbefestigungen und Anwendung von Gelenkzwängen  
- **Durchführung der Vorspannungssimulation:** Quasistatische Analyse zur Erfassung von Sitzkompression und Dummy-Setzung  
- **Export des vorgespannten Zustands:** Speicherung der verformten Sitz- und Dummy-Konfiguration zur Verwendung im Crash-Setup

---

# 🔗 Schritt 3: Gurtführung und Vorspannung

## Ziel
- Modellierung realistischer Sicherheitsgurtgeometrie und Anwendung der Anfangsspannung für korrekte Rückhaltewirkung  
- Sicherstellung der Führung gemäß Dummy-Haltung und regulatorischen Standards

## Teilschritte
- **Import der finalen Geometrie:** Laden des vorgespannten Sitzes und des final positionierten Dummys  
- **Definition des Gurtsystems (Parametrisch):**  
  - Modellierung von Aufroller, Schloss, Befestigungspunkten und Gurtband  
  - Verwendung parameterbasierter Eingaben  
  - Spezifikation der 2D-Gurtlänge und 1D-Balkenverbindungen  
  - Automatisierte Geometrieerstellung und Vernetzung  
- **Gurtführung über Dummy:** Ausrichtung des Gurts über Schulter, Brust und Becken  
- **Anwendung der Anfangsspannung:** Simulation realistischer Aufroller-Einzugskraft (20–50 N Vorspannung)  
- **Kontakt- & Zwangsdefinition:** Definition von Kontakt mit Reibung und Fixierung der Gurtenden  
- **Validierung & Export:**  
  - Überprüfung der Führung, Spannkraft und Kontaktdruck  
  - Export der finalen Formen für Crashsimulation

---

# Crash-Lastfall — Knie-Mapping & Aufprallbewertung (Analyse)

## Analyseübersicht
- Nichtlineare transient-dynamische Simulation von Knieaufprall bei Fahrer und Beifahrer  
- Lastfälle basierend auf Euro NCAP-Protokollen  
- Volle Interaktion mit Rückhaltesystemen enthalten

## Wichtige Bewertungskennzahlen
- **Femurkraft:** ≤ 3,8 kN  
- **Knieverschiebung & -gleiten:** ≤ 6 mm  
- **Gurtkräfte & Rückhalteverhalten:** Bewertung der Gurtkräfte und Dummy-Kinematik  
- **Energieaufnahme & Plastifizierung:** Bestätigung, dass plastische Verformungen innerhalb der Grenzwerte liegen

## Nachbearbeitung & Berichterstattung
- Extraktion von Sensordaten  
- Erstellung automatisierter Berichte  
- Hervorhebung von Grenzwertüberschreitungen

## Ergebnis & Nächste Schritte
- **Bestanden:** Armaturendesign genehmigt  
- **Nicht bestanden:** Änderung von Design, Materialien oder Rückhaltesystem; erneute Analyse durchführen

<img src="https://github.com/Dummy-Seater/Dummy-Seater-Automation/blob/main/Docu/Images/KM-load-bg.svg" alt="Knee-impact-setup" width="100%" />

---

