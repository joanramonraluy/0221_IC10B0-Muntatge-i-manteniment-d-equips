#### **Objectiu**

Conèixer què és un SAI, els seus components i tipus, i la seva aplicació en equips informàtics

#### **Introducció**

En entorns informàtics, la qualitat del subministrament elèctric és tan important com la potència dels equips. Un tall de corrent sobtat o una forta fluctuació de tensió pot provocar pèrdua de dades, danys a discs i alimentacions, o deixar fora de servei sistemes crítics durant minuts o hores. Per reduir aquest risc s’utilitzen els sistemes d’alimentació ininterrompuda, coneguts com a SAI o UPS (les seves sigles en anglès), que actuen com una combinació de bateria, regulador i interruptor automàtic per mantenir els equips en funcionament prou temps per treballar amb seguretat o apagar‑los de manera ordenada.

#### **Definició i funció del SAI**

Un SAI és un dispositiu que es connecta entre la xarxa elèctrica i els equips informàtics i que proporciona energia de reserva mitjançant bateries quan es produeix un tall o una caiguda important de tensió. A diferència d’una simple regleta, un SAI és capaç de detectar anomalies en el subministrament i commutar gairebé de manera instantània a la seva bateria interna, de manera que l’ordinador, els servidors o els dispositius de xarxa continuen rebent energia sense interrupcions apreciables.

​FOTO: per

La funció principal d’un SAI és protegir els equips contra tres tipus de problemes habituals: 

* Talls complets de corrent.  
* Microtalls molt breus que poden bloquejar o reiniciar equips sensibles.  
* Variacions de tensió (pujades o baixades) que poden malmetre fonts d’alimentació i components electrònics. 

💡 **Exemple**: En un despatx o en un laboratori, un SAI permet guardar la feina, tancar aplicacions i apagar els equips de forma controlada quan la xarxa falla, evitant pèrdues de dades i reduint l’estrès mecànic i tèrmic sobre discs i fonts.

#### **Components principals d’un SAI**

Tot i que externament un SAI pot semblar una “caixa negra” amb endolls, a l’interior hi trobem diversos blocs funcionals ben diferenciats. El primer element clau són les bateries, normalment de tipus plom‑àcid o similars, que emmagatzemen energia en forma de corrent continu; aquestes bateries són les encarregades d’alimentar els equips quan la xarxa cau i tenen una autonomia limitada que depèn de la seva capacitat i del consum connectat.

​FOTO: bateria d’un SAI

​Per convertir l’energia de les bateries en un senyal apte per als equips, el SAI incorpora un inversor, que transforma el corrent continu de les bateries en corrent altern a la tensió de xarxa (per exemple, 230 V AC). A l’entrada, un rectificador i circuits de càrrega s’encarreguen de transformar el corrent altern de la xarxa en corrent continu per recarregar les bateries i alimentar internament el sistema quan tot funciona amb normalitat. A més, molts SAI incorporen reguladors de tensió que intenten mantenir un valor elèctric estable encara que la tensió de la xarxa variï dins de certs marges, reduint així l’estrès sobre les fonts dels equips connectats.

​Els SAI moderns també disposen d’indicadors i sistemes de monitoratge: LEDs o pantalles que informen de l’estat de la bateria, el nivell de càrrega, la presència de fallades i el mode de funcionament. Alguns models permeten connectar‑se a l’ordinador mitjançant USB o xarxa i, amb un programari específic, poden ordenar l’apagada automàtica dels equips quan la bateria arriba a un determinat nivell, cosa especialment útil en servidors o instal·lacions sense supervisió constant.

​FOTO: pantalla led d’un SAI

#### **Tipus de SAI**

Tot i que tots els SAI comparteixen la mateixa idea bàsica —mantenir els equips en funcionament quan la xarxa falla i protegir‑los de problemes elèctrics—, no tots ho fan de la mateixa manera. Segons com tracten la tensió d’entrada i com utilitzen la bateria, es distingeixen principalment tres famílies: SAI offline (o standby), SAI line‑interactive i SAI online (o de doble conversió).

En els SAI offline, els equips reben normalment la tensió directament de la xarxa i el SAI només entra en joc quan detecta un tall o una caiguda important, commutant a bateria en un temps molt curt però no nul. Els SAI line‑interactive hi afegeixen un regulador de tensió que corregeix pujades i baixades moderades sense gastar bateria, mentre que en els SAI online la potència es converteix contínuament de CA a CC i de CC a CA, de manera que la sortida està sempre desacoblada i estabilitzada respecte de la xarxa.

##### **SAI offline**

En un SAI offline o standby, el camí principal de l’energia és molt simple: mentre la tensió de xarxa es manté dins d’uns marges considerats acceptables, els equips connectats reben aquesta tensió gairebé de forma directa, amb un mínim filtratge. El SAI està “a l’espera” monitoritzant la línia, i només quan detecta un tall o una caiguda per sota d’un llindar preestablert, activa l’inversor i comença a alimentar els equips des de les bateries internes.

​Aquesta commutació triga uns mil·lisegons, temps que la majoria de fonts d’alimentació de PC i equips electrònics poden aguantar gràcies als seus propis condensadors d’entrada, de manera que l’usuari sovint no percep cap apagada. El principal avantatge d’aquest tipus de SAI és el cost reduït i la simplicitat, que el fan adequat per a estacions de treball individuals, petits despatxos o equips que no són especialment crítics, però que es volen protegir de talls sobtats i microtalls. Com a inconvenient, la tensió que arriba als equips depèn bastant de la qualitat de la xarxa: les variacions moderades de tensió, sorolls i petits pics no sempre queden corregits.

🧰 **Consell pràctic**: Per tant, l'opció recomanada per a servidors crítics, petites sales de CPD, equipament de xarxa essencial o sistemes que no es poden permetre cap interrupció ni degradació significativa del subministrament, tot i que el seu cost i consum en repòs són superiors als dels SAI offline o line‑interactive.

##### **SAI line‑interactive: punt intermedi**

Els SAI line‑interactive se situen a mig camí entre els models offline més senzills i els online de doble conversió pel que fa a protecció i cost. En condicions normals continuen subministrant energia directament des de la xarxa, però incorporen un regulador automàtic de tensió (AVR) que compensa pujades i baixades moderades sense haver de recórrer immediatament a la bateria.

​Això significa que, davant variacions de tensió relativament freqüents, però no extremes, el SAI pot mantenir una sortida més estable als equips sense desgastar tant les bateries, allargant la seva vida útil. Només quan la tensió surt dels marges que l’AVR pot corregir, o quan es produeix un tall complet, el line‑interactive commuta a mode bateria de manera similar a un SAI offline.

🧰 **Consell pràctic**: Per aquest motiu, aquest tipus de SAI és molt habitual en petites sales de servidors, laboratoris i instal·lacions on es vol una protecció superior a la d’un offline, però on no és viable el cost d’un sistema online pur.

##### 

##### **SAI online**

En un SAI online o de doble conversió, el funcionament és molt diferent, perquè la potència no passa “directament” de la xarxa als equips en cap moment. Primer, un rectificador converteix la tensió de xarxa en corrent continu i alimenta un bus intern, al qual es connecten tant les bateries com l’inversor; després, l’inversor genera de nou una tensió de sortida en corrent altern, normalment 230 V, amb una forma d’ona i un valor molt estables. Això vol dir que, fins i tot quan la xarxa puja, baixa o presenta sorolls, la sortida que veu l’ordinador o el servidor continua sent pràcticament idèntica, ja que està completament desacoblada dels problemes de l’entrada.

​Quan es produeix un tall de corrent, la transició a bateria és instantània des del punt de vista de la sortida, perquè les bateries ja estan connectades al bus de corrent continu i l’inversor continua funcionant sense haver de commutar cap relé. Els SAI online proporcionen així el nivell de protecció més alt: ofereixen alimentació molt estable, filtren la major part dels sorolls i transitoris i eliminen pràcticament qualsevol microtall visible pels equips.

🧰 **Consell pràctic**: Per aquest motiu, són l'opció recomanada per a servidors crítics, petites sales de CPD, equipament de xarxa essencial o sistemes que no es poden permetre cap interrupció ni degradació significativa del subministrament, tot i que el seu cost i consum en repòs són superiors als dels SAI offline o line‑interactive.

| Protecció / funció | Què vigila | Què fa el SAI quan actua | Exemple d’ús pràctic |
| ----- | ----- | ----- | ----- |
| Sobretensió (surge / spike) | Pics molt breus de tensió a la xarxa | Deriva o limita el pic perquè no arribi als equips | Descàrregues llunyanes, maniobres a la xarxa elèctrica |
| Subtensió / caiguda de tensió | Baixades de tensió prolongades | Compensa (line‑interactive/online) o passa a bateria | Xarxa “fluixa” que baixa a 180–190 V durant uns segons |
| Tall complet de subministrament | Absència total de tensió d’entrada | Commuta a bateria i manté els equips en marxa | Apagada general o automàtic del quadre que salta |
| Sobrecàrrega de sortida | Massa potència connectada al SAI | Avisa (alarma) i pot tallar o limitar la sortida | Múltiples PCs i perifèrics endollats en un SAI petit |
| Curtcircuit a la sortida | Connexió directa fase–neutre/equip | Desconnecta immediatament la sortida del SAI | PC o dispositiu amb avaria greu al seu interior |
| Protecció tèrmica | Temperatura interna excessiva | Activa ventilador, redueix càrrega o desconnecta sortida | SAI en armari tancat, treballant molt proper al 100 % |
| Supervisió d’estat de bateria | Tensió/capacitat de les bateries | Avisa de “bateria feble” o “bateria a substituir” | SAI antic que ja no dóna el temps d’autonomia esperat |
| Filtratge de soroll / EMI | Sorolls d’alta freqüència i paràsits | Atenua les interferències abans que arribin als equips | Entorns amb maquinària, motors o fonts de baixa qualitat |

Taula descriptiva clara amb els principals tipus de proteccions d’un SAI

#### **Mesures de protecció en els SAI**

Igual que les fonts d’alimentació dels ordinadors, els SAI incorporen diversos sistemes de protecció destinats a evitar danys tant als equips connectats com al mateix dispositiu. Aquests circuits supervisen la tensió de la xarxa, el corrent que circula pels endolls de sortida, la temperatura interna i l’estat de les bateries, i actuen automàticament quan es detecta una situació anòmala.

​Una de les funcions més visibles és la protecció contra sobretensions, especialment en forma de pics breus que poden aparèixer a la xarxa a causa de maniobres, incidències o tempestes llunyanes. El SAI absorbeix o limita aquests impulsos per evitar que arribin directament a les fonts dels ordinadors, reduint el risc de danys sobtats en plaques i components electrònics. A més, els SAI disposen de protecció contra sobrecàrrega i curtcircuits a les preses de sortida: si s’hi connecten massa equips o un dispositiu defectuós, el sistema detecta que el corrent supera el límit admès i talla o redueix la sortida, sovint acompanyat d’un avís sonor o visual.

​També és habitual que els SAI monitoritzin la temperatura interna i l’estat de les bateries. Si la temperatura puja massa, per exemple per una ventilació deficient o per treballar constantment al límit de potència, el SAI pot activar el ventilador, reduir la càrrega o fins i tot desconnectar la sortida per evitar danys. Quan les bateries es degraden amb el temps, molts models alerten mitjançant un LED o missatges al programari de monitoratge, indicant que l’autonomia ja no és la prevista i que cal planificar el seu reemplaçament; ignorar aquests avisos pot fer que, en un tall real, el SAI només mantingui els equips encesos durant uns segons.

💡 **Exemple**: Un SAI que pita i es desconnecta quan s’hi endollen massa equips a la mateixa regleta, un dispositiu que “fa saltar” la protecció del SAI en connectar‑lo, o un avís de bateria avariada que obliga a revisar el sistema abans de confiar‑hi dades crítiques.