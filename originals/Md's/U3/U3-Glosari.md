### **Glosari**

Tipus de Manteniment

* Manteniment Preventiu: Conjunt d'accions programades i cícliques (neteja, actualitzacions) executades sobre un sistema operatiu per mitigar el desgast i reduir la probabilitat d'aturades, independentment de si l'equip presenta símptomes.  
* Manteniment Correctiu: Resposta tècnica reactiva a una avaria ja materialitzada per restaurar el servei. Pot ser immediat (urgència crítica) o diferit (programat per a un moment de menor impacte),.  
* Manteniment Predictiu: Estratègia basada en el monitoratge continu de sensors i dades en temps real (com S.M.A.R.T. o temperatura) per detectar anomalies incipients abans que provoquin una fallada.  
* Manteniment Evolutiu: Intervencions orientades a combatre l'obsolescència tecnològica millorant les prestacions de l'equip (ex: ampliar RAM o canviar a SSD) per satisfer nous requisits de programari.

Gestió de Garanties i RMA

* RMA (Return Merchandise Authorization): Autorització formal que un fabricant emet per acceptar el retorn d'un producte per a la seva revisió o reparació. És imprescindible obtenir aquest codi abans d'enviar res.  
* D.O.A. (Dead On Arrival): Producte que presenta una fallada funcional crítica en el moment de la primera posada en marxa o en un període molt reduït (7-15 dies). Sol implicar una substitució directa (Advanced Swap) en lloc de reparació.  
* CID (Customer Induced Damage): Dany induït pel client, com cops físics, pistes ratllades o pins doblegats. Aquest tipus de dany invalida automàticament la garantia.  
* NDF (No Defect Found): Etiqueta que aplica el fabricant quan retorna un component perquè no ha trobat cap error, sovint carregant costos al taller per un diagnòstic previ incorrecte.

Higiene Tècnica i Neteja

* Alcohol Isopropílic: Dissolvent orgànic (puresa \>90%) utilitzat per netejar electrònica perquè dissol olis i pastes tèrmiques, s'evapora ràpidament i no deixa residus conductors.  
* Back EMF (Força Contraelectromotriu): Corrent elèctric invers generat per un ventilador si es fa girar ràpidament amb aire comprimit sense bloquejar-lo, que pot cremar la placa base.  
* Pasta Tèrmica (TIM): Compost viscós que omple les imperfeccions microscòpiques entre el processador i el dissipador. S'ha de substituir cada 2-3 anys com a preventiu.

Diagnosi de Maquinari (Hardware)

* POST (Power-On Self-Test): Autodiagnòstic seqüencial que fa la BIOS/UEFI en arrencar (CPU → RAM → GPU → Boot). Si falla, s'atura i emet codis d'error.  
* Breadboarding (Configuració Mínima): Tècnica de diagnòstic que consisteix a muntar la placa base fora de la caixa sobre una superfície no conductora només amb CPU i font, per descartar curtcircuits amb el xassís.  
* Clear CMOS: Procediment per restablir la configuració de la BIOS als valors de fàbrica (esborrant possibles errors de configuració) mitjançant un jumper o traient la pila CR2032.  
* Testador de Fonts: Dispositiu físic que permet verificar ràpidament si la font d'alimentació lliura els voltatges correctes (+12 V \+5 V \+3,3 V) dins dels marges de tolerància.

Diagnosi de Programari i Senyals

* S.M.A.R.T.: Tecnologia d'automonitoratge dels discs durs i SSD que registra errors de lectura i sectors reassignats per predir fallades físiques,.  
* Live USB: Sistema operatiu que s'executa des de la memòria RAM sense dependre del disc dur de l'equip, ideal per a diagnòstics no invasius i recuperació de dades.  
* MemTest86: Programari estàndard per estressar i diagnosticar errors en cel·les específiques de la memòria RAM.  
* FurMark / Prime95: Eines de programari per realitzar proves d'estrès tèrmic a la GPU i CPU respectivament, forçant el maquinari al 100% per revelar problemes de refrigeració o estabilitat.  
* Artefactes (Artifacts): Anomalies visuals (formes geomètriques, colors estranys) que indiquen una fallada física a la memòria VRAM o al nucli de la targeta gràfica.  
* DDU (Display Driver Uninstaller): Eina per desinstal·lar completament controladors gràfics corruptes o conflictius abans de fer una instal·lació neta.

Ampliacions i Portàtils

* Coll d'Ampolla (Bottleneck): Component més lent del sistema que limita el rendiment global (sovint el disc dur mecànic en equips antics).  
* Spudger: Eina de plàstic utilitzada per fer palanca i separar les carcasses dels portàtils sense deixar marques ni trencar clips.  
* ZIF (Zero Insertion Force): Tipus de connector utilitzat en portàtils per a cables plans (teclat, trackpad). Requereix obrir una pestanya o mecanisme abans d'inserir o treure el cable.  
* Direct Die: Tipus de muntatge en portàtils on el dissipador toca directament el silici del processador (sense tapa IHS), requerint molta cura per no esquerdar el xip.