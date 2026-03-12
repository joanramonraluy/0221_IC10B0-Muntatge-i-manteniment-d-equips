### **Glosari**

Tipus de Sistemes i Instal·lació

* Sistema Operatiu Convencional: Programari que resideix de manera persistent al disc dur (SSD/HDD). Conserva les dades després d'apagar l'equip i requereix instal·lació prèvia. Exemples: Windows, macOS, GNU/Linux.  
* Live OS (Sistema Live): Sistema operatiu que s'executa íntegrament a la memòria RAM des d'un mitjà extern (USB/DVD) sense tocar el disc dur intern. És volàtil (els canvis es perden en reiniciar) i ideal per a diagnosi i recuperació de dades.  
* Instal·lació Neta (Clean Install): Procediment que implica esborrar qualsevol rastre anterior al disc dur i implantar una còpia fresca del sistema operatiu. Garanteix l'eliminació de virus i errors heretats.  
* Particionament: Divisió lògica del disc dur. En Linux, és habitual separar l'arrel (/), la memòria d'intercanvi (SWAP) i les dades d'usuari (/home) per seguretat i gestió.  
* Sistema de Fitxers: Mètode d'organització de les dades al disc. Els més comuns són NTFS (Windows) i EXT4 (Linux).

Desplegament i Clonació (Empresarial)

* Clonació de Disc (Disk Imaging): Tècnica que crea una còpia exacta bit a bit d'un disc dur, incloent-hi particions i sectors d'arrencada, per replicar-la en altres equips.  
* Equip Mestre (Golden Image / Maqueta): Ordinador configurat a la perfecció amb el sistema, controladors i programari corporatiu, que serveix de model per crear la imatge que es clonarà a la resta d'equips.  
* Sysprep / Regeneració d'IDs: Procés de post-clonació necessari per canviar els identificadors únics (com el SID a Windows o Machine-ID a Linux) i evitar conflictes quan diversos equips clonats es connecten a la mateixa xarxa.  
* PXE (Preboot eXecution Environment): Estàndard que permet arrencar un ordinador a través de la targeta de xarxa, descarregant el sistema operatiu des d'un servidor remot sense necessitat de dispositius d'emmagatzematge físic locals.  
* NBP (Network Bootstrap Program): Petit fitxer executable que el client descarrega via TFTP durant l'arrencada PXE per iniciar el procés d'instal·lació.

Manteniment de Programari i Controladors

* Controlador (Driver): Peça de codi que actua de pont entre el nucli del sistema operatiu i el component físic (maquinari), permetent que funcionin correctament.  
* Firmware (BIOS/UEFI): Programari allotjat en un xip de memòria no volàtil de la placa base. La seva actualització (flashing) és crítica i de risc, necessària per corregir vulnerabilitats o admetre nous processadors.  
* Bloatware (Crapware): Programari preinstal·lat pel fabricant (demos d'antivirus, jocs, utilitats redundants) que consumeix recursos innecessàriament i que cal eliminar per optimitzar el rendiment.  
* Repositoris: Magatzems centralitzats i verificats de programari (típics en Linux i botigues d'aplicacions) que milloren la seguretat respecte a la descàrrega d'executables des de webs de tercers.

Eines de Diagnosi i Seguretat Lògica

* Programari Portable: Aplicacions que s'executen sense instal·lació prèvia, ideals per portar en un "USB tècnic" i no deixar rastre a l'ordinador del client,.  
* Punt de Restauració: "Fotografia" de la configuració del sistema (registre, controladors) en un moment donat, que permet revertir canvis sense afectar els fitxers personals.  
* Regla 3-2-1: Estratègia de còpies de seguretat: 3 còpies de les dades, en 2 tipus de suport diferents, i 1 còpia ubicada fora del lloc físic habitual (núvol o altre edifici).  
* Hardware ID: Codi únic (Vendor ID \+ Device ID) que permet identificar un dispositiu desconegut a l'Administrador de Dispositius per buscar-ne el controlador correcte.

Noves Tendències i Tecnologies

* SoC (System on Chip): Arquitectura on processador, gràfica i memòria s'integren en un sol xip, comú en mòbils i portàtils ultralleugers, dificultant-ne l'ampliació.  
* NPU (Neural Processing Unit): Coprocessador dedicat exclusivament a accelerar tasques d'intel·ligència artificial localment, alliberant la CPU i la GPU.  
* SBC (Single Board Computer): Ordinadors complets en una sola placa de la mida d'una targeta de crèdit (ex: Raspberry Pi), utilitzats en entorns industrials o educatius.  
* Undervolting: Tècnica d'optimització que consisteix a reduir el voltatge del processador sense baixar-ne la velocitat, millorant l'eficiència energètica i reduint la temperatura.  
* Manteniment Predictiu: Ús de dades en temps real i IA (sensors IoT) per detectar patrons anòmals i predir fallades abans que es produeixin.

