# Samenvatting (2026-11-04, nachtrun)

## Wat er ligt
- bronnen.md: kandidaat-bronnen met licentiestatus (alleen uit zoekresultaten, niet geverifieerd).
- onderdelenlijst.csv: alleen kopregel. afvinklijst.html: werkend sjabloon, leest data uit onderdelenlijst.csv via bouw_afvinklijst.py.
- bestanden/firmware/: OSE Marlin-firmware (GPL), 175 mm bouwvolume, twee extrudervarianten. docs/README.md: bronnen en licenties. CAD/STL-repo's zonder licentie niet gekopieerd, alleen gelinkt.

## Niet gedaan (blokkade)
Het netwerkbeleid van deze sessie weigert wiki.opensourceecology.org, opensourceecology.org en alle geteste winkels (o.a. tinytronics.nl, coolblue.nl). Zonder die pagina's kon ik geen BOM, printlijst, bouwvolgorde of prijzen vaststellen; die heb ik niet uit mijn geheugen ingevuld. printlijst.md, onderdelenlijst.md, bouwvolgorde.md zijn dus niet gemaakt. Controle van 10 URL's en totalen: niet van toepassing.

## Aannames
- Geen OSE-repo's gekloond: sessiescope is alleen nealharpal0/Yes-.
- Netwerkbeperking niet omzeild.

## Eerst controleren / oplossen
1. Zet in de omgevingsinstellingen (Network access, https://code.claude.com/docs/en/cloud-environments#network-access) wiki.opensourceecology.org, opensourceecology.org en de gewenste winkels (NL/EU) onder Allowed domains, en geef toegang tot github.com/OpenSourceEcology.
2. Ik kan zelf geen netwerkinstellingen wijzigen; jouw toestemming verandert het proxybeleid niet. Alleen de GitHub-repo's heb ik na je akkoord gelezen.
3. Start de opdracht daarna opnieuw; de structuur ligt klaar.
