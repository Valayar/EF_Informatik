"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[529],{3905:(e,n,t)=>{t.d(n,{Zo:()=>p,kt:()=>c});var r=t(7294);function i(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function a(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function l(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?a(Object(t),!0).forEach((function(n){i(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function s(e,n){if(null==e)return{};var t,r,i=function(e,n){if(null==e)return{};var t,r,i={},a=Object.keys(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||(i[t]=e[t]);return i}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(i[t]=e[t])}return i}var o=r.createContext({}),d=function(e){var n=r.useContext(o),t=n;return e&&(t="function"==typeof e?e(n):l(l({},n),e)),t},p=function(e){var n=d(e.components);return r.createElement(o.Provider,{value:n},e.children)},m={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},u=r.forwardRef((function(e,n){var t=e.components,i=e.mdxType,a=e.originalType,o=e.parentName,p=s(e,["components","mdxType","originalType","parentName"]),u=d(t),c=i,h=u["".concat(o,".").concat(c)]||u[c]||m[c]||a;return t?r.createElement(h,l(l({ref:n},p),{},{components:t})):r.createElement(h,l({ref:n},p))}));function c(e,n){var t=arguments,i=n&&n.mdxType;if("string"==typeof e||i){var a=t.length,l=new Array(a);l[0]=u;var s={};for(var o in n)hasOwnProperty.call(n,o)&&(s[o]=n[o]);s.originalType=e,s.mdxType="string"==typeof e?e:i,l[1]=s;for(var d=2;d<a;d++)l[d]=t[d];return r.createElement.apply(null,l)}return r.createElement.apply(null,t)}u.displayName="MDXCreateElement"},9418:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>o,contentTitle:()=>l,default:()=>m,frontMatter:()=>a,metadata:()=>s,toc:()=>d});var r=t(7462),i=(t(7294),t(3905));const a={},l="Finaler Blogeintrag",s={permalink:"/EF_Informatik/NumTrip game Blog/Finaler Blogeintag",editUrl:"https://github.com/Valayar/EF_Informatik/tree/main/blog/NumTrip game Blog/Finaler Blogeintag.md",source:"@site/blog/NumTrip game Blog/Finaler Blogeintag.md",title:"Finaler Blogeintrag",description:"Ziel des Spiels/Projekts",date:"2024-01-25T20:49:42.000Z",formattedDate:"25. Januar 2024",tags:[],readingTime:3.155,hasTruncateMarker:!1,authors:[],frontMatter:{},prevItem:{title:"Datenstruktur NumTrip",permalink:"/EF_Informatik/NumTrip game Blog/Datenstruktur Numtrip"},nextItem:{title:"Top down entwurf NumTrip",permalink:"/EF_Informatik/NumTrip game Blog/Top down entwurf Numtrip"}},o={authorsImageUrls:[]},d=[{value:"Ziel des Spiels/Projekts",id:"ziel-des-spielsprojekts",level:2},{value:"Was wird zum spielen des Spieles ben\xf6tigt:",id:"was-wird-zum-spielen-des-spieles-ben\xf6tigt",level:2},{value:"Neuer Top Down Entwurf:",id:"neuer-top-down-entwurf",level:2},{value:"Felder Auff\xfcllen",id:"felder-auff\xfcllen",level:2},{value:"Meine Tipps an dich:",id:"meine-tipps-an-dich",level:2}],p={toc:d};function m(e){let{components:n,...a}=e;return(0,i.kt)("wrapper",(0,r.Z)({},p,a,{components:n,mdxType:"MDXLayout"}),(0,i.kt)("h2",{id:"ziel-des-spielsprojekts"},"Ziel des Spiels/Projekts"),(0,i.kt)("p",null,"NumTrip ist ein simples python-Konsolen Spiel. Wir haben ein Spielfeld welches aus 5x5 Feldern mit veschiedenen Zahlen(Werten) besteht. Felder, welche ein angernzendes Feld mit derselben Zahl haben kann man ausw\xe4hlen und der Wert im ausgew\xe4hlten Feld verdoppelt sich. Die angrenzenden Felder werden geelert und mit zuf\xe4lligen neuen gef\xfcllt. Man gewinnt das Spiel indem man einen bestimmten wert Erreicht ohne das einem die M\xf6glichkeiten weitere Z\xfcge zu machen ausgehen. Falls du fragen hast, probiel das Spiel doch einfach aus. "),(0,i.kt)("h2",{id:"was-wird-zum-spielen-des-spieles-ben\xf6tigt"},"Was wird zum spielen des Spieles ben\xf6tigt:"),(0,i.kt)("p",null,"Damit du das Spiel auch spielen kannst, ben\xf6tigst du eine Phyton Konsole, auf welcher Phyton l\xe4uft. Daf\xfcr musst du zuerst einmal ",(0,i.kt)("a",{parentName:"p",href:"https://www.python.org/shell/"},"Python")," installieren. Mein Spiel spielst du vorz\xfcglicherweise in VSC, da mein Spiel die Erweiterung ",(0,i.kt)("a",{parentName:"p",href:"https://pypi.org/project/colorama/"},'"Colorama"')," ben\xf6tigt, damit in der Konsole die Farben von meinem Spiel angezigt werden k\xf6nnen und es nicht aufgrund von fehlenden Voraussetzungen abst\xfcrzt. "),(0,i.kt)("h2",{id:"neuer-top-down-entwurf"},"Neuer Top Down Entwurf:"),(0,i.kt)("p",null,(0,i.kt)("strong",{parentName:"p"},"Top Down Entwurf vor dem programmieren:"),"\n",(0,i.kt)("img",{alt:"Image",src:t(1961).Z,width:"3024",height:"4032"}),"\n",(0,i.kt)("strong",{parentName:"p"},"Top Down Entwurf nach dem programmieren:"),"\n",(0,i.kt)("img",{alt:"Image",src:t(1814).Z,width:"1010",height:"500"}),"\n",(0,i.kt)("strong",{parentName:"p"},"Hier eine Beschiebene Version:"),"\n",(0,i.kt)("img",{alt:"Image",src:t(3193).Z,width:"2244",height:"582"})),(0,i.kt)("h1",{id:"algorythmisches-konzept"},"Algorythmisches Konzept:"),(0,i.kt)("h2",{id:"felder-auff\xfcllen"},"Felder Auff\xfcllen"),(0,i.kt)("p",null,"Dieser Teil des Spieles ist eigentlich Ziemlich simpel. wir m\xfcssen eine Funktion programmieren, welche bei leeren Feldern die Zahl aus dem Feld dar\xfcber nimmt. "),(0,i.kt)("p",null,"Sp\xe4ter m\xfcssen wir der Funktion noch die M\xf6glichkeit geben bei den Obersten Feldern eine zuf\xe4llige Zahl zu importieren. "),(0,i.kt)("p",null,"Da mir dieses Problem zu gross war, habe ich zuerst in einem Seperaten Dokument gearbeitet. "),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Vorgehensweise:"),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("ol",{parentName:"li"},(0,i.kt)("li",{parentName:"ol"},"Simple Liste erstellen "))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("ol",{parentName:"li",start:2},(0,i.kt)("li",{parentName:"ol"},"F\xfcr jeden einzelnen Wert in den Zeilen wiederholen "))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("ol",{parentName:"li",start:3},(0,i.kt)("li",{parentName:"ol"},"Falls oberste Zeile, zufallszahl einf\xfcgen "))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("ol",{parentName:"li",start:4},(0,i.kt)("li",{parentName:"ol"},"mithilfe des Indexes werte von Feldern \xfcberschreiben"))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("ol",{parentName:"li",start:5},(0,i.kt)("li",{parentName:"ol"},"F\xfcr jede Zeile wiederholen ")))),(0,i.kt)("p",null,"Ich habe noch keine bessere Option daf\xfcr gefunden als das Programm f\xfcr jede Zele zu wiederholen, da ich keine gute m\xf6glichkeit hatte zu \xfcberpr\xfcfen ob es keine Leeren felder auf dem Spielfeld gibt. "),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py"},"field = [[1,2, ' '], [' ',' ', ' '],[ ' ', ' ' , ' ']]  # 1.\nsave = []\n\nimport random\nrandom.seed(2)\nnumbers = [1, 2, 4, 8]\n\ndef fieldrearrange():\n    for i in range(5):     # 5. \n        for x in field:\n\n            print(field.index(x))\n            for y in x :                # 2. \n                \n                print(x.index(y))\n                if y == ' ' :\n\n                    if field.index(x) <= 0:                            # 3. \n                        field[0][x.index(y)] = random.choice(numbers)\n            \n                    if field.index(x) > 0:      # 4. \n                        save = field[field.index(x) - 1][x.index(y)]\n                        field[field.index(x) - 1][x.index(y)] = ' '\n                        field[field.index(x)][x.index(y)] = save\n                        save = []\n\nfieldrearrange()   \nprint(field)\n")),(0,i.kt)("h1",{id:"schwierigkeiten-des-projektes"},"Schwierigkeiten des Projektes:"),(0,i.kt)("p",null,"Da dies mein erstes gr\xf6sseres Programmier-projekt war, hatte ich so einige Schwierigkeiten, welche sich aus verschiedensten Faktoren zusammensetzen. Das nicht vertraut sein mit Python oder VSC, oder das simple \xfcberfodert sein aufgrund fehlender kreativit\xe4t zur umsetzung. Meiner meinung nach war meine gr\xf6sste Schwierigkeit/Problematik dieses Projektes mein Zeitmanagement. Ich habe gelernt, dass wenn man selbst gut im Zeitpaln liegt schnell zur\xfcckfallen kann wenn man nach dem Konzept von ",(0,i.kt)("strong",{parentName:"p"},"try and error")," arbeitet. Es kann schnell passieren, dass man nicht das sich gesetzte Ziel erreicht und sich eine L\xf6sung findet. Ich habe mich bei diesem Projekt mehrmals erwischt wie ich etwas f\xfcr 30-45min ausprobiert habe und es schlussendlich wieder komplett verworfen habe, da ich eine andere herangehensweise f\xfcr besser hielt. Das ganze ist im grunde auch nicht so Problematisch, wenn da ich relativ viel spass bei der Arbeit hatte. Jedoch kann das ganze problematisch werden, wenn man sich daurch in der Zeit verkalkuliert oder verliert.                                                                                                    "),(0,i.kt)("h2",{id:"meine-tipps-an-dich"},"Meine Tipps an dich:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("strong",{parentName:"li"},"Tipps im Allgeminen"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},"Tausche dich mit anderen aus"),(0,i.kt)("li",{parentName:"ul"},"frage bei deinen Lehrern/Mitsch\xfclern nach"),(0,i.kt)("li",{parentName:"ul"},"Falls du noch nicht so erfahren bist und es nicht auf Anhieb funktioniert, lass dich dadurch nicht Frustrieren und Arbeite an einem anderen Tag weiter"))),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("strong",{parentName:"li"},"Tipps spezifisch f\xfcr dieses Projekt:"),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},"Lies dir die Theorie f\xfcr 2-Dimensionale Listen in Python nochmals durch "),(0,i.kt)("li",{parentName:"ul"},"Versuche dich an die empfohlene/vorgegebe Struckturierung zu halten")))))}m.isMDXComponent=!0},1961:(e,n,t)=>{t.d(n,{Z:()=>r});const r=t.p+"assets/images/Top_Down_Entwurf-ecb534ec81be27c8c46e96ae8fe153db.jpg"},1814:(e,n,t)=>{t.d(n,{Z:()=>r});const r=t.p+"assets/images/Top_Down_simple-9b9f9db1b995aa5ed67457d6a7f35b7f.png"},3193:(e,n,t)=>{t.d(n,{Z:()=>r});const r=t.p+"assets/images/Top_down_detail-8a934eb7460c3b55f2ad13dc66951f46.png"}}]);