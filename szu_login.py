"""
    Version: 1.0
    Author: 致腾楼320计软实验室
    Date: 2025-01-14
    Description: 登录深大校园网脚本，方便无UI的服务器使用命令行快速登录
"""
import argparse

import execjs
import requests
import re
import json
import hashlib


def crack_salt(pwd, salt):
    return execjs.compile(r'function t(n,t){var r=(65535&n)+(65535&t);return(n>>16)+(t>>16)+('
                          r'r>>16)<<16|65535&r}function r(n,t){return n<<t|n>>>32-t}function e(n,e,o,u,c,f){return t('
                          r'r(t(t(e,n),t(u,f)),c),o)}function o(n,t,r,o,u,c,f){return e(t&r|~t&o,n,t,u,c,f)}function '
                          r'u(n,t,r,o,u,c,f){return e(t&o|r&~o,n,t,u,c,f)}function c(n,t,r,o,u,c,f){return e(t^r^o,n,'
                          r't,u,c,f)}function f(n,t,r,o,u,c,f){return e(r^(t|~o),n,t,u,c,f)}function i(n,'
                          r'r){n[r>>5]|=128<<r%32,n[14+(r+64>>>9<<4)]=r;var e,i,a,d,h,l=1732584193,g=-271733879,'
                          r'v=-1732584194,m=271733878;for(e=0;e<n.length;e+=16)i=l,a=g,d=v,h=m,g=f(g=f(g=f(g=f(g=c('
                          r'g=c(g=c(g=c(g=u(g=u(g=u(g=u(g=o(g=o(g=o(g=o(g,v=o(v,m=o(m,l=o(l,g,v,m,n[e],7,-680876936),'
                          r'g,v,n[e+1],12,-389564586),l,g,n[e+2],17,606105819),m,l,n[e+3],22,-1044525330),v=o(v,m=o(m,'
                          r'l=o(l,g,v,m,n[e+4],7,-176418897),g,v,n[e+5],12,1200080426),l,g,n[e+6],17,-1473231341),m,l,'
                          r'n[e+7],22,-45705983),v=o(v,m=o(m,l=o(l,g,v,m,n[e+8],7,1770035416),g,v,n[e+9],12,'
                          r'-1958414417),l,g,n[e+10],17,-42063),m,l,n[e+11],22,-1990404162),v=o(v,m=o(m,l=o(l,g,v,m,'
                          r'n[e+12],7,1804603682),g,v,n[e+13],12,-40341101),l,g,n[e+14],17,-1502002290),m,l,n[e+15],'
                          r'22,1236535329),v=u(v,m=u(m,l=u(l,g,v,m,n[e+1],5,-165796510),g,v,n[e+6],9,-1069501632),l,g,'
                          r'n[e+11],14,643717713),m,l,n[e],20,-373897302),v=u(v,m=u(m,l=u(l,g,v,m,n[e+5],5,'
                          r'-701558691),g,v,n[e+10],9,38016083),l,g,n[e+15],14,-660478335),m,l,n[e+4],20,-405537848),'
                          r'v=u(v,m=u(m,l=u(l,g,v,m,n[e+9],5,568446438),g,v,n[e+14],9,-1019803690),l,g,n[e+3],14,'
                          r'-187363961),m,l,n[e+8],20,1163531501),v=u(v,m=u(m,l=u(l,g,v,m,n[e+13],5,-1444681467),g,v,'
                          r'n[e+2],9,-51403784),l,g,n[e+7],14,1735328473),m,l,n[e+12],20,-1926607734),v=c(v,m=c(m,'
                          r'l=c(l,g,v,m,n[e+5],4,-378558),g,v,n[e+8],11,-2022574463),l,g,n[e+11],16,1839030562),m,l,'
                          r'n[e+14],23,-35309556),v=c(v,m=c(m,l=c(l,g,v,m,n[e+1],4,-1530992060),g,v,n[e+4],11,'
                          r'1272893353),l,g,n[e+7],16,-155497632),m,l,n[e+10],23,-1094730640),v=c(v,m=c(m,l=c(l,g,v,m,'
                          r'n[e+13],4,681279174),g,v,n[e],11,-358537222),l,g,n[e+3],16,-722521979),m,l,n[e+6],23,'
                          r'76029189),v=c(v,m=c(m,l=c(l,g,v,m,n[e+9],4,-640364487),g,v,n[e+12],11,-421815835),l,g,'
                          r'n[e+15],16,530742520),m,l,n[e+2],23,-995338651),v=f(v,m=f(m,l=f(l,g,v,m,n[e],6,'
                          r'-198630844),g,v,n[e+7],10,1126891415),l,g,n[e+14],15,-1416354905),m,l,n[e+5],21,'
                          r'-57434055),v=f(v,m=f(m,l=f(l,g,v,m,n[e+12],6,1700485571),g,v,n[e+3],10,-1894986606),l,g,'
                          r'n[e+10],15,-1051523),m,l,n[e+1],21,-2054922799),v=f(v,m=f(m,l=f(l,g,v,m,n[e+8],6,'
                          r'1873313359),g,v,n[e+15],10,-30611744),l,g,n[e+6],15,-1560198380),m,l,n[e+13],21,'
                          r'1309151649),v=f(v,m=f(m,l=f(l,g,v,m,n[e+4],6,-145523070),g,v,n[e+11],10,-1120210379),l,g,'
                          r'n[e+2],15,718787259),m,l,n[e+9],21,-343485551),l=t(l,i),g=t(g,a),v=t(v,d),m=t(m,'
                          r'h);return[l,g,v,m]}function a(n){var t,r="",e=32*n.length;for('
                          r't=0;t<e;t+=8)r+=String.fromCharCode(n[t>>5]>>>t%32&255);return r}function d(n){var t,'
                          r'r=[];for(r[(n.length>>2)-1]=void 0,t=0;t<r.length;t+=1)r[t]=0;var e=8*n.length;for('
                          r't=0;t<e;t+=8)r[t>>5]|=(255&n.charCodeAt(t/8))<<t%32;return r}function h(n){return a(i(d('
                          r'n),8*n.length))}function l(n,t){var r,e,o=d(n),u=[],c=[];for(u[15]=c[15]=void 0,'
                          r'o.length>16&&(o=i(o,8*n.length)),r=0;r<16;r+=1)u[r]=909522486^o[r],c[r]=1549556828^o['
                          r'r];return e=i(u.concat(d(t)),512+8*t.length),a(i(c.concat(e),640))}function g(n){var t,r,'
                          r'e="";for(r=0;r<n.length;r+=1)t=n.charCodeAt(r),e+="0123456789abcdef".charAt('
                          r't>>>4&15)+"0123456789abcdef".charAt(15&t);return e}function v(n){return unescape('
                          r'encodeURIComponent(n))}function s(n,t){return l(v(n),v(t))}function C(n,t){return g(s(n,'
                          r't))}').call('C', salt,
                                        pwd)


def crack_info(info, token):
    return execjs.compile(r'base64=(function($){var _PADCHAR="=",'
                          r'_ALPHA="LVoJPiCN2R8G90yg+hmFHuacZ1OWMnrsSTXkYpUq/3dlbfKwv6xztjI7DeBE45QA",'
                          r'_VERSION="1.0";function _getbyte64(s,i){var idx=_ALPHA.indexOf(s.charAt(i));if('
                          r'idx===-1){throw"Cannot decode base64"}return idx}function _setAlpha(s){'
                          r'_ALPHA=s;}function _decode(s){var pads=0,i,b10,imax=s.length,x=[];s=String(s);if('
                          r'imax===0){return s}if(imax%4!==0){throw"Cannot decode base64"}if(s.charAt('
                          r'imax-1)===_PADCHAR){pads=1;if(s.charAt(imax-2)===_PADCHAR){pads=2}imax-=4}for('
                          r'i=0;i<imax;i+=4){b10=(_getbyte64(s,i)<<18)|(_getbyte64(s,i+1)<<12)|(_getbyte64(s,'
                          r'i+2)<<6)|_getbyte64(s,i+3);x.push(String.fromCharCode(b10>>16,(b10>>8)&255,'
                          r'b10&255))}switch(pads){case 1:b10=(_getbyte64(s,i)<<18)|(_getbyte64(s,i+1)<<12)|('
                          r'_getbyte64(s,i+2)<<6);x.push(String.fromCharCode(b10>>16,(b10>>8)&255));break;case '
                          r'2:b10=(_getbyte64(s,i)<<18)|(_getbyte64(s,i+1)<<12);x.push(String.fromCharCode('
                          r'b10>>16));break}return x.join("")}function _getbyte(s,i){var x=s.charCodeAt(i);if('
                          r'x>255){throw"INVALID_CHARACTER_ERR: DOM Exception 5"}return x}function _encode(s){if('
                          r'arguments.length!==1){throw"SyntaxError: exactly one argument required"}s=String('
                          r's);var i,b10,x=[],imax=s.length-s.length%3;if(s.length===0){return s}for('
                          r'i=0;i<imax;i+=3){b10=(_getbyte(s,i)<<16)|(_getbyte(s,i+1)<<8)|_getbyte(s,i+2);x.push('
                          r'_ALPHA.charAt(b10>>18));x.push(_ALPHA.charAt((b10>>12)&63));x.push(_ALPHA.charAt(('
                          r'b10>>6)&63));x.push(_ALPHA.charAt(b10&63))}switch(s.length-imax){case 1:b10=_getbyte('
                          r's,i)<<16;x.push(_ALPHA.charAt(b10>>18)+_ALPHA.charAt(('
                          r'b10>>12)&63)+_PADCHAR+_PADCHAR);break;case 2:b10=(_getbyte(s,i)<<16)|(_getbyte(s,'
                          r'i+1)<<8);x.push(_ALPHA.charAt(b10>>18)+_ALPHA.charAt((b10>>12)&63)+_ALPHA.charAt(('
                          r'b10>>6)&63)+_PADCHAR);break}return x.join("")}return{decode:_decode,encode:_encode,'
                          r'setAlpha:_setAlpha,VERSION:_VERSION}}());function value(info,token){base64.setAlpha('
                          r'"LVoJPiCN2R8G90yg+hmFHuacZ1OWMnrsSTXkYpUq/3dlbfKwv6xztjI7DeBE45QA");function encode('
                          r'str,key){var v=s(str,true);var k=s(key,false);if(k.length<4)k.length=4;var '
                          r'n=v.length-1,z=v[n],y=v[0],c=0x86014019|0x183639A0,m,e,p,q=Math.floor(6+52/(n+1)),'
                          r'd=0;while(0<q--){d=d+c&(0x8CE0D9BF|0x731F2640);e=d>>>2&3;for(p=0;p<n;p++){y=v['
                          r'p+1];m=z>>>5^y<<2;m+=y>>>3^z<<4^(d^y);m+=k[p&3^e]^z;z=v[p]=v[p]+m&('
                          r'0xEFB8D130|0x10472ECF);}y=v[0];m=z>>>5^y<<2;m+=y>>>3^z<<4^(d^y);m+=k[p&3^e]^z;z=v['
                          r'n]=v[n]+m&(0xBB390742|0x44C6F8BD);}return l(v,false);}function s(a,'
                          r'b){var c=a.length;var v=[];for(var i=0;i<c;i+=4){v[i>>2]=a.charCodeAt(i)|a.charCodeAt('
                          r'i+1)<<8|a.charCodeAt(i+2)<<16|a.charCodeAt(i+3)<<24;}if(b)v[v.length]=c;return '
                          r'v;}function l(a,b){var d=a.length;var c=d-1<<2;if(b){var m=a[d-1];if(m<c-3||m>c)return '
                          r'null;c=m;}for(var i=0;i<d;i++){a[i]=String.fromCharCode(a[i]&0xff,a[i]>>>8&0xff,'
                          r'a[i]>>>16&0xff,a[i]>>>24&0xff);}return b?a.join("").substring(0,c):a.join('
                          r'"");}return"{SRBX1}"+base64.encode(encode(info,token));}').call('value', info, token)


def get_config(username):
    # 发送 GET 请求
    url = "https://net.szu.edu.cn/cgi-bin/get_challenge?callback=jQuery1124003478318504449107_1736831232135&username=" + username
    json_data = re.search(r'^\w+\(\s*(\{.*\})\s*\)$', requests.get(url).text)
    if json_data:
        data = json.loads(json_data.group(1))
        challenge = data.get('challenge')
        client_ip = data.get('client_ip')
        return challenge, client_ip
        # 输出结果
    else:
        print("IP获取失败")
        return None
    # 输出结果


def login(username, password, client_ip, info_salt, chksum):
    params = {
        "callback": "jQuery112403759683287198097_1736836702315",
        "action": "login",
        "username": username,
        "password": "{MD5}" + password,
        "os": "Windows 10",
        "name": "Windows",
        "nas_ip": "",
        "double_stack": 0,
        "chksum": chksum,
        "info": info_salt,
        "ac_id": 12,
        "ip": client_ip,
        "n": 200,
        "type": 1
    }
    base_url = "https://net.szu.edu.cn/cgi-bin/srun_portal"
    response = requests.get(base_url, params=params)
    json_data = re.search(r'^\w+\(\s*(\{.*\})\s*\)$', response.text)
    if json_data:
        data = json.loads(json_data.group(1))
        login_user = data.get('username')
        online_ip = data.get('online_ip')
        result = data.get('res')
        suc_msg = data.get('suc_msg')
        return login_user, result, online_ip, suc_msg
    else:
        print("网络异常")
        return None


# 使用方法： python szu_login.py - -username 学号(6位数) --password 密码
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="获取用以登录的账号密码")

    # 添加命令行选项
    parser.add_argument('--username', type=str, help="用户账号(6位数)", required=True)
    parser.add_argument('--password', type=str, help="用户密码", required=True)

    # 解析命令行参数
    args = parser.parse_args()
    username = args.username
    password = args.password
    if len(username) != 6:
        print("请输入6位数的学号")
        exit(-1)
    token, client_ip = get_config(username)
    info = '{"username":"info1","password":"info2","ip":"info3","acid":"12","enc_ver":"srun_bx1"}'
    info = info.replace("info1", username)
    info = info.replace("info2", password)
    info = info.replace("info3", client_ip)
    hmd5 = crack_salt(password, token)
    i = crack_info(info, token)

    data = token + username
    data += token + hmd5
    data += token + "12"  # ac_id
    data += token + client_ip
    data += token + "200"  # n
    data += token + "1"
    data += token + i

    # 创建 SHA-1 哈希对象
    sha1_hash = hashlib.sha1()
    sha1_hash.update(data.encode('utf-8'))
    chksum = sha1_hash.hexdigest()
    login_user, result, online_ip, suc_msg = login(username, hmd5, client_ip, i, chksum)
    if login_user:
        print("用户：" + login_user + ",登录成功(" + result + "),IP:" + online_ip + "," + suc_msg)
    else:
        print("登陆失败：" + result)
