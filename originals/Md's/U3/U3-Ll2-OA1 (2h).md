#### **Objectiu**

Seleccionar i aplicar l'instrumental de mesura físic i les eines de programari de diagnòstic adequades per obtenir dades objectives sobre l'estat operatiu dels components, interpretant els resultats tècnics per identificar l'origen de la disfunció.

#### **Introducció**

La diferència entre un usuari avançat i un tècnic professional resideix en el mètode de treball. Davant d'una avaria, l'aficionat tendeix a operar per intuïció o per "prova i error" (canviant peces a l'atzar fins que l'equip funciona), una estratègia econòmicament ineficient i tècnicament arriscada. El professional, en canvi, basa les seves decisions en evidències quantificables. Per obtenir aquestes evidències, és imprescindible dominar les eines que permeten "interrogar" el sistema i fer visible allò que és invisible a l'ull humà: el flux elèctric, la integritat de les dades o l'estabilitat tèrmica sota càrrega.

En aquest OA, classificarem els mètodes de diagnosi en dues categories fonamentals. D'una banda, explorarem l'instrumental de maquinari, dispositius físics com el multímetre digital o els testadors de fonts d'alimentació, que ens permeten verificar si els components reben l'energia correcta abans fins i tot d'intentar encendre l'equip. Aquestes eines són la primera línia de defensa per descartar fallades elèctriques que podrien danyar els recanvis nous.

D'altra banda, ens endinsarem en l'ús de programari de diagnòstic. Quan l'equip encén, però presenta inestabilitat, reinicis aleatoris o lentitud, necessitem aplicacions capaces d'executar algoritmes intensius per posar a prova la memòria RAM, analitzar la superfície magnètica dels discs durs o forçar la targeta gràfica al seu límit tèrmic. L'objectiu d'aquestes eines no és reparar, sinó provocar la fallada en un entorn controlat per confirmar quina peça és la responsable, generant així un diagnòstic irrefutable.

#### **Diagnosi de Nivell Físic**

Abans de carregar qualsevol sistema operatiu, el tècnic ha de certificar la integritat elèctrica de l'equip. Molts errors aleatoris (reinicis, congelacions) no són culpa del programari, sinó d'un subministrament d'energia inestable. L'eina fonamental per a aquesta tasca és el Testador de Fonts d'Alimentació Digital. Aquest dispositiu permet connectar directament el connector ATX de 24 pins i els connectors auxiliars de la CPU (EPS) i PCIe per verificar, en temps real, si els voltatges lliurats es mantenen dins dels marges de tolerància de l'estàndard ATX (±5%). Un testador és més ràpid que un polímetre per a una comprovació, ja que emet una alarma sonora si detecta tensió insuficient o excessiva en els carrils crítics de \+12 V \+5 V i \+3,3 V.

![][image1]

*Testador de Fonts d'Alimentació Digital*

Per a una diagnosi de precisió o per comprovar la integritat de cables i fusibles, el Polímetre Digital (Multímetre) és insubstituïble. El tècnic ha de dominar l'ús del mode de Continuïtat (simbolitzat per una ona sonora o díode) per detectar circuits oberts —per exemple, un cable d'alimentació trencat internament o un botó d'encesa que no fa contacte— i el mode de Voltatge de Corrent Continu (VDC) per mesurar la tensió real en punts de test de la placa base o bateries de CMOS (CR2032) esgotades. Una bateria CMOS per sota de 2,8 V pot provocar que la BIOS perdi la configuració a cada arrencada, un error comú i fàcil de diagnosticar amb l'eina adequada.

![][image2]

*Polímetre Digital (Multímetre)*

#### **Entorns d'Execució Externs**

Un error conceptual greu en la diagnosi és intentar reparar un sistema operatiu corrupte utilitzant el mateix sistema operatiu. Si Windows està infectat o té fitxers danyats, les eines de diagnòstic executades des de dins poden donar falsos positius o ni tan sols arrencar. La solució professional és l'ús d'entorns Live USB (com Hiren's BootCD PE o Medicat).

![][image3]

*Hiren's BootCD funcionant com a sistema operatiu*

Aquests sistemes operatius lleugers s'executen directament des de la memòria RAM, sense dependre del disc dur de l'equip client. Això atorga al tècnic un avantatge tàctic doble: primer, permet accedir a les dades de l'usuari per fer còpies de seguretat fins i tot si el Windows original no arrenca; segon, proporciona un entorn "net" i aïllat des d'on llançar les eines de testatge de maquinari sense interferències de controladors o virus residents al disc dur. La creació i manteniment d'un "Pendrive Tècnic" actualitzat és una tasca obligatòria per a qualsevol professional del suport.

#### **Programari de Diagnosi Específic i Estressament**

Un cop dins l'entorn de diagnòstic, utilitzarem programari dissenyat per estressar components individuals. L'objectiu és forçar l'error per identificar-ne la causa.

* Memòria RAM (MemTest86): Els errors de memòria RAM són traïdors perquè sovint no són totals, sinó que afecten només a unes poques adreces de memòria específiques, provocant "Pantalles Blaves" (BSOD) aleatòries quan el sistema intenta escriure en aquell sector exacte. MemTest86 és l'estàndard de la indústria; funciona escrivint patrons de dades complexos (algoritmes) a tota la memòria i llegint-los després per comprovar si hi ha hagut corrupció. És una prova cíclica i infinita; una sola passada sense errors pot trigar hores, però un sol error vermell confirma la necessitat de substituir el mòdul.

![][image4]

*Menú principal de MemTest86*

* Emmagatzematge (CrystalDiskMark / Victoria): Per als discs durs i SSD, la diagnosi es basa en la lectura dels atributs S.M.A.R.T. (Self-Monitoring, Analysis and Reporting Technology). Eines com CrystalDiskMark llegeixen el firmware del disc per revelar l'estat de salut intern. El tècnic ha de fixar-se en paràmetres crítics com els "Sectors Reassignats" o els "Errors de CRC UltraDMA" (sovint culpa d'un cable SATA defectuós). Si l'estat és "Risc" o "Dolent", la còpia de seguretat immediata és prioritària abans de qualsevol intent de reparació.

![][image5]

*Imatge de CrystalDiskMark en funcionament*

* Estabilitat Gràfica i Tèrmica (FurMark / Prime95): Quan l'equip s'apaga sobtadament mentre l'usuari juga o renderitza vídeo, sovint és un problema de temperatura o de potència insuficient de la font. Eines com FurMark generen una càrrega artificial màxima sobre la GPU, disparant el consum i la calor. Si l'equip s'apaga instantàniament en iniciar el test, el culpable sol ser la font d'alimentació que no pot subministrar l'amperatge necessari; si l'equip aguanta, però la temperatura puja sense control fins al tall tèrmic, el problema és la refrigeració.

![][image6]

*Test d’estrès de FurMark en acció*

⚠️ **Advertiment de Seguretat:** Executar programari com Prime95 (CPU) o FurMark (GPU) posa el maquinari al 100% de la seva capacitat tèrmica. En equips amb mala refrigeració o molt bruts, això pot portar els components a temperatures perilloses en qüestió de segons. El tècnic mai ha de llançar una prova d'estrès i marxar; ha de monitoritzar la temperatura en temps real durant els primers minuts per avortar la prova manualment si es superen els llindars de seguretat (generalment 90-95 °C).

[image1]: img/image1.png

[image2]: img/image2.png

[image3]: img/image3.png

[image4]: img/image4.png

[image5]: img/image5.png

[image6]: img/image6.png