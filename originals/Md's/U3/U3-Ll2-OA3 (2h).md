#### **Objectiu**

Diagnosticar i resoldre disfuncions en perifèrics d'entrada/sortida i conflictes de programari de control (drivers), discriminant entre fallades físiques (artefactes, píxels morts, connectors danyats) i errors lògics d'assignació de recursos, aplicant tècniques de neteja profunda de controladors.

#### **Introducció**

Sovint, un equip supera correctament la fase de POST i carrega el sistema operatiu, però l'experiència d'ús és defectuosa o impossible. Pantalles que parpellegen, resolucions incorrectes que no es poden canviar, ratolins que es desconnecten aleatòriament o "pantalles blaves" (BSOD) en executar aplicacions gràfiques són símptomes clau d'aquest escenari. El repte per al tècnic resideix a determinar si el culpable és el maquinari extern (un monitor envellit, un cable trencat) o l'interlocutor de programari que gestiona aquest maquinari: el controlador o driver.

Els controladors són peces de codi complexes que actuen de pont entre el nucli del sistema operatiu (Kernel) i el component físic. Un controlador corrupte, una actualització fallida de Windows Update o una incompatibilitat de versions poden generar símptomes idèntics a una targeta gràfica cremada. En aquest OA, aprendrem a distingir els defectes visuals físics (artefactes, problemes de panell) dels errors lògics i dominarem els protocols de "neteja quirúrgica" de controladors per restaurar l'estabilitat del sistema sense haver de formatar.

#### **Diagnosi Visual**

En l'àmbit de la imatge, el tècnic ha de saber interpretar les anomalies visuals. Un problema recurrent són els Artefactes (Artifacts): formes geomètriques estranyes, línies de colors aleatòries o textures corruptes que apareixen en pantalla, especialment en 3D. Aquests són indicadors gairebé segurs d'una fallada física en la memòria VRAM de la targeta gràfica o d'un sobreescalfament del nucli GPU. A diferència d'un error de driver (que sol tancar l'aplicació o reiniciar l'equip), els problemes de visualització físics persisteixen fins i tot a la BIOS o durant l'arrencada.

![][image1]

*Imatge de problemes d’artifacting en la imatge per pantalla del Sistema Operatiu*

D'altra banda, cal verificar la cadena de transmissió. Un cable HDMI o DisplayPort de mala qualitat o mal apantallat pot provocar pèrdues de senyal intermitents ("pantalla negra durant un segon") o "neu" digital. Finalment, en els monitors, hem de distingir entre un Píxel Mort (sempre negre, transistor fos) i un Píxel Encallat (Stuck Pixel, fix en vermell, verd o blau). Mentre que el primer és irreparable, el segon pot reaccionar a teràpies de programari que canvien de color ràpidament per "despertar" el transistor líquid.

🧰 **Consell pràctic**: El protocol EDID Quan connectem un monitor, aquest envia a l'ordinador una petita cadena de dades anomenada EDID (Extended Display Identification Data), que li diu "Sóc marca X, model Y i la meva resolució nativa és 1920x1080". Si el cable està danyat o el xip del monitor falla i aquesta informació no arriba i el sistema operatiu no sabrà quina resolució aplicar i es veurà borrós.

#### **Conflictes de Controladors i el "DLL Hell"**

La majoria de problemes "misteriosos" en els sistemes operatius provenen d'una mala gestió de drivers. Un escenari clàssic succeeix quan Windows Update instal·la automàticament un controlador gràfic genèric mentre l'usuari intenta instal·lar el controlador oficial del fabricant (NVIDIA/AMD). Aquesta col·lisió pot deixar fitxers de llibreries (.dll) duplicats o entrades de registre corruptes, provocant que el sistema no arrenqui la interfície gràfica (pantalla negra amb cursor).

![][image2]

Interfície de l’administrador de dispositius de MS Windows

Per solucionar això, no n'hi ha prou amb desinstal·lar el dispositiu des de l'Administrador de Dispositius, ja que Windows conserva còpies dels fitxers antics i els torna a reinstal·lar al reinici. Cal utilitzar eines especialitzades com DDU (Display Driver Uninstaller). Aquest programari s'executa en Mode Segur (per evitar que els fitxers estiguin en ús) i elimina absolutament qualsevol rastre, clau de registre i carpeta temporal associada a la gràfica, deixant el sistema net per a la instal·lació.

#### **Diagnosi de Perifèrics USB**

Els ports USB són una altra font habitual de conflictes. Un error freqüent és la saturació de corrent. Un port USB estàndard lliura 500 mA (USB 2.0) o 900 mA (USB 3.0). Si connectem un Hub USB passiu (sense endoll propi) i l'omplim de discs durs externs i llums LED, la demanda superarà l'oferta. El sistema reaccionarà desconnectant aleatòriament els dispositius per protegir la placa base (USB Device Not Recognized). El diagnòstic aquí implica verificar el consum a l'Administrador de Dispositius o utilitzar un tester USB físic.

🛠️ **Protocol Tècnic**: Reinstal·lació Neta de Gràfica.

Si un equip té pantalles negres, caigudes de FPS o tancaments de jocs, segueix aquest procediment estricte. No saltis cap pas:

1. Descàrrega Prèvia: Descarrega l'últim driver oficial de la web del fabricant (NVIDIA/AMD/Intel) i l'eina DDU. Guarda-ho a l'escriptori.  
2. Desconnexió de Xarxa: Dintro iesconnecta el cable Ethernet o apaga el Wi-Fi. Això evita que Windows Update intenti descarregar i instal·lar el seu propi controlador automàticament tan bon punt detecti que falta la gràfica.  
3. Mode Segur: Reinicia l'equip entrant en Mode Segur (Safe Mode). Això carrega Windows amb un controlador de vídeo bàsic (VGA), permetent esborrar els fitxers reals de la GPU sense bloquejos.  
4. Execució de DDU: Obre DDU i selecciona l'opció "Clean and Restart" (Netejar i Reiniciar).  
5. Instal·lació: Un cop reiniciat (encara sense internet), instal·la el driver que has descarregat al pas 1\.  
6. Reconnexió: Ara ja pots tornar a connectar internet.

[image1]: img/image1_oa3.png

[image2]: img/image2_oa3.png