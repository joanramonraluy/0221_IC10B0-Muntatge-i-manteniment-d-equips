#### **Objectiu**

Comprendre el funcionament bàsic de les fonts d’alimentació d’un ordinador i saber llegir i interpretar les principals dades tècniques de l’etiqueta (tensions, corrents i potència).

#### **Introducció**

En aquest apartat aprofundirem en allò que realment determina si una font d’alimentació és adequada per a un equip o no: les tensions que proporciona, el corrent màxim que pot lliurar a cada línia i la potència total que és capaç de suportar de manera segura. Ja hem vist què és una font commutada i quines parts té; ara es tracta d’aprendre a “traduir” els números de l’etiqueta a situacions reals, com ara si una font pot alimentar una CPU i una GPU determinades o què passa quan es connecten massa dispositius a una mateixa línia. També veurem les proteccions internes que incorporen les fonts modernes i com aquestes intervenen en casos de sobrecàrrega, curtcircuit o sobreescalfament, i introduirem el concepte d’eficiència i les certificacions 80 PLUS com a indicador orientatiu de consum i escalfor.

#### **Tensions i rails de sortida**

La funció principal d’una font d’alimentació de PC és convertir el corrent altern de la xarxa (230 V AC) en diverses tensions de corrent continu que els components de l’ordinador poden utilitzar de forma segura. Les fonts ATX modernes proporcionen simultàniament diverses línies (rails) de sortida, cadascuna amb una tensió fixada i un corrent màxim permès.

​Els rails principals que trobem a l’etiqueta d’una font ATX són:

* ​+12 V: és la línia principal, utilitzada per alimentar la CPU (connector EPS), la GPU (connectors PCIe), ventiladors i motors de discs.  
* ​+5 V: s’utilitza per a alguns circuits de la placa base, ports USB i perifèrics interns.  
* ​+3,3 V: alimenta memòries RAM i circuits lògics de la placa base.  
* ​5VSB (5 V stand‑by): és una línia de baixa potència que roman activa encara que el PC estigui apagat però endollat, i permet funcions com l’encesa des del botó frontal o des de la xarxa (Wake‑on‑LAN).  
* ​-12 V: línia residual que alguns circuits antics o especials encara poden utilitzar, tot i que el seu ús és molt reduït.

​A l’etiqueta de la font, aquests rails solen aparèixer en forma de taula, on a cada fila hi ha la tensió del rail (+12 V, \+5 V, \+3,3 V, 5VSB, \-12 V) i, al costat, el corrent màxim que pot lliurar en amperes (A). Sovint també hi figura la potència màxima combinada de certs rails, especialment la del 12 V, ja que és la que concentra la major part del consum dels equips moderns. Llegir correctament aquesta taula és essencial per saber fins on es pot “forçar” la font sense entrar en sobrecàrrega.

FOTO: l’etiqueta de la font, aquests rails solen aparèixer en forma de taula

#### **Capacitat de corrent i potència per rail**

Cada rail de la font té un límit de corrent màxim, expressat en amperes (A), que indica quanta intensitat pot lliurar de forma segura sense sobreescalfar-se ni sortir dels paràmetres per als quals ha estat dissenyada. Aquests valors són els que permeten calcular la potència màxima aproximada que pot subministrar cada línia, utilitzant la relació de potència que ja s’ha treballat en la Llei d’Ohm i en les magnituds fonamentals.

​La potència elèctrica es pot entendre, en aquest context, com la quantitat d’energia per unitat de temps que la font entrega a cada rail. Quan parlem d’un rail concret, podem aproximar la seva potència màxima amb la relació: potència ≈ tensió del rail multiplicada pel corrent màxim indicat a l’etiqueta 

💡 **Exemple**: Un rail de 12 V amb 30 A pot arribar a prop de 360 W destinats als components que utilitzen aquesta línia). Tot i que en fonts reals hi ha limitacions de potència combinada i altres detalls, aquest càlcul senzill ajuda a fer-se una idea ràpida de si una font té marge suficient per a una determinada configuració.

​A la pràctica, aquests números no són només dades, sinó límits operatius que condicionen el muntatge i l’actualització de l’equip. 

💡 **Exemple**: Si es coneix que una CPU pot arribar a consumir uns 120 W i una GPU uns 200 W, es pot estimar que tots dos junts exigiran al rail de 12 V al voltant de 320 W; si la font anuncia que el seu carril de 12 V admet fins a 360 W, hi ha marge de seguretat, però si el límit fos molt més baix, es podrien produir apagades sobtades o inestabilitat sota càrrega.

De la mateixa manera, saber quanta potència s’està demanant realment a les línies de 5 V i 3,3 V ajuda a evitar configuracions amb massa discs, perifèrics o dispositius USB en fonts de baixa qualitat o molt justes.

#### **Proteccions internes i límits de seguretat**

Les fonts d’alimentació modernes incorporen diversos sistemes de protecció interna que tenen com a objectiu evitar danys greus tant a la pròpia font com als components connectats en situacions anormals. Aquests circuits de protecció supervisen la tensió, el corrent i la temperatura, i desconnecten la sortida o aturen completament la font quan detecten condicions perilloses.

​Algunes de les proteccions més habituals són:

* ​OCP (Over Current Protection): protecció per sobreconsum; si un rail supera el corrent màxim previst, la font s’apaga per evitar sobreescalfaments o danys.  
* ​OVP (Over Voltage Protection): protecció per sobretensió; si per algun motiu la tensió d’un rail puja massa per sobre del valor nominal, la font es desactiva per no “cremar” la placa base o altres components.  
* ​SCP (Short Circuit Protection): protecció davant d’un curtcircuit; si es produeix un pont directe entre positiu i negatiu, el corrent es dispararia, i la font talla immediatament la sortida.  
* ​OTP (Over Temperature Protection): protecció per sobretemperatura; si la temperatura interna puja per sobre d’un llindar de seguretat (per exemple, per ventilació deficient o acumulació de pols), la font s’atura per refredar-se.

En el dia a dia, aquestes proteccions expliquen molts comportaments aparentment “misteriosos” d’un PC. Un ordinador que s’apaga sobtadament quan s’inicia un joc exigent pot estar forçant el rail de 12 V i activant l’OCP, una regleta sobrecarregada amb molts dispositius pot contribuir a que la font treballi al límit i s’escalfi excessivament, i un cable SATA danyat o mal connectat pot causar un curtcircuit que fa saltar el SCP. Entendre aquestes proteccions ajuda el tècnic a distingir entre un problema greu de maquinari i una simple situació de sobrecàrrega que es pot resoldre redistribuint consums, netejant el sistema o substituint una font insuficient.

#### **Eficiència i etiquetes de consum**

A més de la potència que pot lliurar, una característica clau d’una font és la seva eficiència, és a dir, quin percentatge de l’energia que agafa de la xarxa elèctrica arriba realment als components i quina part es perd en forma de calor. Una font amb baixa eficiència converteix una porció important de l’energia en calor interna, cosa que implica més escalfor al xassís, més treball per al ventilador de la font i un consum elèctric globalment més alt per a fer exactament la mateixa feina.

​Les fonts commutades modernes solen assolir eficiències al voltant del 80–90 % o fins i tot superiors, molt per sobre de les antigues fonts lineals, que podien perdre entre un 30 i un 50 % de l’energia en forma de calor. Això es tradueix en equips més frescos, menys soroll del ventilador (ja que no cal evacuar tanta calor) i una factura elèctrica més baixa a llarg termini, especialment en ordinadors que funcionen moltes hores al dia o en sales amb molts equips.

​Per facilitar la identificació de fonts eficients, existeix el programa de certificació 80 PLUS, que classifica les fonts segons el seu rendiment a diferents nivells de càrrega. En l’àmbit d’aquest curs, n’hi ha prou amb conèixer que una font sense cap certificació sol ser menys eficient, mentre que etiquetes com 80 PLUS Bronze, Silver o Gold indiquen nivells d’eficiència creixents, sent habitual recomanar com a mínim Bronze per a equips d’ús intensiu o amb GPU dedicada. Escollir una font amb bona eficiència i d’una marca fiable és una manera senzilla de reduir problemes d’escalfor, de soroll i de fiabilitat a llarg termini, fins i tot si sobre el paper la potència total és similar a la d’altres fonts més barates.

FOTO: eficiència d’una font 80 plus