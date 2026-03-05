#### **Objectiu**

Diagnosticar els colls d'ampolla de rendiment en un equip mitjançant l'anàlisi de mètriques de recursos (CPU, RAM, Disc), i executar l'ampliació física dels components limitants —principalment emmagatzematge SSD i memòria RAM— verificant la compatibilitat tècnica i quantificant la millora obtinguda a través de proves de rendiment (benchmarking).

#### **Introducció**

Amb el pas del temps, és habitual que els usuaris percebin una degradació en la velocitat dels seus equips: el sistema triga minuts a arrencar, les aplicacions s'obren amb retard o l'ordinador es bloqueja en intentar fer diverses tasques alhora. Davant d'aquest escenari, la solució no sempre implica la compra d'una màquina nova. Sovint, el processador central (CPU) té potència de sobres, però el sistema està sent frenat per un únic component que actua com a coll d'ampolla.

En el manteniment evolutiu, el tècnic actua com un estrateg. La seva missió és detectar quina és la "baula feble" de la cadena de processament. En la gran majoria d'equips amb més de 3 anys d'antiguitat, aquest fre és el disc dur mecànic (HDD). La substitució d'aquesta tecnologia magnètica obsoleta per unitats d'estat sòlid (SSD) representa l'actualització amb major impacte en el rendiment percebut, capaç de revitalitzar equips que es consideraven inservibles. De la mateixa manera, l'ampliació de la memòria RAM permet al sistema gestionar el programari modern, cada cop més voraç en recursos, sense haver de recórrer a la lenta memòria virtual.

Tanmateix, l'ampliació de maquinari comporta un repte lògic: les dades. El client vol que el seu ordinador vagi més ràpid, però no vol perdre els seus documents, configuracions ni programes instal·lats. Per tant, aquest OA va més enllà de connectar un SSD i aprofundeix en les tècniques de clonatge de discs i migració de sistemes. Per tant, aprendrem a utilitzar programari específic per replicar bit a bit el contingut d'un disc antic al nou, aconseguint que l'usuari gaudeixi de la millora de velocitat mantenint el seu entorn de treball intacte.

#### **Diagnosi de Rendiment: Identificació del Coll d'Ampolla**

El manteniment evolutiu comença amb una auditoria. Un ordinador és un sistema interconnectat on el rendiment global està limitat pel seu component més lent, conegut com a coll d'ampolla. Per identificar-lo, s'han d'analitzar les mètriques de rendiment en un escenari d'ús real (amb les aplicacions de l'usuari obertes).

Utilitzant l'Administrador de Tasques de Linux o el Monitor de Recursos de Windows, observarem tres escenaris clàssics:

* Saturació d'E/S (Disc al 100%): Si la línia d'activitat del disc està plana al màxim mentre la CPU i la RAM tenen càrrega baixa, el disc dur mecànic és el fre. És el cas més habitual en equips de més de 3 anys. Solució: Canvi a SSD.  
* Saturació de Memòria (RAM \> 85%): Si la memòria física s'esgota, el sistema operatiu comença a fer paging (utilitzar el disc dur com a RAM lenta), provocant congelacions constants. Solució: Ampliació de mòduls RAM.  
* Saturació de Processament (CPU al 100%): Si el processador està al màxim de forma constant, l'equip ha arribat al seu límit tècnic. En aquest cas, les ampliacions tenen un retorn d'inversió baix i sovint és recomanable la substitució de l'equip (BER).

![][image1]

*Monitor del sistema d’un sistema operatiu Fedora*

#### **L'Emmagatzematge: Transició a Estat Sòlid (SSD)**

L'actualització més rendible del mercat és la substitució de Discs Durs (HDD) per Unitats d'Estat Sòlid (SSD). El tècnic ha de seleccionar la interfície adequada segons la placa base:

* SATA III (Format 2.5"): Compatible amb qualsevol equip que tingui un disc dur tradicional. Ofereix velocitats de lectura/escriptura al voltant de 550 MB/s. És l'opció estàndard per a equips antics o de gamma baixa.  
* NVMe M.2 (Format PCIe): Si la placa base disposa de ranura M.2, aquesta és l'opció obligatòria. Connecta directament al bus PCIe, oferint velocitats de 2.000 MB/s a 7.000 MB/s (Gen3/Gen4).

🧰 **Consell pràctic**: Nota d'Instal·lació M.2: Aquestes unitats s'insereixen amb un angle de 30 graus i es fixen amb un cargol mil·limètric. És crític no perdre aquest cargol i assegurar-se que la unitat queda totalment plana; si queda corbada per tensió, el PCB es trencarà amb la calor.

#### **Ampliació de Memòria RAM: Arquitectura i Compatibilitat**

Afegir memòria RAM és complex degut als requisits de compatibilitat estricta. Abans de comprar, cal utilitzar programari com CPU-Z (pestanya SPD) per llegir les especificacions dels mòduls ja instal·lats sense obrir la caixa.

Els criteris de selecció són jeràrquics:

1. Tecnologia: Mai es poden barrejar generacions (DDR3, DDR4, DDR5), ja que l'osca física (notch) està en posicions diferents.  
2. Format: Distingir entre DIMM (Mòduls llargs per a sobretaula) i SO-DIMM (Mòduls curts per a portàtils i Mini-PC).  
3. Freqüència i Latència: L'ideal és comprar un mòdul idèntic a l'existent. Si es barregen velocitats (ex: un de 2400 MHz i un de 3200 MHz), la placa base frenarà automàticament el més ràpid per igualar-lo al més lent, perdent rendiment.  
4. Configuració Dual Channel: Per maximitzar l'ample de banda, els mòduls s'han d'instal·lar en parelles en els sòcols corresponents (habitualment 2 i 4, o A2/B2). Això duplica la "carretera" de dades cap al processador.

#### **Validació Tècnica: Benchmarking**

Un cop instal·lat el maquinari, la feina no està acabada fins que es quantifica la millora. La percepció subjectiva ("ara va més ràpid") no és suficient per a un informe tècnic. S'utilitzen eines de Benchmarking (proves sintètiques) per generar dades objectives:

* CrystalDiskMark: Eina estàndard per mesurar velocitat de discs. Permet mostrar al client la diferència numèrica: "El seu disc vell llegia a 80 MB/s; el nou SSD llegeix a 550 MB/s".  
* Validació d'Estabilitat: Especialment en canvis de RAM, cal verificar que els nous mòduls no generen errors. Windows inclou l'eina Diagnòstic de Memòria de Windows (mdsched.exe), tot i que l'estàndard professional continua sent una passada ràpida amb MemTest86 si hi ha dubtes de compatibilitat.

![][image2]

*Comparativa de velocitats de lectura i escriptura en discs HDD i SSD*

[image1]: img/image1_l3oa1.png

[image2]: img/image2_l3oa1.png