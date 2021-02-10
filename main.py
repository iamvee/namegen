#!/usr/bin/env python3

""" Namegen - Generate random names """

import sys
import time

def choice(objs):
    """ Select a random item from a list """
    indx = int(time.time() * 1_000_000) % len(objs)
    return objs[indx]

FOODS = [
    {'en': 'anaar-e', 'fa': 'انار'},
    {'en': 'azgil-e', 'fa': 'ازگیل'},
    {'en': 'albaloo-ye', 'fa': 'آلبالوی'},
    {'en': 'aloo-ye', 'fa': 'آلوی'},
    {'en': 'ananas-e', 'fa': 'آناناس'},
    {'en': 'anjir-e', 'fa': 'انجیر'},
    {'en': 'angoor-e', 'fa': 'انگور'},
    {'en': 'avokaado-ye', 'fa': 'آوکادوی'},
    {'en': 'badoom-e', 'fa': 'بادوم'},
    {'en': 'baalang-e', 'fa': 'بالنگ'},
    {'en': 'baloot-e', 'fa': 'بلوط'},
    {'en': 'beh-e', 'fa': 'به'},
    {'en': 'porteghal-e', 'fa': 'پرتغال'},
    {'en': 'peste-ye', 'fa': 'پستهٔ'},
    {'en': 'toranj-e', 'fa': 'ترنج'},
    {'en': 'tamr hendi-ye', 'fa': 'تمر هندی'},
    {'en': 'anbe-ye', 'fa': 'انبهٔ'},
    {'en': 'tameshk-e', 'fa': 'تمشک'},
    {'en': 'toot farangi-ye', 'fa': 'توت فرنگی'},
    {'en': 'toot-e', 'fa': 'توت'},
    {'en': 'kharboze-ye', 'fa': 'خربزهٔ'},
    {'en': 'khormaloo-ye', 'fa': 'خرمالوی'},
    {'en': 'khorma-ye', 'fa': 'خرمای'},
    {'en': 'khiyar-e', 'fa': 'خیار'},
    {'en': 'zoghal akhte-ye', 'fa': 'ذغال اختهٔ'},
    {'en': 'zalzalak-e', 'fa': 'زلزلک'},
    {'en': 'zard aloo-ye', 'fa': 'زردآلوی'},
    {'en': 'zereshk-e', 'fa': 'زرشک'},
    {'en': 'zeytoon-e', 'fa': 'زیتون'},
    {'en': 'senjed-e', 'fa': 'سنجد'},
    {'en': 'sib-e', 'fa': 'سیب'},
    {'en': 'shaatoot-e', 'fa': 'شاتوت'},
    {'en': 'shaftaaloo-ye', 'fa': 'شفتالوی'},
    {'en': 'shalil-e', 'fa': 'شلیل'},
    {'en': 'taalebi-e', 'fa': 'طالبی'},
    {'en': 'fandogh-e', 'fa': 'فندق'},
    {'en': 'gheisi-e', 'fa': 'قیسی'},
    {'en': 'komboze-ye', 'fa': 'کمبوزهٔ'},
    {'en': 'kivi-ye', 'fa': 'کیوی'},
    {'en': 'gerdoo-ye', 'fa': 'گردوی'},
    {'en': 'grip froot-e', 'fa': 'گریپ فروت'},
    {'en': 'golabi-ye', 'fa': 'گلابی'},
    {'en': 'alooche-ye', 'fa': 'آلوچهٔ'},
    {'en': 'gilas-e', 'fa': 'گیلاس'},
    {'en': 'limoo torsh-e', 'fa': 'لیمو ترش'},
    {'en': 'limoo shirin-e', 'fa': 'لیمو شیرین'},
    {'en': 'nargil-e', 'fa': 'نارگیل'},
    {'en': 'movz-e', 'fa': 'موز'},
    {'en': 'narengi-e', 'fa': 'نارنگی'},
    {'en': 'holoo-ye', 'fa': 'هلوی'},
    {'en': 'hendoone-ye', 'fa': 'هندوانهٔ'},
    {'en': 'karafs-e', 'fa': 'کرفس'},
    {'en': 'shivid-e', 'fa': 'شوید'},
    {'en': 'torob-e', 'fa': 'ترب'},
    {'en': 'piyaz-e', 'fa': 'پیاز'},
    {'en': 'sir-e', 'fa': 'سیر'},
    {'en': 'havij-e', 'fa': 'هویج'},
    {'en': 'nokhod-e', 'fa': 'نخود'},
    {'en': 'loobiya sefid-e', 'fa': 'لوبی سفید'},
    {'en': 'loobiya chiti-ye', 'fa': 'لوبیا چیتی'},
    {'en': 'ghoore-ye', 'fa': 'غورهٔ'},
    {'en': 'kalam-e', 'fa': 'کلم'},
    {'en': 'kadoo halvaee-ye', 'fa': 'کدو حلوایی'},
    {'en': 'delester-e', 'fa': 'دلستر'},
    {'en': 'nooshabe-ye', 'fa': 'نوشابهٔ'},
    {'en': 'panir-e', 'fa': 'پنیر'},
    {'en': 'tah chin-e', 'fa': 'ته چین'},
    {'en': 'ton maahi-ye', 'fa': 'تن ماهی'},
    {'en': 'faloode-ye', 'fa': 'فالودهٔ'},
    {'en': 'shir berenj-e', 'fa': 'شیر برنج'}
]

ADJS = [
    {'en': 'ashofteh', 'fa': 'آشفته'},
    {'en': 'aloodeh', 'fa': 'آلوده'},
    {'en': 'afsordeh', 'fa': 'افسرده'},
    {'en': 'motor savar', 'fa': 'موتور سوار'},
    {'en': 'bargozideh', 'fa': 'برگزیده'},
    {'en': 'pokhteh', 'fa': 'پخته'},
    {'en': 'parvardeh', 'fa': 'پرورده'},
    {'en': 'shargاi', 'fa': 'شرقی'},
    {'en': 'parishan', 'fa': 'پریشان'},
    {'en': 'pichideh', 'fa': 'پیچیده'},
    {'en': 'pishrafteh', 'fa': 'پیشرفته'},
    {'en': 'gharb zadeh', 'fa': 'غرب زده'},
    {'en': 'tafteh', 'fa': 'تافته'},
    {'en': 'taftideh', 'fa': 'تفتیده'},
    {'en': 'chasbideh', 'fa': 'چسبیده'},
    {'en': 'khamideh', 'fa': 'خمیده'},
    {'en': 'kharaaman', 'fa': 'خرامان'},
    {'en': 'chegher', 'fa': 'چغر'},
    {'en': 'khalideh', 'fa': 'خلیده'},
    {'en': 'khaste', 'fa': 'خسته'},
    {'en': 'dars khaandeh', 'fa': 'درس خوانده'},
    {'en': 'deldadeh', 'fa': 'دلداده'},
    {'en': 'delpazir', 'fa': 'دلپذیر'},
    {'en': 'dom borideh', 'fa': 'دم بریده'},
    {'en': 'rahideh', 'fa': 'رهیده'},
    {'en': 'ablah', 'fa': 'ابله'},
    {'en': 'rang parideh', 'fa': 'رنگ پریده'},
    {'en': 'resideh', 'fa': 'رسیده'},
    {'en': 'zereh push', 'fa': 'زره پوش'},
    {'en': 'zabanzad', 'fa': 'زبانزد'},
    {'en': 'zir afkan', 'fa': 'زیر افکن'},
    {'en': 'zhoolideh', 'fa': 'ژولیده'},
    {'en': 'salkhordeh', 'fa': 'سالخورده'},
    {'en': 'sar afkandeh', 'fa': 'سرافکنده'},
    {'en': 'sar sepordeh', 'fa': 'سر سپرده'},
    {'en': 'sar shekasteh', 'fa': 'سر شکسته'},
    {'en': 'sar gashteh', 'fa': 'سر گشته'},
    {'en': 'sookhteh', 'fa': 'سوخته'},
    {'en': 'sharab zadeh', 'fa': 'شراب زده'},
    {'en': 'shoorideh', 'fa': 'شوریده'},
    {'en': 'shifteh', 'fa': 'شیفته'},
    {'en': 'farrokhzad', 'fa': 'فرخزاد'},
    {'en': 'farsoodeh', 'fa': 'فرسوده'},
    {'en': 'farifteh', 'fa': 'فریفته'},
    {'en': 'foroo_heshteh', 'fa': 'فروهشته'},
    {'en': 'kar azmoodeh', 'fa': 'کار آزموده'},
    {'en': 'kar amad', 'fa': 'کارآمد'},
    {'en': 'gosasteh', 'fa': 'گسسته'},
    {'en': 'gozideh', 'fa': 'گزیده'},
    {'en': 'gomashteh', 'fa': 'گماشته'},
    {'en': 'legam gosikhteh', 'fa': 'لگام گسیخته'},
    {'en': 'miyaneh ro', 'fa': 'میانه رو'},
    {'en': 'modabber', 'fa': 'مدبر'},
    {'en': 'naadaan', 'fa': 'نادان'},
    {'en': 'sharlatan', 'fa': 'شارلاتان'},
    {'en': 'naz parvardeh', 'fa': 'ناز پرورده'},
    {'en': 'vabasteh', 'fa': 'وابسته'},
    {'en': 'varafteh', 'fa': 'وارفته'},
    {'en': 'varasteh', 'fa': 'وارسته'},
    {'en': 'varparideh', 'fa': 'ورپریده'},
    {'en': 'varshekasteh', 'fa': 'ورشکسته'},
    {'en': 'haraasaan', 'fa': 'هراسان'},
    {'en': 'bi_namoos', 'fa': 'بی ناموس'},
    {'en': 'khak_barsar', 'fa': 'خاک برسر'},
    {'en': 'oghde_ee', 'fa': 'عقده‌ای'},
    {'en': 'kheng', 'fa': 'خنگ'},
    {'en': 'dana', 'fa': 'دانا'},
    {'en': 'khoshhal', 'fa': 'خوشحال'},
    {'en': 'kheng', 'fa': 'خنگ'},
    {'en': 'ghozmit', 'fa': 'قزمیت'},
    {'en': 'afsordeh_sima', 'fa': 'افسرده سیما'},
    {'en': 'boland parvaz', 'fa': 'بلند پرواز'},
    {'en': 'delsard', 'fa': 'دلسرد'},
    {'en': 'kaftar baaz', 'fa': 'کفترباز'},
    {'en': 'chabok', 'fa': 'چابک'},
    {'en': 'khafan', 'fa': 'خفن'},
    {'en': 'daneshmand', 'fa': 'دانشمند'},
    {'en': 'data scientist', 'fa': 'دیتا ساینتیست'},
    {'en': 'mofles', 'fa': 'مفلس'},
    {'en': 'dordi_kash', 'fa': 'دردی کش'},
    {'en': 'sharaab_zadeh', 'fa': 'شراب زده'},
    {'en': 'kharaab', 'fa': 'خراب'},
    {'en': 'oskol', 'fa': 'اسکل'},
    {'en': 'gij', 'fa': 'گیج'}
]

def gen(lang='fa') -> str:
    """ Generates a name and returns that as a string """
    rand_name, rand_adjective = choice(FOODS), choice(ADJS)
    return f"{rand_name[lang]} {rand_adjective[lang]}"

if __name__ == '__main__':
    flags = sys.argv[1:]

    if '-n' in flags:
        ind = flags.index('-n')
        count = int(flags.pop(ind+1))
        flags.remove('-n')
    else:
        count = 1

    for i in range(count):
        name, adjective = choice(FOODS), choice(ADJS)
        flags = ['fa', 'en'] if not flags else flags
        if 'fa' in flags:
            print(gen('fa'))

        if 'en' in flags:
            print(gen('en'))
