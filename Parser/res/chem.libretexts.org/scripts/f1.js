!function(){"use strict";function e(e){var t=function(e,t){if("object"!=typeof e||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function t(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function r(t,r){for(var i=0;i<r.length;i++){var n=r[i];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(t,e(n.key),n)}}function i(e,t,i){return t&&r(e.prototype,t),i&&r(e,i),Object.defineProperty(e,"prototype",{writable:!1}),e}function n(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),Object.defineProperty(e,"prototype",{writable:!1}),t&&o(e,t)}function s(e){return s=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},s(e)}function o(e,t){return o=Object.setPrototypeOf?Object.setPrototypeOf.bind():function(e,t){return e.__proto__=t,e},o(e,t)}function a(e,t){if(t&&("object"==typeof t||"function"==typeof t))return t;if(void 0!==t)throw new TypeError("Derived constructors may only return object or undefined");return function(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}(e)}var c=function(){function e(r){var i=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},n=i.data,s=void 0===n?{}:n,o=i.fingerprint,a=void 0===o?"widget-error":o;t(this,e),this._error=new Error(r),this._data=s,this._fingerprint=a}return i(e,[{key:"error",get:function(){return this._error}},{key:"data",get:function(){return this._data}},{key:"fingerprint",get:function(){return this._fingerprint}}]),e}(),g=function(e){function r(e,i){var n=(arguments.length>2&&void 0!==arguments[2]?arguments[2]:{}).fingerprint,o=void 0===n?"widget-dom-error":n;t(this,r);var c=(i.body||{}).outerHTML||"";return a(this,s(r).call(this,e,{data:{html:{body:c}},fingerprint:o}))}return n(r,e),r}(c),l=function(e){function r(e,i){var n;return t(this,r),(n=a(this,s(r).call(this,r.message,i,{fingerprint:"widget-dom-embed-target-not-found-error"})))._data.embedId=e,n}return n(r,e),i(r,null,[{key:"message",get:function(){return"Web widget could not be initialized because the target element could not be found"}}]),r}(g),d=[];if("true"==="true".toLowerCase()){var u="";""===u&&(u="Back");var b="";""===b&&(b="Back"),d.push({name:"back",text:u,title:b})}if("true"==="true".toLowerCase()){var p="";""===p&&(p="Forward");var w="";""===w&&(w="Forward"),d.push({name:"forward",text:p,title:w})}if("true"==="true".toLowerCase()){var _="";""===_&&(_="Home");var f="";""===f&&(f="Home"),d.push({name:"home",text:_,title:f})}if("true"==="true".toLowerCase()){var m="";""===m&&(m="Open article");var j="";""===j&&(j="Open article"),d.push({name:"open",text:m,title:j})}var h=null;if("true"==="true".toLowerCase()){var v="";""===v&&(v="search"),h={hint:v}}var y=null;if("f1-button"==="f1".toLowerCase()){var z="";""===z&&(z="Help"),y={path:"",text:z}}var x={dialog:{buttons:d,search:h,paths:{home:"",search:""},footer:{text:"Powered by CXone Expert"},modalStyle:".mt-f1-scroll{height:100%;overflow:hidden}.mt-f1-overlay{background:#999;left:0;opacity:.5;position:fixed;top:0}.mt-f1-container{left:0!important;margin:auto;max-width:800px;position:fixed;right:0!important;width:90%!important}@media all and (max-width:25em){.mt-f1-container{width:100%!important}}.mt-f1-modal-wrapper{border:0;border-radius:.5em;box-shadow:0 0 15px rgba(0,0,0,.4);overflow:hidden;padding:0;width:100%}@media all and (max-width:25em){.mt-f1-modal-wrapper{border-radius:0}}.mt-f1-modal-header{float:right}.mt-f1-modal-content{border:0;border-radius:.5em}"},helpButton:y};x.selector=".F1, .mt-f1-success",function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=document.createElement("script");t.setAttribute("type","text/javascript"),t.dataset&&(t.dataset.mindtouchModule="true"),t.src="https://a.mtstatic.com/@app/web-widgets/assets/f1.widget.js?_=1246c35ba31dd5091e4d1df287a9296da2c3b424:site_4334",t.onload=function(){var t="f1",r={personId:"site_4334:2:NTk2OTZkYjgtMmUyYS00OTYyLTg5ZjktNTQxNzYwMDExMzg1fDIwMjQtMDktMTlUMTk6MTE6MjY=",enabled:"true"==="false".toLowerCase()};r.accessToken="9e1313fa437b4ef4ab9aece8ac67890e";r.environment="production";r.codeVersion="1246c35ba31dd5091e4d1df287a9296da2c3b424",e.embedId="",e.host="https://chem.libretexts.org",e.origin=document.location.href,e.rollbar=r,e.style=".html-mixin{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}.html-body-mixin{background-color:transparent;color:#000;font:normal 100%/1.2 arial,helvetica,sans-serif;margin:0;overflow-x:hidden;padding:0}html{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body,html{background-color:transparent;color:#000;font:normal 100%/1.2 arial,helvetica,sans-serif;margin:0;overflow-x:hidden;padding:0}:host{background-color:transparent;color:#000;font:normal 100%/1.2 arial,helvetica,sans-serif;margin:0;overflow-x:hidden;padding:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block;vertical-align:baseline}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0}a{color:#30b3f6;text-decoration:none}a:hover{color:#b4b4b4}a:visited{text-decoration:none}a:active{color:#b4b4b4;outline:#30b3f6 dotted 1px}a:focus{color:#b4b4b4;outline:#30b3f6 dotted 1px}.mt-button,a.mt-button,button,input[type=button],input[type=reset],input[type=submit]{background-color:#efefef;border:1px solid #969696;border-radius:.25em;box-sizing:border-box;color:#000;cursor:pointer;display:inline-block;line-height:2;margin:0;max-height:2em;max-width:100%;outline:0;overflow:hidden;padding:0 .8em;text-align:center;text-decoration:none;text-overflow:ellipsis}.mt-button:active,.mt-button:focus,.mt-button:hover,a.mt-button:active,a.mt-button:focus,a.mt-button:hover,button:active,button:focus,button:hover,input[type=button]:active,input[type=button]:focus,input[type=button]:hover,input[type=reset]:active,input[type=reset]:focus,input[type=reset]:hover,input[type=submit]:active,input[type=submit]:focus,input[type=submit]:hover{border:1px solid #30b3f6}.mt-button:hover,a.mt-button:hover,button:hover,input[type=button]:hover,input[type=reset]:hover,input[type=submit]:hover{background-color:#bcbcbc;border-color:#30b3f6;box-shadow:0 0 .3em rgba(48,179,246,.5);color:#000}.mt-button:focus,a.mt-button:focus,button:focus,input[type=button]:focus,input[type=reset]:focus,input[type=submit]:focus{background-color:#bcbcbc;border-color:#30b3f6;box-shadow:0 0 .5em rgba(48,179,246,.5);color:#000}.mt-button:active,a.mt-button:active,button:active,input[type=button]:active,input[type=reset]:active,input[type=submit]:active{background-color:#bcbcbc;border-color:#30b3f6;box-shadow:inset .2em .1em .5em rgba(0,0,0,.3);color:#000}input[type=search]{-webkit-appearance:textfield}.mt-button-primary,a.mt-button-primary,input[type=button].mt-button-primary,input[type=submit].mt-button-primary{background:#747474;border:1px solid #747474;color:#fff;outline:0;text-shadow:none}.mt-button-primary:hover,a.mt-button-primary:hover,input[type=button].mt-button-primary:hover,input[type=submit].mt-button-primary:hover{background:#4e4e4e;border-color:#18aaf5;color:#fff}.mt-button-primary:focus,a.mt-button-primary:focus,input[type=button].mt-button-primary:focus,input[type=submit].mt-button-primary:focus{background:#4e4e4e;border-color:#18aaf5;color:#fff}.mt-button-primary:active,a.mt-button-primary:active,input[type=button].mt-button-primary:active,input[type=submit].mt-button-primary:active{background-color:#4e4e4e;border-color:#30b3f6;box-shadow:inset .2em .1em .5em rgba(0,0,0,.5);color:#fff}form{margin:0}.mt-fieldset,fieldset{border:1px solid #bbb;border-radius:.25em;margin-bottom:1.5em;overflow:hidden;padding:1em 1.5em 1.5em}.field,.mt-field{margin-bottom:1.5em}.mt-submit{clear:both;margin-bottom:0}.mt-legend,legend{font-size:1.2em;margin:0 -.5em;padding:0 .5em}.mt-label,label{display:block;margin:0 .5em .5em 0}.mt-label:after,label:after{content:\':\'}.mt-label-checkbox{display:inline-block;margin:0 0 .5em;width:auto}.mt-label-checkbox:after{content:\'\'}.mt-radio .mt-label-checkbox{margin-right:1em}.mt-select,.mt-text,.mt-textarea,input,select,textarea{border:1px solid #bbb;border-radius:.25em;box-sizing:border-box;color:#000;margin:0;padding:.5em;text-indent:.5em;width:100%}.mt-select,.mt-textarea,select,textarea{width:auto}.mt-select,select{padding:.25em 0;text-indent:0;white-space:nowrap}.mt-textarea,textarea{clear:both;min-height:5em}input[type=radio]{display:inline-block;margin:0 0 .5em;width:auto}input[type=button],input[type=submit]{width:auto}.mt-select:hover,.mt-text:hover,.mt-textarea:hover,input:hover,select:hover,textarea:hover{border:1px solid #30b3f6}.mt-select:active,.mt-select:focus,.mt-text:active,.mt-text:focus,.mt-textarea:active,.mt-textarea:focus,input:active,input:focus,select:active,select:focus,textarea:active,textarea:focus{border:1px solid #30b3f6;box-shadow:inset .1em .1em .4em rgba(0,0,0,.15);outline:0}.mt-checkbox,input[type=checkbox],input[type=radio]{border:0;display:inline-block;height:auto;margin:0 .5em 0 0;outline:0;padding:0;position:relative;top:1px;width:auto}.mt-checkbox:active,.mt-checkbox:focus,input[type=checkbox]:active,input[type=checkbox]:focus,input[type=radio]:active,input[type=radio]:focus{outline:1px solid #30b3f6}input[placeholder]{text-overflow:ellipsis}input::-moz-placeholder{text-overflow:ellipsis}input:-moz-placeholder{text-overflow:ellipsis}input:-ms-input-placeholder{text-overflow:ellipsis}::-webkit-input-placeholder{text-overflow:ellipsis}:focus::-webkit-input-placeholder{color:transparent}:focus::-moz-placeholder{color:transparent}:focus:-moz-placeholder{color:transparent}:focus:-ms-input-placeholder{color:transparent}.mt-disabled,.mt-disabled:active,.mt-disabled:focus,.mt-disabled:hover,input.disabled,input.disabled:active,input.disabled:focus,input.disabled:hover,input[disabled],input[disabled]:active,input[disabled]:focus,input[disabled]:hover,select.disabled,select.disabled:active,select.disabled:focus,select.disabled:hover,select[disabled],select[disabled]:active,select[disabled]:focus,select[disabled]:hover,textarea.disabled,textarea.disabled:active,textarea.disabled:focus,textarea.disabled:hover,textarea[disabled],textarea[disabled]:active,textarea[disabled]:focus,textarea[disabled]:hover{background:#ececec!important;border:1px solid #c6c6c6!important;box-shadow:none!important;color:#b9b9b9!important;cursor:default!important}a.mt-disabled,a.mt-disabled:active,a.mt-disabled:focus,a.mt-disabled:hover,a:disabled:active,a:disabled:focus,a:disabled:hover,label.mt-disabled,label.mt-disabled:active,label.mt-disabled:focus a:disabled,label.mt-disabled:hover,label:disabled,label:disabled:active,label:disabled:focus,label:disabled:hover{background:0 0!important;border:0!important;color:#b9b9b9!important}h1,h2,h3,h4,h5,h6{color:#000;font:normal 200%/1.5 arial,helvetica,sans-serif;margin:2em 0 .5em;padding:0}h1{font-size:250%}h2{font-size:225%}h3{font-size:200%}h4{font-size:175%}h5{font-size:150%}h6{font-size:125%}dd,ol,ul{line-height:1.4;padding-left:1.4em}ol{list-style:decimal}ul{list-style:disc}ol ul,ul ul{list-style:circle}ol ol ul,ol ul ul,ul ol ul,ul ul ul{list-style:square}dt{font-weight:700}dd,li,ol ol,ol ul,ul ol,ul ul{margin:.25em 0}.mt-help,.mt-note,.mt-required{color:#999;font-size:90%;font-style:italic;line-height:1.5}.mt-error{color:#912b1d}.mt-flex-container{display:flex}.mt-show{display:block}.mt-hide{display:none!important}@-webkit-keyframes mt-spin-loader-animation{0%{-moz-transform:rotate(0);-ms-transform:rotate(0);-o-transform:rotate(0);-webkit-transform:rotate(0);transform:rotate(0)}100%{-moz-transform:rotate(360deg);-ms-transform:rotate(360deg);-o-transform:rotate(360deg);-webkit-transform:rotate(360deg);transform:rotate(360deg)}}@-moz-keyframes mt-spin-loader-animation{0%{-moz-transform:rotate(0);-ms-transform:rotate(0);-o-transform:rotate(0);-webkit-transform:rotate(0);transform:rotate(0)}100%{-moz-transform:rotate(360deg);-ms-transform:rotate(360deg);-o-transform:rotate(360deg);-webkit-transform:rotate(360deg);transform:rotate(360deg)}}@keyframes mt-spin-loader-animation{0%{-moz-transform:rotate(0);-ms-transform:rotate(0);-o-transform:rotate(0);-webkit-transform:rotate(0);transform:rotate(0)}100%{-moz-transform:rotate(360deg);-ms-transform:rotate(360deg);-o-transform:rotate(360deg);-webkit-transform:rotate(360deg);transform:rotate(360deg)}}.mt-spin-loader{-moz-animation-duration:.75s;-webkit-animation-duration:.75s;animation-duration:.75s;-moz-animation-iteration-count:infinite;-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite;-moz-animation-name:mt-spin-loader-animation;-webkit-animation-name:mt-spin-loader-animation;animation-name:mt-spin-loader-animation;-moz-animation-timing-function:linear;-webkit-animation-timing-function:linear;animation-timing-function:linear;border:8px solid #999;border-radius:50%;border-right-color:transparent;bottom:0;display:inline-block;height:30px;left:50%;margin:-15px;position:absolute;right:0;top:50%;width:30px}.mt-spin-overlay{background-color:#fff;height:100%;left:0;opacity:.75;position:fixed;top:0;width:100%;z-index:9999}blockquote,body,dd,div,dl,dt,fieldset,form,h1,h2,h3,h4,h5,h6,input,li,ol,p,pre,td,textarea,th,ul{margin:0;padding:0}table{border-collapse:collapse;border-spacing:0}address,caption,cite,code,dfn,em,strong,th,var{font-style:normal;font-weight:400}ol,ul{list-style:none}caption,th{text-align:left}h1,h2,h3,h4,h5,h6{font-size:100%;font-weight:400}q:after,q:before{content:\'\'}caption{margin-bottom:.5em;text-align:center}abbr,acronym,fieldset,img{border:0}.mt-f1-modal-header{margin:1.25em 1em 0 0;text-align:right}@media all and (max-width:37.5em){.mt-f1-modal-header{margin-right:.75em}}.mt-f1-modal-header .mt-f1-close{border:none;fill:#999;line-height:initial;padding:0}.mt-f1-modal-header .mt-f1-close:active,.mt-f1-modal-header .mt-f1-close:focus,.mt-f1-modal-header .mt-f1-close:hover{background:inherit}.mt-f1-modal-header svg{height:13px;width:13px}.mt-f1-modal-header:active,.mt-f1-modal-header:focus,.mt-f1-modal-header:hover{fill:#30b3f6}.mt-f1-buttons{float:left}@media all and (max-width:37.5em){.mt-f1-buttons{padding-left:.91em}}.mt-f1-buttons li{margin-right:2em}@media all and (max-width:37.5em){.mt-f1-buttons li{margin-right:1em}}@media all and (max-width:37.5em){.mt-f1-buttons li:first-child a{margin-left:0}}.mt-f1-buttons li:last-child{margin:0}.mt-f1-frame{background:#fff;border:0;height:526px}.mt-f1-dialog{font-family:Arial,Helvetica,sans-serif;font-size:.8em}.mt-f1-dialog a{font-weight:700;text-decoration:none}.mt-f1-dialog-bar{background:#efefef;overflow:hidden;padding:0}.mt-f1-dialog-bar a svg{display:none}.mt-f1-dialog-top{border-bottom:1px solid #b4b4b4;border-top-left-radius:.5em;border-top-right-radius:.5em;min-height:3.5em}.mt-f1-dialog-top ul{align-items:center;display:flex;overflow:hidden;padding:.75em .75em .75em 1em}@media all and (max-width:37.5em){.mt-f1-dialog-top ul{padding-right:0}}.mt-f1-dialog-top a{color:#666}.mt-f1-dialog-top a:hover{color:#30b3f6}.mt-f1-dialog-bottom{height:0}.mt-f1-dialog-content{border-bottom-left-radius:.5em;border-bottom-right-radius:.5em;overflow:hidden;transform:translateY(0)}.mt-f1-dialog-content.mtf1-ios{-webkit-overflow-scrolling:touch;overflow-y:scroll}.mt-f1-dialog-top .mt-f1-last{background:0 0;border-right:0;padding-right:0}.mt-f1-dialog-search-submit{background:0 0;border:0;box-shadow:none;cursor:pointer;font-size:115%;line-height:1.2;margin-left:.5em;padding:0;position:absolute;top:1em}.mt-f1-dialog-search-submit svg{fill:#999999;height:1.2em;width:1.2em}.mt-f1-dialog-search-submit:active,.mt-f1-dialog-search-submit:focus,.mt-f1-dialog-search-submit:hover{background:0 0;border:0;box-shadow:none;outline:0;padding:0}.mt-f1-dialog-search-submit:active:before,.mt-f1-dialog-search-submit:focus:before,.mt-f1-dialog-search-submit:hover:before{color:#30b3f6}.mt-f1-dialog-search-input{background:#fff;border:1px solid #b4b4b4;border-radius:.25em;box-sizing:border-box;display:flex;font-size:1em;margin:0;outline:0;padding:.25em 0 .25em 1.75em;width:20em}@media all and (max-width:37.5em){.mt-f1-dialog-bar a{display:inline-block;font-size:115%;height:1.2em;line-height:1.2;margin:.25em 0 0 .5em;overflow:hidden;width:1.2em}.mt-f1-dialog-bar a svg{display:inline-block;fill:#999999;height:1.2em;overflow:hidden;width:1.2em}.mt-f1-dialog-search-input{width:10em}.mt-f1-dialog-top{border-radius:0}}",e.token="xhr_2_1726773087_cfbf85238c63f0b75df23fe49c03b473d3f29e036dcfa8ffc62de57ef702ddc2";try{if(!e.embedId)return void window._MindTouchWebWidgetFactory.create(t,e).load();var i=document.getElementById("mindtouch-embed-".concat(e.embedId));if(!i)throw new l(e.embedId,document);var n=window._MindTouchWebWidgetFactory.create(t,e);"false"!==(i.dataset||{}).autoload&&n.load()}catch(e){var s="The requested CXone Expert Touchpoint could not be loaded by your web browser.";""===s&&(s=e.message),(console||{error:function(){}}).error(s)}},document.body.appendChild(t)}(x)}();