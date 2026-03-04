#### **Objectiu**

Classificar i diferenciar les estratègies d'intervenció tècnica (preventiva, correctiva, predictiva i evolutiva) segons l'estat del sistema i l'objectiu de l'operació, identificant els escenaris d'aplicació idonis per a cadascuna.

#### **Introducció**

En l'àmbit industrial i professional, el manteniment es defineix com el conjunt d'activitats tècniques i administratives orientades a conservar un actiu físic o a restaurar-lo a un estat en què pugui dur a terme la funció requerida. Per a un tècnic informàtic, entendre aquest concepte és vital: els ordinadors no són dispositius estàtics; són sistemes dinàmics sotmesos a estrès tèrmic, desgast mecànic i obsolescència de programari.

La gestió eficient d'un parc informàtic no es basa en la improvisació, sinó en l'elecció de l'estratègia adequada per a cada situació. Hem d'esperar que l'equip es trenqui per actuar? És rendible aturar la producció per revisar màquines que funcionen bé? En aquest apartat analitzarem les quatre grans tipologies d'intervenció, aprenent a distingir quan cal ser proactiu (evitar l'error) i quan cal ser reactiu (corregir l'error), sempre amb l'objectiu final de maximitzar la disponibilitat del sistema i minimitzar els costos d'aturada.

#### **Manteniment Preventiu**

Aquesta tipologia agrupa el conjunt d'accions programades i cícliques que s'executen sobre un sistema en estat operatiu, amb l'objectiu fonamental de mitigar el desgast físic dels components i reduir la probabilitat d'aturades no planificades. La característica definitòria del manteniment preventiu és la seva periodicitat; les intervencions es regeixen pel calendari o per les hores d'ús acumulades, independentment de si l'equip presenta símptomes de fallada o no. L'objectiu és maximitzar el temps mitjà entre fallades (MTBF) actuant abans que l'avaria es manifesti.

Les operacions preventives aborden tant l'àmbit físic com el lògic. A nivell de maquinari, les tasques es centren a combatre els enemics naturals de l'electrònica: la temperatura i la brutícia. Això inclou la neteja interna de circuits de ventilació per evitar l'acumulació de pols que actua com a aïllant tèrmic, la verificació de la rotació dels ventiladors i la substitució periòdica de consumibles degradables com la pasta tèrmica. A nivell de programari, la prevenció implica mantenir el sistema immune a vulnerabilitats mitjançant l'actualització de microprogramari (BIOS/UEFI) i pedaços de seguretat, així com la higienització del sistema de fitxers per evitar la pèrdua de rendiment.

Protocol d'Actuació Estàndard (Checklist): Per executar un manteniment preventiu eficaç, el tècnic ha de seguir una rutina sistemàtica que cobreixi tant el maquinari com el programari:

1. Inspecció Física i Neteja: L'operació comença amb la desconnexió elèctrica i l'obertura del xassís. S'ha de procedir al desallotjament de pols mitjançant aire comprimit, centrant-se en els filtres antipols, les aletes dels dissipadors i la font d'alimentació. És crític verificar visualment l'estat dels condensadors de la placa base (buscant inflors o fugues d'electròlit) i assegurar que tots els cables estan fermament connectats i no interfereixen amb el flux d'aire.  
2. Verificació Tèrmica: Un cop net, s'encén l'equip i es comprova que tots els ventiladors giren sense sorolls mecànics (indicatius de rodaments desgastats). Si l'equip té més de tres anys, el protocol dicta la substitució obligatòria de la pasta tèrmica del processador.  
3. Higiene Lògica: A nivell de sistema operatiu, s'executen eines per alliberar espai en disc (eliminació de fitxers temporals i de la memòria cau), es verifiquen les actualitzacions de seguretat pendents i es comprova la integritat de les còpies de seguretat automatitzades.

🎯 **Aclariment pràctic**: En l'enginyeria de fiabilitat, la vida útil dels components segueix una gràfica en "U". Els equips fallen molt al principi (defectes de fàbrica) i molt al final (desgast). El manteniment preventiu té la funció d'allargar la fase central d'estabilitat i retardar l'ascens de la corba de desgast final.

![][image1]

*Gráfica de la “Bathub Curve” (corba de la banyera)*

#### **Manteniment Correctiu**

El manteniment correctiu és la resposta tècnica directa a una avaria o disfunció que ja s'ha materialitzat. En aquest escenari, el sistema ha perdut la seva capacitat operativa, total o parcialment, i l'objectiu de la intervenció és la restauració del servei (Restore to Operation) en el menor temps possible. A diferència del preventiu, que és proactiu, el correctiu és intrínsecament reactiu i no es pot planificar en el temps, només gestionar.

Dins d'aquesta categoria, distingim entre el correctiu immediat i el diferit. L'immediat s'aplica quan l'avaria és crítica i paralitza l'activitat de l'usuari o de l'organització (per exemple, una font d'alimentació cremada en un servidor), exigint una actuació d'urgència. El diferit, en canvi, permet programar la reparació per a un moment de menor impacte productiu, ja sigui perquè l'avaria no atura totalment el sistema (com un ventilador sorollós o un port USB frontal danyat) o perquè és necessari esperar l'arribada d'un recanvi específic.

Flux de Treball Correctiu: L'actuació no es limita a canviar la peça trencada, sinó que segueix un procés analític:

1. Diagnosi i Aïllament: Identificar inequívocament el component causant de la fallada mitjançant proves creuades o eines de diagnòstic, descartant errors de configuració.  
2. Valoració de Viabilitat: Abans de procedir, cal respondre a la pregunta: val la pena reparar-ho? Si el cost de la reparació (peça \+ mà d'obra) supera el 50-60% del valor d'un equip nou equivalent, o si l'equip té una antiguitat superior a 5-6 anys, el procediment recomanat és la substitució completa de la màquina.  
3. Substitució i Validació: Després de canviar el component, és imperatiu realitzar proves d'estrès per confirmar que l'avaria s'ha resolt i que el nou component no provoca incompatibilitats.

🧰 **Consell pràctic**: Un usuari domèstic sol operar sota un model purament correctiu ("Ho arreglo quan es trenca"). Un tècnic professional, però, ha de fomentar contractes de manteniment preventiu als seus clients. La lògica és econòmica: una aturada correctiva d'urgència sempre és més cara (pel cost de la peça i, sobretot, pel temps de productivitat perdut) que una parada programada per fer una neteja preventiva.

#### 

#### **Manteniment Predictiu**

Representa l'evolució tecnològica del manteniment. Aquesta estratègia es basa en el monitoratge continu i l'anàlisi de dades en temps real per detectar anomalies incipients abans que aquestes provoquin una fallada funcional. Mentre que el preventiu es basa en estadístiques generals (canviar l'oli cada 10.000 km), el predictiu es basa en l'estat real del component (analitzar l'oli per veure si realment està degradat).

Per aplicar-lo, el tècnic utilitza eines de programari que llegeixen els sensors interns del maquinari. 

💡 **Exemple**: La tecnologia S.M.A.R.T. en unitats d'emmagatzematge, que alerta sobre la reassignació de sectors defectuosos setmanes abans que el disc deixi de funcionar. De la mateixa manera, el monitoratge de sensors tèrmics permet detectar tendències alcistes en la temperatura de la CPU que indiquen una degradació del sistema de refrigeració molt abans que s'assoleixin nivells crítics.

Paràmetres Clau de Monitoratge: El tècnic ha de saber interpretar les dades proporcionades pels sensors del sistema:

* Emmagatzematge (S.M.A.R.T.): Els discs durs i SSD registren errors de lectura, sectors reassignats i hores d'ús. Un augment sobtat en la taxa d'errors de lectura (Raw Read Error Rate) és un indicador fiable que el disc fallarà en les properes setmanes.  
* Refrigeració i Revolucions: Si els registres indiquen que el ventilador de la CPU necessita girar a 4000 RPM per mantenir la temperatura que abans mantenia a 2000 RPM, el sistema està avisant d'una degradació de la pasta tèrmica o d'una obstrucció severa, encara que l'ordinador no s'hagi apagat mai.

![][image2]

*Imatge d’un test S.M.A.R.T. a la BIOS*

**Manteniment Evolutiu (o Adaptatiu)**

Aquesta tipologia es diferencia de les anteriors perquè no respon a cap avaria, desgast o error, sinó al fenomen de l'obsolescència tecnològica. Aquí, el sistema funciona correctament segons les seves especificacions originals, però aquestes han esdevingut insuficients per satisfer els requisits del nou programari o les necessitats creixents de l'usuari.

Les intervencions evolutives tenen com a objectiu millorar les prestacions originals de l'equip. Els casos més habituals inclouen l'ampliació de la capacitat de memòria RAM per millorar la multitasca, la substitució de discs mecànics (HDD) per unitats d'estat sòlid (SSD) per reduir la latència del sistema, o la instal·lació de maquinari dedicat, com targetes gràfiques, per a usos específics.

Detecció de Colls d'Ampolla (Bottlenecks): Per executar un manteniment evolutiu racional, cal identificar quin component està limitant el rendiment global.

* Símptoma de Memòria: Si l'usuari experimenta lentitud en canviar entre finestres obertes i el disc dur té una activitat constant (fent swapping), l'actuació prescrita és l'ampliació de la memòria RAM.  
* Símptoma d'Emmagatzematge: Si el sistema triga minuts a arrencar o a obrir aplicacions pesades, però un cop obertes funcionen bé, el coll d'ampolla és la velocitat de transferència. L'actuació correcta és la migració de HDD mecànic a SSD.

🧰 **Consell pràctic**: El tècnic té la responsabilitat ètica d'assessorar sobre la viabilitat d'un manteniment evolutiu. En equips molt antics, el cost dels components d'actualització més la mà d'obra pot superar el valor residual de la màquina o no garantir un rendiment satisfactori a causa de colls d'ampolla en el processador. En aquests casos, l'actuació correcta és desaconsellar la inversió i recomanar la substitució completa de l'actiu.

[image1]: ../../../Unitats/Unitat_3_HTML/Llico_1/img/image1.png

[image2]: ../../../Unitats/Unitat_3_HTML/Llico_1/img/image2.png