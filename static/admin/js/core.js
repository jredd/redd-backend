function addEvent(t,e,o){if(t.addEventListener)return t.addEventListener(e,o,!1),!0;if(t.attachEvent){var r=t.attachEvent("on"+e,o);return r}return!1}function removeEvent(t,e,o){return t.removeEventListener?(t.removeEventListener(e,o,!1),!0):t.detachEvent?(t.detachEvent("on"+e,o),!0):!1}function cancelEventPropagation(t){t||(t=window.event),t.cancelBubble=!0,t.stopPropagation&&t.stopPropagation()}function quickElement(){var t=document.createElement(arguments[0]);if(arguments[2]){var e=document.createTextNode(arguments[2]);t.appendChild(e)}for(var o=arguments.length,r=3;o>r;r+=2)t.setAttribute(arguments[r],arguments[r+1]);return arguments[1].appendChild(t),t}function removeChildren(t){for(;t.hasChildNodes();)t.removeChild(t.lastChild)}function findPosX(t){var e=0;if(t.offsetParent){for(;t.offsetParent;)e+=t.offsetLeft-(isOpera?0:t.scrollLeft),t=t.offsetParent;isIE&&t.parentElement&&(e+=t.offsetLeft-t.scrollLeft)}else t.x&&(e+=t.x);return e}function findPosY(t){var e=0;if(t.offsetParent){for(;t.offsetParent;)e+=t.offsetTop-(isOpera?0:t.scrollTop),t=t.offsetParent;isIE&&t.parentElement&&(e+=t.offsetTop-t.scrollTop)}else t.y&&(e+=t.y);return e}function getStyle(t,e){var o="";return document.defaultView&&document.defaultView.getComputedStyle?o=document.defaultView.getComputedStyle(t,"").getPropertyValue(e):t.currentStyle&&(e=e.replace(/\-(\w)/g,function(t,e){return e.toUpperCase()}),o=t.currentStyle[e]),o}var isOpera=navigator.userAgent.indexOf("Opera")>=0&&parseFloat(navigator.appVersion),isIE=document.all&&!isOpera&&parseFloat(navigator.appVersion.split("MSIE ")[1].split(";")[0]),xmlhttp;xmlhttp||"undefined"==typeof XMLHttpRequest||(xmlhttp=new XMLHttpRequest),Date.prototype.getTwelveHours=function(){return hours=this.getHours(),0==hours?12:12>=hours?hours:hours-12},Date.prototype.getTwoDigitMonth=function(){return this.getMonth()<9?"0"+(this.getMonth()+1):this.getMonth()+1},Date.prototype.getTwoDigitDate=function(){return this.getDate()<10?"0"+this.getDate():this.getDate()},Date.prototype.getTwoDigitTwelveHour=function(){return this.getTwelveHours()<10?"0"+this.getTwelveHours():this.getTwelveHours()},Date.prototype.getTwoDigitHour=function(){return this.getHours()<10?"0"+this.getHours():this.getHours()},Date.prototype.getTwoDigitMinute=function(){return this.getMinutes()<10?"0"+this.getMinutes():this.getMinutes()},Date.prototype.getTwoDigitSecond=function(){return this.getSeconds()<10?"0"+this.getSeconds():this.getSeconds()},Date.prototype.getHourMinute=function(){return this.getTwoDigitHour()+":"+this.getTwoDigitMinute()},Date.prototype.getHourMinuteSecond=function(){return this.getTwoDigitHour()+":"+this.getTwoDigitMinute()+":"+this.getTwoDigitSecond()},Date.prototype.strftime=function(t){for(var e={c:this.toString(),d:this.getTwoDigitDate(),H:this.getTwoDigitHour(),I:this.getTwoDigitTwelveHour(),m:this.getTwoDigitMonth(),M:this.getTwoDigitMinute(),p:this.getHours()>=12?"PM":"AM",S:this.getTwoDigitSecond(),w:"0"+this.getDay(),x:this.toLocaleDateString(),X:this.toLocaleTimeString(),y:(""+this.getFullYear()).substr(2,4),Y:""+this.getFullYear(),"%":"%"},o="",r=0;r<t.length;)"%"===t.charAt(r)?(o+=e[t.charAt(r+1)],++r):o+=t.charAt(r),++r;return o},String.prototype.pad_left=function(t,e){for(var o=this,r=0;o.length<t;r++)o=e+o;return o};