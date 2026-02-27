#### **Objectiu**

Interpretar els senyals acústics, visuals i comportamentals de l'equip durant el procés d'autodiagnòstic (POST) per identificar errors de maquinari i aplicar protocols tècnics de resolució d'incidències.

#### **Introducció**

Un cop finalitzat el muntatge mecànic i el cablejat de l'equip, s'inicia la fase de validació funcional. Aquest procediment és crític, ja que és el primer moment en què el sistema rep corrent elèctric i els components interactuen entre si. L'objectiu no és simplement aconseguir que l'equip s'encengui, sinó verificar la integritat de totes les connexions i la correcta detecció del maquinari instal·lat.

En aquest OA analitzarem el comportament del sistema durant la seqüència d'arrencada. Aprendrem a interpretar els codis d'error que la placa base emet mitjançant indicadors lluminosos (LEDs) o senyals acústics abans de l'activació de la sortida de vídeo. Aquesta capacitat de diagnòstic és fonamental per diferenciar entre una fallada crítica de maquinari i un error de configuració o muntatge, cosa que permet aplicar la solució correctiva adequada de manera eficient.

#### **Procediment de Verificació Elèctrica Inicial**

Abans de procedir a l'encesa, és imperatiu realitzar una última comprovació de seguretat per evitar danys elèctrics als components.

Protocol de Pre-encesa (Checklist):

1. Alimentació: Verificar la connexió ferma del cable ATX (24 pins) i el connector EPS de la CPU (4/8 pins).  
2. Gràfica: Assegurar que la targeta gràfica té connectats els cables d'alimentació PCIe corresponents.  
3. Memòria: Confirmar que els mòduls RAM estan totalment inserits i els mecanismes de retenció tancats.  
4. Refrigeració: Comprovar l'estabilitat mecànica del dissipador sobre la CPU.  
5. Vídeo: Verificar que el cable del monitor està connectat a la targeta gràfica dedicada (horitzontal), i no a la placa base (llevat que s'utilitzi gràfica integrada).

Execució de l'encesa:

1. Connectar el cable d'alimentació i activar l'interruptor de la font (Posició "I"). Observar si s'encenen els LEDs d'estat de la placa base (indicador de corrent en espera o standby).  
2. Seguretat: Mantenir l'atenció en la font d'alimentació. En cas de sentir sorolls anòmals (espurneig) o detectar olor de cremat en prémer el botó d'encesa, s'ha d'interrompre el subministrament elèctric immediatament.  
3. Accionar el polsador d'encesa del xassís.

#### **Seqüència Lògica del POST (Power-On Self-Test)**

En iniciar l'equip, el microprogramari (BIOS/UEFI) executa una rutina d'autodiagnòstic seqüencial. És vital conèixer l'ordre d'aquesta seqüència per identificar en quin punt s'atura el sistema:

1. Verificació de CPU: La placa valida la presència i l'estat del processador.  
2. Verificació de DRAM: El sistema inicialitza i comprova la memòria RAM. Nota: Aquesta fase és la més propensa a errors de contacte o incompatibilitat.  
3. Verificació de VGA: Es detecta i inicialitza el dispositiu de sortida de vídeo.  
4. Verificació de BOOT: Es cerquen dispositius d'emmagatzematge amb sectors d'arrencada vàlids.

Si el sistema supera aquestes quatre etapes, emetrà un senyal de confirmació (habitualment un xiulet curt) i mostrarà imatge en pantalla.

🧰 **Consell pràctic sobre DDR5**: En equips d'última generació, la fase de verificació de DRAM pot demorar-se diversos minuts durant la primera arrencada a causa del procés d'entrenament de memòria (Memory Training). No s'ha de reiniciar l'equip durant aquest procés.

#### **Sistemes de Diagnòstic Integrats**

En cas d'error abans de la sortida de vídeo, la placa base comunica la incidència a través de dos mètodes principals:

A) Indicadors de Depuració (EZ Debug LEDs) Panell de 4 LEDs situat generalment a la vora dreta de la placa base (etiquetats: CPU, DRAM, VGA, BOOT).

* Funcionament: S'il·luminen seqüencialment durant el test. Si un LED roman encès de forma fixa, indica el component que ha fallat i atura la seqüència.  
  * CPU Fix: Error crític de processador o alimentació EPS absent.  
  * DRAM Fix: Error de memòria. Mòdul mal inserit o incompatible.  
  * VGA Fix: Error de targeta gràfica o absència de monitor detectat.  
  * BOOT Fix: No s'ha trobat sistema operatiu (comportament normal en discs nous).

B) Codis Acústics (Beep Codes) Requereix un altaveu de sistema (buzzer) connectat al panell frontal. Tot i que els codis varien segons el fabricant (AMI, Award), els més comuns són:

* 1 Bip Curt: POST correcte.  
* Bips llargs/repetitius: Error de memòria RAM.  
* 1 llarg \+ 3 curts: Error de targeta gràfica.  
* 5 Bips curts: Error de processador.

#### **Diagnòstic i Resolució d'Incidències Bàsiques**

* CAS A: Absència total de resposta elèctrica L'equip no mostra cap activitat (ventiladors aturats, sense llums).  
  * Verificació 1: Comprovar l'interruptor de la font i el cable de paret.  
  * Verificació 2: Revisar la connexió del cable ATX de 24 pins (requereix inserció ferma).  
  * Verificació 3: Validar el polsador de la caixa.  
    * Procediment tècnic: Desconnectar els cables del panell frontal i realitzar un pont momentani amb un tornavís entre els dos pins "PWR\_SW" de la placa. Si l'equip arrenca, el defecte resideix en el botó del xassís.  
* CAS B: Cicles de reinici continu (Boot Loop) L'equip s'encén, opera uns segons, s'apaga i torna a iniciar-se indefinidament.  
  * Diagnòstic: El sistema de protecció de la placa base s'activa per un error crític o curtcircuit.  
  * Acció: Reinstal·lar els mòduls de RAM. Si persisteix, verificar que no hi hagi separadors metàl·lics innecessaris sota la placa base fent contacte amb el circuit imprès.  
* CAS C: Sistema actiu sense senyal de vídeo (No Signal) L'equip sembla operar correctament (ventiladors i llums actius), però el monitor no rep senyal.  
  * Causa freqüent: Connexió incorrecta del cable de vídeo.  
  * Acció: Assegurar-se que el monitor està connectat directament a la targeta gràfica dedicada. Si es connecta a la placa base tenint una GPU instal·lada, el port de la placa queda inhabilitat.  
  * Acció secundària: Provar amb un altre cable de vídeo o monitor per descartar fallada del perifèric.