#### **Objectiu**

Aplicar mesures amb el multímetre en fonts d’alimentació i altres circuits senzills, interpretant els resultats per decidir si una font és usable o presenta problemes bàsics.

#### **Introducció**

Un cop conegut el funcionament del multímetre i les característiques principals de les fonts d’alimentació, el pas següent és aprendre a relacionar les mesures reals amb l’estat del sistema. No n’hi ha prou amb “llegir números” a la pantalla: cal saber si una tensió és correcta, si un problema és acceptable o si indica un problema seriós, i com documentar aquestes observacions de forma senzilla però ordenada. En aquest apartat es treballarà la mesura de tensions als rails d’una font, la diferència entre mesurar “en buit” i amb consum, i es veuran criteris pràctics per decidir si una font pot continuar en servei o convé substituir‑la.

#### **Mesura de tensions en els rails de sortida**

Per valorar l’estat d’una font d’alimentació d’ordinador, una de les proves bàsiques consisteix a mesurar les tensions principals dels rails de sortida: \+12 V, \+5 V i \+3,3 V. Aquestes mesures s’han de fer sempre utilitzant punts de prova segurs, com ara connectors externs, adaptadors específics o els mateixos connectors que alimenten la placa base i els dispositius, evitant en tot moment obrir la carcassa de la font o tocar la part de 230 V.

​En una primera fase, es pot mesurar la tensió “en buit”, és a dir, amb la font en funcionament però amb molt poca càrrega o sense cap equip exigent connectat. En aquesta situació, les tensions acostumen a apropar‑se molt al valor nominal indicat a l’etiqueta, com ara 12 V, 5 V o 3,3 V, i serveixen per comprovar que la regulació bàsica de la font funciona. Tot seguit, és important repetir la mesura amb el sistema sota consum real, per exemple amb la placa base, discs i altres components connectats i, si és possible, realitzant alguna tasca que incrementi la càrrega.

​FOTO: persona mesurant la font amb un multímetre

La diferència entre la tensió en buit i la tensió amb consum proporciona informació sobre la qualitat de l’alimentació. En una font en bon estat, les variacions han de ser moderades: la tensió pot baixar lleugerament sota càrrega, però ha de mantenir‑se dins d’un marge raonable al voltant del valor nominal. Si en connectar la càrrega la tensió cau de forma exagerada o fluctua molt, això pot indicar que la font està al límit de la seva capacitat, que ha envellit o que hi ha algun problema intern en la regulació.

#### **Interpretació de desviacions i anomalies**

Per poder interpretar correctament les mesures, cal disposar d’uns marges senzills que ajudin a decidir si una tensió es pot considerar “correcta”. En aquesta unitat no cal entrar en normatives detallades, però sí treballar amb la idea que una tensió acceptable ha d’estar pròxima al valor nominal i no presentar desviacions extremes.

💡 **Exemple**: un rail de 12 V que es manté entorn d’uns 12 V amb petites variacions és molt més fiable que un que baixa clarament per sota dels 11 V en càrrega.

Algunes desviacions típiques que es poden produir són: 

* Una font que aparentment dona 12 V correctes en buit, però que, quan es connecta l’ordinador o es força una mica la càrrega, cau fins a valors notablement inferiors.   
* Una línia de 5 V que es manté massa baixa i provoca inestabilitat en ports USB o discs   
* Una línia de 3,3 V que oscil·la i pot afectar a la placa base i la RAM. 

També es poden relacionar les mesures amb símptomes observats: ordinador que no arriba a arrencar, apagat sobtat en iniciar una aplicació exigent, reinicis aleatoris o errors intermitents que desapareixen en substituir la font per una altra.

​Mitjançant aquesta interpretació, s’aprèn a identificar fonts possiblement defectuoses o mal dimensionades a partir de dades objectives i no només d’intuïcions. Una font que mostra una tensió relativament estable i dins del rang alt i baix amb la màxima càrrega prevista es pot considerar usable per a aquell equip, mentre que una que es veu clarament tensionada o que presenta caigudes importants hauria de ser etiquetada com a sospitosa i, en molts casos, reemplaçada.

