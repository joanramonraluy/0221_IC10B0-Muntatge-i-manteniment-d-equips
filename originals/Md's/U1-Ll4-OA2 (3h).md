#### **Objectiu**

Aprendre a dimensionar un SAI segons les necessitats dels equips i calcular autonomia.

#### **Introducció**

Un SAI només és realment útil si està ben dimensionat: ha de ser capaç d’aguantar la potència dels equips connectats i de proporcionar prou temps d’autonomia perquè es puguin tancar sistemes i guardar dades amb seguretat. Si el SAI és massa just, pot treballar al límit, activar constantment les proteccions o apagar‑se abans d’hora; si és exageradament sobredimensionat, s’estarà assumint un cost i un volum innecessaris. En aquest apartat es treballaran mètodes senzills per sumar consums, afegir un marge de seguretat raonable i interpretar les dades d’autonomia que proporcionen els fabricants, aplicant‑ho a situacions típiques d’un laboratori o despatx informàtic.

#### **Càlcul de la potència necessària**

El primer pas per dimensionar un SAI és determinar la potència total que ha de suportar. Aquesta potència s’expressa habitualment en watts (W) o en voltampers (VA), i correspon a la suma dels consums dels equips que s’hi connectaran: ordinadors, monitors, dispositius de xarxa, servidors, etc. Per aconseguir una estimació raonable es poden utilitzar diverses fonts d’informació: etiquetes de potència dels equips, dades del fabricant, valors aproximats per tipus de dispositiu o fins i tot eines de monitoratge de consum quan se’n disposa.

🎯 **Aclariment pràctic**: ​En la pràctica, no sempre és necessari ni recomanable utilitzar el valor màxim teòric de cada font d’alimentació, ja que moltes fonts estan sobrades respecte al consum real del PC. Una estratègia habitual és considerar consums típics: per exemple, un PC d’ofimàtica pot estar al voltant dels 80–120 W, mentre que una estació amb GPU dedicada pot apropar‑se als 300 W o més depenent del model. Aquests valors s’afegeixen als dels monitors i altres perifèrics (com routers o switches) per obtenir una potència total estimada.

Un cop sumats els consums, cal aplicar un marge de seguretat que tingui en compte pics puntuals, possibles ampliacions futures i envelliment dels components. Un marge típic pot situar‑se al voltant d’un 20–30 % per sobre del consum calculat; així, si la suma aproximada és de 600 W, es podria buscar un SAI de com a mínim uns 800–900 VA/W depenent del factor de potència del model. Aquest marge ajuda a evitar que el SAI treballi constantment al 100 % de càrrega, fet que reduiria la seva vida útil i l’autonomia disponible.

#### **Càlcul i factors d’autonomia**

La segona peça clau en el dimensionament és l’autonomia, és a dir, el temps durant el qual el SAI pot mantenir alimentats els equips quan la xarxa falla. Els fabricants solen indicar taules o gràfics d’autonomia en funció del percentatge de càrrega, per exemple: “10 minuts al 50 % de càrrega, 4 minuts al 100 %”. Cal saber interpretar que, com més gran és la càrrega connectada, més ràpidament es buida la bateria i menys temps es disposa per actuar.

Per establir una autonomia mínima acceptable, cal pensar en l’ús real: en molts despatxos o laboratoris n’hi ha prou amb 5–10 minuts per guardar feina i apagar equips de forma ordenada; en entorns més crítics pot interessar disposar de 15–30 minuts o fins i tot més. Això implica que, a l’hora d’escollir el SAI, no n’hi ha prou amb mirar la potència màxima: cal verificar també quina autonomia ofereix a la càrrega estimada i si aquesta encaixa amb les necessitats del lloc.

​Diversos factors afecten directament la durada real: la càrrega efectiva (percentatge de la potència nominal que s’està utilitzant), l’eficiència interna del SAI i l’estat de les bateries. Amb el temps, les bateries perden capacitat fins i tot si el dispositiu no s’utilitza sovint; per això, un SAI que quan és nou pot donar 10 minuts a una certa càrrega, pot arribar a oferir només uns pocs minuts després de diversos anys sense manteniment. A més, un SAI que treballa sempre molt a prop del seu límit de potència veurà reduïda la seva autonomia i pot escalfar‑se més, accelerant la degradació de les bateries.

#### **Càlcul més precís d’autonomia d’un SAI**

Una manera clara i fàcil d’entendre el dimensionament és separar‑lo en tres passos: primer calcular el consum dels equips, després decidir la potència del SAI i, finalment, veure quants minuts pot aguantar.

**Pas 1: calcular el consum dels equips**

Abans de pensar quin SAI necessitem, cal saber quanta potència demanaran els equips que hi connectarem.  No es tracta de connectar‑hi “tot el que hi hagi”, sinó de decidir quins dispositius són realment importants i han de quedar protegits: ordinadors, servidors, equips de xarxa, etc.

Per fer‑ho, pots seguir aquests passos:

1. Fer una llista dels equips que es volen protegir (per exemple, 3 PC d’ofimàtica, 3 monitors, 1 switch de xarxa i 1 NAS).    
2. Assignar a cada tipus d’equip un consum orientatiu en watts, basat en dades de catàleg o en valors típics:    
   * PC d’ofimàtica: uns 100 W.  
   * Monitor: uns 30 W.   
   * Switch petit: uns 20 W.   
   * NAS o petit servidor: uns 40 W.   
   * Multiplicar pel nombre d’unitats i sumar‑ho tot per obtenir la potència total aproximada.  

Per exemple:

* 3 PC: 3 · 100 W \= 300 W 	   
* 3 monitors: 3 · 30 W \= 90 W  
* 1 switch: 20 W  
* 1 NAS: 40 W

Potència total aproximada:

P\_total \= 300 \+ 90 \+ 20 \+ 40 \= 450 W

Aquesta és la potència que el SAI haurà de ser capaç de subministrar quan tots aquests equips estiguin en funcionament.

**Pas 2: decidir la potència mínima del SAI**

Un cop sabem la potència que consumeixen els equips, hem de decidir quina potència mínima ha de tenir el SAI.  No és recomanable que el SAI treballi sempre al 100 % de la seva capacitat, perquè això redueix la seva vida útil i l’autonomia disponible i el fa més sensible a qualsevol pic de consum.  Per això s’acostuma a afegir un marge de seguretat, per exemple del 20–30 %.

Podem expressar‑ho així:

P\_SAI\_mín ≈ P\_total · 1,3

En l’exemple anterior, amb P\_total \= 450 W:

P\_SAI\_mín ≈ 450 · 1,3 ≈ 585 W

Això vol dir que buscarem un SAI que, com a mínim, pugui subministrar al voltant de 600 W.  Molts SAI indiquen la seva potència en VA (voltampers) i no en watts; per passar de watts a VA, es pot utilitzar una aproximació senzilla assumint un factor de potència de 0,8 en equips informàtics:

VA ≈ w0,8

En el nostre cas:

VA ≈ 5850,8 ≈ 730 VA

Per tant, un SAI d’uns 800–1000 VA seria una opció raonable per a aquesta instal·lació.  Amb aquest pas, els alumnes ja han après a dimensionar la   potència   del SAI abans de mirar el tema del temps d’autonomia.\[1\]

**Pas 3: calcular l’autonomia amb un SAI concret**

El tercer pas és calcular durant quant de temps podrà mantenir els equips encesos un SAI concret.  Per això ja no n’hi ha prou amb la potència; cal tenir en compte l’energia que poden proporcionar les bateries internes del SAI i comparar‑la amb el consum dels equips.

Les bateries es descriuen per:  

* Tensió total V (12 V, 24 V, 48 V…).   
* Capacitat \\(C\\) en amperes hora (Ah).\[1\]

Per obtenir una aproximació de l’energia “usable” que el SAI pot donar als equips, fem servir la relació:

E\_usable ≈ V · C · η (en Wh)

On η és un factor d’eficiència que té en compte les pèrdues internes del SAI (es pot utilitzar un valor típic com 0,75)

Exemple: suposem que triem un SAI amb:

* Banc de bateries: 24 V i 9 Ah.    
* Eficiència global estimada: η \= 0,75.  

Energia teòrica de les bateries:

E ≈ 24 · 9 \= 216 Wh

Energia usable aproximada:

E\_usable ≈ 216 · 0,75 ≈ 162 Wh

Això significa que el SAI pot lliurar aproximadament 162 Wh als equips abans que la bateria es descarregui.

Per calcular l’autonomia aproximada, només cal dividir aquesta energia pel consum total dels equips P\_total:\[

t\_hores ≈ E\_usableP\_total 

En el nostre exemple, amb P\_total \= 450 W:

t\_hores ≈ 162450 ≈ 0,36 hores

Per passar a minuts:

t\_minuts ≈ 0,36 · 60 ≈ 22 minuts

Per tant, amb aquest SAI i aquests equips, l’autonomia teòrica seria d’uns 20–25 minuts, suficients per guardar la feina i apagar els sistemes de forma ordenada.  