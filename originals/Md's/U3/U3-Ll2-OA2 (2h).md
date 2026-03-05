#### **Objectiu**

Executar el protocol de diagnòstic seqüencial en equips sense resposta visual (No Video/No POST), interpretant els codis d'error acústics (xiulets) i lluminosos (LEDs de depuració) del sistema BIOS/UEFI per aïllar i identificar el component físic defectuós.

#### **Introducció**

L'escenari més desafiant per a un tècnic de suport es presenta quan un ordinador rep corrent elèctric i activa els seus ventiladors, però no mostra cap imatge en pantalla ni carrega el sistema operatiu. En aquesta situació, coneguda tècnicament com a fallada de POST (Power-On Self-Test), el professional perd la seva eina principal d'interacció: la interfície visual. L'equip s'ha convertit en una "caixa negra" inerta que es nega a comunicar-se, i la temptació de substituir components a l'atzar és elevada, però és una estratègia que sovint condueix a diagnòstics erronis i despeses innecessàries.

Per resoldre aquest bloqueig, és imprescindible comprendre que la placa base disposa de mecanismes de comunicació primitius, però extremadament fiables dissenyats per operar abans que existeixi la sortida de vídeo. El procés de POST és una autodiagnosi interna que verifica seqüencialment la presència i integritat de la CPU, la memòria RAM i la targeta gràfica. Quan un d'aquests elements falla, la BIOS atura l'arrencada i emet un codi d'error específic, ja sigui mitjançant seqüències de xiulets (codis acústics) o a través de panells de LEDs integrats en la placa (codis Q-Code o Debug LEDs).

Tot i això, la interpretació d'aquests codis és només la primera part de la solució. Quan el sistema no emet cap senyal o els codis són inconclusos, el tècnic ha d'aplicar el protocol d'aïllament per "Configuració Mínima". Aquesta metodologia consisteix a desmuntar l'equip fins a la seva expressió funcional més bàsica (només placa, processador i font d'alimentació) i afegir components un a un. En aquest OA, aprendrem a sistematitzar aquest procés de "divideix i venceràs", discriminant pas a pas quin element està provocant el col·lapse del bus del sistema.

#### **La Seqüència POST i la Interpretació de Codis**

El procés d'arrencada d'un ordinador segueix una jerarquia estricta governada per la BIOS/UEFI, coneguda com a POST (Power-On Self-Test). Comprendre aquest ordre és vital: primer s'inicialitza la CPU, després es verifica la memòria RAM, seguidament es detecta la targeta gràfica (GPU) i, finalment, es busquen dispositius d'emmagatzematge. Quan l'equip es queda amb la pantalla negra, significa que s'ha "encallat" en un d'aquests passos. La placa base intenta comunicar quin és el pas fallit a través de dos mètodes principals:

* Codis Acústics (Beep Codes): Tot i ser una tecnologia antiga, el brunzidor piezoelèctric (speaker) continua sent l'eina de diagnòstic més fiable quan no hi ha imatge. Cada fabricant de BIOS (AMI, Award, Phoenix) té el seu propi "idioma", però hi ha estàndards universals que el tècnic ha de memoritzar. Un xiulet curt únic indica "Tot Correcte". Una seqüència repetitiva de xiulets llargs sol indicar error de memòria RAM mal inserida o defectuosa. Una seqüència d'un xiulet llarg seguit de dos o tres de curts assenyala generalment una fallada en el sistema de vídeo (targeta gràfica no detectada o sense alimentació). És fonamental que el taller disposi de brunzidors externs per connectar als pins "SPK" del panell frontal, ja que moltes caixes modernes ja no n'incorporen de sèrie.

![][image1]

*Pins SPK o SPEAK del panell frontal a la placa base*

* Diagnosi Visual (Debug LEDs i Q-Code): Les plaques base modernes simplifiquen aquest procés mitjançant un sistema de quatre LEDs d'estat soldat al PCB, etiquetats habitualment com a CPU, DRAM, VGA i BOOT. Durant l'arrencada, aquests llums s'encenen seqüencialment; si el sistema es congela i el LED de "DRAM" es queda encès fixament, el tècnic sap immediatament que el problema està en la memòria, sense necessitat de comptar xiulets. En gammes més altes, trobem pantalles de dos dígits (Display de 7 segments) que mostren codis hexadecimals (Q-Codes). Un codi "00" o "D0" sovint indica una fallada crítica de la CPU o la placa base, mentre que un codi "55" és específic de falta de memòria.

![][image2]

*Placa base amb pantalla de dos dígits a la part superior esquerra*

#### **Estratègia de la “Configuració Mínima”**

Quan els codis d'error són confusos o inexistents (l'equip encén ventiladors, però no fa res més), l'única via científica és el desmuntatge total. Sovint, un error de "No POST" està causat per un curtcircuit derivat d'un contacte metàl·lic entre la part posterior de la placa base i el xassís, o per un perifèric USB defectuós que bloqueja el bus de 5 V. Per descartar aquestes variables externes, s'aplica la tècnica del "Breadboarding" (muntatge en banc).

Aquesta tècnica consisteix a extreure la placa base de la caixa i col·locar-la sobre una superfície no conductora (com la seva pròpia caixa de cartró o una catifa antiestàtica). En aquest escenari aïllat, es connecta únicament la font d'alimentació, el processador (amb el seu dissipador) i el brunzidor. No es connecta memòria RAM, ni disc dur, ni targeta gràfica, ni cables de la caixa (USB/Àudio), excepte el botó d'encesa (o es fa pont amb un tornavís als pins Power Switch). Si en encendre aquesta configuració mínima la placa emet xiulets desesperats demanant memòria RAM, és una excel·lent notícia: significa que la placa base, la CPU i la font d'alimentació estan "vives" i es comuniquen. A partir d'aquí, s'afegeixen components un a un (primer un mòdul de RAM, després la gràfica) fins que el sistema deixi d'arrencar; l'últim component afegit serà el culpable.

#### **El Factor "Clear CMOS"**

Abans de declarar un component com a defectuós, hi ha un pas obligatori: el restabliment de la BIOS. Una configuració incorrecta de voltatges, una freqüència de memòria no suportada (XMP inestable) o una corrupció de dades a la memòria CMOS poden provocar que un equip perfectament funcional sembli avariat. El tècnic ha de localitzar el pont (jumper) de CLR\_CMOS a la placa base o retirar la pila de botó CR2032 durant un minut amb la font desconnectada. Aquesta acció talla l'energia al xip que guarda la configuració, forçant la BIOS a carregar els valors de fàbrica (Fail-Safe Defaults) en la següent arrencada, recuperant sovint equips que es donaven per perduts.

![][image3]

*Pila de botó CR2032 inserida a la placa base*

💡 **Exemple**: Procediment Tècnic: Arbre de Decisió per a "Pantalla Negra".

Quan un equip encén (ventiladors giren) però no dona vídeo, segueix estrictament aquest flux per no perdre temps:

1. Reset de BIOS: Fes un Clear CMOS abans de tocar res més. Prova d'arrencar.  
2. Verificació de RAM: Si tens dos mòduls, treu-ne un. Prova d'arrencar. Si falla, canvia'l per l'altre i prova-ho en un sòcol de memòria diferent. (La memòria és la causa del 60% de pantalles negres).  
3. Aïllament de Gràfica: Si la CPU té gràfics integrats, retira la targeta gràfica dedicada i connecta el monitor a la placa base.  
4. Desconnexió de Perifèrics: Desconnecta tots els discs durs, lectors de DVD i dispositius USB (fins i tot teclat i ratolí). Un disc dur amb la controladora en curtcircuit pot bloquejar l'arrencada de tot l'equip.  
5. Mètode "Fora de la Caixa": Si res funciona, desmunta-ho tot i fes breadboarding només amb CPU i Font.  
6. Si pita (demanant RAM): La placa i CPU estan bé.  
7. Si no pita (i tens brunzidor connectat): El problema és crític: o la Font, o la Placa Base, o la CPU estan avariades.

[image1]: img/image1_oa2.png

[image2]: img/image2_oa2.png

[image3]: img/image3_oa2.png