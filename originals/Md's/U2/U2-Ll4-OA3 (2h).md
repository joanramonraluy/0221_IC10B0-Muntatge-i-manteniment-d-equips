#### **Objectiu**

Executar proves de verificació preliminars per certificar que el muntatge s'ha realitzat correctament i que no hi ha components defectuosos d'origen, preparant l'equip per a la fase de manteniment i diagnòstic profund que es tractarà a la Unitat 3\.

#### **Introducció**

La configuració de la BIOS/UEFI marca el final de la intervenció lògica. Tanmateix, abans de tancar el xassís definitivament, és necessari realitzar una validació ràpida de l'estabilitat. No es tracta de fer un diagnòstic exhaustiu d'avaries, sinó d'assegurar-nos que el muntatge que acabem de fer és sòlid i que cap component ha arribat defectuós de fàbrica (Dead on Arrival).

En aquest darrer OA, utilitzarem eines bàsiques per confirmar que el dissipador fa bon contacte i que la memòria RAM no presenta errors físics immediats. Si detectem qualsevol anomalia ara, podrem corregir el muntatge a l'instant; si ho deixem passar, es convertirà en una incidència tècnica que haurem de resoldre amb els protocols avançats de la propera unitat.

#### **Monitoratge Passiu de Valors (H/W Monitor)**

El primer pas per validar que el muntatge del dissipador és correcte és l'observació estàtica dins de la BIOS.

Paràmetres de Control: Mantindrem l'equip encès dins de la BIOS durant 10 minuts.

* Temperatura de la CPU: Hauria d'estabilitzar-se entre 30 °C i 45 °C.  
  * Validació del Muntatge: Si la temperatura puja ràpidament a 60 °C o més estant en repòs, és un indicatiu clar que hem aplicat malament la pasta tèrmica o que el dissipador no està fent la pressió necessària. En aquest cas, caldrà desmuntar i revisar la instal·lació mecànica.  
* Voltatges: Cal confirmar que la font d'alimentació mostra valors estables. Una anàlisi més profunda de l'estabilitat elèctrica sota càrrega màxima es realitzarà a la Unitat 3\.

#### **Comprovació d'Integritat de Memòria (MemTest86)**

La memòria RAM és el component més propens a venir defectuós de fàbrica. Per evitar instal·lar un sistema operatiu sobre una base inestable, farem una passada ràpida amb MemTest86.

🎯 **Aclariment pràctic**: MemTest86 és el programari estàndard de la indústria (Gold Standard) per al diagnòstic i verificació de mòduls de memòria RAM en arquitectures x86 i ARM. Desenvolupat originalment l'any 1994, s'ha mantingut com l'eina de referència tant per a entusiastes com per a departaments tècnics professionals.

Procediment Simplificat:

1. Arrencar des de l'USB de diagnòstic.  
2. Deixar que el test faci el primer cicle (Pass 1).  
3. Interpretació:  
   * Si apareix algun error (vermell), el mòdul està defectuós i s'ha de tramitar la garantia abans de continuar.

🎯 **Aclariment**: A la Unitat 3 aprendrem a utilitzar aquesta eina per diagnosticar mòduls que fallen intermitentment en equips vells, però per ara només busquem defectes de fabricació evidents.

#### 

#### **Tancament Físic i Gestió Final**

Un cop certificat que el maquinari respon correctament i no hi ha errors de muntatge, procedim al tancament definitiu.

Protocol de Finalització:

1. Desconnexió Segura: Apagar i desconnectar de la xarxa.  
2. Gestió de Cablejat (Revisió): Verificar que cap cable intern frega amb els ventiladors. L'optimització del flux d'aire per a rendiment extrem es tractarà més endavant.  
3. Tancament del Xassís: Col·locar els panells laterals amb cura.  
4. Neteja: Retirar empremtes i pols. Un equip nou ha de semblar impecable.

