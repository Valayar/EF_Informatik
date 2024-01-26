"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[588],{3905:(e,n,t)=>{t.d(n,{Zo:()=>u,kt:()=>m});var r=t(7294);function i(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function a(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function l(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?a(Object(t),!0).forEach((function(n){i(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function o(e,n){if(null==e)return{};var t,r,i=function(e,n){if(null==e)return{};var t,r,i={},a=Object.keys(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||(i[t]=e[t]);return i}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(i[t]=e[t])}return i}var p=r.createContext({}),s=function(e){var n=r.useContext(p),t=n;return e&&(t="function"==typeof e?e(n):l(l({},n),e)),t},u=function(e){var n=s(e.components);return r.createElement(p.Provider,{value:n},e.children)},c={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},d=r.forwardRef((function(e,n){var t=e.components,i=e.mdxType,a=e.originalType,p=e.parentName,u=o(e,["components","mdxType","originalType","parentName"]),d=s(t),m=i,f=d["".concat(p,".").concat(m)]||d[m]||c[m]||a;return t?r.createElement(f,l(l({ref:n},u),{},{components:t})):r.createElement(f,l({ref:n},u))}));function m(e,n){var t=arguments,i=n&&n.mdxType;if("string"==typeof e||i){var a=t.length,l=new Array(a);l[0]=d;var o={};for(var p in n)hasOwnProperty.call(n,p)&&(o[p]=n[p]);o.originalType=e,o.mdxType="string"==typeof e?e:i,l[1]=o;for(var s=2;s<a;s++)l[s]=t[s];return r.createElement.apply(null,l)}return r.createElement.apply(null,t)}d.displayName="MDXCreateElement"},2529:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>p,contentTitle:()=>l,default:()=>c,frontMatter:()=>a,metadata:()=>o,toc:()=>s});var r=t(7462),i=(t(7294),t(3905));const a={},l="Arbeit an NumTrip",o={permalink:"/EF_Informatik/NumTrip game Blog/Arbeit an NumTrip",editUrl:"https://github.com/Valayar/EF_Informatik/tree/main/blog/NumTrip game Blog/Arbeit an NumTrip.md",source:"@site/blog/NumTrip game Blog/Arbeit an NumTrip.md",title:"Arbeit an NumTrip",description:"Floodfill",date:"2024-01-25T20:49:42.000Z",formattedDate:"25. Januar 2024",tags:[],readingTime:1.7,hasTruncateMarker:!1,authors:[],frontMatter:{},prevItem:{title:"Wiedereinstieg in Python",permalink:"/EF_Informatik/Wiedereinstieg in Python"},nextItem:{title:"Datenstruktur NumTrip",permalink:"/EF_Informatik/NumTrip game Blog/Datenstruktur Numtrip"}},p={authorsImageUrls:[]},s=[],u={toc:s};function c(e){let{components:n,...t}=e;return(0,i.kt)("wrapper",(0,r.Z)({},u,t,{components:n,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"nachbarzellen-kombinieren"},"Nachbarzellen Kombinieren"),(0,i.kt)("p",null," ",(0,i.kt)("strong",{parentName:"p"},"Floodfill")),(0,i.kt)("p",null,"Das Prinzip einer Floodfill funktion ist ja noch relativ einfach zu verstehen. Wie diese in der Programmierspache implementiert wird, ist eine andere Sache. zun\xe4chst hatte ich mir den zugeh\xf6renden Wikipediaeintrag dazu angeschaut. "),(0,i.kt)("p",null,"jedoch konnte ich mir den unterschied von diesen zwei Codebl\xf6cken nicht erkl\xe4ren."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py"},"def fill4(x, y, alteFarbe, neueFarbe):\n    if getPixel(x, y) == alteFarbe:\n        setPixel(x, y, neueFarbe)\n        fill4(x, y + 1, alteFarbe, neueFarbe)  # unten\n        fill4(x, y - 1, alteFarbe, neueFarbe)  # oben\n        fill4(x + 1, y, alteFarbe, neueFarbe)  # rechts\n        fill4(x - 1, y, alteFarbe, neueFarbe)  # links\n")),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py"},"def fill4(x, y, alteFarbe, neueFarbe):\n    stack.push(x, y)\n    while stack.isNotEmpty():\n        (x, y) = stack.pop()\n        if getPixel(x, y) == alteFarbe:\n            setPixel(x, y, neueFarbe)\n            stack.push(x, y + 1)\n            stack.push(x, y - 1)\n            stack.push(x + 1, y)\n            stack.push(x - 1, y)\n")),(0,i.kt)("p",null,"Der obere ist ganz allgemein, der andere ist prim\xe4r f\xfcr Phyton. "),(0,i.kt)("p",null,"Ich habe mir noch ein noch ein Praxisbeispiel zum Floodfill-Algorythmus angeschaut.\nDurch dieses habe ich die Anwendung besser verstehen k\xf6nnen. "),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py"},"def flood_fill(x ,y, old, new):\n    # we need the x and y of the start position, the old value,\n    # and the new value\n    # the flood fill has 4 parts\n    # firstly, make sure the x and y are inbounds\n    if x < 0 or x >= len(field[0]) or y < 0 or y >= len(field):\n        return\n    # secondly, check if the current position equals the old value\n    if field[y][x] != old:\n        return\n    \n    # thirdly, set the current position to the new value\n    field[y][x] = new\n    # fourthly, attempt to fill the neighboring positions\n    flood_fill(x+1, y, old, new)\n    flood_fill(x-1, y, old, new)\n    flood_fill(x, y+1, old, new)\n    flood_fill(x, y-1, old, new)\n")),(0,i.kt)("p",null,"Dieses Beispiel l\xf6st das Problem des oberen Algorythmus welcher nicht erkennt kann ob man sich innerhalb des Feldes befindet. Weil sobald ein Feld ausserhalb der Liste ver\xe4ndert werden soll, bekommen wir die Fehlermeldung: ",(0,i.kt)("strong",{parentName:"p"},"IndexError: list index out of range")," "),(0,i.kt)("p",null,"Ich habe diesen Beispielscode modifiziert und in meinem NumTrip Game implementiert. "),(0,i.kt)("p",null,"Quellenangaben:",(0,i.kt)("br",{parentName:"p"}),"\n",(0,i.kt)("a",{parentName:"p",href:"https://de.wikipedia.org/wiki/Floodfill"},"Wikipediaeintrag Floodfill"),(0,i.kt)("br",{parentName:"p"}),"\n",(0,i.kt)("a",{parentName:"p",href:"https://python.plainenglish.io/a-python-example-of-the-flood-fill-algorithm-bced7f96f569"},"A Python Example of the Flood Fill Algorithm\n")))}c.isMDXComponent=!0}}]);