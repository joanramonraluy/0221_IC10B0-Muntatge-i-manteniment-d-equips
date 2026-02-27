#### **Arquitectura i Blocs Funcionals**

L'ordinador es basa en l'Arquitectura de Von Neumann, que divideix el sistema en tres parts: CPU (processament), Memòria (emmagatzematge temporal) i Entrada/Sortida, totes connectades per busos.

* Bloc de Processament: Inclou la CPU (cervell que executa instruccions) i la GPU (especialitzada en càlcul paral·lel i imatges).  
* Bloc de Memòria: Dividit en Volàtil (RAM, d'accés ultraràpid) i Persistent (Discs SSD/HDD per guardar dades a llarg termini).  
* Bloc d'Interconnexió: La Placa Base, que actua com a esquelet i sistema nerviós central.

  #### **El Nucli: Placa Base, CPU i RAM**

* Placa Base: El seu Factor de Forma (ATX, Micro-ATX, Mini-ITX) determina la mida i compatibilitat amb la caixa. El Chipset controla la comunicació amb els components, i el Sòcol (Socket) és on s'instal·la la CPU (LGA per a Intel/AMD nous, PGA per a AMD antics).  
* Processador (CPU): Es defineix per la seva freqüència (GHz), el nombre de nuclis i fils (threads), i la memòria Caché. Requereix un sistema de refrigeració (aire o líquida) i pasta tèrmica per evitar el *thermal throttling*.  
* Memòria RAM: És la memòria de treball. Per optimitzar el rendiment, s'han d'instal·lar mòduls en parelles per activar el Dual Channel.  
   **Emmagatzematge i Gràfics**  
* GPU: Pot ser Integrada (dins la CPU, per a ofimàtica) o Dedicada (targeta independent amb la seva pròpia VRAM, per a gaming o disseny).  
* Discs: Els SSD NVMe (M.2) són l'estàndard actual per velocitat, connectats directament a la placa base. Els HDD (mecànics) s'usen per a grans volums de dades pel seu baix cost.  
  **El Procés de Muntatge (Punts Crítics)**  
* Seguretat: Abans de tocar res, utilitzar una polsera antiestàtica (ESD) per no danyar els xips.  
* Premuntatge: Instal·lar CPU, RAM i M.2 a la placa base a sobre de la seva caixa de cartró (superfície aïllant) abans de ficar-la al xassís.  
* Separadors (Standoffs): Vital comprovar que la placa base no toqui directament el metall de la caixa per evitar curtcircuits.  
* Pasta Tèrmica: Aplicar només la mida d'un pèsol; l'excés pot ser contraproduent.  
   **Verificació i BIOS/UEFI**  
  Un cop muntat, el sistema executa el POST (Power-On Self-Test). Si alguna cosa falla, la placa avisa amb Beep Codes (xiulets) o Debug LEDs.  
* Dins la UEFI, és obligatori activar el perfil XMP/EXPO perquè la RAM funcioni a la seva velocitat real i configurar la seqüència d'arrencada (*Boot Priority*)  
  