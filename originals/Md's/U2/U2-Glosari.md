### **Glosari**

Processament i Arquitectura

* Arquitectura de Von Neumann: Model teòric en què es basen els ordinadors moderns, dividint la màquina en tres parts: CPU (processament), Memòria (emmagatzematge temporal) i Entrada/Sortida (comunicació), connectades per busos.  
* CPU (Unitat Central de Processament): El "cervell" de l'ordinador encarregat d'executar instruccions i fer càlculs. Està compost per milers de milions de transistors.  
* Nucli (Core): Unitat de processament independent dins d'un xip. Un processador Octa-core té 8 "cervells" físics que treballen simultàniament.  
* Fil (Thread): Unitat lògica d'execució. Tecnologies com Hyper-Threading o SMT permeten que un sol nucli físic gestioni dos fils (cues de treball) alhora.  
* IPC (Instruccions per Cicle): Quantitat de treball real que el processador fa en cada cicle de rellotge. És tan important com la freqüència per determinar la velocitat real.  
* TDP (Thermal Design Power): Mesura en Watts (W) que indica la quantitat de calor que el sistema de refrigeració ha de ser capaç de dissipar perquè la CPU funcioni correctament.  
* Arquitectura Híbrida (big.LITTLE): Disseny modern (com Intel 13a/14a gen) que barreja nuclis de rendiment (P-Cores) per a tasques pesades i nuclis d'eficiència (E-Cores) per a tasques de fons.

Placa Base i Connectivitat

* Factor de Forma (Form Factor): Estàndard que defineix la mida i els forats de muntatge de la placa base. Els més comuns són ATX (estàndard), Micro-ATX (reduït) i Mini-ITX (compacte).  
* Sòcol (Socket): Connector on s'instal·la el processador.  
  * LGA (Land Grid Array): Els pins estan a la placa base (típic d'Intel i AMD AM5).  
  * PGA (Pin Grid Array): Els pins estan al processador (típic d'AMD antics).  
* Chipset: Conjunt de xips (actualment PCH) que controla la comunicació de baixa velocitat com USB, SATA i algunes línies PCIe.  
* VRM (Mòdul Regulador de Voltatge): Components que converteixen els 12 V de la font als voltatges baixos (aprox. 1,1 V \- 1,4 V) i precisos que necessita la CPU.  
* PCIe (PCI Express): Bus d'expansió d'alta velocitat. Les ranures x16 (llargues) s'usen per a targetes gràfiques i les x1 (curtes) per a targetes de xarxa o so.

Memòria i Emmagatzematge

* RAM (Memòria d'Accés Aleatori): Memòria de treball volàtil i ultraràpida que emmagatzema les dades que el processador necessita immediatament. Es perd en apagar l'equip.  
* Dual Channel: Tecnologia que permet accedir a dos mòduls de RAM simultàniament, duplicant l'ample de banda (carrils de dades) de 64 a 128 bits.  
* XMP / EXPO: Perfils de configuració que cal activar a la BIOS per fer que la RAM funcioni a la seva velocitat màxima anunciada, superant l'estàndard bàsic JEDEC.  
* HDD (Disc Dur Mecànic): Dispositiu d'emmagatzematge magnètic amb plats giratoris i capçals mecànics. És econòmic per a gran capacitat però lent en accés aleatori.  
* SSD (Unitat d'Estat Sòlid): Emmagatzematge basat en memòria Flash sense parts mòbils. És molt més ràpid que un HDD.  
* NVMe: Protocol de comunicació per a SSDs que utilitza les línies PCIe per aconseguir velocitats molt superiors (fins a 7.000+ MB/s) respecte al protocol SATA.  
* M.2: Factor de forma ("forma de xiclet") per a discs SSD. Pot utilitzar tecnologia SATA (lenta) o NVMe (ràpida).

Gràfics (GPU)

* GPU (Unitat de Processament Gràfic): Circuit especialitzat en el processament paral·lel massiu, ideal per a gràfics 3D, renderitzat i IA.  
* iGPU (Gràfica Integrada): Nucli gràfic integrat dins el mateix processador. Utilitza la RAM del sistema com a memòria de vídeo.  
* dGPU (Gràfica Dedicada): Targeta independent amb el seu propi processador i memòria (VRAM). Ofereix molt més rendiment, però consumeix més energia.  
* VRAM (Video RAM): Memòria exclusiva de la targeta gràfica (tipus GDDR6/X) dissenyada per moure grans quantitats de dades de cop (ample de banda).

Muntatge, Refrigeració i Seguretat

* Pasta Tèrmica: Compost que s'aplica entre el processador (IHS) i el dissipador per omplir les imperfeccions microscòpiques i facilitar la transferència de calor.  
* Thermal Throttling: Mecanisme de protecció on el processador redueix dràsticament la seva velocitat i voltatge per evitar cremar-se quan arriba a la temperatura màxima.  
* Flux d'Aire (Airflow): Gestió del corrent d'aire dins la caixa.  
  * Pressió Positiva: Més ventiladors ficant aire que traient-ne (més net, menys pols).  
  * Pressió Negativa: Més ventiladors traient aire (pot refredar bé, però absorbeix pols per les escletxes).  
* ESD (Descàrrega Electrostàtica): Electricitat estàtica acumulada al cos que pot danyar els xips. S'evita amb una polsera antiestàtica connectada a terra.

BIOS, UEFI i Configuració

* UEFI (Unified Extensible Firmware Interface): El microprogramari modern que substitueix la BIOS. Interfície gràfica que controla el maquinari abans de carregar el sistema operatiu.  
* POST (Power-On Self-Test): Autodiagnòstic que fa l'equip en encendre's (CPU, RAM, GPU, Boot). Si falla, emet codis d'error (xiulets o LED).  
* Secure Boot: Protocol de seguretat que verifica la signatura digital del gestor d'arrencada per evitar l'execució de programari maliciós (rootkits) a l'inici.  
* TPM (Trusted Platform Module): Mòdul de seguretat (físic o per firmware fTPM) necessari per a Windows 11 que gestiona claus criptogràfiques.