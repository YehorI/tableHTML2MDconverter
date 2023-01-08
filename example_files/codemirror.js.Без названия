(function(e,t){"object"==typeof exports&&"undefined"!=typeof module?module.exports=t():"function"==typeof define&&define.amd?define(t):(e=e||self).CodeMirror=t()})(this,(function(){"use strict"
var e=navigator.userAgent,t=navigator.platform,r=/gecko\/\d/i.test(e),n=/MSIE \d/.test(e),i=/Trident\/(?:[7-9]|\d{2,})\..*rv:(\d+)/.exec(e),o=/Edge\/(\d+)/.exec(e),a=n||i||o,l=a&&(n?document.documentMode||6:+(o||i)[1]),s=!o&&/WebKit\//.test(e),c=s&&/Qt\/\d+\.\d+/.test(e),u=!o&&/Chrome\//.test(e),d=/Opera\//.test(e),f=/Apple Computer/.test(navigator.vendor),p=/Mac OS X 1\d\D([8-9]|\d\d)\D/.test(e),h=/PhantomJS/.test(e),m=!o&&/AppleWebKit/.test(e)&&/Mobile\/\w+/.test(e),g=/Android/.test(e),v=m||g||/webOS|BlackBerry|Opera Mini|Opera Mobi|IEMobile/i.test(e),y=m||/Mac/.test(t),b=/\bCrOS\b/.test(e),x=/win/i.test(t),w=d&&e.match(/Version\/(\d*\.\d*)/)
w&&(w=Number(w[1])),w&&w>=15&&(d=!1,s=!0)
var k=y&&(c||d&&(null==w||w<12.11)),_=r||a&&l>=9
function C(e){return new RegExp("(^|\\s)"+e+"(?:$|\\s)\\s*")}var S,T=function(e,t){var r=e.className,n=C(t).exec(r)
if(n){var i=r.slice(n.index+n[0].length)
e.className=r.slice(0,n.index)+(i?n[1]+i:"")}}
function M(e){for(var t=e.childNodes.length;t>0;--t)e.removeChild(e.firstChild)
return e}function L(e,t){return M(e).appendChild(t)}function z(e,t,r,n){var i=document.createElement(e)
if(r&&(i.className=r),n&&(i.style.cssText=n),"string"==typeof t)i.appendChild(document.createTextNode(t))
else if(t)for(var o=0;o<t.length;++o)i.appendChild(t[o])
return i}function A(e,t,r,n){var i=z(e,t,r,n)
return i.setAttribute("role","presentation"),i}function E(e,t){if(3==t.nodeType&&(t=t.parentNode),e.contains)return e.contains(t)
do{if(11==t.nodeType&&(t=t.host),t==e)return!0}while(t=t.parentNode)}function N(){var e
try{e=document.activeElement}catch(Ae){e=document.body||null}for(;e&&e.shadowRoot&&e.shadowRoot.activeElement;)e=e.shadowRoot.activeElement
return e}function q(e,t){var r=e.className
C(t).test(r)||(e.className+=(r?" ":"")+t)}function O(e,t){for(var r=e.split(" "),n=0;n<r.length;n++)r[n]&&!C(r[n]).test(t)&&(t+=" "+r[n])
return t}S=document.createRange?function(e,t,r,n){var i=document.createRange()
return i.setEnd(n||e,r),i.setStart(e,t),i}:function(e,t,r){var n=document.body.createTextRange()
try{n.moveToElementText(e.parentNode)}catch(Ae){return n}return n.collapse(!0),n.moveEnd("character",r),n.moveStart("character",t),n}
var I=function(e){e.select()}
function D(e){var t=Array.prototype.slice.call(arguments,1)
return function(){return e.apply(null,t)}}function F(e,t,r){for(var n in t||(t={}),e)!e.hasOwnProperty(n)||!1===r&&t.hasOwnProperty(n)||(t[n]=e[n])
return t}function P(e,t,r,n,i){null==t&&-1==(t=e.search(/[^\s\u00a0]/))&&(t=e.length)
for(var o=n||0,a=i||0;;){var l=e.indexOf("\t",o)
if(l<0||l>=t)return a+(t-o)
a+=l-o,a+=r-a%r,o=l+1}}m?I=function(e){e.selectionStart=0,e.selectionEnd=e.value.length}:a&&(I=function(e){try{e.select()}catch(t){}})
var W=function(){this.id=null,this.f=null,this.time=0,this.handler=D(this.onTimeout,this)}
function R(e,t){for(var r=0;r<e.length;++r)if(e[r]==t)return r
return-1}W.prototype.onTimeout=function(e){e.id=0,e.time<=+new Date?e.f():setTimeout(e.handler,e.time-+new Date)},W.prototype.set=function(e,t){this.f=t
var r=+new Date+e;(!this.id||r<this.time)&&(clearTimeout(this.id),this.id=setTimeout(this.handler,e),this.time=r)}
var $={toString:function(){return"CodeMirror.Pass"}},j={scroll:!1},H={origin:"*mouse"},B={origin:"+move"}
function U(e,t,r){for(var n=0,i=0;;){var o=e.indexOf("\t",n);-1==o&&(o=e.length)
var a=o-n
if(o==e.length||i+a>=t)return n+Math.min(a,t-i)
if(i+=o-n,n=o+1,(i+=r-i%r)>=t)return n}}var G=[""]
function V(e){for(;G.length<=e;)G.push(K(G)+" ")
return G[e]}function K(e){return e[e.length-1]}function Z(e,t){for(var r=[],n=0;n<e.length;n++)r[n]=t(e[n],n)
return r}function X(){}function Y(e,t){var r
return Object.create?r=Object.create(e):(X.prototype=e,r=new X),t&&F(t,r),r}var Q=/[\u00df\u0587\u0590-\u05f4\u0600-\u06ff\u3040-\u309f\u30a0-\u30ff\u3400-\u4db5\u4e00-\u9fcc\uac00-\ud7af]/
function J(e){return/\w/.test(e)||e>""&&(e.toUpperCase()!=e.toLowerCase()||Q.test(e))}function ee(e,t){return t?!!(t.source.indexOf("\\w")>-1&&J(e))||t.test(e):J(e)}function te(e){for(var t in e)if(e.hasOwnProperty(t)&&e[t])return!1
return!0}var re=/[\u0300-\u036f\u0483-\u0489\u0591-\u05bd\u05bf\u05c1\u05c2\u05c4\u05c5\u05c7\u0610-\u061a\u064b-\u065e\u0670\u06d6-\u06dc\u06de-\u06e4\u06e7\u06e8\u06ea-\u06ed\u0711\u0730-\u074a\u07a6-\u07b0\u07eb-\u07f3\u0816-\u0819\u081b-\u0823\u0825-\u0827\u0829-\u082d\u0900-\u0902\u093c\u0941-\u0948\u094d\u0951-\u0955\u0962\u0963\u0981\u09bc\u09be\u09c1-\u09c4\u09cd\u09d7\u09e2\u09e3\u0a01\u0a02\u0a3c\u0a41\u0a42\u0a47\u0a48\u0a4b-\u0a4d\u0a51\u0a70\u0a71\u0a75\u0a81\u0a82\u0abc\u0ac1-\u0ac5\u0ac7\u0ac8\u0acd\u0ae2\u0ae3\u0b01\u0b3c\u0b3e\u0b3f\u0b41-\u0b44\u0b4d\u0b56\u0b57\u0b62\u0b63\u0b82\u0bbe\u0bc0\u0bcd\u0bd7\u0c3e-\u0c40\u0c46-\u0c48\u0c4a-\u0c4d\u0c55\u0c56\u0c62\u0c63\u0cbc\u0cbf\u0cc2\u0cc6\u0ccc\u0ccd\u0cd5\u0cd6\u0ce2\u0ce3\u0d3e\u0d41-\u0d44\u0d4d\u0d57\u0d62\u0d63\u0dca\u0dcf\u0dd2-\u0dd4\u0dd6\u0ddf\u0e31\u0e34-\u0e3a\u0e47-\u0e4e\u0eb1\u0eb4-\u0eb9\u0ebb\u0ebc\u0ec8-\u0ecd\u0f18\u0f19\u0f35\u0f37\u0f39\u0f71-\u0f7e\u0f80-\u0f84\u0f86\u0f87\u0f90-\u0f97\u0f99-\u0fbc\u0fc6\u102d-\u1030\u1032-\u1037\u1039\u103a\u103d\u103e\u1058\u1059\u105e-\u1060\u1071-\u1074\u1082\u1085\u1086\u108d\u109d\u135f\u1712-\u1714\u1732-\u1734\u1752\u1753\u1772\u1773\u17b7-\u17bd\u17c6\u17c9-\u17d3\u17dd\u180b-\u180d\u18a9\u1920-\u1922\u1927\u1928\u1932\u1939-\u193b\u1a17\u1a18\u1a56\u1a58-\u1a5e\u1a60\u1a62\u1a65-\u1a6c\u1a73-\u1a7c\u1a7f\u1b00-\u1b03\u1b34\u1b36-\u1b3a\u1b3c\u1b42\u1b6b-\u1b73\u1b80\u1b81\u1ba2-\u1ba5\u1ba8\u1ba9\u1c2c-\u1c33\u1c36\u1c37\u1cd0-\u1cd2\u1cd4-\u1ce0\u1ce2-\u1ce8\u1ced\u1dc0-\u1de6\u1dfd-\u1dff\u200c\u200d\u20d0-\u20f0\u2cef-\u2cf1\u2de0-\u2dff\u302a-\u302f\u3099\u309a\ua66f-\ua672\ua67c\ua67d\ua6f0\ua6f1\ua802\ua806\ua80b\ua825\ua826\ua8c4\ua8e0-\ua8f1\ua926-\ua92d\ua947-\ua951\ua980-\ua982\ua9b3\ua9b6-\ua9b9\ua9bc\uaa29-\uaa2e\uaa31\uaa32\uaa35\uaa36\uaa43\uaa4c\uaab0\uaab2-\uaab4\uaab7\uaab8\uaabe\uaabf\uaac1\uabe5\uabe8\uabed\udc00-\udfff\ufb1e\ufe00-\ufe0f\ufe20-\ufe26\uff9e\uff9f]/
function ne(e){return e.charCodeAt(0)>=768&&re.test(e)}function ie(e,t,r){for(;(r<0?t>0:t<e.length)&&ne(e.charAt(t));)t+=r
return t}function oe(e,t,r){for(var n=t>r?-1:1;;){if(t==r)return t
var i=(t+r)/2,o=n<0?Math.ceil(i):Math.floor(i)
if(o==t)return e(o)?t:r
e(o)?r=o:t=o+n}}var ae=null
function le(e,t,r){var n
ae=null
for(var i=0;i<e.length;++i){var o=e[i]
if(o.from<t&&o.to>t)return i
o.to==t&&(o.from!=o.to&&"before"==r?n=i:ae=i),o.from==t&&(o.from!=o.to&&"before"!=r?n=i:ae=i)}return null!=n?n:ae}var se=function(){var e=/[\u0590-\u05f4\u0600-\u06ff\u0700-\u08ac]/,t=/[stwN]/,r=/[LRr]/,n=/[Lb1n]/,i=/[1n]/
function o(e,t,r){this.level=e,this.from=t,this.to=r}return function(a,l){var s="ltr"==l?"L":"R"
if(0==a.length||"ltr"==l&&!e.test(a))return!1
for(var c,u=a.length,d=[],f=0;f<u;++f)d.push((c=a.charCodeAt(f))<=247?"bbbbbbbbbtstwsbbbbbbbbbbbbbbssstwNN%%%NNNNNN,N,N1111111111NNNNNNNLLLLLLLLLLLLLLLLLLLLLLLLLLNNNNNNLLLLLLLLLLLLLLLLLLLLLLLLLLNNNNbbbbbbsbbbbbbbbbbbbbbbbbbbbbbbbbb,N%%%%NNNNLNNNNN%%11NLNNN1LNNNNNLLLLLLLLLLLLLLLLLLLLLLLNLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLN".charAt(c):1424<=c&&c<=1524?"R":1536<=c&&c<=1785?"nnnnnnNNr%%r,rNNmmmmmmmmmmmrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrmmmmmmmmmmmmmmmmmmmmmnnnnnnnnnn%nnrrrmrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrmmmmmmmnNmmmmmmrrmmNmmmmrr1111111111".charAt(c-1536):1774<=c&&c<=2220?"r":8192<=c&&c<=8203?"w":8204==c?"b":"L")
for(var p=0,h=s;p<u;++p){var m=d[p]
"m"==m?d[p]=h:h=m}for(var g=0,v=s;g<u;++g){var y=d[g]
"1"==y&&"r"==v?d[g]="n":r.test(y)&&(v=y,"r"==y&&(d[g]="R"))}for(var b=1,x=d[0];b<u-1;++b){var w=d[b]
"+"==w&&"1"==x&&"1"==d[b+1]?d[b]="1":","!=w||x!=d[b+1]||"1"!=x&&"n"!=x||(d[b]=x),x=w}for(var k=0;k<u;++k){var _=d[k]
if(","==_)d[k]="N"
else if("%"==_){var C=void 0
for(C=k+1;C<u&&"%"==d[C];++C);for(var S=k&&"!"==d[k-1]||C<u&&"1"==d[C]?"1":"N",T=k;T<C;++T)d[T]=S
k=C-1}}for(var M=0,L=s;M<u;++M){var z=d[M]
"L"==L&&"1"==z?d[M]="L":r.test(z)&&(L=z)}for(var A=0;A<u;++A)if(t.test(d[A])){var E=void 0
for(E=A+1;E<u&&t.test(d[E]);++E);for(var N="L"==(A?d[A-1]:s),q=N==("L"==(E<u?d[E]:s))?N?"L":"R":s,O=A;O<E;++O)d[O]=q
A=E-1}for(var I,D=[],F=0;F<u;)if(n.test(d[F])){var P=F
for(++F;F<u&&n.test(d[F]);++F);D.push(new o(0,P,F))}else{var W=F,R=D.length,$="rtl"==l?1:0
for(++F;F<u&&"L"!=d[F];++F);for(var j=W;j<F;)if(i.test(d[j])){W<j&&(D.splice(R,0,new o(1,W,j)),R+=$)
var H=j
for(++j;j<F&&i.test(d[j]);++j);D.splice(R,0,new o(2,H,j)),R+=$,W=j}else++j
W<F&&D.splice(R,0,new o(1,W,F))}return"ltr"==l&&(1==D[0].level&&(I=a.match(/^\s+/))&&(D[0].from=I[0].length,D.unshift(new o(0,0,I[0].length))),1==K(D).level&&(I=a.match(/\s+$/))&&(K(D).to-=I[0].length,D.push(new o(0,u-I[0].length,u)))),"rtl"==l?D.reverse():D}}()
function ce(e,t){var r=e.order
return null==r&&(r=e.order=se(e.text,t)),r}var ue=[],de=function(e,t,r){if(e.addEventListener)e.addEventListener(t,r,!1)
else if(e.attachEvent)e.attachEvent("on"+t,r)
else{var n=e._handlers||(e._handlers={})
n[t]=(n[t]||ue).concat(r)}}
function fe(e,t){return e._handlers&&e._handlers[t]||ue}function pe(e,t,r){if(e.removeEventListener)e.removeEventListener(t,r,!1)
else if(e.detachEvent)e.detachEvent("on"+t,r)
else{var n=e._handlers,i=n&&n[t]
if(i){var o=R(i,r)
o>-1&&(n[t]=i.slice(0,o).concat(i.slice(o+1)))}}}function he(e,t){var r=fe(e,t)
if(r.length)for(var n=Array.prototype.slice.call(arguments,2),i=0;i<r.length;++i)r[i].apply(null,n)}function me(e,t,r){return"string"==typeof t&&(t={type:t,preventDefault:function(){this.defaultPrevented=!0}}),he(e,r||t.type,e,t),we(t)||t.codemirrorIgnore}function ge(e){var t=e._handlers&&e._handlers.cursorActivity
if(t)for(var r=e.curOp.cursorActivityHandlers||(e.curOp.cursorActivityHandlers=[]),n=0;n<t.length;++n)-1==R(r,t[n])&&r.push(t[n])}function ve(e,t){return fe(e,t).length>0}function ye(e){e.prototype.on=function(e,t){de(this,e,t)},e.prototype.off=function(e,t){pe(this,e,t)}}function be(e){e.preventDefault?e.preventDefault():e.returnValue=!1}function xe(e){e.stopPropagation?e.stopPropagation():e.cancelBubble=!0}function we(e){return null!=e.defaultPrevented?e.defaultPrevented:0==e.returnValue}function ke(e){be(e),xe(e)}function _e(e){return e.target||e.srcElement}function Ce(e){var t=e.which
return null==t&&(1&e.button?t=1:2&e.button?t=3:4&e.button&&(t=2)),y&&e.ctrlKey&&1==t&&(t=3),t}var Se,Te,Me=function(){if(a&&l<9)return!1
var e=z("div")
return"draggable"in e||"dragDrop"in e}()
function Le(e){if(null==Se){var t=z("span","​")
L(e,z("span",[t,document.createTextNode("x")])),0!=e.firstChild.offsetHeight&&(Se=t.offsetWidth<=1&&t.offsetHeight>2&&!(a&&l<8))}var r=Se?z("span","​"):z("span"," ",null,"display: inline-block; width: 1px; margin-right: -1px")
return r.setAttribute("cm-text",""),r}function ze(e){if(null!=Te)return Te
var t=L(e,document.createTextNode("AخA")),r=S(t,0,1).getBoundingClientRect(),n=S(t,1,2).getBoundingClientRect()
return M(e),!(!r||r.left==r.right)&&(Te=n.right-r.right<3)}var Ae,Ee=3!="\n\nb".split(/\n/).length?function(e){for(var t=0,r=[],n=e.length;t<=n;){var i=e.indexOf("\n",t);-1==i&&(i=e.length)
var o=e.slice(t,"\r"==e.charAt(i-1)?i-1:i),a=o.indexOf("\r");-1!=a?(r.push(o.slice(0,a)),t+=a+1):(r.push(o),t=i+1)}return r}:function(e){return e.split(/\r\n?|\n/)},Ne=window.getSelection?function(e){try{return e.selectionStart!=e.selectionEnd}catch(Ae){return!1}}:function(e){var t
try{t=e.ownerDocument.selection.createRange()}catch(Ae){}return!(!t||t.parentElement()!=e)&&0!=t.compareEndPoints("StartToEnd",t)},qe="oncopy"in(Ae=z("div"))||(Ae.setAttribute("oncopy","return;"),"function"==typeof Ae.oncopy),Oe=null
var Ie={},De={}
function Fe(e,t){arguments.length>2&&(t.dependencies=Array.prototype.slice.call(arguments,2)),Ie[e]=t}function Pe(e){if("string"==typeof e&&De.hasOwnProperty(e))e=De[e]
else if(e&&"string"==typeof e.name&&De.hasOwnProperty(e.name)){var t=De[e.name]
"string"==typeof t&&(t={name:t}),(e=Y(t,e)).name=t.name}else{if("string"==typeof e&&/^[\w\-]+\/[\w\-]+\+xml$/.test(e))return Pe("application/xml")
if("string"==typeof e&&/^[\w\-]+\/[\w\-]+\+json$/.test(e))return Pe("application/json")}return"string"==typeof e?{name:e}:e||{name:"null"}}function We(e,t){t=Pe(t)
var r=Ie[t.name]
if(!r)return We(e,"text/plain")
var n=r(e,t)
if(Re.hasOwnProperty(t.name)){var i=Re[t.name]
for(var o in i)i.hasOwnProperty(o)&&(n.hasOwnProperty(o)&&(n["_"+o]=n[o]),n[o]=i[o])}if(n.name=t.name,t.helperType&&(n.helperType=t.helperType),t.modeProps)for(var a in t.modeProps)n[a]=t.modeProps[a]
return n}var Re={}
function $e(e,t){F(t,Re.hasOwnProperty(e)?Re[e]:Re[e]={})}function je(e,t){if(!0===t)return t
if(e.copyState)return e.copyState(t)
var r={}
for(var n in t){var i=t[n]
i instanceof Array&&(i=i.concat([])),r[n]=i}return r}function He(e,t){for(var r;e.innerMode&&(r=e.innerMode(t))&&r.mode!=e;)t=r.state,e=r.mode
return r||{mode:e,state:t}}function Be(e,t,r){return!e.startState||e.startState(t,r)}var Ue=function(e,t,r){this.pos=this.start=0,this.string=e,this.tabSize=t||8,this.lastColumnPos=this.lastColumnValue=0,this.lineStart=0,this.lineOracle=r}
function Ge(e,t){if((t-=e.first)<0||t>=e.size)throw new Error("There is no line "+(t+e.first)+" in the document.")
for(var r=e;!r.lines;)for(var n=0;;++n){var i=r.children[n],o=i.chunkSize()
if(t<o){r=i
break}t-=o}return r.lines[t]}function Ve(e,t,r){var n=[],i=t.line
return e.iter(t.line,r.line+1,(function(e){var o=e.text
i==r.line&&(o=o.slice(0,r.ch)),i==t.line&&(o=o.slice(t.ch)),n.push(o),++i})),n}function Ke(e,t,r){var n=[]
return e.iter(t,r,(function(e){n.push(e.text)})),n}function Ze(e,t){var r=t-e.height
if(r)for(var n=e;n;n=n.parent)n.height+=r}function Xe(e){if(null==e.parent)return null
for(var t=e.parent,r=R(t.lines,e),n=t.parent;n;t=n,n=n.parent)for(var i=0;n.children[i]!=t;++i)r+=n.children[i].chunkSize()
return r+t.first}function Ye(e,t){var r=e.first
e:do{for(var n=0;n<e.children.length;++n){var i=e.children[n],o=i.height
if(t<o){e=i
continue e}t-=o,r+=i.chunkSize()}return r}while(!e.lines)
for(var a=0;a<e.lines.length;++a){var l=e.lines[a].height
if(t<l)break
t-=l}return r+a}function Qe(e,t){return t>=e.first&&t<e.first+e.size}function Je(e,t){return String(e.lineNumberFormatter(t+e.firstLineNumber))}function et(e,t,r){if(void 0===r&&(r=null),!(this instanceof et))return new et(e,t,r)
this.line=e,this.ch=t,this.sticky=r}function tt(e,t){return e.line-t.line||e.ch-t.ch}function rt(e,t){return e.sticky==t.sticky&&0==tt(e,t)}function nt(e){return et(e.line,e.ch)}function it(e,t){return tt(e,t)<0?t:e}function ot(e,t){return tt(e,t)<0?e:t}function at(e,t){return Math.max(e.first,Math.min(t,e.first+e.size-1))}function lt(e,t){if(t.line<e.first)return et(e.first,0)
var r=e.first+e.size-1
return t.line>r?et(r,Ge(e,r).text.length):function(e,t){var r=e.ch
return null==r||r>t?et(e.line,t):r<0?et(e.line,0):e}(t,Ge(e,t.line).text.length)}function st(e,t){for(var r=[],n=0;n<t.length;n++)r[n]=lt(e,t[n])
return r}Ue.prototype.eol=function(){return this.pos>=this.string.length},Ue.prototype.sol=function(){return this.pos==this.lineStart},Ue.prototype.peek=function(){return this.string.charAt(this.pos)||void 0},Ue.prototype.next=function(){if(this.pos<this.string.length)return this.string.charAt(this.pos++)},Ue.prototype.eat=function(e){var t=this.string.charAt(this.pos)
if("string"==typeof e?t==e:t&&(e.test?e.test(t):e(t)))return++this.pos,t},Ue.prototype.eatWhile=function(e){for(var t=this.pos;this.eat(e););return this.pos>t},Ue.prototype.eatSpace=function(){for(var e=this.pos;/[\s\u00a0]/.test(this.string.charAt(this.pos));)++this.pos
return this.pos>e},Ue.prototype.skipToEnd=function(){this.pos=this.string.length},Ue.prototype.skipTo=function(e){var t=this.string.indexOf(e,this.pos)
if(t>-1)return this.pos=t,!0},Ue.prototype.backUp=function(e){this.pos-=e},Ue.prototype.column=function(){return this.lastColumnPos<this.start&&(this.lastColumnValue=P(this.string,this.start,this.tabSize,this.lastColumnPos,this.lastColumnValue),this.lastColumnPos=this.start),this.lastColumnValue-(this.lineStart?P(this.string,this.lineStart,this.tabSize):0)},Ue.prototype.indentation=function(){return P(this.string,null,this.tabSize)-(this.lineStart?P(this.string,this.lineStart,this.tabSize):0)},Ue.prototype.match=function(e,t,r){if("string"!=typeof e){var n=this.string.slice(this.pos).match(e)
return n&&n.index>0?null:(n&&!1!==t&&(this.pos+=n[0].length),n)}var i=function(e){return r?e.toLowerCase():e}
if(i(this.string.substr(this.pos,e.length))==i(e))return!1!==t&&(this.pos+=e.length),!0},Ue.prototype.current=function(){return this.string.slice(this.start,this.pos)},Ue.prototype.hideFirstChars=function(e,t){this.lineStart+=e
try{return t()}finally{this.lineStart-=e}},Ue.prototype.lookAhead=function(e){var t=this.lineOracle
return t&&t.lookAhead(e)},Ue.prototype.baseToken=function(){var e=this.lineOracle
return e&&e.baseToken(this.pos)}
var ct=function(e,t){this.state=e,this.lookAhead=t},ut=function(e,t,r,n){this.state=t,this.doc=e,this.line=r,this.maxLookAhead=n||0,this.baseTokens=null,this.baseTokenPos=1}
function dt(e,t,r,n){var i=[e.state.modeGen],o={}
xt(e,t.text,e.doc.mode,r,(function(e,t){return i.push(e,t)}),o,n)
for(var a=r.state,l=function(n){r.baseTokens=i
var l=e.state.overlays[n],s=1,c=0
r.state=!0,xt(e,t.text,l.mode,r,(function(e,t){for(var r=s;c<e;){var n=i[s]
n>e&&i.splice(s,1,e,i[s+1],n),s+=2,c=Math.min(e,n)}if(t)if(l.opaque)i.splice(r,s-r,e,"overlay "+t),s=r+2
else for(;r<s;r+=2){var o=i[r+1]
i[r+1]=(o?o+" ":"")+"overlay "+t}}),o),r.state=a,r.baseTokens=null,r.baseTokenPos=1},s=0;s<e.state.overlays.length;++s)l(s)
return{styles:i,classes:o.bgClass||o.textClass?o:null}}function ft(e,t,r){if(!t.styles||t.styles[0]!=e.state.modeGen){var n=pt(e,Xe(t)),i=t.text.length>e.options.maxHighlightLength&&je(e.doc.mode,n.state),o=dt(e,t,n)
i&&(n.state=i),t.stateAfter=n.save(!i),t.styles=o.styles,o.classes?t.styleClasses=o.classes:t.styleClasses&&(t.styleClasses=null),r===e.doc.highlightFrontier&&(e.doc.modeFrontier=Math.max(e.doc.modeFrontier,++e.doc.highlightFrontier))}return t.styles}function pt(e,t,r){var n=e.doc,i=e.display
if(!n.mode.startState)return new ut(n,!0,t)
var o=function(e,t,r){for(var n,i,o=e.doc,a=r?-1:t-(e.doc.mode.innerMode?1e3:100),l=t;l>a;--l){if(l<=o.first)return o.first
var s=Ge(o,l-1),c=s.stateAfter
if(c&&(!r||l+(c instanceof ct?c.lookAhead:0)<=o.modeFrontier))return l
var u=P(s.text,null,e.options.tabSize);(null==i||n>u)&&(i=l-1,n=u)}return i}(e,t,r),a=o>n.first&&Ge(n,o-1).stateAfter,l=a?ut.fromSaved(n,a,o):new ut(n,Be(n.mode),o)
return n.iter(o,t,(function(r){ht(e,r.text,l)
var n=l.line
r.stateAfter=n==t-1||n%5==0||n>=i.viewFrom&&n<i.viewTo?l.save():null,l.nextLine()})),r&&(n.modeFrontier=l.line),l}function ht(e,t,r,n){var i=e.doc.mode,o=new Ue(t,e.options.tabSize,r)
for(o.start=o.pos=n||0,""==t&&mt(i,r.state);!o.eol();)gt(i,o,r.state),o.start=o.pos}function mt(e,t){if(e.blankLine)return e.blankLine(t)
if(e.innerMode){var r=He(e,t)
return r.mode.blankLine?r.mode.blankLine(r.state):void 0}}function gt(e,t,r,n){for(var i=0;i<10;i++){n&&(n[0]=He(e,r).mode)
var o=e.token(t,r)
if(t.pos>t.start)return o}throw new Error("Mode "+e.name+" failed to advance stream.")}ut.prototype.lookAhead=function(e){var t=this.doc.getLine(this.line+e)
return null!=t&&e>this.maxLookAhead&&(this.maxLookAhead=e),t},ut.prototype.baseToken=function(e){if(!this.baseTokens)return null
for(;this.baseTokens[this.baseTokenPos]<=e;)this.baseTokenPos+=2
var t=this.baseTokens[this.baseTokenPos+1]
return{type:t&&t.replace(/( |^)overlay .*/,""),size:this.baseTokens[this.baseTokenPos]-e}},ut.prototype.nextLine=function(){this.line++,this.maxLookAhead>0&&this.maxLookAhead--},ut.fromSaved=function(e,t,r){return t instanceof ct?new ut(e,je(e.mode,t.state),r,t.lookAhead):new ut(e,je(e.mode,t),r)},ut.prototype.save=function(e){var t=!1!==e?je(this.doc.mode,this.state):this.state
return this.maxLookAhead>0?new ct(t,this.maxLookAhead):t}
var vt=function(e,t,r){this.start=e.start,this.end=e.pos,this.string=e.current(),this.type=t||null,this.state=r}
function yt(e,t,r,n){var i,o,a=e.doc,l=a.mode,s=Ge(a,(t=lt(a,t)).line),c=pt(e,t.line,r),u=new Ue(s.text,e.options.tabSize,c)
for(n&&(o=[]);(n||u.pos<t.ch)&&!u.eol();)u.start=u.pos,i=gt(l,u,c.state),n&&o.push(new vt(u,i,je(a.mode,c.state)))
return n?o:new vt(u,i,c.state)}function bt(e,t){if(e)for(;;){var r=e.match(/(?:^|\s+)line-(background-)?(\S+)/)
if(!r)break
e=e.slice(0,r.index)+e.slice(r.index+r[0].length)
var n=r[1]?"bgClass":"textClass"
null==t[n]?t[n]=r[2]:new RegExp("(?:^|s)"+r[2]+"(?:$|s)").test(t[n])||(t[n]+=" "+r[2])}return e}function xt(e,t,r,n,i,o,a){var l=r.flattenSpans
null==l&&(l=e.options.flattenSpans)
var s,c=0,u=null,d=new Ue(t,e.options.tabSize,n),f=e.options.addModeClass&&[null]
for(""==t&&bt(mt(r,n.state),o);!d.eol();){if(d.pos>e.options.maxHighlightLength?(l=!1,a&&ht(e,t,n,d.pos),d.pos=t.length,s=null):s=bt(gt(r,d,n.state,f),o),f){var p=f[0].name
p&&(s="m-"+(s?p+" "+s:p))}if(!l||u!=s){for(;c<d.start;)i(c=Math.min(d.start,c+5e3),u)
u=s}d.start=d.pos}for(;c<d.pos;){var h=Math.min(d.pos,c+5e3)
i(h,u),c=h}}var wt=!1,kt=!1
function _t(e,t,r){this.marker=e,this.from=t,this.to=r}function Ct(e,t){if(e)for(var r=0;r<e.length;++r){var n=e[r]
if(n.marker==t)return n}}function St(e,t){for(var r,n=0;n<e.length;++n)e[n]!=t&&(r||(r=[])).push(e[n])
return r}function Tt(e,t){if(t.full)return null
var r=Qe(e,t.from.line)&&Ge(e,t.from.line).markedSpans,n=Qe(e,t.to.line)&&Ge(e,t.to.line).markedSpans
if(!r&&!n)return null
var i=t.from.ch,o=t.to.ch,a=0==tt(t.from,t.to),l=function(e,t,r){var n
if(e)for(var i=0;i<e.length;++i){var o=e[i],a=o.marker
if(null==o.from||(a.inclusiveLeft?o.from<=t:o.from<t)||o.from==t&&"bookmark"==a.type&&(!r||!o.marker.insertLeft)){var l=null==o.to||(a.inclusiveRight?o.to>=t:o.to>t);(n||(n=[])).push(new _t(a,o.from,l?null:o.to))}}return n}(r,i,a),s=function(e,t,r){var n
if(e)for(var i=0;i<e.length;++i){var o=e[i],a=o.marker
if(null==o.to||(a.inclusiveRight?o.to>=t:o.to>t)||o.from==t&&"bookmark"==a.type&&(!r||o.marker.insertLeft)){var l=null==o.from||(a.inclusiveLeft?o.from<=t:o.from<t);(n||(n=[])).push(new _t(a,l?null:o.from-t,null==o.to?null:o.to-t))}}return n}(n,o,a),c=1==t.text.length,u=K(t.text).length+(c?i:0)
if(l)for(var d=0;d<l.length;++d){var f=l[d]
if(null==f.to){var p=Ct(s,f.marker)
p?c&&(f.to=null==p.to?null:p.to+u):f.to=i}}if(s)for(var h=0;h<s.length;++h){var m=s[h]
if(null!=m.to&&(m.to+=u),null==m.from)Ct(l,m.marker)||(m.from=u,c&&(l||(l=[])).push(m))
else m.from+=u,c&&(l||(l=[])).push(m)}l&&(l=Mt(l)),s&&s!=l&&(s=Mt(s))
var g=[l]
if(!c){var v,y=t.text.length-2
if(y>0&&l)for(var b=0;b<l.length;++b)null==l[b].to&&(v||(v=[])).push(new _t(l[b].marker,null,null))
for(var x=0;x<y;++x)g.push(v)
g.push(s)}return g}function Mt(e){for(var t=0;t<e.length;++t){var r=e[t]
null!=r.from&&r.from==r.to&&!1!==r.marker.clearWhenEmpty&&e.splice(t--,1)}return e.length?e:null}function Lt(e){var t=e.markedSpans
if(t){for(var r=0;r<t.length;++r)t[r].marker.detachLine(e)
e.markedSpans=null}}function zt(e,t){if(t){for(var r=0;r<t.length;++r)t[r].marker.attachLine(e)
e.markedSpans=t}}function At(e){return e.inclusiveLeft?-1:0}function Et(e){return e.inclusiveRight?1:0}function Nt(e,t){var r=e.lines.length-t.lines.length
if(0!=r)return r
var n=e.find(),i=t.find(),o=tt(n.from,i.from)||At(e)-At(t)
if(o)return-o
var a=tt(n.to,i.to)||Et(e)-Et(t)
return a||t.id-e.id}function qt(e,t){var r,n=kt&&e.markedSpans
if(n)for(var i=void 0,o=0;o<n.length;++o)(i=n[o]).marker.collapsed&&null==(t?i.from:i.to)&&(!r||Nt(r,i.marker)<0)&&(r=i.marker)
return r}function Ot(e){return qt(e,!0)}function It(e){return qt(e,!1)}function Dt(e,t){var r,n=kt&&e.markedSpans
if(n)for(var i=0;i<n.length;++i){var o=n[i]
o.marker.collapsed&&(null==o.from||o.from<t)&&(null==o.to||o.to>t)&&(!r||Nt(r,o.marker)<0)&&(r=o.marker)}return r}function Ft(e,t,r,n,i){var o=Ge(e,t),a=kt&&o.markedSpans
if(a)for(var l=0;l<a.length;++l){var s=a[l]
if(s.marker.collapsed){var c=s.marker.find(0),u=tt(c.from,r)||At(s.marker)-At(i),d=tt(c.to,n)||Et(s.marker)-Et(i)
if(!(u>=0&&d<=0||u<=0&&d>=0)&&(u<=0&&(s.marker.inclusiveRight&&i.inclusiveLeft?tt(c.to,r)>=0:tt(c.to,r)>0)||u>=0&&(s.marker.inclusiveRight&&i.inclusiveLeft?tt(c.from,n)<=0:tt(c.from,n)<0)))return!0}}}function Pt(e){for(var t;t=Ot(e);)e=t.find(-1,!0).line
return e}function Wt(e,t){var r=Ge(e,t),n=Pt(r)
return r==n?t:Xe(n)}function Rt(e,t){if(t>e.lastLine())return t
var r,n=Ge(e,t)
if(!$t(e,n))return t
for(;r=It(n);)n=r.find(1,!0).line
return Xe(n)+1}function $t(e,t){var r=kt&&t.markedSpans
if(r)for(var n=void 0,i=0;i<r.length;++i)if((n=r[i]).marker.collapsed){if(null==n.from)return!0
if(!n.marker.widgetNode&&0==n.from&&n.marker.inclusiveLeft&&jt(e,t,n))return!0}}function jt(e,t,r){if(null==r.to){var n=r.marker.find(1,!0)
return jt(e,n.line,Ct(n.line.markedSpans,r.marker))}if(r.marker.inclusiveRight&&r.to==t.text.length)return!0
for(var i=void 0,o=0;o<t.markedSpans.length;++o)if((i=t.markedSpans[o]).marker.collapsed&&!i.marker.widgetNode&&i.from==r.to&&(null==i.to||i.to!=r.from)&&(i.marker.inclusiveLeft||r.marker.inclusiveRight)&&jt(e,t,i))return!0}function Ht(e){for(var t=0,r=(e=Pt(e)).parent,n=0;n<r.lines.length;++n){var i=r.lines[n]
if(i==e)break
t+=i.height}for(var o=r.parent;o;o=(r=o).parent)for(var a=0;a<o.children.length;++a){var l=o.children[a]
if(l==r)break
t+=l.height}return t}function Bt(e){if(0==e.height)return 0
for(var t,r=e.text.length,n=e;t=Ot(n);){var i=t.find(0,!0)
n=i.from.line,r+=i.from.ch-i.to.ch}for(n=e;t=It(n);){var o=t.find(0,!0)
r-=n.text.length-o.from.ch,r+=(n=o.to.line).text.length-o.to.ch}return r}function Ut(e){var t=e.display,r=e.doc
t.maxLine=Ge(r,r.first),t.maxLineLength=Bt(t.maxLine),t.maxLineChanged=!0,r.iter((function(e){var r=Bt(e)
r>t.maxLineLength&&(t.maxLineLength=r,t.maxLine=e)}))}var Gt=function(e,t,r){this.text=e,zt(this,t),this.height=r?r(this):1}
function Vt(e){e.parent=null,Lt(e)}Gt.prototype.lineNo=function(){return Xe(this)},ye(Gt)
var Kt={},Zt={}
function Xt(e,t){if(!e||/^\s*$/.test(e))return null
var r=t.addModeClass?Zt:Kt
return r[e]||(r[e]=e.replace(/\S+/g,"cm-$&"))}function Yt(e,t){var r=A("span",null,null,s?"padding-right: .1px":null),n={pre:A("pre",[r],"CodeMirror-line"),content:r,col:0,pos:0,cm:e,trailingSpace:!1,splitSpaces:e.getOption("lineWrapping")}
t.measure={}
for(var i=0;i<=(t.rest?t.rest.length:0);i++){var o=i?t.rest[i-1]:t.line,a=void 0
n.pos=0,n.addToken=Jt,ze(e.display.measure)&&(a=ce(o,e.doc.direction))&&(n.addToken=er(n.addToken,a)),n.map=[],rr(o,n,ft(e,o,t!=e.display.externalMeasured&&Xe(o))),o.styleClasses&&(o.styleClasses.bgClass&&(n.bgClass=O(o.styleClasses.bgClass,n.bgClass||"")),o.styleClasses.textClass&&(n.textClass=O(o.styleClasses.textClass,n.textClass||""))),0==n.map.length&&n.map.push(0,0,n.content.appendChild(Le(e.display.measure))),0==i?(t.measure.map=n.map,t.measure.cache={}):((t.measure.maps||(t.measure.maps=[])).push(n.map),(t.measure.caches||(t.measure.caches=[])).push({}))}if(s){var l=n.content.lastChild;(/\bcm-tab\b/.test(l.className)||l.querySelector&&l.querySelector(".cm-tab"))&&(n.content.className="cm-tab-wrap-hack")}return he(e,"renderLine",e,t.line,n.pre),n.pre.className&&(n.textClass=O(n.pre.className,n.textClass||"")),n}function Qt(e){var t=z("span","•","cm-invalidchar")
return t.title="\\u"+e.charCodeAt(0).toString(16),t.setAttribute("aria-label",t.title),t}function Jt(e,t,r,n,i,o,s){if(t){var c,u=e.splitSpaces?function(e,t){if(e.length>1&&!/  /.test(e))return e
for(var r=t,n="",i=0;i<e.length;i++){var o=e.charAt(i)
" "!=o||!r||i!=e.length-1&&32!=e.charCodeAt(i+1)||(o=" "),n+=o,r=" "==o}return n}(t,e.trailingSpace):t,d=e.cm.state.specialChars,f=!1
if(d.test(t)){c=document.createDocumentFragment()
for(var p=0;;){d.lastIndex=p
var h=d.exec(t),m=h?h.index-p:t.length-p
if(m){var g=document.createTextNode(u.slice(p,p+m))
a&&l<9?c.appendChild(z("span",[g])):c.appendChild(g),e.map.push(e.pos,e.pos+m,g),e.col+=m,e.pos+=m}if(!h)break
p+=m+1
var v=void 0
if("\t"==h[0]){var y=e.cm.options.tabSize,b=y-e.col%y;(v=c.appendChild(z("span",V(b),"cm-tab"))).setAttribute("role","presentation"),v.setAttribute("cm-text","\t"),e.col+=b}else"\r"==h[0]||"\n"==h[0]?((v=c.appendChild(z("span","\r"==h[0]?"␍":"␤","cm-invalidchar"))).setAttribute("cm-text",h[0]),e.col+=1):((v=e.cm.options.specialCharPlaceholder(h[0])).setAttribute("cm-text",h[0]),a&&l<9?c.appendChild(z("span",[v])):c.appendChild(v),e.col+=1)
e.map.push(e.pos,e.pos+1,v),e.pos++}}else e.col+=t.length,c=document.createTextNode(u),e.map.push(e.pos,e.pos+t.length,c),a&&l<9&&(f=!0),e.pos+=t.length
if(e.trailingSpace=32==u.charCodeAt(t.length-1),r||n||i||f||o){var x=r||""
n&&(x+=n),i&&(x+=i)
var w=z("span",[c],x,o)
if(s)for(var k in s)s.hasOwnProperty(k)&&"style"!=k&&"class"!=k&&w.setAttribute(k,s[k])
return e.content.appendChild(w)}e.content.appendChild(c)}}function er(e,t){return function(r,n,i,o,a,l,s){i=i?i+" cm-force-border":"cm-force-border"
for(var c=r.pos,u=c+n.length;;){for(var d=void 0,f=0;f<t.length&&!((d=t[f]).to>c&&d.from<=c);f++);if(d.to>=u)return e(r,n,i,o,a,l,s)
e(r,n.slice(0,d.to-c),i,o,null,l,s),o=null,n=n.slice(d.to-c),c=d.to}}}function tr(e,t,r,n){var i=!n&&r.widgetNode
i&&e.map.push(e.pos,e.pos+t,i),!n&&e.cm.display.input.needsContentAttribute&&(i||(i=e.content.appendChild(document.createElement("span"))),i.setAttribute("cm-marker",r.id)),i&&(e.cm.display.input.setUneditable(i),e.content.appendChild(i)),e.pos+=t,e.trailingSpace=!1}function rr(e,t,r){var n=e.markedSpans,i=e.text,o=0
if(n)for(var a,l,s,c,u,d,f,p=i.length,h=0,m=1,g="",v=0;;){if(v==h){s=c=u=l="",f=null,d=null,v=1/0
for(var y=[],b=void 0,x=0;x<n.length;++x){var w=n[x],k=w.marker
if("bookmark"==k.type&&w.from==h&&k.widgetNode)y.push(k)
else if(w.from<=h&&(null==w.to||w.to>h||k.collapsed&&w.to==h&&w.from==h)){if(null!=w.to&&w.to!=h&&v>w.to&&(v=w.to,c=""),k.className&&(s+=" "+k.className),k.css&&(l=(l?l+";":"")+k.css),k.startStyle&&w.from==h&&(u+=" "+k.startStyle),k.endStyle&&w.to==v&&(b||(b=[])).push(k.endStyle,w.to),k.title&&((f||(f={})).title=k.title),k.attributes)for(var _ in k.attributes)(f||(f={}))[_]=k.attributes[_]
k.collapsed&&(!d||Nt(d.marker,k)<0)&&(d=w)}else w.from>h&&v>w.from&&(v=w.from)}if(b)for(var C=0;C<b.length;C+=2)b[C+1]==v&&(c+=" "+b[C])
if(!d||d.from==h)for(var S=0;S<y.length;++S)tr(t,0,y[S])
if(d&&(d.from||0)==h){if(tr(t,(null==d.to?p+1:d.to)-h,d.marker,null==d.from),null==d.to)return
d.to==h&&(d=!1)}}if(h>=p)break
for(var T=Math.min(p,v);;){if(g){var M=h+g.length
if(!d){var L=M>T?g.slice(0,T-h):g
t.addToken(t,L,a?a+s:s,u,h+L.length==v?c:"",l,f)}if(M>=T){g=g.slice(T-h),h=T
break}h=M,u=""}g=i.slice(o,o=r[m++]),a=Xt(r[m++],t.cm.options)}}else for(var z=1;z<r.length;z+=2)t.addToken(t,i.slice(o,o=r[z]),Xt(r[z+1],t.cm.options))}function nr(e,t,r){this.line=t,this.rest=function(e){for(var t,r;t=It(e);)e=t.find(1,!0).line,(r||(r=[])).push(e)
return r}(t),this.size=this.rest?Xe(K(this.rest))-r+1:1,this.node=this.text=null,this.hidden=$t(e,t)}function ir(e,t,r){for(var n,i=[],o=t;o<r;o=n){var a=new nr(e.doc,Ge(e.doc,o),o)
n=o+a.size,i.push(a)}return i}var or=null
var ar=null
function lr(e,t){var r=fe(e,t)
if(r.length){var n,i=Array.prototype.slice.call(arguments,2)
or?n=or.delayedCallbacks:ar?n=ar:(n=ar=[],setTimeout(sr,0))
for(var o=function(e){n.push((function(){return r[e].apply(null,i)}))},a=0;a<r.length;++a)o(a)}}function sr(){var e=ar
ar=null
for(var t=0;t<e.length;++t)e[t]()}function cr(e,t,r,n){for(var i=0;i<t.changes.length;i++){var o=t.changes[i]
"text"==o?fr(e,t):"gutter"==o?hr(e,t,r,n):"class"==o?pr(e,t):"widget"==o&&mr(e,t,n)}t.changes=null}function ur(e){return e.node==e.text&&(e.node=z("div",null,null,"position: relative"),e.text.parentNode&&e.text.parentNode.replaceChild(e.node,e.text),e.node.appendChild(e.text),a&&l<8&&(e.node.style.zIndex=2)),e.node}function dr(e,t){var r=e.display.externalMeasured
return r&&r.line==t.line?(e.display.externalMeasured=null,t.measure=r.measure,r.built):Yt(e,t)}function fr(e,t){var r=t.text.className,n=dr(e,t)
t.text==t.node&&(t.node=n.pre),t.text.parentNode.replaceChild(n.pre,t.text),t.text=n.pre,n.bgClass!=t.bgClass||n.textClass!=t.textClass?(t.bgClass=n.bgClass,t.textClass=n.textClass,pr(e,t)):r&&(t.text.className=r)}function pr(e,t){(function(e,t){var r=t.bgClass?t.bgClass+" "+(t.line.bgClass||""):t.line.bgClass
if(r&&(r+=" CodeMirror-linebackground"),t.background)r?t.background.className=r:(t.background.parentNode.removeChild(t.background),t.background=null)
else if(r){var n=ur(t)
t.background=n.insertBefore(z("div",null,r),n.firstChild),e.display.input.setUneditable(t.background)}})(e,t),t.line.wrapClass?ur(t).className=t.line.wrapClass:t.node!=t.text&&(t.node.className="")
var r=t.textClass?t.textClass+" "+(t.line.textClass||""):t.line.textClass
t.text.className=r||""}function hr(e,t,r,n){if(t.gutter&&(t.node.removeChild(t.gutter),t.gutter=null),t.gutterBackground&&(t.node.removeChild(t.gutterBackground),t.gutterBackground=null),t.line.gutterClass){var i=ur(t)
t.gutterBackground=z("div",null,"CodeMirror-gutter-background "+t.line.gutterClass,"left: "+(e.options.fixedGutter?n.fixedPos:-n.gutterTotalWidth)+"px; width: "+n.gutterTotalWidth+"px"),e.display.input.setUneditable(t.gutterBackground),i.insertBefore(t.gutterBackground,t.text)}var o=t.line.gutterMarkers
if(e.options.lineNumbers||o){var a=ur(t),l=t.gutter=z("div",null,"CodeMirror-gutter-wrapper","left: "+(e.options.fixedGutter?n.fixedPos:-n.gutterTotalWidth)+"px")
if(e.display.input.setUneditable(l),a.insertBefore(l,t.text),t.line.gutterClass&&(l.className+=" "+t.line.gutterClass),!e.options.lineNumbers||o&&o["CodeMirror-linenumbers"]||(t.lineNumber=l.appendChild(z("div",Je(e.options,r),"CodeMirror-linenumber CodeMirror-gutter-elt","left: "+n.gutterLeft["CodeMirror-linenumbers"]+"px; width: "+e.display.lineNumInnerWidth+"px"))),o)for(var s=0;s<e.display.gutterSpecs.length;++s){var c=e.display.gutterSpecs[s].className,u=o.hasOwnProperty(c)&&o[c]
u&&l.appendChild(z("div",[u],"CodeMirror-gutter-elt","left: "+n.gutterLeft[c]+"px; width: "+n.gutterWidth[c]+"px"))}}}function mr(e,t,r){t.alignable&&(t.alignable=null)
for(var n=C("CodeMirror-linewidget"),i=t.node.firstChild,o=void 0;i;i=o)o=i.nextSibling,n.test(i.className)&&t.node.removeChild(i)
vr(e,t,r)}function gr(e,t,r,n){var i=dr(e,t)
return t.text=t.node=i.pre,i.bgClass&&(t.bgClass=i.bgClass),i.textClass&&(t.textClass=i.textClass),pr(e,t),hr(e,t,r,n),vr(e,t,n),t.node}function vr(e,t,r){if(yr(e,t.line,t,r,!0),t.rest)for(var n=0;n<t.rest.length;n++)yr(e,t.rest[n],t,r,!1)}function yr(e,t,r,n,i){if(t.widgets)for(var o=ur(r),a=0,l=t.widgets;a<l.length;++a){var s=l[a],c=z("div",[s.node],"CodeMirror-linewidget"+(s.className?" "+s.className:""))
s.handleMouseEvents||c.setAttribute("cm-ignore-events","true"),br(s,c,r,n),e.display.input.setUneditable(c),i&&s.above?o.insertBefore(c,r.gutter||r.text):o.appendChild(c),lr(s,"redraw")}}function br(e,t,r,n){if(e.noHScroll){(r.alignable||(r.alignable=[])).push(t)
var i=n.wrapperWidth
t.style.left=n.fixedPos+"px",e.coverGutter||(i-=n.gutterTotalWidth,t.style.paddingLeft=n.gutterTotalWidth+"px"),t.style.width=i+"px"}e.coverGutter&&(t.style.zIndex=5,t.style.position="relative",e.noHScroll||(t.style.marginLeft=-n.gutterTotalWidth+"px"))}function xr(e){if(null!=e.height)return e.height
var t=e.doc.cm
if(!t)return 0
if(!E(document.body,e.node)){var r="position: relative;"
e.coverGutter&&(r+="margin-left: -"+t.display.gutters.offsetWidth+"px;"),e.noHScroll&&(r+="width: "+t.display.wrapper.clientWidth+"px;"),L(t.display.measure,z("div",[e.node],null,r))}return e.height=e.node.parentNode.offsetHeight}function wr(e,t){for(var r=_e(t);r!=e.wrapper;r=r.parentNode)if(!r||1==r.nodeType&&"true"==r.getAttribute("cm-ignore-events")||r.parentNode==e.sizer&&r!=e.mover)return!0}function kr(e){return e.lineSpace.offsetTop}function _r(e){return e.mover.offsetHeight-e.lineSpace.offsetHeight}function Cr(e){if(e.cachedPaddingH)return e.cachedPaddingH
var t=L(e.measure,z("pre","x","CodeMirror-line-like")),r=window.getComputedStyle?window.getComputedStyle(t):t.currentStyle,n={left:parseInt(r.paddingLeft),right:parseInt(r.paddingRight)}
return isNaN(n.left)||isNaN(n.right)||(e.cachedPaddingH=n),n}function Sr(e){return 30-e.display.nativeBarWidth}function Tr(e){return e.display.scroller.clientWidth-Sr(e)-e.display.barWidth}function Mr(e){return e.display.scroller.clientHeight-Sr(e)-e.display.barHeight}function Lr(e,t,r){if(e.line==t)return{map:e.measure.map,cache:e.measure.cache}
for(var n=0;n<e.rest.length;n++)if(e.rest[n]==t)return{map:e.measure.maps[n],cache:e.measure.caches[n]}
for(var i=0;i<e.rest.length;i++)if(Xe(e.rest[i])>r)return{map:e.measure.maps[i],cache:e.measure.caches[i],before:!0}}function zr(e,t,r,n){return Nr(e,Er(e,t),r,n)}function Ar(e,t){if(t>=e.display.viewFrom&&t<e.display.viewTo)return e.display.view[un(e,t)]
var r=e.display.externalMeasured
return r&&t>=r.lineN&&t<r.lineN+r.size?r:void 0}function Er(e,t){var r=Xe(t),n=Ar(e,r)
n&&!n.text?n=null:n&&n.changes&&(cr(e,n,r,on(e)),e.curOp.forceUpdate=!0),n||(n=function(e,t){var r=Xe(t=Pt(t)),n=e.display.externalMeasured=new nr(e.doc,t,r)
n.lineN=r
var i=n.built=Yt(e,n)
return n.text=i.pre,L(e.display.lineMeasure,i.pre),n}(e,t))
var i=Lr(n,t,r)
return{line:t,view:n,rect:null,map:i.map,cache:i.cache,before:i.before,hasHeights:!1}}function Nr(e,t,r,n,i){t.before&&(r=-1)
var o,s=r+(n||"")
return t.cache.hasOwnProperty(s)?o=t.cache[s]:(t.rect||(t.rect=t.view.text.getBoundingClientRect()),t.hasHeights||(function(e,t,r){var n=e.options.lineWrapping,i=n&&Tr(e)
if(!t.measure.heights||n&&t.measure.width!=i){var o=t.measure.heights=[]
if(n){t.measure.width=i
for(var a=t.text.firstChild.getClientRects(),l=0;l<a.length-1;l++){var s=a[l],c=a[l+1]
Math.abs(s.bottom-c.bottom)>2&&o.push((s.bottom+c.top)/2-r.top)}}o.push(r.bottom-r.top)}}(e,t.view,t.rect),t.hasHeights=!0),(o=function(e,t,r,n){var i,o=Ir(t.map,r,n),s=o.node,c=o.start,u=o.end,d=o.collapse
if(3==s.nodeType){for(var f=0;f<4;f++){for(;c&&ne(t.line.text.charAt(o.coverStart+c));)--c
for(;o.coverStart+u<o.coverEnd&&ne(t.line.text.charAt(o.coverStart+u));)++u
if((i=a&&l<9&&0==c&&u==o.coverEnd-o.coverStart?s.parentNode.getBoundingClientRect():Dr(S(s,c,u).getClientRects(),n)).left||i.right||0==c)break
u=c,c-=1,d="right"}a&&l<11&&(i=function(e,t){if(!window.screen||null==screen.logicalXDPI||screen.logicalXDPI==screen.deviceXDPI||!function(e){if(null!=Oe)return Oe
var t=L(e,z("span","x")),r=t.getBoundingClientRect(),n=S(t,0,1).getBoundingClientRect()
return Oe=Math.abs(r.left-n.left)>1}(e))return t
var r=screen.logicalXDPI/screen.deviceXDPI,n=screen.logicalYDPI/screen.deviceYDPI
return{left:t.left*r,right:t.right*r,top:t.top*n,bottom:t.bottom*n}}(e.display.measure,i))}else{var p
c>0&&(d=n="right"),i=e.options.lineWrapping&&(p=s.getClientRects()).length>1?p["right"==n?p.length-1:0]:s.getBoundingClientRect()}if(a&&l<9&&!c&&(!i||!i.left&&!i.right)){var h=s.parentNode.getClientRects()[0]
i=h?{left:h.left,right:h.left+nn(e.display),top:h.top,bottom:h.bottom}:Or}for(var m=i.top-t.rect.top,g=i.bottom-t.rect.top,v=(m+g)/2,y=t.view.measure.heights,b=0;b<y.length-1&&!(v<y[b]);b++);var x=b?y[b-1]:0,w=y[b],k={left:("right"==d?i.right:i.left)-t.rect.left,right:("left"==d?i.left:i.right)-t.rect.left,top:x,bottom:w}
i.left||i.right||(k.bogus=!0)
e.options.singleCursorHeightPerLine||(k.rtop=m,k.rbottom=g)
return k}(e,t,r,n)).bogus||(t.cache[s]=o)),{left:o.left,right:o.right,top:i?o.rtop:o.top,bottom:i?o.rbottom:o.bottom}}var qr,Or={left:0,right:0,top:0,bottom:0}
function Ir(e,t,r){for(var n,i,o,a,l,s,c=0;c<e.length;c+=3)if(l=e[c],s=e[c+1],t<l?(i=0,o=1,a="left"):t<s?o=(i=t-l)+1:(c==e.length-3||t==s&&e[c+3]>t)&&(i=(o=s-l)-1,t>=s&&(a="right")),null!=i){if(n=e[c+2],l==s&&r==(n.insertLeft?"left":"right")&&(a=r),"left"==r&&0==i)for(;c&&e[c-2]==e[c-3]&&e[c-1].insertLeft;)n=e[2+(c-=3)],a="left"
if("right"==r&&i==s-l)for(;c<e.length-3&&e[c+3]==e[c+4]&&!e[c+5].insertLeft;)n=e[(c+=3)+2],a="right"
break}return{node:n,start:i,end:o,collapse:a,coverStart:l,coverEnd:s}}function Dr(e,t){var r=Or
if("left"==t)for(var n=0;n<e.length&&(r=e[n]).left==r.right;n++);else for(var i=e.length-1;i>=0&&(r=e[i]).left==r.right;i--);return r}function Fr(e){if(e.measure&&(e.measure.cache={},e.measure.heights=null,e.rest))for(var t=0;t<e.rest.length;t++)e.measure.caches[t]={}}function Pr(e){e.display.externalMeasure=null,M(e.display.lineMeasure)
for(var t=0;t<e.display.view.length;t++)Fr(e.display.view[t])}function Wr(e){Pr(e),e.display.cachedCharWidth=e.display.cachedTextHeight=e.display.cachedPaddingH=null,e.options.lineWrapping||(e.display.maxLineChanged=!0),e.display.lineNumChars=null}function Rr(){return u&&g?-(document.body.getBoundingClientRect().left-parseInt(getComputedStyle(document.body).marginLeft)):window.pageXOffset||(document.documentElement||document.body).scrollLeft}function $r(){return u&&g?-(document.body.getBoundingClientRect().top-parseInt(getComputedStyle(document.body).marginTop)):window.pageYOffset||(document.documentElement||document.body).scrollTop}function jr(e){var t=0
if(e.widgets)for(var r=0;r<e.widgets.length;++r)e.widgets[r].above&&(t+=xr(e.widgets[r]))
return t}function Hr(e,t,r,n,i){if(!i){var o=jr(t)
r.top+=o,r.bottom+=o}if("line"==n)return r
n||(n="local")
var a=Ht(t)
if("local"==n?a+=kr(e.display):a-=e.display.viewOffset,"page"==n||"window"==n){var l=e.display.lineSpace.getBoundingClientRect()
a+=l.top+("window"==n?0:$r())
var s=l.left+("window"==n?0:Rr())
r.left+=s,r.right+=s}return r.top+=a,r.bottom+=a,r}function Br(e,t,r){if("div"==r)return t
var n=t.left,i=t.top
if("page"==r)n-=Rr(),i-=$r()
else if("local"==r||!r){var o=e.display.sizer.getBoundingClientRect()
n+=o.left,i+=o.top}var a=e.display.lineSpace.getBoundingClientRect()
return{left:n-a.left,top:i-a.top}}function Ur(e,t,r,n,i){return n||(n=Ge(e.doc,t.line)),Hr(e,n,zr(e,n,t.ch,i),r)}function Gr(e,t,r,n,i,o){function a(t,a){var l=Nr(e,i,t,a?"right":"left",o)
return a?l.left=l.right:l.right=l.left,Hr(e,n,l,r)}n=n||Ge(e.doc,t.line),i||(i=Er(e,n))
var l=ce(n,e.doc.direction),s=t.ch,c=t.sticky
if(s>=n.text.length?(s=n.text.length,c="before"):s<=0&&(s=0,c="after"),!l)return a("before"==c?s-1:s,"before"==c)
function u(e,t,r){return a(r?e-1:e,1==l[t].level!=r)}var d=le(l,s,c),f=ae,p=u(s,d,"before"==c)
return null!=f&&(p.other=u(s,f,"before"!=c)),p}function Vr(e,t){var r=0
t=lt(e.doc,t),e.options.lineWrapping||(r=nn(e.display)*t.ch)
var n=Ge(e.doc,t.line),i=Ht(n)+kr(e.display)
return{left:r,right:r,top:i,bottom:i+n.height}}function Kr(e,t,r,n,i){var o=et(e,t,r)
return o.xRel=i,n&&(o.outside=n),o}function Zr(e,t,r){var n=e.doc
if((r+=e.display.viewOffset)<0)return Kr(n.first,0,null,-1,-1)
var i=Ye(n,r),o=n.first+n.size-1
if(i>o)return Kr(n.first+n.size-1,Ge(n,o).text.length,null,1,1)
t<0&&(t=0)
for(var a=Ge(n,i);;){var l=Jr(e,a,i,t,r),s=Dt(a,l.ch+(l.xRel>0||l.outside>0?1:0))
if(!s)return l
var c=s.find(1)
if(c.line==i)return c
a=Ge(n,i=c.line)}}function Xr(e,t,r,n){n-=jr(t)
var i=t.text.length,o=oe((function(t){return Nr(e,r,t-1).bottom<=n}),i,0)
return{begin:o,end:i=oe((function(t){return Nr(e,r,t).top>n}),o,i)}}function Yr(e,t,r,n){return r||(r=Er(e,t)),Xr(e,t,r,Hr(e,t,Nr(e,r,n),"line").top)}function Qr(e,t,r,n){return!(e.bottom<=r)&&(e.top>r||(n?e.left:e.right)>t)}function Jr(e,t,r,n,i){i-=Ht(t)
var o=Er(e,t),a=jr(t),l=0,s=t.text.length,c=!0,u=ce(t,e.doc.direction)
if(u){var d=(e.options.lineWrapping?tn:en)(e,t,r,o,u,n,i)
l=(c=1!=d.level)?d.from:d.to-1,s=c?d.to:d.from-1}var f,p,h=null,m=null,g=oe((function(t){var r=Nr(e,o,t)
return r.top+=a,r.bottom+=a,!!Qr(r,n,i,!1)&&(r.top<=i&&r.left<=n&&(h=t,m=r),!0)}),l,s),v=!1
if(m){var y=n-m.left<m.right-n,b=y==c
g=h+(b?0:1),p=b?"after":"before",f=y?m.left:m.right}else{c||g!=s&&g!=l||g++,p=0==g?"after":g==t.text.length?"before":Nr(e,o,g-(c?1:0)).bottom+a<=i==c?"after":"before"
var x=Gr(e,et(r,g,p),"line",t,o)
f=x.left,v=i<x.top?-1:i>=x.bottom?1:0}return Kr(r,g=ie(t.text,g,1),p,v,n-f)}function en(e,t,r,n,i,o,a){var l=oe((function(l){var s=i[l],c=1!=s.level
return Qr(Gr(e,et(r,c?s.to:s.from,c?"before":"after"),"line",t,n),o,a,!0)}),0,i.length-1),s=i[l]
if(l>0){var c=1!=s.level,u=Gr(e,et(r,c?s.from:s.to,c?"after":"before"),"line",t,n)
Qr(u,o,a,!0)&&u.top>a&&(s=i[l-1])}return s}function tn(e,t,r,n,i,o,a){var l=Xr(e,t,n,a),s=l.begin,c=l.end;/\s/.test(t.text.charAt(c-1))&&c--
for(var u=null,d=null,f=0;f<i.length;f++){var p=i[f]
if(!(p.from>=c||p.to<=s)){var h=Nr(e,n,1!=p.level?Math.min(c,p.to)-1:Math.max(s,p.from)).right,m=h<o?o-h+1e9:h-o;(!u||d>m)&&(u=p,d=m)}}return u||(u=i[i.length-1]),u.from<s&&(u={from:s,to:u.to,level:u.level}),u.to>c&&(u={from:u.from,to:c,level:u.level}),u}function rn(e){if(null!=e.cachedTextHeight)return e.cachedTextHeight
if(null==qr){qr=z("pre",null,"CodeMirror-line-like")
for(var t=0;t<49;++t)qr.appendChild(document.createTextNode("x")),qr.appendChild(z("br"))
qr.appendChild(document.createTextNode("x"))}L(e.measure,qr)
var r=qr.offsetHeight/50
return r>3&&(e.cachedTextHeight=r),M(e.measure),r||1}function nn(e){if(null!=e.cachedCharWidth)return e.cachedCharWidth
var t=z("span","xxxxxxxxxx"),r=z("pre",[t],"CodeMirror-line-like")
L(e.measure,r)
var n=t.getBoundingClientRect(),i=(n.right-n.left)/10
return i>2&&(e.cachedCharWidth=i),i||10}function on(e){for(var t=e.display,r={},n={},i=t.gutters.clientLeft,o=t.gutters.firstChild,a=0;o;o=o.nextSibling,++a){var l=e.display.gutterSpecs[a].className
r[l]=o.offsetLeft+o.clientLeft+i,n[l]=o.clientWidth}return{fixedPos:an(t),gutterTotalWidth:t.gutters.offsetWidth,gutterLeft:r,gutterWidth:n,wrapperWidth:t.wrapper.clientWidth}}function an(e){return e.scroller.getBoundingClientRect().left-e.sizer.getBoundingClientRect().left}function ln(e){var t=rn(e.display),r=e.options.lineWrapping,n=r&&Math.max(5,e.display.scroller.clientWidth/nn(e.display)-3)
return function(i){if($t(e.doc,i))return 0
var o=0
if(i.widgets)for(var a=0;a<i.widgets.length;a++)i.widgets[a].height&&(o+=i.widgets[a].height)
return r?o+(Math.ceil(i.text.length/n)||1)*t:o+t}}function sn(e){var t=e.doc,r=ln(e)
t.iter((function(e){var t=r(e)
t!=e.height&&Ze(e,t)}))}function cn(e,t,r,n){var i=e.display
if(!r&&"true"==_e(t).getAttribute("cm-not-content"))return null
var o,a,l=i.lineSpace.getBoundingClientRect()
try{o=t.clientX-l.left,a=t.clientY-l.top}catch(t){return null}var s,c=Zr(e,o,a)
if(n&&c.xRel>0&&(s=Ge(e.doc,c.line).text).length==c.ch){var u=P(s,s.length,e.options.tabSize)-s.length
c=et(c.line,Math.max(0,Math.round((o-Cr(e.display).left)/nn(e.display))-u))}return c}function un(e,t){if(t>=e.display.viewTo)return null
if((t-=e.display.viewFrom)<0)return null
for(var r=e.display.view,n=0;n<r.length;n++)if((t-=r[n].size)<0)return n}function dn(e,t,r,n){null==t&&(t=e.doc.first),null==r&&(r=e.doc.first+e.doc.size),n||(n=0)
var i=e.display
if(n&&r<i.viewTo&&(null==i.updateLineNumbers||i.updateLineNumbers>t)&&(i.updateLineNumbers=t),e.curOp.viewChanged=!0,t>=i.viewTo)kt&&Wt(e.doc,t)<i.viewTo&&pn(e)
else if(r<=i.viewFrom)kt&&Rt(e.doc,r+n)>i.viewFrom?pn(e):(i.viewFrom+=n,i.viewTo+=n)
else if(t<=i.viewFrom&&r>=i.viewTo)pn(e)
else if(t<=i.viewFrom){var o=hn(e,r,r+n,1)
o?(i.view=i.view.slice(o.index),i.viewFrom=o.lineN,i.viewTo+=n):pn(e)}else if(r>=i.viewTo){var a=hn(e,t,t,-1)
a?(i.view=i.view.slice(0,a.index),i.viewTo=a.lineN):pn(e)}else{var l=hn(e,t,t,-1),s=hn(e,r,r+n,1)
l&&s?(i.view=i.view.slice(0,l.index).concat(ir(e,l.lineN,s.lineN)).concat(i.view.slice(s.index)),i.viewTo+=n):pn(e)}var c=i.externalMeasured
c&&(r<c.lineN?c.lineN+=n:t<c.lineN+c.size&&(i.externalMeasured=null))}function fn(e,t,r){e.curOp.viewChanged=!0
var n=e.display,i=e.display.externalMeasured
if(i&&t>=i.lineN&&t<i.lineN+i.size&&(n.externalMeasured=null),!(t<n.viewFrom||t>=n.viewTo)){var o=n.view[un(e,t)]
if(null!=o.node){var a=o.changes||(o.changes=[]);-1==R(a,r)&&a.push(r)}}}function pn(e){e.display.viewFrom=e.display.viewTo=e.doc.first,e.display.view=[],e.display.viewOffset=0}function hn(e,t,r,n){var i,o=un(e,t),a=e.display.view
if(!kt||r==e.doc.first+e.doc.size)return{index:o,lineN:r}
for(var l=e.display.viewFrom,s=0;s<o;s++)l+=a[s].size
if(l!=t){if(n>0){if(o==a.length-1)return null
i=l+a[o].size-t,o++}else i=l-t
t+=i,r+=i}for(;Wt(e.doc,r)!=r;){if(o==(n<0?0:a.length-1))return null
r+=n*a[o-(n<0?1:0)].size,o+=n}return{index:o,lineN:r}}function mn(e){for(var t=e.display.view,r=0,n=0;n<t.length;n++){var i=t[n]
i.hidden||i.node&&!i.changes||++r}return r}function gn(e){e.display.input.showSelection(e.display.input.prepareSelection())}function vn(e,t){void 0===t&&(t=!0)
for(var r=e.doc,n={},i=n.cursors=document.createDocumentFragment(),o=n.selection=document.createDocumentFragment(),a=0;a<r.sel.ranges.length;a++)if(t||a!=r.sel.primIndex){var l=r.sel.ranges[a]
if(!(l.from().line>=e.display.viewTo||l.to().line<e.display.viewFrom)){var s=l.empty();(s||e.options.showCursorWhenSelecting)&&yn(e,l.head,i),s||xn(e,l,o)}}return n}function yn(e,t,r){var n=Gr(e,t,"div",null,null,!e.options.singleCursorHeightPerLine),i=r.appendChild(z("div"," ","CodeMirror-cursor"))
if(i.style.left=n.left+"px",i.style.top=n.top+"px",i.style.height=Math.max(0,n.bottom-n.top)*e.options.cursorHeight+"px",n.other){var o=r.appendChild(z("div"," ","CodeMirror-cursor CodeMirror-secondarycursor"))
o.style.display="",o.style.left=n.other.left+"px",o.style.top=n.other.top+"px",o.style.height=.85*(n.other.bottom-n.other.top)+"px"}}function bn(e,t){return e.top-t.top||e.left-t.left}function xn(e,t,r){var n=e.display,i=e.doc,o=document.createDocumentFragment(),a=Cr(e.display),l=a.left,s=Math.max(n.sizerWidth,Tr(e)-n.sizer.offsetLeft)-a.right,c="ltr"==i.direction
function u(e,t,r,n){t<0&&(t=0),t=Math.round(t),n=Math.round(n),o.appendChild(z("div",null,"CodeMirror-selected","position: absolute; left: "+e+"px;\n                             top: "+t+"px; width: "+(null==r?s-e:r)+"px;\n                             height: "+(n-t)+"px"))}function d(t,r,n){var o,a,d=Ge(i,t),f=d.text.length
function p(r,n){return Ur(e,et(t,r),"div",d,n)}function h(t,r,n){var i=Yr(e,d,null,t),o="ltr"==r==("after"==n)?"left":"right"
return p("after"==n?i.begin:i.end-(/\s/.test(d.text.charAt(i.end-1))?2:1),o)[o]}var m=ce(d,i.direction)
return function(e,t,r,n){if(!e)return n(t,r,"ltr",0)
for(var i=!1,o=0;o<e.length;++o){var a=e[o];(a.from<r&&a.to>t||t==r&&a.to==t)&&(n(Math.max(a.from,t),Math.min(a.to,r),1==a.level?"rtl":"ltr",o),i=!0)}i||n(t,r,"ltr")}(m,r||0,null==n?f:n,(function(e,t,i,d){var g="ltr"==i,v=p(e,g?"left":"right"),y=p(t-1,g?"right":"left"),b=null==r&&0==e,x=null==n&&t==f,w=0==d,k=!m||d==m.length-1
if(y.top-v.top<=3){var _=(c?x:b)&&k,C=(c?b:x)&&w?l:(g?v:y).left,S=_?s:(g?y:v).right
u(C,v.top,S-C,v.bottom)}else{var T,M,L,z
g?(T=c&&b&&w?l:v.left,M=c?s:h(e,i,"before"),L=c?l:h(t,i,"after"),z=c&&x&&k?s:y.right):(T=c?h(e,i,"before"):l,M=!c&&b&&w?s:v.right,L=!c&&x&&k?l:y.left,z=c?h(t,i,"after"):s),u(T,v.top,M-T,v.bottom),v.bottom<y.top&&u(l,v.bottom,null,y.top),u(L,y.top,z-L,y.bottom)}(!o||bn(v,o)<0)&&(o=v),bn(y,o)<0&&(o=y),(!a||bn(v,a)<0)&&(a=v),bn(y,a)<0&&(a=y)})),{start:o,end:a}}var f=t.from(),p=t.to()
if(f.line==p.line)d(f.line,f.ch,p.ch)
else{var h=Ge(i,f.line),m=Ge(i,p.line),g=Pt(h)==Pt(m),v=d(f.line,f.ch,g?h.text.length+1:null).end,y=d(p.line,g?0:null,p.ch).start
g&&(v.top<y.top-2?(u(v.right,v.top,null,v.bottom),u(l,y.top,y.left,y.bottom)):u(v.right,v.top,y.left-v.right,v.bottom)),v.bottom<y.top&&u(l,v.bottom,null,y.top)}r.appendChild(o)}function wn(e){if(e.state.focused){var t=e.display
clearInterval(t.blinker)
var r=!0
t.cursorDiv.style.visibility="",e.options.cursorBlinkRate>0?t.blinker=setInterval((function(){return t.cursorDiv.style.visibility=(r=!r)?"":"hidden"}),e.options.cursorBlinkRate):e.options.cursorBlinkRate<0&&(t.cursorDiv.style.visibility="hidden")}}function kn(e){e.state.focused||(e.display.input.focus(),Cn(e))}function _n(e){e.state.delayingBlurEvent=!0,setTimeout((function(){e.state.delayingBlurEvent&&(e.state.delayingBlurEvent=!1,Sn(e))}),100)}function Cn(e,t){e.state.delayingBlurEvent&&(e.state.delayingBlurEvent=!1),"nocursor"!=e.options.readOnly&&(e.state.focused||(he(e,"focus",e,t),e.state.focused=!0,q(e.display.wrapper,"CodeMirror-focused"),e.curOp||e.display.selForContextMenu==e.doc.sel||(e.display.input.reset(),s&&setTimeout((function(){return e.display.input.reset(!0)}),20)),e.display.input.receivedFocus()),wn(e))}function Sn(e,t){e.state.delayingBlurEvent||(e.state.focused&&(he(e,"blur",e,t),e.state.focused=!1,T(e.display.wrapper,"CodeMirror-focused")),clearInterval(e.display.blinker),setTimeout((function(){e.state.focused||(e.display.shift=!1)}),150))}function Tn(e){for(var t=e.display,r=t.lineDiv.offsetTop,n=0;n<t.view.length;n++){var i=t.view[n],o=e.options.lineWrapping,s=void 0,c=0
if(!i.hidden){if(a&&l<8){var u=i.node.offsetTop+i.node.offsetHeight
s=u-r,r=u}else{var d=i.node.getBoundingClientRect()
s=d.bottom-d.top,!o&&i.text.firstChild&&(c=i.text.firstChild.getBoundingClientRect().right-d.left-1)}var f=i.line.height-s
if((f>.005||f<-.005)&&(Ze(i.line,s),Mn(i.line),i.rest))for(var p=0;p<i.rest.length;p++)Mn(i.rest[p])
if(c>e.display.sizerWidth){var h=Math.ceil(c/nn(e.display))
h>e.display.maxLineLength&&(e.display.maxLineLength=h,e.display.maxLine=i.line,e.display.maxLineChanged=!0)}}}}function Mn(e){if(e.widgets)for(var t=0;t<e.widgets.length;++t){var r=e.widgets[t],n=r.node.parentNode
n&&(r.height=n.offsetHeight)}}function Ln(e,t,r){var n=r&&null!=r.top?Math.max(0,r.top):e.scroller.scrollTop
n=Math.floor(n-kr(e))
var i=r&&null!=r.bottom?r.bottom:n+e.wrapper.clientHeight,o=Ye(t,n),a=Ye(t,i)
if(r&&r.ensure){var l=r.ensure.from.line,s=r.ensure.to.line
l<o?(o=l,a=Ye(t,Ht(Ge(t,l))+e.wrapper.clientHeight)):Math.min(s,t.lastLine())>=a&&(o=Ye(t,Ht(Ge(t,s))-e.wrapper.clientHeight),a=s)}return{from:o,to:Math.max(a,o+1)}}function zn(e,t){var r=e.display,n=rn(e.display)
t.top<0&&(t.top=0)
var i=e.curOp&&null!=e.curOp.scrollTop?e.curOp.scrollTop:r.scroller.scrollTop,o=Mr(e),a={}
t.bottom-t.top>o&&(t.bottom=t.top+o)
var l=e.doc.height+_r(r),s=t.top<n,c=t.bottom>l-n
if(t.top<i)a.scrollTop=s?0:t.top
else if(t.bottom>i+o){var u=Math.min(t.top,(c?l:t.bottom)-o)
u!=i&&(a.scrollTop=u)}var d=e.curOp&&null!=e.curOp.scrollLeft?e.curOp.scrollLeft:r.scroller.scrollLeft,f=Tr(e)-(e.options.fixedGutter?r.gutters.offsetWidth:0),p=t.right-t.left>f
return p&&(t.right=t.left+f),t.left<10?a.scrollLeft=0:t.left<d?a.scrollLeft=Math.max(0,t.left-(p?0:10)):t.right>f+d-3&&(a.scrollLeft=t.right+(p?0:10)-f),a}function An(e,t){null!=t&&(qn(e),e.curOp.scrollTop=(null==e.curOp.scrollTop?e.doc.scrollTop:e.curOp.scrollTop)+t)}function En(e){qn(e)
var t=e.getCursor()
e.curOp.scrollToPos={from:t,to:t,margin:e.options.cursorScrollMargin}}function Nn(e,t,r){null==t&&null==r||qn(e),null!=t&&(e.curOp.scrollLeft=t),null!=r&&(e.curOp.scrollTop=r)}function qn(e){var t=e.curOp.scrollToPos
t&&(e.curOp.scrollToPos=null,On(e,Vr(e,t.from),Vr(e,t.to),t.margin))}function On(e,t,r,n){var i=zn(e,{left:Math.min(t.left,r.left),top:Math.min(t.top,r.top)-n,right:Math.max(t.right,r.right),bottom:Math.max(t.bottom,r.bottom)+n})
Nn(e,i.scrollLeft,i.scrollTop)}function In(e,t){Math.abs(e.doc.scrollTop-t)<2||(r||si(e,{top:t}),Dn(e,t,!0),r&&si(e),ni(e,100))}function Dn(e,t,r){t=Math.max(0,Math.min(e.display.scroller.scrollHeight-e.display.scroller.clientHeight,t)),(e.display.scroller.scrollTop!=t||r)&&(e.doc.scrollTop=t,e.display.scrollbars.setScrollTop(t),e.display.scroller.scrollTop!=t&&(e.display.scroller.scrollTop=t))}function Fn(e,t,r,n){t=Math.max(0,Math.min(t,e.display.scroller.scrollWidth-e.display.scroller.clientWidth)),(r?t==e.doc.scrollLeft:Math.abs(e.doc.scrollLeft-t)<2)&&!n||(e.doc.scrollLeft=t,di(e),e.display.scroller.scrollLeft!=t&&(e.display.scroller.scrollLeft=t),e.display.scrollbars.setScrollLeft(t))}function Pn(e){var t=e.display,r=t.gutters.offsetWidth,n=Math.round(e.doc.height+_r(e.display))
return{clientHeight:t.scroller.clientHeight,viewHeight:t.wrapper.clientHeight,scrollWidth:t.scroller.scrollWidth,clientWidth:t.scroller.clientWidth,viewWidth:t.wrapper.clientWidth,barLeft:e.options.fixedGutter?r:0,docHeight:n,scrollHeight:n+Sr(e)+t.barHeight,nativeBarWidth:t.nativeBarWidth,gutterWidth:r}}var Wn=function(e,t,r){this.cm=r
var n=this.vert=z("div",[z("div",null,null,"min-width: 1px")],"CodeMirror-vscrollbar"),i=this.horiz=z("div",[z("div",null,null,"height: 100%; min-height: 1px")],"CodeMirror-hscrollbar")
n.tabIndex=i.tabIndex=-1,e(n),e(i),de(n,"scroll",(function(){n.clientHeight&&t(n.scrollTop,"vertical")})),de(i,"scroll",(function(){i.clientWidth&&t(i.scrollLeft,"horizontal")})),this.checkedZeroWidth=!1,a&&l<8&&(this.horiz.style.minHeight=this.vert.style.minWidth="18px")}
Wn.prototype.update=function(e){var t=e.scrollWidth>e.clientWidth+1,r=e.scrollHeight>e.clientHeight+1,n=e.nativeBarWidth
if(r){this.vert.style.display="block",this.vert.style.bottom=t?n+"px":"0"
var i=e.viewHeight-(t?n:0)
this.vert.firstChild.style.height=Math.max(0,e.scrollHeight-e.clientHeight+i)+"px"}else this.vert.style.display="",this.vert.firstChild.style.height="0"
if(t){this.horiz.style.display="block",this.horiz.style.right=r?n+"px":"0",this.horiz.style.left=e.barLeft+"px"
var o=e.viewWidth-e.barLeft-(r?n:0)
this.horiz.firstChild.style.width=Math.max(0,e.scrollWidth-e.clientWidth+o)+"px"}else this.horiz.style.display="",this.horiz.firstChild.style.width="0"
return!this.checkedZeroWidth&&e.clientHeight>0&&(0==n&&this.zeroWidthHack(),this.checkedZeroWidth=!0),{right:r?n:0,bottom:t?n:0}},Wn.prototype.setScrollLeft=function(e){this.horiz.scrollLeft!=e&&(this.horiz.scrollLeft=e),this.disableHoriz&&this.enableZeroWidthBar(this.horiz,this.disableHoriz,"horiz")},Wn.prototype.setScrollTop=function(e){this.vert.scrollTop!=e&&(this.vert.scrollTop=e),this.disableVert&&this.enableZeroWidthBar(this.vert,this.disableVert,"vert")},Wn.prototype.zeroWidthHack=function(){var e=y&&!p?"12px":"18px"
this.horiz.style.height=this.vert.style.width=e,this.horiz.style.pointerEvents=this.vert.style.pointerEvents="none",this.disableHoriz=new W,this.disableVert=new W},Wn.prototype.enableZeroWidthBar=function(e,t,r){e.style.pointerEvents="auto",t.set(1e3,(function n(){var i=e.getBoundingClientRect();("vert"==r?document.elementFromPoint(i.right-1,(i.top+i.bottom)/2):document.elementFromPoint((i.right+i.left)/2,i.bottom-1))!=e?e.style.pointerEvents="none":t.set(1e3,n)}))},Wn.prototype.clear=function(){var e=this.horiz.parentNode
e.removeChild(this.horiz),e.removeChild(this.vert)}
var Rn=function(){}
function $n(e,t){t||(t=Pn(e))
var r=e.display.barWidth,n=e.display.barHeight
jn(e,t)
for(var i=0;i<4&&r!=e.display.barWidth||n!=e.display.barHeight;i++)r!=e.display.barWidth&&e.options.lineWrapping&&Tn(e),jn(e,Pn(e)),r=e.display.barWidth,n=e.display.barHeight}function jn(e,t){var r=e.display,n=r.scrollbars.update(t)
r.sizer.style.paddingRight=(r.barWidth=n.right)+"px",r.sizer.style.paddingBottom=(r.barHeight=n.bottom)+"px",r.heightForcer.style.borderBottom=n.bottom+"px solid transparent",n.right&&n.bottom?(r.scrollbarFiller.style.display="block",r.scrollbarFiller.style.height=n.bottom+"px",r.scrollbarFiller.style.width=n.right+"px"):r.scrollbarFiller.style.display="",n.bottom&&e.options.coverGutterNextToScrollbar&&e.options.fixedGutter?(r.gutterFiller.style.display="block",r.gutterFiller.style.height=n.bottom+"px",r.gutterFiller.style.width=t.gutterWidth+"px"):r.gutterFiller.style.display=""}Rn.prototype.update=function(){return{bottom:0,right:0}},Rn.prototype.setScrollLeft=function(){},Rn.prototype.setScrollTop=function(){},Rn.prototype.clear=function(){}
var Hn={native:Wn,null:Rn}
function Bn(e){e.display.scrollbars&&(e.display.scrollbars.clear(),e.display.scrollbars.addClass&&T(e.display.wrapper,e.display.scrollbars.addClass)),e.display.scrollbars=new Hn[e.options.scrollbarStyle]((function(t){e.display.wrapper.insertBefore(t,e.display.scrollbarFiller),de(t,"mousedown",(function(){e.state.focused&&setTimeout((function(){return e.display.input.focus()}),0)})),t.setAttribute("cm-not-content","true")}),(function(t,r){"horizontal"==r?Fn(e,t):In(e,t)}),e),e.display.scrollbars.addClass&&q(e.display.wrapper,e.display.scrollbars.addClass)}var Un=0
function Gn(e){var t
e.curOp={cm:e,viewChanged:!1,startHeight:e.doc.height,forceUpdate:!1,updateInput:0,typing:!1,changeObjs:null,cursorActivityHandlers:null,cursorActivityCalled:0,selectionChanged:!1,updateMaxLine:!1,scrollLeft:null,scrollTop:null,scrollToPos:null,focus:!1,id:++Un},t=e.curOp,or?or.ops.push(t):t.ownsGroup=or={ops:[t],delayedCallbacks:[]}}function Vn(e){var t=e.curOp
t&&function(e,t){var r=e.ownsGroup
if(r)try{(function(e){var t=e.delayedCallbacks,r=0
do{for(;r<t.length;r++)t[r].call(null)
for(var n=0;n<e.ops.length;n++){var i=e.ops[n]
if(i.cursorActivityHandlers)for(;i.cursorActivityCalled<i.cursorActivityHandlers.length;)i.cursorActivityHandlers[i.cursorActivityCalled++].call(null,i.cm)}}while(r<t.length)})(r)}finally{or=null,t(r)}}(t,(function(e){for(var t=0;t<e.ops.length;t++)e.ops[t].cm.curOp=null;(function(e){for(var t=e.ops,r=0;r<t.length;r++)Kn(t[r])
for(var n=0;n<t.length;n++)Zn(t[n])
for(var i=0;i<t.length;i++)Xn(t[i])
for(var o=0;o<t.length;o++)Yn(t[o])
for(var a=0;a<t.length;a++)Qn(t[a])})(e)}))}function Kn(e){var t=e.cm,r=t.display;(function(e){var t=e.display
!t.scrollbarsClipped&&t.scroller.offsetWidth&&(t.nativeBarWidth=t.scroller.offsetWidth-t.scroller.clientWidth,t.heightForcer.style.height=Sr(e)+"px",t.sizer.style.marginBottom=-t.nativeBarWidth+"px",t.sizer.style.borderRightWidth=Sr(e)+"px",t.scrollbarsClipped=!0)})(t),e.updateMaxLine&&Ut(t),e.mustUpdate=e.viewChanged||e.forceUpdate||null!=e.scrollTop||e.scrollToPos&&(e.scrollToPos.from.line<r.viewFrom||e.scrollToPos.to.line>=r.viewTo)||r.maxLineChanged&&t.options.lineWrapping,e.update=e.mustUpdate&&new oi(t,e.mustUpdate&&{top:e.scrollTop,ensure:e.scrollToPos},e.forceUpdate)}function Zn(e){e.updatedDisplay=e.mustUpdate&&ai(e.cm,e.update)}function Xn(e){var t=e.cm,r=t.display
e.updatedDisplay&&Tn(t),e.barMeasure=Pn(t),r.maxLineChanged&&!t.options.lineWrapping&&(e.adjustWidthTo=zr(t,r.maxLine,r.maxLine.text.length).left+3,t.display.sizerWidth=e.adjustWidthTo,e.barMeasure.scrollWidth=Math.max(r.scroller.clientWidth,r.sizer.offsetLeft+e.adjustWidthTo+Sr(t)+t.display.barWidth),e.maxScrollLeft=Math.max(0,r.sizer.offsetLeft+e.adjustWidthTo-Tr(t))),(e.updatedDisplay||e.selectionChanged)&&(e.preparedSelection=r.input.prepareSelection())}function Yn(e){var t=e.cm
null!=e.adjustWidthTo&&(t.display.sizer.style.minWidth=e.adjustWidthTo+"px",e.maxScrollLeft<t.doc.scrollLeft&&Fn(t,Math.min(t.display.scroller.scrollLeft,e.maxScrollLeft),!0),t.display.maxLineChanged=!1)
var r=e.focus&&e.focus==N()
e.preparedSelection&&t.display.input.showSelection(e.preparedSelection,r),(e.updatedDisplay||e.startHeight!=t.doc.height)&&$n(t,e.barMeasure),e.updatedDisplay&&ui(t,e.barMeasure),e.selectionChanged&&wn(t),t.state.focused&&e.updateInput&&t.display.input.reset(e.typing),r&&kn(e.cm)}function Qn(e){var t=e.cm,r=t.display,n=t.doc;(e.updatedDisplay&&li(t,e.update),null==r.wheelStartX||null==e.scrollTop&&null==e.scrollLeft&&!e.scrollToPos||(r.wheelStartX=r.wheelStartY=null),null!=e.scrollTop&&Dn(t,e.scrollTop,e.forceScroll),null!=e.scrollLeft&&Fn(t,e.scrollLeft,!0,!0),e.scrollToPos)&&function(e,t){if(!me(e,"scrollCursorIntoView")){var r=e.display,n=r.sizer.getBoundingClientRect(),i=null
if(t.top+n.top<0?i=!0:t.bottom+n.top>(window.innerHeight||document.documentElement.clientHeight)&&(i=!1),null!=i&&!h){var o=z("div","​",null,"position: absolute;\n                         top: "+(t.top-r.viewOffset-kr(e.display))+"px;\n                         height: "+(t.bottom-t.top+Sr(e)+r.barHeight)+"px;\n                         left: "+t.left+"px; width: "+Math.max(2,t.right-t.left)+"px;")
e.display.lineSpace.appendChild(o),o.scrollIntoView(i),e.display.lineSpace.removeChild(o)}}}(t,function(e,t,r,n){var i
null==n&&(n=0),e.options.lineWrapping||t!=r||(r="before"==(t=t.ch?et(t.line,"before"==t.sticky?t.ch-1:t.ch,"after"):t).sticky?et(t.line,t.ch+1,"before"):t)
for(var o=0;o<5;o++){var a=!1,l=Gr(e,t),s=r&&r!=t?Gr(e,r):l,c=zn(e,i={left:Math.min(l.left,s.left),top:Math.min(l.top,s.top)-n,right:Math.max(l.left,s.left),bottom:Math.max(l.bottom,s.bottom)+n}),u=e.doc.scrollTop,d=e.doc.scrollLeft
if(null!=c.scrollTop&&(In(e,c.scrollTop),Math.abs(e.doc.scrollTop-u)>1&&(a=!0)),null!=c.scrollLeft&&(Fn(e,c.scrollLeft),Math.abs(e.doc.scrollLeft-d)>1&&(a=!0)),!a)break}return i}(t,lt(n,e.scrollToPos.from),lt(n,e.scrollToPos.to),e.scrollToPos.margin))
var i=e.maybeHiddenMarkers,o=e.maybeUnhiddenMarkers
if(i)for(var a=0;a<i.length;++a)i[a].lines.length||he(i[a],"hide")
if(o)for(var l=0;l<o.length;++l)o[l].lines.length&&he(o[l],"unhide")
r.wrapper.offsetHeight&&(n.scrollTop=t.display.scroller.scrollTop),e.changeObjs&&he(t,"changes",t,e.changeObjs),e.update&&e.update.finish()}function Jn(e,t){if(e.curOp)return t()
Gn(e)
try{return t()}finally{Vn(e)}}function ei(e,t){return function(){if(e.curOp)return t.apply(e,arguments)
Gn(e)
try{return t.apply(e,arguments)}finally{Vn(e)}}}function ti(e){return function(){if(this.curOp)return e.apply(this,arguments)
Gn(this)
try{return e.apply(this,arguments)}finally{Vn(this)}}}function ri(e){return function(){var t=this.cm
if(!t||t.curOp)return e.apply(this,arguments)
Gn(t)
try{return e.apply(this,arguments)}finally{Vn(t)}}}function ni(e,t){e.doc.highlightFrontier<e.display.viewTo&&e.state.highlight.set(t,D(ii,e))}function ii(e){var t=e.doc
if(!(t.highlightFrontier>=e.display.viewTo)){var r=+new Date+e.options.workTime,n=pt(e,t.highlightFrontier),i=[]
t.iter(n.line,Math.min(t.first+t.size,e.display.viewTo+500),(function(o){if(n.line>=e.display.viewFrom){var a=o.styles,l=o.text.length>e.options.maxHighlightLength?je(t.mode,n.state):null,s=dt(e,o,n,!0)
l&&(n.state=l),o.styles=s.styles
var c=o.styleClasses,u=s.classes
u?o.styleClasses=u:c&&(o.styleClasses=null)
for(var d=!a||a.length!=o.styles.length||c!=u&&(!c||!u||c.bgClass!=u.bgClass||c.textClass!=u.textClass),f=0;!d&&f<a.length;++f)d=a[f]!=o.styles[f]
d&&i.push(n.line),o.stateAfter=n.save(),n.nextLine()}else o.text.length<=e.options.maxHighlightLength&&ht(e,o.text,n),o.stateAfter=n.line%5==0?n.save():null,n.nextLine()
if(+new Date>r)return ni(e,e.options.workDelay),!0})),t.highlightFrontier=n.line,t.modeFrontier=Math.max(t.modeFrontier,n.line),i.length&&Jn(e,(function(){for(var t=0;t<i.length;t++)fn(e,i[t],"text")}))}}var oi=function(e,t,r){var n=e.display
this.viewport=t,this.visible=Ln(n,e.doc,t),this.editorIsHidden=!n.wrapper.offsetWidth,this.wrapperHeight=n.wrapper.clientHeight,this.wrapperWidth=n.wrapper.clientWidth,this.oldDisplayWidth=Tr(e),this.force=r,this.dims=on(e),this.events=[]}
function ai(e,t){var r=e.display,n=e.doc
if(t.editorIsHidden)return pn(e),!1
if(!t.force&&t.visible.from>=r.viewFrom&&t.visible.to<=r.viewTo&&(null==r.updateLineNumbers||r.updateLineNumbers>=r.viewTo)&&r.renderedView==r.view&&0==mn(e))return!1
fi(e)&&(pn(e),t.dims=on(e))
var i=n.first+n.size,o=Math.max(t.visible.from-e.options.viewportMargin,n.first),a=Math.min(i,t.visible.to+e.options.viewportMargin)
r.viewFrom<o&&o-r.viewFrom<20&&(o=Math.max(n.first,r.viewFrom)),r.viewTo>a&&r.viewTo-a<20&&(a=Math.min(i,r.viewTo)),kt&&(o=Wt(e.doc,o),a=Rt(e.doc,a))
var l=o!=r.viewFrom||a!=r.viewTo||r.lastWrapHeight!=t.wrapperHeight||r.lastWrapWidth!=t.wrapperWidth;(function(e,t,r){var n=e.display
0==n.view.length||t>=n.viewTo||r<=n.viewFrom?(n.view=ir(e,t,r),n.viewFrom=t):(n.viewFrom>t?n.view=ir(e,t,n.viewFrom).concat(n.view):n.viewFrom<t&&(n.view=n.view.slice(un(e,t))),n.viewFrom=t,n.viewTo<r?n.view=n.view.concat(ir(e,n.viewTo,r)):n.viewTo>r&&(n.view=n.view.slice(0,un(e,r)))),n.viewTo=r})(e,o,a),r.viewOffset=Ht(Ge(e.doc,r.viewFrom)),e.display.mover.style.top=r.viewOffset+"px"
var c=mn(e)
if(!l&&0==c&&!t.force&&r.renderedView==r.view&&(null==r.updateLineNumbers||r.updateLineNumbers>=r.viewTo))return!1
var u=function(e){if(e.hasFocus())return null
var t=N()
if(!t||!E(e.display.lineDiv,t))return null
var r={activeElt:t}
if(window.getSelection){var n=window.getSelection()
n.anchorNode&&n.extend&&E(e.display.lineDiv,n.anchorNode)&&(r.anchorNode=n.anchorNode,r.anchorOffset=n.anchorOffset,r.focusNode=n.focusNode,r.focusOffset=n.focusOffset)}return r}(e)
return c>4&&(r.lineDiv.style.display="none"),function(e,t,r){var n=e.display,i=e.options.lineNumbers,o=n.lineDiv,a=o.firstChild
function l(t){var r=t.nextSibling
return s&&y&&e.display.currentWheelTarget==t?t.style.display="none":t.parentNode.removeChild(t),r}for(var c=n.view,u=n.viewFrom,d=0;d<c.length;d++){var f=c[d]
if(f.hidden);else if(f.node&&f.node.parentNode==o){for(;a!=f.node;)a=l(a)
var p=i&&null!=t&&t<=u&&f.lineNumber
f.changes&&(R(f.changes,"gutter")>-1&&(p=!1),cr(e,f,u,r)),p&&(M(f.lineNumber),f.lineNumber.appendChild(document.createTextNode(Je(e.options,u)))),a=f.node.nextSibling}else{var h=gr(e,f,u,r)
o.insertBefore(h,a)}u+=f.size}for(;a;)a=l(a)}(e,r.updateLineNumbers,t.dims),c>4&&(r.lineDiv.style.display=""),r.renderedView=r.view,function(e){if(e&&e.activeElt&&e.activeElt!=N()&&(e.activeElt.focus(),e.anchorNode&&E(document.body,e.anchorNode)&&E(document.body,e.focusNode))){var t=window.getSelection(),r=document.createRange()
r.setEnd(e.anchorNode,e.anchorOffset),r.collapse(!1),t.removeAllRanges(),t.addRange(r),t.extend(e.focusNode,e.focusOffset)}}(u),M(r.cursorDiv),M(r.selectionDiv),r.gutters.style.height=r.sizer.style.minHeight=0,l&&(r.lastWrapHeight=t.wrapperHeight,r.lastWrapWidth=t.wrapperWidth,ni(e,400)),r.updateLineNumbers=null,!0}function li(e,t){for(var r=t.viewport,n=!0;(n&&e.options.lineWrapping&&t.oldDisplayWidth!=Tr(e)||(r&&null!=r.top&&(r={top:Math.min(e.doc.height+_r(e.display)-Mr(e),r.top)}),t.visible=Ln(e.display,e.doc,r),!(t.visible.from>=e.display.viewFrom&&t.visible.to<=e.display.viewTo)))&&ai(e,t);n=!1){Tn(e)
var i=Pn(e)
gn(e),$n(e,i),ui(e,i),t.force=!1}t.signal(e,"update",e),e.display.viewFrom==e.display.reportedViewFrom&&e.display.viewTo==e.display.reportedViewTo||(t.signal(e,"viewportChange",e,e.display.viewFrom,e.display.viewTo),e.display.reportedViewFrom=e.display.viewFrom,e.display.reportedViewTo=e.display.viewTo)}function si(e,t){var r=new oi(e,t)
if(ai(e,r)){Tn(e),li(e,r)
var n=Pn(e)
gn(e),$n(e,n),ui(e,n),r.finish()}}function ci(e){var t=e.gutters.offsetWidth
e.sizer.style.marginLeft=t+"px"}function ui(e,t){e.display.sizer.style.minHeight=t.docHeight+"px",e.display.heightForcer.style.top=t.docHeight+"px",e.display.gutters.style.height=t.docHeight+e.display.barHeight+Sr(e)+"px"}function di(e){var t=e.display,r=t.view
if(t.alignWidgets||t.gutters.firstChild&&e.options.fixedGutter){for(var n=an(t)-t.scroller.scrollLeft+e.doc.scrollLeft,i=t.gutters.offsetWidth,o=n+"px",a=0;a<r.length;a++)if(!r[a].hidden){e.options.fixedGutter&&(r[a].gutter&&(r[a].gutter.style.left=o),r[a].gutterBackground&&(r[a].gutterBackground.style.left=o))
var l=r[a].alignable
if(l)for(var s=0;s<l.length;s++)l[s].style.left=o}e.options.fixedGutter&&(t.gutters.style.left=n+i+"px")}}function fi(e){if(!e.options.lineNumbers)return!1
var t=e.doc,r=Je(e.options,t.first+t.size-1),n=e.display
if(r.length!=n.lineNumChars){var i=n.measure.appendChild(z("div",[z("div",r)],"CodeMirror-linenumber CodeMirror-gutter-elt")),o=i.firstChild.offsetWidth,a=i.offsetWidth-o
return n.lineGutter.style.width="",n.lineNumInnerWidth=Math.max(o,n.lineGutter.offsetWidth-a)+1,n.lineNumWidth=n.lineNumInnerWidth+a,n.lineNumChars=n.lineNumInnerWidth?r.length:-1,n.lineGutter.style.width=n.lineNumWidth+"px",ci(e.display),!0}return!1}function pi(e,t){for(var r=[],n=!1,i=0;i<e.length;i++){var o=e[i],a=null
if("string"!=typeof o&&(a=o.style,o=o.className),"CodeMirror-linenumbers"==o){if(!t)continue
n=!0}r.push({className:o,style:a})}return t&&!n&&r.push({className:"CodeMirror-linenumbers",style:null}),r}function hi(e){var t=e.gutters,r=e.gutterSpecs
M(t),e.lineGutter=null
for(var n=0;n<r.length;++n){var i=r[n],o=i.className,a=i.style,l=t.appendChild(z("div",null,"CodeMirror-gutter "+o))
a&&(l.style.cssText=a),"CodeMirror-linenumbers"==o&&(e.lineGutter=l,l.style.width=(e.lineNumWidth||1)+"px")}t.style.display=r.length?"":"none",ci(e)}function mi(e){hi(e.display),dn(e),di(e)}function gi(e,t,n,i){var o=this
this.input=n,o.scrollbarFiller=z("div",null,"CodeMirror-scrollbar-filler"),o.scrollbarFiller.setAttribute("cm-not-content","true"),o.gutterFiller=z("div",null,"CodeMirror-gutter-filler"),o.gutterFiller.setAttribute("cm-not-content","true"),o.lineDiv=A("div",null,"CodeMirror-code"),o.selectionDiv=z("div",null,null,"position: relative; z-index: 1"),o.cursorDiv=z("div",null,"CodeMirror-cursors"),o.measure=z("div",null,"CodeMirror-measure"),o.lineMeasure=z("div",null,"CodeMirror-measure"),o.lineSpace=A("div",[o.measure,o.lineMeasure,o.selectionDiv,o.cursorDiv,o.lineDiv],null,"position: relative; outline: none")
var c=A("div",[o.lineSpace],"CodeMirror-lines")
o.mover=z("div",[c],null,"position: relative"),o.sizer=z("div",[o.mover],"CodeMirror-sizer"),o.sizerWidth=null,o.heightForcer=z("div",null,null,"position: absolute; height: 30px; width: 1px;"),o.gutters=z("div",null,"CodeMirror-gutters"),o.lineGutter=null,o.scroller=z("div",[o.sizer,o.heightForcer,o.gutters],"CodeMirror-scroll"),o.scroller.setAttribute("tabIndex","-1"),o.wrapper=z("div",[o.scrollbarFiller,o.gutterFiller,o.scroller],"CodeMirror"),a&&l<8&&(o.gutters.style.zIndex=-1,o.scroller.style.paddingRight=0),s||r&&v||(o.scroller.draggable=!0),e&&(e.appendChild?e.appendChild(o.wrapper):e(o.wrapper)),o.viewFrom=o.viewTo=t.first,o.reportedViewFrom=o.reportedViewTo=t.first,o.view=[],o.renderedView=null,o.externalMeasured=null,o.viewOffset=0,o.lastWrapHeight=o.lastWrapWidth=0,o.updateLineNumbers=null,o.nativeBarWidth=o.barHeight=o.barWidth=0,o.scrollbarsClipped=!1,o.lineNumWidth=o.lineNumInnerWidth=o.lineNumChars=null,o.alignWidgets=!1,o.cachedCharWidth=o.cachedTextHeight=o.cachedPaddingH=null,o.maxLine=null,o.maxLineLength=0,o.maxLineChanged=!1,o.wheelDX=o.wheelDY=o.wheelStartX=o.wheelStartY=null,o.shift=!1
o.selForContextMenu=null,o.activeTouch=null,o.gutterSpecs=pi(i.gutters,i.lineNumbers),hi(o),n.init(o)}oi.prototype.signal=function(e,t){ve(e,t)&&this.events.push(arguments)},oi.prototype.finish=function(){for(var e=0;e<this.events.length;e++)he.apply(null,this.events[e])}
var vi=0,yi=null
function bi(e){var t=e.wheelDeltaX,r=e.wheelDeltaY
return null==t&&e.detail&&e.axis==e.HORIZONTAL_AXIS&&(t=e.detail),null==r&&e.detail&&e.axis==e.VERTICAL_AXIS?r=e.detail:null==r&&(r=e.wheelDelta),{x:t,y:r}}function xi(e){var t=bi(e)
return t.x*=yi,t.y*=yi,t}function wi(e,t){var n=bi(t),i=n.x,o=n.y,a=e.display,l=a.scroller,c=l.scrollWidth>l.clientWidth,u=l.scrollHeight>l.clientHeight
if(i&&c||o&&u){if(o&&y&&s)e:for(var f=t.target,p=a.view;f!=l;f=f.parentNode)for(var h=0;h<p.length;h++)if(p[h].node==f){e.display.currentWheelTarget=f
break e}if(i&&!r&&!d&&null!=yi)return o&&u&&In(e,Math.max(0,l.scrollTop+o*yi)),Fn(e,Math.max(0,l.scrollLeft+i*yi)),(!o||o&&u)&&be(t),void(a.wheelStartX=null)
if(o&&null!=yi){var m=o*yi,g=e.doc.scrollTop,v=g+a.wrapper.clientHeight
m<0?g=Math.max(0,g+m-50):v=Math.min(e.doc.height,v+m+50),si(e,{top:g,bottom:v})}vi<20&&(null==a.wheelStartX?(a.wheelStartX=l.scrollLeft,a.wheelStartY=l.scrollTop,a.wheelDX=i,a.wheelDY=o,setTimeout((function(){if(null!=a.wheelStartX){var e=l.scrollLeft-a.wheelStartX,t=l.scrollTop-a.wheelStartY,r=t&&a.wheelDY&&t/a.wheelDY||e&&a.wheelDX&&e/a.wheelDX
a.wheelStartX=a.wheelStartY=null,r&&(yi=(yi*vi+r)/(vi+1),++vi)}}),200)):(a.wheelDX+=i,a.wheelDY+=o))}}a?yi=-.53:r?yi=15:u?yi=-.7:f&&(yi=-1/3)
var ki=function(e,t){this.ranges=e,this.primIndex=t}
ki.prototype.primary=function(){return this.ranges[this.primIndex]},ki.prototype.equals=function(e){if(e==this)return!0
if(e.primIndex!=this.primIndex||e.ranges.length!=this.ranges.length)return!1
for(var t=0;t<this.ranges.length;t++){var r=this.ranges[t],n=e.ranges[t]
if(!rt(r.anchor,n.anchor)||!rt(r.head,n.head))return!1}return!0},ki.prototype.deepCopy=function(){for(var e=[],t=0;t<this.ranges.length;t++)e[t]=new _i(nt(this.ranges[t].anchor),nt(this.ranges[t].head))
return new ki(e,this.primIndex)},ki.prototype.somethingSelected=function(){for(var e=0;e<this.ranges.length;e++)if(!this.ranges[e].empty())return!0
return!1},ki.prototype.contains=function(e,t){t||(t=e)
for(var r=0;r<this.ranges.length;r++){var n=this.ranges[r]
if(tt(t,n.from())>=0&&tt(e,n.to())<=0)return r}return-1}
var _i=function(e,t){this.anchor=e,this.head=t}
function Ci(e,t,r){var n=e&&e.options.selectionsMayTouch,i=t[r]
t.sort((function(e,t){return tt(e.from(),t.from())})),r=R(t,i)
for(var o=1;o<t.length;o++){var a=t[o],l=t[o-1],s=tt(l.to(),a.from())
if(n&&!a.empty()?s>0:s>=0){var c=ot(l.from(),a.from()),u=it(l.to(),a.to()),d=l.empty()?a.from()==a.head:l.from()==l.head
o<=r&&--r,t.splice(--o,2,new _i(d?u:c,d?c:u))}}return new ki(t,r)}function Si(e,t){return new ki([new _i(e,t||e)],0)}function Ti(e){return e.text?et(e.from.line+e.text.length-1,K(e.text).length+(1==e.text.length?e.from.ch:0)):e.to}function Mi(e,t){if(tt(e,t.from)<0)return e
if(tt(e,t.to)<=0)return Ti(t)
var r=e.line+t.text.length-(t.to.line-t.from.line)-1,n=e.ch
return e.line==t.to.line&&(n+=Ti(t).ch-t.to.ch),et(r,n)}function Li(e,t){for(var r=[],n=0;n<e.sel.ranges.length;n++){var i=e.sel.ranges[n]
r.push(new _i(Mi(i.anchor,t),Mi(i.head,t)))}return Ci(e.cm,r,e.sel.primIndex)}function zi(e,t,r){return e.line==t.line?et(r.line,e.ch-t.ch+r.ch):et(r.line+(e.line-t.line),e.ch)}function Ai(e){e.doc.mode=We(e.options,e.doc.modeOption),Ei(e)}function Ei(e){e.doc.iter((function(e){e.stateAfter&&(e.stateAfter=null),e.styles&&(e.styles=null)})),e.doc.modeFrontier=e.doc.highlightFrontier=e.doc.first,ni(e,100),e.state.modeGen++,e.curOp&&dn(e)}function Ni(e,t){return 0==t.from.ch&&0==t.to.ch&&""==K(t.text)&&(!e.cm||e.cm.options.wholeLineUpdateBefore)}function qi(e,t,r,n){function i(e){return r?r[e]:null}function o(e,r,i){(function(e,t,r,n){e.text=t,e.stateAfter&&(e.stateAfter=null),e.styles&&(e.styles=null),null!=e.order&&(e.order=null),Lt(e),zt(e,r)
var i=n?n(e):1
i!=e.height&&Ze(e,i)})(e,r,i,n),lr(e,"change",e,t)}function a(e,t){for(var r=[],o=e;o<t;++o)r.push(new Gt(c[o],i(o),n))
return r}var l=t.from,s=t.to,c=t.text,u=Ge(e,l.line),d=Ge(e,s.line),f=K(c),p=i(c.length-1),h=s.line-l.line
if(t.full)e.insert(0,a(0,c.length)),e.remove(c.length,e.size-c.length)
else if(Ni(e,t)){var m=a(0,c.length-1)
o(d,d.text,p),h&&e.remove(l.line,h),m.length&&e.insert(l.line,m)}else if(u==d)if(1==c.length)o(u,u.text.slice(0,l.ch)+f+u.text.slice(s.ch),p)
else{var g=a(1,c.length-1)
g.push(new Gt(f+u.text.slice(s.ch),p,n)),o(u,u.text.slice(0,l.ch)+c[0],i(0)),e.insert(l.line+1,g)}else if(1==c.length)o(u,u.text.slice(0,l.ch)+c[0]+d.text.slice(s.ch),i(0)),e.remove(l.line+1,h)
else{o(u,u.text.slice(0,l.ch)+c[0],i(0)),o(d,f+d.text.slice(s.ch),p)
var v=a(1,c.length-1)
h>1&&e.remove(l.line+1,h-1),e.insert(l.line+1,v)}lr(e,"change",e,t)}function Oi(e,t,r){(function e(n,i,o){if(n.linked)for(var a=0;a<n.linked.length;++a){var l=n.linked[a]
if(l.doc!=i){var s=o&&l.sharedHist
r&&!s||(t(l.doc,s),e(l.doc,n,s))}}})(e,null,!0)}function Ii(e,t){if(t.cm)throw new Error("This document is already in use.")
e.doc=t,t.cm=e,sn(e),Ai(e),Di(e),e.options.lineWrapping||Ut(e),e.options.mode=t.modeOption,dn(e)}function Di(e){("rtl"==e.doc.direction?q:T)(e.display.lineDiv,"CodeMirror-rtl")}function Fi(e){this.done=[],this.undone=[],this.undoDepth=1/0,this.lastModTime=this.lastSelTime=0,this.lastOp=this.lastSelOp=null,this.lastOrigin=this.lastSelOrigin=null,this.generation=this.maxGeneration=e||1}function Pi(e,t){var r={from:nt(t.from),to:Ti(t),text:Ve(e,t.from,t.to)}
return Hi(e,r,t.from.line,t.to.line+1),Oi(e,(function(e){return Hi(e,r,t.from.line,t.to.line+1)}),!0),r}function Wi(e){for(;e.length;){if(!K(e).ranges)break
e.pop()}}function Ri(e,t,r,n){var i=e.history
i.undone.length=0
var o,a,l=+new Date
if((i.lastOp==n||i.lastOrigin==t.origin&&t.origin&&("+"==t.origin.charAt(0)&&i.lastModTime>l-(e.cm?e.cm.options.historyEventDelay:500)||"*"==t.origin.charAt(0)))&&(o=function(e,t){return t?(Wi(e.done),K(e.done)):e.done.length&&!K(e.done).ranges?K(e.done):e.done.length>1&&!e.done[e.done.length-2].ranges?(e.done.pop(),K(e.done)):void 0}(i,i.lastOp==n)))a=K(o.changes),0==tt(t.from,t.to)&&0==tt(t.from,a.to)?a.to=Ti(t):o.changes.push(Pi(e,t))
else{var s=K(i.done)
for(s&&s.ranges||ji(e.sel,i.done),o={changes:[Pi(e,t)],generation:i.generation},i.done.push(o);i.done.length>i.undoDepth;)i.done.shift(),i.done[0].ranges||i.done.shift()}i.done.push(r),i.generation=++i.maxGeneration,i.lastModTime=i.lastSelTime=l,i.lastOp=i.lastSelOp=n,i.lastOrigin=i.lastSelOrigin=t.origin,a||he(e,"historyAdded")}function $i(e,t,r,n){var i=e.history,o=n&&n.origin
r==i.lastSelOp||o&&i.lastSelOrigin==o&&(i.lastModTime==i.lastSelTime&&i.lastOrigin==o||function(e,t,r,n){var i=t.charAt(0)
return"*"==i||"+"==i&&r.ranges.length==n.ranges.length&&r.somethingSelected()==n.somethingSelected()&&new Date-e.history.lastSelTime<=(e.cm?e.cm.options.historyEventDelay:500)}(e,o,K(i.done),t))?i.done[i.done.length-1]=t:ji(t,i.done),i.lastSelTime=+new Date,i.lastSelOrigin=o,i.lastSelOp=r,n&&!1!==n.clearRedo&&Wi(i.undone)}function ji(e,t){var r=K(t)
r&&r.ranges&&r.equals(e)||t.push(e)}function Hi(e,t,r,n){var i=t["spans_"+e.id],o=0
e.iter(Math.max(e.first,r),Math.min(e.first+e.size,n),(function(r){r.markedSpans&&((i||(i=t["spans_"+e.id]={}))[o]=r.markedSpans),++o}))}function Bi(e){if(!e)return null
for(var t,r=0;r<e.length;++r)e[r].marker.explicitlyCleared?t||(t=e.slice(0,r)):t&&t.push(e[r])
return t?t.length?t:null:e}function Ui(e,t){var r=function(e,t){var r=t["spans_"+e.id]
if(!r)return null
for(var n=[],i=0;i<t.text.length;++i)n.push(Bi(r[i]))
return n}(e,t),n=Tt(e,t)
if(!r)return n
if(!n)return r
for(var i=0;i<r.length;++i){var o=r[i],a=n[i]
if(o&&a)e:for(var l=0;l<a.length;++l){for(var s=a[l],c=0;c<o.length;++c)if(o[c].marker==s.marker)continue e
o.push(s)}else a&&(r[i]=a)}return r}function Gi(e,t,r){for(var n=[],i=0;i<e.length;++i){var o=e[i]
if(o.ranges)n.push(r?ki.prototype.deepCopy.call(o):o)
else{var a=o.changes,l=[]
n.push({changes:l})
for(var s=0;s<a.length;++s){var c=a[s],u=void 0
if(l.push({from:c.from,to:c.to,text:c.text}),t)for(var d in c)(u=d.match(/^spans_(\d+)$/))&&R(t,Number(u[1]))>-1&&(K(l)[d]=c[d],delete c[d])}}}return n}function Vi(e,t,r,n){if(n){var i=e.anchor
if(r){var o=tt(t,i)<0
o!=tt(r,i)<0?(i=t,t=r):o!=tt(t,r)<0&&(t=r)}return new _i(i,t)}return new _i(r||t,t)}function Ki(e,t,r,n,i){null==i&&(i=e.cm&&(e.cm.display.shift||e.extend)),Ji(e,new ki([Vi(e.sel.primary(),t,r,i)],0),n)}function Zi(e,t,r){for(var n=[],i=e.cm&&(e.cm.display.shift||e.extend),o=0;o<e.sel.ranges.length;o++)n[o]=Vi(e.sel.ranges[o],t[o],null,i)
Ji(e,Ci(e.cm,n,e.sel.primIndex),r)}function Xi(e,t,r,n){var i=e.sel.ranges.slice(0)
i[t]=r,Ji(e,Ci(e.cm,i,e.sel.primIndex),n)}function Yi(e,t,r,n){Ji(e,Si(t,r),n)}function Qi(e,t,r){var n=e.history.done,i=K(n)
i&&i.ranges?(n[n.length-1]=t,eo(e,t,r)):Ji(e,t,r)}function Ji(e,t,r){eo(e,t,r),$i(e,e.sel,e.cm?e.cm.curOp.id:NaN,r)}function eo(e,t,r){(ve(e,"beforeSelectionChange")||e.cm&&ve(e.cm,"beforeSelectionChange"))&&(t=function(e,t,r){var n={ranges:t.ranges,update:function(t){this.ranges=[]
for(var r=0;r<t.length;r++)this.ranges[r]=new _i(lt(e,t[r].anchor),lt(e,t[r].head))},origin:r&&r.origin}
return he(e,"beforeSelectionChange",e,n),e.cm&&he(e.cm,"beforeSelectionChange",e.cm,n),n.ranges!=t.ranges?Ci(e.cm,n.ranges,n.ranges.length-1):t}(e,t,r))
var n=r&&r.bias||(tt(t.primary().head,e.sel.primary().head)<0?-1:1)
to(e,no(e,t,n,!0)),r&&!1===r.scroll||!e.cm||En(e.cm)}function to(e,t){t.equals(e.sel)||(e.sel=t,e.cm&&(e.cm.curOp.updateInput=1,e.cm.curOp.selectionChanged=!0,ge(e.cm)),lr(e,"cursorActivity",e))}function ro(e){to(e,no(e,e.sel,null,!1))}function no(e,t,r,n){for(var i,o=0;o<t.ranges.length;o++){var a=t.ranges[o],l=t.ranges.length==e.sel.ranges.length&&e.sel.ranges[o],s=oo(e,a.anchor,l&&l.anchor,r,n),c=oo(e,a.head,l&&l.head,r,n);(i||s!=a.anchor||c!=a.head)&&(i||(i=t.ranges.slice(0,o)),i[o]=new _i(s,c))}return i?Ci(e.cm,i,t.primIndex):t}function io(e,t,r,n,i){var o=Ge(e,t.line)
if(o.markedSpans)for(var a=0;a<o.markedSpans.length;++a){var l=o.markedSpans[a],s=l.marker,c="selectLeft"in s?!s.selectLeft:s.inclusiveLeft,u="selectRight"in s?!s.selectRight:s.inclusiveRight
if((null==l.from||(c?l.from<=t.ch:l.from<t.ch))&&(null==l.to||(u?l.to>=t.ch:l.to>t.ch))){if(i&&(he(s,"beforeCursorEnter"),s.explicitlyCleared)){if(o.markedSpans){--a
continue}break}if(!s.atomic)continue
if(r){var d=s.find(n<0?1:-1),f=void 0
if((n<0?u:c)&&(d=ao(e,d,-n,d&&d.line==t.line?o:null)),d&&d.line==t.line&&(f=tt(d,r))&&(n<0?f<0:f>0))return io(e,d,t,n,i)}var p=s.find(n<0?-1:1)
return(n<0?c:u)&&(p=ao(e,p,n,p.line==t.line?o:null)),p?io(e,p,t,n,i):null}}return t}function oo(e,t,r,n,i){var o=n||1,a=io(e,t,r,o,i)||!i&&io(e,t,r,o,!0)||io(e,t,r,-o,i)||!i&&io(e,t,r,-o,!0)
return a||(e.cantEdit=!0,et(e.first,0))}function ao(e,t,r,n){return r<0&&0==t.ch?t.line>e.first?lt(e,et(t.line-1)):null:r>0&&t.ch==(n||Ge(e,t.line)).text.length?t.line<e.first+e.size-1?et(t.line+1,0):null:new et(t.line,t.ch+r)}function lo(e){e.setSelection(et(e.firstLine(),0),et(e.lastLine()),j)}function so(e,t,r){var n={canceled:!1,from:t.from,to:t.to,text:t.text,origin:t.origin,cancel:function(){return n.canceled=!0}}
return r&&(n.update=function(t,r,i,o){t&&(n.from=lt(e,t)),r&&(n.to=lt(e,r)),i&&(n.text=i),void 0!==o&&(n.origin=o)}),he(e,"beforeChange",e,n),e.cm&&he(e.cm,"beforeChange",e.cm,n),n.canceled?(e.cm&&(e.cm.curOp.updateInput=2),null):{from:n.from,to:n.to,text:n.text,origin:n.origin}}function co(e,t,r){if(e.cm){if(!e.cm.curOp)return ei(e.cm,co)(e,t,r)
if(e.cm.state.suppressEdits)return}if(!(ve(e,"beforeChange")||e.cm&&ve(e.cm,"beforeChange"))||(t=so(e,t,!0))){var n=wt&&!r&&function(e,t,r){var n=null
if(e.iter(t.line,r.line+1,(function(e){if(e.markedSpans)for(var t=0;t<e.markedSpans.length;++t){var r=e.markedSpans[t].marker
!r.readOnly||n&&-1!=R(n,r)||(n||(n=[])).push(r)}})),!n)return null
for(var i=[{from:t,to:r}],o=0;o<n.length;++o)for(var a=n[o],l=a.find(0),s=0;s<i.length;++s){var c=i[s]
if(!(tt(c.to,l.from)<0||tt(c.from,l.to)>0)){var u=[s,1],d=tt(c.from,l.from),f=tt(c.to,l.to);(d<0||!a.inclusiveLeft&&!d)&&u.push({from:c.from,to:l.from}),(f>0||!a.inclusiveRight&&!f)&&u.push({from:l.to,to:c.to}),i.splice.apply(i,u),s+=u.length-3}}return i}(e,t.from,t.to)
if(n)for(var i=n.length-1;i>=0;--i)uo(e,{from:n[i].from,to:n[i].to,text:i?[""]:t.text,origin:t.origin})
else uo(e,t)}}function uo(e,t){if(1!=t.text.length||""!=t.text[0]||0!=tt(t.from,t.to)){var r=Li(e,t)
Ri(e,t,r,e.cm?e.cm.curOp.id:NaN),ho(e,t,r,Tt(e,t))
var n=[]
Oi(e,(function(e,r){r||-1!=R(n,e.history)||(yo(e.history,t),n.push(e.history)),ho(e,t,null,Tt(e,t))}))}}function fo(e,t,r){var n=e.cm&&e.cm.state.suppressEdits
if(!n||r){for(var i,o=e.history,a=e.sel,l="undo"==t?o.done:o.undone,s="undo"==t?o.undone:o.done,c=0;c<l.length&&(i=l[c],r?!i.ranges||i.equals(e.sel):i.ranges);c++);if(c!=l.length){for(o.lastOrigin=o.lastSelOrigin=null;;){if(!(i=l.pop()).ranges){if(n)return void l.push(i)
break}if(ji(i,s),r&&!i.equals(e.sel))return void Ji(e,i,{clearRedo:!1})
a=i}var u=[]
ji(a,s),s.push({changes:u,generation:o.generation}),o.generation=i.generation||++o.maxGeneration
for(var d=ve(e,"beforeChange")||e.cm&&ve(e.cm,"beforeChange"),f=function(r){var n=i.changes[r]
if(n.origin=t,d&&!so(e,n,!1))return l.length=0,{}
u.push(Pi(e,n))
var o=r?Li(e,n):K(l)
ho(e,n,o,Ui(e,n)),!r&&e.cm&&e.cm.scrollIntoView({from:n.from,to:Ti(n)})
var a=[]
Oi(e,(function(e,t){t||-1!=R(a,e.history)||(yo(e.history,n),a.push(e.history)),ho(e,n,null,Ui(e,n))}))},p=i.changes.length-1;p>=0;--p){var h=f(p)
if(h)return h.v}}}}function po(e,t){if(0!=t&&(e.first+=t,e.sel=new ki(Z(e.sel.ranges,(function(e){return new _i(et(e.anchor.line+t,e.anchor.ch),et(e.head.line+t,e.head.ch))})),e.sel.primIndex),e.cm)){dn(e.cm,e.first,e.first-t,t)
for(var r=e.cm.display,n=r.viewFrom;n<r.viewTo;n++)fn(e.cm,n,"gutter")}}function ho(e,t,r,n){if(e.cm&&!e.cm.curOp)return ei(e.cm,ho)(e,t,r,n)
if(t.to.line<e.first)po(e,t.text.length-1-(t.to.line-t.from.line))
else if(!(t.from.line>e.lastLine())){if(t.from.line<e.first){var i=t.text.length-1-(e.first-t.from.line)
po(e,i),t={from:et(e.first,0),to:et(t.to.line+i,t.to.ch),text:[K(t.text)],origin:t.origin}}var o=e.lastLine()
t.to.line>o&&(t={from:t.from,to:et(o,Ge(e,o).text.length),text:[t.text[0]],origin:t.origin}),t.removed=Ve(e,t.from,t.to),r||(r=Li(e,t)),e.cm?function(e,t,r){var n=e.doc,i=e.display,o=t.from,a=t.to,l=!1,s=o.line
e.options.lineWrapping||(s=Xe(Pt(Ge(n,o.line))),n.iter(s,a.line+1,(function(e){if(e==i.maxLine)return l=!0,!0})))
n.sel.contains(t.from,t.to)>-1&&ge(e)
qi(n,t,r,ln(e)),e.options.lineWrapping||(n.iter(s,o.line+t.text.length,(function(e){var t=Bt(e)
t>i.maxLineLength&&(i.maxLine=e,i.maxLineLength=t,i.maxLineChanged=!0,l=!1)})),l&&(e.curOp.updateMaxLine=!0));(function(e,t){if(e.modeFrontier=Math.min(e.modeFrontier,t),!(e.highlightFrontier<t-10)){for(var r=e.first,n=t-1;n>r;n--){var i=Ge(e,n).stateAfter
if(i&&(!(i instanceof ct)||n+i.lookAhead<t)){r=n+1
break}}e.highlightFrontier=Math.min(e.highlightFrontier,r)}})(n,o.line),ni(e,400)
var c=t.text.length-(a.line-o.line)-1
t.full?dn(e):o.line!=a.line||1!=t.text.length||Ni(e.doc,t)?dn(e,o.line,a.line+1,c):fn(e,o.line,"text")
var u=ve(e,"changes"),d=ve(e,"change")
if(d||u){var f={from:o,to:a,text:t.text,removed:t.removed,origin:t.origin}
d&&lr(e,"change",e,f),u&&(e.curOp.changeObjs||(e.curOp.changeObjs=[])).push(f)}e.display.selForContextMenu=null}(e.cm,t,n):qi(e,t,n),eo(e,r,j),e.cantEdit&&oo(e,et(e.firstLine(),0))&&(e.cantEdit=!1)}}function mo(e,t,r,n,i){var o
n||(n=r),tt(n,r)<0&&(r=(o=[n,r])[0],n=o[1]),"string"==typeof t&&(t=e.splitLines(t)),co(e,{from:r,to:n,text:t,origin:i})}function go(e,t,r,n){r<e.line?e.line+=n:t<e.line&&(e.line=t,e.ch=0)}function vo(e,t,r,n){for(var i=0;i<e.length;++i){var o=e[i],a=!0
if(o.ranges){o.copied||((o=e[i]=o.deepCopy()).copied=!0)
for(var l=0;l<o.ranges.length;l++)go(o.ranges[l].anchor,t,r,n),go(o.ranges[l].head,t,r,n)}else{for(var s=0;s<o.changes.length;++s){var c=o.changes[s]
if(r<c.from.line)c.from=et(c.from.line+n,c.from.ch),c.to=et(c.to.line+n,c.to.ch)
else if(t<=c.to.line){a=!1
break}}a||(e.splice(0,i+1),i=0)}}}function yo(e,t){var r=t.from.line,n=t.to.line,i=t.text.length-(n-r)-1
vo(e.done,r,n,i),vo(e.undone,r,n,i)}function bo(e,t,r,n){var i=t,o=t
return"number"==typeof t?o=Ge(e,at(e,t)):i=Xe(t),null==i?null:(n(o,i)&&e.cm&&fn(e.cm,i,r),o)}function xo(e){this.lines=e,this.parent=null
for(var t=0,r=0;r<e.length;++r)e[r].parent=this,t+=e[r].height
this.height=t}function wo(e){this.children=e
for(var t=0,r=0,n=0;n<e.length;++n){var i=e[n]
t+=i.chunkSize(),r+=i.height,i.parent=this}this.size=t,this.height=r,this.parent=null}_i.prototype.from=function(){return ot(this.anchor,this.head)},_i.prototype.to=function(){return it(this.anchor,this.head)},_i.prototype.empty=function(){return this.head.line==this.anchor.line&&this.head.ch==this.anchor.ch},xo.prototype={chunkSize:function(){return this.lines.length},removeInner:function(e,t){for(var r=e,n=e+t;r<n;++r){var i=this.lines[r]
this.height-=i.height,Vt(i),lr(i,"delete")}this.lines.splice(e,t)},collapse:function(e){e.push.apply(e,this.lines)},insertInner:function(e,t,r){this.height+=r,this.lines=this.lines.slice(0,e).concat(t).concat(this.lines.slice(e))
for(var n=0;n<t.length;++n)t[n].parent=this},iterN:function(e,t,r){for(var n=e+t;e<n;++e)if(r(this.lines[e]))return!0}},wo.prototype={chunkSize:function(){return this.size},removeInner:function(e,t){this.size-=t
for(var r=0;r<this.children.length;++r){var n=this.children[r],i=n.chunkSize()
if(e<i){var o=Math.min(t,i-e),a=n.height
if(n.removeInner(e,o),this.height-=a-n.height,i==o&&(this.children.splice(r--,1),n.parent=null),0==(t-=o))break
e=0}else e-=i}if(this.size-t<25&&(this.children.length>1||!(this.children[0]instanceof xo))){var l=[]
this.collapse(l),this.children=[new xo(l)],this.children[0].parent=this}},collapse:function(e){for(var t=0;t<this.children.length;++t)this.children[t].collapse(e)},insertInner:function(e,t,r){this.size+=t.length,this.height+=r
for(var n=0;n<this.children.length;++n){var i=this.children[n],o=i.chunkSize()
if(e<=o){if(i.insertInner(e,t,r),i.lines&&i.lines.length>50){for(var a=i.lines.length%25+25,l=a;l<i.lines.length;){var s=new xo(i.lines.slice(l,l+=25))
i.height-=s.height,this.children.splice(++n,0,s),s.parent=this}i.lines=i.lines.slice(0,a),this.maybeSpill()}break}e-=o}},maybeSpill:function(){if(!(this.children.length<=10)){var e=this
do{var t=new wo(e.children.splice(e.children.length-5,5))
if(e.parent){e.size-=t.size,e.height-=t.height
var r=R(e.parent.children,e)
e.parent.children.splice(r+1,0,t)}else{var n=new wo(e.children)
n.parent=e,e.children=[n,t],e=n}t.parent=e.parent}while(e.children.length>10)
e.parent.maybeSpill()}},iterN:function(e,t,r){for(var n=0;n<this.children.length;++n){var i=this.children[n],o=i.chunkSize()
if(e<o){var a=Math.min(t,o-e)
if(i.iterN(e,a,r))return!0
if(0==(t-=a))break
e=0}else e-=o}}}
var ko=function(e,t,r){if(r)for(var n in r)r.hasOwnProperty(n)&&(this[n]=r[n])
this.doc=e,this.node=t}
function _o(e,t,r){Ht(t)<(e.curOp&&e.curOp.scrollTop||e.doc.scrollTop)&&An(e,r)}ko.prototype.clear=function(){var e=this.doc.cm,t=this.line.widgets,r=this.line,n=Xe(r)
if(null!=n&&t){for(var i=0;i<t.length;++i)t[i]==this&&t.splice(i--,1)
t.length||(r.widgets=null)
var o=xr(this)
Ze(r,Math.max(0,r.height-o)),e&&(Jn(e,(function(){_o(e,r,-o),fn(e,n,"widget")})),lr(e,"lineWidgetCleared",e,this,n))}},ko.prototype.changed=function(){var e=this,t=this.height,r=this.doc.cm,n=this.line
this.height=null
var i=xr(this)-t
i&&($t(this.doc,n)||Ze(n,n.height+i),r&&Jn(r,(function(){r.curOp.forceUpdate=!0,_o(r,n,i),lr(r,"lineWidgetChanged",r,e,Xe(n))})))},ye(ko)
var Co=0,So=function(e,t){this.lines=[],this.type=t,this.doc=e,this.id=++Co}
function To(e,t,r,n,i){if(n&&n.shared)return function(e,t,r,n,i){(n=F(n)).shared=!1
var o=[To(e,t,r,n,i)],a=o[0],l=n.widgetNode
return Oi(e,(function(e){l&&(n.widgetNode=l.cloneNode(!0)),o.push(To(e,lt(e,t),lt(e,r),n,i))
for(var s=0;s<e.linked.length;++s)if(e.linked[s].isParent)return
a=K(o)})),new Mo(o,a)}(e,t,r,n,i)
if(e.cm&&!e.cm.curOp)return ei(e.cm,To)(e,t,r,n,i)
var o=new So(e,i),a=tt(t,r)
if(n&&F(n,o,!1),a>0||0==a&&!1!==o.clearWhenEmpty)return o
if(o.replacedWith&&(o.collapsed=!0,o.widgetNode=A("span",[o.replacedWith],"CodeMirror-widget"),n.handleMouseEvents||o.widgetNode.setAttribute("cm-ignore-events","true"),n.insertLeft&&(o.widgetNode.insertLeft=!0)),o.collapsed){if(Ft(e,t.line,t,r,o)||t.line!=r.line&&Ft(e,r.line,t,r,o))throw new Error("Inserting collapsed marker partially overlapping an existing one")
kt=!0}o.addToHistory&&Ri(e,{from:t,to:r,origin:"markText"},e.sel,NaN)
var l,s=t.line,c=e.cm
if(e.iter(s,r.line+1,(function(e){c&&o.collapsed&&!c.options.lineWrapping&&Pt(e)==c.display.maxLine&&(l=!0),o.collapsed&&s!=t.line&&Ze(e,0),function(e,t){e.markedSpans=e.markedSpans?e.markedSpans.concat([t]):[t],t.marker.attachLine(e)}(e,new _t(o,s==t.line?t.ch:null,s==r.line?r.ch:null)),++s})),o.collapsed&&e.iter(t.line,r.line+1,(function(t){$t(e,t)&&Ze(t,0)})),o.clearOnEnter&&de(o,"beforeCursorEnter",(function(){return o.clear()})),o.readOnly&&(wt=!0,(e.history.done.length||e.history.undone.length)&&e.clearHistory()),o.collapsed&&(o.id=++Co,o.atomic=!0),c){if(l&&(c.curOp.updateMaxLine=!0),o.collapsed)dn(c,t.line,r.line+1)
else if(o.className||o.startStyle||o.endStyle||o.css||o.attributes||o.title)for(var u=t.line;u<=r.line;u++)fn(c,u,"text")
o.atomic&&ro(c.doc),lr(c,"markerAdded",c,o)}return o}So.prototype.clear=function(){if(!this.explicitlyCleared){var e=this.doc.cm,t=e&&!e.curOp
if(t&&Gn(e),ve(this,"clear")){var r=this.find()
r&&lr(this,"clear",r.from,r.to)}for(var n=null,i=null,o=0;o<this.lines.length;++o){var a=this.lines[o],l=Ct(a.markedSpans,this)
e&&!this.collapsed?fn(e,Xe(a),"text"):e&&(null!=l.to&&(i=Xe(a)),null!=l.from&&(n=Xe(a))),a.markedSpans=St(a.markedSpans,l),null==l.from&&this.collapsed&&!$t(this.doc,a)&&e&&Ze(a,rn(e.display))}if(e&&this.collapsed&&!e.options.lineWrapping)for(var s=0;s<this.lines.length;++s){var c=Pt(this.lines[s]),u=Bt(c)
u>e.display.maxLineLength&&(e.display.maxLine=c,e.display.maxLineLength=u,e.display.maxLineChanged=!0)}null!=n&&e&&this.collapsed&&dn(e,n,i+1),this.lines.length=0,this.explicitlyCleared=!0,this.atomic&&this.doc.cantEdit&&(this.doc.cantEdit=!1,e&&ro(e.doc)),e&&lr(e,"markerCleared",e,this,n,i),t&&Vn(e),this.parent&&this.parent.clear()}},So.prototype.find=function(e,t){var r,n
null==e&&"bookmark"==this.type&&(e=1)
for(var i=0;i<this.lines.length;++i){var o=this.lines[i],a=Ct(o.markedSpans,this)
if(null!=a.from&&(r=et(t?o:Xe(o),a.from),-1==e))return r
if(null!=a.to&&(n=et(t?o:Xe(o),a.to),1==e))return n}return r&&{from:r,to:n}},So.prototype.changed=function(){var e=this,t=this.find(-1,!0),r=this,n=this.doc.cm
t&&n&&Jn(n,(function(){var i=t.line,o=Xe(t.line),a=Ar(n,o)
if(a&&(Fr(a),n.curOp.selectionChanged=n.curOp.forceUpdate=!0),n.curOp.updateMaxLine=!0,!$t(r.doc,i)&&null!=r.height){var l=r.height
r.height=null
var s=xr(r)-l
s&&Ze(i,i.height+s)}lr(n,"markerChanged",n,e)}))},So.prototype.attachLine=function(e){if(!this.lines.length&&this.doc.cm){var t=this.doc.cm.curOp
t.maybeHiddenMarkers&&-1!=R(t.maybeHiddenMarkers,this)||(t.maybeUnhiddenMarkers||(t.maybeUnhiddenMarkers=[])).push(this)}this.lines.push(e)},So.prototype.detachLine=function(e){if(this.lines.splice(R(this.lines,e),1),!this.lines.length&&this.doc.cm){var t=this.doc.cm.curOp;(t.maybeHiddenMarkers||(t.maybeHiddenMarkers=[])).push(this)}},ye(So)
var Mo=function(e,t){this.markers=e,this.primary=t
for(var r=0;r<e.length;++r)e[r].parent=this}
function Lo(e){return e.findMarks(et(e.first,0),e.clipPos(et(e.lastLine())),(function(e){return e.parent}))}function zo(e){for(var t=function(t){var r=e[t],n=[r.primary.doc]
Oi(r.primary.doc,(function(e){return n.push(e)}))
for(var i=0;i<r.markers.length;i++){var o=r.markers[i];-1==R(n,o.doc)&&(o.parent=null,r.markers.splice(i--,1))}},r=0;r<e.length;r++)t(r)}Mo.prototype.clear=function(){if(!this.explicitlyCleared){this.explicitlyCleared=!0
for(var e=0;e<this.markers.length;++e)this.markers[e].clear()
lr(this,"clear")}},Mo.prototype.find=function(e,t){return this.primary.find(e,t)},ye(Mo)
var Ao=0,Eo=function(e,t,r,n,i){if(!(this instanceof Eo))return new Eo(e,t,r,n,i)
null==r&&(r=0),wo.call(this,[new xo([new Gt("",null)])]),this.first=r,this.scrollTop=this.scrollLeft=0,this.cantEdit=!1,this.cleanGeneration=1,this.modeFrontier=this.highlightFrontier=r
var o=et(r,0)
this.sel=Si(o),this.history=new Fi(null),this.id=++Ao,this.modeOption=t,this.lineSep=n,this.direction="rtl"==i?"rtl":"ltr",this.extend=!1,"string"==typeof e&&(e=this.splitLines(e)),qi(this,{from:o,to:o,text:e}),Ji(this,Si(o),j)}
Eo.prototype=Y(wo.prototype,{constructor:Eo,iter:function(e,t,r){r?this.iterN(e-this.first,t-e,r):this.iterN(this.first,this.first+this.size,e)},insert:function(e,t){for(var r=0,n=0;n<t.length;++n)r+=t[n].height
this.insertInner(e-this.first,t,r)},remove:function(e,t){this.removeInner(e-this.first,t)},getValue:function(e){var t=Ke(this,this.first,this.first+this.size)
return!1===e?t:t.join(e||this.lineSeparator())},setValue:ri((function(e){var t=et(this.first,0),r=this.first+this.size-1
co(this,{from:t,to:et(r,Ge(this,r).text.length),text:this.splitLines(e),origin:"setValue",full:!0},!0),this.cm&&Nn(this.cm,0,0),Ji(this,Si(t),j)})),replaceRange:function(e,t,r,n){mo(this,e,t=lt(this,t),r=r?lt(this,r):t,n)},getRange:function(e,t,r){var n=Ve(this,lt(this,e),lt(this,t))
return!1===r?n:n.join(r||this.lineSeparator())},getLine:function(e){var t=this.getLineHandle(e)
return t&&t.text},getLineHandle:function(e){if(Qe(this,e))return Ge(this,e)},getLineNumber:function(e){return Xe(e)},getLineHandleVisualStart:function(e){return"number"==typeof e&&(e=Ge(this,e)),Pt(e)},lineCount:function(){return this.size},firstLine:function(){return this.first},lastLine:function(){return this.first+this.size-1},clipPos:function(e){return lt(this,e)},getCursor:function(e){var t=this.sel.primary()
return null==e||"head"==e?t.head:"anchor"==e?t.anchor:"end"==e||"to"==e||!1===e?t.to():t.from()},listSelections:function(){return this.sel.ranges},somethingSelected:function(){return this.sel.somethingSelected()},setCursor:ri((function(e,t,r){Yi(this,lt(this,"number"==typeof e?et(e,t||0):e),null,r)})),setSelection:ri((function(e,t,r){Yi(this,lt(this,e),lt(this,t||e),r)})),extendSelection:ri((function(e,t,r){Ki(this,lt(this,e),t&&lt(this,t),r)})),extendSelections:ri((function(e,t){Zi(this,st(this,e),t)})),extendSelectionsBy:ri((function(e,t){Zi(this,st(this,Z(this.sel.ranges,e)),t)})),setSelections:ri((function(e,t,r){if(e.length){for(var n=[],i=0;i<e.length;i++)n[i]=new _i(lt(this,e[i].anchor),lt(this,e[i].head))
null==t&&(t=Math.min(e.length-1,this.sel.primIndex)),Ji(this,Ci(this.cm,n,t),r)}})),addSelection:ri((function(e,t,r){var n=this.sel.ranges.slice(0)
n.push(new _i(lt(this,e),lt(this,t||e))),Ji(this,Ci(this.cm,n,n.length-1),r)})),getSelection:function(e){for(var t,r=this.sel.ranges,n=0;n<r.length;n++){var i=Ve(this,r[n].from(),r[n].to())
t=t?t.concat(i):i}return!1===e?t:t.join(e||this.lineSeparator())},getSelections:function(e){for(var t=[],r=this.sel.ranges,n=0;n<r.length;n++){var i=Ve(this,r[n].from(),r[n].to())
!1!==e&&(i=i.join(e||this.lineSeparator())),t[n]=i}return t},replaceSelection:function(e,t,r){for(var n=[],i=0;i<this.sel.ranges.length;i++)n[i]=e
this.replaceSelections(n,t,r||"+input")},replaceSelections:ri((function(e,t,r){for(var n=[],i=this.sel,o=0;o<i.ranges.length;o++){var a=i.ranges[o]
n[o]={from:a.from(),to:a.to(),text:this.splitLines(e[o]),origin:r}}for(var l=t&&"end"!=t&&function(e,t,r){for(var n=[],i=et(e.first,0),o=i,a=0;a<t.length;a++){var l=t[a],s=zi(l.from,i,o),c=zi(Ti(l),i,o)
if(i=l.to,o=c,"around"==r){var u=e.sel.ranges[a],d=tt(u.head,u.anchor)<0
n[a]=new _i(d?c:s,d?s:c)}else n[a]=new _i(s,s)}return new ki(n,e.sel.primIndex)}(this,n,t),s=n.length-1;s>=0;s--)co(this,n[s])
l?Qi(this,l):this.cm&&En(this.cm)})),undo:ri((function(){fo(this,"undo")})),redo:ri((function(){fo(this,"redo")})),undoSelection:ri((function(){fo(this,"undo",!0)})),redoSelection:ri((function(){fo(this,"redo",!0)})),setExtending:function(e){this.extend=e},getExtending:function(){return this.extend},historySize:function(){for(var e=this.history,t=0,r=0,n=0;n<e.done.length;n++)e.done[n].ranges||++t
for(var i=0;i<e.undone.length;i++)e.undone[i].ranges||++r
return{undo:t,redo:r}},clearHistory:function(){var e=this
this.history=new Fi(this.history.maxGeneration),Oi(this,(function(t){return t.history=e.history}),!0)},markClean:function(){this.cleanGeneration=this.changeGeneration(!0)},changeGeneration:function(e){return e&&(this.history.lastOp=this.history.lastSelOp=this.history.lastOrigin=null),this.history.generation},isClean:function(e){return this.history.generation==(e||this.cleanGeneration)},getHistory:function(){return{done:Gi(this.history.done),undone:Gi(this.history.undone)}},setHistory:function(e){var t=this.history=new Fi(this.history.maxGeneration)
t.done=Gi(e.done.slice(0),null,!0),t.undone=Gi(e.undone.slice(0),null,!0)},setGutterMarker:ri((function(e,t,r){return bo(this,e,"gutter",(function(e){var n=e.gutterMarkers||(e.gutterMarkers={})
return n[t]=r,!r&&te(n)&&(e.gutterMarkers=null),!0}))})),clearGutter:ri((function(e){var t=this
this.iter((function(r){r.gutterMarkers&&r.gutterMarkers[e]&&bo(t,r,"gutter",(function(){return r.gutterMarkers[e]=null,te(r.gutterMarkers)&&(r.gutterMarkers=null),!0}))}))})),lineInfo:function(e){var t
if("number"==typeof e){if(!Qe(this,e))return null
if(t=e,!(e=Ge(this,e)))return null}else if(null==(t=Xe(e)))return null
return{line:t,handle:e,text:e.text,gutterMarkers:e.gutterMarkers,textClass:e.textClass,bgClass:e.bgClass,wrapClass:e.wrapClass,widgets:e.widgets}},addLineClass:ri((function(e,t,r){return bo(this,e,"gutter"==t?"gutter":"class",(function(e){var n="text"==t?"textClass":"background"==t?"bgClass":"gutter"==t?"gutterClass":"wrapClass"
if(e[n]){if(C(r).test(e[n]))return!1
e[n]+=" "+r}else e[n]=r
return!0}))})),removeLineClass:ri((function(e,t,r){return bo(this,e,"gutter"==t?"gutter":"class",(function(e){var n="text"==t?"textClass":"background"==t?"bgClass":"gutter"==t?"gutterClass":"wrapClass",i=e[n]
if(!i)return!1
if(null==r)e[n]=null
else{var o=i.match(C(r))
if(!o)return!1
var a=o.index+o[0].length
e[n]=i.slice(0,o.index)+(o.index&&a!=i.length?" ":"")+i.slice(a)||null}return!0}))})),addLineWidget:ri((function(e,t,r){return function(e,t,r,n){var i=new ko(e,r,n),o=e.cm
return o&&i.noHScroll&&(o.display.alignWidgets=!0),bo(e,t,"widget",(function(t){var r=t.widgets||(t.widgets=[])
if(null==i.insertAt?r.push(i):r.splice(Math.min(r.length-1,Math.max(0,i.insertAt)),0,i),i.line=t,o&&!$t(e,t)){var n=Ht(t)<e.scrollTop
Ze(t,t.height+xr(i)),n&&An(o,i.height),o.curOp.forceUpdate=!0}return!0})),o&&lr(o,"lineWidgetAdded",o,i,"number"==typeof t?t:Xe(t)),i}(this,e,t,r)})),removeLineWidget:function(e){e.clear()},markText:function(e,t,r){return To(this,lt(this,e),lt(this,t),r,r&&r.type||"range")},setBookmark:function(e,t){var r={replacedWith:t&&(null==t.nodeType?t.widget:t),insertLeft:t&&t.insertLeft,clearWhenEmpty:!1,shared:t&&t.shared,handleMouseEvents:t&&t.handleMouseEvents}
return To(this,e=lt(this,e),e,r,"bookmark")},findMarksAt:function(e){var t=[],r=Ge(this,(e=lt(this,e)).line).markedSpans
if(r)for(var n=0;n<r.length;++n){var i=r[n];(null==i.from||i.from<=e.ch)&&(null==i.to||i.to>=e.ch)&&t.push(i.marker.parent||i.marker)}return t},findMarks:function(e,t,r){e=lt(this,e),t=lt(this,t)
var n=[],i=e.line
return this.iter(e.line,t.line+1,(function(o){var a=o.markedSpans
if(a)for(var l=0;l<a.length;l++){var s=a[l]
null!=s.to&&i==e.line&&e.ch>=s.to||null==s.from&&i!=e.line||null!=s.from&&i==t.line&&s.from>=t.ch||r&&!r(s.marker)||n.push(s.marker.parent||s.marker)}++i})),n},getAllMarks:function(){var e=[]
return this.iter((function(t){var r=t.markedSpans
if(r)for(var n=0;n<r.length;++n)null!=r[n].from&&e.push(r[n].marker)})),e},posFromIndex:function(e){var t,r=this.first,n=this.lineSeparator().length
return this.iter((function(i){var o=i.text.length+n
if(o>e)return t=e,!0
e-=o,++r})),lt(this,et(r,t))},indexFromPos:function(e){var t=(e=lt(this,e)).ch
if(e.line<this.first||e.ch<0)return 0
var r=this.lineSeparator().length
return this.iter(this.first,e.line,(function(e){t+=e.text.length+r})),t},copy:function(e){var t=new Eo(Ke(this,this.first,this.first+this.size),this.modeOption,this.first,this.lineSep,this.direction)
return t.scrollTop=this.scrollTop,t.scrollLeft=this.scrollLeft,t.sel=this.sel,t.extend=!1,e&&(t.history.undoDepth=this.history.undoDepth,t.setHistory(this.getHistory())),t},linkedDoc:function(e){e||(e={})
var t=this.first,r=this.first+this.size
null!=e.from&&e.from>t&&(t=e.from),null!=e.to&&e.to<r&&(r=e.to)
var n=new Eo(Ke(this,t,r),e.mode||this.modeOption,t,this.lineSep,this.direction)
return e.sharedHist&&(n.history=this.history),(this.linked||(this.linked=[])).push({doc:n,sharedHist:e.sharedHist}),n.linked=[{doc:this,isParent:!0,sharedHist:e.sharedHist}],function(e,t){for(var r=0;r<t.length;r++){var n=t[r],i=n.find(),o=e.clipPos(i.from),a=e.clipPos(i.to)
if(tt(o,a)){var l=To(e,o,a,n.primary,n.primary.type)
n.markers.push(l),l.parent=n}}}(n,Lo(this)),n},unlinkDoc:function(e){if(e instanceof Ma&&(e=e.doc),this.linked)for(var t=0;t<this.linked.length;++t){if(this.linked[t].doc==e){this.linked.splice(t,1),e.unlinkDoc(this),zo(Lo(this))
break}}if(e.history==this.history){var r=[e.id]
Oi(e,(function(e){return r.push(e.id)}),!0),e.history=new Fi(null),e.history.done=Gi(this.history.done,r),e.history.undone=Gi(this.history.undone,r)}},iterLinkedDocs:function(e){Oi(this,e)},getMode:function(){return this.mode},getEditor:function(){return this.cm},splitLines:function(e){return this.lineSep?e.split(this.lineSep):Ee(e)},lineSeparator:function(){return this.lineSep||"\n"},setDirection:ri((function(e){var t;("rtl"!=e&&(e="ltr"),e!=this.direction)&&(this.direction=e,this.iter((function(e){return e.order=null})),this.cm&&Jn(t=this.cm,(function(){Di(t),dn(t)})))}))}),Eo.prototype.eachLine=Eo.prototype.iter
var No=0
function qo(e){var t=this
if(Oo(t),!me(t,e)&&!wr(t.display,e)){be(e),a&&(No=+new Date)
var r=cn(t,e,!0),n=e.dataTransfer.files
if(r&&!t.isReadOnly())if(n&&n.length&&window.FileReader&&window.File)for(var i=n.length,o=Array(i),l=0,s=function(){++l==i&&ei(t,(function(){var e={from:r=lt(t.doc,r),to:r,text:t.doc.splitLines(o.filter((function(e){return null!=e})).join(t.doc.lineSeparator())),origin:"paste"}
co(t.doc,e),Qi(t.doc,Si(lt(t.doc,r),lt(t.doc,Ti(e))))}))()},c=function(e,r){if(t.options.allowDropFileTypes&&-1==R(t.options.allowDropFileTypes,e.type))s()
else{var n=new FileReader
n.onerror=function(){return s()},n.onload=function(){var e=n.result;/[\x00-\x08\x0e-\x1f]{2}/.test(e)||(o[r]=e),s()},n.readAsText(e)}},u=0;u<n.length;u++)c(n[u],u)
else{if(t.state.draggingText&&t.doc.sel.contains(r)>-1)return t.state.draggingText(e),void setTimeout((function(){return t.display.input.focus()}),20)
try{var d=e.dataTransfer.getData("Text")
if(d){var f
if(t.state.draggingText&&!t.state.draggingText.copy&&(f=t.listSelections()),eo(t.doc,Si(r,r)),f)for(var p=0;p<f.length;++p)mo(t.doc,"",f[p].anchor,f[p].head,"drag")
t.replaceSelection(d,"around","paste"),t.display.input.focus()}}catch(e){}}}}function Oo(e){e.display.dragCursor&&(e.display.lineSpace.removeChild(e.display.dragCursor),e.display.dragCursor=null)}function Io(e){if(document.getElementsByClassName){for(var t=document.getElementsByClassName("CodeMirror"),r=[],n=0;n<t.length;n++){var i=t[n].CodeMirror
i&&r.push(i)}r.length&&r[0].operation((function(){for(var t=0;t<r.length;t++)e(r[t])}))}}var Do=!1
function Fo(){var e
Do||(de(window,"resize",(function(){null==e&&(e=setTimeout((function(){e=null,Io(Po)}),100))})),de(window,"blur",(function(){return Io(Sn)})),Do=!0)}function Po(e){var t=e.display
t.cachedCharWidth=t.cachedTextHeight=t.cachedPaddingH=null,t.scrollbarsClipped=!1,e.setSize()}for(var Wo={3:"Pause",8:"Backspace",9:"Tab",13:"Enter",16:"Shift",17:"Ctrl",18:"Alt",19:"Pause",20:"CapsLock",27:"Esc",32:"Space",33:"PageUp",34:"PageDown",35:"End",36:"Home",37:"Left",38:"Up",39:"Right",40:"Down",44:"PrintScrn",45:"Insert",46:"Delete",59:";",61:"=",91:"Mod",92:"Mod",93:"Mod",106:"*",107:"=",109:"-",110:".",111:"/",145:"ScrollLock",173:"-",186:";",187:"=",188:",",189:"-",190:".",191:"/",192:"`",219:"[",220:"\\",221:"]",222:"'",63232:"Up",63233:"Down",63234:"Left",63235:"Right",63272:"Delete",63273:"Home",63275:"End",63276:"PageUp",63277:"PageDown",63302:"Insert"},Ro=0;Ro<10;Ro++)Wo[Ro+48]=Wo[Ro+96]=String(Ro)
for(var $o=65;$o<=90;$o++)Wo[$o]=String.fromCharCode($o)
for(var jo=1;jo<=12;jo++)Wo[jo+111]=Wo[jo+63235]="F"+jo
var Ho={}
function Bo(e){var t,r,n,i,o=e.split(/-(?!$)/)
e=o[o.length-1]
for(var a=0;a<o.length-1;a++){var l=o[a]
if(/^(cmd|meta|m)$/i.test(l))i=!0
else if(/^a(lt)?$/i.test(l))t=!0
else if(/^(c|ctrl|control)$/i.test(l))r=!0
else{if(!/^s(hift)?$/i.test(l))throw new Error("Unrecognized modifier name: "+l)
n=!0}}return t&&(e="Alt-"+e),r&&(e="Ctrl-"+e),i&&(e="Cmd-"+e),n&&(e="Shift-"+e),e}function Uo(e){var t={}
for(var r in e)if(e.hasOwnProperty(r)){var n=e[r]
if(/^(name|fallthrough|(de|at)tach)$/.test(r))continue
if("..."==n){delete e[r]
continue}for(var i=Z(r.split(" "),Bo),o=0;o<i.length;o++){var a=void 0,l=void 0
o==i.length-1?(l=i.join(" "),a=n):(l=i.slice(0,o+1).join(" "),a="...")
var s=t[l]
if(s){if(s!=a)throw new Error("Inconsistent bindings for "+l)}else t[l]=a}delete e[r]}for(var c in t)e[c]=t[c]
return e}function Go(e,t,r,n){var i=(t=Xo(t)).call?t.call(e,n):t[e]
if(!1===i)return"nothing"
if("..."===i)return"multi"
if(null!=i&&r(i))return"handled"
if(t.fallthrough){if("[object Array]"!=Object.prototype.toString.call(t.fallthrough))return Go(e,t.fallthrough,r,n)
for(var o=0;o<t.fallthrough.length;o++){var a=Go(e,t.fallthrough[o],r,n)
if(a)return a}}}function Vo(e){var t="string"==typeof e?e:Wo[e.keyCode]
return"Ctrl"==t||"Alt"==t||"Shift"==t||"Mod"==t}function Ko(e,t,r){var n=e
return t.altKey&&"Alt"!=n&&(e="Alt-"+e),(k?t.metaKey:t.ctrlKey)&&"Ctrl"!=n&&(e="Ctrl-"+e),(k?t.ctrlKey:t.metaKey)&&"Cmd"!=n&&(e="Cmd-"+e),!r&&t.shiftKey&&"Shift"!=n&&(e="Shift-"+e),e}function Zo(e,t){if(d&&34==e.keyCode&&e.char)return!1
var r=Wo[e.keyCode]
return null!=r&&!e.altGraphKey&&(3==e.keyCode&&e.code&&(r=e.code),Ko(r,e,t))}function Xo(e){return"string"==typeof e?Ho[e]:e}function Yo(e,t){for(var r=e.doc.sel.ranges,n=[],i=0;i<r.length;i++){for(var o=t(r[i]);n.length&&tt(o.from,K(n).to)<=0;){var a=n.pop()
if(tt(a.from,o.from)<0){o.from=a.from
break}}n.push(o)}Jn(e,(function(){for(var t=n.length-1;t>=0;t--)mo(e.doc,"",n[t].from,n[t].to,"+delete")
En(e)}))}function Qo(e,t,r){var n=ie(e.text,t+r,r)
return n<0||n>e.text.length?null:n}function Jo(e,t,r){var n=Qo(e,t.ch,r)
return null==n?null:new et(t.line,n,r<0?"after":"before")}function ea(e,t,r,n,i){if(e){"rtl"==t.doc.direction&&(i=-i)
var o=ce(r,t.doc.direction)
if(o){var a,l=i<0?K(o):o[0],s=i<0==(1==l.level)?"after":"before"
if(l.level>0||"rtl"==t.doc.direction){var c=Er(t,r)
a=i<0?r.text.length-1:0
var u=Nr(t,c,a).top
a=oe((function(e){return Nr(t,c,e).top==u}),i<0==(1==l.level)?l.from:l.to-1,a),"before"==s&&(a=Qo(r,a,1))}else a=i<0?l.to:l.from
return new et(n,a,s)}}return new et(n,i<0?r.text.length:0,i<0?"before":"after")}Ho.basic={Left:"goCharLeft",Right:"goCharRight",Up:"goLineUp",Down:"goLineDown",End:"goLineEnd",Home:"goLineStartSmart",PageUp:"goPageUp",PageDown:"goPageDown",Delete:"delCharAfter",Backspace:"delCharBefore","Shift-Backspace":"delCharBefore",Tab:"defaultTab","Shift-Tab":"indentAuto",Enter:"newlineAndIndent",Insert:"toggleOverwrite",Esc:"singleSelection"},Ho.pcDefault={"Ctrl-A":"selectAll","Ctrl-D":"deleteLine","Ctrl-Z":"undo","Shift-Ctrl-Z":"redo","Ctrl-Y":"redo","Ctrl-Home":"goDocStart","Ctrl-End":"goDocEnd","Ctrl-Up":"goLineUp","Ctrl-Down":"goLineDown","Ctrl-Left":"goGroupLeft","Ctrl-Right":"goGroupRight","Alt-Left":"goLineStart","Alt-Right":"goLineEnd","Ctrl-Backspace":"delGroupBefore","Ctrl-Delete":"delGroupAfter","Ctrl-S":"save","Ctrl-F":"find","Ctrl-G":"findNext","Shift-Ctrl-G":"findPrev","Shift-Ctrl-F":"replace","Shift-Ctrl-R":"replaceAll","Ctrl-[":"indentLess","Ctrl-]":"indentMore","Ctrl-U":"undoSelection","Shift-Ctrl-U":"redoSelection","Alt-U":"redoSelection",fallthrough:"basic"},Ho.emacsy={"Ctrl-F":"goCharRight","Ctrl-B":"goCharLeft","Ctrl-P":"goLineUp","Ctrl-N":"goLineDown","Alt-F":"goWordRight","Alt-B":"goWordLeft","Ctrl-A":"goLineStart","Ctrl-E":"goLineEnd","Ctrl-V":"goPageDown","Shift-Ctrl-V":"goPageUp","Ctrl-D":"delCharAfter","Ctrl-H":"delCharBefore","Alt-D":"delWordAfter","Alt-Backspace":"delWordBefore","Ctrl-K":"killLine","Ctrl-T":"transposeChars","Ctrl-O":"openLine"},Ho.macDefault={"Cmd-A":"selectAll","Cmd-D":"deleteLine","Cmd-Z":"undo","Shift-Cmd-Z":"redo","Cmd-Y":"redo","Cmd-Home":"goDocStart","Cmd-Up":"goDocStart","Cmd-End":"goDocEnd","Cmd-Down":"goDocEnd","Alt-Left":"goGroupLeft","Alt-Right":"goGroupRight","Cmd-Left":"goLineLeft","Cmd-Right":"goLineRight","Alt-Backspace":"delGroupBefore","Ctrl-Alt-Backspace":"delGroupAfter","Alt-Delete":"delGroupAfter","Cmd-S":"save","Cmd-F":"find","Cmd-G":"findNext","Shift-Cmd-G":"findPrev","Cmd-Alt-F":"replace","Shift-Cmd-Alt-F":"replaceAll","Cmd-[":"indentLess","Cmd-]":"indentMore","Cmd-Backspace":"delWrappedLineLeft","Cmd-Delete":"delWrappedLineRight","Cmd-U":"undoSelection","Shift-Cmd-U":"redoSelection","Ctrl-Up":"goDocStart","Ctrl-Down":"goDocEnd",fallthrough:["basic","emacsy"]},Ho.default=y?Ho.macDefault:Ho.pcDefault
var ta={selectAll:lo,singleSelection:function(e){return e.setSelection(e.getCursor("anchor"),e.getCursor("head"),j)},killLine:function(e){return Yo(e,(function(t){if(t.empty()){var r=Ge(e.doc,t.head.line).text.length
return t.head.ch==r&&t.head.line<e.lastLine()?{from:t.head,to:et(t.head.line+1,0)}:{from:t.head,to:et(t.head.line,r)}}return{from:t.from(),to:t.to()}}))},deleteLine:function(e){return Yo(e,(function(t){return{from:et(t.from().line,0),to:lt(e.doc,et(t.to().line+1,0))}}))},delLineLeft:function(e){return Yo(e,(function(e){return{from:et(e.from().line,0),to:e.from()}}))},delWrappedLineLeft:function(e){return Yo(e,(function(t){var r=e.charCoords(t.head,"div").top+5
return{from:e.coordsChar({left:0,top:r},"div"),to:t.from()}}))},delWrappedLineRight:function(e){return Yo(e,(function(t){var r=e.charCoords(t.head,"div").top+5,n=e.coordsChar({left:e.display.lineDiv.offsetWidth+100,top:r},"div")
return{from:t.from(),to:n}}))},undo:function(e){return e.undo()},redo:function(e){return e.redo()},undoSelection:function(e){return e.undoSelection()},redoSelection:function(e){return e.redoSelection()},goDocStart:function(e){return e.extendSelection(et(e.firstLine(),0))},goDocEnd:function(e){return e.extendSelection(et(e.lastLine()))},goLineStart:function(e){return e.extendSelectionsBy((function(t){return ra(e,t.head.line)}),{origin:"+move",bias:1})},goLineStartSmart:function(e){return e.extendSelectionsBy((function(t){return na(e,t.head)}),{origin:"+move",bias:1})},goLineEnd:function(e){return e.extendSelectionsBy((function(t){return function(e,t){var r=Ge(e.doc,t),n=function(e){for(var t;t=It(e);)e=t.find(1,!0).line
return e}(r)
n!=r&&(t=Xe(n))
return ea(!0,e,r,t,-1)}(e,t.head.line)}),{origin:"+move",bias:-1})},goLineRight:function(e){return e.extendSelectionsBy((function(t){var r=e.cursorCoords(t.head,"div").top+5
return e.coordsChar({left:e.display.lineDiv.offsetWidth+100,top:r},"div")}),B)},goLineLeft:function(e){return e.extendSelectionsBy((function(t){var r=e.cursorCoords(t.head,"div").top+5
return e.coordsChar({left:0,top:r},"div")}),B)},goLineLeftSmart:function(e){return e.extendSelectionsBy((function(t){var r=e.cursorCoords(t.head,"div").top+5,n=e.coordsChar({left:0,top:r},"div")
return n.ch<e.getLine(n.line).search(/\S/)?na(e,t.head):n}),B)},goLineUp:function(e){return e.moveV(-1,"line")},goLineDown:function(e){return e.moveV(1,"line")},goPageUp:function(e){return e.moveV(-1,"page")},goPageDown:function(e){return e.moveV(1,"page")},goCharLeft:function(e){return e.moveH(-1,"char")},goCharRight:function(e){return e.moveH(1,"char")},goColumnLeft:function(e){return e.moveH(-1,"column")},goColumnRight:function(e){return e.moveH(1,"column")},goWordLeft:function(e){return e.moveH(-1,"word")},goGroupRight:function(e){return e.moveH(1,"group")},goGroupLeft:function(e){return e.moveH(-1,"group")},goWordRight:function(e){return e.moveH(1,"word")},delCharBefore:function(e){return e.deleteH(-1,"char")},delCharAfter:function(e){return e.deleteH(1,"char")},delWordBefore:function(e){return e.deleteH(-1,"word")},delWordAfter:function(e){return e.deleteH(1,"word")},delGroupBefore:function(e){return e.deleteH(-1,"group")},delGroupAfter:function(e){return e.deleteH(1,"group")},indentAuto:function(e){return e.indentSelection("smart")},indentMore:function(e){return e.indentSelection("add")},indentLess:function(e){return e.indentSelection("subtract")},insertTab:function(e){return e.replaceSelection("\t")},insertSoftTab:function(e){for(var t=[],r=e.listSelections(),n=e.options.tabSize,i=0;i<r.length;i++){var o=r[i].from(),a=P(e.getLine(o.line),o.ch,n)
t.push(V(n-a%n))}e.replaceSelections(t)},defaultTab:function(e){e.somethingSelected()?e.indentSelection("add"):e.execCommand("insertTab")},transposeChars:function(e){return Jn(e,(function(){for(var t=e.listSelections(),r=[],n=0;n<t.length;n++)if(t[n].empty()){var i=t[n].head,o=Ge(e.doc,i.line).text
if(o)if(i.ch==o.length&&(i=new et(i.line,i.ch-1)),i.ch>0)i=new et(i.line,i.ch+1),e.replaceRange(o.charAt(i.ch-1)+o.charAt(i.ch-2),et(i.line,i.ch-2),i,"+transpose")
else if(i.line>e.doc.first){var a=Ge(e.doc,i.line-1).text
a&&(i=new et(i.line,1),e.replaceRange(o.charAt(0)+e.doc.lineSeparator()+a.charAt(a.length-1),et(i.line-1,a.length-1),i,"+transpose"))}r.push(new _i(i,i))}e.setSelections(r)}))},newlineAndIndent:function(e){return Jn(e,(function(){for(var t=e.listSelections(),r=t.length-1;r>=0;r--)e.replaceRange(e.doc.lineSeparator(),t[r].anchor,t[r].head,"+input")
t=e.listSelections()
for(var n=0;n<t.length;n++)e.indentLine(t[n].from().line,null,!0)
En(e)}))},openLine:function(e){return e.replaceSelection("\n","start")},toggleOverwrite:function(e){return e.toggleOverwrite()}}
function ra(e,t){var r=Ge(e.doc,t),n=Pt(r)
return n!=r&&(t=Xe(n)),ea(!0,e,n,t,1)}function na(e,t){var r=ra(e,t.line),n=Ge(e.doc,r.line),i=ce(n,e.doc.direction)
if(!i||0==i[0].level){var o=Math.max(r.ch,n.text.search(/\S/)),a=t.line==r.line&&t.ch<=o&&t.ch
return et(r.line,a?0:o,r.sticky)}return r}function ia(e,t,r){if("string"==typeof t&&!(t=ta[t]))return!1
e.display.input.ensurePolled()
var n=e.display.shift,i=!1
try{e.isReadOnly()&&(e.state.suppressEdits=!0),r&&(e.display.shift=!1),i=t(e)!=$}finally{e.display.shift=n,e.state.suppressEdits=!1}return i}var oa=new W
function aa(e,t,r,n){var i=e.state.keySeq
if(i){if(Vo(t))return"handled"
if(/\'$/.test(t)?e.state.keySeq=null:oa.set(50,(function(){e.state.keySeq==i&&(e.state.keySeq=null,e.display.input.reset())})),la(e,i+" "+t,r,n))return!0}return la(e,t,r,n)}function la(e,t,r,n){var i=function(e,t,r){for(var n=0;n<e.state.keyMaps.length;n++){var i=Go(t,e.state.keyMaps[n],r,e)
if(i)return i}return e.options.extraKeys&&Go(t,e.options.extraKeys,r,e)||Go(t,e.options.keyMap,r,e)}(e,t,n)
return"multi"==i&&(e.state.keySeq=t),"handled"==i&&lr(e,"keyHandled",e,t,r),"handled"!=i&&"multi"!=i||(be(r),wn(e)),!!i}function sa(e,t){var r=Zo(t,!0)
return!!r&&(t.shiftKey&&!e.state.keySeq?aa(e,"Shift-"+r,t,(function(t){return ia(e,t,!0)}))||aa(e,r,t,(function(t){if("string"==typeof t?/^go[A-Z]/.test(t):t.motion)return ia(e,t)})):aa(e,r,t,(function(t){return ia(e,t)})))}var ca=null
function ua(e){var t=this
if(t.curOp.focus=N(),!me(t,e)){a&&l<11&&27==e.keyCode&&(e.returnValue=!1)
var n=e.keyCode
t.display.shift=16==n||e.shiftKey
var i=sa(t,e)
d&&(ca=i?n:null,i||88!=n||qe||!(y?e.metaKey:e.ctrlKey)||t.replaceSelection("",null,"cut")),r&&!y&&!i&&46==n&&e.shiftKey&&!e.ctrlKey&&document.execCommand&&document.execCommand("cut"),18!=n||/\bCodeMirror-crosshair\b/.test(t.display.lineDiv.className)||function(e){var t=e.display.lineDiv
function r(e){18!=e.keyCode&&e.altKey||(T(t,"CodeMirror-crosshair"),pe(document,"keyup",r),pe(document,"mouseover",r))}q(t,"CodeMirror-crosshair"),de(document,"keyup",r),de(document,"mouseover",r)}(t)}}function da(e){16==e.keyCode&&(this.doc.sel.shift=!1),me(this,e)}function fa(e){var t=this
if(!(wr(t.display,e)||me(t,e)||e.ctrlKey&&!e.altKey||y&&e.metaKey)){var r=e.keyCode,n=e.charCode
if(d&&r==ca)return ca=null,void be(e)
if(!d||e.which&&!(e.which<10)||!sa(t,e)){var i=String.fromCharCode(null==n?r:n)
"\b"!=i&&(function(e,t,r){return aa(e,"'"+r+"'",t,(function(t){return ia(e,t,!0)}))}(t,e,i)||t.display.input.onKeyPress(e))}}}var pa,ha,ma=function(e,t,r){this.time=e,this.pos=t,this.button=r}
function ga(e){var t=this,r=t.display
if(!(me(t,e)||r.activeTouch&&r.input.supportsTouch()))if(r.input.ensurePolled(),r.shift=e.shiftKey,wr(r,e))s||(r.scroller.draggable=!1,setTimeout((function(){return r.scroller.draggable=!0}),100))
else if(!ba(t,e)){var n=cn(t,e),i=Ce(e),o=n?function(e,t){var r=+new Date
return ha&&ha.compare(r,e,t)?(pa=ha=null,"triple"):pa&&pa.compare(r,e,t)?(ha=new ma(r,e,t),pa=null,"double"):(pa=new ma(r,e,t),ha=null,"single")}(n,i):"single"
window.focus(),1==i&&t.state.selectingText&&t.state.selectingText(e),n&&function(e,t,r,n,i){var o="Click"
"double"==n?o="Double"+o:"triple"==n&&(o="Triple"+o)
return aa(e,Ko(o=(1==t?"Left":2==t?"Middle":"Right")+o,i),i,(function(t){if("string"==typeof t&&(t=ta[t]),!t)return!1
var n=!1
try{e.isReadOnly()&&(e.state.suppressEdits=!0),n=t(e,r)!=$}finally{e.state.suppressEdits=!1}return n}))}(t,i,n,o,e)||(1==i?n?function(e,t,r,n){a?setTimeout(D(kn,e),0):e.curOp.focus=N()
var i,o=function(e,t,r){var n=e.getOption("configureMouse"),i=n?n(e,t,r):{}
if(null==i.unit){var o=b?r.shiftKey&&r.metaKey:r.altKey
i.unit=o?"rectangle":"single"==t?"char":"double"==t?"word":"line"}(null==i.extend||e.doc.extend)&&(i.extend=e.doc.extend||r.shiftKey)
null==i.addNew&&(i.addNew=y?r.metaKey:r.ctrlKey)
null==i.moveOnDrag&&(i.moveOnDrag=!(y?r.altKey:r.ctrlKey))
return i}(e,r,n),c=e.doc.sel
e.options.dragDrop&&Me&&!e.isReadOnly()&&"single"==r&&(i=c.contains(t))>-1&&(tt((i=c.ranges[i]).from(),t)<0||t.xRel>0)&&(tt(i.to(),t)>0||t.xRel<0)?function(e,t,r,n){var i=e.display,o=!1,c=ei(e,(function(t){s&&(i.scroller.draggable=!1),e.state.draggingText=!1,pe(i.wrapper.ownerDocument,"mouseup",c),pe(i.wrapper.ownerDocument,"mousemove",u),pe(i.scroller,"dragstart",d),pe(i.scroller,"drop",c),o||(be(t),n.addNew||Ki(e.doc,r,null,null,n.extend),s||a&&9==l?setTimeout((function(){i.wrapper.ownerDocument.body.focus(),i.input.focus()}),20):i.input.focus())})),u=function(e){o=o||Math.abs(t.clientX-e.clientX)+Math.abs(t.clientY-e.clientY)>=10},d=function(){return o=!0}
s&&(i.scroller.draggable=!0)
e.state.draggingText=c,c.copy=!n.moveOnDrag,i.scroller.dragDrop&&i.scroller.dragDrop()
de(i.wrapper.ownerDocument,"mouseup",c),de(i.wrapper.ownerDocument,"mousemove",u),de(i.scroller,"dragstart",d),de(i.scroller,"drop",c),_n(e),setTimeout((function(){return i.input.focus()}),20)}(e,n,t,o):function(e,t,r,n){var i=e.display,o=e.doc
be(t)
var a,l,s=o.sel,c=s.ranges
n.addNew&&!n.extend?(l=o.sel.contains(r),a=l>-1?c[l]:new _i(r,r)):(a=o.sel.primary(),l=o.sel.primIndex)
if("rectangle"==n.unit)n.addNew||(a=new _i(r,r)),r=cn(e,t,!0,!0),l=-1
else{var u=va(e,r,n.unit)
a=n.extend?Vi(a,u.anchor,u.head,n.extend):u}n.addNew?-1==l?(l=c.length,Ji(o,Ci(e,c.concat([a]),l),{scroll:!1,origin:"*mouse"})):c.length>1&&c[l].empty()&&"char"==n.unit&&!n.extend?(Ji(o,Ci(e,c.slice(0,l).concat(c.slice(l+1)),0),{scroll:!1,origin:"*mouse"}),s=o.sel):Xi(o,l,a,H):(l=0,Ji(o,new ki([a],0),H),s=o.sel)
var d=r
function f(t){if(0!=tt(d,t))if(d=t,"rectangle"==n.unit){for(var i=[],c=e.options.tabSize,u=P(Ge(o,r.line).text,r.ch,c),f=P(Ge(o,t.line).text,t.ch,c),p=Math.min(u,f),h=Math.max(u,f),m=Math.min(r.line,t.line),g=Math.min(e.lastLine(),Math.max(r.line,t.line));m<=g;m++){var v=Ge(o,m).text,y=U(v,p,c)
p==h?i.push(new _i(et(m,y),et(m,y))):v.length>y&&i.push(new _i(et(m,y),et(m,U(v,h,c))))}i.length||i.push(new _i(r,r)),Ji(o,Ci(e,s.ranges.slice(0,l).concat(i),l),{origin:"*mouse",scroll:!1}),e.scrollIntoView(t)}else{var b,x=a,w=va(e,t,n.unit),k=x.anchor
tt(w.anchor,k)>0?(b=w.head,k=ot(x.from(),w.anchor)):(b=w.anchor,k=it(x.to(),w.head))
var _=s.ranges.slice(0)
_[l]=function(e,t){var r=t.anchor,n=t.head,i=Ge(e.doc,r.line)
if(0==tt(r,n)&&r.sticky==n.sticky)return t
var o=ce(i)
if(!o)return t
var a=le(o,r.ch,r.sticky),l=o[a]
if(l.from!=r.ch&&l.to!=r.ch)return t
var s,c=a+(l.from==r.ch==(1!=l.level)?0:1)
if(0==c||c==o.length)return t
if(n.line!=r.line)s=(n.line-r.line)*("ltr"==e.doc.direction?1:-1)>0
else{var u=le(o,n.ch,n.sticky),d=u-a||(n.ch-r.ch)*(1==l.level?-1:1)
s=u==c-1||u==c?d<0:d>0}var f=o[c+(s?-1:0)],p=s==(1==f.level),h=p?f.from:f.to,m=p?"after":"before"
return r.ch==h&&r.sticky==m?t:new _i(new et(r.line,h,m),n)}(e,new _i(lt(o,k),b)),Ji(o,Ci(e,_,l),H)}}var p=i.wrapper.getBoundingClientRect(),h=0
function m(t){var r=++h,a=cn(e,t,!0,"rectangle"==n.unit)
if(a)if(0!=tt(a,d)){e.curOp.focus=N(),f(a)
var l=Ln(i,o);(a.line>=l.to||a.line<l.from)&&setTimeout(ei(e,(function(){h==r&&m(t)})),150)}else{var s=t.clientY<p.top?-20:t.clientY>p.bottom?20:0
s&&setTimeout(ei(e,(function(){h==r&&(i.scroller.scrollTop+=s,m(t))})),50)}}function g(t){e.state.selectingText=!1,h=1/0,t&&(be(t),i.input.focus()),pe(i.wrapper.ownerDocument,"mousemove",v),pe(i.wrapper.ownerDocument,"mouseup",y),o.history.lastSelOrigin=null}var v=ei(e,(function(e){0!==e.buttons&&Ce(e)?m(e):g(e)})),y=ei(e,g)
e.state.selectingText=y,de(i.wrapper.ownerDocument,"mousemove",v),de(i.wrapper.ownerDocument,"mouseup",y)}(e,n,t,o)}(t,n,o,e):_e(e)==r.scroller&&be(e):2==i?(n&&Ki(t.doc,n),setTimeout((function(){return r.input.focus()}),20)):3==i&&(_?t.display.input.onContextMenu(e):_n(t)))}}function va(e,t,r){if("char"==r)return new _i(t,t)
if("word"==r)return e.findWordAt(t)
if("line"==r)return new _i(et(t.line,0),lt(e.doc,et(t.line+1,0)))
var n=r(e,t)
return new _i(n.from,n.to)}function ya(e,t,r,n){var i,o
if(t.touches)i=t.touches[0].clientX,o=t.touches[0].clientY
else try{i=t.clientX,o=t.clientY}catch(t){return!1}if(i>=Math.floor(e.display.gutters.getBoundingClientRect().right))return!1
n&&be(t)
var a=e.display,l=a.lineDiv.getBoundingClientRect()
if(o>l.bottom||!ve(e,r))return we(t)
o-=l.top-a.viewOffset
for(var s=0;s<e.display.gutterSpecs.length;++s){var c=a.gutters.childNodes[s]
if(c&&c.getBoundingClientRect().right>=i)return he(e,r,e,Ye(e.doc,o),e.display.gutterSpecs[s].className,t),we(t)}}function ba(e,t){return ya(e,t,"gutterClick",!0)}function xa(e,t){wr(e.display,t)||function(e,t){if(!ve(e,"gutterContextMenu"))return!1
return ya(e,t,"gutterContextMenu",!1)}(e,t)||me(e,t,"contextmenu")||_||e.display.input.onContextMenu(t)}function wa(e){e.display.wrapper.className=e.display.wrapper.className.replace(/\s*cm-s-\S+/g,"")+e.options.theme.replace(/(^|\s)\s*/g," cm-s-"),Wr(e)}ma.prototype.compare=function(e,t,r){return this.time+400>e&&0==tt(t,this.pos)&&r==this.button}
var ka={toString:function(){return"CodeMirror.Init"}},_a={},Ca={}
function Sa(e,t,r){if(!t!=!(r&&r!=ka)){var n=e.display.dragFunctions,i=t?de:pe
i(e.display.scroller,"dragstart",n.start),i(e.display.scroller,"dragenter",n.enter),i(e.display.scroller,"dragover",n.over),i(e.display.scroller,"dragleave",n.leave),i(e.display.scroller,"drop",n.drop)}}function Ta(e){e.options.lineWrapping?(q(e.display.wrapper,"CodeMirror-wrap"),e.display.sizer.style.minWidth="",e.display.sizerWidth=null):(T(e.display.wrapper,"CodeMirror-wrap"),Ut(e)),sn(e),dn(e),Wr(e),setTimeout((function(){return $n(e)}),100)}function Ma(e,t){var r=this
if(!(this instanceof Ma))return new Ma(e,t)
this.options=t=t?F(t):{},F(_a,t,!1)
var n=t.value
"string"==typeof n?n=new Eo(n,t.mode,null,t.lineSeparator,t.direction):t.mode&&(n.modeOption=t.mode),this.doc=n
var i=new Ma.inputStyles[t.inputStyle](this),o=this.display=new gi(e,n,i,t)
for(var c in o.wrapper.CodeMirror=this,wa(this),t.lineWrapping&&(this.display.wrapper.className+=" CodeMirror-wrap"),Bn(this),this.state={keyMaps:[],overlays:[],modeGen:0,overwrite:!1,delayingBlurEvent:!1,focused:!1,suppressEdits:!1,pasteIncoming:-1,cutIncoming:-1,selectingText:!1,draggingText:!1,highlight:new W,keySeq:null,specialChars:null},t.autofocus&&!v&&o.input.focus(),a&&l<11&&setTimeout((function(){return r.display.input.reset(!0)}),20),function(e){var t=e.display
de(t.scroller,"mousedown",ei(e,ga)),de(t.scroller,"dblclick",a&&l<11?ei(e,(function(t){if(!me(e,t)){var r=cn(e,t)
if(r&&!ba(e,t)&&!wr(e.display,t)){be(t)
var n=e.findWordAt(r)
Ki(e.doc,n.anchor,n.head)}}})):function(t){return me(e,t)||be(t)})
de(t.scroller,"contextmenu",(function(t){return xa(e,t)})),de(t.input.getField(),"contextmenu",(function(r){t.scroller.contains(r.target)||xa(e,r)}))
var r,n={end:0}
function i(){t.activeTouch&&(r=setTimeout((function(){return t.activeTouch=null}),1e3),(n=t.activeTouch).end=+new Date)}function o(e){if(1!=e.touches.length)return!1
var t=e.touches[0]
return t.radiusX<=1&&t.radiusY<=1}function s(e,t){if(null==t.left)return!0
var r=t.left-e.left,n=t.top-e.top
return r*r+n*n>400}de(t.scroller,"touchstart",(function(i){if(!me(e,i)&&!o(i)&&!ba(e,i)){t.input.ensurePolled(),clearTimeout(r)
var a=+new Date
t.activeTouch={start:a,moved:!1,prev:a-n.end<=300?n:null},1==i.touches.length&&(t.activeTouch.left=i.touches[0].pageX,t.activeTouch.top=i.touches[0].pageY)}})),de(t.scroller,"touchmove",(function(){t.activeTouch&&(t.activeTouch.moved=!0)})),de(t.scroller,"touchend",(function(r){var n=t.activeTouch
if(n&&!wr(t,r)&&null!=n.left&&!n.moved&&new Date-n.start<300){var o,a=e.coordsChar(t.activeTouch,"page")
o=!n.prev||s(n,n.prev)?new _i(a,a):!n.prev.prev||s(n,n.prev.prev)?e.findWordAt(a):new _i(et(a.line,0),lt(e.doc,et(a.line+1,0))),e.setSelection(o.anchor,o.head),e.focus(),be(r)}i()})),de(t.scroller,"touchcancel",i),de(t.scroller,"scroll",(function(){t.scroller.clientHeight&&(In(e,t.scroller.scrollTop),Fn(e,t.scroller.scrollLeft,!0),he(e,"scroll",e))})),de(t.scroller,"mousewheel",(function(t){return wi(e,t)})),de(t.scroller,"DOMMouseScroll",(function(t){return wi(e,t)})),de(t.wrapper,"scroll",(function(){return t.wrapper.scrollTop=t.wrapper.scrollLeft=0})),t.dragFunctions={enter:function(t){me(e,t)||ke(t)},over:function(t){me(e,t)||(function(e,t){var r=cn(e,t)
if(r){var n=document.createDocumentFragment()
yn(e,r,n),e.display.dragCursor||(e.display.dragCursor=z("div",null,"CodeMirror-cursors CodeMirror-dragcursors"),e.display.lineSpace.insertBefore(e.display.dragCursor,e.display.cursorDiv)),L(e.display.dragCursor,n)}}(e,t),ke(t))},start:function(t){return function(e,t){if(a&&(!e.state.draggingText||+new Date-No<100))ke(t)
else if(!me(e,t)&&!wr(e.display,t)&&(t.dataTransfer.setData("Text",e.getSelection()),t.dataTransfer.effectAllowed="copyMove",t.dataTransfer.setDragImage&&!f)){var r=z("img",null,null,"position: fixed; left: 0; top: 0;")
r.src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",d&&(r.width=r.height=1,e.display.wrapper.appendChild(r),r._top=r.offsetTop),t.dataTransfer.setDragImage(r,0,0),d&&r.parentNode.removeChild(r)}}(e,t)},drop:ei(e,qo),leave:function(t){me(e,t)||Oo(e)}}
var c=t.input.getField()
de(c,"keyup",(function(t){return da.call(e,t)})),de(c,"keydown",ei(e,ua)),de(c,"keypress",ei(e,fa)),de(c,"focus",(function(t){return Cn(e,t)})),de(c,"blur",(function(t){return Sn(e,t)}))}(this),Fo(),Gn(this),this.curOp.forceUpdate=!0,Ii(this,n),t.autofocus&&!v||this.hasFocus()?setTimeout(D(Cn,this),20):Sn(this),Ca)Ca.hasOwnProperty(c)&&Ca[c](this,t[c],ka)
fi(this),t.finishInit&&t.finishInit(this)
for(var u=0;u<La.length;++u)La[u](this)
Vn(this),s&&t.lineWrapping&&"optimizelegibility"==getComputedStyle(o.lineDiv).textRendering&&(o.lineDiv.style.textRendering="auto")}Ma.defaults=_a,Ma.optionHandlers=Ca
var La=[]
function za(e,t,r,n){var i,o=e.doc
null==r&&(r="add"),"smart"==r&&(o.mode.indent?i=pt(e,t).state:r="prev")
var a=e.options.tabSize,l=Ge(o,t),s=P(l.text,null,a)
l.stateAfter&&(l.stateAfter=null)
var c,u=l.text.match(/^\s*/)[0]
if(n||/\S/.test(l.text)){if("smart"==r&&((c=o.mode.indent(i,l.text.slice(u.length),l.text))==$||c>150)){if(!n)return
r="prev"}}else c=0,r="not"
"prev"==r?c=t>o.first?P(Ge(o,t-1).text,null,a):0:"add"==r?c=s+e.options.indentUnit:"subtract"==r?c=s-e.options.indentUnit:"number"==typeof r&&(c=s+r),c=Math.max(0,c)
var d="",f=0
if(e.options.indentWithTabs)for(var p=Math.floor(c/a);p;--p)f+=a,d+="\t"
if(f<c&&(d+=V(c-f)),d!=u)return mo(o,d,et(t,0),et(t,u.length),"+input"),l.stateAfter=null,!0
for(var h=0;h<o.sel.ranges.length;h++){var m=o.sel.ranges[h]
if(m.head.line==t&&m.head.ch<u.length){var g=et(t,u.length)
Xi(o,h,new _i(g,g))
break}}}Ma.defineInitHook=function(e){return La.push(e)}
var Aa=null
function Ea(e){Aa=e}function Na(e,t,r,n,i){var o=e.doc
e.display.shift=!1,n||(n=o.sel)
var a=+new Date-200,l="paste"==i||e.state.pasteIncoming>a,s=Ee(t),c=null
if(l&&n.ranges.length>1)if(Aa&&Aa.text.join("\n")==t){if(n.ranges.length%Aa.text.length==0){c=[]
for(var u=0;u<Aa.text.length;u++)c.push(o.splitLines(Aa.text[u]))}}else s.length==n.ranges.length&&e.options.pasteLinesPerSelection&&(c=Z(s,(function(e){return[e]})))
for(var d=e.curOp.updateInput,f=n.ranges.length-1;f>=0;f--){var p=n.ranges[f],h=p.from(),m=p.to()
p.empty()&&(r&&r>0?h=et(h.line,h.ch-r):e.state.overwrite&&!l?m=et(m.line,Math.min(Ge(o,m.line).text.length,m.ch+K(s).length)):l&&Aa&&Aa.lineWise&&Aa.text.join("\n")==t&&(h=m=et(h.line,0)))
var g={from:h,to:m,text:c?c[f%c.length]:s,origin:i||(l?"paste":e.state.cutIncoming>a?"cut":"+input")}
co(e.doc,g),lr(e,"inputRead",e,g)}t&&!l&&Oa(e,t),En(e),e.curOp.updateInput<2&&(e.curOp.updateInput=d),e.curOp.typing=!0,e.state.pasteIncoming=e.state.cutIncoming=-1}function qa(e,t){var r=e.clipboardData&&e.clipboardData.getData("Text")
if(r)return e.preventDefault(),t.isReadOnly()||t.options.disableInput||Jn(t,(function(){return Na(t,r,0,null,"paste")})),!0}function Oa(e,t){if(e.options.electricChars&&e.options.smartIndent)for(var r=e.doc.sel,n=r.ranges.length-1;n>=0;n--){var i=r.ranges[n]
if(!(i.head.ch>100||n&&r.ranges[n-1].head.line==i.head.line)){var o=e.getModeAt(i.head),a=!1
if(o.electricChars){for(var l=0;l<o.electricChars.length;l++)if(t.indexOf(o.electricChars.charAt(l))>-1){a=za(e,i.head.line,"smart")
break}}else o.electricInput&&o.electricInput.test(Ge(e.doc,i.head.line).text.slice(0,i.head.ch))&&(a=za(e,i.head.line,"smart"))
a&&lr(e,"electricInput",e,i.head.line)}}}function Ia(e){for(var t=[],r=[],n=0;n<e.doc.sel.ranges.length;n++){var i=e.doc.sel.ranges[n].head.line,o={anchor:et(i,0),head:et(i+1,0)}
r.push(o),t.push(e.getRange(o.anchor,o.head))}return{text:t,ranges:r}}function Da(e,t,r,n){e.setAttribute("autocorrect",r?"":"off"),e.setAttribute("autocapitalize",n?"":"off"),e.setAttribute("spellcheck",!!t)}function Fa(){var e=z("textarea",null,null,"position: absolute; bottom: -1em; padding: 0; width: 1px; height: 1em; outline: none"),t=z("div",[e],null,"overflow: hidden; position: relative; width: 3px; height: 0px;")
return s?e.style.width="1000px":e.setAttribute("wrap","off"),m&&(e.style.border="1px solid black"),Da(e),t}function Pa(e,t,r,n,i){var o=t,a=r,l=Ge(e,t.line),s=i&&"rtl"==e.direction?-r:r
function c(n){var o,a
if(null==(o=i?function(e,t,r,n){var i=ce(t,e.doc.direction)
if(!i)return Jo(t,r,n)
r.ch>=t.text.length?(r.ch=t.text.length,r.sticky="before"):r.ch<=0&&(r.ch=0,r.sticky="after")
var o=le(i,r.ch,r.sticky),a=i[o]
if("ltr"==e.doc.direction&&a.level%2==0&&(n>0?a.to>r.ch:a.from<r.ch))return Jo(t,r,n)
var l,s=function(e,r){return Qo(t,e instanceof et?e.ch:e,r)},c=function(r){return e.options.lineWrapping?(l=l||Er(e,t),Yr(e,t,l,r)):{begin:0,end:t.text.length}},u=c("before"==r.sticky?s(r,-1):r.ch)
if("rtl"==e.doc.direction||1==a.level){var d=1==a.level==n<0,f=s(r,d?1:-1)
if(null!=f&&(d?f<=a.to&&f<=u.end:f>=a.from&&f>=u.begin)){var p=d?"before":"after"
return new et(r.line,f,p)}}var h=function(e,t,n){for(var o=function(e,t){return t?new et(r.line,s(e,1),"before"):new et(r.line,e,"after")};e>=0&&e<i.length;e+=t){var a=i[e],l=t>0==(1!=a.level),c=l?n.begin:s(n.end,-1)
if(a.from<=c&&c<a.to)return o(c,l)
if(c=l?a.from:s(a.to,-1),n.begin<=c&&c<n.end)return o(c,l)}},m=h(o+n,n,u)
if(m)return m
var g=n>0?u.end:s(u.begin,-1)
return null==g||n>0&&g==t.text.length||!(m=h(n>0?0:i.length-1,n,c(g)))?null:m}(e.cm,l,t,r):Jo(l,t,r))){if(n||(a=t.line+s)<e.first||a>=e.first+e.size||(t=new et(a,t.ch,t.sticky),!(l=Ge(e,a))))return!1
t=ea(i,e.cm,l,t.line,s)}else t=o
return!0}if("char"==n)c()
else if("column"==n)c(!0)
else if("word"==n||"group"==n)for(var u=null,d="group"==n,f=e.cm&&e.cm.getHelper(t,"wordChars"),p=!0;!(r<0)||c(!p);p=!1){var h=l.text.charAt(t.ch)||"\n",m=ee(h,f)?"w":d&&"\n"==h?"n":!d||/\s/.test(h)?null:"p"
if(!d||p||m||(m="s"),u&&u!=m){r<0&&(r=1,c(),t.sticky="after")
break}if(m&&(u=m),r>0&&!c(!p))break}var g=oo(e,t,o,a,!0)
return rt(o,g)&&(g.hitSide=!0),g}function Wa(e,t,r,n){var i,o,a=e.doc,l=t.left
if("page"==n){var s=Math.min(e.display.wrapper.clientHeight,window.innerHeight||document.documentElement.clientHeight),c=Math.max(s-.5*rn(e.display),3)
i=(r>0?t.bottom:t.top)+r*c}else"line"==n&&(i=r>0?t.bottom+3:t.top-3)
for(;(o=Zr(e,l,i)).outside;){if(r<0?i<=0:i>=a.height){o.hitSide=!0
break}i+=5*r}return o}var Ra=function(e){this.cm=e,this.lastAnchorNode=this.lastAnchorOffset=this.lastFocusNode=this.lastFocusOffset=null,this.polling=new W,this.composing=null,this.gracePeriod=!1,this.readDOMTimeout=null}
function $a(e,t){var r=Ar(e,t.line)
if(!r||r.hidden)return null
var n=Ge(e.doc,t.line),i=Lr(r,n,t.line),o=ce(n,e.doc.direction),a="left"
o&&(a=le(o,t.ch)%2?"right":"left")
var l=Ir(i.map,t.ch,a)
return l.offset="right"==l.collapse?l.end:l.start,l}function ja(e,t){return t&&(e.bad=!0),e}function Ha(e,t,r){var n
if(t==e.display.lineDiv){if(!(n=e.display.lineDiv.childNodes[r]))return ja(e.clipPos(et(e.display.viewTo-1)),!0)
t=null,r=0}else for(n=t;;n=n.parentNode){if(!n||n==e.display.lineDiv)return null
if(n.parentNode&&n.parentNode==e.display.lineDiv)break}for(var i=0;i<e.display.view.length;i++){var o=e.display.view[i]
if(o.node==n)return Ba(o,t,r)}}function Ba(e,t,r){var n=e.text.firstChild,i=!1
if(!t||!E(n,t))return ja(et(Xe(e.line),0),!0)
if(t==n&&(i=!0,t=n.childNodes[r],r=0,!t)){var o=e.rest?K(e.rest):e.line
return ja(et(Xe(o),o.text.length),i)}var a=3==t.nodeType?t:null,l=t
for(a||1!=t.childNodes.length||3!=t.firstChild.nodeType||(a=t.firstChild,r&&(r=a.nodeValue.length));l.parentNode!=n;)l=l.parentNode
var s=e.measure,c=s.maps
function u(t,r,n){for(var i=-1;i<(c?c.length:0);i++)for(var o=i<0?s.map:c[i],a=0;a<o.length;a+=3){var l=o[a+2]
if(l==t||l==r){var u=Xe(i<0?e.line:e.rest[i]),d=o[a]+n
return(n<0||l!=t)&&(d=o[a+(n?1:0)]),et(u,d)}}}var d=u(a,l,r)
if(d)return ja(d,i)
for(var f=l.nextSibling,p=a?a.nodeValue.length-r:0;f;f=f.nextSibling){if(d=u(f,f.firstChild,0))return ja(et(d.line,d.ch-p),i)
p+=f.textContent.length}for(var h=l.previousSibling,m=r;h;h=h.previousSibling){if(d=u(h,h.firstChild,-1))return ja(et(d.line,d.ch+m),i)
m+=h.textContent.length}}Ra.prototype.init=function(e){var t=this,r=this,n=r.cm,i=r.div=e.lineDiv
function o(e){if(!me(n,e)){if(n.somethingSelected())Ea({lineWise:!1,text:n.getSelections()}),"cut"==e.type&&n.replaceSelection("",null,"cut")
else{if(!n.options.lineWiseCopyCut)return
var t=Ia(n)
Ea({lineWise:!0,text:t.text}),"cut"==e.type&&n.operation((function(){n.setSelections(t.ranges,0,j),n.replaceSelection("",null,"cut")}))}if(e.clipboardData){e.clipboardData.clearData()
var o=Aa.text.join("\n")
if(e.clipboardData.setData("Text",o),e.clipboardData.getData("Text")==o)return void e.preventDefault()}var a=Fa(),l=a.firstChild
n.display.lineSpace.insertBefore(a,n.display.lineSpace.firstChild),l.value=Aa.text.join("\n")
var s=document.activeElement
I(l),setTimeout((function(){n.display.lineSpace.removeChild(a),s.focus(),s==i&&r.showPrimarySelection()}),50)}}Da(i,n.options.spellcheck,n.options.autocorrect,n.options.autocapitalize),de(i,"paste",(function(e){me(n,e)||qa(e,n)||l<=11&&setTimeout(ei(n,(function(){return t.updateFromDOM()})),20)})),de(i,"compositionstart",(function(e){t.composing={data:e.data,done:!1}})),de(i,"compositionupdate",(function(e){t.composing||(t.composing={data:e.data,done:!1})})),de(i,"compositionend",(function(e){t.composing&&(e.data!=t.composing.data&&t.readFromDOMSoon(),t.composing.done=!0)})),de(i,"touchstart",(function(){return r.forceCompositionEnd()})),de(i,"input",(function(){t.composing||t.readFromDOMSoon()})),de(i,"copy",o),de(i,"cut",o)},Ra.prototype.prepareSelection=function(){var e=vn(this.cm,!1)
return e.focus=this.cm.state.focused,e},Ra.prototype.showSelection=function(e,t){e&&this.cm.display.view.length&&((e.focus||t)&&this.showPrimarySelection(),this.showMultipleSelections(e))},Ra.prototype.getSelection=function(){return this.cm.display.wrapper.ownerDocument.getSelection()},Ra.prototype.showPrimarySelection=function(){var e=this.getSelection(),t=this.cm,n=t.doc.sel.primary(),i=n.from(),o=n.to()
if(t.display.viewTo==t.display.viewFrom||i.line>=t.display.viewTo||o.line<t.display.viewFrom)e.removeAllRanges()
else{var a=Ha(t,e.anchorNode,e.anchorOffset),l=Ha(t,e.focusNode,e.focusOffset)
if(!a||a.bad||!l||l.bad||0!=tt(ot(a,l),i)||0!=tt(it(a,l),o)){var s=t.display.view,c=i.line>=t.display.viewFrom&&$a(t,i)||{node:s[0].measure.map[2],offset:0},u=o.line<t.display.viewTo&&$a(t,o)
if(!u){var d=s[s.length-1].measure,f=d.maps?d.maps[d.maps.length-1]:d.map
u={node:f[f.length-1],offset:f[f.length-2]-f[f.length-3]}}if(c&&u){var p,h=e.rangeCount&&e.getRangeAt(0)
try{p=S(c.node,c.offset,u.offset,u.node)}catch(Ae){}p&&(!r&&t.state.focused?(e.collapse(c.node,c.offset),p.collapsed||(e.removeAllRanges(),e.addRange(p))):(e.removeAllRanges(),e.addRange(p)),h&&null==e.anchorNode?e.addRange(h):r&&this.startGracePeriod()),this.rememberSelection()}else e.removeAllRanges()}}},Ra.prototype.startGracePeriod=function(){var e=this
clearTimeout(this.gracePeriod),this.gracePeriod=setTimeout((function(){e.gracePeriod=!1,e.selectionChanged()&&e.cm.operation((function(){return e.cm.curOp.selectionChanged=!0}))}),20)},Ra.prototype.showMultipleSelections=function(e){L(this.cm.display.cursorDiv,e.cursors),L(this.cm.display.selectionDiv,e.selection)},Ra.prototype.rememberSelection=function(){var e=this.getSelection()
this.lastAnchorNode=e.anchorNode,this.lastAnchorOffset=e.anchorOffset,this.lastFocusNode=e.focusNode,this.lastFocusOffset=e.focusOffset},Ra.prototype.selectionInEditor=function(){var e=this.getSelection()
if(!e.rangeCount)return!1
var t=e.getRangeAt(0).commonAncestorContainer
return E(this.div,t)},Ra.prototype.focus=function(){"nocursor"!=this.cm.options.readOnly&&(this.selectionInEditor()||this.showSelection(this.prepareSelection(),!0),this.div.focus())},Ra.prototype.blur=function(){this.div.blur()},Ra.prototype.getField=function(){return this.div},Ra.prototype.supportsTouch=function(){return!0},Ra.prototype.receivedFocus=function(){var e=this
this.selectionInEditor()?this.pollSelection():Jn(this.cm,(function(){return e.cm.curOp.selectionChanged=!0})),this.polling.set(this.cm.options.pollInterval,(function t(){e.cm.state.focused&&(e.pollSelection(),e.polling.set(e.cm.options.pollInterval,t))}))},Ra.prototype.selectionChanged=function(){var e=this.getSelection()
return e.anchorNode!=this.lastAnchorNode||e.anchorOffset!=this.lastAnchorOffset||e.focusNode!=this.lastFocusNode||e.focusOffset!=this.lastFocusOffset},Ra.prototype.pollSelection=function(){if(null==this.readDOMTimeout&&!this.gracePeriod&&this.selectionChanged()){var e=this.getSelection(),t=this.cm
if(g&&u&&this.cm.display.gutterSpecs.length&&function(e){for(var t=e;t;t=t.parentNode)if(/CodeMirror-gutter-wrapper/.test(t.className))return!0
return!1}(e.anchorNode))return this.cm.triggerOnKeyDown({type:"keydown",keyCode:8,preventDefault:Math.abs}),this.blur(),void this.focus()
if(!this.composing){this.rememberSelection()
var r=Ha(t,e.anchorNode,e.anchorOffset),n=Ha(t,e.focusNode,e.focusOffset)
r&&n&&Jn(t,(function(){Ji(t.doc,Si(r,n),j),(r.bad||n.bad)&&(t.curOp.selectionChanged=!0)}))}}},Ra.prototype.pollContent=function(){null!=this.readDOMTimeout&&(clearTimeout(this.readDOMTimeout),this.readDOMTimeout=null)
var e,t,r,n=this.cm,i=n.display,o=n.doc.sel.primary(),a=o.from(),l=o.to()
if(0==a.ch&&a.line>n.firstLine()&&(a=et(a.line-1,Ge(n.doc,a.line-1).length)),l.ch==Ge(n.doc,l.line).text.length&&l.line<n.lastLine()&&(l=et(l.line+1,0)),a.line<i.viewFrom||l.line>i.viewTo-1)return!1
a.line==i.viewFrom||0==(e=un(n,a.line))?(t=Xe(i.view[0].line),r=i.view[0].node):(t=Xe(i.view[e].line),r=i.view[e-1].node.nextSibling)
var s,c,u=un(n,l.line)
if(u==i.view.length-1?(s=i.viewTo-1,c=i.lineDiv.lastChild):(s=Xe(i.view[u+1].line)-1,c=i.view[u+1].node.previousSibling),!r)return!1
for(var d=n.doc.splitLines(function(e,t,r,n,i){var o="",a=!1,l=e.doc.lineSeparator(),s=!1
function c(e){return function(t){return t.id==e}}function u(){a&&(o+=l,s&&(o+=l),a=s=!1)}function d(e){e&&(u(),o+=e)}function f(t){if(1==t.nodeType){var r=t.getAttribute("cm-text")
if(r)return void d(r)
var o,p=t.getAttribute("cm-marker")
if(p){var h=e.findMarks(et(n,0),et(i+1,0),c(+p))
return void(h.length&&(o=h[0].find(0))&&d(Ve(e.doc,o.from,o.to).join(l)))}if("false"==t.getAttribute("contenteditable"))return
var m=/^(pre|div|p|li|table|br)$/i.test(t.nodeName)
if(!/^br$/i.test(t.nodeName)&&0==t.textContent.length)return
m&&u()
for(var g=0;g<t.childNodes.length;g++)f(t.childNodes[g]);/^(pre|p)$/i.test(t.nodeName)&&(s=!0),m&&(a=!0)}else 3==t.nodeType&&d(t.nodeValue.replace(/\u200b/g,"").replace(/\u00a0/g," "))}for(;f(t),t!=r;)t=t.nextSibling,s=!1
return o}(n,r,c,t,s)),f=Ve(n.doc,et(t,0),et(s,Ge(n.doc,s).text.length));d.length>1&&f.length>1;)if(K(d)==K(f))d.pop(),f.pop(),s--
else{if(d[0]!=f[0])break
d.shift(),f.shift(),t++}for(var p=0,h=0,m=d[0],g=f[0],v=Math.min(m.length,g.length);p<v&&m.charCodeAt(p)==g.charCodeAt(p);)++p
for(var y=K(d),b=K(f),x=Math.min(y.length-(1==d.length?p:0),b.length-(1==f.length?p:0));h<x&&y.charCodeAt(y.length-h-1)==b.charCodeAt(b.length-h-1);)++h
if(1==d.length&&1==f.length&&t==a.line)for(;p&&p>a.ch&&y.charCodeAt(y.length-h-1)==b.charCodeAt(b.length-h-1);)p--,h++
d[d.length-1]=y.slice(0,y.length-h).replace(/^\u200b+/,""),d[0]=d[0].slice(p).replace(/\u200b+$/,"")
var w=et(t,p),k=et(s,f.length?K(f).length-h:0)
return d.length>1||d[0]||tt(w,k)?(mo(n.doc,d,w,k,"+input"),!0):void 0},Ra.prototype.ensurePolled=function(){this.forceCompositionEnd()},Ra.prototype.reset=function(){this.forceCompositionEnd()},Ra.prototype.forceCompositionEnd=function(){this.composing&&(clearTimeout(this.readDOMTimeout),this.composing=null,this.updateFromDOM(),this.div.blur(),this.div.focus())},Ra.prototype.readFromDOMSoon=function(){var e=this
null==this.readDOMTimeout&&(this.readDOMTimeout=setTimeout((function(){if(e.readDOMTimeout=null,e.composing){if(!e.composing.done)return
e.composing=null}e.updateFromDOM()}),80))},Ra.prototype.updateFromDOM=function(){var e=this
!this.cm.isReadOnly()&&this.pollContent()||Jn(this.cm,(function(){return dn(e.cm)}))},Ra.prototype.setUneditable=function(e){e.contentEditable="false"},Ra.prototype.onKeyPress=function(e){0==e.charCode||this.composing||(e.preventDefault(),this.cm.isReadOnly()||ei(this.cm,Na)(this.cm,String.fromCharCode(null==e.charCode?e.keyCode:e.charCode),0))},Ra.prototype.readOnlyChanged=function(e){this.div.contentEditable=String("nocursor"!=e)},Ra.prototype.onContextMenu=function(){},Ra.prototype.resetPosition=function(){},Ra.prototype.needsContentAttribute=!0
var Ua=function(e){this.cm=e,this.prevInput="",this.pollingFast=!1,this.polling=new W,this.hasSelection=!1,this.composing=null}
Ua.prototype.init=function(e){var t=this,r=this,n=this.cm
this.createField(e)
var i=this.textarea
function o(e){if(!me(n,e)){if(n.somethingSelected())Ea({lineWise:!1,text:n.getSelections()})
else{if(!n.options.lineWiseCopyCut)return
var t=Ia(n)
Ea({lineWise:!0,text:t.text}),"cut"==e.type?n.setSelections(t.ranges,null,j):(r.prevInput="",i.value=t.text.join("\n"),I(i))}"cut"==e.type&&(n.state.cutIncoming=+new Date)}}e.wrapper.insertBefore(this.wrapper,e.wrapper.firstChild),m&&(i.style.width="0px"),de(i,"input",(function(){a&&l>=9&&t.hasSelection&&(t.hasSelection=null),r.poll()})),de(i,"paste",(function(e){me(n,e)||qa(e,n)||(n.state.pasteIncoming=+new Date,r.fastPoll())})),de(i,"cut",o),de(i,"copy",o),de(e.scroller,"paste",(function(t){if(!wr(e,t)&&!me(n,t)){if(!i.dispatchEvent)return n.state.pasteIncoming=+new Date,void r.focus()
var o=new Event("paste")
o.clipboardData=t.clipboardData,i.dispatchEvent(o)}})),de(e.lineSpace,"selectstart",(function(t){wr(e,t)||be(t)})),de(i,"compositionstart",(function(){var e=n.getCursor("from")
r.composing&&r.composing.range.clear(),r.composing={start:e,range:n.markText(e,n.getCursor("to"),{className:"CodeMirror-composing"})}})),de(i,"compositionend",(function(){r.composing&&(r.poll(),r.composing.range.clear(),r.composing=null)}))},Ua.prototype.createField=function(e){this.wrapper=Fa(),this.textarea=this.wrapper.firstChild},Ua.prototype.prepareSelection=function(){var e=this.cm,t=e.display,r=e.doc,n=vn(e)
if(e.options.moveInputWithCursor){var i=Gr(e,r.sel.primary().head,"div"),o=t.wrapper.getBoundingClientRect(),a=t.lineDiv.getBoundingClientRect()
n.teTop=Math.max(0,Math.min(t.wrapper.clientHeight-10,i.top+a.top-o.top)),n.teLeft=Math.max(0,Math.min(t.wrapper.clientWidth-10,i.left+a.left-o.left))}return n},Ua.prototype.showSelection=function(e){var t=this.cm.display
L(t.cursorDiv,e.cursors),L(t.selectionDiv,e.selection),null!=e.teTop&&(this.wrapper.style.top=e.teTop+"px",this.wrapper.style.left=e.teLeft+"px")},Ua.prototype.reset=function(e){if(!this.contextMenuPending&&!this.composing){var t=this.cm
if(t.somethingSelected()){this.prevInput=""
var r=t.getSelection()
this.textarea.value=r,t.state.focused&&I(this.textarea),a&&l>=9&&(this.hasSelection=r)}else e||(this.prevInput=this.textarea.value="",a&&l>=9&&(this.hasSelection=null))}},Ua.prototype.getField=function(){return this.textarea},Ua.prototype.supportsTouch=function(){return!1},Ua.prototype.focus=function(){if("nocursor"!=this.cm.options.readOnly&&(!v||N()!=this.textarea))try{this.textarea.focus()}catch(Ae){}},Ua.prototype.blur=function(){this.textarea.blur()},Ua.prototype.resetPosition=function(){this.wrapper.style.top=this.wrapper.style.left=0},Ua.prototype.receivedFocus=function(){this.slowPoll()},Ua.prototype.slowPoll=function(){var e=this
this.pollingFast||this.polling.set(this.cm.options.pollInterval,(function(){e.poll(),e.cm.state.focused&&e.slowPoll()}))},Ua.prototype.fastPoll=function(){var e=!1,t=this
t.pollingFast=!0,t.polling.set(20,(function r(){t.poll()||e?(t.pollingFast=!1,t.slowPoll()):(e=!0,t.polling.set(60,r))}))},Ua.prototype.poll=function(){var e=this,t=this.cm,r=this.textarea,n=this.prevInput
if(this.contextMenuPending||!t.state.focused||Ne(r)&&!n&&!this.composing||t.isReadOnly()||t.options.disableInput||t.state.keySeq)return!1
var i=r.value
if(i==n&&!t.somethingSelected())return!1
if(a&&l>=9&&this.hasSelection===i||y&&/[\uf700-\uf7ff]/.test(i))return t.display.input.reset(),!1
if(t.doc.sel==t.display.selForContextMenu){var o=i.charCodeAt(0)
if(8203!=o||n||(n="​"),8666==o)return this.reset(),this.cm.execCommand("undo")}for(var s=0,c=Math.min(n.length,i.length);s<c&&n.charCodeAt(s)==i.charCodeAt(s);)++s
return Jn(t,(function(){Na(t,i.slice(s),n.length-s,null,e.composing?"*compose":null),i.length>1e3||i.indexOf("\n")>-1?r.value=e.prevInput="":e.prevInput=i,e.composing&&(e.composing.range.clear(),e.composing.range=t.markText(e.composing.start,t.getCursor("to"),{className:"CodeMirror-composing"}))})),!0},Ua.prototype.ensurePolled=function(){this.pollingFast&&this.poll()&&(this.pollingFast=!1)},Ua.prototype.onKeyPress=function(){a&&l>=9&&(this.hasSelection=null),this.fastPoll()},Ua.prototype.onContextMenu=function(e){var t=this,r=t.cm,n=r.display,i=t.textarea
t.contextMenuPending&&t.contextMenuPending()
var o=cn(r,e),c=n.scroller.scrollTop
if(o&&!d){r.options.resetSelectionOnContextMenu&&-1==r.doc.sel.contains(o)&&ei(r,Ji)(r.doc,Si(o),j)
var u,f=i.style.cssText,p=t.wrapper.style.cssText,h=t.wrapper.offsetParent.getBoundingClientRect()
if(t.wrapper.style.cssText="position: static",i.style.cssText="position: absolute; width: 30px; height: 30px;\n      top: "+(e.clientY-h.top-5)+"px; left: "+(e.clientX-h.left-5)+"px;\n      z-index: 1000; background: "+(a?"rgba(255, 255, 255, .05)":"transparent")+";\n      outline: none; border-width: 0; outline: none; overflow: hidden; opacity: .05; filter: alpha(opacity=5);",s&&(u=window.scrollY),n.input.focus(),s&&window.scrollTo(null,u),n.input.reset(),r.somethingSelected()||(i.value=t.prevInput=" "),t.contextMenuPending=v,n.selForContextMenu=r.doc.sel,clearTimeout(n.detectingSelectAll),a&&l>=9&&g(),_){ke(e)
var m=function(){pe(window,"mouseup",m),setTimeout(v,20)}
de(window,"mouseup",m)}else setTimeout(v,50)}function g(){if(null!=i.selectionStart){var e=r.somethingSelected(),o="​"+(e?i.value:"")
i.value="⇚",i.value=o,t.prevInput=e?"":"​",i.selectionStart=1,i.selectionEnd=o.length,n.selForContextMenu=r.doc.sel}}function v(){if(t.contextMenuPending==v&&(t.contextMenuPending=!1,t.wrapper.style.cssText=p,i.style.cssText=f,a&&l<9&&n.scrollbars.setScrollTop(n.scroller.scrollTop=c),null!=i.selectionStart)){(!a||a&&l<9)&&g()
var e=0,o=function(){n.selForContextMenu==r.doc.sel&&0==i.selectionStart&&i.selectionEnd>0&&"​"==t.prevInput?ei(r,lo)(r):e++<10?n.detectingSelectAll=setTimeout(o,500):(n.selForContextMenu=null,n.input.reset())}
n.detectingSelectAll=setTimeout(o,200)}}},Ua.prototype.readOnlyChanged=function(e){e||this.reset(),this.textarea.disabled="nocursor"==e},Ua.prototype.setUneditable=function(){},Ua.prototype.needsContentAttribute=!1,function(e){var t=e.optionHandlers
function r(r,n,i,o){e.defaults[r]=n,i&&(t[r]=o?function(e,t,r){r!=ka&&i(e,t,r)}:i)}e.defineOption=r,e.Init=ka,r("value","",(function(e,t){return e.setValue(t)}),!0),r("mode",null,(function(e,t){e.doc.modeOption=t,Ai(e)}),!0),r("indentUnit",2,Ai,!0),r("indentWithTabs",!1),r("smartIndent",!0),r("tabSize",4,(function(e){Ei(e),Wr(e),dn(e)}),!0),r("lineSeparator",null,(function(e,t){if(e.doc.lineSep=t,t){var r=[],n=e.doc.first
e.doc.iter((function(e){for(var i=0;;){var o=e.text.indexOf(t,i)
if(-1==o)break
i=o+t.length,r.push(et(n,o))}n++}))
for(var i=r.length-1;i>=0;i--)mo(e.doc,t,r[i],et(r[i].line,r[i].ch+t.length))}})),r("specialChars",/[\u0000-\u001f\u007f-\u009f\u00ad\u061c\u200b-\u200f\u2028\u2029\ufeff\ufff9-\ufffc]/g,(function(e,t,r){e.state.specialChars=new RegExp(t.source+(t.test("\t")?"":"|\t"),"g"),r!=ka&&e.refresh()})),r("specialCharPlaceholder",Qt,(function(e){return e.refresh()}),!0),r("electricChars",!0),r("inputStyle",v?"contenteditable":"textarea",(function(){throw new Error("inputStyle can not (yet) be changed in a running editor")}),!0),r("spellcheck",!1,(function(e,t){return e.getInputField().spellcheck=t}),!0),r("autocorrect",!1,(function(e,t){return e.getInputField().autocorrect=t}),!0),r("autocapitalize",!1,(function(e,t){return e.getInputField().autocapitalize=t}),!0),r("rtlMoveVisually",!x),r("wholeLineUpdateBefore",!0),r("theme","default",(function(e){wa(e),mi(e)}),!0),r("keyMap","default",(function(e,t,r){var n=Xo(t),i=r!=ka&&Xo(r)
i&&i.detach&&i.detach(e,n),n.attach&&n.attach(e,i||null)})),r("extraKeys",null),r("configureMouse",null),r("lineWrapping",!1,Ta,!0),r("gutters",[],(function(e,t){e.display.gutterSpecs=pi(t,e.options.lineNumbers),mi(e)}),!0),r("fixedGutter",!0,(function(e,t){e.display.gutters.style.left=t?an(e.display)+"px":"0",e.refresh()}),!0),r("coverGutterNextToScrollbar",!1,(function(e){return $n(e)}),!0),r("scrollbarStyle","native",(function(e){Bn(e),$n(e),e.display.scrollbars.setScrollTop(e.doc.scrollTop),e.display.scrollbars.setScrollLeft(e.doc.scrollLeft)}),!0),r("lineNumbers",!1,(function(e,t){e.display.gutterSpecs=pi(e.options.gutters,t),mi(e)}),!0),r("firstLineNumber",1,mi,!0),r("lineNumberFormatter",(function(e){return e}),mi,!0)
r("showCursorWhenSelecting",!1,gn,!0),r("resetSelectionOnContextMenu",!0),r("lineWiseCopyCut",!0),r("pasteLinesPerSelection",!0),r("selectionsMayTouch",!1),r("readOnly",!1,(function(e,t){"nocursor"==t&&(Sn(e),e.display.input.blur()),e.display.input.readOnlyChanged(t)})),r("disableInput",!1,(function(e,t){t||e.display.input.reset()}),!0),r("dragDrop",!0,Sa),r("allowDropFileTypes",null),r("cursorBlinkRate",530),r("cursorScrollMargin",0),r("cursorHeight",1,gn,!0),r("singleCursorHeightPerLine",!0,gn,!0),r("workTime",100),r("workDelay",100),r("flattenSpans",!0,Ei,!0),r("addModeClass",!1,Ei,!0),r("pollInterval",100),r("undoDepth",200,(function(e,t){return e.doc.history.undoDepth=t})),r("historyEventDelay",1250),r("viewportMargin",10,(function(e){return e.refresh()}),!0),r("maxHighlightLength",1e4,Ei,!0),r("moveInputWithCursor",!0,(function(e,t){t||e.display.input.resetPosition()})),r("tabindex",null,(function(e,t){return e.display.input.getField().tabIndex=t||""})),r("autofocus",null),r("direction","ltr",(function(e,t){return e.doc.setDirection(t)}),!0),r("phrases",null)}(Ma),function(e){var t=e.optionHandlers,r=e.helpers={}
e.prototype={constructor:e,focus:function(){window.focus(),this.display.input.focus()},setOption:function(e,r){var n=this.options,i=n[e]
n[e]==r&&"mode"!=e||(n[e]=r,t.hasOwnProperty(e)&&ei(this,t[e])(this,r,i),he(this,"optionChange",this,e))},getOption:function(e){return this.options[e]},getDoc:function(){return this.doc},addKeyMap:function(e,t){this.state.keyMaps[t?"push":"unshift"](Xo(e))},removeKeyMap:function(e){for(var t=this.state.keyMaps,r=0;r<t.length;++r)if(t[r]==e||t[r].name==e)return t.splice(r,1),!0},addOverlay:ti((function(t,r){var n=t.token?t:e.getMode(this.options,t)
if(n.startState)throw new Error("Overlays may not be stateful.");(function(e,t,r){for(var n=0,i=r(t);n<e.length&&r(e[n])<=i;)n++
e.splice(n,0,t)})(this.state.overlays,{mode:n,modeSpec:t,opaque:r&&r.opaque,priority:r&&r.priority||0},(function(e){return e.priority})),this.state.modeGen++,dn(this)})),removeOverlay:ti((function(e){for(var t=this.state.overlays,r=0;r<t.length;++r){var n=t[r].modeSpec
if(n==e||"string"==typeof e&&n.name==e)return t.splice(r,1),this.state.modeGen++,void dn(this)}})),indentLine:ti((function(e,t,r){"string"!=typeof t&&"number"!=typeof t&&(t=null==t?this.options.smartIndent?"smart":"prev":t?"add":"subtract"),Qe(this.doc,e)&&za(this,e,t,r)})),indentSelection:ti((function(e){for(var t=this.doc.sel.ranges,r=-1,n=0;n<t.length;n++){var i=t[n]
if(i.empty())i.head.line>r&&(za(this,i.head.line,e,!0),r=i.head.line,n==this.doc.sel.primIndex&&En(this))
else{var o=i.from(),a=i.to(),l=Math.max(r,o.line)
r=Math.min(this.lastLine(),a.line-(a.ch?0:1))+1
for(var s=l;s<r;++s)za(this,s,e)
var c=this.doc.sel.ranges
0==o.ch&&t.length==c.length&&c[n].from().ch>0&&Xi(this.doc,n,new _i(o,c[n].to()),j)}}})),getTokenAt:function(e,t){return yt(this,e,t)},getLineTokens:function(e,t){return yt(this,et(e),t,!0)},getTokenTypeAt:function(e){e=lt(this.doc,e)
var t,r=ft(this,Ge(this.doc,e.line)),n=0,i=(r.length-1)/2,o=e.ch
if(0==o)t=r[2]
else for(;;){var a=n+i>>1
if((a?r[2*a-1]:0)>=o)i=a
else{if(!(r[2*a+1]<o)){t=r[2*a+2]
break}n=a+1}}var l=t?t.indexOf("overlay "):-1
return l<0?t:0==l?null:t.slice(0,l-1)},getModeAt:function(t){var r=this.doc.mode
return r.innerMode?e.innerMode(r,this.getTokenAt(t).state).mode:r},getHelper:function(e,t){return this.getHelpers(e,t)[0]},getHelpers:function(e,t){var n=[]
if(!r.hasOwnProperty(t))return n
var i=r[t],o=this.getModeAt(e)
if("string"==typeof o[t])i[o[t]]&&n.push(i[o[t]])
else if(o[t])for(var a=0;a<o[t].length;a++){var l=i[o[t][a]]
l&&n.push(l)}else o.helperType&&i[o.helperType]?n.push(i[o.helperType]):i[o.name]&&n.push(i[o.name])
for(var s=0;s<i._global.length;s++){var c=i._global[s]
c.pred(o,this)&&-1==R(n,c.val)&&n.push(c.val)}return n},getStateAfter:function(e,t){var r=this.doc
return pt(this,(e=at(r,null==e?r.first+r.size-1:e))+1,t).state},cursorCoords:function(e,t){var r=this.doc.sel.primary()
return Gr(this,null==e?r.head:"object"==typeof e?lt(this.doc,e):e?r.from():r.to(),t||"page")},charCoords:function(e,t){return Ur(this,lt(this.doc,e),t||"page")},coordsChar:function(e,t){return Zr(this,(e=Br(this,e,t||"page")).left,e.top)},lineAtHeight:function(e,t){return e=Br(this,{top:e,left:0},t||"page").top,Ye(this.doc,e+this.display.viewOffset)},heightAtLine:function(e,t,r){var n,i=!1
if("number"==typeof e){var o=this.doc.first+this.doc.size-1
e<this.doc.first?e=this.doc.first:e>o&&(e=o,i=!0),n=Ge(this.doc,e)}else n=e
return Hr(this,n,{top:0,left:0},t||"page",r||i).top+(i?this.doc.height-Ht(n):0)},defaultTextHeight:function(){return rn(this.display)},defaultCharWidth:function(){return nn(this.display)},getViewport:function(){return{from:this.display.viewFrom,to:this.display.viewTo}},addWidget:function(e,t,r,n,i){var o,a,l,s=this.display,c=(e=Gr(this,lt(this.doc,e))).bottom,u=e.left
if(t.style.position="absolute",t.setAttribute("cm-ignore-events","true"),this.display.input.setUneditable(t),s.sizer.appendChild(t),"over"==n)c=e.top
else if("above"==n||"near"==n){var d=Math.max(s.wrapper.clientHeight,this.doc.height),f=Math.max(s.sizer.clientWidth,s.lineSpace.clientWidth);("above"==n||e.bottom+t.offsetHeight>d)&&e.top>t.offsetHeight?c=e.top-t.offsetHeight:e.bottom+t.offsetHeight<=d&&(c=e.bottom),u+t.offsetWidth>f&&(u=f-t.offsetWidth)}t.style.top=c+"px",t.style.left=t.style.right="","right"==i?(u=s.sizer.clientWidth-t.offsetWidth,t.style.right="0px"):("left"==i?u=0:"middle"==i&&(u=(s.sizer.clientWidth-t.offsetWidth)/2),t.style.left=u+"px"),r&&(o=this,a={left:u,top:c,right:u+t.offsetWidth,bottom:c+t.offsetHeight},null!=(l=zn(o,a)).scrollTop&&In(o,l.scrollTop),null!=l.scrollLeft&&Fn(o,l.scrollLeft))},triggerOnKeyDown:ti(ua),triggerOnKeyPress:ti(fa),triggerOnKeyUp:da,triggerOnMouseDown:ti(ga),execCommand:function(e){if(ta.hasOwnProperty(e))return ta[e].call(null,this)},triggerElectric:ti((function(e){Oa(this,e)})),findPosH:function(e,t,r,n){var i=1
t<0&&(i=-1,t=-t)
for(var o=lt(this.doc,e),a=0;a<t&&!(o=Pa(this.doc,o,i,r,n)).hitSide;++a);return o},moveH:ti((function(e,t){var r=this
this.extendSelectionsBy((function(n){return r.display.shift||r.doc.extend||n.empty()?Pa(r.doc,n.head,e,t,r.options.rtlMoveVisually):e<0?n.from():n.to()}),B)})),deleteH:ti((function(e,t){var r=this.doc.sel,n=this.doc
r.somethingSelected()?n.replaceSelection("",null,"+delete"):Yo(this,(function(r){var i=Pa(n,r.head,e,t,!1)
return e<0?{from:i,to:r.head}:{from:r.head,to:i}}))})),findPosV:function(e,t,r,n){var i=1,o=n
t<0&&(i=-1,t=-t)
for(var a=lt(this.doc,e),l=0;l<t;++l){var s=Gr(this,a,"div")
if(null==o?o=s.left:s.left=o,(a=Wa(this,s,i,r)).hitSide)break}return a},moveV:ti((function(e,t){var r=this,n=this.doc,i=[],o=!this.display.shift&&!n.extend&&n.sel.somethingSelected()
if(n.extendSelectionsBy((function(a){if(o)return e<0?a.from():a.to()
var l=Gr(r,a.head,"div")
null!=a.goalColumn&&(l.left=a.goalColumn),i.push(l.left)
var s=Wa(r,l,e,t)
return"page"==t&&a==n.sel.primary()&&An(r,Ur(r,s,"div").top-l.top),s}),B),i.length)for(var a=0;a<n.sel.ranges.length;a++)n.sel.ranges[a].goalColumn=i[a]})),findWordAt:function(e){var t=Ge(this.doc,e.line).text,r=e.ch,n=e.ch
if(t){var i=this.getHelper(e,"wordChars")
"before"!=e.sticky&&n!=t.length||!r?++n:--r
for(var o=t.charAt(r),a=ee(o,i)?function(e){return ee(e,i)}:/\s/.test(o)?function(e){return/\s/.test(e)}:function(e){return!/\s/.test(e)&&!ee(e)};r>0&&a(t.charAt(r-1));)--r
for(;n<t.length&&a(t.charAt(n));)++n}return new _i(et(e.line,r),et(e.line,n))},toggleOverwrite:function(e){null!=e&&e==this.state.overwrite||((this.state.overwrite=!this.state.overwrite)?q(this.display.cursorDiv,"CodeMirror-overwrite"):T(this.display.cursorDiv,"CodeMirror-overwrite"),he(this,"overwriteToggle",this,this.state.overwrite))},hasFocus:function(){return this.display.input.getField()==N()},isReadOnly:function(){return!(!this.options.readOnly&&!this.doc.cantEdit)},scrollTo:ti((function(e,t){Nn(this,e,t)})),getScrollInfo:function(){var e=this.display.scroller
return{left:e.scrollLeft,top:e.scrollTop,height:e.scrollHeight-Sr(this)-this.display.barHeight,width:e.scrollWidth-Sr(this)-this.display.barWidth,clientHeight:Mr(this),clientWidth:Tr(this)}},scrollIntoView:ti((function(e,t){null==e?(e={from:this.doc.sel.primary().head,to:null},null==t&&(t=this.options.cursorScrollMargin)):"number"==typeof e?e={from:et(e,0),to:null}:null==e.from&&(e={from:e,to:null}),e.to||(e.to=e.from),e.margin=t||0,null!=e.from.line?function(e,t){qn(e),e.curOp.scrollToPos=t}(this,e):On(this,e.from,e.to,e.margin)})),setSize:ti((function(e,t){var r=this,n=function(e){return"number"==typeof e||/^\d+$/.test(String(e))?e+"px":e}
null!=e&&(this.display.wrapper.style.width=n(e)),null!=t&&(this.display.wrapper.style.height=n(t)),this.options.lineWrapping&&Pr(this)
var i=this.display.viewFrom
this.doc.iter(i,this.display.viewTo,(function(e){if(e.widgets)for(var t=0;t<e.widgets.length;t++)if(e.widgets[t].noHScroll){fn(r,i,"widget")
break}++i})),this.curOp.forceUpdate=!0,he(this,"refresh",this)})),operation:function(e){return Jn(this,e)},startOperation:function(){return Gn(this)},endOperation:function(){return Vn(this)},refresh:ti((function(){var e=this.display.cachedTextHeight
dn(this),this.curOp.forceUpdate=!0,Wr(this),Nn(this,this.doc.scrollLeft,this.doc.scrollTop),ci(this.display),(null==e||Math.abs(e-rn(this.display))>.5)&&sn(this),he(this,"refresh",this)})),swapDoc:ti((function(e){var t=this.doc
return t.cm=null,this.state.selectingText&&this.state.selectingText(),Ii(this,e),Wr(this),this.display.input.reset(),Nn(this,e.scrollLeft,e.scrollTop),this.curOp.forceScroll=!0,lr(this,"swapDoc",this,t),t})),phrase:function(e){var t=this.options.phrases
return t&&Object.prototype.hasOwnProperty.call(t,e)?t[e]:e},getInputField:function(){return this.display.input.getField()},getWrapperElement:function(){return this.display.wrapper},getScrollerElement:function(){return this.display.scroller},getGutterElement:function(){return this.display.gutters}},ye(e),e.registerHelper=function(t,n,i){r.hasOwnProperty(t)||(r[t]=e[t]={_global:[]}),r[t][n]=i},e.registerGlobalHelper=function(t,n,i,o){e.registerHelper(t,n,o),r[t]._global.push({pred:i,val:o})}}(Ma)
var Ga="iter insert remove copy getEditor constructor".split(" ")
for(var Va in Eo.prototype)Eo.prototype.hasOwnProperty(Va)&&R(Ga,Va)<0&&(Ma.prototype[Va]=function(e){return function(){return e.apply(this.doc,arguments)}}(Eo.prototype[Va]))
return ye(Eo),Ma.inputStyles={textarea:Ua,contenteditable:Ra},Ma.defineMode=function(e){Ma.defaults.mode||"null"==e||(Ma.defaults.mode=e),Fe.apply(this,arguments)},Ma.defineMIME=function(e,t){De[e]=t},Ma.defineMode("null",(function(){return{token:function(e){return e.skipToEnd()}}})),Ma.defineMIME("text/plain","null"),Ma.defineExtension=function(e,t){Ma.prototype[e]=t},Ma.defineDocExtension=function(e,t){Eo.prototype[e]=t},Ma.fromTextArea=function(e,t){if((t=t?F(t):{}).value=e.value,!t.tabindex&&e.tabIndex&&(t.tabindex=e.tabIndex),!t.placeholder&&e.placeholder&&(t.placeholder=e.placeholder),null==t.autofocus){var r=N()
t.autofocus=r==e||null!=e.getAttribute("autofocus")&&r==document.body}function n(){e.value=l.getValue()}var i
if(e.form&&(de(e.form,"submit",n),!t.leaveSubmitMethodAlone)){var o=e.form
i=o.submit
try{var a=o.submit=function(){n(),o.submit=i,o.submit(),o.submit=a}}catch(Ae){}}t.finishInit=function(r){r.save=n,r.getTextArea=function(){return e},r.toTextArea=function(){r.toTextArea=isNaN,n(),e.parentNode.removeChild(r.getWrapperElement()),e.style.display="",e.form&&(pe(e.form,"submit",n),t.leaveSubmitMethodAlone||"function"!=typeof e.form.submit||(e.form.submit=i))}},e.style.display="none"
var l=Ma((function(t){return e.parentNode.insertBefore(t,e.nextSibling)}),t)
return l},function(e){e.off=pe,e.on=de,e.wheelEventPixels=xi,e.Doc=Eo,e.splitLines=Ee,e.countColumn=P,e.findColumn=U,e.isWordChar=J,e.Pass=$,e.signal=he,e.Line=Gt,e.changeEnd=Ti,e.scrollbarModel=Hn,e.Pos=et,e.cmpPos=tt,e.modes=Ie,e.mimeModes=De,e.resolveMode=Pe,e.getMode=We,e.modeExtensions=Re,e.extendMode=$e,e.copyState=je,e.startState=Be,e.innerMode=He,e.commands=ta,e.keyMap=Ho,e.keyName=Zo,e.isModifierKey=Vo,e.lookupKey=Go,e.normalizeKeyMap=Uo
e.StringStream=Ue,e.SharedTextMarker=Mo,e.TextMarker=So,e.LineWidget=ko,e.e_preventDefault=be,e.e_stopPropagation=xe,e.e_stop=ke,e.addClass=q,e.contains=E,e.rmClass=T,e.keyNames=Wo}(Ma),Ma.version="5.52.0",Ma})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
function t(e,t){if(!e.hasOwnProperty(t))throw new Error("Undefined state "+t+" in simple mode")}function r(e,t){if(!e)return/(?:)/
var r=""
return e instanceof RegExp?(e.ignoreCase&&(r="i"),e=e.source):e=String(e),new RegExp((!1===t?"":"^")+"(?:"+e+")",r)}function n(e,n){(e.next||e.push)&&t(n,e.next||e.push),this.regex=r(e.regex),this.token=function(e){if(!e)return null
if(e.apply)return e
if("string"==typeof e)return e.replace(/\./g," ")
for(var t=[],r=0;r<e.length;r++)t.push(e[r]&&e[r].replace(/\./g," "))
return t}(e.token),this.data=e}function i(e,t){return function(r,n){if(n.pending){var i=n.pending.shift()
return 0==n.pending.length&&(n.pending=null),r.pos+=i.text.length,i.token}if(n.local){if(n.local.end&&r.match(n.local.end)){var o=n.local.endToken||null
return n.local=n.localState=null,o}var l
o=n.local.mode.token(r,n.localState)
return n.local.endScan&&(l=n.local.endScan.exec(r.current()))&&(r.pos=r.start+l.index),o}for(var s=e[n.state],c=0;c<s.length;c++){var u=s[c],d=(!u.data.sol||r.sol())&&r.match(u.regex)
if(d){u.data.next?n.state=u.data.next:u.data.push?((n.stack||(n.stack=[])).push(n.state),n.state=u.data.push):u.data.pop&&n.stack&&n.stack.length&&(n.state=n.stack.pop()),u.data.mode&&a(t,n,u.data.mode,u.token),u.data.indent&&n.indent.push(r.indentation()+t.indentUnit),u.data.dedent&&n.indent.pop()
var f=u.token
if(f&&f.apply&&(f=f(d)),d.length>2&&u.token&&"string"!=typeof u.token){n.pending=[]
for(var p=2;p<d.length;p++)d[p]&&n.pending.push({text:d[p],token:u.token[p-1]})
return r.backUp(d[0].length-(d[1]?d[1].length:0)),f[0]}return f&&f.join?f[0]:f}}return r.next(),null}}function o(e,t){if(e===t)return!0
if(!e||"object"!=typeof e||!t||"object"!=typeof t)return!1
var r=0
for(var n in e)if(e.hasOwnProperty(n)){if(!t.hasOwnProperty(n)||!o(e[n],t[n]))return!1
r++}for(var n in t)t.hasOwnProperty(n)&&r--
return 0==r}function a(t,n,i,a){var l
if(i.persistent)for(var s=n.persistentStates;s&&!l;s=s.next)(i.spec?o(i.spec,s.spec):i.mode==s.mode)&&(l=s)
var c=l?l.mode:i.mode||e.getMode(t,i.spec),u=l?l.state:e.startState(c)
i.persistent&&!l&&(n.persistentStates={mode:c,spec:i.spec,state:u,next:n.persistentStates}),n.localState=u,n.local={mode:c,end:i.end&&r(i.end),endScan:i.end&&!1!==i.forceEnd&&r(i.end,!1),endToken:a&&a.join?a[a.length-1]:a}}function l(t,r){return function(n,i,o){if(n.local&&n.local.mode.indent)return n.local.mode.indent(n.localState,i,o)
if(null==n.indent||n.local||r.dontIndentStates&&function(e,t){for(var r=0;r<t.length;r++)if(t[r]===e)return!0}(n.state,r.dontIndentStates)>-1)return e.Pass
var a=n.indent.length-1,l=t[n.state]
e:for(;;){for(var s=0;s<l.length;s++){var c=l[s]
if(c.data.dedent&&!1!==c.data.dedentIfLineStart){var u=c.regex.exec(i)
if(u&&u[0]){a--,(c.next||c.push)&&(l=t[c.next||c.push]),i=i.slice(u[0].length)
continue e}}}break}return a<0?0:n.indent[a]}}e.defineSimpleMode=function(t,r){e.defineMode(t,(function(t){return e.simpleMode(t,r)}))},e.simpleMode=function(r,o){t(o,"start")
var a={},s=o.meta||{},c=!1
for(var u in o)if(u!=s&&o.hasOwnProperty(u))for(var d=a[u]=[],f=o[u],p=0;p<f.length;p++){var h=f[p]
d.push(new n(h,o)),(h.indent||h.dedent)&&(c=!0)}var m={startState:function(){return{state:"start",pending:null,local:null,localState:null,indent:c?[]:null}},copyState:function(t){var r={state:t.state,pending:t.pending,local:t.local,localState:null,indent:t.indent&&t.indent.slice(0)}
t.localState&&(r.localState=e.copyState(t.local.mode,t.localState)),t.stack&&(r.stack=t.stack.slice(0))
for(var n=t.persistentStates;n;n=n.next)r.persistentStates={mode:n.mode,spec:n.spec,state:n.state==t.localState?r.localState:e.copyState(n.mode,n.state),next:r.persistentStates}
return r},token:i(a,r),innerMode:function(e){return e.local&&{mode:e.local.mode,state:e.localState}},indent:l(a,s)}
if(s)for(var g in s)s.hasOwnProperty(g)&&(m[g]=s[g])
return m}})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
function t(e,t,r,n,i,o){this.indented=e,this.column=t,this.type=r,this.info=n,this.align=i,this.prev=o}function r(e,r,n,i){var o=e.indented
return e.context&&"statement"==e.context.type&&"statement"!=n&&(o=e.context.indented),e.context=new t(o,r,n,i,null,e.context)}function n(e){var t=e.context.type
return")"!=t&&"]"!=t&&"}"!=t||(e.indented=e.context.indented),e.context=e.context.prev}function i(e,t,r){return"variable"==t.prevToken||"type"==t.prevToken||(!!/\S(?:[^- ]>|[*\]])\s*$|\*$/.test(e.string.slice(0,r))||(!(!t.typeAtEndOfLine||e.column()!=e.indentation())||void 0))}function o(e){for(;;){if(!e||"top"==e.type)return!0
if("}"==e.type&&"namespace"!=e.prev.info)return!1
e=e.prev}}function a(e){for(var t={},r=e.split(" "),n=0;n<r.length;++n)t[r[n]]=!0
return t}function l(e,t){return"function"==typeof e?e(t):e.propertyIsEnumerable(t)}e.defineMode("clike",(function(a,s){var c,u,d=a.indentUnit,f=s.statementIndentUnit||d,p=s.dontAlignCalls,h=s.keywords||{},m=s.types||{},g=s.builtin||{},v=s.blockKeywords||{},y=s.defKeywords||{},b=s.atoms||{},x=s.hooks||{},w=s.multiLineStrings,k=!1!==s.indentStatements,_=!1!==s.indentSwitch,C=s.namespaceSeparator,S=s.isPunctuationChar||/[\[\]{}\(\),;\:\.]/,T=s.numberStart||/[\d\.]/,M=s.number||/^(?:0x[a-f\d]+|0b[01]+|(?:\d+\.?\d*|\.\d+)(?:e[-+]?\d+)?)(u|ll?|l|f)?/i,L=s.isOperatorChar||/[+\-*&%=<>!?|\/]/,z=s.isIdentifierChar||/[\w\$_\xa1-\uffff]/,A=s.isReservedIdentifier||!1
function E(e,t){var r,n=e.next()
if(x[n]){var i=x[n](e,t)
if(!1!==i)return i}if('"'==n||"'"==n)return t.tokenize=(r=n,function(e,t){for(var n,i=!1,o=!1;null!=(n=e.next());){if(n==r&&!i){o=!0
break}i=!i&&"\\"==n}return(o||!i&&!w)&&(t.tokenize=null),"string"}),t.tokenize(e,t)
if(S.test(n))return c=n,null
if(T.test(n)){if(e.backUp(1),e.match(M))return"number"
e.next()}if("/"==n){if(e.eat("*"))return t.tokenize=N,N(e,t)
if(e.eat("/"))return e.skipToEnd(),"comment"}if(L.test(n)){for(;!e.match(/^\/[\/*]/,!1)&&e.eat(L););return"operator"}if(e.eatWhile(z),C)for(;e.match(C);)e.eatWhile(z)
var o=e.current()
return l(h,o)?(l(v,o)&&(c="newstatement"),l(y,o)&&(u=!0),"keyword"):l(m,o)?"type":l(g,o)||A&&A(o)?(l(v,o)&&(c="newstatement"),"builtin"):l(b,o)?"atom":"variable"}function N(e,t){for(var r,n=!1;r=e.next();){if("/"==r&&n){t.tokenize=null
break}n="*"==r}return"comment"}function q(e,t){s.typeFirstDefinitions&&e.eol()&&o(t.context)&&(t.typeAtEndOfLine=i(e,t,e.pos))}return{startState:function(e){return{tokenize:null,context:new t((e||0)-d,0,"top",null,!1),indented:0,startOfLine:!0,prevToken:null}},token:function(e,t){var a=t.context
if(e.sol()&&(null==a.align&&(a.align=!1),t.indented=e.indentation(),t.startOfLine=!0),e.eatSpace())return q(e,t),null
c=u=null
var l=(t.tokenize||E)(e,t)
if("comment"==l||"meta"==l)return l
if(null==a.align&&(a.align=!0),";"==c||":"==c||","==c&&e.match(/^\s*(?:\/\/.*)?$/,!1))for(;"statement"==t.context.type;)n(t)
else if("{"==c)r(t,e.column(),"}")
else if("["==c)r(t,e.column(),"]")
else if("("==c)r(t,e.column(),")")
else if("}"==c){for(;"statement"==a.type;)a=n(t)
for("}"==a.type&&(a=n(t));"statement"==a.type;)a=n(t)}else c==a.type?n(t):k&&(("}"==a.type||"top"==a.type)&&";"!=c||"statement"==a.type&&"newstatement"==c)&&r(t,e.column(),"statement",e.current())
if("variable"==l&&("def"==t.prevToken||s.typeFirstDefinitions&&i(e,t,e.start)&&o(t.context)&&e.match(/^\s*\(/,!1))&&(l="def"),x.token){var d=x.token(e,t,l)
void 0!==d&&(l=d)}return"def"==l&&!1===s.styleDefs&&(l="variable"),t.startOfLine=!1,t.prevToken=u?"def":l||c,q(e,t),l},indent:function(t,r){if(t.tokenize!=E&&null!=t.tokenize||t.typeAtEndOfLine)return e.Pass
var n=t.context,i=r&&r.charAt(0),o=i==n.type
if("statement"==n.type&&"}"==i&&(n=n.prev),s.dontIndentStatements)for(;"statement"==n.type&&s.dontIndentStatements.test(n.info);)n=n.prev
if(x.indent){var a=x.indent(t,n,r,d)
if("number"==typeof a)return a}var l=n.prev&&"switch"==n.prev.info
if(s.allmanIndentation&&/[{(]/.test(i)){for(;"top"!=n.type&&"}"!=n.type;)n=n.prev
return n.indented}return"statement"==n.type?n.indented+("{"==i?0:f):!n.align||p&&")"==n.type?")"!=n.type||o?n.indented+(o?0:d)+(o||!l||/^(?:case|default)\b/.test(r)?0:d):n.indented+f:n.column+(o?0:1)},electricInput:_?/^\s*(?:case .*?:|default:|\{\}?|\})$/:/^\s*[{}]$/,blockCommentStart:"/*",blockCommentEnd:"*/",blockCommentContinue:" * ",lineComment:"//",fold:"brace"}}))
var s="auto if break case register continue return default do sizeof static else struct switch extern typedef union for goto while enum const volatile inline restrict asm fortran",c="alignas alignof and and_eq audit axiom bitand bitor catch class compl concept constexpr const_cast decltype delete dynamic_cast explicit export final friend import module mutable namespace new noexcept not not_eq operator or or_eq override private protected public reinterpret_cast requires static_assert static_cast template this thread_local throw try typeid typename using virtual xor xor_eq",u="bycopy byref in inout oneway out self super atomic nonatomic retain copy readwrite readonly strong weak assign typeof nullable nonnull null_resettable _cmd @interface @implementation @end @protocol @encode @property @synthesize @dynamic @class @public @package @private @protected @required @optional @try @catch @finally @import @selector @encode @defs @synchronized @autoreleasepool @compatibility_alias @available",d="FOUNDATION_EXPORT FOUNDATION_EXTERN NS_INLINE NS_FORMAT_FUNCTION  NS_RETURNS_RETAINEDNS_ERROR_ENUM NS_RETURNS_NOT_RETAINED NS_RETURNS_INNER_POINTER NS_DESIGNATED_INITIALIZER NS_ENUM NS_OPTIONS NS_REQUIRES_NIL_TERMINATION NS_ASSUME_NONNULL_BEGIN NS_ASSUME_NONNULL_END NS_SWIFT_NAME NS_REFINED_FOR_SWIFT",f=a("int long char short double float unsigned signed void bool"),p=a("SEL instancetype id Class Protocol BOOL")
function h(e){return l(f,e)||/.+_t$/.test(e)}function m(e){return h(e)||l(p,e)}var g="case do else for if switch while struct enum union",v="struct enum union"
function y(e,t){if(!t.startOfLine)return!1
for(var r,n=null;r=e.peek();){if("\\"==r&&e.match(/^.$/)){n=y
break}if("/"==r&&e.match(/^\/[\/\*]/,!1))break
e.next()}return t.tokenize=n,"meta"}function b(e,t){return"type"==t.prevToken&&"type"}function x(e){return!(!e||e.length<2)&&("_"==e[0]&&("_"==e[1]||e[1]!==e[1].toLowerCase()))}function w(e){return e.eatWhile(/[\w\.']/),"number"}function k(e,t){if(e.backUp(1),e.match(/(R|u8R|uR|UR|LR)/)){var r=e.match(/"([^\s\\()]{0,16})\(/)
return!!r&&(t.cpp11RawStringDelim=r[1],t.tokenize=S,S(e,t))}return e.match(/(u8|u|U|L)/)?!!e.match(/["']/,!1)&&"string":(e.next(),!1)}function _(e){var t=/(\w+)::~?(\w+)$/.exec(e)
return t&&t[1]==t[2]}function C(e,t){for(var r;null!=(r=e.next());)if('"'==r&&!e.eat('"')){t.tokenize=null
break}return"string"}function S(e,t){var r=t.cpp11RawStringDelim.replace(/[^\w\s]/g,"\\$&")
return e.match(new RegExp(".*?\\)"+r+'"'))?t.tokenize=null:e.skipToEnd(),"string"}function T(t,r){"string"==typeof t&&(t=[t])
var n=[]
function i(e){if(e)for(var t in e)e.hasOwnProperty(t)&&n.push(t)}i(r.keywords),i(r.types),i(r.builtin),i(r.atoms),n.length&&(r.helperType=t[0],e.registerHelper("hintWords",t[0],n))
for(var o=0;o<t.length;++o)e.defineMIME(t[o],r)}function M(e,t){for(var r=!1;!e.eol();){if(!r&&e.match('"""')){t.tokenize=null
break}r="\\"==e.next()&&!r}return"string"}function L(e){return function(t,r){for(var n;n=t.next();){if("*"==n&&t.eat("/")){if(1==e){r.tokenize=null
break}return r.tokenize=L(e-1),r.tokenize(t,r)}if("/"==n&&t.eat("*"))return r.tokenize=L(e+1),r.tokenize(t,r)}return"comment"}}T(["text/x-csrc","text/x-c","text/x-chdr"],{name:"clike",keywords:a(s),types:h,blockKeywords:a(g),defKeywords:a(v),typeFirstDefinitions:!0,atoms:a("NULL true false"),isReservedIdentifier:x,hooks:{"#":y,"*":b},modeProps:{fold:["brace","include"]}}),T(["text/x-c++src","text/x-c++hdr"],{name:"clike",keywords:a(s+" "+c),types:h,blockKeywords:a(g+" class try catch"),defKeywords:a(v+" class namespace"),typeFirstDefinitions:!0,atoms:a("true false NULL nullptr"),dontIndentStatements:/^template$/,isIdentifierChar:/[\w\$_~\xa1-\uffff]/,isReservedIdentifier:x,hooks:{"#":y,"*":b,u:k,U:k,L:k,R:k,0:w,1:w,2:w,3:w,4:w,5:w,6:w,7:w,8:w,9:w,token:function(e,t,r){if("variable"==r&&"("==e.peek()&&(";"==t.prevToken||null==t.prevToken||"}"==t.prevToken)&&_(e.current()))return"def"}},namespaceSeparator:"::",modeProps:{fold:["brace","include"]}}),T("text/x-java",{name:"clike",keywords:a("abstract assert break case catch class const continue default do else enum extends final finally for goto if implements import instanceof interface native new package private protected public return static strictfp super switch synchronized this throw throws transient try volatile while @interface"),types:a("byte short int long float double boolean char void Boolean Byte Character Double Float Integer Long Number Object Short String StringBuffer StringBuilder Void"),blockKeywords:a("catch class do else finally for if switch try while"),defKeywords:a("class interface enum @interface"),typeFirstDefinitions:!0,atoms:a("true false null"),number:/^(?:0x[a-f\d_]+|0b[01_]+|(?:[\d_]+\.?\d*|\.\d+)(?:e[-+]?[\d_]+)?)(u|ll?|l|f)?/i,hooks:{"@":function(e){return!e.match("interface",!1)&&(e.eatWhile(/[\w\$_]/),"meta")}},modeProps:{fold:["brace","import"]}}),T("text/x-csharp",{name:"clike",keywords:a("abstract as async await base break case catch checked class const continue default delegate do else enum event explicit extern finally fixed for foreach goto if implicit in interface internal is lock namespace new operator out override params private protected public readonly ref return sealed sizeof stackalloc static struct switch this throw try typeof unchecked unsafe using virtual void volatile while add alias ascending descending dynamic from get global group into join let orderby partial remove select set value var yield"),types:a("Action Boolean Byte Char DateTime DateTimeOffset Decimal Double Func Guid Int16 Int32 Int64 Object SByte Single String Task TimeSpan UInt16 UInt32 UInt64 bool byte char decimal double short int long object sbyte float string ushort uint ulong"),blockKeywords:a("catch class do else finally for foreach if struct switch try while"),defKeywords:a("class interface namespace struct var"),typeFirstDefinitions:!0,atoms:a("true false null"),hooks:{"@":function(e,t){return e.eat('"')?(t.tokenize=C,C(e,t)):(e.eatWhile(/[\w\$_]/),"meta")}}}),T("text/x-scala",{name:"clike",keywords:a("abstract case catch class def do else extends final finally for forSome if implicit import lazy match new null object override package private protected return sealed super this throw trait try type val var while with yield _ assert assume require print println printf readLine readBoolean readByte readShort readChar readInt readLong readFloat readDouble"),types:a("AnyVal App Application Array BufferedIterator BigDecimal BigInt Char Console Either Enumeration Equiv Error Exception Fractional Function IndexedSeq Int Integral Iterable Iterator List Map Numeric Nil NotNull Option Ordered Ordering PartialFunction PartialOrdering Product Proxy Range Responder Seq Serializable Set Specializable Stream StringBuilder StringContext Symbol Throwable Traversable TraversableOnce Tuple Unit Vector Boolean Byte Character CharSequence Class ClassLoader Cloneable Comparable Compiler Double Exception Float Integer Long Math Number Object Package Pair Process Runtime Runnable SecurityManager Short StackTraceElement StrictMath String StringBuffer System Thread ThreadGroup ThreadLocal Throwable Triple Void"),multiLineStrings:!0,blockKeywords:a("catch class enum do else finally for forSome if match switch try while"),defKeywords:a("class enum def object package trait type val var"),atoms:a("true false null"),indentStatements:!1,indentSwitch:!1,isOperatorChar:/[+\-*&%=<>!?|\/#:@]/,hooks:{"@":function(e){return e.eatWhile(/[\w\$_]/),"meta"},'"':function(e,t){return!!e.match('""')&&(t.tokenize=M,t.tokenize(e,t))},"'":function(e){return e.eatWhile(/[\w\$_\xa1-\uffff]/),"atom"},"=":function(e,r){var n=r.context
return!("}"!=n.type||!n.align||!e.eat(">"))&&(r.context=new t(n.indented,n.column,n.type,n.info,null,n.prev),"operator")},"/":function(e,t){return!!e.eat("*")&&(t.tokenize=L(1),t.tokenize(e,t))}},modeProps:{closeBrackets:{pairs:'()[]{}""',triples:'"'}}}),T("text/x-kotlin",{name:"clike",keywords:a("package as typealias class interface this super val operator var fun for is in This throw return annotation break continue object if else while do try when !in !is as? file import where by get set abstract enum open inner override private public internal protected catch finally out final vararg reified dynamic companion constructor init sealed field property receiver param sparam lateinit data inline noinline tailrec external annotation crossinline const operator infix suspend actual expect setparam"),types:a("Boolean Byte Character CharSequence Class ClassLoader Cloneable Comparable Compiler Double Exception Float Integer Long Math Number Object Package Pair Process Runtime Runnable SecurityManager Short StackTraceElement StrictMath String StringBuffer System Thread ThreadGroup ThreadLocal Throwable Triple Void Annotation Any BooleanArray ByteArray Char CharArray DeprecationLevel DoubleArray Enum FloatArray Function Int IntArray Lazy LazyThreadSafetyMode LongArray Nothing ShortArray Unit"),intendSwitch:!1,indentStatements:!1,multiLineStrings:!0,number:/^(?:0x[a-f\d_]+|0b[01_]+|(?:[\d_]+(\.\d+)?|\.\d+)(?:e[-+]?[\d_]+)?)(u|ll?|l|f)?/i,blockKeywords:a("catch class do else finally for if where try while enum"),defKeywords:a("class val var object interface fun"),atoms:a("true false null this"),hooks:{"@":function(e){return e.eatWhile(/[\w\$_]/),"meta"},"*":function(e,t){return"."==t.prevToken?"variable":"operator"},'"':function(e,t){var r
return t.tokenize=(r=e.match('""'),function(e,t){for(var n,i=!1,o=!1;!e.eol();){if(!r&&!i&&e.match('"')){o=!0
break}if(r&&e.match('"""')){o=!0
break}n=e.next(),!i&&"$"==n&&e.match("{")&&e.skipTo("}"),i=!i&&"\\"==n&&!r}return!o&&r||(t.tokenize=null),"string"}),t.tokenize(e,t)},"/":function(e,t){return!!e.eat("*")&&(t.tokenize=L(1),t.tokenize(e,t))},indent:function(e,t,r,n){var i=r&&r.charAt(0)
return"}"!=e.prevToken&&")"!=e.prevToken||""!=r?"operator"==e.prevToken&&"}"!=r&&"}"!=e.context.type||"variable"==e.prevToken&&"."==i||("}"==e.prevToken||")"==e.prevToken)&&"."==i?2*n+t.indented:t.align&&"}"==t.type?t.indented+(e.context.type==(r||"").charAt(0)?0:n):void 0:e.indented}},modeProps:{closeBrackets:{triples:'"'}}}),T(["x-shader/x-vertex","x-shader/x-fragment"],{name:"clike",keywords:a("sampler1D sampler2D sampler3D samplerCube sampler1DShadow sampler2DShadow const attribute uniform varying break continue discard return for while do if else struct in out inout"),types:a("float int bool void vec2 vec3 vec4 ivec2 ivec3 ivec4 bvec2 bvec3 bvec4 mat2 mat3 mat4"),blockKeywords:a("for while do if else struct"),builtin:a("radians degrees sin cos tan asin acos atan pow exp log exp2 sqrt inversesqrt abs sign floor ceil fract mod min max clamp mix step smoothstep length distance dot cross normalize ftransform faceforward reflect refract matrixCompMult lessThan lessThanEqual greaterThan greaterThanEqual equal notEqual any all not texture1D texture1DProj texture1DLod texture1DProjLod texture2D texture2DProj texture2DLod texture2DProjLod texture3D texture3DProj texture3DLod texture3DProjLod textureCube textureCubeLod shadow1D shadow2D shadow1DProj shadow2DProj shadow1DLod shadow2DLod shadow1DProjLod shadow2DProjLod dFdx dFdy fwidth noise1 noise2 noise3 noise4"),atoms:a("true false gl_FragColor gl_SecondaryColor gl_Normal gl_Vertex gl_MultiTexCoord0 gl_MultiTexCoord1 gl_MultiTexCoord2 gl_MultiTexCoord3 gl_MultiTexCoord4 gl_MultiTexCoord5 gl_MultiTexCoord6 gl_MultiTexCoord7 gl_FogCoord gl_PointCoord gl_Position gl_PointSize gl_ClipVertex gl_FrontColor gl_BackColor gl_FrontSecondaryColor gl_BackSecondaryColor gl_TexCoord gl_FogFragCoord gl_FragCoord gl_FrontFacing gl_FragData gl_FragDepth gl_ModelViewMatrix gl_ProjectionMatrix gl_ModelViewProjectionMatrix gl_TextureMatrix gl_NormalMatrix gl_ModelViewMatrixInverse gl_ProjectionMatrixInverse gl_ModelViewProjectionMatrixInverse gl_TexureMatrixTranspose gl_ModelViewMatrixInverseTranspose gl_ProjectionMatrixInverseTranspose gl_ModelViewProjectionMatrixInverseTranspose gl_TextureMatrixInverseTranspose gl_NormalScale gl_DepthRange gl_ClipPlane gl_Point gl_FrontMaterial gl_BackMaterial gl_LightSource gl_LightModel gl_FrontLightModelProduct gl_BackLightModelProduct gl_TextureColor gl_EyePlaneS gl_EyePlaneT gl_EyePlaneR gl_EyePlaneQ gl_FogParameters gl_MaxLights gl_MaxClipPlanes gl_MaxTextureUnits gl_MaxTextureCoords gl_MaxVertexAttribs gl_MaxVertexUniformComponents gl_MaxVaryingFloats gl_MaxVertexTextureImageUnits gl_MaxTextureImageUnits gl_MaxFragmentUniformComponents gl_MaxCombineTextureImageUnits gl_MaxDrawBuffers"),indentSwitch:!1,hooks:{"#":y},modeProps:{fold:["brace","include"]}}),T("text/x-nesc",{name:"clike",keywords:a(s+" as atomic async call command component components configuration event generic implementation includes interface module new norace nx_struct nx_union post provides signal task uses abstract extends"),types:h,blockKeywords:a(g),atoms:a("null true false"),hooks:{"#":y},modeProps:{fold:["brace","include"]}}),T("text/x-objectivec",{name:"clike",keywords:a(s+" "+u),types:m,builtin:a(d),blockKeywords:a(g+" @synthesize @try @catch @finally @autoreleasepool @synchronized"),defKeywords:a(v+" @interface @implementation @protocol @class"),dontIndentStatements:/^@.*$/,typeFirstDefinitions:!0,atoms:a("YES NO NULL Nil nil true false nullptr"),isReservedIdentifier:x,hooks:{"#":y,"*":b},modeProps:{fold:["brace","include"]}}),T("text/x-objectivec++",{name:"clike",keywords:a(s+" "+u+" "+c),types:m,builtin:a(d),blockKeywords:a(g+" @synthesize @try @catch @finally @autoreleasepool @synchronized class try catch"),defKeywords:a(v+" @interface @implementation @protocol @class class namespace"),dontIndentStatements:/^@.*$|^template$/,typeFirstDefinitions:!0,atoms:a("YES NO NULL Nil nil true false nullptr"),isReservedIdentifier:x,hooks:{"#":y,"*":b,u:k,U:k,L:k,R:k,0:w,1:w,2:w,3:w,4:w,5:w,6:w,7:w,8:w,9:w,token:function(e,t,r){if("variable"==r&&"("==e.peek()&&(";"==t.prevToken||null==t.prevToken||"}"==t.prevToken)&&_(e.current()))return"def"}},namespaceSeparator:"::",modeProps:{fold:["brace","include"]}}),T("text/x-squirrel",{name:"clike",keywords:a("base break clone continue const default delete enum extends function in class foreach local resume return this throw typeof yield constructor instanceof static"),types:h,blockKeywords:a("case catch class else for foreach if switch try while"),defKeywords:a("function local class"),typeFirstDefinitions:!0,atoms:a("true false null"),hooks:{"#":y},modeProps:{fold:["brace","include"]}})
var z=null
function A(e){return function(t,r){for(var n,i=!1,o=!1;!t.eol();){if(!i&&t.match('"')&&("single"==e||t.match('""'))){o=!0
break}if(!i&&t.match("``")){z=A(e),o=!0
break}n=t.next(),i="single"==e&&!i&&"\\"==n}return o&&(r.tokenize=null),"string"}}T("text/x-ceylon",{name:"clike",keywords:a("abstracts alias assembly assert assign break case catch class continue dynamic else exists extends finally for function given if import in interface is let module new nonempty object of out outer package return satisfies super switch then this throw try value void while"),types:function(e){var t=e.charAt(0)
return t===t.toUpperCase()&&t!==t.toLowerCase()},blockKeywords:a("case catch class dynamic else finally for function if interface module new object switch try while"),defKeywords:a("class dynamic function interface module object package value"),builtin:a("abstract actual aliased annotation by default deprecated doc final formal late license native optional sealed see serializable shared suppressWarnings tagged throws variable"),isPunctuationChar:/[\[\]{}\(\),;\:\.`]/,isOperatorChar:/[+\-*&%=<>!?|^~:\/]/,numberStart:/[\d#$]/,number:/^(?:#[\da-fA-F_]+|\$[01_]+|[\d_]+[kMGTPmunpf]?|[\d_]+\.[\d_]+(?:[eE][-+]?\d+|[kMGTPmunpf]|)|)/i,multiLineStrings:!0,typeFirstDefinitions:!0,atoms:a("true false null larger smaller equal empty finished"),indentSwitch:!1,styleDefs:!1,hooks:{"@":function(e){return e.eatWhile(/[\w\$_]/),"meta"},'"':function(e,t){return t.tokenize=A(e.match('""')?"triple":"single"),t.tokenize(e,t)},"`":function(e,t){return!(!z||!e.match("`"))&&(t.tokenize=z,z=null,t.tokenize(e,t))},"'":function(e){return e.eatWhile(/[\w\$_\xa1-\uffff]/),"atom"},token:function(e,t,r){if(("variable"==r||"type"==r)&&"."==t.prevToken)return"variable-2"}},modeProps:{fold:["brace","import"],closeBrackets:{triples:'"'}}})})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
e.defineMode("clojure",(function(t){var r=["false","nil","true"],n=[".","catch","def","do","if","monitor-enter","monitor-exit","new","quote","recur","set!","throw","try","var"],i=["*","*'","*1","*2","*3","*agent*","*allow-unresolved-vars*","*assert*","*clojure-version*","*command-line-args*","*compile-files*","*compile-path*","*compiler-options*","*data-readers*","*default-data-reader-fn*","*e","*err*","*file*","*flush-on-newline*","*fn-loader*","*in*","*math-context*","*ns*","*out*","*print-dup*","*print-length*","*print-level*","*print-meta*","*print-namespace-maps*","*print-readably*","*read-eval*","*reader-resolver*","*source-path*","*suppress-read*","*unchecked-math*","*use-context-classloader*","*verbose-defrecords*","*warn-on-reflection*","+","+'","-","-'","->","->>","->ArrayChunk","->Eduction","->Vec","->VecNode","->VecSeq","-cache-protocol-fn","-reset-methods","..","/","<","<=","=","==",">",">=","EMPTY-NODE","Inst","StackTraceElement->vec","Throwable->map","accessor","aclone","add-classpath","add-watch","agent","agent-error","agent-errors","aget","alength","alias","all-ns","alter","alter-meta!","alter-var-root","amap","ancestors","and","any?","apply","areduce","array-map","as->","aset","aset-boolean","aset-byte","aset-char","aset-double","aset-float","aset-int","aset-long","aset-short","assert","assoc","assoc!","assoc-in","associative?","atom","await","await-for","await1","bases","bean","bigdec","bigint","biginteger","binding","bit-and","bit-and-not","bit-clear","bit-flip","bit-not","bit-or","bit-set","bit-shift-left","bit-shift-right","bit-test","bit-xor","boolean","boolean-array","boolean?","booleans","bound-fn","bound-fn*","bound?","bounded-count","butlast","byte","byte-array","bytes","bytes?","case","cast","cat","char","char-array","char-escape-string","char-name-string","char?","chars","chunk","chunk-append","chunk-buffer","chunk-cons","chunk-first","chunk-next","chunk-rest","chunked-seq?","class","class?","clear-agent-errors","clojure-version","coll?","comment","commute","comp","comparator","compare","compare-and-set!","compile","complement","completing","concat","cond","cond->","cond->>","condp","conj","conj!","cons","constantly","construct-proxy","contains?","count","counted?","create-ns","create-struct","cycle","dec","dec'","decimal?","declare","dedupe","default-data-readers","definline","definterface","defmacro","defmethod","defmulti","defn","defn-","defonce","defprotocol","defrecord","defstruct","deftype","delay","delay?","deliver","denominator","deref","derive","descendants","destructure","disj","disj!","dissoc","dissoc!","distinct","distinct?","doall","dorun","doseq","dosync","dotimes","doto","double","double-array","double?","doubles","drop","drop-last","drop-while","eduction","empty","empty?","ensure","ensure-reduced","enumeration-seq","error-handler","error-mode","eval","even?","every-pred","every?","ex-data","ex-info","extend","extend-protocol","extend-type","extenders","extends?","false?","ffirst","file-seq","filter","filterv","find","find-keyword","find-ns","find-protocol-impl","find-protocol-method","find-var","first","flatten","float","float-array","float?","floats","flush","fn","fn?","fnext","fnil","for","force","format","frequencies","future","future-call","future-cancel","future-cancelled?","future-done?","future?","gen-class","gen-interface","gensym","get","get-in","get-method","get-proxy-class","get-thread-bindings","get-validator","group-by","halt-when","hash","hash-combine","hash-map","hash-ordered-coll","hash-set","hash-unordered-coll","ident?","identical?","identity","if-let","if-not","if-some","ifn?","import","in-ns","inc","inc'","indexed?","init-proxy","inst-ms","inst-ms*","inst?","instance?","int","int-array","int?","integer?","interleave","intern","interpose","into","into-array","ints","io!","isa?","iterate","iterator-seq","juxt","keep","keep-indexed","key","keys","keyword","keyword?","last","lazy-cat","lazy-seq","let","letfn","line-seq","list","list*","list?","load","load-file","load-reader","load-string","loaded-libs","locking","long","long-array","longs","loop","macroexpand","macroexpand-1","make-array","make-hierarchy","map","map-entry?","map-indexed","map?","mapcat","mapv","max","max-key","memfn","memoize","merge","merge-with","meta","method-sig","methods","min","min-key","mix-collection-hash","mod","munge","name","namespace","namespace-munge","nat-int?","neg-int?","neg?","newline","next","nfirst","nil?","nnext","not","not-any?","not-empty","not-every?","not=","ns","ns-aliases","ns-imports","ns-interns","ns-map","ns-name","ns-publics","ns-refers","ns-resolve","ns-unalias","ns-unmap","nth","nthnext","nthrest","num","number?","numerator","object-array","odd?","or","parents","partial","partition","partition-all","partition-by","pcalls","peek","persistent!","pmap","pop","pop!","pop-thread-bindings","pos-int?","pos?","pr","pr-str","prefer-method","prefers","primitives-classnames","print","print-ctor","print-dup","print-method","print-simple","print-str","printf","println","println-str","prn","prn-str","promise","proxy","proxy-call-with-super","proxy-mappings","proxy-name","proxy-super","push-thread-bindings","pvalues","qualified-ident?","qualified-keyword?","qualified-symbol?","quot","rand","rand-int","rand-nth","random-sample","range","ratio?","rational?","rationalize","re-find","re-groups","re-matcher","re-matches","re-pattern","re-seq","read","read-line","read-string","reader-conditional","reader-conditional?","realized?","record?","reduce","reduce-kv","reduced","reduced?","reductions","ref","ref-history-count","ref-max-history","ref-min-history","ref-set","refer","refer-clojure","reify","release-pending-sends","rem","remove","remove-all-methods","remove-method","remove-ns","remove-watch","repeat","repeatedly","replace","replicate","require","reset!","reset-meta!","reset-vals!","resolve","rest","restart-agent","resultset-seq","reverse","reversible?","rseq","rsubseq","run!","satisfies?","second","select-keys","send","send-off","send-via","seq","seq?","seqable?","seque","sequence","sequential?","set","set-agent-send-executor!","set-agent-send-off-executor!","set-error-handler!","set-error-mode!","set-validator!","set?","short","short-array","shorts","shuffle","shutdown-agents","simple-ident?","simple-keyword?","simple-symbol?","slurp","some","some->","some->>","some-fn","some?","sort","sort-by","sorted-map","sorted-map-by","sorted-set","sorted-set-by","sorted?","special-symbol?","spit","split-at","split-with","str","string?","struct","struct-map","subs","subseq","subvec","supers","swap!","swap-vals!","symbol","symbol?","sync","tagged-literal","tagged-literal?","take","take-last","take-nth","take-while","test","the-ns","thread-bound?","time","to-array","to-array-2d","trampoline","transduce","transient","tree-seq","true?","type","unchecked-add","unchecked-add-int","unchecked-byte","unchecked-char","unchecked-dec","unchecked-dec-int","unchecked-divide-int","unchecked-double","unchecked-float","unchecked-inc","unchecked-inc-int","unchecked-int","unchecked-long","unchecked-multiply","unchecked-multiply-int","unchecked-negate","unchecked-negate-int","unchecked-remainder-int","unchecked-short","unchecked-subtract","unchecked-subtract-int","underive","unquote","unquote-splicing","unreduced","unsigned-bit-shift-right","update","update-in","update-proxy","uri?","use","uuid?","val","vals","var-get","var-set","var?","vary-meta","vec","vector","vector-of","vector?","volatile!","volatile?","vreset!","vswap!","when","when-first","when-let","when-not","when-some","while","with-bindings","with-bindings*","with-in-str","with-loading-context","with-local-vars","with-meta","with-open","with-out-str","with-precision","with-redefs","with-redefs-fn","xml-seq","zero?","zipmap"]
e.registerHelper("hintWords","clojure",[].concat(r,n,i))
var o=g(r),a=g(n),l=g(i),s=g(["->","->>","as->","binding","bound-fn","case","catch","comment","cond","cond->","cond->>","condp","def","definterface","defmethod","defn","defmacro","defprotocol","defrecord","defstruct","deftype","do","doseq","dotimes","doto","extend","extend-protocol","extend-type","fn","for","future","if","if-let","if-not","if-some","let","letfn","locking","loop","ns","proxy","reify","struct-map","some->","some->>","try","when","when-first","when-let","when-not","when-some","while","with-bindings","with-bindings*","with-in-str","with-loading-context","with-local-vars","with-meta","with-open","with-out-str","with-precision","with-redefs","with-redefs-fn"]),c=/^(?:[\\\[\]\s"(),;@^`{}~]|$)/,u=/^(?:[+\-]?\d+(?:(?:N|(?:[eE][+\-]?\d+))|(?:\.?\d*(?:M|(?:[eE][+\-]?\d+))?)|\/\d+|[xX][0-9a-fA-F]+|r[0-9a-zA-Z]+)?(?=[\\\[\]\s"#'(),;@^`{}~]|$))/,d=/^(?:\\(?:backspace|formfeed|newline|return|space|tab|o[0-7]{3}|u[0-9A-Fa-f]{4}|x[0-9A-Fa-f]{4}|.)?(?=[\\\[\]\s"(),;@^`{}~]|$))/,f=/^(?:(?:[^\\\/\[\]\d\s"#'(),;@^`{}~][^\\\[\]\s"(),;@^`{}~]*(?:\.[^\\\/\[\]\d\s"#'(),;@^`{}~][^\\\[\]\s"(),;@^`{}~]*)*\/)?(?:\/|[^\\\/\[\]\d\s"#'(),;@^`{}~][^\\\[\]\s"(),;@^`{}~]*)*(?=[\\\[\]\s"(),;@^`{}~]|$))/
function p(e,t){if(e.eatSpace()||e.eat(","))return["space",null]
if(e.match(u))return[null,"number"]
if(e.match(d))return[null,"string-2"]
if(e.eat(/^"/))return(t.tokenize=h)(e,t)
if(e.eat(/^[(\[{]/))return["open","bracket"]
if(e.eat(/^[)\]}]/))return["close","bracket"]
if(e.eat(/^;/))return e.skipToEnd(),["space","comment"]
if(e.eat(/^[#'@^`~]/))return[null,"meta"]
var r=e.match(f),n=r&&r[0]
return n?"comment"===n&&"("===t.lastToken?(t.tokenize=m)(e,t):v(n,o)||":"===n.charAt(0)?["symbol","atom"]:v(n,a)||v(n,l)?["symbol","keyword"]:"("===t.lastToken?["symbol","builtin"]:["symbol","variable"]:(e.next(),e.eatWhile((function(e){return!v(e,c)})),[null,"error"])}function h(e,t){for(var r,n=!1;r=e.next();){if('"'===r&&!n){t.tokenize=p
break}n=!n&&"\\"===r}return[null,"string"]}function m(e,t){for(var r,n=1;r=e.next();)if(")"===r&&n--,"("===r&&n++,0===n){e.backUp(1),t.tokenize=p
break}return["space","comment"]}function g(e){for(var t={},r=0;r<e.length;++r)t[e[r]]=!0
return t}function v(e,t){return t instanceof RegExp?t.test(e):t instanceof Object?t.propertyIsEnumerable(e):void 0}return{startState:function(){return{ctx:{prev:null,start:0,indentTo:0},lastToken:null,tokenize:p}},token:function(e,r){e.sol()&&"number"!=typeof r.ctx.indentTo&&(r.ctx.indentTo=r.ctx.start+1)
var n=r.tokenize(e,r),i=n[0],o=n[1],a=e.current()
return"space"!==i&&("("===r.lastToken&&null===r.ctx.indentTo?"symbol"===i&&v(a,s)?r.ctx.indentTo=r.ctx.start+t.indentUnit:r.ctx.indentTo="next":"next"===r.ctx.indentTo&&(r.ctx.indentTo=e.column()),r.lastToken=a),"open"===i?r.ctx={prev:r.ctx,start:e.column(),indentTo:null}:"close"===i&&(r.ctx=r.ctx.prev||r.ctx),o},indent:function(e){var t=e.ctx.indentTo
return"number"==typeof t?t:e.ctx.start+1},closeBrackets:{pairs:'()[]{}""'},lineComment:";;"}})),e.defineMIME("text/x-clojure","clojure"),e.defineMIME("text/x-clojurescript","clojure"),e.defineMIME("application/edn","clojure")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
function t(e){for(var t={},r=0;r<e.length;++r)t[e[r].toLowerCase()]=!0
return t}e.defineMode("css",(function(t,r){var n=r.inline
r.propertyKeywords||(r=e.resolveMode("text/css"))
var i,o,a=t.indentUnit,l=r.tokenHooks,s=r.documentTypes||{},c=r.mediaTypes||{},u=r.mediaFeatures||{},d=r.mediaValueKeywords||{},f=r.propertyKeywords||{},p=r.nonStandardPropertyKeywords||{},h=r.fontProperties||{},m=r.counterDescriptors||{},g=r.colorKeywords||{},v=r.valueKeywords||{},y=r.allowNested,b=r.lineComment,x=!0===r.supportsAtComponent
function w(e,t){return i=t,e}function k(e,t){var r=e.next()
if(l[r]){var n=l[r](e,t)
if(!1!==n)return n}return"@"==r?(e.eatWhile(/[\w\\\-]/),w("def",e.current())):"="==r||("~"==r||"|"==r)&&e.eat("=")?w(null,"compare"):'"'==r||"'"==r?(t.tokenize=_(r),t.tokenize(e,t)):"#"==r?(e.eatWhile(/[\w\\\-]/),w("atom","hash")):"!"==r?(e.match(/^\s*\w*/),w("keyword","important")):/\d/.test(r)||"."==r&&e.eat(/\d/)?(e.eatWhile(/[\w.%]/),w("number","unit")):"-"!==r?/[,+>*\/]/.test(r)?w(null,"select-op"):"."==r&&e.match(/^-?[_a-z][_a-z0-9-]*/i)?w("qualifier","qualifier"):/[:;{}\[\]\(\)]/.test(r)?w(null,r):e.match(/[\w-.]+(?=\()/)?(/^(url(-prefix)?|domain|regexp)$/.test(e.current().toLowerCase())&&(t.tokenize=C),w("variable callee","variable")):/[\w\\\-]/.test(r)?(e.eatWhile(/[\w\\\-]/),w("property","word")):w(null,null):/[\d.]/.test(e.peek())?(e.eatWhile(/[\w.%]/),w("number","unit")):e.match(/^-[\w\\\-]*/)?(e.eatWhile(/[\w\\\-]/),e.match(/^\s*:/,!1)?w("variable-2","variable-definition"):w("variable-2","variable")):e.match(/^\w+-/)?w("meta","meta"):void 0}function _(e){return function(t,r){for(var n,i=!1;null!=(n=t.next());){if(n==e&&!i){")"==e&&t.backUp(1)
break}i=!i&&"\\"==n}return(n==e||!i&&")"!=e)&&(r.tokenize=null),w("string","string")}}function C(e,t){return e.next(),e.match(/\s*[\"\')]/,!1)?t.tokenize=null:t.tokenize=_(")"),w(null,"(")}function S(e,t,r){this.type=e,this.indent=t,this.prev=r}function T(e,t,r,n){return e.context=new S(r,t.indentation()+(!1===n?0:a),e.context),r}function M(e){return e.context.prev&&(e.context=e.context.prev),e.context.type}function L(e,t,r){return E[r.context.type](e,t,r)}function z(e,t,r,n){for(var i=n||1;i>0;i--)r.context=r.context.prev
return L(e,t,r)}function A(e){var t=e.current().toLowerCase()
o=v.hasOwnProperty(t)?"atom":g.hasOwnProperty(t)?"keyword":"variable"}var E={top:function(e,t,r){if("{"==e)return T(r,t,"block")
if("}"==e&&r.context.prev)return M(r)
if(x&&/@component/i.test(e))return T(r,t,"atComponentBlock")
if(/^@(-moz-)?document$/i.test(e))return T(r,t,"documentTypes")
if(/^@(media|supports|(-moz-)?document|import)$/i.test(e))return T(r,t,"atBlock")
if(/^@(font-face|counter-style)/i.test(e))return r.stateArg=e,"restricted_atBlock_before"
if(/^@(-(moz|ms|o|webkit)-)?keyframes$/i.test(e))return"keyframes"
if(e&&"@"==e.charAt(0))return T(r,t,"at")
if("hash"==e)o="builtin"
else if("word"==e)o="tag"
else{if("variable-definition"==e)return"maybeprop"
if("interpolation"==e)return T(r,t,"interpolation")
if(":"==e)return"pseudo"
if(y&&"("==e)return T(r,t,"parens")}return r.context.type},block:function(e,t,r){if("word"==e){var n=t.current().toLowerCase()
return f.hasOwnProperty(n)?(o="property","maybeprop"):p.hasOwnProperty(n)?(o="string-2","maybeprop"):y?(o=t.match(/^\s*:(?:\s|$)/,!1)?"property":"tag","block"):(o+=" error","maybeprop")}return"meta"==e?"block":y||"hash"!=e&&"qualifier"!=e?E.top(e,t,r):(o="error","block")},maybeprop:function(e,t,r){return":"==e?T(r,t,"prop"):L(e,t,r)},prop:function(e,t,r){if(";"==e)return M(r)
if("{"==e&&y)return T(r,t,"propBlock")
if("}"==e||"{"==e)return z(e,t,r)
if("("==e)return T(r,t,"parens")
if("hash"!=e||/^#([0-9a-fA-f]{3,4}|[0-9a-fA-f]{6}|[0-9a-fA-f]{8})$/.test(t.current())){if("word"==e)A(t)
else if("interpolation"==e)return T(r,t,"interpolation")}else o+=" error"
return"prop"},propBlock:function(e,t,r){return"}"==e?M(r):"word"==e?(o="property","maybeprop"):r.context.type},parens:function(e,t,r){return"{"==e||"}"==e?z(e,t,r):")"==e?M(r):"("==e?T(r,t,"parens"):"interpolation"==e?T(r,t,"interpolation"):("word"==e&&A(t),"parens")},pseudo:function(e,t,r){return"meta"==e?"pseudo":"word"==e?(o="variable-3",r.context.type):L(e,t,r)},documentTypes:function(e,t,r){return"word"==e&&s.hasOwnProperty(t.current())?(o="tag",r.context.type):E.atBlock(e,t,r)},atBlock:function(e,t,r){if("("==e)return T(r,t,"atBlock_parens")
if("}"==e||";"==e)return z(e,t,r)
if("{"==e)return M(r)&&T(r,t,y?"block":"top")
if("interpolation"==e)return T(r,t,"interpolation")
if("word"==e){var n=t.current().toLowerCase()
o="only"==n||"not"==n||"and"==n||"or"==n?"keyword":c.hasOwnProperty(n)?"attribute":u.hasOwnProperty(n)?"property":d.hasOwnProperty(n)?"keyword":f.hasOwnProperty(n)?"property":p.hasOwnProperty(n)?"string-2":v.hasOwnProperty(n)?"atom":g.hasOwnProperty(n)?"keyword":"error"}return r.context.type},atComponentBlock:function(e,t,r){return"}"==e?z(e,t,r):"{"==e?M(r)&&T(r,t,y?"block":"top",!1):("word"==e&&(o="error"),r.context.type)},atBlock_parens:function(e,t,r){return")"==e?M(r):"{"==e||"}"==e?z(e,t,r,2):E.atBlock(e,t,r)},restricted_atBlock_before:function(e,t,r){return"{"==e?T(r,t,"restricted_atBlock"):"word"==e&&"@counter-style"==r.stateArg?(o="variable","restricted_atBlock_before"):L(e,t,r)},restricted_atBlock:function(e,t,r){return"}"==e?(r.stateArg=null,M(r)):"word"==e?(o="@font-face"==r.stateArg&&!h.hasOwnProperty(t.current().toLowerCase())||"@counter-style"==r.stateArg&&!m.hasOwnProperty(t.current().toLowerCase())?"error":"property","maybeprop"):"restricted_atBlock"},keyframes:function(e,t,r){return"word"==e?(o="variable","keyframes"):"{"==e?T(r,t,"top"):L(e,t,r)},at:function(e,t,r){return";"==e?M(r):"{"==e||"}"==e?z(e,t,r):("word"==e?o="tag":"hash"==e&&(o="builtin"),"at")},interpolation:function(e,t,r){return"}"==e?M(r):"{"==e||";"==e?z(e,t,r):("word"==e?o="variable":"variable"!=e&&"("!=e&&")"!=e&&(o="error"),"interpolation")}}
return{startState:function(e){return{tokenize:null,state:n?"block":"top",stateArg:null,context:new S(n?"block":"top",e||0,null)}},token:function(e,t){if(!t.tokenize&&e.eatSpace())return null
var r=(t.tokenize||k)(e,t)
return r&&"object"==typeof r&&(i=r[1],r=r[0]),o=r,"comment"!=i&&(t.state=E[t.state](i,e,t)),o},indent:function(e,t){var r=e.context,n=t&&t.charAt(0),i=r.indent
return"prop"!=r.type||"}"!=n&&")"!=n||(r=r.prev),r.prev&&("}"!=n||"block"!=r.type&&"top"!=r.type&&"interpolation"!=r.type&&"restricted_atBlock"!=r.type?(")"!=n||"parens"!=r.type&&"atBlock_parens"!=r.type)&&("{"!=n||"at"!=r.type&&"atBlock"!=r.type)||(i=Math.max(0,r.indent-a)):i=(r=r.prev).indent),i},electricChars:"}",blockCommentStart:"/*",blockCommentEnd:"*/",blockCommentContinue:" * ",lineComment:b,fold:"brace"}}))
var r=["domain","regexp","url","url-prefix"],n=t(r),i=["all","aural","braille","handheld","print","projection","screen","tty","tv","embossed"],o=t(i),a=["width","min-width","max-width","height","min-height","max-height","device-width","min-device-width","max-device-width","device-height","min-device-height","max-device-height","aspect-ratio","min-aspect-ratio","max-aspect-ratio","device-aspect-ratio","min-device-aspect-ratio","max-device-aspect-ratio","color","min-color","max-color","color-index","min-color-index","max-color-index","monochrome","min-monochrome","max-monochrome","resolution","min-resolution","max-resolution","scan","grid","orientation","device-pixel-ratio","min-device-pixel-ratio","max-device-pixel-ratio","pointer","any-pointer","hover","any-hover"],l=t(a),s=["landscape","portrait","none","coarse","fine","on-demand","hover","interlace","progressive"],c=t(s),u=["align-content","align-items","align-self","alignment-adjust","alignment-baseline","anchor-point","animation","animation-delay","animation-direction","animation-duration","animation-fill-mode","animation-iteration-count","animation-name","animation-play-state","animation-timing-function","appearance","azimuth","backface-visibility","background","background-attachment","background-blend-mode","background-clip","background-color","background-image","background-origin","background-position","background-repeat","background-size","baseline-shift","binding","bleed","bookmark-label","bookmark-level","bookmark-state","bookmark-target","border","border-bottom","border-bottom-color","border-bottom-left-radius","border-bottom-right-radius","border-bottom-style","border-bottom-width","border-collapse","border-color","border-image","border-image-outset","border-image-repeat","border-image-slice","border-image-source","border-image-width","border-left","border-left-color","border-left-style","border-left-width","border-radius","border-right","border-right-color","border-right-style","border-right-width","border-spacing","border-style","border-top","border-top-color","border-top-left-radius","border-top-right-radius","border-top-style","border-top-width","border-width","bottom","box-decoration-break","box-shadow","box-sizing","break-after","break-before","break-inside","caption-side","caret-color","clear","clip","color","color-profile","column-count","column-fill","column-gap","column-rule","column-rule-color","column-rule-style","column-rule-width","column-span","column-width","columns","content","counter-increment","counter-reset","crop","cue","cue-after","cue-before","cursor","direction","display","dominant-baseline","drop-initial-after-adjust","drop-initial-after-align","drop-initial-before-adjust","drop-initial-before-align","drop-initial-size","drop-initial-value","elevation","empty-cells","fit","fit-position","flex","flex-basis","flex-direction","flex-flow","flex-grow","flex-shrink","flex-wrap","float","float-offset","flow-from","flow-into","font","font-feature-settings","font-family","font-kerning","font-language-override","font-size","font-size-adjust","font-stretch","font-style","font-synthesis","font-variant","font-variant-alternates","font-variant-caps","font-variant-east-asian","font-variant-ligatures","font-variant-numeric","font-variant-position","font-weight","grid","grid-area","grid-auto-columns","grid-auto-flow","grid-auto-rows","grid-column","grid-column-end","grid-column-gap","grid-column-start","grid-gap","grid-row","grid-row-end","grid-row-gap","grid-row-start","grid-template","grid-template-areas","grid-template-columns","grid-template-rows","hanging-punctuation","height","hyphens","icon","image-orientation","image-rendering","image-resolution","inline-box-align","justify-content","justify-items","justify-self","left","letter-spacing","line-break","line-height","line-stacking","line-stacking-ruby","line-stacking-shift","line-stacking-strategy","list-style","list-style-image","list-style-position","list-style-type","margin","margin-bottom","margin-left","margin-right","margin-top","marks","marquee-direction","marquee-loop","marquee-play-count","marquee-speed","marquee-style","max-height","max-width","min-height","min-width","mix-blend-mode","move-to","nav-down","nav-index","nav-left","nav-right","nav-up","object-fit","object-position","opacity","order","orphans","outline","outline-color","outline-offset","outline-style","outline-width","overflow","overflow-style","overflow-wrap","overflow-x","overflow-y","padding","padding-bottom","padding-left","padding-right","padding-top","page","page-break-after","page-break-before","page-break-inside","page-policy","pause","pause-after","pause-before","perspective","perspective-origin","pitch","pitch-range","place-content","place-items","place-self","play-during","position","presentation-level","punctuation-trim","quotes","region-break-after","region-break-before","region-break-inside","region-fragment","rendering-intent","resize","rest","rest-after","rest-before","richness","right","rotation","rotation-point","ruby-align","ruby-overhang","ruby-position","ruby-span","shape-image-threshold","shape-inside","shape-margin","shape-outside","size","speak","speak-as","speak-header","speak-numeral","speak-punctuation","speech-rate","stress","string-set","tab-size","table-layout","target","target-name","target-new","target-position","text-align","text-align-last","text-decoration","text-decoration-color","text-decoration-line","text-decoration-skip","text-decoration-style","text-emphasis","text-emphasis-color","text-emphasis-position","text-emphasis-style","text-height","text-indent","text-justify","text-outline","text-overflow","text-shadow","text-size-adjust","text-space-collapse","text-transform","text-underline-position","text-wrap","top","transform","transform-origin","transform-style","transition","transition-delay","transition-duration","transition-property","transition-timing-function","unicode-bidi","user-select","vertical-align","visibility","voice-balance","voice-duration","voice-family","voice-pitch","voice-range","voice-rate","voice-stress","voice-volume","volume","white-space","widows","width","will-change","word-break","word-spacing","word-wrap","z-index","clip-path","clip-rule","mask","enable-background","filter","flood-color","flood-opacity","lighting-color","stop-color","stop-opacity","pointer-events","color-interpolation","color-interpolation-filters","color-rendering","fill","fill-opacity","fill-rule","image-rendering","marker","marker-end","marker-mid","marker-start","shape-rendering","stroke","stroke-dasharray","stroke-dashoffset","stroke-linecap","stroke-linejoin","stroke-miterlimit","stroke-opacity","stroke-width","text-rendering","baseline-shift","dominant-baseline","glyph-orientation-horizontal","glyph-orientation-vertical","text-anchor","writing-mode"],d=t(u),f=["scrollbar-arrow-color","scrollbar-base-color","scrollbar-dark-shadow-color","scrollbar-face-color","scrollbar-highlight-color","scrollbar-shadow-color","scrollbar-3d-light-color","scrollbar-track-color","shape-inside","searchfield-cancel-button","searchfield-decoration","searchfield-results-button","searchfield-results-decoration","zoom"],p=t(f),h=t(["font-family","src","unicode-range","font-variant","font-feature-settings","font-stretch","font-weight","font-style"]),m=t(["additive-symbols","fallback","negative","pad","prefix","range","speak-as","suffix","symbols","system"]),g=["aliceblue","antiquewhite","aqua","aquamarine","azure","beige","bisque","black","blanchedalmond","blue","blueviolet","brown","burlywood","cadetblue","chartreuse","chocolate","coral","cornflowerblue","cornsilk","crimson","cyan","darkblue","darkcyan","darkgoldenrod","darkgray","darkgreen","darkkhaki","darkmagenta","darkolivegreen","darkorange","darkorchid","darkred","darksalmon","darkseagreen","darkslateblue","darkslategray","darkturquoise","darkviolet","deeppink","deepskyblue","dimgray","dodgerblue","firebrick","floralwhite","forestgreen","fuchsia","gainsboro","ghostwhite","gold","goldenrod","gray","grey","green","greenyellow","honeydew","hotpink","indianred","indigo","ivory","khaki","lavender","lavenderblush","lawngreen","lemonchiffon","lightblue","lightcoral","lightcyan","lightgoldenrodyellow","lightgray","lightgreen","lightpink","lightsalmon","lightseagreen","lightskyblue","lightslategray","lightsteelblue","lightyellow","lime","limegreen","linen","magenta","maroon","mediumaquamarine","mediumblue","mediumorchid","mediumpurple","mediumseagreen","mediumslateblue","mediumspringgreen","mediumturquoise","mediumvioletred","midnightblue","mintcream","mistyrose","moccasin","navajowhite","navy","oldlace","olive","olivedrab","orange","orangered","orchid","palegoldenrod","palegreen","paleturquoise","palevioletred","papayawhip","peachpuff","peru","pink","plum","powderblue","purple","rebeccapurple","red","rosybrown","royalblue","saddlebrown","salmon","sandybrown","seagreen","seashell","sienna","silver","skyblue","slateblue","slategray","snow","springgreen","steelblue","tan","teal","thistle","tomato","turquoise","violet","wheat","white","whitesmoke","yellow","yellowgreen"],v=t(g),y=["above","absolute","activeborder","additive","activecaption","afar","after-white-space","ahead","alias","all","all-scroll","alphabetic","alternate","always","amharic","amharic-abegede","antialiased","appworkspace","arabic-indic","armenian","asterisks","attr","auto","auto-flow","avoid","avoid-column","avoid-page","avoid-region","background","backwards","baseline","below","bidi-override","binary","bengali","blink","block","block-axis","bold","bolder","border","border-box","both","bottom","break","break-all","break-word","bullets","button","button-bevel","buttonface","buttonhighlight","buttonshadow","buttontext","calc","cambodian","capitalize","caps-lock-indicator","caption","captiontext","caret","cell","center","checkbox","circle","cjk-decimal","cjk-earthly-branch","cjk-heavenly-stem","cjk-ideographic","clear","clip","close-quote","col-resize","collapse","color","color-burn","color-dodge","column","column-reverse","compact","condensed","contain","content","contents","content-box","context-menu","continuous","copy","counter","counters","cover","crop","cross","crosshair","currentcolor","cursive","cyclic","darken","dashed","decimal","decimal-leading-zero","default","default-button","dense","destination-atop","destination-in","destination-out","destination-over","devanagari","difference","disc","discard","disclosure-closed","disclosure-open","document","dot-dash","dot-dot-dash","dotted","double","down","e-resize","ease","ease-in","ease-in-out","ease-out","element","ellipse","ellipsis","embed","end","ethiopic","ethiopic-abegede","ethiopic-abegede-am-et","ethiopic-abegede-gez","ethiopic-abegede-ti-er","ethiopic-abegede-ti-et","ethiopic-halehame-aa-er","ethiopic-halehame-aa-et","ethiopic-halehame-am-et","ethiopic-halehame-gez","ethiopic-halehame-om-et","ethiopic-halehame-sid-et","ethiopic-halehame-so-et","ethiopic-halehame-ti-er","ethiopic-halehame-ti-et","ethiopic-halehame-tig","ethiopic-numeric","ew-resize","exclusion","expanded","extends","extra-condensed","extra-expanded","fantasy","fast","fill","fixed","flat","flex","flex-end","flex-start","footnotes","forwards","from","geometricPrecision","georgian","graytext","grid","groove","gujarati","gurmukhi","hand","hangul","hangul-consonant","hard-light","hebrew","help","hidden","hide","higher","highlight","highlighttext","hiragana","hiragana-iroha","horizontal","hsl","hsla","hue","icon","ignore","inactiveborder","inactivecaption","inactivecaptiontext","infinite","infobackground","infotext","inherit","initial","inline","inline-axis","inline-block","inline-flex","inline-grid","inline-table","inset","inside","intrinsic","invert","italic","japanese-formal","japanese-informal","justify","kannada","katakana","katakana-iroha","keep-all","khmer","korean-hangul-formal","korean-hanja-formal","korean-hanja-informal","landscape","lao","large","larger","left","level","lighter","lighten","line-through","linear","linear-gradient","lines","list-item","listbox","listitem","local","logical","loud","lower","lower-alpha","lower-armenian","lower-greek","lower-hexadecimal","lower-latin","lower-norwegian","lower-roman","lowercase","ltr","luminosity","malayalam","match","matrix","matrix3d","media-controls-background","media-current-time-display","media-fullscreen-button","media-mute-button","media-play-button","media-return-to-realtime-button","media-rewind-button","media-seek-back-button","media-seek-forward-button","media-slider","media-sliderthumb","media-time-remaining-display","media-volume-slider","media-volume-slider-container","media-volume-sliderthumb","medium","menu","menulist","menulist-button","menulist-text","menulist-textfield","menutext","message-box","middle","min-intrinsic","mix","mongolian","monospace","move","multiple","multiply","myanmar","n-resize","narrower","ne-resize","nesw-resize","no-close-quote","no-drop","no-open-quote","no-repeat","none","normal","not-allowed","nowrap","ns-resize","numbers","numeric","nw-resize","nwse-resize","oblique","octal","opacity","open-quote","optimizeLegibility","optimizeSpeed","oriya","oromo","outset","outside","outside-shape","overlay","overline","padding","padding-box","painted","page","paused","persian","perspective","plus-darker","plus-lighter","pointer","polygon","portrait","pre","pre-line","pre-wrap","preserve-3d","progress","push-button","radial-gradient","radio","read-only","read-write","read-write-plaintext-only","rectangle","region","relative","repeat","repeating-linear-gradient","repeating-radial-gradient","repeat-x","repeat-y","reset","reverse","rgb","rgba","ridge","right","rotate","rotate3d","rotateX","rotateY","rotateZ","round","row","row-resize","row-reverse","rtl","run-in","running","s-resize","sans-serif","saturation","scale","scale3d","scaleX","scaleY","scaleZ","screen","scroll","scrollbar","scroll-position","se-resize","searchfield","searchfield-cancel-button","searchfield-decoration","searchfield-results-button","searchfield-results-decoration","self-start","self-end","semi-condensed","semi-expanded","separate","serif","show","sidama","simp-chinese-formal","simp-chinese-informal","single","skew","skewX","skewY","skip-white-space","slide","slider-horizontal","slider-vertical","sliderthumb-horizontal","sliderthumb-vertical","slow","small","small-caps","small-caption","smaller","soft-light","solid","somali","source-atop","source-in","source-out","source-over","space","space-around","space-between","space-evenly","spell-out","square","square-button","start","static","status-bar","stretch","stroke","sub","subpixel-antialiased","super","sw-resize","symbolic","symbols","system-ui","table","table-caption","table-cell","table-column","table-column-group","table-footer-group","table-header-group","table-row","table-row-group","tamil","telugu","text","text-bottom","text-top","textarea","textfield","thai","thick","thin","threeddarkshadow","threedface","threedhighlight","threedlightshadow","threedshadow","tibetan","tigre","tigrinya-er","tigrinya-er-abegede","tigrinya-et","tigrinya-et-abegede","to","top","trad-chinese-formal","trad-chinese-informal","transform","translate","translate3d","translateX","translateY","translateZ","transparent","ultra-condensed","ultra-expanded","underline","unset","up","upper-alpha","upper-armenian","upper-greek","upper-hexadecimal","upper-latin","upper-norwegian","upper-roman","uppercase","urdu","url","var","vertical","vertical-text","visible","visibleFill","visiblePainted","visibleStroke","visual","w-resize","wait","wave","wider","window","windowframe","windowtext","words","wrap","wrap-reverse","x-large","x-small","xor","xx-large","xx-small"],b=t(y),x=r.concat(i).concat(a).concat(s).concat(u).concat(f).concat(g).concat(y)
function w(e,t){for(var r,n=!1;null!=(r=e.next());){if(n&&"/"==r){t.tokenize=null
break}n="*"==r}return["comment","comment"]}e.registerHelper("hintWords","css",x),e.defineMIME("text/css",{documentTypes:n,mediaTypes:o,mediaFeatures:l,mediaValueKeywords:c,propertyKeywords:d,nonStandardPropertyKeywords:p,fontProperties:h,counterDescriptors:m,colorKeywords:v,valueKeywords:b,tokenHooks:{"/":function(e,t){return!!e.eat("*")&&(t.tokenize=w,w(e,t))}},name:"css"}),e.defineMIME("text/x-scss",{mediaTypes:o,mediaFeatures:l,mediaValueKeywords:c,propertyKeywords:d,nonStandardPropertyKeywords:p,colorKeywords:v,valueKeywords:b,fontProperties:h,allowNested:!0,lineComment:"//",tokenHooks:{"/":function(e,t){return e.eat("/")?(e.skipToEnd(),["comment","comment"]):e.eat("*")?(t.tokenize=w,w(e,t)):["operator","operator"]},":":function(e){return!!e.match(/\s*\{/,!1)&&[null,null]},$:function(e){return e.match(/^[\w-]+/),e.match(/^\s*:/,!1)?["variable-2","variable-definition"]:["variable-2","variable"]},"#":function(e){return!!e.eat("{")&&[null,"interpolation"]}},name:"css",helperType:"scss"}),e.defineMIME("text/x-less",{mediaTypes:o,mediaFeatures:l,mediaValueKeywords:c,propertyKeywords:d,nonStandardPropertyKeywords:p,colorKeywords:v,valueKeywords:b,fontProperties:h,allowNested:!0,lineComment:"//",tokenHooks:{"/":function(e,t){return e.eat("/")?(e.skipToEnd(),["comment","comment"]):e.eat("*")?(t.tokenize=w,w(e,t)):["operator","operator"]},"@":function(e){return e.eat("{")?[null,"interpolation"]:!e.match(/^(charset|document|font-face|import|(-(moz|ms|o|webkit)-)?keyframes|media|namespace|page|supports)\b/i,!1)&&(e.eatWhile(/[\w\\\-]/),e.match(/^\s*:/,!1)?["variable-2","variable-definition"]:["variable-2","variable"])},"&":function(){return["atom","atom"]}},name:"css",helperType:"less"}),e.defineMIME("text/x-gss",{documentTypes:n,mediaTypes:o,mediaFeatures:l,propertyKeywords:d,nonStandardPropertyKeywords:p,fontProperties:h,counterDescriptors:m,colorKeywords:v,valueKeywords:b,supportsAtComponent:!0,tokenHooks:{"/":function(e,t){return!!e.eat("*")&&(t.tokenize=w,w(e,t))}},name:"css",helperType:"gss"})})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror"),require("../clike/clike")):"function"==typeof define&&define.amd?define(["../../lib/codemirror","../clike/clike"],e):e(CodeMirror)}((function(e){"use strict"
var t="this super static final const abstract class extends external factory implements mixin get native set typedef with enum throw rethrow assert break case continue default in return new deferred async await covariant try catch finally do else for if switch while import library export part of show hide is as extension on yield".split(" "),r="try catch finally do else for if switch while".split(" "),n="true false null".split(" "),i="void bool num int double dynamic var String".split(" ")
function o(e){for(var t={},r=0;r<e.length;++r)t[e[r]]=!0
return t}function a(e){(e.interpolationStack||(e.interpolationStack=[])).push(e.tokenize)}function l(e){return(e.interpolationStack||(e.interpolationStack=[])).pop()}function s(e,t,r,n){var i=!1
if(t.eat(e)){if(!t.eat(e))return"string"
i=!0}function o(t,r){for(var o=!1;!t.eol();){if(!n&&!o&&"$"==t.peek())return a(r),r.tokenize=c,"string"
var l=t.next()
if(l==e&&!o&&(!i||t.match(e+e))){r.tokenize=null
break}o=!n&&!o&&"\\"==l}return"string"}return r.tokenize=o,o(t,r)}function c(e,t){return e.eat("$"),e.eat("{")?t.tokenize=null:t.tokenize=u,null}function u(e,t){return e.eatWhile(/[\w_]/),t.tokenize=l(t),"variable"}function d(e){return function(t,r){for(var n;n=t.next();){if("*"==n&&t.eat("/")){if(1==e){r.tokenize=null
break}return r.tokenize=d(e-1),r.tokenize(t,r)}if("/"==n&&t.eat("*"))return r.tokenize=d(e+1),r.tokenize(t,r)}return"comment"}}e.defineMIME("application/dart",{name:"clike",keywords:o(t),blockKeywords:o(r),builtin:o(i),atoms:o(n),hooks:{"@":function(e){return e.eatWhile(/[\w\$_\.]/),"meta"},"'":function(e,t){return s("'",e,t,!1)},'"':function(e,t){return s('"',e,t,!1)},r:function(e,t){var r=e.peek()
return("'"==r||'"'==r)&&s(e.next(),e,t,!0)},"}":function(e,t){return function(e){return e.interpolationStack?e.interpolationStack.length:0}(t)>0&&(t.tokenize=l(t),null)},"/":function(e,t){return!!e.eat("*")&&(t.tokenize=d(1),t.tokenize(e,t))},token:function(e,t,r){if("variable"==r&&RegExp("^[_$]*[A-Z][a-zA-Z0-9_$]*$","g").test(e.current()))return"variable-2"}}}),e.registerHelper("hintWords","application/dart",t.concat(n).concat(i)),e.defineMode("dart",(function(t){return e.getMode(t,"application/dart")}),"clike")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
e.defineMode("gas",(function(e,t){var r=[],n="",i={".abort":"builtin",".align":"builtin",".altmacro":"builtin",".ascii":"builtin",".asciz":"builtin",".balign":"builtin",".balignw":"builtin",".balignl":"builtin",".bundle_align_mode":"builtin",".bundle_lock":"builtin",".bundle_unlock":"builtin",".byte":"builtin",".cfi_startproc":"builtin",".comm":"builtin",".data":"builtin",".def":"builtin",".desc":"builtin",".dim":"builtin",".double":"builtin",".eject":"builtin",".else":"builtin",".elseif":"builtin",".end":"builtin",".endef":"builtin",".endfunc":"builtin",".endif":"builtin",".equ":"builtin",".equiv":"builtin",".eqv":"builtin",".err":"builtin",".error":"builtin",".exitm":"builtin",".extern":"builtin",".fail":"builtin",".file":"builtin",".fill":"builtin",".float":"builtin",".func":"builtin",".global":"builtin",".gnu_attribute":"builtin",".hidden":"builtin",".hword":"builtin",".ident":"builtin",".if":"builtin",".incbin":"builtin",".include":"builtin",".int":"builtin",".internal":"builtin",".irp":"builtin",".irpc":"builtin",".lcomm":"builtin",".lflags":"builtin",".line":"builtin",".linkonce":"builtin",".list":"builtin",".ln":"builtin",".loc":"builtin",".loc_mark_labels":"builtin",".local":"builtin",".long":"builtin",".macro":"builtin",".mri":"builtin",".noaltmacro":"builtin",".nolist":"builtin",".octa":"builtin",".offset":"builtin",".org":"builtin",".p2align":"builtin",".popsection":"builtin",".previous":"builtin",".print":"builtin",".protected":"builtin",".psize":"builtin",".purgem":"builtin",".pushsection":"builtin",".quad":"builtin",".reloc":"builtin",".rept":"builtin",".sbttl":"builtin",".scl":"builtin",".section":"builtin",".set":"builtin",".short":"builtin",".single":"builtin",".size":"builtin",".skip":"builtin",".sleb128":"builtin",".space":"builtin",".stab":"builtin",".string":"builtin",".struct":"builtin",".subsection":"builtin",".symver":"builtin",".tag":"builtin",".text":"builtin",".title":"builtin",".type":"builtin",".uleb128":"builtin",".val":"builtin",".version":"builtin",".vtable_entry":"builtin",".vtable_inherit":"builtin",".warning":"builtin",".weak":"builtin",".weakref":"builtin",".word":"builtin"},o={}
var a=(t.architecture||"x86").toLowerCase()
function l(e,t){for(var r,n=!1;null!=(r=e.next());){if("/"===r&&n){t.tokenize=null
break}n="*"===r}return"comment"}return"x86"===a?function(e){n="#",o.ax="variable",o.eax="variable-2",o.rax="variable-3",o.bx="variable",o.ebx="variable-2",o.rbx="variable-3",o.cx="variable",o.ecx="variable-2",o.rcx="variable-3",o.dx="variable",o.edx="variable-2",o.rdx="variable-3",o.si="variable",o.esi="variable-2",o.rsi="variable-3",o.di="variable",o.edi="variable-2",o.rdi="variable-3",o.sp="variable",o.esp="variable-2",o.rsp="variable-3",o.bp="variable",o.ebp="variable-2",o.rbp="variable-3",o.ip="variable",o.eip="variable-2",o.rip="variable-3",o.cs="keyword",o.ds="keyword"
o.ss="keyword",o.es="keyword",o.fs="keyword",o.gs="keyword"}():"arm"!==a&&"armv6"!==a||(n="@",i.syntax="builtin",o.r0="variable",o.r1="variable",o.r2="variable",o.r3="variable",o.r4="variable",o.r5="variable",o.r6="variable",o.r7="variable",o.r8="variable",o.r9="variable",o.r10="variable",o.r11="variable",o.r12="variable",o.sp="variable-2",o.lr="variable-2",o.pc="variable-2",o.r13=o.sp,o.r14=o.lr,o.r15=o.pc,r.push((function(e,t){if("#"===e)return t.eatWhile(/\w/),"number"}))),{startState:function(){return{tokenize:null}},token:function(e,t){if(t.tokenize)return t.tokenize(e,t)
if(e.eatSpace())return null
var a,s,c=e.next()
if("/"===c&&e.eat("*"))return t.tokenize=l,l(e,t)
if(c===n)return e.skipToEnd(),"comment"
if('"'===c)return function(e,t){for(var r,n=!1;null!=(r=e.next());){if(r===t&&!n)return!1
n=!n&&"\\"===r}}(e,'"'),"string"
if("."===c)return e.eatWhile(/\w/),s=e.current().toLowerCase(),(a=i[s])||null
if("="===c)return e.eatWhile(/\w/),"tag"
if("{"===c)return"braket"
if("}"===c)return"braket"
if(/\d/.test(c))return"0"===c&&e.eat("x")?(e.eatWhile(/[0-9a-fA-F]/),"number"):(e.eatWhile(/\d/),"number")
if(/\w/.test(c))return e.eatWhile(/\w/),e.eat(":")?"tag":(s=e.current().toLowerCase(),(a=o[s])||null)
for(var u=0;u<r.length;u++)if(a=r[u](c,e,t))return a},lineComment:n,blockCommentStart:"/*",blockCommentEnd:"*/"}}))})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
e.defineMode("go",(function(t){var r,n=t.indentUnit,i={break:!0,case:!0,chan:!0,const:!0,continue:!0,default:!0,defer:!0,else:!0,fallthrough:!0,for:!0,func:!0,go:!0,goto:!0,if:!0,import:!0,interface:!0,map:!0,package:!0,range:!0,return:!0,select:!0,struct:!0,switch:!0,type:!0,var:!0,bool:!0,byte:!0,complex64:!0,complex128:!0,float32:!0,float64:!0,int8:!0,int16:!0,int32:!0,int64:!0,string:!0,uint8:!0,uint16:!0,uint32:!0,uint64:!0,int:!0,uint:!0,uintptr:!0,error:!0,rune:!0},o={true:!0,false:!0,iota:!0,nil:!0,append:!0,cap:!0,close:!0,complex:!0,copy:!0,delete:!0,imag:!0,len:!0,make:!0,new:!0,panic:!0,print:!0,println:!0,real:!0,recover:!0},a=/[+\-*&^%:=<>!|\/]/
function l(e,t){var n,c=e.next()
if('"'==c||"'"==c||"`"==c)return t.tokenize=(n=c,function(e,t){for(var r,i=!1,o=!1;null!=(r=e.next());){if(r==n&&!i){o=!0
break}i=!i&&"`"!=n&&"\\"==r}return(o||!i&&"`"!=n)&&(t.tokenize=l),"string"}),t.tokenize(e,t)
if(/[\d\.]/.test(c))return"."==c?e.match(/^[0-9]+([eE][\-+]?[0-9]+)?/):"0"==c?e.match(/^[xX][0-9a-fA-F]+/)||e.match(/^0[0-7]+/):e.match(/^[0-9]*\.?[0-9]*([eE][\-+]?[0-9]+)?/),"number"
if(/[\[\]{}\(\),;\:\.]/.test(c))return r=c,null
if("/"==c){if(e.eat("*"))return t.tokenize=s,s(e,t)
if(e.eat("/"))return e.skipToEnd(),"comment"}if(a.test(c))return e.eatWhile(a),"operator"
e.eatWhile(/[\w\$_\xa1-\uffff]/)
var u=e.current()
return i.propertyIsEnumerable(u)?("case"!=u&&"default"!=u||(r="case"),"keyword"):o.propertyIsEnumerable(u)?"atom":"variable"}function s(e,t){for(var r,n=!1;r=e.next();){if("/"==r&&n){t.tokenize=l
break}n="*"==r}return"comment"}function c(e,t,r,n,i){this.indented=e,this.column=t,this.type=r,this.align=n,this.prev=i}function u(e,t,r){return e.context=new c(e.indented,t,r,null,e.context)}function d(e){if(e.context.prev){var t=e.context.type
return")"!=t&&"]"!=t&&"}"!=t||(e.indented=e.context.indented),e.context=e.context.prev}}return{startState:function(e){return{tokenize:null,context:new c((e||0)-n,0,"top",!1),indented:0,startOfLine:!0}},token:function(e,t){var n=t.context
if(e.sol()&&(null==n.align&&(n.align=!1),t.indented=e.indentation(),t.startOfLine=!0,"case"==n.type&&(n.type="}")),e.eatSpace())return null
r=null
var i=(t.tokenize||l)(e,t)
return"comment"==i||(null==n.align&&(n.align=!0),"{"==r?u(t,e.column(),"}"):"["==r?u(t,e.column(),"]"):"("==r?u(t,e.column(),")"):"case"==r?n.type="case":("}"==r&&"}"==n.type||r==n.type)&&d(t),t.startOfLine=!1),i},indent:function(t,r){if(t.tokenize!=l&&null!=t.tokenize)return e.Pass
var i=t.context,o=r&&r.charAt(0)
if("case"==i.type&&/^(?:case|default)\b/.test(r))return t.context.type="}",i.indented
var a=o==i.type
return i.align?i.column+(a?0:1):i.indented+(a?0:n)},electricChars:"{}):",closeBrackets:"()[]{}''\"\"``",fold:"brace",blockCommentStart:"/*",blockCommentEnd:"*/",lineComment:"//"}})),e.defineMIME("text/x-go","go")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
e.defineMode("haskell",(function(e,t){function r(e,t,r){return t(r),r(e,t)}var n=/[a-z_]/,i=/[A-Z]/,o=/\d/,a=/[0-9A-Fa-f]/,l=/[0-7]/,s=/[a-z_A-Z0-9'\xa1-\uffff]/,c=/[-!#$%&*+.\/<=>?@\\^|~:]/,u=/[(),;[\]`{}]/,d=/[ \t\v\f]/
function f(e,t){if(e.eatWhile(d))return null
var f=e.next()
if(u.test(f)){if("{"==f&&e.eat("-")){var m="comment"
return e.eat("#")&&(m="meta"),r(e,t,p(m,1))}return null}if("'"==f)return e.eat("\\"),e.next(),e.eat("'")?"string":"string error"
if('"'==f)return r(e,t,h)
if(i.test(f))return e.eatWhile(s),e.eat(".")?"qualifier":"variable-2"
if(n.test(f))return e.eatWhile(s),"variable"
if(o.test(f)){if("0"==f){if(e.eat(/[xX]/))return e.eatWhile(a),"integer"
if(e.eat(/[oO]/))return e.eatWhile(l),"number"}e.eatWhile(o)
m="number"
return e.match(/^\.\d+/)&&(m="number"),e.eat(/[eE]/)&&(m="number",e.eat(/[-+]/),e.eatWhile(o)),m}if("."==f&&e.eat("."))return"keyword"
if(c.test(f)){if("-"==f&&e.eat(/-/)&&(e.eatWhile(/-/),!e.eat(c)))return e.skipToEnd(),"comment"
m="variable"
return":"==f&&(m="variable-2"),e.eatWhile(c),m}return"error"}function p(e,t){return 0==t?f:function(r,n){for(var i=t;!r.eol();){var o=r.next()
if("{"==o&&r.eat("-"))++i
else if("-"==o&&r.eat("}")&&0==--i)return n(f),e}return n(p(e,i)),e}}function h(e,t){for(;!e.eol();){var r=e.next()
if('"'==r)return t(f),"string"
if("\\"==r){if(e.eol()||e.eat(d))return t(m),"string"
e.eat("&")||e.next()}}return t(f),"string error"}function m(e,t){return e.eat("\\")?r(e,t,h):(e.next(),t(f),"error")}var g=function(){var e={}
function r(t){return function(){for(var r=0;r<arguments.length;r++)e[arguments[r]]=t}}r("keyword")("case","class","data","default","deriving","do","else","foreign","if","import","in","infix","infixl","infixr","instance","let","module","newtype","of","then","type","where","_"),r("keyword")("..",":","::","=","\\","<-","->","@","~","=>"),r("builtin")("!!","$!","$","&&","+","++","-",".","/","/=","<","<*","<=","<$>","<*>","=<<","==",">",">=",">>",">>=","^","^^","||","*","*>","**"),r("builtin")("Applicative","Bool","Bounded","Char","Double","EQ","Either","Enum","Eq","False","FilePath","Float","Floating","Fractional","Functor","GT","IO","IOError","Int","Integer","Integral","Just","LT","Left","Maybe","Monad","Nothing","Num","Ord","Ordering","Rational","Read","ReadS","Real","RealFloat","RealFrac","Right","Show","ShowS","String","True"),r("builtin")("abs","acos","acosh","all","and","any","appendFile","asTypeOf","asin","asinh","atan","atan2","atanh","break","catch","ceiling","compare","concat","concatMap","const","cos","cosh","curry","cycle","decodeFloat","div","divMod","drop","dropWhile","either","elem","encodeFloat","enumFrom","enumFromThen","enumFromThenTo","enumFromTo","error","even","exp","exponent","fail","filter","flip","floatDigits","floatRadix","floatRange","floor","fmap","foldl","foldl1","foldr","foldr1","fromEnum","fromInteger","fromIntegral","fromRational","fst","gcd","getChar","getContents","getLine","head","id","init","interact","ioError","isDenormalized","isIEEE","isInfinite","isNaN","isNegativeZero","iterate","last","lcm","length","lex","lines","log","logBase","lookup","map","mapM","mapM_","max","maxBound","maximum","maybe","min","minBound","minimum","mod","negate","not","notElem","null","odd","or","otherwise","pi","pred","print","product","properFraction","pure","putChar","putStr","putStrLn","quot","quotRem","read","readFile","readIO","readList","readLn","readParen","reads","readsPrec","realToFrac","recip","rem","repeat","replicate","return","reverse","round","scaleFloat","scanl","scanl1","scanr","scanr1","seq","sequence","sequence_","show","showChar","showList","showParen","showString","shows","showsPrec","significand","signum","sin","sinh","snd","span","splitAt","sqrt","subtract","succ","sum","tail","take","takeWhile","tan","tanh","toEnum","toInteger","toRational","truncate","uncurry","undefined","unlines","until","unwords","unzip","unzip3","userError","words","writeFile","zip","zip3","zipWith","zipWith3")
var n=t.overrideKeywords
if(n)for(var i in n)n.hasOwnProperty(i)&&(e[i]=n[i])
return e}()
return{startState:function(){return{f:f}},copyState:function(e){return{f:e.f}},token:function(e,t){var r=t.f(e,(function(e){t.f=e})),n=e.current()
return g.hasOwnProperty(n)?g[n]:r},blockCommentStart:"{-",blockCommentEnd:"-}",lineComment:"--"}})),e.defineMIME("text/x-haskell","haskell")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror"),require("../xml/xml"),require("../javascript/javascript"),require("../css/css")):"function"==typeof define&&define.amd?define(["../../lib/codemirror","../xml/xml","../javascript/javascript","../css/css"],e):e(CodeMirror)}((function(e){"use strict"
var t={script:[["lang",/(javascript|babel)/i,"javascript"],["type",/^(?:text|application)\/(?:x-)?(?:java|ecma)script$|^module$|^$/i,"javascript"],["type",/./,"text/plain"],[null,null,"javascript"]],style:[["lang",/^css$/i,"css"],["type",/^(text\/)?(x-)?(stylesheet|css)$/i,"css"],["type",/./,"text/plain"],[null,null,"css"]]}
var r={}
function n(e,t){var n=e.match(function(e){return r[e]||(r[e]=new RegExp("\\s+"+e+"\\s*=\\s*('|\")?([^'\"]+)('|\")?\\s*"))}(t))
return n?/^\s*(.*?)\s*$/.exec(n[2])[1]:""}function i(e,t){return new RegExp((t?"^":"")+"</s*"+e+"s*>","i")}function o(e,t){for(var r in e)for(var n=t[r]||(t[r]=[]),i=e[r],o=i.length-1;o>=0;o--)n.unshift(i[o])}e.defineMode("htmlmixed",(function(r,a){var l=e.getMode(r,{name:"xml",htmlMode:!0,multilineTagIndentFactor:a.multilineTagIndentFactor,multilineTagIndentPastTag:a.multilineTagIndentPastTag}),s={},c=a&&a.tags,u=a&&a.scriptTypes
if(o(t,s),c&&o(c,s),u)for(var d=u.length-1;d>=0;d--)s.script.unshift(["type",u[d].matches,u[d].mode])
function f(t,o){var a,c=l.token(t,o.htmlState),u=/\btag\b/.test(c)
if(u&&!/[<>\s\/]/.test(t.current())&&(a=o.htmlState.tagName&&o.htmlState.tagName.toLowerCase())&&s.hasOwnProperty(a))o.inTag=a+" "
else if(o.inTag&&u&&/>$/.test(t.current())){var d=/^([\S]+) (.*)/.exec(o.inTag)
o.inTag=null
var p=">"==t.current()&&function(e,t){for(var r=0;r<e.length;r++){var i=e[r]
if(!i[0]||i[1].test(n(t,i[0])))return i[2]}}(s[d[1]],d[2]),h=e.getMode(r,p),m=i(d[1],!0),g=i(d[1],!1)
o.token=function(e,t){return e.match(m,!1)?(t.token=f,t.localState=t.localMode=null,null):function(e,t,r){var n=e.current(),i=n.search(t)
return i>-1?e.backUp(n.length-i):n.match(/<\/?$/)&&(e.backUp(n.length),e.match(t,!1)||e.match(n)),r}(e,g,t.localMode.token(e,t.localState))},o.localMode=h,o.localState=e.startState(h,l.indent(o.htmlState,"",""))}else o.inTag&&(o.inTag+=t.current(),t.eol()&&(o.inTag+=" "))
return c}return{startState:function(){return{token:f,inTag:null,localMode:null,localState:null,htmlState:e.startState(l)}},copyState:function(t){var r
return t.localState&&(r=e.copyState(t.localMode,t.localState)),{token:t.token,inTag:t.inTag,localMode:t.localMode,localState:r,htmlState:e.copyState(l,t.htmlState)}},token:function(e,t){return t.token(e,t)},indent:function(t,r,n){return!t.localMode||/^\s*<\//.test(r)?l.indent(t.htmlState,r,n):t.localMode.indent?t.localMode.indent(t.localState,r,n):e.Pass},innerMode:function(e){return{state:e.localState||e.htmlState,mode:e.localMode||l}}}}),"xml","javascript","css"),e.defineMIME("text/html","htmlmixed")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
e.defineMode("javascript",(function(t,r){var n,i,o=t.indentUnit,a=r.statementIndent,l=r.jsonld,s=r.json||l,c=r.typescript,u=r.wordCharacters||/[\w$\xa1-\uffff]/,d=function(){function e(e){return{type:e,style:"keyword"}}var t=e("keyword a"),r=e("keyword b"),n=e("keyword c"),i=e("keyword d"),o=e("operator"),a={type:"atom",style:"atom"}
return{if:e("if"),while:t,with:t,else:r,do:r,try:r,finally:r,return:i,break:i,continue:i,new:e("new"),delete:n,void:n,throw:n,debugger:e("debugger"),var:e("var"),const:e("var"),let:e("var"),function:e("function"),catch:e("catch"),for:e("for"),switch:e("switch"),case:e("case"),default:e("default"),in:o,typeof:o,instanceof:o,true:a,false:a,null:a,undefined:a,NaN:a,Infinity:a,this:e("this"),class:e("class"),super:e("atom"),yield:n,export:e("export"),import:e("import"),extends:n,await:n}}(),f=/[+\-*&%=<>!?|~^@]/,p=/^@(context|id|value|language|type|container|list|set|reverse|index|base|vocab|graph)"/
function h(e,t,r){return n=e,i=r,t}function m(e,t){var r,n=e.next()
if('"'==n||"'"==n)return t.tokenize=(r=n,function(e,t){var n,i=!1
if(l&&"@"==e.peek()&&e.match(p))return t.tokenize=m,h("jsonld-keyword","meta")
for(;null!=(n=e.next())&&(n!=r||i);)i=!i&&"\\"==n
return i||(t.tokenize=m),h("string","string")}),t.tokenize(e,t)
if("."==n&&e.match(/^\d[\d_]*(?:[eE][+\-]?[\d_]+)?/))return h("number","number")
if("."==n&&e.match(".."))return h("spread","meta")
if(/[\[\]{}\(\),;\:\.]/.test(n))return h(n)
if("="==n&&e.eat(">"))return h("=>","operator")
if("0"==n&&e.match(/^(?:x[\dA-Fa-f_]+|o[0-7_]+|b[01_]+)n?/))return h("number","number")
if(/\d/.test(n))return e.match(/^[\d_]*(?:n|(?:\.[\d_]*)?(?:[eE][+\-]?[\d_]+)?)?/),h("number","number")
if("/"==n)return e.eat("*")?(t.tokenize=g,g(e,t)):e.eat("/")?(e.skipToEnd(),h("comment","comment")):Ke(e,t,1)?(function(e){for(var t,r=!1,n=!1;null!=(t=e.next());){if(!r){if("/"==t&&!n)return
"["==t?n=!0:n&&"]"==t&&(n=!1)}r=!r&&"\\"==t}}(e),e.match(/^\b(([gimyus])(?![gimyus]*\2))+\b/),h("regexp","string-2")):(e.eat("="),h("operator","operator",e.current()))
if("`"==n)return t.tokenize=v,v(e,t)
if("#"==n)return e.skipToEnd(),h("error","error")
if("<"==n&&e.match("!--")||"-"==n&&e.match("->"))return e.skipToEnd(),h("comment","comment")
if(f.test(n))return">"==n&&t.lexical&&">"==t.lexical.type||(e.eat("=")?"!"!=n&&"="!=n||e.eat("="):/[<>*+\-]/.test(n)&&(e.eat(n),">"==n&&e.eat(n))),h("operator","operator",e.current())
if(u.test(n)){e.eatWhile(u)
var i=e.current()
if("."!=t.lastType){if(d.propertyIsEnumerable(i)){var o=d[i]
return h(o.type,o.style,i)}if("async"==i&&e.match(/^(\s|\/\*.*?\*\/)*[\[\(\w]/,!1))return h("async","keyword",i)}return h("variable","variable",i)}}function g(e,t){for(var r,n=!1;r=e.next();){if("/"==r&&n){t.tokenize=m
break}n="*"==r}return h("comment","comment")}function v(e,t){for(var r,n=!1;null!=(r=e.next());){if(!n&&("`"==r||"$"==r&&e.eat("{"))){t.tokenize=m
break}n=!n&&"\\"==r}return h("quasi","string-2",e.current())}function y(e,t){t.fatArrowAt&&(t.fatArrowAt=null)
var r=e.string.indexOf("=>",e.start)
if(!(r<0)){if(c){var n=/:\s*(?:\w+(?:<[^>]*>|\[\])?|\{[^}]*\})\s*$/.exec(e.string.slice(e.start,r))
n&&(r=n.index)}for(var i=0,o=!1,a=r-1;a>=0;--a){var l=e.string.charAt(a),s="([{}])".indexOf(l)
if(s>=0&&s<3){if(!i){++a
break}if(0==--i){"("==l&&(o=!0)
break}}else if(s>=3&&s<6)++i
else if(u.test(l))o=!0
else if(/["'\/`]/.test(l))for(;;--a){if(0==a)return
if(e.string.charAt(a-1)==l&&"\\"!=e.string.charAt(a-2)){a--
break}}else if(o&&!i){++a
break}}o&&!i&&(t.fatArrowAt=a)}}var b={atom:!0,number:!0,variable:!0,string:!0,regexp:!0,this:!0,"jsonld-keyword":!0}
function x(e,t,r,n,i,o){this.indented=e,this.column=t,this.type=r,this.prev=i,this.info=o,null!=n&&(this.align=n)}function w(e,t){for(var r=e.localVars;r;r=r.next)if(r.name==t)return!0
for(var n=e.context;n;n=n.prev)for(r=n.vars;r;r=r.next)if(r.name==t)return!0}var k={state:null,column:null,marked:null,cc:null}
function _(){for(var e=arguments.length-1;e>=0;e--)k.cc.push(arguments[e])}function C(){return _.apply(null,arguments),!0}function S(e,t){for(var r=t;r;r=r.next)if(r.name==e)return!0
return!1}function T(e){var t=k.state
if(k.marked="def",t.context)if("var"==t.lexical.info&&t.context&&t.context.block){var n=M(e,t.context)
if(null!=n)return void(t.context=n)}else if(!S(e,t.localVars))return void(t.localVars=new A(e,t.localVars))
r.globalVars&&!S(e,t.globalVars)&&(t.globalVars=new A(e,t.globalVars))}function M(e,t){if(t){if(t.block){var r=M(e,t.prev)
return r?r==t.prev?t:new z(r,t.vars,!0):null}return S(e,t.vars)?t:new z(t.prev,new A(e,t.vars),!1)}return null}function L(e){return"public"==e||"private"==e||"protected"==e||"abstract"==e||"readonly"==e}function z(e,t,r){this.prev=e,this.vars=t,this.block=r}function A(e,t){this.name=e,this.next=t}var E=new A("this",new A("arguments",null))
function N(){k.state.context=new z(k.state.context,k.state.localVars,!1),k.state.localVars=E}function q(){k.state.context=new z(k.state.context,k.state.localVars,!0),k.state.localVars=null}function O(){k.state.localVars=k.state.context.vars,k.state.context=k.state.context.prev}function I(e,t){var r=function(){var r=k.state,n=r.indented
if("stat"==r.lexical.type)n=r.lexical.indented
else for(var i=r.lexical;i&&")"==i.type&&i.align;i=i.prev)n=i.indented
r.lexical=new x(n,k.stream.column(),e,null,r.lexical,t)}
return r.lex=!0,r}function D(){var e=k.state
e.lexical.prev&&(")"==e.lexical.type&&(e.indented=e.lexical.indented),e.lexical=e.lexical.prev)}function F(e){return function t(r){return r==e?C():";"==e||"}"==r||")"==r||"]"==r?_():C(t)}}function P(e,t){return"var"==e?C(I("vardef",t),be,F(";"),D):"keyword a"==e?C(I("form"),j,P,D):"keyword b"==e?C(I("form"),P,D):"keyword d"==e?k.stream.match(/^\s*$/,!1)?C():C(I("stat"),B,F(";"),D):"debugger"==e?C(F(";")):"{"==e?C(I("}"),q,ae,D,O):";"==e?C():"if"==e?("else"==k.state.lexical.info&&k.state.cc[k.state.cc.length-1]==D&&k.state.cc.pop()(),C(I("form"),j,P,D,Se)):"function"==e?C(ze):"for"==e?C(I("form"),Te,P,D):"class"==e||c&&"interface"==t?(k.marked="keyword",C(I("form","class"==e?e:t),Oe,D)):"variable"==e?c&&"declare"==t?(k.marked="keyword",C(P)):c&&("module"==t||"enum"==t||"type"==t)&&k.stream.match(/^\s*\w/,!1)?(k.marked="keyword","enum"==t?C(Ge):"type"==t?C(Ee,F("operator"),de,F(";")):C(I("form"),xe,F("{"),I("}"),ae,D,D)):c&&"namespace"==t?(k.marked="keyword",C(I("form"),R,P,D)):c&&"abstract"==t?(k.marked="keyword",C(P)):C(I("stat"),J):"switch"==e?C(I("form"),j,F("{"),I("}","switch"),q,ae,D,D,O):"case"==e?C(R,F(":")):"default"==e?C(F(":")):"catch"==e?C(I("form"),N,W,P,D,O):"export"==e?C(I("stat"),Pe,D):"import"==e?C(I("stat"),Re,D):"async"==e?C(P):"@"==t?C(R,P):_(I("stat"),R,F(";"),D)}function W(e){if("("==e)return C(Ne,F(")"))}function R(e,t){return H(e,t,!1)}function $(e,t){return H(e,t,!0)}function j(e){return"("!=e?_():C(I(")"),R,F(")"),D)}function H(e,t,r){if(k.state.fatArrowAt==k.stream.start){var n=r?X:Z
if("("==e)return C(N,I(")"),ie(Ne,")"),D,F("=>"),n,O)
if("variable"==e)return _(N,xe,F("=>"),n,O)}var i=r?G:U
return b.hasOwnProperty(e)?C(i):"function"==e?C(ze,i):"class"==e||c&&"interface"==t?(k.marked="keyword",C(I("form"),qe,D)):"keyword c"==e||"async"==e?C(r?$:R):"("==e?C(I(")"),B,F(")"),D,i):"operator"==e||"spread"==e?C(r?$:R):"["==e?C(I("]"),Ue,D,i):"{"==e?oe(te,"}",null,i):"quasi"==e?_(V,i):"new"==e?C(function(e){return function(t){return"."==t?C(e?Q:Y):"variable"==t&&c?C(ge,e?G:U):_(e?$:R)}}(r)):"import"==e?C(R):C()}function B(e){return e.match(/[;\}\)\],]/)?_():_(R)}function U(e,t){return","==e?C(B):G(e,t,!1)}function G(e,t,r){var n=0==r?U:G,i=0==r?R:$
return"=>"==e?C(N,r?X:Z,O):"operator"==e?/\+\+|--/.test(t)||c&&"!"==t?C(n):c&&"<"==t&&k.stream.match(/^([^>]|<.*?>)*>\s*\(/,!1)?C(I(">"),ie(de,">"),D,n):"?"==t?C(R,F(":"),i):C(i):"quasi"==e?_(V,n):";"!=e?"("==e?oe($,")","call",n):"."==e?C(ee,n):"["==e?C(I("]"),B,F("]"),D,n):c&&"as"==t?(k.marked="keyword",C(de,n)):"regexp"==e?(k.state.lastType=k.marked="operator",k.stream.backUp(k.stream.pos-k.stream.start-1),C(i)):void 0:void 0}function V(e,t){return"quasi"!=e?_():"${"!=t.slice(t.length-2)?C(V):C(R,K)}function K(e){if("}"==e)return k.marked="string-2",k.state.tokenize=v,C(V)}function Z(e){return y(k.stream,k.state),_("{"==e?P:R)}function X(e){return y(k.stream,k.state),_("{"==e?P:$)}function Y(e,t){if("target"==t)return k.marked="keyword",C(U)}function Q(e,t){if("target"==t)return k.marked="keyword",C(G)}function J(e){return":"==e?C(D,P):_(U,F(";"),D)}function ee(e){if("variable"==e)return k.marked="property",C()}function te(e,t){return"async"==e?(k.marked="property",C(te)):"variable"==e||"keyword"==k.style?(k.marked="property","get"==t||"set"==t?C(re):(c&&k.state.fatArrowAt==k.stream.start&&(r=k.stream.match(/^\s*:\s*/,!1))&&(k.state.fatArrowAt=k.stream.pos+r[0].length),C(ne))):"number"==e||"string"==e?(k.marked=l?"property":k.style+" property",C(ne)):"jsonld-keyword"==e?C(ne):c&&L(t)?(k.marked="keyword",C(te)):"["==e?C(R,le,F("]"),ne):"spread"==e?C($,ne):"*"==t?(k.marked="keyword",C(te)):":"==e?_(ne):void 0
var r}function re(e){return"variable"!=e?_(ne):(k.marked="property",C(ze))}function ne(e){return":"==e?C($):"("==e?_(ze):void 0}function ie(e,t,r){function n(i,o){if(r?r.indexOf(i)>-1:","==i){var a=k.state.lexical
return"call"==a.info&&(a.pos=(a.pos||0)+1),C((function(r,n){return r==t||n==t?_():_(e)}),n)}return i==t||o==t?C():r&&r.indexOf(";")>-1?_(e):C(F(t))}return function(r,i){return r==t||i==t?C():_(e,n)}}function oe(e,t,r){for(var n=3;n<arguments.length;n++)k.cc.push(arguments[n])
return C(I(t,r),ie(e,t),D)}function ae(e){return"}"==e?C():_(P,ae)}function le(e,t){if(c){if(":"==e)return C(de)
if("?"==t)return C(le)}}function se(e,t){if(c&&(":"==e||"in"==t))return C(de)}function ce(e){if(c&&":"==e)return k.stream.match(/^\s*\w+\s+is\b/,!1)?C(R,ue,de):C(de)}function ue(e,t){if("is"==t)return k.marked="keyword",C()}function de(e,t){return"keyof"==t||"typeof"==t||"infer"==t?(k.marked="keyword",C("typeof"==t?$:de)):"variable"==e||"void"==t?(k.marked="type",C(me)):"|"==t||"&"==t?C(de):"string"==e||"number"==e||"atom"==e?C(me):"["==e?C(I("]"),ie(de,"]",","),D,me):"{"==e?C(I("}"),ie(pe,"}",",;"),D,me):"("==e?C(ie(he,")"),fe,me):"<"==e?C(ie(de,">"),de):void 0}function fe(e){if("=>"==e)return C(de)}function pe(e,t){return"variable"==e||"keyword"==k.style?(k.marked="property",C(pe)):"?"==t||"number"==e||"string"==e?C(pe):":"==e?C(de):"["==e?C(F("variable"),se,F("]"),pe):"("==e?_(Ae,pe):void 0}function he(e,t){return"variable"==e&&k.stream.match(/^\s*[?:]/,!1)||"?"==t?C(he):":"==e?C(de):"spread"==e?C(he):_(de)}function me(e,t){return"<"==t?C(I(">"),ie(de,">"),D,me):"|"==t||"."==e||"&"==t?C(de):"["==e?C(de,F("]"),me):"extends"==t||"implements"==t?(k.marked="keyword",C(de)):"?"==t?C(de,F(":"),de):void 0}function ge(e,t){if("<"==t)return C(I(">"),ie(de,">"),D,me)}function ve(){return _(de,ye)}function ye(e,t){if("="==t)return C(de)}function be(e,t){return"enum"==t?(k.marked="keyword",C(Ge)):_(xe,le,_e,Ce)}function xe(e,t){return c&&L(t)?(k.marked="keyword",C(xe)):"variable"==e?(T(t),C()):"spread"==e?C(xe):"["==e?oe(ke,"]"):"{"==e?oe(we,"}"):void 0}function we(e,t){return"variable"!=e||k.stream.match(/^\s*:/,!1)?("variable"==e&&(k.marked="property"),"spread"==e?C(xe):"}"==e?_():"["==e?C(R,F("]"),F(":"),we):C(F(":"),xe,_e)):(T(t),C(_e))}function ke(){return _(xe,_e)}function _e(e,t){if("="==t)return C($)}function Ce(e){if(","==e)return C(be)}function Se(e,t){if("keyword b"==e&&"else"==t)return C(I("form","else"),P,D)}function Te(e,t){return"await"==t?C(Te):"("==e?C(I(")"),Me,D):void 0}function Me(e){return"var"==e?C(be,Le):"variable"==e?C(Le):_(Le)}function Le(e,t){return")"==e?C():";"==e?C(Le):"in"==t||"of"==t?(k.marked="keyword",C(R,Le)):_(R,Le)}function ze(e,t){return"*"==t?(k.marked="keyword",C(ze)):"variable"==e?(T(t),C(ze)):"("==e?C(N,I(")"),ie(Ne,")"),D,ce,P,O):c&&"<"==t?C(I(">"),ie(ve,">"),D,ze):void 0}function Ae(e,t){return"*"==t?(k.marked="keyword",C(Ae)):"variable"==e?(T(t),C(Ae)):"("==e?C(N,I(")"),ie(Ne,")"),D,ce,O):c&&"<"==t?C(I(">"),ie(ve,">"),D,Ae):void 0}function Ee(e,t){return"keyword"==e||"variable"==e?(k.marked="type",C(Ee)):"<"==t?C(I(">"),ie(ve,">"),D):void 0}function Ne(e,t){return"@"==t&&C(R,Ne),"spread"==e?C(Ne):c&&L(t)?(k.marked="keyword",C(Ne)):c&&"this"==e?C(le,_e):_(xe,le,_e)}function qe(e,t){return"variable"==e?Oe(e,t):Ie(e,t)}function Oe(e,t){if("variable"==e)return T(t),C(Ie)}function Ie(e,t){return"<"==t?C(I(">"),ie(ve,">"),D,Ie):"extends"==t||"implements"==t||c&&","==e?("implements"==t&&(k.marked="keyword"),C(c?de:R,Ie)):"{"==e?C(I("}"),De,D):void 0}function De(e,t){return"async"==e||"variable"==e&&("static"==t||"get"==t||"set"==t||c&&L(t))&&k.stream.match(/^\s+[\w$\xa1-\uffff]/,!1)?(k.marked="keyword",C(De)):"variable"==e||"keyword"==k.style?(k.marked="property",C(c?Fe:ze,De)):"number"==e||"string"==e?C(c?Fe:ze,De):"["==e?C(R,le,F("]"),c?Fe:ze,De):"*"==t?(k.marked="keyword",C(De)):c&&"("==e?_(Ae,De):";"==e||","==e?C(De):"}"==e?C():"@"==t?C(R,De):void 0}function Fe(e,t){if("?"==t)return C(Fe)
if(":"==e)return C(de,_e)
if("="==t)return C($)
var r=k.state.lexical.prev
return _(r&&"interface"==r.info?Ae:ze)}function Pe(e,t){return"*"==t?(k.marked="keyword",C(Be,F(";"))):"default"==t?(k.marked="keyword",C(R,F(";"))):"{"==e?C(ie(We,"}"),Be,F(";")):_(P)}function We(e,t){return"as"==t?(k.marked="keyword",C(F("variable"))):"variable"==e?_($,We):void 0}function Re(e){return"string"==e?C():"("==e?_(R):_($e,je,Be)}function $e(e,t){return"{"==e?oe($e,"}"):("variable"==e&&T(t),"*"==t&&(k.marked="keyword"),C(He))}function je(e){if(","==e)return C($e,je)}function He(e,t){if("as"==t)return k.marked="keyword",C($e)}function Be(e,t){if("from"==t)return k.marked="keyword",C(R)}function Ue(e){return"]"==e?C():_(ie($,"]"))}function Ge(){return _(I("form"),xe,F("{"),I("}"),ie(Ve,"}"),D,D)}function Ve(){return _(xe,_e)}function Ke(e,t,r){return t.tokenize==m&&/^(?:operator|sof|keyword [bcd]|case|new|export|default|spread|[\[{}\(,;:]|=>)$/.test(t.lastType)||"quasi"==t.lastType&&/\{\s*$/.test(e.string.slice(0,e.pos-(r||0)))}return O.lex=!0,D.lex=!0,{startState:function(e){var t={tokenize:m,lastType:"sof",cc:[],lexical:new x((e||0)-o,0,"block",!1),localVars:r.localVars,context:r.localVars&&new z(null,null,!1),indented:e||0}
return r.globalVars&&"object"==typeof r.globalVars&&(t.globalVars=r.globalVars),t},token:function(e,t){if(e.sol()&&(t.lexical.hasOwnProperty("align")||(t.lexical.align=!1),t.indented=e.indentation(),y(e,t)),t.tokenize!=g&&e.eatSpace())return null
var r=t.tokenize(e,t)
return"comment"==n?r:(t.lastType="operator"!=n||"++"!=i&&"--"!=i?n:"incdec",function(e,t,r,n,i){var o=e.cc
for(k.state=e,k.stream=i,k.marked=null,k.cc=o,k.style=t,e.lexical.hasOwnProperty("align")||(e.lexical.align=!0);;)if((o.length?o.pop():s?R:P)(r,n)){for(;o.length&&o[o.length-1].lex;)o.pop()()
return k.marked?k.marked:"variable"==r&&w(e,n)?"variable-2":t}}(t,r,n,i,e))},indent:function(t,n){if(t.tokenize==g)return e.Pass
if(t.tokenize!=m)return 0
var i,l=n&&n.charAt(0),s=t.lexical
if(!/^\s*else\b/.test(n))for(var c=t.cc.length-1;c>=0;--c){var u=t.cc[c]
if(u==D)s=s.prev
else if(u!=Se)break}for(;("stat"==s.type||"form"==s.type)&&("}"==l||(i=t.cc[t.cc.length-1])&&(i==U||i==G)&&!/^[,\.=+\-*:?[\(]/.test(n));)s=s.prev
a&&")"==s.type&&"stat"==s.prev.type&&(s=s.prev)
var d=s.type,p=l==d
return"vardef"==d?s.indented+("operator"==t.lastType||","==t.lastType?s.info.length+1:0):"form"==d&&"{"==l?s.indented:"form"==d?s.indented+o:"stat"==d?s.indented+(function(e,t){return"operator"==e.lastType||","==e.lastType||f.test(t.charAt(0))||/[,.]/.test(t.charAt(0))}(t,n)?a||o:0):"switch"!=s.info||p||0==r.doubleIndentSwitch?s.align?s.column+(p?0:1):s.indented+(p?0:o):s.indented+(/^(?:case|default)\b/.test(n)?o:2*o)},electricInput:/^\s*(?:case .*?:|default:|\{|\})$/,blockCommentStart:s?null:"/*",blockCommentEnd:s?null:"*/",blockCommentContinue:s?null:" * ",lineComment:s?null:"//",fold:"brace",closeBrackets:"()[]{}''\"\"``",helperType:s?"json":"javascript",jsonldMode:l,jsonMode:s,expressionAllowed:Ke,skipExpression:function(e){var t=e.cc[e.cc.length-1]
t!=R&&t!=$||e.cc.pop()}}})),e.registerHelper("wordChars","javascript",/[\w$]/),e.defineMIME("text/javascript","javascript"),e.defineMIME("text/ecmascript","javascript"),e.defineMIME("application/javascript","javascript"),e.defineMIME("application/x-javascript","javascript"),e.defineMIME("application/ecmascript","javascript"),e.defineMIME("application/json",{name:"javascript",json:!0}),e.defineMIME("application/x-json",{name:"javascript",json:!0}),e.defineMIME("application/ld+json",{name:"javascript",jsonld:!0}),e.defineMIME("text/typescript",{name:"javascript",typescript:!0}),e.defineMIME("application/typescript",{name:"javascript",typescript:!0})})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
e.defineMode("julia",(function(t,r){function n(e,t){return void 0===t&&(t="\\b"),new RegExp("^(("+e.join(")|(")+"))"+t)}var i=r.operators||n(["[<>]:","[<>=]=","<<=?",">>>?=?","=>","->","\\/\\/","[\\\\%*+\\-<>!=\\/^|&\\u00F7\\u22BB]=?","\\?","\\$","~",":","\\u00D7","\\u2208","\\u2209","\\u220B","\\u220C","\\u2218","\\u221A","\\u221B","\\u2229","\\u222A","\\u2260","\\u2264","\\u2265","\\u2286","\\u2288","\\u228A","\\u22C5","\\b(in|isa)\\b(?!.?\\()"],""),o=r.delimiters||/^[;,()[\]{}]/,a=r.identifiers||/^[_A-Za-z\u00A1-\u2217\u2219-\uFFFF][\w\u00A1-\u2217\u2219-\uFFFF]*!*/,l=n(["\\\\[0-7]{1,3}","\\\\x[A-Fa-f0-9]{1,2}","\\\\[abefnrtv0%?'\"\\\\]","([^\\u0027\\u005C\\uD800-\\uDFFF]|[\\uD800-\\uDFFF][\\uDC00-\\uDFFF])"],"'"),s=["if","else","elseif","while","for","begin","let","end","do","try","catch","finally","return","break","continue","global","local","const","export","import","importall","using","function","where","macro","module","baremodule","struct","type","mutable","immutable","quote","typealias","abstract","primitive","bitstype"],c=["true","false","nothing","NaN","Inf"]
e.registerHelper("hintWords","julia",s.concat(c))
var u=n(["begin","function","type","struct","immutable","let","macro","for","while","quote","if","else","elseif","try","finally","catch","do"]),d=n(["end","else","elseif","catch","finally"]),f=n(s),p=n(c),h=/^@[_A-Za-z][\w]*/,m=/^:[_A-Za-z\u00A1-\uFFFF][\w\u00A1-\uFFFF]*!*/,g=/^(`|([_A-Za-z\u00A1-\uFFFF]*"("")?))/
function v(e){return e.nestedArrays>0}function y(e,t){return void 0===t&&(t=0),e.scopes.length<=t?null:e.scopes[e.scopes.length-(t+1)]}function b(e,t){if(e.match(/^#=/,!1))return t.tokenize=k,t.tokenize(e,t)
var r=t.leavingExpr
if(e.sol()&&(r=!1),t.leavingExpr=!1,r&&e.match(/^'+/))return"operator"
if(e.match(/\.{4,}/))return"error"
if(e.match(/\.{1,3}/))return"operator"
if(e.eatSpace())return null
var n,l=e.peek()
if("#"===l)return e.skipToEnd(),"comment"
if("["===l&&(t.scopes.push("["),t.nestedArrays++),"("===l&&(t.scopes.push("("),t.nestedGenerators++),v(t)&&"]"===l){for(;"["!==y(t);)t.scopes.pop()
t.scopes.pop(),t.nestedArrays--,t.leavingExpr=!0}if(function(e){return e.nestedGenerators>0}(t)&&")"===l){for(;"("!==y(t);)t.scopes.pop()
t.scopes.pop(),t.nestedGenerators--,t.leavingExpr=!0}if(v(t)){if("end"==t.lastToken&&e.match(/^:/))return"operator"
if(e.match(/^end/))return"number"}if((n=e.match(u,!1))&&t.scopes.push(n[0]),e.match(d,!1)&&t.scopes.pop(),e.match(/^::(?![:\$])/))return t.tokenize=w,t.tokenize(e,t)
if(!r&&e.match(m)||e.match(/:([<>]:|<<=?|>>>?=?|->|\/\/|\.{2,3}|[\.\\%*+\-<>!\/^|&]=?|[~\?\$])/))return"builtin"
if(e.match(i))return"operator"
if(e.match(/^\.?\d/,!1)){var s=RegExp(/^im\b/),c=!1
if(e.match(/^0x\.[0-9a-f_]+p[\+\-]?[_\d]+/i)&&(c=!0),e.match(/^0x[0-9a-f_]+/i)&&(c=!0),e.match(/^0b[01_]+/i)&&(c=!0),e.match(/^0o[0-7_]+/i)&&(c=!0),e.match(/^(?:(?:\d[_\d]*)?\.(?!\.)(?:\d[_\d]*)?|\d[_\d]*\.(?!\.)(?:\d[_\d]*))?([Eef][\+\-]?[_\d]+)?/i)&&(c=!0),e.match(/^\d[_\d]*(e[\+\-]?\d+)?/i)&&(c=!0),c)return e.match(s),t.leavingExpr=!0,"number"}if(e.match(/^'/))return t.tokenize=_,t.tokenize(e,t)
if(e.match(g))return t.tokenize=function(e){'"""'===e.substr(-3)?e='"""':'"'===e.substr(-1)&&(e='"')
function t(t,r){if(t.eat("\\"))t.next()
else{if(t.match(e))return r.tokenize=b,r.leavingExpr=!0,"string"
t.eat(/[`"]/)}return t.eatWhile(/[^\\`"]/),"string"}return t}(e.current()),t.tokenize(e,t)
if(e.match(h))return"meta"
if(e.match(o))return null
if(e.match(f))return"keyword"
if(e.match(p))return"builtin"
var C=t.isDefinition||"function"==t.lastToken||"macro"==t.lastToken||"type"==t.lastToken||"struct"==t.lastToken||"immutable"==t.lastToken
return e.match(a)?C?"."===e.peek()?(t.isDefinition=!0,"variable"):(t.isDefinition=!1,"def"):e.match(/^({[^}]*})*\(/,!1)?(t.tokenize=x,t.tokenize(e,t)):(t.leavingExpr=!0,"variable"):(e.next(),"error")}function x(e,t){var r=e.match(/^(\(\s*)/)
if(r&&(t.firstParenPos<0&&(t.firstParenPos=t.scopes.length),t.scopes.push("("),t.charsAdvanced+=r[1].length),"("==y(t)&&e.match(/^\)/)&&(t.scopes.pop(),t.charsAdvanced+=1,t.scopes.length<=t.firstParenPos)){var n=e.match(/^(\s*where\s+[^\s=]+)*\s*?=(?!=)/,!1)
return e.backUp(t.charsAdvanced),t.firstParenPos=-1,t.charsAdvanced=0,t.tokenize=b,n?"def":"builtin"}if(e.match(/^$/g,!1)){for(e.backUp(t.charsAdvanced);t.scopes.length>t.firstParenPos;)t.scopes.pop()
return t.firstParenPos=-1,t.charsAdvanced=0,t.tokenize=b,"builtin"}return t.charsAdvanced+=e.match(/^([^()]*)/)[1].length,t.tokenize(e,t)}function w(e,t){return e.match(/.*?(?=,|;|{|}|\(|\)|=|$|\s)/),e.match(/^{/)?t.nestedParameters++:e.match(/^}/)&&t.nestedParameters>0&&t.nestedParameters--,t.nestedParameters>0?e.match(/.*?(?={|})/)||e.next():0==t.nestedParameters&&(t.tokenize=b),"builtin"}function k(e,t){return e.match(/^#=/)&&t.nestedComments++,e.match(/.*?(?=(#=|=#))/)||e.skipToEnd(),e.match(/^=#/)&&(t.nestedComments--,0==t.nestedComments&&(t.tokenize=b)),"comment"}function _(e,t){var r,n=!1
if(e.match(l))n=!0
else if(r=e.match(/\\u([a-f0-9]{1,4})(?=')/i)){((i=parseInt(r[1],16))<=55295||i>=57344)&&(n=!0,e.next())}else if(r=e.match(/\\U([A-Fa-f0-9]{5,8})(?=')/)){var i;(i=parseInt(r[1],16))<=1114111&&(n=!0,e.next())}return n?(t.leavingExpr=!0,t.tokenize=b,"string"):(e.match(/^[^']+(?=')/)||e.skipToEnd(),e.match(/^'/)&&(t.tokenize=b),"error")}return{startState:function(){return{tokenize:b,scopes:[],lastToken:null,leavingExpr:!1,isDefinition:!1,nestedArrays:0,nestedComments:0,nestedGenerators:0,nestedParameters:0,charsAdvanced:0,firstParenPos:-1}},token:function(e,t){var r=t.tokenize(e,t),n=e.current()
return n&&r&&(t.lastToken=n),r},indent:function(e,r){var n=0
return"]"!==r&&")"!==r&&"end"!==r&&"else"!==r&&"catch"!==r&&"elseif"!==r&&"finally"!==r||(n=-1),(e.scopes.length+n)*t.indentUnit},electricInput:/\b(end|else|catch|finally)\b/,blockCommentStart:"#=",blockCommentEnd:"=#",lineComment:"#",closeBrackets:'()[]{}""',fold:"indent"}})),e.defineMIME("text/x-julia","julia")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
e.defineMode("octave",(function(){function e(e){return new RegExp("^(("+e.join(")|(")+"))\\b")}var t=new RegExp("^[\\+\\-\\*/&|\\^~<>!@'\\\\]"),r=new RegExp("^[\\(\\[\\{\\},:=;\\.]"),n=new RegExp("^((==)|(~=)|(<=)|(>=)|(<<)|(>>)|(\\.[\\+\\-\\*/\\^\\\\]))"),i=new RegExp("^((!=)|(\\+=)|(\\-=)|(\\*=)|(/=)|(&=)|(\\|=)|(\\^=))"),o=new RegExp("^((>>=)|(<<=))"),a=new RegExp("^[\\]\\)]"),l=new RegExp("^[_A-Za-z¡-￿][_A-Za-z0-9¡-￿]*"),s=e(["error","eval","function","abs","acos","atan","asin","cos","cosh","exp","log","prod","sum","log10","max","min","sign","sin","sinh","sqrt","tan","reshape","break","zeros","default","margin","round","ones","rand","syn","ceil","floor","size","clear","zeros","eye","mean","std","cov","det","eig","inv","norm","rank","trace","expm","logm","sqrtm","linspace","plot","title","xlabel","ylabel","legend","text","grid","meshgrid","mesh","num2str","fft","ifft","arrayfun","cellfun","input","fliplr","flipud","ismember"]),c=e(["return","case","switch","else","elseif","end","endif","endfunction","if","otherwise","do","for","while","try","catch","classdef","properties","events","methods","global","persistent","endfor","endwhile","printf","sprintf","disp","until","continue","pkg"])
function u(e,t){return e.sol()||"'"!==e.peek()?(t.tokenize=f,f(e,t)):(e.next(),t.tokenize=f,"operator")}function d(e,t){return e.match(/^.*%}/)?(t.tokenize=f,"comment"):(e.skipToEnd(),"comment")}function f(p,h){if(p.eatSpace())return null
if(p.match("%{"))return h.tokenize=d,p.skipToEnd(),"comment"
if(p.match(/^[%#]/))return p.skipToEnd(),"comment"
if(p.match(/^[0-9\.+-]/,!1)){if(p.match(/^[+-]?0x[0-9a-fA-F]+[ij]?/))return p.tokenize=f,"number"
if(p.match(/^[+-]?\d*\.\d+([EeDd][+-]?\d+)?[ij]?/))return"number"
if(p.match(/^[+-]?\d+([EeDd][+-]?\d+)?[ij]?/))return"number"}if(p.match(e(["nan","NaN","inf","Inf"])))return"number"
var m=p.match(/^"(?:[^"]|"")*("|$)/)||p.match(/^'(?:[^']|'')*('|$)/)
return m?m[1]?"string":"string error":p.match(c)?"keyword":p.match(s)?"builtin":p.match(l)?"variable":p.match(t)||p.match(n)?"operator":p.match(r)||p.match(i)||p.match(o)?null:p.match(a)?(h.tokenize=u,null):(p.next(),"error")}return{startState:function(){return{tokenize:f}},token:function(e,t){var r=t.tokenize(e,t)
return"number"!==r&&"variable"!==r||(t.tokenize=u),r},lineComment:"%",fold:"indent"}})),e.defineMIME("text/x-octave","octave")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
e.defineMode("pascal",(function(){var e=function(e){for(var t={},r=e.split(" "),n=0;n<r.length;++n)t[r[n]]=!0
return t}("absolute and array asm begin case const constructor destructor div do downto else end file for function goto if implementation in inherited inline interface label mod nil not object of operator or packed procedure program record reintroduce repeat self set shl shr string then to type unit until uses var while with xor as class dispinterface except exports finalization finally initialization inline is library on out packed property raise resourcestring threadvar try absolute abstract alias assembler bitpacked break cdecl continue cppdecl cvar default deprecated dynamic enumerator experimental export external far far16 forward generic helper implements index interrupt iocheck local message name near nodefault noreturn nostackframe oldfpccall otherwise overload override pascal platform private protected public published read register reintroduce result safecall saveregisters softfloat specialize static stdcall stored strict unaligned unimplemented varargs virtual write"),t={null:!0},r=/[+\-*&%=<>!?|\/]/
function n(n,o){var a,l=n.next()
if("#"==l&&o.startOfLine)return n.skipToEnd(),"meta"
if('"'==l||"'"==l)return o.tokenize=(a=l,function(e,t){for(var r,n=!1,i=!1;null!=(r=e.next());){if(r==a&&!n){i=!0
break}n=!n&&"\\"==r}return!i&&n||(t.tokenize=null),"string"}),o.tokenize(n,o)
if("("==l&&n.eat("*"))return o.tokenize=i,i(n,o)
if(/[\[\]{}\(\),;\:\.]/.test(l))return null
if(/\d/.test(l))return n.eatWhile(/[\w\.]/),"number"
if("/"==l&&n.eat("/"))return n.skipToEnd(),"comment"
if(r.test(l))return n.eatWhile(r),"operator"
n.eatWhile(/[\w\$_]/)
var s=n.current()
return e.propertyIsEnumerable(s)?"keyword":t.propertyIsEnumerable(s)?"atom":"variable"}function i(e,t){for(var r,n=!1;r=e.next();){if(")"==r&&n){t.tokenize=null
break}n="*"==r}return"comment"}return{startState:function(){return{tokenize:null}},token:function(e,t){if(e.eatSpace())return null
var r=(t.tokenize||n)(e,t)
return r},electricChars:"{}"}})),e.defineMIME("text/x-pascal","pascal")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
function t(e,t){return e.string.charAt(e.pos+(t||0))}function r(e,t){if(t){var r=e.pos-t
return e.string.substr(r>=0?r:0,t)}return e.string.substr(0,e.pos-1)}function n(e,t){var r=e.string.length,n=r-e.pos+1
return e.string.substr(e.pos,t&&t<r?t:n)}function i(e,t){var r,n=e.pos+t
n<=0?e.pos=0:n>=(r=e.string.length-1)?e.pos=r:e.pos=n}e.defineMode("perl",(function(){var e={"->":4,"++":4,"--":4,"**":4,"=~":4,"!~":4,"*":4,"/":4,"%":4,x:4,"+":4,"-":4,".":4,"<<":4,">>":4,"<":4,">":4,"<=":4,">=":4,lt:4,gt:4,le:4,ge:4,"==":4,"!=":4,"<=>":4,eq:4,ne:4,cmp:4,"~~":4,"&":4,"|":4,"^":4,"&&":4,"||":4,"//":4,"..":4,"...":4,"?":4,":":4,"=":4,"+=":4,"-=":4,"*=":4,",":4,"=>":4,"::":4,not:4,and:4,or:4,xor:4,BEGIN:[5,1],END:[5,1],PRINT:[5,1],PRINTF:[5,1],GETC:[5,1],READ:[5,1],READLINE:[5,1],DESTROY:[5,1],TIE:[5,1],TIEHANDLE:[5,1],UNTIE:[5,1],STDIN:5,STDIN_TOP:5,STDOUT:5,STDOUT_TOP:5,STDERR:5,STDERR_TOP:5,$ARG:5,$_:5,"@ARG":5,"@_":5,$LIST_SEPARATOR:5,'$"':5,$PROCESS_ID:5,$PID:5,$$:5,$REAL_GROUP_ID:5,$GID:5,"$(":5,$EFFECTIVE_GROUP_ID:5,$EGID:5,"$)":5,$PROGRAM_NAME:5,$0:5,$SUBSCRIPT_SEPARATOR:5,$SUBSEP:5,"$;":5,$REAL_USER_ID:5,$UID:5,"$<":5,$EFFECTIVE_USER_ID:5,$EUID:5,"$>":5,$a:5,$b:5,$COMPILING:5,"$^C":5,$DEBUGGING:5,"$^D":5,"${^ENCODING}":5,$ENV:5,"%ENV":5,$SYSTEM_FD_MAX:5,"$^F":5,"@F":5,"${^GLOBAL_PHASE}":5,"$^H":5,"%^H":5,"@INC":5,"%INC":5,$INPLACE_EDIT:5,"$^I":5,"$^M":5,$OSNAME:5,"$^O":5,"${^OPEN}":5,$PERLDB:5,"$^P":5,$SIG:5,"%SIG":5,$BASETIME:5,"$^T":5,"${^TAINT}":5,"${^UNICODE}":5,"${^UTF8CACHE}":5,"${^UTF8LOCALE}":5,$PERL_VERSION:5,"$^V":5,"${^WIN32_SLOPPY_STAT}":5,$EXECUTABLE_NAME:5,"$^X":5,$1:5,$MATCH:5,"$&":5,"${^MATCH}":5,$PREMATCH:5,"$`":5,"${^PREMATCH}":5,$POSTMATCH:5,"$'":5,"${^POSTMATCH}":5,$LAST_PAREN_MATCH:5,"$+":5,$LAST_SUBMATCH_RESULT:5,"$^N":5,"@LAST_MATCH_END":5,"@+":5,"%LAST_PAREN_MATCH":5,"%+":5,"@LAST_MATCH_START":5,"@-":5,"%LAST_MATCH_START":5,"%-":5,$LAST_REGEXP_CODE_RESULT:5,"$^R":5,"${^RE_DEBUG_FLAGS}":5,"${^RE_TRIE_MAXBUF}":5,$ARGV:5,"@ARGV":5,ARGV:5,ARGVOUT:5,$OUTPUT_FIELD_SEPARATOR:5,$OFS:5,"$,":5,$INPUT_LINE_NUMBER:5,$NR:5,"$.":5,$INPUT_RECORD_SEPARATOR:5,$RS:5,"$/":5,$OUTPUT_RECORD_SEPARATOR:5,$ORS:5,"$\\":5,$OUTPUT_AUTOFLUSH:5,"$|":5,$ACCUMULATOR:5,"$^A":5,$FORMAT_FORMFEED:5,"$^L":5,$FORMAT_PAGE_NUMBER:5,"$%":5,$FORMAT_LINES_LEFT:5,"$-":5,$FORMAT_LINE_BREAK_CHARACTERS:5,"$:":5,$FORMAT_LINES_PER_PAGE:5,"$=":5,$FORMAT_TOP_NAME:5,"$^":5,$FORMAT_NAME:5,"$~":5,"${^CHILD_ERROR_NATIVE}":5,$EXTENDED_OS_ERROR:5,"$^E":5,$EXCEPTIONS_BEING_CAUGHT:5,"$^S":5,$WARNING:5,"$^W":5,"${^WARNING_BITS}":5,$OS_ERROR:5,$ERRNO:5,"$!":5,"%OS_ERROR":5,"%ERRNO":5,"%!":5,$CHILD_ERROR:5,"$?":5,$EVAL_ERROR:5,"$@":5,$OFMT:5,"$#":5,"$*":5,$ARRAY_BASE:5,"$[":5,$OLD_PERL_VERSION:5,"$]":5,if:[1,1],elsif:[1,1],else:[1,1],while:[1,1],unless:[1,1],for:[1,1],foreach:[1,1],abs:1,accept:1,alarm:1,atan2:1,bind:1,binmode:1,bless:1,bootstrap:1,break:1,caller:1,chdir:1,chmod:1,chomp:1,chop:1,chown:1,chr:1,chroot:1,close:1,closedir:1,connect:1,continue:[1,1],cos:1,crypt:1,dbmclose:1,dbmopen:1,default:1,defined:1,delete:1,die:1,do:1,dump:1,each:1,endgrent:1,endhostent:1,endnetent:1,endprotoent:1,endpwent:1,endservent:1,eof:1,eval:1,exec:1,exists:1,exit:1,exp:1,fcntl:1,fileno:1,flock:1,fork:1,format:1,formline:1,getc:1,getgrent:1,getgrgid:1,getgrnam:1,gethostbyaddr:1,gethostbyname:1,gethostent:1,getlogin:1,getnetbyaddr:1,getnetbyname:1,getnetent:1,getpeername:1,getpgrp:1,getppid:1,getpriority:1,getprotobyname:1,getprotobynumber:1,getprotoent:1,getpwent:1,getpwnam:1,getpwuid:1,getservbyname:1,getservbyport:1,getservent:1,getsockname:1,getsockopt:1,given:1,glob:1,gmtime:1,goto:1,grep:1,hex:1,import:1,index:1,int:1,ioctl:1,join:1,keys:1,kill:1,last:1,lc:1,lcfirst:1,length:1,link:1,listen:1,local:2,localtime:1,lock:1,log:1,lstat:1,m:null,map:1,mkdir:1,msgctl:1,msgget:1,msgrcv:1,msgsnd:1,my:2,new:1,next:1,no:1,oct:1,open:1,opendir:1,ord:1,our:2,pack:1,package:1,pipe:1,pop:1,pos:1,print:1,printf:1,prototype:1,push:1,q:null,qq:null,qr:null,quotemeta:null,qw:null,qx:null,rand:1,read:1,readdir:1,readline:1,readlink:1,readpipe:1,recv:1,redo:1,ref:1,rename:1,require:1,reset:1,return:1,reverse:1,rewinddir:1,rindex:1,rmdir:1,s:null,say:1,scalar:1,seek:1,seekdir:1,select:1,semctl:1,semget:1,semop:1,send:1,setgrent:1,sethostent:1,setnetent:1,setpgrp:1,setpriority:1,setprotoent:1,setpwent:1,setservent:1,setsockopt:1,shift:1,shmctl:1,shmget:1,shmread:1,shmwrite:1,shutdown:1,sin:1,sleep:1,socket:1,socketpair:1,sort:1,splice:1,split:1,sprintf:1,sqrt:1,srand:1,stat:1,state:1,study:1,sub:1,substr:1,symlink:1,syscall:1,sysopen:1,sysread:1,sysseek:1,system:1,syswrite:1,tell:1,telldir:1,tie:1,tied:1,time:1,times:1,tr:null,truncate:1,uc:1,ucfirst:1,umask:1,undef:1,unlink:1,unpack:1,unshift:1,untie:1,use:1,utime:1,values:1,vec:1,wait:1,waitpid:1,wantarray:1,warn:1,when:1,write:1,y:null},o="string-2",a=/[goseximacplud]/
function l(e,t,r,n,i){return t.chain=null,t.style=null,t.tail=null,t.tokenize=function(e,t){for(var o,a=!1,l=0;o=e.next();){if(o===r[l]&&!a)return void 0!==r[++l]?(t.chain=r[l],t.style=n,t.tail=i):i&&e.eatWhile(i),t.tokenize=c,n
a=!a&&"\\"==o}return n},t.tokenize(e,t)}function s(e,t,r){return t.tokenize=function(e,t){return e.string==r&&(t.tokenize=c),e.skipToEnd(),"string"},t.tokenize(e,t)}function c(c,u){if(c.eatSpace())return null
if(u.chain)return l(c,u,u.chain,u.style,u.tail)
if(c.match(/^\-?[\d\.]/,!1)&&c.match(/^(\-?(\d*\.\d+(e[+-]?\d+)?|\d+\.\d*)|0x[\da-fA-F]+|0b[01]+|\d+(e[+-]?\d+)?)/))return"number"
if(c.match(/^<<(?=\w)/))return c.eatWhile(/\w/),s(c,u,c.current().substr(2))
if(c.sol()&&c.match(/^\=item(?!\w)/))return s(c,u,"=cut")
var d=c.next()
if('"'==d||"'"==d){if(r(c,3)=="<<"+d){var f=c.pos
c.eatWhile(/\w/)
var p=c.current().substr(1)
if(p&&c.eat(d))return s(c,u,p)
c.pos=f}return l(c,u,[d],"string")}if("q"==d&&(!(h=t(c,-2))||!/\w/.test(h)))if("x"==(h=t(c,0))){if("("==(h=t(c,1)))return i(c,2),l(c,u,[")"],o,a)
if("["==h)return i(c,2),l(c,u,["]"],o,a)
if("{"==h)return i(c,2),l(c,u,["}"],o,a)
if("<"==h)return i(c,2),l(c,u,[">"],o,a)
if(/[\^'"!~\/]/.test(h))return i(c,1),l(c,u,[c.eat(h)],o,a)}else if("q"==h){if("("==(h=t(c,1)))return i(c,2),l(c,u,[")"],"string")
if("["==h)return i(c,2),l(c,u,["]"],"string")
if("{"==h)return i(c,2),l(c,u,["}"],"string")
if("<"==h)return i(c,2),l(c,u,[">"],"string")
if(/[\^'"!~\/]/.test(h))return i(c,1),l(c,u,[c.eat(h)],"string")}else if("w"==h){if("("==(h=t(c,1)))return i(c,2),l(c,u,[")"],"bracket")
if("["==h)return i(c,2),l(c,u,["]"],"bracket")
if("{"==h)return i(c,2),l(c,u,["}"],"bracket")
if("<"==h)return i(c,2),l(c,u,[">"],"bracket")
if(/[\^'"!~\/]/.test(h))return i(c,1),l(c,u,[c.eat(h)],"bracket")}else if("r"==h){if("("==(h=t(c,1)))return i(c,2),l(c,u,[")"],o,a)
if("["==h)return i(c,2),l(c,u,["]"],o,a)
if("{"==h)return i(c,2),l(c,u,["}"],o,a)
if("<"==h)return i(c,2),l(c,u,[">"],o,a)
if(/[\^'"!~\/]/.test(h))return i(c,1),l(c,u,[c.eat(h)],o,a)}else if(/[\^'"!~\/(\[{<]/.test(h)){if("("==h)return i(c,1),l(c,u,[")"],"string")
if("["==h)return i(c,1),l(c,u,["]"],"string")
if("{"==h)return i(c,1),l(c,u,["}"],"string")
if("<"==h)return i(c,1),l(c,u,[">"],"string")
if(/[\^'"!~\/]/.test(h))return l(c,u,[c.eat(h)],"string")}if("m"==d&&((!(h=t(c,-2))||!/\w/.test(h))&&(h=c.eat(/[(\[{<\^'"!~\/]/)))){if(/[\^'"!~\/]/.test(h))return l(c,u,[h],o,a)
if("("==h)return l(c,u,[")"],o,a)
if("["==h)return l(c,u,["]"],o,a)
if("{"==h)return l(c,u,["}"],o,a)
if("<"==h)return l(c,u,[">"],o,a)}if("s"==d&&(!(h=/[\/>\]})\w]/.test(t(c,-2)))&&(h=c.eat(/[(\[{<\^'"!~\/]/))))return l(c,u,"["==h?["]","]"]:"{"==h?["}","}"]:"<"==h?[">",">"]:"("==h?[")",")"]:[h,h],o,a)
if("y"==d&&(!(h=/[\/>\]})\w]/.test(t(c,-2)))&&(h=c.eat(/[(\[{<\^'"!~\/]/))))return l(c,u,"["==h?["]","]"]:"{"==h?["}","}"]:"<"==h?[">",">"]:"("==h?[")",")"]:[h,h],o,a)
if("t"==d&&(!(h=/[\/>\]})\w]/.test(t(c,-2)))&&(h=c.eat("r"))&&(h=c.eat(/[(\[{<\^'"!~\/]/))))return l(c,u,"["==h?["]","]"]:"{"==h?["}","}"]:"<"==h?[">",">"]:"("==h?[")",")"]:[h,h],o,a)
if("`"==d)return l(c,u,[d],"variable-2")
if("/"==d)return/~\s*$/.test(r(c))?l(c,u,[d],o,a):"operator"
if("$"==d){f=c.pos
if(c.eatWhile(/\d/)||c.eat("{")&&c.eatWhile(/\d/)&&c.eat("}"))return"variable-2"
c.pos=f}if(/[$@%]/.test(d)){f=c.pos
if(c.eat("^")&&c.eat(/[A-Z]/)||!/[@$%&]/.test(t(c,-2))&&c.eat(/[=|\\\-#?@;:&`~\^!\[\]*'"$+.,\/<>()]/)){var h=c.current()
if(e[h])return"variable-2"}c.pos=f}if(/[$@%&]/.test(d)&&(c.eatWhile(/[\w$\[\]]/)||c.eat("{")&&c.eatWhile(/[\w$\[\]]/)&&c.eat("}"))){h=c.current()
return e[h]?"variable-2":"variable"}if("#"==d&&"$"!=t(c,-2))return c.skipToEnd(),"comment"
if(/[:+\-\^*$&%@=<>!?|\/~\.]/.test(d)){f=c.pos
if(c.eatWhile(/[:+\-\^*$&%@=<>!?|\/~\.]/),e[c.current()])return"operator"
c.pos=f}if("_"==d&&1==c.pos){if("_END__"==n(c,6))return l(c,u,["\0"],"comment")
if("_DATA__"==n(c,7))return l(c,u,["\0"],"variable-2")
if("_C__"==n(c,7))return l(c,u,["\0"],"string")}if(/\w/.test(d)){f=c.pos
if("{"==t(c,-2)&&("}"==t(c,0)||c.eatWhile(/\w/)&&"}"==t(c,0)))return"string"
c.pos=f}if(/[A-Z]/.test(d)){var m=t(c,-2)
f=c.pos
if(c.eatWhile(/[A-Z_]/),!/[\da-z]/.test(t(c,0)))return(h=e[c.current()])?(h[1]&&(h=h[0]),":"!=m?1==h?"keyword":2==h?"def":3==h?"atom":4==h?"operator":5==h?"variable-2":"meta":"meta"):"meta"
c.pos=f}if(/[a-zA-Z_]/.test(d)){m=t(c,-2)
return c.eatWhile(/\w/),(h=e[c.current()])?(h[1]&&(h=h[0]),":"!=m?1==h?"keyword":2==h?"def":3==h?"atom":4==h?"operator":5==h?"variable-2":"meta":"meta"):"meta"}return null}return{startState:function(){return{tokenize:c,chain:null,style:null,tail:null}},token:function(e,t){return(t.tokenize||c)(e,t)},lineComment:"#"}})),e.registerHelper("wordChars","perl",/[\w$]/),e.defineMIME("text/x-perl","perl")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror"),require("../htmlmixed/htmlmixed"),require("../clike/clike")):"function"==typeof define&&define.amd?define(["../../lib/codemirror","../htmlmixed/htmlmixed","../clike/clike"],e):e(CodeMirror)}((function(e){"use strict"
function t(e){for(var t={},r=e.split(" "),n=0;n<r.length;++n)t[r[n]]=!0
return t}function r(e,t,i){return 0==e.length?n(t):function(o,a){for(var l=e[0],s=0;s<l.length;s++)if(o.match(l[s][0]))return a.tokenize=r(e.slice(1),t),l[s][1]
return a.tokenize=n(t,i),"string"}}function n(e,t){return function(n,i){return function(e,t,n,i){if(!1!==i&&e.match("${",!1)||e.match("{$",!1))return t.tokenize=null,"string"
if(!1!==i&&e.match(/^\$[a-zA-Z_][a-zA-Z0-9_]*/))return e.match("[",!1)&&(t.tokenize=r([[["[",null]],[[/\d[\w\.]*/,"number"],[/\$[a-zA-Z_][a-zA-Z0-9_]*/,"variable-2"],[/[\w\$]+/,"variable"]],[["]",null]]],n,i)),e.match(/\-\>\w/,!1)&&(t.tokenize=r([[["->",null]],[[/[\w]+/,"variable"]]],n,i)),"variable-2"
var o=!1
for(;!e.eol()&&(o||!1===i||!e.match("{$",!1)&&!e.match(/^(\$[a-zA-Z_][a-zA-Z0-9_]*|\$\{)/,!1));){if(!o&&e.match(n)){t.tokenize=null,t.tokStack.pop(),t.tokStack.pop()
break}o="\\"==e.next()&&!o}return"string"}(n,i,e,t)}}var i="abstract and array as break case catch class clone const continue declare default do else elseif enddeclare endfor endforeach endif endswitch endwhile extends final for foreach function global goto if implements interface instanceof namespace new or private protected public static switch throw trait try use var while xor die echo empty exit eval include include_once isset list require require_once return print unset __halt_compiler self static parent yield insteadof finally",o="true false null TRUE FALSE NULL __CLASS__ __DIR__ __FILE__ __LINE__ __METHOD__ __FUNCTION__ __NAMESPACE__ __TRAIT__",a="func_num_args func_get_arg func_get_args strlen strcmp strncmp strcasecmp strncasecmp each error_reporting define defined trigger_error user_error set_error_handler restore_error_handler get_declared_classes get_loaded_extensions extension_loaded get_extension_funcs debug_backtrace constant bin2hex hex2bin sleep usleep time mktime gmmktime strftime gmstrftime strtotime date gmdate getdate localtime checkdate flush wordwrap htmlspecialchars htmlentities html_entity_decode md5 md5_file crc32 getimagesize image_type_to_mime_type phpinfo phpversion phpcredits strnatcmp strnatcasecmp substr_count strspn strcspn strtok strtoupper strtolower strpos strrpos strrev hebrev hebrevc nl2br basename dirname pathinfo stripslashes stripcslashes strstr stristr strrchr str_shuffle str_word_count strcoll substr substr_replace quotemeta ucfirst ucwords strtr addslashes addcslashes rtrim str_replace str_repeat count_chars chunk_split trim ltrim strip_tags similar_text explode implode setlocale localeconv parse_str str_pad chop strchr sprintf printf vprintf vsprintf sscanf fscanf parse_url urlencode urldecode rawurlencode rawurldecode readlink linkinfo link unlink exec system escapeshellcmd escapeshellarg passthru shell_exec proc_open proc_close rand srand getrandmax mt_rand mt_srand mt_getrandmax base64_decode base64_encode abs ceil floor round is_finite is_nan is_infinite bindec hexdec octdec decbin decoct dechex base_convert number_format fmod ip2long long2ip getenv putenv getopt microtime gettimeofday getrusage uniqid quoted_printable_decode set_time_limit get_cfg_var magic_quotes_runtime set_magic_quotes_runtime get_magic_quotes_gpc get_magic_quotes_runtime import_request_variables error_log serialize unserialize memory_get_usage var_dump var_export debug_zval_dump print_r highlight_file show_source highlight_string ini_get ini_get_all ini_set ini_alter ini_restore get_include_path set_include_path restore_include_path setcookie header headers_sent connection_aborted connection_status ignore_user_abort parse_ini_file is_uploaded_file move_uploaded_file intval floatval doubleval strval gettype settype is_null is_resource is_bool is_long is_float is_int is_integer is_double is_real is_numeric is_string is_array is_object is_scalar ereg ereg_replace eregi eregi_replace split spliti join sql_regcase dl pclose popen readfile rewind rmdir umask fclose feof fgetc fgets fgetss fread fopen fpassthru ftruncate fstat fseek ftell fflush fwrite fputs mkdir rename copy tempnam tmpfile file file_get_contents file_put_contents stream_select stream_context_create stream_context_set_params stream_context_set_option stream_context_get_options stream_filter_prepend stream_filter_append fgetcsv flock get_meta_tags stream_set_write_buffer set_file_buffer set_socket_blocking stream_set_blocking socket_set_blocking stream_get_meta_data stream_register_wrapper stream_wrapper_register stream_set_timeout socket_set_timeout socket_get_status realpath fnmatch fsockopen pfsockopen pack unpack get_browser crypt opendir closedir chdir getcwd rewinddir readdir dir glob fileatime filectime filegroup fileinode filemtime fileowner fileperms filesize filetype file_exists is_writable is_writeable is_readable is_executable is_file is_dir is_link stat lstat chown touch clearstatcache mail ob_start ob_flush ob_clean ob_end_flush ob_end_clean ob_get_flush ob_get_clean ob_get_length ob_get_level ob_get_status ob_get_contents ob_implicit_flush ob_list_handlers ksort krsort natsort natcasesort asort arsort sort rsort usort uasort uksort shuffle array_walk count end prev next reset current key min max in_array array_search extract compact array_fill range array_multisort array_push array_pop array_shift array_unshift array_splice array_slice array_merge array_merge_recursive array_keys array_values array_count_values array_reverse array_reduce array_pad array_flip array_change_key_case array_rand array_unique array_intersect array_intersect_assoc array_diff array_diff_assoc array_sum array_filter array_map array_chunk array_key_exists array_intersect_key array_combine array_column pos sizeof key_exists assert assert_options version_compare ftok str_rot13 aggregate session_name session_module_name session_save_path session_id session_regenerate_id session_decode session_register session_unregister session_is_registered session_encode session_start session_destroy session_unset session_set_save_handler session_cache_limiter session_cache_expire session_set_cookie_params session_get_cookie_params session_write_close preg_match preg_match_all preg_replace preg_replace_callback preg_split preg_quote preg_grep overload ctype_alnum ctype_alpha ctype_cntrl ctype_digit ctype_lower ctype_graph ctype_print ctype_punct ctype_space ctype_upper ctype_xdigit virtual apache_request_headers apache_note apache_lookup_uri apache_child_terminate apache_setenv apache_response_headers apache_get_version getallheaders mysql_connect mysql_pconnect mysql_close mysql_select_db mysql_create_db mysql_drop_db mysql_query mysql_unbuffered_query mysql_db_query mysql_list_dbs mysql_list_tables mysql_list_fields mysql_list_processes mysql_error mysql_errno mysql_affected_rows mysql_insert_id mysql_result mysql_num_rows mysql_num_fields mysql_fetch_row mysql_fetch_array mysql_fetch_assoc mysql_fetch_object mysql_data_seek mysql_fetch_lengths mysql_fetch_field mysql_field_seek mysql_free_result mysql_field_name mysql_field_table mysql_field_len mysql_field_type mysql_field_flags mysql_escape_string mysql_real_escape_string mysql_stat mysql_thread_id mysql_client_encoding mysql_get_client_info mysql_get_host_info mysql_get_proto_info mysql_get_server_info mysql_info mysql mysql_fieldname mysql_fieldtable mysql_fieldlen mysql_fieldtype mysql_fieldflags mysql_selectdb mysql_createdb mysql_dropdb mysql_freeresult mysql_numfields mysql_numrows mysql_listdbs mysql_listtables mysql_listfields mysql_db_name mysql_dbname mysql_tablename mysql_table_name pg_connect pg_pconnect pg_close pg_connection_status pg_connection_busy pg_connection_reset pg_host pg_dbname pg_port pg_tty pg_options pg_ping pg_query pg_send_query pg_cancel_query pg_fetch_result pg_fetch_row pg_fetch_assoc pg_fetch_array pg_fetch_object pg_fetch_all pg_affected_rows pg_get_result pg_result_seek pg_result_status pg_free_result pg_last_oid pg_num_rows pg_num_fields pg_field_name pg_field_num pg_field_size pg_field_type pg_field_prtlen pg_field_is_null pg_get_notify pg_get_pid pg_result_error pg_last_error pg_last_notice pg_put_line pg_end_copy pg_copy_to pg_copy_from pg_trace pg_untrace pg_lo_create pg_lo_unlink pg_lo_open pg_lo_close pg_lo_read pg_lo_write pg_lo_read_all pg_lo_import pg_lo_export pg_lo_seek pg_lo_tell pg_escape_string pg_escape_bytea pg_unescape_bytea pg_client_encoding pg_set_client_encoding pg_meta_data pg_convert pg_insert pg_update pg_delete pg_select pg_exec pg_getlastoid pg_cmdtuples pg_errormessage pg_numrows pg_numfields pg_fieldname pg_fieldsize pg_fieldtype pg_fieldnum pg_fieldprtlen pg_fieldisnull pg_freeresult pg_result pg_loreadall pg_locreate pg_lounlink pg_loopen pg_loclose pg_loread pg_lowrite pg_loimport pg_loexport http_response_code get_declared_traits getimagesizefromstring socket_import_stream stream_set_chunk_size trait_exists header_register_callback class_uses session_status session_register_shutdown echo print global static exit array empty eval isset unset die include require include_once require_once json_decode json_encode json_last_error json_last_error_msg curl_close curl_copy_handle curl_errno curl_error curl_escape curl_exec curl_file_create curl_getinfo curl_init curl_multi_add_handle curl_multi_close curl_multi_exec curl_multi_getcontent curl_multi_info_read curl_multi_init curl_multi_remove_handle curl_multi_select curl_multi_setopt curl_multi_strerror curl_pause curl_reset curl_setopt_array curl_setopt curl_share_close curl_share_init curl_share_setopt curl_strerror curl_unescape curl_version mysqli_affected_rows mysqli_autocommit mysqli_change_user mysqli_character_set_name mysqli_close mysqli_commit mysqli_connect_errno mysqli_connect_error mysqli_connect mysqli_data_seek mysqli_debug mysqli_dump_debug_info mysqli_errno mysqli_error_list mysqli_error mysqli_fetch_all mysqli_fetch_array mysqli_fetch_assoc mysqli_fetch_field_direct mysqli_fetch_field mysqli_fetch_fields mysqli_fetch_lengths mysqli_fetch_object mysqli_fetch_row mysqli_field_count mysqli_field_seek mysqli_field_tell mysqli_free_result mysqli_get_charset mysqli_get_client_info mysqli_get_client_stats mysqli_get_client_version mysqli_get_connection_stats mysqli_get_host_info mysqli_get_proto_info mysqli_get_server_info mysqli_get_server_version mysqli_info mysqli_init mysqli_insert_id mysqli_kill mysqli_more_results mysqli_multi_query mysqli_next_result mysqli_num_fields mysqli_num_rows mysqli_options mysqli_ping mysqli_prepare mysqli_query mysqli_real_connect mysqli_real_escape_string mysqli_real_query mysqli_reap_async_query mysqli_refresh mysqli_rollback mysqli_select_db mysqli_set_charset mysqli_set_local_infile_default mysqli_set_local_infile_handler mysqli_sqlstate mysqli_ssl_set mysqli_stat mysqli_stmt_init mysqli_store_result mysqli_thread_id mysqli_thread_safe mysqli_use_result mysqli_warning_count"
e.registerHelper("hintWords","php",[i,o,a].join(" ").split(" ")),e.registerHelper("wordChars","php",/[\w$]/)
var l={name:"clike",helperType:"php",keywords:t(i),blockKeywords:t("catch do else elseif for foreach if switch try while finally"),defKeywords:t("class function interface namespace trait"),atoms:t(o),builtin:t(a),multiLineStrings:!0,hooks:{$:function(e){return e.eatWhile(/[\w\$_]/),"variable-2"},"<":function(e,t){var r
if(r=e.match(/<<\s*/)){var i=e.eat(/['"]/)
e.eatWhile(/[\w\.]/)
var o=e.current().slice(r[0].length+(i?2:1))
if(i&&e.eat(i),o)return(t.tokStack||(t.tokStack=[])).push(o,0),t.tokenize=n(o,"'"!=i),"string"}return!1},"#":function(e){for(;!e.eol()&&!e.match("?>",!1);)e.next()
return"comment"},"/":function(e){if(e.eat("/")){for(;!e.eol()&&!e.match("?>",!1);)e.next()
return"comment"}return!1},'"':function(e,t){return(t.tokStack||(t.tokStack=[])).push('"',0),t.tokenize=n('"'),"string"},"{":function(e,t){return t.tokStack&&t.tokStack.length&&t.tokStack[t.tokStack.length-1]++,!1},"}":function(e,t){return t.tokStack&&t.tokStack.length>0&&!--t.tokStack[t.tokStack.length-1]&&(t.tokenize=n(t.tokStack[t.tokStack.length-2])),!1}}}
e.defineMode("php",(function(t,r){var n=e.getMode(t,r&&r.htmlMode||"text/html"),i=e.getMode(t,l)
return{startState:function(){var t=e.startState(n),o=r.startOpen?e.startState(i):null
return{html:t,php:o,curMode:r.startOpen?i:n,curState:r.startOpen?o:t,pending:null}},copyState:function(t){var r,o=t.html,a=e.copyState(n,o),l=t.php,s=l&&e.copyState(i,l)
return r=t.curMode==n?a:s,{html:a,php:s,curMode:t.curMode,curState:r,pending:t.pending}},token:function(t,r){var o=r.curMode==i
if(t.sol()&&r.pending&&'"'!=r.pending&&"'"!=r.pending&&(r.pending=null),o)return o&&null==r.php.tokenize&&t.match("?>")?(r.curMode=n,r.curState=r.html,r.php.context.prev||(r.php=null),"meta"):i.token(t,r.curState)
if(t.match(/^<\?\w*/))return r.curMode=i,r.php||(r.php=e.startState(i,n.indent(r.html,"",""))),r.curState=r.php,"meta"
if('"'==r.pending||"'"==r.pending){for(;!t.eol()&&t.next()!=r.pending;);var a="string"}else if(r.pending&&t.pos<r.pending.end){t.pos=r.pending.end
a=r.pending.style}else a=n.token(t,r.curState)
r.pending&&(r.pending=null)
var l,s=t.current(),c=s.search(/<\?/)
return-1!=c&&("string"==a&&(l=s.match(/[\'\"]$/))&&!/\?>/.test(s)?r.pending=l[0]:r.pending={end:t.pos,style:a},t.backUp(s.length-c)),a},indent:function(e,t,r){return e.curMode!=i&&/^\s*<\//.test(t)||e.curMode==i&&/^\?>/.test(t)?n.indent(e.html,t,r):e.curMode.indent(e.curState,t,r)},blockCommentStart:"/*",blockCommentEnd:"*/",lineComment:"//",innerMode:function(e){return{state:e.curState,mode:e.curMode}}}}),"htmlmixed","clike"),e.defineMIME("application/x-httpd-php","php"),e.defineMIME("application/x-httpd-php-open",{name:"php",startOpen:!0}),e.defineMIME("text/x-php",l)})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
function t(e){return new RegExp("^(("+e.join(")|(")+"))\\b")}var r=t(["and","or","not","is"]),n=["as","assert","break","class","continue","def","del","elif","else","except","finally","for","from","global","if","import","lambda","pass","raise","return","try","while","with","yield","in"],i=["abs","all","any","bin","bool","bytearray","callable","chr","classmethod","compile","complex","delattr","dict","dir","divmod","enumerate","eval","filter","float","format","frozenset","getattr","globals","hasattr","hash","help","hex","id","input","int","isinstance","issubclass","iter","len","list","locals","map","max","memoryview","min","next","object","oct","open","ord","pow","property","range","repr","reversed","round","set","setattr","slice","sorted","staticmethod","str","sum","super","tuple","type","vars","zip","__import__","NotImplemented","Ellipsis","__debug__"]
function o(e){return e.scopes[e.scopes.length-1]}e.registerHelper("hintWords","python",n.concat(i)),e.defineMode("python",(function(a,l){for(var s="error",c=l.delimiters||l.singleDelimiters||/^[\(\)\[\]\{\}@,:`=;\.\\]/,u=[l.singleOperators,l.doubleOperators,l.doubleDelimiters,l.tripleDelimiters,l.operators||/^([-+*/%\/&|^]=?|[<>=]+|\/\/=?|\*\*=?|!=|[~!@]|\.\.\.)/],d=0;d<u.length;d++)u[d]||u.splice(d--,1)
var f=l.hangingIndent||a.indentUnit,p=n,h=i
null!=l.extra_keywords&&(p=p.concat(l.extra_keywords)),null!=l.extra_builtins&&(h=h.concat(l.extra_builtins))
var m=!(l.version&&Number(l.version)<3)
if(m){var g=l.identifiers||/^[_A-Za-z\u00A1-\uFFFF][_A-Za-z0-9\u00A1-\uFFFF]*/
p=p.concat(["nonlocal","False","True","None","async","await"]),h=h.concat(["ascii","bytes","exec","print"])
var v=new RegExp("^(([rbuf]|(br)|(fr))?('{3}|\"{3}|['\"]))","i")}else{g=l.identifiers||/^[_A-Za-z][_A-Za-z0-9]*/
p=p.concat(["exec","print"]),h=h.concat(["apply","basestring","buffer","cmp","coerce","execfile","file","intern","long","raw_input","reduce","reload","unichr","unicode","xrange","False","True","None"])
v=new RegExp("^(([rubf]|(ur)|(br))?('{3}|\"{3}|['\"]))","i")}var y=t(p),b=t(h)
function x(e,t){var r=e.sol()&&"\\"!=t.lastToken
if(r&&(t.indent=e.indentation()),r&&"py"==o(t).type){var n=o(t).offset
if(e.eatSpace()){var i=e.indentation()
return i>n?k(t):i<n&&_(e,t)&&"#"!=e.peek()&&(t.errorToken=!0),null}var a=w(e,t)
return n>0&&_(e,t)&&(a+=" error"),a}return w(e,t)}function w(e,t){if(e.eatSpace())return null
if(e.match(/^#.*/))return"comment"
if(e.match(/^[0-9\.]/,!1)){var n=!1
if(e.match(/^[\d_]*\.\d+(e[\+\-]?\d+)?/i)&&(n=!0),e.match(/^[\d_]+\.\d*/)&&(n=!0),e.match(/^\.\d+/)&&(n=!0),n)return e.eat(/J/i),"number"
var i=!1
if(e.match(/^0x[0-9a-f_]+/i)&&(i=!0),e.match(/^0b[01_]+/i)&&(i=!0),e.match(/^0o[0-7_]+/i)&&(i=!0),e.match(/^[1-9][\d_]*(e[\+\-]?[\d_]+)?/)&&(e.eat(/J/i),i=!0),e.match(/^0(?![\dx])/i)&&(i=!0),i)return e.eat(/L/i),"number"}if(e.match(v))return-1!==e.current().toLowerCase().indexOf("f")?(t.tokenize=function(e,t){for(;"rubf".indexOf(e.charAt(0).toLowerCase())>=0;)e=e.substr(1)
var r=1==e.length,n="string"
function i(e){return function(t,r){var n=w(t,r)
return"punctuation"==n&&("{"==t.current()?r.tokenize=i(e+1):"}"==t.current()&&(r.tokenize=e>1?i(e-1):o)),n}}function o(o,a){for(;!o.eol();)if(o.eatWhile(/[^'"\{\}\\]/),o.eat("\\")){if(o.next(),r&&o.eol())return n}else{if(o.match(e))return a.tokenize=t,n
if(o.match("{{"))return n
if(o.match("{",!1))return a.tokenize=i(0),o.current()?n:a.tokenize(o,a)
if(o.match("}}"))return n
if(o.match("}"))return s
o.eat(/['"]/)}if(r){if(l.singleLineStringErrors)return s
a.tokenize=t}return n}return o.isString=!0,o}(e.current(),t.tokenize),t.tokenize(e,t)):(t.tokenize=function(e,t){for(;"rubf".indexOf(e.charAt(0).toLowerCase())>=0;)e=e.substr(1)
var r=1==e.length,n="string"
function i(i,o){for(;!i.eol();)if(i.eatWhile(/[^'"\\]/),i.eat("\\")){if(i.next(),r&&i.eol())return n}else{if(i.match(e))return o.tokenize=t,n
i.eat(/['"]/)}if(r){if(l.singleLineStringErrors)return s
o.tokenize=t}return n}return i.isString=!0,i}(e.current(),t.tokenize),t.tokenize(e,t))
for(var o=0;o<u.length;o++)if(e.match(u[o]))return"operator"
return e.match(c)?"punctuation":"."==t.lastToken&&e.match(g)?"property":e.match(y)||e.match(r)?"keyword":e.match(b)?"builtin":e.match(/^(self|cls)\b/)?"variable-2":e.match(g)?"def"==t.lastToken||"class"==t.lastToken?"def":"variable":(e.next(),s)}function k(e){for(;"py"!=o(e).type;)e.scopes.pop()
e.scopes.push({offset:o(e).offset+a.indentUnit,type:"py",align:null})}function _(e,t){for(var r=e.indentation();t.scopes.length>1&&o(t).offset>r;){if("py"!=o(t).type)return!0
t.scopes.pop()}return o(t).offset!=r}function C(e,t){e.sol()&&(t.beginningOfLine=!0)
var r=t.tokenize(e,t),n=e.current()
if(t.beginningOfLine&&"@"==n)return e.match(g,!1)?"meta":m?"operator":s
if(/\S/.test(n)&&(t.beginningOfLine=!1),"variable"!=r&&"builtin"!=r||"meta"!=t.lastToken||(r="meta"),"pass"!=n&&"return"!=n||(t.dedent+=1),"lambda"==n&&(t.lambda=!0),":"!=n||t.lambda||"py"!=o(t).type||k(t),1==n.length&&!/string|comment/.test(r)){var i="[({".indexOf(n)
if(-1!=i&&function(e,t,r){var n=e.match(/^([\s\[\{\(]|#.*)*$/,!1)?null:e.column()+1
t.scopes.push({offset:t.indent+f,type:r,align:n})}(e,t,"])}".slice(i,i+1)),-1!=(i="])}".indexOf(n))){if(o(t).type!=n)return s
t.indent=t.scopes.pop().offset-f}}return t.dedent>0&&e.eol()&&"py"==o(t).type&&(t.scopes.length>1&&t.scopes.pop(),t.dedent-=1),r}return{startState:function(e){return{tokenize:x,scopes:[{offset:e||0,type:"py",align:null}],indent:e||0,lastToken:null,lambda:!1,dedent:0}},token:function(e,t){var r=t.errorToken
r&&(t.errorToken=!1)
var n=C(e,t)
return n&&"comment"!=n&&(t.lastToken="keyword"==n||"punctuation"==n?e.current():n),"punctuation"==n&&(n=null),e.eol()&&t.lambda&&(t.lambda=!1),r?n+" "+s:n},indent:function(t,r){if(t.tokenize!=x)return t.tokenize.isString?e.Pass:0
var n=o(t),i=n.type==r.charAt(0)
return null!=n.align?n.align-(i?1:0):n.offset-(i?f:0)},electricInput:/^\s*[\}\]\)]$/,closeBrackets:{triples:"'\""},lineComment:"#",fold:"indent"}})),e.defineMIME("text/x-python","python")
var a
e.defineMIME("text/x-cython",{name:"python",extra_keywords:(a="by cdef cimport cpdef ctypedef enum except extern gil include nogil property public readonly struct union DEF IF ELIF ELSE",a.split(" "))})})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
e.registerHelper("wordChars","r",/[\w.]/),e.defineMode("r",(function(t){function r(e){for(var t={},r=0;r<e.length;++r)t[e[r]]=!0
return t}var n=["NULL","NA","Inf","NaN","NA_integer_","NA_real_","NA_complex_","NA_character_","TRUE","FALSE"],i=["list","quote","bquote","eval","return","call","parse","deparse"],o=["if","else","repeat","while","function","for","in","next","break"]
e.registerHelper("hintWords","r",n.concat(i,o))
var a,l=r(n),s=r(i),c=r(o),u=r(["if","else","repeat","while","function","for"]),d=/[+\-*\/^<>=!&|~$:]/
function f(e,t){a=null
var r,n=e.next()
if("#"==n)return e.skipToEnd(),"comment"
if("0"==n&&e.eat("x"))return e.eatWhile(/[\da-f]/i),"number"
if("."==n&&e.eat(/\d/))return e.match(/\d*(?:e[+\-]?\d+)?/),"number"
if(/\d/.test(n))return e.match(/\d*(?:\.\d+)?(?:e[+\-]\d+)?L?/),"number"
if("'"==n||'"'==n)return t.tokenize=(r=n,function(e,t){if(e.eat("\\")){var n=e.next()
return"x"==n?e.match(/^[a-f0-9]{2}/i):("u"==n||"U"==n)&&e.eat("{")&&e.skipTo("}")?e.next():"u"==n?e.match(/^[a-f0-9]{4}/i):"U"==n?e.match(/^[a-f0-9]{8}/i):/[0-7]/.test(n)&&e.match(/^[0-7]{1,2}/),"string-2"}for(var i;null!=(i=e.next());){if(i==r){t.tokenize=f
break}if("\\"==i){e.backUp(1)
break}}return"string"}),"string"
if("`"==n)return e.match(/[^`]+`/),"variable-3"
if("."==n&&e.match(/.[.\d]+/))return"keyword"
if(/[\w\.]/.test(n)&&"_"!=n){e.eatWhile(/[\w\.]/)
var i=e.current()
return l.propertyIsEnumerable(i)?"atom":c.propertyIsEnumerable(i)?(u.propertyIsEnumerable(i)&&!e.match(/\s*if(\s+|$)/,!1)&&(a="block"),"keyword"):s.propertyIsEnumerable(i)?"builtin":"variable"}return"%"==n?(e.skipTo("%")&&e.next(),"operator variable-2"):"<"==n&&e.eat("-")||"<"==n&&e.match("<-")||"-"==n&&e.match(/>>?/)?"operator arrow":"="==n&&t.ctx.argList?"arg-is":d.test(n)?"$"==n?"operator dollar":(e.eatWhile(d),"operator"):/[\(\){}\[\];]/.test(n)?(a=n,";"==n?"semi":null):null}function p(e,t,r){e.ctx={type:t,indent:e.indent,flags:0,column:r.column(),prev:e.ctx}}function h(e,t){var r=e.ctx
e.ctx={type:r.type,indent:r.indent,flags:r.flags|t,column:r.column,prev:r.prev}}function m(e){e.indent=e.ctx.indent,e.ctx=e.ctx.prev}return{startState:function(){return{tokenize:f,ctx:{type:"top",indent:-t.indentUnit,flags:2},indent:0,afterIdent:!1}},token:function(e,t){if(e.sol()&&(0==(3&t.ctx.flags)&&(t.ctx.flags|=2),4&t.ctx.flags&&m(t),t.indent=e.indentation()),e.eatSpace())return null
var r=t.tokenize(e,t)
return"comment"!=r&&0==(2&t.ctx.flags)&&h(t,1),";"!=a&&"{"!=a&&"}"!=a||"block"!=t.ctx.type||m(t),"{"==a?p(t,"}",e):"("==a?(p(t,")",e),t.afterIdent&&(t.ctx.argList=!0)):"["==a?p(t,"]",e):"block"==a?p(t,"block",e):a==t.ctx.type?m(t):"block"==t.ctx.type&&"comment"!=r&&h(t,4),t.afterIdent="variable"==r||"keyword"==r,r},indent:function(e,r){if(e.tokenize!=f)return 0
var n=r&&r.charAt(0),i=e.ctx,o=n==i.type
return 4&i.flags&&(i=i.prev),"block"==i.type?i.indent+("{"==n?0:t.indentUnit):1&i.flags?i.column+(o?0:1):i.indent+(o?0:t.indentUnit)},lineComment:"#"}})),e.defineMIME("text/x-rsrc","r")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
e.defineMode("ruby",(function(t){function r(e){for(var t={},r=0,n=e.length;r<n;++r)t[e[r]]=!0
return t}var n,i=r(["alias","and","BEGIN","begin","break","case","class","def","defined?","do","else","elsif","END","end","ensure","false","for","if","in","module","next","not","or","redo","rescue","retry","return","self","super","then","true","undef","unless","until","when","while","yield","nil","raise","throw","catch","fail","loop","callcc","caller","lambda","proc","public","protected","private","require","load","require_relative","extend","autoload","__END__","__FILE__","__LINE__","__dir__"]),o=r(["def","class","case","for","while","until","module","then","catch","loop","proc","begin"]),a=r(["end","until"]),l={"[":"]","{":"}","(":")"},s={"]":"[","}":"{",")":"("}
function c(e,t,r){return r.tokenize.push(e),e(t,r)}function u(e,t){if(e.sol()&&e.match("=begin")&&e.eol())return t.tokenize.push(h),"comment"
if(e.eatSpace())return null
var r,i,o,a=e.next()
if("`"==a||"'"==a||'"'==a)return c(p(a,"string",'"'==a||"`"==a),e,t)
if("/"==a)return function(e){var t,r=e.pos,n=0,i=!1,o=!1
for(;null!=(t=e.next());)if(o)o=!1
else{if("[{(".indexOf(t)>-1)n++
else if("]})".indexOf(t)>-1){if(--n<0)break}else if("/"==t&&0==n){i=!0
break}o="\\"==t}return e.backUp(e.pos-r),i}(e)?c(p(a,"string-2",!0),e,t):"operator"
if("%"==a){var s="string",u=!0
e.eat("s")?s="atom":e.eat(/[WQ]/)?s="string":e.eat(/[r]/)?s="string-2":e.eat(/[wxq]/)&&(s="string",u=!1)
var d=e.eat(/[^\w\s=]/)
return d?(l.propertyIsEnumerable(d)&&(d=l[d]),c(p(d,s,u,!0),e,t)):"operator"}if("#"==a)return e.skipToEnd(),"comment"
if("<"==a&&(r=e.match(/^<([-~])[\`\"\']?([a-zA-Z_?]\w*)[\`\"\']?(?:;|$)/)))return c((i=r[2],o=r[1],function(e,t){return o&&e.eatSpace(),e.match(i)?t.tokenize.pop():e.skipToEnd(),"string"}),e,t)
if("0"==a)return e.eat("x")?e.eatWhile(/[\da-fA-F]/):e.eat("b")?e.eatWhile(/[01]/):e.eatWhile(/[0-7]/),"number"
if(/\d/.test(a))return e.match(/^[\d_]*(?:\.[\d_]+)?(?:[eE][+\-]?[\d_]+)?/),"number"
if("?"==a){for(;e.match(/^\\[CM]-/););return e.eat("\\")?e.eatWhile(/\w/):e.next(),"string"}if(":"==a)return e.eat("'")?c(p("'","atom",!1),e,t):e.eat('"')?c(p('"',"atom",!0),e,t):e.eat(/[\<\>]/)?(e.eat(/[\<\>]/),"atom"):e.eat(/[\+\-\*\/\&\|\:\!]/)?"atom":e.eat(/[a-zA-Z$@_\xa1-\uffff]/)?(e.eatWhile(/[\w$\xa1-\uffff]/),e.eat(/[\?\!\=]/),"atom"):"operator"
if("@"==a&&e.match(/^@?[a-zA-Z_\xa1-\uffff]/))return e.eat("@"),e.eatWhile(/[\w\xa1-\uffff]/),"variable-2"
if("$"==a)return e.eat(/[a-zA-Z_]/)?e.eatWhile(/[\w]/):e.eat(/\d/)?e.eat(/\d/):e.next(),"variable-3"
if(/[a-zA-Z_\xa1-\uffff]/.test(a))return e.eatWhile(/[\w\xa1-\uffff]/),e.eat(/[\?\!]/),e.eat(":")?"atom":"ident"
if("|"!=a||!t.varList&&"{"!=t.lastTok&&"do"!=t.lastTok){if(/[\(\)\[\]{}\\;]/.test(a))return n=a,null
if("-"==a&&e.eat(">"))return"arrow"
if(/[=+\-\/*:\.^%<>~|]/.test(a)){var f=e.eatWhile(/[=+\-\/*:\.^%<>~|]/)
return"."!=a||f||(n="."),"operator"}return null}return n="|",null}function d(e){return e||(e=1),function(t,r){if("}"==t.peek()){if(1==e)return r.tokenize.pop(),r.tokenize[r.tokenize.length-1](t,r)
r.tokenize[r.tokenize.length-1]=d(e-1)}else"{"==t.peek()&&(r.tokenize[r.tokenize.length-1]=d(e+1))
return u(t,r)}}function f(){var e=!1
return function(t,r){return e?(r.tokenize.pop(),r.tokenize[r.tokenize.length-1](t,r)):(e=!0,u(t,r))}}function p(e,t,r,n){return function(i,o){var a,l=!1
for("read-quoted-paused"===o.context.type&&(o.context=o.context.prev,i.eat("}"));null!=(a=i.next());){if(a==e&&(n||!l)){o.tokenize.pop()
break}if(r&&"#"==a&&!l){if(i.eat("{")){"}"==e&&(o.context={prev:o.context,type:"read-quoted-paused"}),o.tokenize.push(d())
break}if(/[@\$]/.test(i.peek())){o.tokenize.push(f())
break}}l=!l&&"\\"==a}return t}}function h(e,t){return e.sol()&&e.match("=end")&&e.eol()&&t.tokenize.pop(),e.skipToEnd(),"comment"}return{startState:function(){return{tokenize:[u],indented:0,context:{type:"top",indented:-t.indentUnit},continuedLine:!1,lastTok:null,varList:!1}},token:function(e,t){n=null,e.sol()&&(t.indented=e.indentation())
var r,l=t.tokenize[t.tokenize.length-1](e,t),s=n
if("ident"==l){var c=e.current()
"keyword"==(l="."==t.lastTok?"property":i.propertyIsEnumerable(e.current())?"keyword":/^[A-Z]/.test(c)?"tag":"def"==t.lastTok||"class"==t.lastTok||t.varList?"def":"variable")&&(s=c,o.propertyIsEnumerable(c)?r="indent":a.propertyIsEnumerable(c)?r="dedent":"if"!=c&&"unless"!=c||e.column()!=e.indentation()?"do"==c&&t.context.indented<t.indented&&(r="indent"):r="indent")}return(n||l&&"comment"!=l)&&(t.lastTok=s),"|"==n&&(t.varList=!t.varList),"indent"==r||/[\(\[\{]/.test(n)?t.context={prev:t.context,type:n||l,indented:t.indented}:("dedent"==r||/[\)\]\}]/.test(n))&&t.context.prev&&(t.context=t.context.prev),e.eol()&&(t.continuedLine="\\"==n||"operator"==l),l},indent:function(r,n){if(r.tokenize[r.tokenize.length-1]!=u)return e.Pass
var i=n&&n.charAt(0),o=r.context,a=o.type==s[i]||"keyword"==o.type&&/^(?:end|until|else|elsif|when|rescue)\b/.test(n)
return o.indented+(a?0:t.indentUnit)+(r.continuedLine?t.indentUnit:0)},electricInput:/^\s*(?:end|rescue|elsif|else|\})$/,lineComment:"#",fold:"indent"}})),e.defineMIME("text/x-ruby","ruby")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror"),require("../../addon/mode/simple")):"function"==typeof define&&define.amd?define(["../../lib/codemirror","../../addon/mode/simple"],e):e(CodeMirror)}((function(e){"use strict"
e.defineSimpleMode("rust",{start:[{regex:/b?"/,token:"string",next:"string"},{regex:/b?r"/,token:"string",next:"string_raw"},{regex:/b?r#+"/,token:"string",next:"string_raw_hash"},{regex:/'(?:[^'\\]|\\(?:[nrt0'"]|x[\da-fA-F]{2}|u\{[\da-fA-F]{6}\}))'/,token:"string-2"},{regex:/b'(?:[^']|\\(?:['\\nrt0]|x[\da-fA-F]{2}))'/,token:"string-2"},{regex:/(?:(?:[0-9][0-9_]*)(?:(?:[Ee][+-]?[0-9_]+)|\.[0-9_]+(?:[Ee][+-]?[0-9_]+)?)(?:f32|f64)?)|(?:0(?:b[01_]+|(?:o[0-7_]+)|(?:x[0-9a-fA-F_]+))|(?:[0-9][0-9_]*))(?:u8|u16|u32|u64|i8|i16|i32|i64|isize|usize)?/,token:"number"},{regex:/(let(?:\s+mut)?|fn|enum|mod|struct|type)(\s+)([a-zA-Z_][a-zA-Z0-9_]*)/,token:["keyword",null,"def"]},{regex:/(?:abstract|alignof|as|box|break|continue|const|crate|do|else|enum|extern|fn|for|final|if|impl|in|loop|macro|match|mod|move|offsetof|override|priv|proc|pub|pure|ref|return|self|sizeof|static|struct|super|trait|type|typeof|unsafe|unsized|use|virtual|where|while|yield)\b/,token:"keyword"},{regex:/\b(?:Self|isize|usize|char|bool|u8|u16|u32|u64|f16|f32|f64|i8|i16|i32|i64|str|Option)\b/,token:"atom"},{regex:/\b(?:true|false|Some|None|Ok|Err)\b/,token:"builtin"},{regex:/\b(fn)(\s+)([a-zA-Z_][a-zA-Z0-9_]*)/,token:["keyword",null,"def"]},{regex:/#!?\[.*\]/,token:"meta"},{regex:/\/\/.*/,token:"comment"},{regex:/\/\*/,token:"comment",next:"comment"},{regex:/[-+\/*=<>!]+/,token:"operator"},{regex:/[a-zA-Z_]\w*!/,token:"variable-3"},{regex:/[a-zA-Z_]\w*/,token:"variable"},{regex:/[\{\[\(]/,indent:!0},{regex:/[\}\]\)]/,dedent:!0}],string:[{regex:/"/,token:"string",next:"start"},{regex:/(?:[^\\"]|\\(?:.|$))*/,token:"string"}],string_raw:[{regex:/"/,token:"string",next:"start"},{regex:/[^"]*/,token:"string"}],string_raw_hash:[{regex:/"#+/,token:"string",next:"start"},{regex:/(?:[^"]|"(?!#))*/,token:"string"}],comment:[{regex:/.*?\*\//,token:"comment",next:"start"},{regex:/.*/,token:"comment"}],meta:{dontIndentStates:["comment"],electricInput:/^\s*\}$/,blockCommentStart:"/*",blockCommentEnd:"*/",lineComment:"//",fold:"brace"}}),e.defineMIME("text/x-rustsrc","rust"),e.defineMIME("text/rust","rust")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
e.defineMode("shell",(function(){var t={}
function r(e,r){for(var n=0;n<r.length;n++)t[r[n]]=e}var n=["true","false"],i=["if","then","do","else","elif","while","until","for","in","esac","fi","fin","fil","done","exit","set","unset","export","function"],o=["ab","awk","bash","beep","cat","cc","cd","chown","chmod","chroot","clear","cp","curl","cut","diff","echo","find","gawk","gcc","get","git","grep","hg","kill","killall","ln","ls","make","mkdir","openssl","mv","nc","nl","node","npm","ping","ps","restart","rm","rmdir","sed","service","sh","shopt","shred","source","sort","sleep","ssh","start","stop","su","sudo","svn","tee","telnet","top","touch","vi","vim","wall","wc","wget","who","write","yes","zsh"]
function a(e,r){if(e.eatSpace())return null
var n=e.sol(),i=e.next()
if("\\"===i)return e.next(),null
if("'"===i||'"'===i||"`"===i)return r.tokens.unshift(l(i,"`"===i?"quote":"string")),u(e,r)
if("#"===i)return n&&e.eat("!")?(e.skipToEnd(),"meta"):(e.skipToEnd(),"comment")
if("$"===i)return r.tokens.unshift(c),u(e,r)
if("+"===i||"="===i)return"operator"
if("-"===i)return e.eat("-"),e.eatWhile(/\w/),"attribute"
if(/\d/.test(i)&&(e.eatWhile(/\d/),e.eol()||!/\w/.test(e.peek())))return"number"
e.eatWhile(/[\w-]/)
var o=e.current()
return"="===e.peek()&&/\w+/.test(o)?"def":t.hasOwnProperty(o)?t[o]:null}function l(e,t){var r="("==e?")":"{"==e?"}":e
return function(n,i){for(var o,a=!1;null!=(o=n.next());){if(o===r&&!a){i.tokens.shift()
break}if("$"===o&&!a&&"'"!==e&&n.peek()!=r){a=!0,n.backUp(1),i.tokens.unshift(c)
break}if(!a&&e!==r&&o===e)return i.tokens.unshift(l(e,t)),u(n,i)
if(!a&&/['"]/.test(o)&&!/['"]/.test(e)){i.tokens.unshift(s(o,"string")),n.backUp(1)
break}a=!a&&"\\"===o}return t}}function s(e,t){return function(r,n){return n.tokens[0]=l(e,t),r.next(),u(r,n)}}e.registerHelper("hintWords","shell",n.concat(i,o)),r("atom",n),r("keyword",i),r("builtin",o)
var c=function(e,t){t.tokens.length>1&&e.eat("$")
var r=e.next()
return/['"({]/.test(r)?(t.tokens[0]=l(r,"("==r?"quote":"{"==r?"def":"string"),u(e,t)):(/\d/.test(r)||e.eatWhile(/\w/),t.tokens.shift(),"def")}
function u(e,t){return(t.tokens[0]||a)(e,t)}return{startState:function(){return{tokens:[]}},token:function(e,t){return u(e,t)},closeBrackets:"()[]{}''\"\"``",lineComment:"#",fold:"brace"}})),e.defineMIME("text/x-sh","shell"),e.defineMIME("application/x-sh","shell")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
function t(e){for(var t;null!=(t=e.next());)if("`"==t&&!e.eat("`"))return"variable-2"
return e.backUp(e.current().length-1),e.eatWhile(/\w/)?"variable-2":null}function r(e){return e.eat("@")&&(e.match(/^session\./),e.match(/^local\./),e.match(/^global\./)),e.eat("'")?(e.match(/^.*'/),"variable-2"):e.eat('"')?(e.match(/^.*"/),"variable-2"):e.eat("`")?(e.match(/^.*`/),"variable-2"):e.match(/^[0-9a-zA-Z$\.\_]+/)?"variable-2":null}function n(e){return e.eat("N")?"atom":e.match(/^[a-zA-Z.#!?]/)?"variable-2":null}e.defineMode("sql",(function(t,r){var n=r.client||{},l=r.atoms||{false:!0,true:!0,null:!0},s=r.builtin||o(a),c=r.keywords||o(i),u=r.operatorChars||/^[*+\-%<>!=&|~^\/]/,d=r.support||{},f=r.hooks||{},p=r.dateSQL||{date:!0,time:!0,timestamp:!0},h=!1!==r.backslashStringEscapes,m=r.brackets||/^[\{}\(\)\[\]]/,g=r.punctuation||/^[;.,:]/
function v(e,t){var r=e.next()
if(f[r]){var i=f[r](e,t)
if(!1!==i)return i}if(d.hexNumber&&("0"==r&&e.match(/^[xX][0-9a-fA-F]+/)||("x"==r||"X"==r)&&e.match(/^'[0-9a-fA-F]+'/)))return"number"
if(d.binaryNumber&&(("b"==r||"B"==r)&&e.match(/^'[01]+'/)||"0"==r&&e.match(/^b[01]+/)))return"number"
if(r.charCodeAt(0)>47&&r.charCodeAt(0)<58)return e.match(/^[0-9]*(\.[0-9]+)?([eE][-+]?[0-9]+)?/),d.decimallessFloat&&e.match(/^\.(?!\.)/),"number"
if("?"==r&&(e.eatSpace()||e.eol()||e.eat(";")))return"variable-3"
if("'"==r||'"'==r&&d.doubleQuote)return t.tokenize=y(r),t.tokenize(e,t)
if((d.nCharCast&&("n"==r||"N"==r)||d.charsetCast&&"_"==r&&e.match(/[a-z][a-z0-9]*/i))&&("'"==e.peek()||'"'==e.peek()))return"keyword"
if(d.escapeConstant&&("e"==r||"E"==r)&&("'"==e.peek()||'"'==e.peek()&&d.doubleQuote))return t.tokenize=function(e,t){return(t.tokenize=y(e.next(),!0))(e,t)},"keyword"
if(d.commentSlashSlash&&"/"==r&&e.eat("/"))return e.skipToEnd(),"comment"
if(d.commentHash&&"#"==r||"-"==r&&e.eat("-")&&(!d.commentSpaceRequired||e.eat(" ")))return e.skipToEnd(),"comment"
if("/"==r&&e.eat("*"))return t.tokenize=b(1),t.tokenize(e,t)
if("."!=r){if(u.test(r))return e.eatWhile(u),"operator"
if(m.test(r))return"bracket"
if(g.test(r))return e.eatWhile(g),"punctuation"
if("{"==r&&(e.match(/^( )*(d|D|t|T|ts|TS)( )*'[^']*'( )*}/)||e.match(/^( )*(d|D|t|T|ts|TS)( )*"[^"]*"( )*}/)))return"number"
e.eatWhile(/^[_\w\d]/)
var o=e.current().toLowerCase()
return p.hasOwnProperty(o)&&(e.match(/^( )+'[^']*'/)||e.match(/^( )+"[^"]*"/))?"number":l.hasOwnProperty(o)?"atom":s.hasOwnProperty(o)?"builtin":c.hasOwnProperty(o)?"keyword":n.hasOwnProperty(o)?"string-2":null}return d.zerolessFloat&&e.match(/^(?:\d+(?:e[+-]?\d+)?)/i)?"number":e.match(/^\.+/)?null:d.ODBCdotTable&&e.match(/^[\w\d_]+/)?"variable-2":void 0}function y(e,t){return function(r,n){for(var i,o=!1;null!=(i=r.next());){if(i==e&&!o){n.tokenize=v
break}o=(h||t)&&!o&&"\\"==i}return"string"}}function b(e){return function(t,r){var n=t.match(/^.*?(\/\*|\*\/)/)
return n?"/*"==n[1]?r.tokenize=b(e+1):r.tokenize=e>1?b(e-1):v:t.skipToEnd(),"comment"}}function x(e,t,r){t.context={prev:t.context,indent:e.indentation(),col:e.column(),type:r}}return{startState:function(){return{tokenize:v,context:null}},token:function(e,t){if(e.sol()&&t.context&&null==t.context.align&&(t.context.align=!1),t.tokenize==v&&e.eatSpace())return null
var r=t.tokenize(e,t)
if("comment"==r)return r
t.context&&null==t.context.align&&(t.context.align=!0)
var n=e.current()
return"("==n?x(e,t,")"):"["==n?x(e,t,"]"):t.context&&t.context.type==n&&function(e){e.indent=e.context.indent,e.context=e.context.prev}(t),r},indent:function(r,n){var i=r.context
if(!i)return e.Pass
var o=n.charAt(0)==i.type
return i.align?i.col+(o?0:1):i.indent+(o?0:t.indentUnit)},blockCommentStart:"/*",blockCommentEnd:"*/",lineComment:d.commentSlashSlash?"//":d.commentHash?"#":"--",closeBrackets:"()[]{}''\"\"``"}}))
var i="alter and as asc between by count create delete desc distinct drop from group having in insert into is join like not on or order select set table union update values where limit "
function o(e){for(var t={},r=e.split(" "),n=0;n<r.length;++n)t[r[n]]=!0
return t}var a="bool boolean bit blob enum long longblob longtext medium mediumblob mediumint mediumtext time timestamp tinyblob tinyint tinytext text bigint int int1 int2 int3 int4 int8 integer float float4 float8 double char varbinary varchar varcharacter precision real date datetime year unsigned signed decimal numeric"
e.defineMIME("text/x-sql",{name:"sql",keywords:o(i+"begin"),builtin:o(a),atoms:o("false true null unknown"),dateSQL:o("date time timestamp"),support:o("ODBCdotTable doubleQuote binaryNumber hexNumber")}),e.defineMIME("text/x-mssql",{name:"sql",client:o("$partition binary_checksum checksum connectionproperty context_info current_request_id error_line error_message error_number error_procedure error_severity error_state formatmessage get_filestream_transaction_context getansinull host_id host_name isnull isnumeric min_active_rowversion newid newsequentialid rowcount_big xact_state object_id"),keywords:o(i+"begin trigger proc view index for add constraint key primary foreign collate clustered nonclustered declare exec go if use index holdlock nolock nowait paglock readcommitted readcommittedlock readpast readuncommitted repeatableread rowlock serializable snapshot tablock tablockx updlock with"),builtin:o("bigint numeric bit smallint decimal smallmoney int tinyint money float real char varchar text nchar nvarchar ntext binary varbinary image cursor timestamp hierarchyid uniqueidentifier sql_variant xml table "),atoms:o("is not null like and or in left right between inner outer join all any some cross unpivot pivot exists"),operatorChars:/^[*+\-%<>!=^\&|\/]/,brackets:/^[\{}\(\)]/,punctuation:/^[;.,:/]/,backslashStringEscapes:!1,dateSQL:o("date datetimeoffset datetime2 smalldatetime datetime time"),hooks:{"@":r}}),e.defineMIME("text/x-mysql",{name:"sql",client:o("charset clear connect edit ego exit go help nopager notee nowarning pager print prompt quit rehash source status system tee"),keywords:o(i+"accessible action add after algorithm all analyze asensitive at authors auto_increment autocommit avg avg_row_length before binary binlog both btree cache call cascade cascaded case catalog_name chain change changed character check checkpoint checksum class_origin client_statistics close coalesce code collate collation collations column columns comment commit committed completion concurrent condition connection consistent constraint contains continue contributors convert cross current current_date current_time current_timestamp current_user cursor data database databases day_hour day_microsecond day_minute day_second deallocate dec declare default delay_key_write delayed delimiter des_key_file describe deterministic dev_pop dev_samp deviance diagnostics directory disable discard distinctrow div dual dumpfile each elseif enable enclosed end ends engine engines enum errors escape escaped even event events every execute exists exit explain extended fast fetch field fields first flush for force foreign found_rows full fulltext function general get global grant grants group group_concat handler hash help high_priority hosts hour_microsecond hour_minute hour_second if ignore ignore_server_ids import index index_statistics infile inner innodb inout insensitive insert_method install interval invoker isolation iterate key keys kill language last leading leave left level limit linear lines list load local localtime localtimestamp lock logs low_priority master master_heartbeat_period master_ssl_verify_server_cert masters match max max_rows maxvalue message_text middleint migrate min min_rows minute_microsecond minute_second mod mode modifies modify mutex mysql_errno natural next no no_write_to_binlog offline offset one online open optimize option optionally out outer outfile pack_keys parser partition partitions password phase plugin plugins prepare preserve prev primary privileges procedure processlist profile profiles purge query quick range read read_write reads real rebuild recover references regexp relaylog release remove rename reorganize repair repeatable replace require resignal restrict resume return returns revoke right rlike rollback rollup row row_format rtree savepoint schedule schema schema_name schemas second_microsecond security sensitive separator serializable server session share show signal slave slow smallint snapshot soname spatial specific sql sql_big_result sql_buffer_result sql_cache sql_calc_found_rows sql_no_cache sql_small_result sqlexception sqlstate sqlwarning ssl start starting starts status std stddev stddev_pop stddev_samp storage straight_join subclass_origin sum suspend table_name table_statistics tables tablespace temporary terminated to trailing transaction trigger triggers truncate uncommitted undo uninstall unique unlock upgrade usage use use_frm user user_resources user_statistics using utc_date utc_time utc_timestamp value variables varying view views warnings when while with work write xa xor year_month zerofill begin do then else loop repeat"),builtin:o("bool boolean bit blob decimal double float long longblob longtext medium mediumblob mediumint mediumtext time timestamp tinyblob tinyint tinytext text bigint int int1 int2 int3 int4 int8 integer float float4 float8 double char varbinary varchar varcharacter precision date datetime year unsigned signed numeric"),atoms:o("false true null unknown"),operatorChars:/^[*+\-%<>!=&|^]/,dateSQL:o("date time timestamp"),support:o("ODBCdotTable decimallessFloat zerolessFloat binaryNumber hexNumber doubleQuote nCharCast charsetCast commentHash commentSpaceRequired"),hooks:{"@":r,"`":t,"\\":n}}),e.defineMIME("text/x-mariadb",{name:"sql",client:o("charset clear connect edit ego exit go help nopager notee nowarning pager print prompt quit rehash source status system tee"),keywords:o(i+"accessible action add after algorithm all always analyze asensitive at authors auto_increment autocommit avg avg_row_length before binary binlog both btree cache call cascade cascaded case catalog_name chain change changed character check checkpoint checksum class_origin client_statistics close coalesce code collate collation collations column columns comment commit committed completion concurrent condition connection consistent constraint contains continue contributors convert cross current current_date current_time current_timestamp current_user cursor data database databases day_hour day_microsecond day_minute day_second deallocate dec declare default delay_key_write delayed delimiter des_key_file describe deterministic dev_pop dev_samp deviance diagnostics directory disable discard distinctrow div dual dumpfile each elseif enable enclosed end ends engine engines enum errors escape escaped even event events every execute exists exit explain extended fast fetch field fields first flush for force foreign found_rows full fulltext function general generated get global grant grants group groupby_concat handler hard hash help high_priority hosts hour_microsecond hour_minute hour_second if ignore ignore_server_ids import index index_statistics infile inner innodb inout insensitive insert_method install interval invoker isolation iterate key keys kill language last leading leave left level limit linear lines list load local localtime localtimestamp lock logs low_priority master master_heartbeat_period master_ssl_verify_server_cert masters match max max_rows maxvalue message_text middleint migrate min min_rows minute_microsecond minute_second mod mode modifies modify mutex mysql_errno natural next no no_write_to_binlog offline offset one online open optimize option optionally out outer outfile pack_keys parser partition partitions password persistent phase plugin plugins prepare preserve prev primary privileges procedure processlist profile profiles purge query quick range read read_write reads real rebuild recover references regexp relaylog release remove rename reorganize repair repeatable replace require resignal restrict resume return returns revoke right rlike rollback rollup row row_format rtree savepoint schedule schema schema_name schemas second_microsecond security sensitive separator serializable server session share show shutdown signal slave slow smallint snapshot soft soname spatial specific sql sql_big_result sql_buffer_result sql_cache sql_calc_found_rows sql_no_cache sql_small_result sqlexception sqlstate sqlwarning ssl start starting starts status std stddev stddev_pop stddev_samp storage straight_join subclass_origin sum suspend table_name table_statistics tables tablespace temporary terminated to trailing transaction trigger triggers truncate uncommitted undo uninstall unique unlock upgrade usage use use_frm user user_resources user_statistics using utc_date utc_time utc_timestamp value variables varying view views virtual warnings when while with work write xa xor year_month zerofill begin do then else loop repeat"),builtin:o("bool boolean bit blob decimal double float long longblob longtext medium mediumblob mediumint mediumtext time timestamp tinyblob tinyint tinytext text bigint int int1 int2 int3 int4 int8 integer float float4 float8 double char varbinary varchar varcharacter precision date datetime year unsigned signed numeric"),atoms:o("false true null unknown"),operatorChars:/^[*+\-%<>!=&|^]/,dateSQL:o("date time timestamp"),support:o("ODBCdotTable decimallessFloat zerolessFloat binaryNumber hexNumber doubleQuote nCharCast charsetCast commentHash commentSpaceRequired"),hooks:{"@":r,"`":t,"\\":n}}),e.defineMIME("text/x-sqlite",{name:"sql",client:o("auth backup bail binary changes check clone databases dbinfo dump echo eqp exit explain fullschema headers help import imposter indexes iotrace limit lint load log mode nullvalue once open output print prompt quit read restore save scanstats schema separator session shell show stats system tables testcase timeout timer trace vfsinfo vfslist vfsname width"),keywords:o(i+"abort action add after all analyze attach autoincrement before begin cascade case cast check collate column commit conflict constraint cross current_date current_time current_timestamp database default deferrable deferred detach each else end escape except exclusive exists explain fail for foreign full glob if ignore immediate index indexed initially inner instead intersect isnull key left limit match natural no notnull null of offset outer plan pragma primary query raise recursive references regexp reindex release rename replace restrict right rollback row savepoint temp temporary then to transaction trigger unique using vacuum view virtual when with without"),builtin:o("bool boolean bit blob decimal double float long longblob longtext medium mediumblob mediumint mediumtext time timestamp tinyblob tinyint tinytext text clob bigint int int2 int8 integer float double char varchar date datetime year unsigned signed numeric real"),atoms:o("null current_date current_time current_timestamp"),operatorChars:/^[*+\-%<>!=&|/~]/,dateSQL:o("date time timestamp datetime"),support:o("decimallessFloat zerolessFloat"),identifierQuote:'"',hooks:{"@":r,":":r,"?":r,$:r,'"':function(e){for(var t;null!=(t=e.next());)if('"'==t&&!e.eat('"'))return"variable-2"
return e.backUp(e.current().length-1),e.eatWhile(/\w/)?"variable-2":null},"`":t}}),e.defineMIME("text/x-cassandra",{name:"sql",client:{},keywords:o("add all allow alter and any apply as asc authorize batch begin by clustering columnfamily compact consistency count create custom delete desc distinct drop each_quorum exists filtering from grant if in index insert into key keyspace keyspaces level limit local_one local_quorum modify nan norecursive nosuperuser not of on one order password permission permissions primary quorum rename revoke schema select set storage superuser table three to token truncate ttl two type unlogged update use user users using values where with writetime"),builtin:o("ascii bigint blob boolean counter decimal double float frozen inet int list map static text timestamp timeuuid tuple uuid varchar varint"),atoms:o("false true infinity NaN"),operatorChars:/^[<>=]/,dateSQL:{},support:o("commentSlashSlash decimallessFloat"),hooks:{}}),e.defineMIME("text/x-plsql",{name:"sql",client:o("appinfo arraysize autocommit autoprint autorecovery autotrace blockterminator break btitle cmdsep colsep compatibility compute concat copycommit copytypecheck define describe echo editfile embedded escape exec execute feedback flagger flush heading headsep instance linesize lno loboffset logsource long longchunksize markup native newpage numformat numwidth pagesize pause pno recsep recsepchar release repfooter repheader serveroutput shiftinout show showmode size spool sqlblanklines sqlcase sqlcode sqlcontinue sqlnumber sqlpluscompatibility sqlprefix sqlprompt sqlterminator suffix tab term termout time timing trimout trimspool ttitle underline verify version wrap"),keywords:o("abort accept access add all alter and any array arraylen as asc assert assign at attributes audit authorization avg base_table begin between binary_integer body boolean by case cast char char_base check close cluster clusters colauth column comment commit compress connect connected constant constraint crash create current currval cursor data_base database date dba deallocate debugoff debugon decimal declare default definition delay delete desc digits dispose distinct do drop else elseif elsif enable end entry escape exception exception_init exchange exclusive exists exit external fast fetch file for force form from function generic goto grant group having identified if immediate in increment index indexes indicator initial initrans insert interface intersect into is key level library like limited local lock log logging long loop master maxextents maxtrans member minextents minus mislabel mode modify multiset new next no noaudit nocompress nologging noparallel not nowait number_base object of off offline on online only open option or order out package parallel partition pctfree pctincrease pctused pls_integer positive positiven pragma primary prior private privileges procedure public raise range raw read rebuild record ref references refresh release rename replace resource restrict return returning returns reverse revoke rollback row rowid rowlabel rownum rows run savepoint schema segment select separate session set share snapshot some space split sql start statement storage subtype successful synonym tabauth table tables tablespace task terminate then to trigger truncate type union unique unlimited unrecoverable unusable update use using validate value values variable view views when whenever where while with work"),builtin:o("abs acos add_months ascii asin atan atan2 average bfile bfilename bigserial bit blob ceil character chartorowid chr clob concat convert cos cosh count dec decode deref dual dump dup_val_on_index empty error exp false float floor found glb greatest hextoraw initcap instr instrb int integer isopen last_day least length lengthb ln lower lpad ltrim lub make_ref max min mlslabel mod months_between natural naturaln nchar nclob new_time next_day nextval nls_charset_decl_len nls_charset_id nls_charset_name nls_initcap nls_lower nls_sort nls_upper nlssort no_data_found notfound null number numeric nvarchar2 nvl others power rawtohex real reftohex round rowcount rowidtochar rowtype rpad rtrim serial sign signtype sin sinh smallint soundex sqlcode sqlerrm sqrt stddev string substr substrb sum sysdate tan tanh to_char text to_date to_label to_multi_byte to_number to_single_byte translate true trunc uid unlogged upper user userenv varchar varchar2 variance varying vsize xml"),operatorChars:/^[*\/+\-%<>!=~]/,dateSQL:o("date time timestamp"),support:o("doubleQuote nCharCast zerolessFloat binaryNumber hexNumber")}),e.defineMIME("text/x-hive",{name:"sql",keywords:o("select alter $elem$ $key$ $value$ add after all analyze and archive as asc before between binary both bucket buckets by cascade case cast change cluster clustered clusterstatus collection column columns comment compute concatenate continue create cross cursor data database databases dbproperties deferred delete delimited desc describe directory disable distinct distribute drop else enable end escaped exclusive exists explain export extended external fetch fields fileformat first format formatted from full function functions grant group having hold_ddltime idxproperties if import in index indexes inpath inputdriver inputformat insert intersect into is items join keys lateral left like limit lines load local location lock locks mapjoin materialized minus msck no_drop nocompress not of offline on option or order out outer outputdriver outputformat overwrite partition partitioned partitions percent plus preserve procedure purge range rcfile read readonly reads rebuild recordreader recordwriter recover reduce regexp rename repair replace restrict revoke right rlike row schema schemas semi sequencefile serde serdeproperties set shared show show_database sort sorted ssl statistics stored streamtable table tables tablesample tblproperties temporary terminated textfile then tmp to touch transform trigger unarchive undo union uniquejoin unlock update use using utc utc_tmestamp view when where while with admin authorization char compact compactions conf cube current current_date current_timestamp day decimal defined dependency directories elem_type exchange file following for grouping hour ignore inner interval jar less logical macro minute month more none noscan over owner partialscan preceding pretty principals protection reload rewrite role roles rollup rows second server sets skewed transactions truncate unbounded unset uri user values window year"),builtin:o("bool boolean long timestamp tinyint smallint bigint int float double date datetime unsigned string array struct map uniontype key_type utctimestamp value_type varchar"),atoms:o("false true null unknown"),operatorChars:/^[*+\-%<>!=]/,dateSQL:o("date timestamp"),support:o("ODBCdotTable doubleQuote binaryNumber hexNumber")}),e.defineMIME("text/x-pgsql",{name:"sql",client:o("source"),keywords:o(i+"a abort abs absent absolute access according action ada add admin after aggregate alias all allocate also alter always analyse analyze and any are array array_agg array_max_cardinality as asc asensitive assert assertion assignment asymmetric at atomic attach attribute attributes authorization avg backward base64 before begin begin_frame begin_partition bernoulli between bigint binary bit bit_length blob blocked bom boolean both breadth by c cache call called cardinality cascade cascaded case cast catalog catalog_name ceil ceiling chain char char_length character character_length character_set_catalog character_set_name character_set_schema characteristics characters check checkpoint class class_origin clob close cluster coalesce cobol collate collation collation_catalog collation_name collation_schema collect column column_name columns command_function command_function_code comment comments commit committed concurrently condition condition_number configuration conflict connect connection connection_name constant constraint constraint_catalog constraint_name constraint_schema constraints constructor contains content continue control conversion convert copy corr corresponding cost count covar_pop covar_samp create cross csv cube cume_dist current current_catalog current_date current_default_transform_group current_path current_role current_row current_schema current_time current_timestamp current_transform_group_for_type current_user cursor cursor_name cycle data database datalink datatype date datetime_interval_code datetime_interval_precision day db deallocate debug dec decimal declare default defaults deferrable deferred defined definer degree delete delimiter delimiters dense_rank depends depth deref derived desc describe descriptor detach detail deterministic diagnostics dictionary disable discard disconnect dispatch distinct dlnewcopy dlpreviouscopy dlurlcomplete dlurlcompleteonly dlurlcompletewrite dlurlpath dlurlpathonly dlurlpathwrite dlurlscheme dlurlserver dlvalue do document domain double drop dump dynamic dynamic_function dynamic_function_code each element else elseif elsif empty enable encoding encrypted end end_frame end_partition endexec enforced enum equals errcode error escape event every except exception exclude excluding exclusive exec execute exists exit exp explain expression extension external extract false family fetch file filter final first first_value flag float floor following for force foreach foreign fortran forward found frame_row free freeze from fs full function functions fusion g general generated get global go goto grant granted greatest group grouping groups handler having header hex hierarchy hint hold hour id identity if ignore ilike immediate immediately immutable implementation implicit import in include including increment indent index indexes indicator info inherit inherits initially inline inner inout input insensitive insert instance instantiable instead int integer integrity intersect intersection interval into invoker is isnull isolation join k key key_member key_type label lag language large last last_value lateral lead leading leakproof least left length level library like like_regex limit link listen ln load local localtime localtimestamp location locator lock locked log logged loop lower m map mapping match matched materialized max max_cardinality maxvalue member merge message message_length message_octet_length message_text method min minute minvalue mod mode modifies module month more move multiset mumps name names namespace national natural nchar nclob nesting new next nfc nfd nfkc nfkd nil no none normalize normalized not nothing notice notify notnull nowait nth_value ntile null nullable nullif nulls number numeric object occurrences_regex octet_length octets of off offset oids old on only open operator option options or order ordering ordinality others out outer output over overlaps overlay overriding owned owner p pad parallel parameter parameter_mode parameter_name parameter_ordinal_position parameter_specific_catalog parameter_specific_name parameter_specific_schema parser partial partition pascal passing passthrough password path percent percent_rank percentile_cont percentile_disc perform period permission pg_context pg_datatype_name pg_exception_context pg_exception_detail pg_exception_hint placing plans pli policy portion position position_regex power precedes preceding precision prepare prepared preserve primary print_strict_params prior privileges procedural procedure procedures program public publication query quote raise range rank read reads real reassign recheck recovery recursive ref references referencing refresh regr_avgx regr_avgy regr_count regr_intercept regr_r2 regr_slope regr_sxx regr_sxy regr_syy reindex relative release rename repeatable replace replica requiring reset respect restart restore restrict result result_oid return returned_cardinality returned_length returned_octet_length returned_sqlstate returning returns reverse revoke right role rollback rollup routine routine_catalog routine_name routine_schema routines row row_count row_number rows rowtype rule savepoint scale schema schema_name schemas scope scope_catalog scope_name scope_schema scroll search second section security select selective self sensitive sequence sequences serializable server server_name session session_user set setof sets share show similar simple size skip slice smallint snapshot some source space specific specific_name specifictype sql sqlcode sqlerror sqlexception sqlstate sqlwarning sqrt stable stacked standalone start state statement static statistics stddev_pop stddev_samp stdin stdout storage strict strip structure style subclass_origin submultiset subscription substring substring_regex succeeds sum symmetric sysid system system_time system_user t table table_name tables tablesample tablespace temp template temporary text then ties time timestamp timezone_hour timezone_minute to token top_level_count trailing transaction transaction_active transactions_committed transactions_rolled_back transform transforms translate translate_regex translation treat trigger trigger_catalog trigger_name trigger_schema trim trim_array true truncate trusted type types uescape unbounded uncommitted under unencrypted union unique unknown unlink unlisten unlogged unnamed unnest until untyped update upper uri usage use_column use_variable user user_defined_type_catalog user_defined_type_code user_defined_type_name user_defined_type_schema using vacuum valid validate validator value value_of values var_pop var_samp varbinary varchar variable_conflict variadic varying verbose version versioning view views volatile warning when whenever where while whitespace width_bucket window with within without work wrapper write xml xmlagg xmlattributes xmlbinary xmlcast xmlcomment xmlconcat xmldeclaration xmldocument xmlelement xmlexists xmlforest xmliterate xmlnamespaces xmlparse xmlpi xmlquery xmlroot xmlschema xmlserialize xmltable xmltext xmlvalidate year yes zone"),builtin:o("bigint int8 bigserial serial8 bit varying varbit boolean bool box bytea character char varchar cidr circle date double precision float8 inet integer int int4 interval json jsonb line lseg macaddr macaddr8 money numeric decimal path pg_lsn point polygon real float4 smallint int2 smallserial serial2 serial serial4 text time without zone with timetz timestamp timestamptz tsquery tsvector txid_snapshot uuid xml"),atoms:o("false true null unknown"),operatorChars:/^[*\/+\-%<>!=&|^\/#@?~]/,backslashStringEscapes:!1,dateSQL:o("date time timestamp"),support:o("ODBCdotTable decimallessFloat zerolessFloat binaryNumber hexNumber nCharCast charsetCast escapeConstant")}),e.defineMIME("text/x-gql",{name:"sql",keywords:o("ancestor and asc by contains desc descendant distinct from group has in is limit offset on order select superset where"),atoms:o("false true"),builtin:o("blob datetime first key __key__ string integer double boolean null"),operatorChars:/^[*+\-%<>!=]/}),e.defineMIME("text/x-gpsql",{name:"sql",client:o("source"),keywords:o("abort absolute access action active add admin after aggregate all also alter always analyse analyze and any array as asc assertion assignment asymmetric at authorization backward before begin between bigint binary bit boolean both by cache called cascade cascaded case cast chain char character characteristics check checkpoint class close cluster coalesce codegen collate column comment commit committed concurrency concurrently configuration connection constraint constraints contains content continue conversion copy cost cpu_rate_limit create createdb createexttable createrole createuser cross csv cube current current_catalog current_date current_role current_schema current_time current_timestamp current_user cursor cycle data database day deallocate dec decimal declare decode default defaults deferrable deferred definer delete delimiter delimiters deny desc dictionary disable discard distinct distributed do document domain double drop dxl each else enable encoding encrypted end enum errors escape every except exchange exclude excluding exclusive execute exists explain extension external extract false family fetch fields filespace fill filter first float following for force foreign format forward freeze from full function global grant granted greatest group group_id grouping handler hash having header hold host hour identity if ignore ilike immediate immutable implicit in including inclusive increment index indexes inherit inherits initially inline inner inout input insensitive insert instead int integer intersect interval into invoker is isnull isolation join key language large last leading least left level like limit list listen load local localtime localtimestamp location lock log login mapping master match maxvalue median merge minute minvalue missing mode modifies modify month move name names national natural nchar new newline next no nocreatedb nocreateexttable nocreaterole nocreateuser noinherit nologin none noovercommit nosuperuser not nothing notify notnull nowait null nullif nulls numeric object of off offset oids old on only operator option options or order ordered others out outer over overcommit overlaps overlay owned owner parser partial partition partitions passing password percent percentile_cont percentile_disc placing plans position preceding precision prepare prepared preserve primary prior privileges procedural procedure protocol queue quote randomly range read readable reads real reassign recheck recursive ref references reindex reject relative release rename repeatable replace replica reset resource restart restrict returning returns revoke right role rollback rollup rootpartition row rows rule savepoint scatter schema scroll search second security segment select sequence serializable session session_user set setof sets share show similar simple smallint some split sql stable standalone start statement statistics stdin stdout storage strict strip subpartition subpartitions substring superuser symmetric sysid system table tablespace temp template temporary text then threshold ties time timestamp to trailing transaction treat trigger trim true truncate trusted type unbounded uncommitted unencrypted union unique unknown unlisten until update user using vacuum valid validation validator value values varchar variadic varying verbose version view volatile web when where whitespace window with within without work writable write xml xmlattributes xmlconcat xmlelement xmlexists xmlforest xmlparse xmlpi xmlroot xmlserialize year yes zone"),builtin:o("bigint int8 bigserial serial8 bit varying varbit boolean bool box bytea character char varchar cidr circle date double precision float float8 inet integer int int4 interval json jsonb line lseg macaddr macaddr8 money numeric decimal path pg_lsn point polygon real float4 smallint int2 smallserial serial2 serial serial4 text time without zone with timetz timestamp timestamptz tsquery tsvector txid_snapshot uuid xml"),atoms:o("false true null unknown"),operatorChars:/^[*+\-%<>!=&|^\/#@?~]/,dateSQL:o("date time timestamp"),support:o("ODBCdotTable decimallessFloat zerolessFloat binaryNumber hexNumber nCharCast charsetCast")}),e.defineMIME("text/x-sparksql",{name:"sql",keywords:o("add after all alter analyze and anti archive array as asc at between bucket buckets by cache cascade case cast change clear cluster clustered codegen collection column columns comment commit compact compactions compute concatenate cost create cross cube current current_date current_timestamp database databases datata dbproperties defined delete delimited deny desc describe dfs directories distinct distribute drop else end escaped except exchange exists explain export extended external false fields fileformat first following for format formatted from full function functions global grant group grouping having if ignore import in index indexes inner inpath inputformat insert intersect interval into is items join keys last lateral lazy left like limit lines list load local location lock locks logical macro map minus msck natural no not null nulls of on optimize option options or order out outer outputformat over overwrite partition partitioned partitions percent preceding principals purge range recordreader recordwriter recover reduce refresh regexp rename repair replace reset restrict revoke right rlike role roles rollback rollup row rows schema schemas select semi separated serde serdeproperties set sets show skewed sort sorted start statistics stored stratify struct table tables tablesample tblproperties temp temporary terminated then to touch transaction transactions transform true truncate unarchive unbounded uncache union unlock unset use using values view when where window with"),builtin:o("tinyint smallint int bigint boolean float double string binary timestamp decimal array map struct uniontype delimited serde sequencefile textfile rcfile inputformat outputformat"),atoms:o("false true null"),operatorChars:/^[*\/+\-%<>!=~&|^]/,dateSQL:o("date time timestamp"),support:o("ODBCdotTable doubleQuote zerolessFloat")}),e.defineMIME("text/x-esper",{name:"sql",client:o("source"),keywords:o("alter and as asc between by count create delete desc distinct drop from group having in insert into is join like not on or order select set table union update values where limit after all and as at asc avedev avg between by case cast coalesce count create current_timestamp day days delete define desc distinct else end escape events every exists false first from full group having hour hours in inner insert instanceof into irstream is istream join last lastweekday left limit like max match_recognize matches median measures metadatasql min minute minutes msec millisecond milliseconds not null offset on or order outer output partition pattern prev prior regexp retain-union retain-intersection right rstream sec second seconds select set some snapshot sql stddev sum then true unidirectional until update variable weekday when where window"),builtin:{},atoms:o("false true null"),operatorChars:/^[*+\-%<>!=&|^\/#@?~]/,dateSQL:o("time"),support:o("decimallessFloat zerolessFloat binaryNumber hexNumber")})})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
function t(e){for(var t={},r=0;r<e.length;r++)t[e[r]]=!0
return t}var r=t(["_","var","let","class","enum","extension","import","protocol","struct","func","typealias","associatedtype","open","public","internal","fileprivate","private","deinit","init","new","override","self","subscript","super","convenience","dynamic","final","indirect","lazy","required","static","unowned","unowned(safe)","unowned(unsafe)","weak","as","is","break","case","continue","default","else","fallthrough","for","guard","if","in","repeat","switch","where","while","defer","return","inout","mutating","nonmutating","catch","do","rethrows","throw","throws","try","didSet","get","set","willSet","assignment","associativity","infix","left","none","operator","postfix","precedence","precedencegroup","prefix","right","Any","AnyObject","Type","dynamicType","Self","Protocol","__COLUMN__","__FILE__","__FUNCTION__","__LINE__"]),n=t(["var","let","class","enum","extension","import","protocol","struct","func","typealias","associatedtype","for"]),i=t(["true","false","nil","self","super","_"]),o=t(["Array","Bool","Character","Dictionary","Double","Float","Int","Int8","Int16","Int32","Int64","Never","Optional","Set","String","UInt8","UInt16","UInt32","UInt64","Void"]),a=/^\-?0b[01][01_]*/,l=/^\-?0o[0-7][0-7_]*/,s=/^\-?0x[\dA-Fa-f][\dA-Fa-f_]*(?:(?:\.[\dA-Fa-f][\dA-Fa-f_]*)?[Pp]\-?\d[\d_]*)?/,c=/^\-?\d[\d_]*(?:\.\d[\d_]*)?(?:[Ee]\-?\d[\d_]*)?/,u=/^\$\d+|(`?)[_A-Za-z][_A-Za-z$0-9]*\1/,d=/^\.(?:\$\d+|(`?)[_A-Za-z][_A-Za-z$0-9]*\1)/,f=/^\#[A-Za-z]+/,p=/^@(?:\$\d+|(`?)[_A-Za-z][_A-Za-z$0-9]*\1)/
function h(e,t,h){if(e.sol()&&(t.indented=e.indentation()),e.eatSpace())return null
var m,y=e.peek()
if("/"==y){if(e.match("//"))return e.skipToEnd(),"comment"
if(e.match("/*"))return t.tokenize.push(v),v(e,t)}if(e.match(f))return"builtin"
if(e.match(p))return"attribute"
if(e.match(a))return"number"
if(e.match(l))return"number"
if(e.match(s))return"number"
if(e.match(c))return"number"
if(e.match(d))return"property"
if("+-/*%=|&<>~^?!".indexOf(y)>-1)return e.next(),"operator"
if(":;,.(){}[]".indexOf(y)>-1)return e.next(),e.match(".."),"punctuation"
if(m=e.match(/("""|"|')/)){var b=g.bind(null,m[0])
return t.tokenize.push(b),b(e,t)}if(e.match(u)){var x=e.current()
return o.hasOwnProperty(x)?"variable-2":i.hasOwnProperty(x)?"atom":r.hasOwnProperty(x)?(n.hasOwnProperty(x)&&(t.prev="define"),"keyword"):"define"==h?"def":"variable"}return e.next(),null}function m(){var e=0
return function(t,r,n){var i=h(t,r,n)
if("punctuation"==i)if("("==t.current())++e
else if(")"==t.current()){if(0==e)return t.backUp(1),r.tokenize.pop(),r.tokenize[r.tokenize.length-1](t,r);--e}return i}}function g(e,t,r){for(var n,i=1==e.length,o=!1;n=t.peek();)if(o){if(t.next(),"("==n)return r.tokenize.push(m()),"string"
o=!1}else{if(t.match(e))return r.tokenize.pop(),"string"
t.next(),o="\\"==n}return i&&r.tokenize.pop(),"string"}function v(e,t){for(var r;e.match(/^[^/*]+/,!0),r=e.next();)"/"===r&&e.eat("*")?t.tokenize.push(v):"*"===r&&e.eat("/")&&t.tokenize.pop()
return"comment"}function y(e,t,r){this.prev=e,this.align=t,this.indented=r}function b(e,t){var r=t.match(/^\s*($|\/[\/\*])/,!1)?null:t.column()+1
e.context=new y(e.context,r,e.indented)}function x(e){e.context&&(e.indented=e.context.indented,e.context=e.context.prev)}e.defineMode("swift",(function(e){return{startState:function(){return{prev:null,context:null,indented:0,tokenize:[]}},token:function(e,t){var r=t.prev
t.prev=null
var n=(t.tokenize[t.tokenize.length-1]||h)(e,t,r)
if(n&&"comment"!=n?t.prev||(t.prev=n):t.prev=r,"punctuation"==n){var i=/[\(\[\{]|([\]\)\}])/.exec(e.current())
i&&(i[1]?x:b)(t,e)}return n},indent:function(t,r){var n=t.context
if(!n)return 0
var i=/^[\]\}\)]/.test(r)
return null!=n.align?n.align-(i?1:0):n.indented+(i?0:e.indentUnit)},electricInput:/^\s*[\)\}\]]$/,lineComment:"//",blockCommentStart:"/*",blockCommentEnd:"*/",fold:"brace",closeBrackets:"()[]{}''\"\"``"}})),e.defineMIME("text/x-swift","swift")})),function(e){"object"==typeof exports&&"object"==typeof module?e(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],e):e(CodeMirror)}((function(e){"use strict"
var t={autoSelfClosers:{area:!0,base:!0,br:!0,col:!0,command:!0,embed:!0,frame:!0,hr:!0,img:!0,input:!0,keygen:!0,link:!0,meta:!0,param:!0,source:!0,track:!0,wbr:!0,menuitem:!0},implicitlyClosed:{dd:!0,li:!0,optgroup:!0,option:!0,p:!0,rp:!0,rt:!0,tbody:!0,td:!0,tfoot:!0,th:!0,tr:!0},contextGrabbers:{dd:{dd:!0,dt:!0},dt:{dd:!0,dt:!0},li:{li:!0},option:{option:!0,optgroup:!0},optgroup:{optgroup:!0},p:{address:!0,article:!0,aside:!0,blockquote:!0,dir:!0,div:!0,dl:!0,fieldset:!0,footer:!0,form:!0,h1:!0,h2:!0,h3:!0,h4:!0,h5:!0,h6:!0,header:!0,hgroup:!0,hr:!0,menu:!0,nav:!0,ol:!0,p:!0,pre:!0,section:!0,table:!0,ul:!0},rp:{rp:!0,rt:!0},rt:{rp:!0,rt:!0},tbody:{tbody:!0,tfoot:!0},td:{td:!0,th:!0},tfoot:{tbody:!0},th:{td:!0,th:!0},thead:{tbody:!0,tfoot:!0},tr:{tr:!0}},doNotIndent:{pre:!0},allowUnquoted:!0,allowMissing:!0,caseFold:!0},r={autoSelfClosers:{},implicitlyClosed:{},contextGrabbers:{},doNotIndent:{},allowUnquoted:!1,allowMissing:!1,allowMissingTagName:!1,caseFold:!1}
e.defineMode("xml",(function(n,i){var o,a,l=n.indentUnit,s={},c=i.htmlMode?t:r
for(var u in c)s[u]=c[u]
for(var u in i)s[u]=i[u]
function d(e,t){function r(r){return t.tokenize=r,r(e,t)}var n=e.next()
return"<"==n?e.eat("!")?e.eat("[")?e.match("CDATA[")?r(p("atom","]]>")):null:e.match("--")?r(p("comment","--\x3e")):e.match("DOCTYPE",!0,!0)?(e.eatWhile(/[\w\._\-]/),r(h(1))):null:e.eat("?")?(e.eatWhile(/[\w\._\-]/),t.tokenize=p("meta","?>"),"meta"):(o=e.eat("/")?"closeTag":"openTag",t.tokenize=f,"tag bracket"):"&"==n?(e.eat("#")?e.eat("x")?e.eatWhile(/[a-fA-F\d]/)&&e.eat(";"):e.eatWhile(/[\d]/)&&e.eat(";"):e.eatWhile(/[\w\.\-:]/)&&e.eat(";"))?"atom":"error":(e.eatWhile(/[^&<]/),null)}function f(e,t){var r,n,i=e.next()
if(">"==i||"/"==i&&e.eat(">"))return t.tokenize=d,o=">"==i?"endTag":"selfcloseTag","tag bracket"
if("="==i)return o="equals",null
if("<"==i){t.tokenize=d,t.state=y,t.tagName=t.tagStart=null
var a=t.tokenize(e,t)
return a?a+" tag error":"tag error"}return/[\'\"]/.test(i)?(t.tokenize=(r=i,(n=function(e,t){for(;!e.eol();)if(e.next()==r){t.tokenize=f
break}return"string"}).isInAttribute=!0,n),t.stringStartCol=e.column(),t.tokenize(e,t)):(e.match(/^[^\s\u00a0=<>\"\']*[^\s\u00a0=<>\"\'\/]/),"word")}function p(e,t){return function(r,n){for(;!r.eol();){if(r.match(t)){n.tokenize=d
break}r.next()}return e}}function h(e){return function(t,r){for(var n;null!=(n=t.next());){if("<"==n)return r.tokenize=h(e+1),r.tokenize(t,r)
if(">"==n){if(1==e){r.tokenize=d
break}return r.tokenize=h(e-1),r.tokenize(t,r)}}return"meta"}}function m(e,t,r){this.prev=e.context,this.tagName=t,this.indent=e.indented,this.startOfLine=r,(s.doNotIndent.hasOwnProperty(t)||e.context&&e.context.noIndent)&&(this.noIndent=!0)}function g(e){e.context&&(e.context=e.context.prev)}function v(e,t){for(var r;;){if(!e.context)return
if(r=e.context.tagName,!s.contextGrabbers.hasOwnProperty(r)||!s.contextGrabbers[r].hasOwnProperty(t))return
g(e)}}function y(e,t,r){return"openTag"==e?(r.tagStart=t.column(),b):"closeTag"==e?x:y}function b(e,t,r){return"word"==e?(r.tagName=t.current(),a="tag",_):s.allowMissingTagName&&"endTag"==e?(a="tag bracket",_(e,t,r)):(a="error",b)}function x(e,t,r){if("word"==e){var n=t.current()
return r.context&&r.context.tagName!=n&&s.implicitlyClosed.hasOwnProperty(r.context.tagName)&&g(r),r.context&&r.context.tagName==n||!1===s.matchClosing?(a="tag",w):(a="tag error",k)}return s.allowMissingTagName&&"endTag"==e?(a="tag bracket",w(e,t,r)):(a="error",k)}function w(e,t,r){return"endTag"!=e?(a="error",w):(g(r),y)}function k(e,t,r){return a="error",w(e,0,r)}function _(e,t,r){if("word"==e)return a="attribute",C
if("endTag"==e||"selfcloseTag"==e){var n=r.tagName,i=r.tagStart
return r.tagName=r.tagStart=null,"selfcloseTag"==e||s.autoSelfClosers.hasOwnProperty(n)?v(r,n):(v(r,n),r.context=new m(r,n,i==r.indented)),y}return a="error",_}function C(e,t,r){return"equals"==e?S:(s.allowMissing||(a="error"),_(e,0,r))}function S(e,t,r){return"string"==e?T:"word"==e&&s.allowUnquoted?(a="string",_):(a="error",_(e,0,r))}function T(e,t,r){return"string"==e?T:_(e,0,r)}return d.isInText=!0,{startState:function(e){var t={tokenize:d,state:y,indented:e||0,tagName:null,tagStart:null,context:null}
return null!=e&&(t.baseIndent=e),t},token:function(e,t){if(!t.tagName&&e.sol()&&(t.indented=e.indentation()),e.eatSpace())return null
o=null
var r=t.tokenize(e,t)
return(r||o)&&"comment"!=r&&(a=null,t.state=t.state(o||r,e,t),a&&(r="error"==a?r+" error":a)),r},indent:function(t,r,n){var i=t.context
if(t.tokenize.isInAttribute)return t.tagStart==t.indented?t.stringStartCol+1:t.indented+l
if(i&&i.noIndent)return e.Pass
if(t.tokenize!=f&&t.tokenize!=d)return n?n.match(/^(\s*)/)[0].length:0
if(t.tagName)return!1!==s.multilineTagIndentPastTag?t.tagStart+t.tagName.length+2:t.tagStart+l*(s.multilineTagIndentFactor||1)
if(s.alignCDATA&&/<!\[CDATA\[/.test(r))return 0
var o=r&&/^<(\/)?([\w_:\.-]*)/.exec(r)
if(o&&o[1])for(;i;){if(i.tagName==o[2]){i=i.prev
break}if(!s.implicitlyClosed.hasOwnProperty(i.tagName))break
i=i.prev}else if(o)for(;i;){var a=s.contextGrabbers[i.tagName]
if(!a||!a.hasOwnProperty(o[2]))break
i=i.prev}for(;i&&i.prev&&!i.startOfLine;)i=i.prev
return i?i.indent+l:t.baseIndent||0},electricInput:/<\/[\s\w:]+>$/,blockCommentStart:"\x3c!--",blockCommentEnd:"--\x3e",configuration:s.htmlMode?"html":"xml",helperType:s.htmlMode?"html":"xml",skipAttribute:function(e){e.state==S&&(e.state=_)},xmlCurrentTag:function(e){return e.tagName?{name:e.tagName,close:"closeTag"==e.type}:null},xmlCurrentContext:function(e){for(var t=[],r=e.context;r;r=r.prev)r.tagName&&t.push(r.tagName)
return t.reverse()}}})),e.defineMIME("text/xml","xml"),e.defineMIME("application/xml","xml"),e.mimeModes.hasOwnProperty("text/html")||e.defineMIME("text/html",{name:"xml",htmlMode:!0})}))
