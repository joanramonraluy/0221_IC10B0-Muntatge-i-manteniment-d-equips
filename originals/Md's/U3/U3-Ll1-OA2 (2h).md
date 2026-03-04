#### **Objectiu**

Interpretar la normativa legal i la documentació tècnica dels fabricants per gestionar eficaçment els tràmits d'Autorització de Retorn de Mercaderia (RMA), discriminant entre defectes de fabricació i danys induïts per evitar costos innecessaris.

#### **Introducció**

L'execució de tasques de manteniment correctiu deriva freqüentment en la identificació de components de maquinari amb fallades irreversibles que requereixen substitució. En un entorn professional, la resolució d'aquestes incidències no passa necessàriament per l'adquisició immediata d'un recanvi nou, sinó per l'exercici dels drets de garantia davant del proveïdor. Aquesta gestió, coneguda tècnicament com a logística inversa, constitueix una part fonamental de l'economia del departament tècnic.

Tanmateix, el retorn de material tecnològic no és un procés automàtic ni trivial. Els fabricants imposen protocols administratius estrictes i criteris d'acceptació rigorosos per filtrar devolucions fraudulentes o errors de diagnòstic. Un tècnic que desconegui com tramitar correctament una RMA (Return Merchandise Authorization) o que no sàpiga identificar quan una garantia ha estat invalidada per un mal ús, generarà pèrdues de temps i diners a la seva organització o clients. Per tant, és important gestionar correctament el cicle de vida administratiu d'una reparació externa.

#### **El Marc Administratiu: El Procediment RMA**

En l'ecosistema professional de la informàtica, la gestió de components defectuosos es regeix per protocols estrictes de logística inversa. A diferència del consumidor final, que pot acudir a la botiga amb un tiquet de compra, el tècnic professional ha d'operar sota l'estàndard RMA (Return Merchandise Authorization). Aquest concepte defineix l'autorització formal que un fabricant o distribuïdor majorista emet per acceptar el retorn d'un producte per a la seva revisió, reparació o substitució. És fonamental entendre que l'enviament d'un component sense aquest codi assignat prèviament derivarà inevitablement en el rebuig de la mercaderia a la recepció del magatzem, sent retornada a ports deguts i generant costos innecessaris per al taller.

El cicle de vida d'una RMA s'inicia amb l'obertura d'una incidència (ticket) en el portal de suport del proveïdor (Vendor). En aquesta fase, el tècnic no pot limitar-se a declarar que el dispositiu "no funciona"; ha d'aportar una descripció tècnica precisa de la falla, incloent-hi les proves creuades realitzades per descartar altres components i, sovint, evidències digitals com captures de pantalla dels codis d'error, fitxers de registre (logs) o fotografies de l'estat físic del producte. Un cop el fabricant valida la sol·licitud, s'emet el número d'RMA i les instruccions d'embalatge. La responsabilitat del tècnic s'estén fins al correcte empaquetament del producte: l'ús de bosses antiestàtiques (ESD) i proteccions mecàniques és mandatori. Si un component arriba al servei tècnic oficial amb danys de transport derivats d'un embalatge deficient, la garantia quedarà anul·lada automàticament, independentment de l'avaria original.

🎯 **Consell pràctic**: La Traçabilitat pel Número de Sèrie (S/N):  la garantia no està vinculada únicament a la factura de compra, sinó al Número de Sèrie (S/N) únic gravat al component. Els fabricants mantenen bases de dades detallades que permeten traçar la vida del producte: data de fabricació, data de sortida de fàbrica i distribuïdor assignat. Això implica que intentar tramitar la garantia d'un producte adquirit en un altre mercat geogràfic (Grey Market) o amb l'etiqueta del S/N il·legible o manipulada, causarà una denegació immediata del servei.

#### **![](img/image3.png)**

Dades del fabricant d’un component NVIDIA

#### **Gestió d'Incidències Crítiques: El Protocol D.O.A.**

Dins de la gestió de garanties, existeix una tipologia d'incidència que rep un tractament prioritari: el D.O.A. (Dead On Arrival o Mort a l'Arribada). Aquest terme tècnic classifica aquells productes que presenten una fallada funcional crítica en el moment de la primera posada en marxa o dins d'un període de temps molt reduït posterior al lliurament, habitualment establert per contracte entre 7 i 15 dies naturals (o fins a 30 dies en determinats fabricants Premium).

La correcta identificació i tramitació d'un DOA és estratègica per a la qualitat del servei al client. Mentre que una garantia estàndard implica l'entrada del producte en un circuit de reparació que pot demorar setmanes (mentre el fabricant intenta arreglar la placa electrònica), la declaració d'un DOA activa un protocol de substitució directa (Advanced Swap). En aquest escenari, el proveïdor envia immediatament una unitat totalment nova per substituir la defectuosa, sovint abans fins i tot de rebre la unitat avariada. 

🧰 **Consell pràctic**: Per a un tècnic, la capacitat de diagnosticar ràpidament un error de fabricació durant el muntatge o la primera setmana d'ús és vital per evitar que el client final hagi d'esperar el temps d'una reparació convencional per un producte que acaba de comprar.

#### **Auditoria Prèvia i Criteris d'Exclusió (Void Warranty)**

Abans d'iniciar qualsevol tràmit administratiu, el tècnic ha d'executar una inspecció visual forense del component per validar que compleix els requisits de cobertura. Els fabricants apliquen criteris d'exclusió molt estrictes per filtrar avaries causades per un mal ús. La causa més freqüent de rebuig és el Dany Induït pel Client (CID \- Customer Induced Damage). Aquesta categoria engloba qualsevol desperfecte físic estructural: cantonades de PCB trencades per impacte, pistes del circuit imprès seccionades per relliscades de tornavís, ports connectors arrencats per estrebades de cable o, el cas més paradigmàtic en processadors i plaques base, els pins del sòcol (LGA) o de la CPU (PGA) doblegats o trencats. La presència de qualsevol d'aquests signes invalida la totalitat de la garantia.

Addicionalment, s'ha de verificar l'absència de danys elèctrics externs o ambientals. Un component que presenti zones ennegrides, olor d'ozó o components (MOSFETs, condensadors) esclatats serà catalogat com a víctima de sobretensió elèctrica (Electrical Overstress \- EOS), una avaria considerada externa al producte i no coberta. De la mateixa manera, en entorns amb alta salinitat o humitat, l'aparició d'oxidació en els contactes metàl·lics o al voltant dels xips serà motiu de rebuig automàtic per condicions ambientals inadequades. Finalment, la integritat dels precintes de seguretat ("Warranty Void if Removed") és sagrada; la seva perforació, absència o manipulació, evidència una intervenció no autoritzada, alliberant al fabricant de qualsevol responsabilitat.

![](img/image4.png)

*Warranty Void if Removed en un component electronic*

#### **Documentació Tècnica i Justificació**

L'èxit d'una tramitació de garantia depèn en gran mesura de la qualitat de l'informe tècnic adjunt. El fabricant necessita repetir l'error per validar-lo, i per això el tècnic ha de redactar una descripció de l'avaria que sigui reproduïble. Una descripció vaga com "no funciona" o "falla a vegades" és insuficient i pot provocar que el component sigui retornat amb l'etiqueta NDF (No Defect Found), carregant al taller amb les despeses d'enviament i diagnòstic.

L'informe ideal ha d'estructurar-se detallant l'entorn de proves i els passos per reproduir l'error. 

💡 **Exemple**: S'instal·la la targeta gràfica en banc de proves amb font de 850 W certificada. En executar el test d'estrès FurMark, al cap de 120 segons la temperatura de la GPU assoleix els 95 °C i el sistema es reinicia, indicant un possible error en l'assemblatge del dissipador o la pasta tèrmica interna. S'ha provat en un segon equip amb idèntic resultat, descartant fallada de la font d'alimentació.

El nivell de detall tècnic de l’exemple anterior demostra professionalitat, agilitza l'aprovació de l'RMA i minimitza les discussions amb el departament de suport del fabricant.

🧰 **Consell pràctic**: L'ús de la Garantia com a Eina de Diagnòstic És una mala praxi professional utilitzar el procediment d'RMA com a mètode de "prova i error". Enviar un component a garantia només perquè "no sabem què li passa" sense haver confirmat que està avariat (provant-lo en un altre equip) satura els serveis tècnics, genera costos logístics i danya la reputació del tècnic davant del distribuïdor. La garantia és per a components confirmats com a defectuosos, no per a sospitosos.


