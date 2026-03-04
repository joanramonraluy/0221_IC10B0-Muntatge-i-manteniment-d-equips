#### **Objectiu**

Executar els procediments de neteja integral i restauració del sistema de refrigeració, seleccionant els productes químics i l'instrumental adequat per garantir la integritat electrònica i recuperar l'eficiència tèrmica original de l'equip.

#### **Introducció**

Dins de les operacions de manteniment preventiu, la higiene tècnica constitueix la intervenció física més directa sobre el maquinari. Lluny de ser una qüestió purament estètica, la neteja interna és un requisit funcional crític: l'acumulació de pols i partícules en suspensió actua com un aïllant tèrmic que obstrueix els fluxos d'aire, provocant sobreescalfament i, en entorns humits, pot esdevenir conductora i provocar curtcircuits en els circuits impresos.

Tanmateix, la neteja d'equips electrònics comporta riscos específics. L'ús de productes de neteja domèstics, draps inadequats o tècniques agressives pot generar descàrregues electrostàtiques (ESD), corrosió química o danys mecànics en components microscòpics. En aquest OA, definirem els estàndards de la indústria per a la higienització segura, l'ús de dissolvents orgànics com l'alcohol isopropílic i el procediment correcte per a la renovació dels materials d'interfície tèrmica (pasta tèrmica), una operació vital per allargar la vida útil dels processadors.

#### **Química i Instrumental de Neteja Electrònica**

La intervenció física sobre circuits electrònics requereix l'ús d'agents químics i materials específics que garanteixin l'eliminació de contaminants sense comprometre la integritat elèctrica dels components. L'enemic principal a combatre és la pols (que actua com a aïllant tèrmic i pont elèctric si absorbeix humitat) i els residus greixosos.

L'agent de neteja estàndard en la indústria és l'Alcohol Isopropílic (Isopropanol), que ha de tenir una puresa superior al 90% (idealment 99,9%). A diferència de l'alcohol etílic de farmaciola (que conté aigua i additius), l'isopropanol és un dissolvent orgànic no polar, la qual cosa significa que dissol eficaçment olis i pastes tèrmiques, s'evapora gairebé instantàniament sense deixar residus conductors i no provoca oxidació en els contactes metàl·lics. L'ús d'aigua, detergents domèstics o netejavidres està estrictament prohibit a l'interior d'un xassís, ja que els seus residus poden provocar curtcircuits o corrosió a llarg termini.

Pel que fa a l'instrumental mecànic, el tècnic ha de disposar d'un sistema de propulsió d'aire (compressor amb filtre d'humitat o esprai d'aire comprimit) per al desallotjament de partícules. Per a la neteja de contacte, s'utilitzen raspalls de truges sintètiques amb propietats ESD (descàrrega electroestàtica) per evitar generar electricitat estàtica durant la fricció, i draps de microfibra d'alta densitat que no desprenguin fibres que puguin quedar atrapades entre els pins dels xips.

![](img/image5.png)

*Esprai d’aire comprimit*

#### **Protocol de Neteja del Sistema de Ventilació**

L'acumulació de pols en els dissipadors (heatsinks) redueix dràsticament la superfície d'intercanvi tèrmic, forçant els ventiladors a girar més ràpid i reduint la vida útil dels components. El procediment de neteja ha de seguir un ordre lògic, començant pels filtres antipols externs i avançant cap a l'interior.

Aquest ordre lògic respon a dos principis físics bàsics: la gravetat i la prevenció de la contaminació creuada. Si netegem l'interior sense haver netejat abans l'exterior, en obrir la caixa o manipular els filtres, tota la brutícia acumulada a fora caurà sobre els components electrònics nets.

Per garantir la màxima eficiència i evitar haver de repetir passos, l'ordre d'actuació estricte és el següent:

1. Fase Exterior  
   * Filtres Antipols: Abans d'obrir el panell lateral, extreu tots els filtres magnètics o de rail (frontal, superior i inferior de la font).  
     * Acció: Neteja'ls lluny de l'equip amb aigua i sabó (i asseca'ls perfectament) o amb aire comprimit.  
     * Per què primer? Si obres la caixa amb els filtres bruts, la vibració farà que caigui la pols sobre la placa base.  
   * Reixetes de Ventilació: Neteja les reixetes fixes del xassís amb un drap o raspall per evitar que la pols externa entri en treure la pressió negativa de la caixa.  
2. Fase d'Obertura i Desallotjament  
   * Obertura: Retira els panells laterals.  
   * Expulsió General (Aire Comprimit): Aplica aire comprimit per desallotjar les "boles de pols" que hi hagi solts pel fons de la caixa.  
     * Direcció: Sempre de Dalt a Baix i del Centre cap a Fora. Fes que la pols caigui a terra o surti fora de la caixa. Mai bufis de baix a dalt, o la pols es tornarà a dipositar als components superiors.  
3. Fase de Detall (Components Mecànics)  
   * Dissipadors: És on s'acumula la pols més persistent. Utilitza aire comprimit a través de les aletes d'alumini.  
   * Ventiladors: La pols s'adhereix a la vora de les aspes per fricció estàtica i no marxa només amb aire.  
     * Acció: Bloqueja el ventilador i neteja cada aspa manualment amb un bastonet de cotó humitejat en alcohol isopropílic o un raspall ESD.  
4. Fase de Contacte (Placa i Circuits)  
   * Un cop hem tret la pols "volàtil", queda la capa fina de pols adherida a la placa base.  
   * Acció: Utilitza un pinzell ESD suau per escombrar delicadament la superfície de la placa base i la part posterior de la targeta gràfica.  
5. Fase Final  
   * Fons de la Caixa: Aspira o recull amb un drap humit la pols que ha caigut al fons del xassís durant tot el procés anterior.  
   * Tancament: Torna a col·locar els filtres (ja nets i secs) i els panells laterals.  
   * Neteja Estètica: Neteja l'exterior de la caixa i el vidre trempat amb microfibra.

Un punt crític de seguretat durant aquest procés és el bloqueig mecànic dels rotors. Quan s'aplica aire comprimit a alta pressió sobre un ventilador, aquest pot girar a revolucions molt superiors a les de disseny. Com que un motor elèctric és constructivament idèntic a un generador, un ventilador girant lliurement per l'efecte de l'aire genera un corrent elèctric invers (Back EMF) que retorna cap a la placa base. Aquest voltatge no regulat pot cremar fàcilment el controlador del ventilador (Fan Header) o altres components sensibles de la placa. Per tant, el tècnic ha d'immobilitzar sempre les aspes amb un dit o una eina no conductora abans de bufar.

🎯 **Aclariment pràctic**: Tot i que són potents, els compressors d'aire genèrics (de taller mecànic o benzinera) no s'han d'utilitzar mai directament sobre electrònica delicada sense un filtre separador d'aigua. L'aire comprimit industrial sol contenir microgotes d'oli i humitat de condensació del tanc que, en ser projectades sobre la placa base, poden causar curtcircuits immediats o corrosió futura.

#### 

#### **Gestió i Substitució del Compost Tèrmic (TIM)**

La pasta tèrmica (Thermal Interface Material) és un compost viscós la funció del qual és omplir les imperfeccions microscòpiques entre la superfície del processador i la base del dissipador per maximitzar la transferència de calor. Amb el temps i els cicles de temperatura, la matriu de silicona o oli de la pasta s'evapora, deixant un residu sòlid i esquerdat que perd conductivitat. Es recomana la seva substitució cada 2-3 anys com a part del manteniment preventiu.

![](img/image6.png)

*Pasta tèrmica damunt que cal substituir en el processador*

El procés de substitució exigeix una neteja meticulosa. S'ha de retirar la pasta antiga utilitzant paper de cel·lulosa humitejat en alcohol isopropílic fins que les superfícies metàl·liques quedin impol·lutes. Per a l'aplicació de la nova pasta, la tècnica més acceptada per a la majoria de processadors d'escriptori és el mètode del "gra d'arròs": aplicar una petita quantitat al centre geomètric del processador. La pressió exercida pel mecanisme de muntatge del dissipador s'encarregarà d'escampar el material radialment, creant una capa fina i uniforme sense bombolles d'aire.

Substitució de Pasta Tèrmica

1. L'èxit d'aquesta operació depèn de la neteja, no de la quantitat de pasta nova.  
2. Retirada: Utilitza paper de cuina sec per treure el gruix de la pasta vella.  
3. Purificació: Humiteja un paper net o un bastonet de cotó amb Alcohol Isopropílic. Frega la superfície del processador i la base del dissipador fins que no surti gris al paper. El metall ha de brillar.  
4. Aplicació: Col·loca una gota de pasta nova al centre geomètric de la CPU.  
   * Mida de referència: Com un pèsol petit o un gra d'arròs (aprox. 4 mm de diàmetre). No l'escampis manualment; es poden crear bombolles d'aire.  
5. Assentament: Col·loca el dissipador a sobre, ben pla. Un cop faci contacte, no l'aixequis per mirar, o trencaràs el segell de buit.  
6. Fixació: Collar els cargols en patró de creu (X) (cantonada superior esquerra \+ inferior dreta, etc.) per repartir la pressió uniformement.

🧰 **Consell pràctic**: La pasta tèrmica no és un gran conductor de calor per si mateixa (és molt pitjor que el metall); només és millor que l'aire. Per tant, l'objectiu és tenir la capa més fina possible que cobreixi tota la superfície. Aplicar massa pasta tèrmica és contraproduent, ja que crea una barrera gruixuda que dificulta el pas de la calor del CPU al dissipador, empitjorant les temperatures en lloc de millorar-les.

#### **Higiene de Perifèrics i Pantalles**

El manteniment físic s'estén a la interfície humana. En el cas dels monitors, les pantalles modernes (LCD/OLED) compten amb recobriments químics antireflectants que són extremadament sensibles. L'ús de productes netejavidres comercials basats en amoníac o alcohol d'alta concentració destrueix aquesta capa protectora, causant taques permanents ("clouding"). La neteja s'ha de realitzar exclusivament amb productes específics per a panells o amb un drap humitejat lleugerament amb aigua destil·lada.

És imperatiu no polvoritzar mai líquid directament sobre la pantalla. La gravetat farà que el líquid llisqui cap avall, penetrant pel marc inferior (bezel) on s'ubiquen els circuits de control del panell (PCB Driver), provocant fallades irreversibles en la imatge. El líquid s'ha d'aplicar sempre al drap, mai al dispositiu. Pel que fa als teclats mecànics o de membrana, l'acumulació de matèria orgànica sota les tecles es tracta desmuntant els casquets (keycaps) i utilitzant aire comprimit i hisops amb alcohol per desinfectar la superfície.