Standarder
==========

Committing
----------

En commit skal starte med **#** og **issuenr** den hører til. Videre forklarer man på **engelsk** i **nåtid** hva man har gjort.

Spending
--------

Etter en **commit** eller **en mengde arbeid** (dersom ingenting committes), skal man skrive inn en **/spend** på **issuen** man jobbet på. Dette gjøres av **hver person** hver for seg, slik at om 2 personer jobber sammen i 1 time på en issue må hver av de ta en **/spend** på 1 time for totalt 2 timer med arbeid på issuen. Dette er for å gjøre det lett å se hvem som jobber (så ikke ta /spend for andre). Videre bør man skrive en **kommentar** hva man brukte tid på.

Estimate
--------

En **estimate** skal settes i det en **issue** blir **opprettet**. Her skal man dele opp i **research**, **implementation**, **testing** og **merging**. Man skal skrive inn en samlet **/estimate**, men gi verdi per oppgave i **beskrivelsen**. **Estimaten** skal også ta hensyn til antall personer som jobber på oppgaven. Dersom man tror **4 personer** som jobber **sammen** i **1 time** er nok for å løse **issuen** skal man sette **4 timer** som **estimate**.

Naming
------

Vi bruker **snake_case** på **variabler og filer** (man trenger ikke å finne flerordsnavn på filer eller variabler der det er naturlig, ettordsnavn på variabler eller filnavn blir i små bokstaver uten underscore), **kebab-case** på **css-klasser** (som bootstrap) og **CamelCase** på **klasser** i **javaScript** og **Python**. 

Issue-setup
-----------

Vi skal sette opp **alle issuer** for en **sprint** i **starten** av **sprinten**. Hvis man innser at det hører til **mer i en issue**, skal man **commite** til **den** og **presisere** at det var **mer til issuen**, selv om man går **over estimaten**. **Issues** skal bli skrevet på **engelsk**.

Branching
-----------

Alle brukersentrerte oppgaver skal utføres på en egen **grein/branch**. Alle som skal jobbe med samme **oppgave/issue** hopper på samme branch før det gjøres endringer. I terminalen opprettes en branch slik: **"git checkout -b "branch-name"**. Personen som oppretter branchen må i tillegg pushe en **initial commit* som gjøres slik: **git commit --allow-empty -m "Initial commit"**
