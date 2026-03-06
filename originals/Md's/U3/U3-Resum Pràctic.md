#### **Tipus de Manteniment**

No tots els manteniments són iguals. Es divideixen segons el moment en què s'actua:

* Manteniment Preventiu: Es fa abans que aparegui el problema per allargar la vida de l'equip (neteja de pols, canvi de pasta tèrmica cada 2-3 anys, actualització de drivers).  
* Manteniment Predictiu: Basat en eines de monitoratge que ens avisen abans que un component falli (ex: revisar l'estat de salut d'un disc amb l'atribut S.M.A.R.T.).  
* Manteniment Correctiu: Es realitza quan l'equip ja ha fallat. Inclou la reparació o substitució de peces.

#### **Eines de Diagnosi i Monitoratge**

Per no treballar a cegues, utilitzem programari especialitzat:

* Temperatura i voltatges: Eines com HWMonitor o Open Hardware Monitor. Ens permeten detectar si hi ha *thermal throttling* (baixada de rendiment per excés de calor).  
* Estat dels Discs: CrystalDiskInfo per llegir les dades S.M.A.R.T. (estat Bo, Alerta o Crític).  
* Memòria RAM: MemTest86 (s'executa des d'un USB abans que carregui el sistema operatiu) per detectar mòduls defectuosos.  
* Estrès del sistema: OCCT o Prime95 per forçar l'equip i veure si és estable sota càrrega màxima.

 **Metodologia de Resolució d'Avaries (Troubleshooting)**

Davant d'un error, cal seguir un ordre lògic per estalviar temps:

1. Identificar el problema: Recollir informació (què feia l'usuari?, hi ha missatges d'error?, xiulets?).  
2. Teoria de causes probables: Començar per les més evidents (està endollat?, el monitor està encès?).  
3. Provar la teoria: Si pensem que és la RAM, provar amb un sol mòdul o canviar-lo de ranura.  
4. Pla d'acció: Fer la reparació definitiva.  
5. Verificar el sistema: Comprovar que tot funciona i que no hem provocat un nou problema.  
6. Documentar: Registrar què ha passat i com s'ha solucionat (molt important en entorns professionals).

 **Avaries Comunes i Solucions**

* L'equip no encén: Possible fallada de la font d'alimentació o del cable de corrent.  
* L'equip encén, però no hi ha imatge: Problema de RAM (netejar contactes), GPU o placa base. Escolta els Beep Codes.  
* Pantalles Blaves (BSOD): Solen ser causades per drivers incompatibles, actualitzacions de Windows corruptes o fallades físiques de la RAM/Disc.  
* Sorolls estranys: Ventiladors obstruïts per pols o un disc dur mecànic (HDD) a punt de morir.

 **Gestió de Residus**

Com a tècnics, tenim una responsabilitat ambiental:

* Els components informàtics contenen metalls pesants i substàncies tòxiques.  
* Mai s'han de llençar a les escombraries convencionals. Cal portar-los a un Punt Net o centre de reciclatge especialitzat (RAEE \- Residus d'Aparells Elèctrics i Electrònics).

