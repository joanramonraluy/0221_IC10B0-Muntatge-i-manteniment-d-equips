#### **Objectiu**

Aprendre a utilitzar el multímetre per mesurar de forma segura tensió, corrent i resistència en circuits senzills i fonts d’alimentació.

#### **Introducció**

El multímetre és una de les eines més importants per a qualsevol tècnic de muntatge i manteniment d’equips informàtics. Permet comprovar si una font d’alimentació dona la tensió correcta, si un cable està trencat, si una resistència té el valor esperat o si hi ha continuïtat en un circuit. Tot i això, un ús incorrecte pot danyar l’aparell o, fins i tot pitjor, provocar curtcircuits i situacions perilloses en els equips que es volen reparar. En aquest apartat aprendrem a identificar les parts principals d’un multímetre digital típic, a seleccionar la funció adequada en cada cas i a connectar les puntes de prova amb seguretat abans de fer qualsevol mesura.

#### **Parts del multímetre i seguretat bàsica**

Un multímetre digital està format per diversos elements que cal conèixer abans de començar a utilitzar‑lo. A la part frontal hi trobem una pantalleta que mostra el valor mesurat, una roda o botons de selecció de funcions i rangs, i sovint alguns botons addicionals com HOLD o modes especials (continuïtat, prova de díodes, etc.). A la part inferior hi ha les preses de connexió on s’endollen les puntes de prova: una presa comuna (COM, habitualment de color negre) i una o dues preses addicionals per a mesures de tensió i resistència (V/Ω) i per a mesures de corrent (A o mA, sovint diferenciades).

FOTO: multimetre

​Les puntes de prova consten d’un cable flexible amb un connector banana a un extrem i una punta metàl·lica aïllada a l’altre, generalment de color vermell per al positiu i negre per al comú. A l’interior del multímetre hi ha, a més, fusibles que protegeixen els circuits interns quan es supera el límit de corrent admès en una de les preses; aquests fusibles poden fondre’s si el multímetre s’utilitza de forma incorrecta, per exemple mesurant corrent en un circuit on hi ha una tensió elevada sense la resistència adequada.

FOTO: fusibles multimetre

​Abans de fer qualsevol mesura, és imprescindible aplicar unes normes bàsiques de seguretat. Cal comprovar sempre en quina presa està connectada la punta vermella i en quin mode està posada la roda selectora, especialment abans de tocar circuits alimentats. No s’ha de tocar mai amb els dits la part metàl·lica de les puntes quan es mesuren tensions o corrents, i s’ha d’evitar manipular el multímetre amb les mans mullades o en superfícies metàl·liques sense aïllament. En treballar amb fonts d’alimentació d’ordinadors de sobretaula, es recomana sempre mesurar només a la part de baixa tensió (sortides DC) i no obrir mai la font per accedir als circuits interns.

#### **Connexió de les puntes segons el tipus de mesura**

La manera de connectar les puntes al multímetre varia en funció de si es vol mesurar tensió, corrent o resistència. La punta negra gairebé sempre es connecta a la presa COM, que fa de referència comuna per a totes les mesures. La punta vermella, en canvi, s’ha de connectar a la presa adequada segons la funció: a la presa marcada com V/Ω quan es mesuren tensions, resistències o continuïtat, i a la presa A o mA quan es mesura corrent, segons el rang de corrent esperat.

🧰 **Consell pràctic**: Una confusió habitual que cal evitar és deixar la punta vermella a la presa de corrent (A o mA) i, després, intentar mesurar tensió sobre un circuit. En aquesta situació, el multímetre es comporta com un pont gairebé directe entre les puntes, i si es connecta entre dos punts amb diferència de potencial es pot produir un curtcircuit i cremar el fusible intern o fins i tot danyar el circuit que es volia comprovar. Per això, abans de tocar el circuit sempre s’ha de fer una doble comprovació ràpida: punta negra a COM, punta vermella a V/Ω per mesurar tensió o resistència, i selector en el mode correcte.

Quan es mesura tensió, el multímetre s’ha de connectar en paral·lel amb el component o la font que es vol analitzar, és a dir, tocant els dos punts entre els quals volem saber la diferència de potencial. En canvi, quan es mesura corrent, el multímetre s’ha d’inserir en sèrie amb el circuit perquè tot el corrent passi a través de l’aparell, cosa que implica obrir el circuit i intercalar les puntes.

🧰 **Consell pràctic**: Per a principiants i en situacions d’aprenentatge sovint es recomana limitar les mesures de corrent a circuits molt senzills i concentrar‑se sobretot en la mesura de tensió i resistència. 

#### **Selecció de funcions i rangs de mesura**

Els multímetres digitals ofereixen diversos modes principals de funcionament, que es seleccionen mitjançant la roda o els botons del frontal. Per als objectius d’aquesta unitat, els modes més utilitzats seran la mesura de tensió DC (corrent continu), la mesura de tensió AC (corrent altern), la mesura de resistència (Ω) i el mode de continuïtat, que acostuma a venir indicat amb el símbol d’un brunzidor o d’una ona sonora. En mode de tensió DC es mesuren, per exemple, les sortides d’una font d’alimentació de PC o d’un carregador de portàtil, mentre que en mode AC es podria mesurar la tensió d’una presa de xarxa (només en condicions molt controlades i amb explicacions prèvies de seguretat).

​Pel que fa als rangs, alguns multímetres treballen amb selecció automàtica (AUTO‑RANGE) i ajusten ells mateixos l’escala més adequada, mentre que d’altres requereixen escollir manualment el rang de valors (per exemple, 20 V, 200 V, 2 kΩ, 20 kΩ, etc.). En multímetres de rang manual, és recomanable començar amb un rang superior al valor esperat per evitar saturar el display i després anar ajustant cap avall per obtenir una lectura més precisa; per exemple, si es vol mesurar una tensió al voltant de 12 V, es pot començar en el rang de 20 V DC.

​FOTO: roda selectora d’un multimetre

Abans de tocar el circuit s’ha de comprovar que el selector està en el mode adequat (DCV, ACV, Ω o continuïtat) i que el rang triat té sentit per a la mesura que es vol fer. Si es deixa el selector en un mode incorrecte, com resistència o continuïtat, i es connecten les puntes a un circuit alimentat, es pot danyar el multímetre o obtenir lectures sense sentit. 

🧰 **Consell pràctic**: Alguns models disposen de la funció HOLD, que permet congelar la lectura a la pantalla un cop aconseguida, cosa útil quan la posició de mesura és incòmoda o les mans estan ocupades subjectant les puntes.

#### 

#### **Mesures pràctiques guiades en fonts i circuits senzills**

Una de les aplicacions més útils del multímetre al taller d’informàtica és la mesura de la tensió de sortida d’una font d’alimentació o d’un carregador, sense necessitat d’obrir la carcassa ni accedir als circuits interns. Per fer aquesta comprovació, es connecta la punta negra a un punt de referència negativa (com el contacte de massa d’un connector) i la punta vermella a la línia de tensió que es vol mesurar, amb el multímetre configurat en mode de tensió DC i rang adequat (per exemple, 20 V per a una sortida de 12 V o 19 V). D’aquesta manera es pot verificar si una font de PC realment proporciona 12 V, 5 V o 3,3 V dins dels marges acceptables, o si un carregador de portàtil dona la tensió indicada a la seva etiqueta.

​El multímetre també permet mesurar resistències en circuits senzills o en plaques de electròniques, així com utilitzar el mode de continuïtat per comprovar si hi ha contacte elèctric entre dos punts. Per mesurar una resistència cal que el component estigui desconnectat o sense tensió aplicada, situar el selector en el mode Ω, tocar amb les puntes els extrems del component i llegir el valor a la pantalla, comparant‑lo amb el valor nominal o amb el codi de colors. El mode de continuïtat, en canvi, no mostra tant el valor exacte com el fet de si el camí està obert o tancat; quan hi ha connexió, el multímetre emet un brunzit, cosa que resulta molt pràctica per comprovar cables, pistes de plaques o contactes de connectors sense haver d’estar mirant constantment el display.

​Aquestes mesures es poden relacionar directament amb la Llei d’Ohm i amb les magnituds de tensió, corrent i resistència treballades a la primera lliçó. Mesurant la tensió en els extrems d’una resistència i coneixent el seu valor òhmic, és possible deduir el corrent que hi circula, i a l’inrevés, mesurant corrent i tensió es podria verificar si el valor real de la resistència coincideix amb l’esperat. D’aquesta manera, el multímetre es converteix no només en una eina de diagnosi, sinó també en un instrument per comprovar a la pràctica les relacions teòriques estudiades a classe i per acostumar l’alumnat a treballar amb valors reals i no només amb exemples sobre el paper.

