# Bronnen D3D Universal (status: grotendeels NIET geverifieerd)

Geraadpleegd op 2026-11-04. Pagina's van de OSE-wiki konden **niet** worden geopend (proxy: 403 CONNECT / ENOTFOUND voor wiki.opensourceecology.org, www.opensourceecology.org en alle geteste webwinkels). Alleen WebSearch en GitHub-zoeken werkten.

## Wat is gevonden (via zoekresultaten, pagina's zelf niet gelezen)
| Bron | URL | Licentie | Opmerking |
|---|---|---|---|
| OSE-wiki D3D Universal | https://wiki.opensourceecology.org/wiki/D3D_Universal | niet geverifieerd | Volgens zoekresultaat: BOM, vBOM, bouwinstructies, fabricagetekeningen |
| OSE-wiki D3D | https://opensourceecology.org/wiki/D3D | niet geverifieerd | |
| Bouwgids D3D Universal v20.07 (Google Slides, aug 2020) | zie zoekresultaat docs.google.com/presentation/d/1VtukaPaT_3JcaUyZhQt-Q7Cz-bWjdQlizudmg00LbUs | niet geverifieerd | Genoemd als bouwinstructie; zoekresultaat noemt $483 totaalkosten (niet gecontroleerd) |
| GitHub OpenSourceEcology/D3D_v19.04 | https://github.com/OpenSourceEcology/D3D_v19.04 | geen licentie in GitHub-metadata | laatste push 2019-08-07 |
| GitHub OpenSourceEcology/D3D-Universal-Mill | https://github.com/OpenSourceEcology/D3D-Universal-Mill | geen licentie vermeld | CNC-variant, push 2019-10-15 |
| GitHub OpenSourceEcology/3D-Printer-OSE-Marlin | https://github.com/OpenSourceEcology/3D-Printer-OSE-Marlin | geen licentie vermeld | firmware, push 2018-08-02 |
| GitHub OpenSourceEcology/3D-Printer-Part-Library | https://github.com/OpenSourceEcology/3D-Printer-Part-Library | geen licentie vermeld | push 2019-06-24 |
| GitHub AlexandriaLittle/d3d-pro | https://github.com/AlexandriaLittle/d3d-pro | CC-BY-SA-4.0 | niet-OSE-account, push 2026-01-20; relatie tot OSE niet geverifieerd |
| GitHub AlexandriaLittle/D3D-Mega-v23.05 | https://github.com/AlexandriaLittle/D3D-Mega-v23.05 | geen licentie vermeld | push 2023-12-06 |

## Nog niet te beantwoorden
Welke versie het recentst/best gedocumenteerd is, welke varianten (bouwvolume) bestaan, en welke basis te kiezen: **niet geverifieerd**. Eerste kandidaat om te onderzoeken: D3D Universal v20.07 (wiki + bouwgids).
Ik heb de OSE-GitHub-repo's niet gekloond: de sessie heeft alleen toegang tot nealharpal0/Yes-.

## Update 2026-11-04 (na toestemming gebruiker)
GitHub-repo's waren via de git-proxy wel te klonen en zijn gelezen:
- 3D-Printer-OSE-Marlin: README noemt twee firmwareversies (D3D v18.07: 0,4 mm nozzle + Prusa i3 MK2 extruder; Marlin: 0,6 mm nozzle + E3D Titan Aero). Configuration.h: RAMPS 1.4 (EFB), X/Y/Z max 175 mm, thermistor type 1, steps/mm E 161,3 (v18.07) resp. 408 (Titan). README verwijst naar https://wiki.opensourceecology.org/wiki/D3D. Licentie: Marlin GPL-3.0+ (bestandskoppen). Gekopieerd naar bestanden/firmware/.
- D3D_v19.04: alleen 2 STL (5/6 carriages) + FreeCAD-heatbedmodellen, README leeg; geen licentie. Niet gekopieerd.
- Volledig STL-pakket, BOM en bouwstappen staan dus **niet** in de GitHub-repo's; die zitten op de wiki (geblokkeerd).
- Indicatie bouwvolume uit firmware: 175 x 175 x 175 mm (bouwvolume van de bestaande firmware, niet van de wiki-versie geverifieerd).
