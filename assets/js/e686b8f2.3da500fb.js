"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[900],{3905:(e,n,t)=>{t.d(n,{Zo:()=>m,kt:()=>p});var r=t(7294);function i(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function a(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function o(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?a(Object(t),!0).forEach((function(n){i(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function s(e,n){if(null==e)return{};var t,r,i=function(e,n){if(null==e)return{};var t,r,i={},a=Object.keys(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||(i[t]=e[t]);return i}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(i[t]=e[t])}return i}var l=r.createContext({}),u=function(e){var n=r.useContext(l),t=n;return e&&(t="function"==typeof e?e(n):o(o({},n),e)),t},m=function(e){var n=u(e.components);return r.createElement(l.Provider,{value:n},e.children)},c={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},d=r.forwardRef((function(e,n){var t=e.components,i=e.mdxType,a=e.originalType,l=e.parentName,m=s(e,["components","mdxType","originalType","parentName"]),d=u(t),p=i,f=d["".concat(l,".").concat(p)]||d[p]||c[p]||a;return t?r.createElement(f,o(o({ref:n},m),{},{components:t})):r.createElement(f,o({ref:n},m))}));function p(e,n){var t=arguments,i=n&&n.mdxType;if("string"==typeof e||i){var a=t.length,o=new Array(a);o[0]=d;var s={};for(var l in n)hasOwnProperty.call(n,l)&&(s[l]=n[l]);s.originalType=e,s.mdxType="string"==typeof e?e:i,o[1]=s;for(var u=2;u<a;u++)o[u]=t[u];return r.createElement.apply(null,o)}return r.createElement.apply(null,t)}d.displayName="MDXCreateElement"},3074:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>l,contentTitle:()=>o,default:()=>c,frontMatter:()=>a,metadata:()=>s,toc:()=>u});var r=t(7462),i=(t(7294),t(3905));const a={},o="Erfahrungen zum Erstellen einer API mit Node-RED",s={permalink:"/EF_Informatik/Erstellen einer API mit Node-RED",editUrl:"https://github.com/Valayar/EF_Informatik/tree/main/blog/Erstellen einer API mit Node-RED.md",source:"@site/blog/Erstellen einer API mit Node-RED.md",title:"Erfahrungen zum Erstellen einer API mit Node-RED",description:"Postman",date:"2024-01-25T20:49:42.000Z",formattedDate:"25. Januar 2024",tags:[],readingTime:1.325,hasTruncateMarker:!1,authors:[],frontMatter:{},nextItem:{title:"Wiedereinstieg in Python",permalink:"/EF_Informatik/Wiedereinstieg in Python"}},l={authorsImageUrls:[]},u=[{value:"Postman",id:"postman",level:2},{value:"Node-RED",id:"node-red",level:2}],m={toc:u};function c(e){let{components:n,...t}=e;return(0,i.kt)("wrapper",(0,r.Z)({},m,t,{components:n,mdxType:"MDXLayout"}),(0,i.kt)("h2",{id:"postman"},"Postman"),(0,i.kt)("p",null,"Postman ist ein Programm, welches daf\xfcr genutzt wird um HTTP Anfragen zu \xfcberpr\xfcfen. Diese Technik wird ben\xf6tigt, falls man daran ist eine Webseite zu Programmieren und wissen muss was der Webserver als Antwort zur\xfcckgibt. So kann man testen ob alles Ordnungsgem\xe4ss funktioniert. Diese Technik wird auch ben\xf6tigt falls man eine API programmiert/entwickelt. (Stichwort Bugfixing) Ich bin mir hierbei zwar nicht ganz sicher, aber ich glaube, dass man diese Technik ben\xf6tigt, falls eine Webseite down ist und den genauen/ungef\xe4hren Fehler zu ermitteln. "),(0,i.kt)("p",null,"In unserem Beispiel haben wir mit Postman genutzt um auf unsere mit Node-RED erstellte API zuzugreifen."),(0,i.kt)("p",null,(0,i.kt)("strong",{parentName:"p"},"Warum Ben\xf6tigt man Postman eigentlich?"),"\nMan kann genauso die gew\xfcnschte Webadresse auch in einen Browser eingeben, und erh\xe4lt dasselbe Resultat. "),(0,i.kt)("p",null,(0,i.kt)("em",{parentName:"p"},"Der Grund daf\xfcr ist dieser: Wenn man es offline oder lokal ausprobieren m\xf6chte muss man Postman verwenden. Node-RED ist nach mir eine Ausnahme")),(0,i.kt)("h2",{id:"node-red"},"Node-RED"),(0,i.kt)("p",null,'Auf Node-RED besteht die von uns erstellte API aus verschiedenen "Workflows". In diesen Flows haben wir verschiedene Bausteine mit verschiedenen Funktionen aneinandergeh\xe4ngt. Durch das aneinanderh\xe4ngen dieser Funktionen wird die API programmiert. Allgemein wichtig ist der HTTP input sowie der HTTP output. So k\xf6nnen wir mit unserer "simulierten Webseite" kommunizieren. In der Konsole von Node-RED sollten wir auch Auslesen k\xf6nnen falls jemand unsere Webseite aufgerufen hat. Im Allgemeinen sollten wir auch nichts ausser dem Statuscode 200 von dieser "Webseite" erhalten. Dadurch wissen wir auch, dass alles funktioniert. Falls die Webseite nun auch eine Funktion haben soll kann man diese zwischen dem In und Output einf\xfcgen. Diese Funktion k\xf6nnen wir nun mit Java script Code f\xfcttern um unserer API eine Funktion zu geben.'))}c.isMDXComponent=!0}}]);