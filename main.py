from sys import exit
from smtplib import SMTP_SSL
from json import loads
from imaplib import IMAP4_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep, localtime, strftime
from requests import get, post, Session
from bs4 import BeautifulSoup
from js2py import eval_js
from fake_useragent import UserAgent
from peewee import CharField, IntegerField, Model,SqliteDatabase, DoesNotExist, IntegrityError
import mailparser


def log(text):
    notify = strftime('\n%d.%m.%Y  %H:%M:%S:\n', localtime()) + text
    print(notify)
    with open('log.txt', 'a+') as f:
        f.write(notify+'\n')


def get_headers(flag, userag, phpsessid_=''):
    if flag == 'post':
        return {
            'Accept': 'text/html,application/xhtml+xml,application/xml;'
                      'q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '161',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '_ga=GA1.2.1703807638.1571679662; '
                      '_gid=GA1.2.1281852873.1571896806; '
                      f'PHPSESSID={phpsessid_}',
            'DNT': '1',
            'Host': 'www.betonsuccess.ru',
            'Origin': 'https://www.betonsuccess.ru',
            'referer': 'https://www.betonsuccess.ru/',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': f'{userag}'
        }
    elif flag == 'bet':
        return {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.1703807638.1571679662; '
                      '_gid=GA1.2.1281852873.1571896806; ',
            'DNT': '1',
            'Host': 'www.betonsuccess.ru',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': f'{userag}'
        }
    elif flag == 'picks':
        return {
            'Accept': 'text/html,application/xhtml+xml,application/xml;'
                      'q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.1703807638.1571679662; '
                      '_gid=GA1.2.1281852873.1571896806; '
                      f'PHPSESSID={phpsessid_}',
            'DNT': '1',
            'Host': 'www.betonsuccess.ru',
            'Referer': 'https://www.betonsuccess.ru/user/orders_free/',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': f'{userag}'
        }
    elif flag == 'js':
        return {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '88',
            'Content-Type': 'application/octet-stream',
            'Cookie': '_ga=GA1.2.1703807638.1571679662; '
                      '_gid=GA1.2.1281852873.1571896806; '
                      f'PHPSESSID={phpsessid_};'
                      '_gat_gtag_UA_38993877_1=1',
            'DNT': '1',
            'Host': 'www.betonsuccess.ru',
            'Origin': 'https://www.betonsuccess.ru',
            'referer': 'https://www.betonsuccess.ru/sub/29691/BskBetsPin.B.L/picks/',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': f'{userag}'
        }


def my_spp2(input_spp2):
    js = '''
    var hexcase = 0;

    spp2('hexcode');

    function spp2(input) {
            var subp = (parseInt(input) + parseInt(1291)) * 2;
            var param2 = hex_md5(subp + '9ae5gae965gae95rgaerg9rg6ae8r7698aer7g');
            return param2;
    }

    function hex_md5(s) {
            return rstr2hex(rstr_md5(str2rstr_utf8(s)));
    }

    function rstr_md5(s) {
            return binl2rstr(binl_md5(rstr2binl(s), s.length * 8));
    }

    function rstr2binl(input) {
            var output = Array(input.length >> 2);
            for (var i = 0; i < output.length; i++)
            output[i] = 0;
            for (var i = 0; i < input.length * 8; i += 8)
            output[i >> 5] |= (input.charCodeAt(i / 8) & 0xFF) << (i % 32);
            return output;
    }

    function rstr2hex(input) {
            try {
                    hexcase
            } catch (e) {
                    hexcase = 0;
            }
            var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
            var output = "";
            var x;
            for (var i = 0; i < input.length; i++) {
                    x = input.charCodeAt(i);
                    output += hex_tab.charAt((x >>> 4) & 0x0F) + hex_tab.charAt(x & 0x0F);
            }
            return output;
    }

    function str2rstr_utf8(input) {
            var output = "";
            var i = -1;
            var x, y;

            while (++i < input.length) { /* Decode utf-16 surrogate pairs */
                    x = input.charCodeAt(i);
                    y = i + 1 < input.length ? input.charCodeAt(i + 1) : 0;
                    if (0xD800 <= x && x <= 0xDBFF && 0xDC00 <= y && y <= 0xDFFF) {
                            x = 0x10000 + ((x & 0x03FF) << 10) + (y & 0x03FF);
                            i++;
                    }

                    /* Encode output as utf-8 */
                    if (x <= 0x7F) output += String.fromCharCode(x);
                    else if (x <= 0x7FF) output += String.fromCharCode(0xC0 | ((x >>> 6) & 0x1F), 0x80 | (x & 0x3F));
                    else if (x <= 0xFFFF) output += String.fromCharCode(0xE0 | ((x >>> 12) & 0x0F), 0x80 | ((x >>> 6) & 0x3F), 0x80 | (x & 0x3F));
                    else if (x <= 0x1FFFFF) output += String.fromCharCode(0xF0 | ((x >>> 18) & 0x07), 0x80 | ((x >>> 12) & 0x3F), 0x80 | ((x >>> 6) & 0x3F), 0x80 | (x & 0x3F));
            }
            return output;
    }

    function binl2rstr(input) {
            var output = "";
            for (var i = 0; i < input.length * 32; i += 8)
            output += String.fromCharCode((input[i >> 5] >>> (i % 32)) & 0xFF);
            return output;
    }

    function binl_md5(x, len) { /* append padding */
            x[len >> 5] |= 0x80 << ((len) % 32);
            x[(((len + 64) >>> 9) << 4) + 14] = len;

            var a = 1732584193;
            var b = -271733879;
            var c = -1732584194;
            var d = 271733878;

            for (var i = 0; i < x.length; i += 16) {
                    var olda = a;
                    var oldb = b;
                    var oldc = c;
                    var oldd = d;

                    a = md5_ff(a, b, c, d, x[i + 0], 7, -680876936);
                    d = md5_ff(d, a, b, c, x[i + 1], 12, -389564586);
                    c = md5_ff(c, d, a, b, x[i + 2], 17, 606105819);
                    b = md5_ff(b, c, d, a, x[i + 3], 22, -1044525330);
                    a = md5_ff(a, b, c, d, x[i + 4], 7, -176418897);
                    d = md5_ff(d, a, b, c, x[i + 5], 12, 1200080426);
                    c = md5_ff(c, d, a, b, x[i + 6], 17, -1473231341);
                    b = md5_ff(b, c, d, a, x[i + 7], 22, -45705983);
                    a = md5_ff(a, b, c, d, x[i + 8], 7, 1770035416);
                    d = md5_ff(d, a, b, c, x[i + 9], 12, -1958414417);
                    c = md5_ff(c, d, a, b, x[i + 10], 17, -42063);
                    b = md5_ff(b, c, d, a, x[i + 11], 22, -1990404162);
                    a = md5_ff(a, b, c, d, x[i + 12], 7, 1804603682);
                    d = md5_ff(d, a, b, c, x[i + 13], 12, -40341101);
                    c = md5_ff(c, d, a, b, x[i + 14], 17, -1502002290);
                    b = md5_ff(b, c, d, a, x[i + 15], 22, 1236535329);

                    a = md5_gg(a, b, c, d, x[i + 1], 5, -165796510);
                    d = md5_gg(d, a, b, c, x[i + 6], 9, -1069501632);
                    c = md5_gg(c, d, a, b, x[i + 11], 14, 643717713);
                    b = md5_gg(b, c, d, a, x[i + 0], 20, -373897302);
                    a = md5_gg(a, b, c, d, x[i + 5], 5, -701558691);
                    d = md5_gg(d, a, b, c, x[i + 10], 9, 38016083);
                    c = md5_gg(c, d, a, b, x[i + 15], 14, -660478335);
                    b = md5_gg(b, c, d, a, x[i + 4], 20, -405537848);
                    a = md5_gg(a, b, c, d, x[i + 9], 5, 568446438);
                    d = md5_gg(d, a, b, c, x[i + 14], 9, -1019803690);
                    c = md5_gg(c, d, a, b, x[i + 3], 14, -187363961);
                    b = md5_gg(b, c, d, a, x[i + 8], 20, 1163531501);
                    a = md5_gg(a, b, c, d, x[i + 13], 5, -1444681467);
                    d = md5_gg(d, a, b, c, x[i + 2], 9, -51403784);
                    c = md5_gg(c, d, a, b, x[i + 7], 14, 1735328473);
                    b = md5_gg(b, c, d, a, x[i + 12], 20, -1926607734);

                    a = md5_hh(a, b, c, d, x[i + 5], 4, -378558);
                    d = md5_hh(d, a, b, c, x[i + 8], 11, -2022574463);
                    c = md5_hh(c, d, a, b, x[i + 11], 16, 1839030562);
                    b = md5_hh(b, c, d, a, x[i + 14], 23, -35309556);
                    a = md5_hh(a, b, c, d, x[i + 1], 4, -1530992060);
                    d = md5_hh(d, a, b, c, x[i + 4], 11, 1272893353);
                    c = md5_hh(c, d, a, b, x[i + 7], 16, -155497632);
                    b = md5_hh(b, c, d, a, x[i + 10], 23, -1094730640);
                    a = md5_hh(a, b, c, d, x[i + 13], 4, 681279174);
                    d = md5_hh(d, a, b, c, x[i + 0], 11, -358537222);
                    c = md5_hh(c, d, a, b, x[i + 3], 16, -722521979);
                    b = md5_hh(b, c, d, a, x[i + 6], 23, 76029189);
                    a = md5_hh(a, b, c, d, x[i + 9], 4, -640364487);
                    d = md5_hh(d, a, b, c, x[i + 12], 11, -421815835);
                    c = md5_hh(c, d, a, b, x[i + 15], 16, 530742520);
                    b = md5_hh(b, c, d, a, x[i + 2], 23, -995338651);

                    a = md5_ii(a, b, c, d, x[i + 0], 6, -198630844);
                    d = md5_ii(d, a, b, c, x[i + 7], 10, 1126891415);
                    c = md5_ii(c, d, a, b, x[i + 14], 15, -1416354905);
                    b = md5_ii(b, c, d, a, x[i + 5], 21, -57434055);
                    a = md5_ii(a, b, c, d, x[i + 12], 6, 1700485571);
                    d = md5_ii(d, a, b, c, x[i + 3], 10, -1894986606);
                    c = md5_ii(c, d, a, b, x[i + 10], 15, -1051523);
                    b = md5_ii(b, c, d, a, x[i + 1], 21, -2054922799);
                    a = md5_ii(a, b, c, d, x[i + 8], 6, 1873313359);
                    d = md5_ii(d, a, b, c, x[i + 15], 10, -30611744);
                    c = md5_ii(c, d, a, b, x[i + 6], 15, -1560198380);
                    b = md5_ii(b, c, d, a, x[i + 13], 21, 1309151649);
                    a = md5_ii(a, b, c, d, x[i + 4], 6, -145523070);
                    d = md5_ii(d, a, b, c, x[i + 11], 10, -1120210379);
                    c = md5_ii(c, d, a, b, x[i + 2], 15, 718787259);
                    b = md5_ii(b, c, d, a, x[i + 9], 21, -343485551);

                    a = safe_add(a, olda);
                    b = safe_add(b, oldb);
                    c = safe_add(c, oldc);
                    d = safe_add(d, oldd);
            }
            return Array(a, b, c, d);
    }

    function safe_add(x, y) {
            var lsw = (x & 0xFFFF) + (y & 0xFFFF);
            var msw = (x >> 16) + (y >> 16) + (lsw >> 16);
            return (msw << 16) | (lsw & 0xFFFF);
    }

    function md5_cmn(q, a, b, x, s, t) {
            return safe_add(bit_rol(safe_add(safe_add(a, q), safe_add(x, t)), s), b);
    }

    function md5_ff(a, b, c, d, x, s, t) {
            return md5_cmn((b & c) | ((~b) & d), a, b, x, s, t);
    }

    function md5_gg(a, b, c, d, x, s, t) {
            return md5_cmn((b & d) | (c & (~d)), a, b, x, s, t);
    }

    function md5_hh(a, b, c, d, x, s, t) {
            return md5_cmn(b ^ c ^ d, a, b, x, s, t);
    }

    function md5_ii(a, b, c, d, x, s, t) {
            return md5_cmn(c ^ (b | (~d)), a, b, x, s, t);
    }

    function bit_rol(num, cnt) {
            return (num << cnt) | (num >>> (32 - cnt));
    }
    '''.replace('hexcode', input_spp2)
    result = eval_js(js)
    return result


def get_recaptcha_response(googlekey, page_url, inv=0):
    url_req = 'http://rucaptcha.com/in.php'

    in_payload = {'key': sets["key"],
                  'method': 'userrecaptcha',
                  'googlekey': googlekey,
                  'pageurl': page_url,
                  'invisible': inv
                  }
    for att in range(3):
        res = 0
        request = get(url_req, proxies=sets["g_prox"], params=in_payload)
        captcha_id = request.text.split('|')[1]

        sleep(10)
        response = 'NO|BAD'
        for rep in range(40):
            url_res = 'http://rucaptcha.com/res.php'
            in_payload = {'key': sets["key"],
                          'action': 'get',
                          'id': captcha_id
                          }
            response = get(url_res, params=in_payload)
            if response.text == 'CAPCHA_NOT_READY':
                sleep(5)
            elif response.text == 'ERROR_CAPTCHA_UNSOLVABLE':
                res = 1
                break
            else:
                break

        if res == 0:
            break
    return response.text.split('|')[1]


def auth_with_google(g_soup, u_auth):
    try:
        googlekey = g_soup.find('div', class_='g-recaptcha')
        if googlekey:
            googlekey = googlekey.get('data-sitekey')
            csrf_val = g_soup.find('input', {'name': 'csrf_token'})['value']
            hash_val = g_soup.find('input', {'name': 'user_hash'})['value']
            g_recaptcha_response = get_recaptcha_response(googlekey, 'https://www.betonsuccess.ru/login/failed')
            payload = "user_name=%s&user_password=%s&g-recaptcha-response=%s&user_hash=%s&csrf_token=%s" % \
                      (sets['user'], sets['pass'], g_recaptcha_response, hash_val, csrf_val)
            g_page = session.post(u_auth, data=payload, proxies=sets["g_prox"],
                                  headers=get_headers('post', useragent, phpsessid), allow_redirects=True)
            g_html = g_page.text
            g_soup = BeautifulSoup(g_html, 'lxml')
            user_info = g_soup.find('div', class_='user_info')
            if user_info is not None:
                return [True, user_info]
            else:
                return [False]
        else:
            return [False]
    except:
        log('Не могу авторизоваться с помошью рукапчи.')
        return [False]


def authorization():
    log('Авторизация . . .')
    try:
        url_auth = 'https://www.betonsuccess.ru/login577.php'
        payload = f'user_name={sets["user"]}&user_password={sets["pass"]}&user_hash={hash_v}&csrf_token={csrf_v}'
        page_ = session.post(url_auth, data=payload, proxies=sets["g_prox"],
                             headers=get_headers('post', useragent, phpsessid), allow_redirects=True)
        html_ = page_.text
        soup_ = BeautifulSoup(html_, 'lxml')
        user_info = soup_.find('div', class_='user_info')
        if user_info is not None:
            log('Авторизация выполнена! > ' + user_info.text.replace('\n', '').strip())
            return True
        else:
            awg = auth_with_google(soup_, url_auth)
            if awg[0]:
                log('Авторизация выполнена через рукапчу! > ' + awg[1].text.replace('\n', '').strip())
                return True
            log('Авторизация НЕ выполнена!')
            return False
    except:
        log('Не могу авторизоваться. Проблемы с прокси или с интернетом.')
        return False


def data_sender(last_n):
    try:
        for md in pw.now_data(last_n):
            if md[1]:
                send_telegram(md[0], 0, 'Новый прогноз')
                send_email(md[0], 0)
            else:
                send_email(md[0])
                send_telegram(md[0])
    except:
        log('Что-то пошло не так. Попробуем снова.')


def ajax_downloader(last_n):
    log('Извлечение новых прогнозов . . .')
    try:
        page_ = session.get(sets['url'], headers=get_headers('picks', useragent, phpsessid),
                            proxies=sets["g_prox"], allow_redirects=False)

        pick_id = []
        html_ = page_.content.decode('cp1251')
        soup_ = BeautifulSoup(html_, 'lxml')
        subs_picks = soup_.find('div', class_='subs_picks')
        sitekey = subs_picks.text.split('rcv2_|')[1].split('|')[0]

        section = soup_.find('div', class_='section')
        table = section.findAll('div', class_='pick_item')

        if table:
            for tbl in table:
                get_id = tbl.findParent('div').get('id')
                if get_id is not None:
                    hide_event = tbl.findAll('td', class_='event')
                    if hide_event is not None:
                        hide_event = hide_event[1].text
                    pick_id.append([get_id.split('_')[1], hide_event])
                else:
                    pick_id = None
            if pick_id is not None:
                text = ''
                for p_i in pick_id:
                    param1 = p_i[0]
                    param2 = my_spp2(param1)

                    if p_i[1] == 'Событие скрыто':
                        url_picks = 'https://www.betonsuccess.ru/openpicksub/?' \
                                    f'PHPSESSID={phpsessid}&JsHttpRequest=15719297063500-xml'
                        param4 = get_recaptcha_response(sitekey, url_picks)
                        payload = f'{sets["ajax_par1"]}={param1}&{sets["ajax_par2"]}={param2}&{sets["ajax_par4"]}={param4}&ua={useragent}'
                    else:
                        url_picks = 'https://www.betonsuccess.ru/showpicksub/?' \
                                    f'PHPSESSID={phpsessid}&JsHttpRequest=15719297063500-xml'
                        payload = f'{sets["ajax_par1"]}={param1}&{sets["ajax_par2"]}={param2}'
                    page_ = session.post(url_picks, data=payload, proxies=sets["g_prox"],
                                         headers=get_headers('js', useragent, phpsessid), allow_redirects=False)
                    ajax_text = page_.text
                    ajax_data = loads(ajax_text)['js'][sets["ajax_par3"]]
                    if ajax_data == 'RCV2':
                        param4 = get_recaptcha_response(sitekey, url_picks, 1)
                        payload = f'{sets["ajax_par1"]}={param1}&{sets["ajax_par2"]}={param2}&{sets["ajax_par4"]}={param4}&ua={useragent}&v2=1'
                        page_ = session.post(url_picks, data=payload, proxies=sets["g_prox"],
                                             headers=get_headers('js', useragent, phpsessid), allow_redirects=False)
                        ajax_text = page_.text
                        ajax_data = loads(ajax_text)['js'][sets["ajax_par3"]]
                    soup_ = BeautifulSoup(ajax_data, 'lxml')
                    pick_item = soup_.find('div', class_='pick_item')
                    tbl_tr = pick_item.findAll('table')[1].findAll('tr')
                    if tbl_tr[0].find('img') is not None:
                        img_app = str(tbl_tr[0].find('img')['src']).replace('.png', '-app.png')
                        url_img = 'https://www.betonsuccess.ru' + img_app
                        pw.record_to_db(url_img, 1, last_n)
                    else:
                        for t1, t2 in zip(tbl_tr[0].findAll('td'), tbl_tr[1].findAll('td')):
                            text += t1.text.strip() + ': ' + t2.text.strip() + '\n'
                        text += '\n'
                        pw.record_to_db(text, 0, last_n)
                log('Прогнозы получены!')
                return True
            else:
                log('Прогнозы не получены! Что-то пошло не так, попробуем еще через некоторое время.')
                return False
        else:
            log('Прогнозы не получены! Что-то пошло не так, попробуем еще через некоторое время.')
            return False
    except:
        log('Не могу получить прогнозы. Проблемы либо с прокси либо с интернетом либо с сайтом.')
        return False


def send_email(message, mode=1):
    try:
        log('Отправка прогноза на почту: ' + sets["send_mail_toaddr"])
        msg = MIMEMultipart()
        msg['From'] = sets["send_mail_login"]
        msg['To'] = sets["send_mail_toaddr"]
        msg['Subject'] = "Прогноз"

        body = message
        html_body = '<table><tr><td><b>Новый прогноз</b></td></tr><tr><td>' \
                    f'<img alt="" src="{message}"></td></tr></table>'
        if mode:
            msg.attach(MIMEText(body, 'plain'))
        else:
            msg.attach(MIMEText(html_body, 'html'))
        text = msg.as_string()

        server = SMTP_SSL(sets["send_mail_host"], sets["send_mail_port"])
        # server.starttls()
        server.login(sets["send_mail_login"], sets["send_mail_pass"])
        server.auth_plain()
        server.sendmail(sets["send_mail_login"], sets["send_mail_toaddr"], text)
        server.quit()
    except:
        log('Уведомление не отправлено. Проблема с интернетом или с сервером почты.')


def send_telegram(msg, mode=1, caption=''):
    try:
        if mode:
            url_ = f'https://api.telegram.org/bot{sets["tele_token"]}/sendMessage'
            data = {'chat_id': sets["tele_chat_id"], 'text': msg}
        else:
            url_ = f'https://api.telegram.org/bot{sets["tele_token"]}/sendPhoto'
            data = {'chat_id': sets["tele_chat_id"], 'photo': msg, 'caption': caption}
        post(url_, data=data, proxies=sets["tele_proxi"])
    except:
        log('Уведомление в Телеграм не отправлено. Проблемы с прокси или с интернетом.')


def notification_mail():
    log('Проверка почты на поступлнение новых прогнозов . . .')
    try:
        box = IMAP4_SSL(sets["notif_mail_host"], sets["notif_mail_port"])
        box.login(sets["notif_mail_login"], sets["notif_mail_pass"])
        box.select()
        typ, data = box.search(None, '(UNSEEN)')
        status = False
        if data[0].split():
            typ, data = box.fetch(data[0].split()[-1], '(RFC822)')
            mail = mailparser.parse_from_bytes(data[0][1])
            if mail.subject.find(sets["notif_mail_compare"]) != -1:
                log('Поступил новый прогноз')
                status = True
            else:
                log('Нет новых прогнозов')
                status = False
        else:
            log('Нет новых прогнозов')
            status = False
        box.close()
        box.logout()
        return status
    except:
        log('Не могу проверить почту. Проблема с интернетом или с сервером почты.')
        return False


def read_file_settings():
    try:
        settings = {
            'url': '',
            'user': '',
            'pass': '',
            'tele_token': '',
            'tele_proxi': '',
            'tele_chat_id': '',
            'send_mail_host': '',
            'send_mail_port': '',
            'send_mail_login': '',
            'send_mail_pass': '',
            'send_mail_toaddr': '',
            'notif_mail_host': '',
            'notif_mail_port': '',
            'notif_mail_login': '',
            'notif_mail_pass': '',
            'notif_mail_compare': '',
            'period_mail': '',
            'period_auth': '',
            'period_dwnd': '',
            'ajax_par1': '',
            'ajax_par2': '',
            'ajax_par3': '',
            'ajax_par4': '',
            'key': '',
            'g_prox': ''
        }

        file = open('settings.txt', 'r', encoding='utf-8')
        res = file.readlines()
        for f in res:
            linestr = f.replace('\n', '')
            if linestr != '' and linestr.find('#') == -1:
                key = linestr.split('=')[0]
                value = linestr.split('=')[1]
                settings[key] = value

        if settings['tele_proxi'].find("https://") != -1:
            settings['tele_proxi'] = {'https': settings['tele_proxi']}
        else:
            settings['tele_proxi'] = ''
        if settings['g_prox'].find("https://") != -1:
            settings['g_prox'] = {'https': settings['g_prox']}
        else:
            settings['g_prox'] = ''
        settings['send_mail_port'] = int(settings['send_mail_port'])
        settings['notif_mail_port'] = int(settings['notif_mail_port'])
        settings['period_mail'] = int(settings['period_mail'])
        settings['period_auth'] = int(settings['period_auth'])
        settings['period_dwnd'] = int(settings['period_dwnd'])

        return settings
    except:
        log('Не удалось прочитать файл настроек settings.txt\n'
            'Либо файл не найден, либо файл заполнен не корректно!')
        return False


class InitDB:

    def __init__(self):
        self.Prognoz.create_table()

    class Prognoz(Model):
        data = CharField(unique=True)
        type = IntegerField()
        iden = IntegerField()

        class Meta:
            database = SqliteDatabase('bet.db')

    def record_to_db(self, dt, tp, it=1):
        try:
            new_record = self.Prognoz(data=dt, type=tp, iden=it)
            new_record.save()
            return True
        except IntegrityError:
            return False

    def delete_db(self, lim):
        dl = self.Prognoz.select().limit(lim)
        delrow = self.Prognoz.delete().where(self.Prognoz.id << dl)
        delrow.execute()

    def last_rec_ident(self):
        try:
            idn = self.Prognoz.select().order_by(self.Prognoz.id.desc()).get().iden
            return idn
        except DoesNotExist:
            return 0

    def now_data(self, iden):
        mass = []
        for person in self.Prognoz.select().where(self.Prognoz.iden == iden):
            mass.append([person.data, person.type])
        return mass


sets = read_file_settings()
if not sets:
    exit()

pw = InitDB()
ua = UserAgent()
useragent = ua.chrome
session = Session()
url_start = 'https://www.betonsuccess.ru/'

# Получение Cookie и других параметров
page = session.get(url_start, headers=get_headers('bet', useragent), proxies=sets["g_prox"], allow_redirects=False)
phpsessid = page.headers['Set-Cookie'].split(';')[0].split('=')[1]
html = page.text
soup = BeautifulSoup(html, 'lxml')
csrf_v = soup.find('input', {'name': 'csrf_token'})['value']
hash_v = soup.find('input', {'name': 'user_hash'})['value']

# Авторизация
while 1:
    auth_valid = authorization()

    if auth_valid:
        while 1:
            status = 1
            if notification_mail():
                last_num = pw.last_rec_ident() + 1
                status = ajax_downloader(last_num)
                for i in range(3):
                    if status:
                        break
                    else:
                        log('Подождем ' + str(sets["period_dwnd"]) + ' сек. перед повторным извлечением прогнозов')
                        sleep(sets["period_dwnd"])
                        status = ajax_downloader(last_num)
                if last_num > 60:
                    pw.delete_db(30)
                data_sender(last_num)
            log('Подождем ' + str(sets["period_mail"]) + ' сек. и снова проверим имеются ли новые прогнозы')
            sleep(sets["period_mail"])
    else:
        log('Подождем ' + str(sets["period_auth"]) + ' сек. и попытаемся снова авторизоваться')
        sleep(sets["period_auth"])
