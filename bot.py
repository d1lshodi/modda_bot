import logging
from aiogram.types import *
from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from btn import *


API_TOKEN = "7285836989:AAHNvMFz2icBuXxK3LsvaociTtiPyzbxpU4"
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
import logging

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.answer("Assalomu alekum 👤",)
    await message.answer('Bizni Karupsiyaga Qarshi kurashish Botimizga xush Kelibsiz🙂',reply_markup=kb)


@dp.message_handler(text='1-bob. Umumiy qoidalar 📜')
async def start(message:types.Message):
    await message.answer('Modalarni Oqish Uchun Menyudan Birini tanlang',reply_markup=menyu_button)

@dp.message_handler(text='2-bob. Korrupsiyaga qarshi kurashish bo‘yicha faoliyatni amalga oshirish 📜')
async def start(message:types.Message):
    await message.answer('Modalarni Oqish Uchun Menyudan Birini tanlang',reply_markup=menyuiki_Button)

@dp.message_handler(text='3-bob. Korrupsiyaga qarshi kurashish sohasida huquqiy ong va huquqiy madaniyatni yuksaltirish 📜')
async def start(message:types.Message):
    await message.answer('Modalarni Oqish Uchun Menyudan Birini tanlang',reply_markup=menyuch_Button)

@dp.message_handler(text='4-bob. Korrupsiyaning oldini olishga doir chora-tadbirlar 📜')
async def start(message:types.Message):
    await message.answer('Modalarni Oqish Uchun Menyudan Birini tanlang',reply_markup=menyutor_Button)

@dp.message_handler(text='5-bob. Korrupsiyaga oid huquqbuzarliklarni aniqlash, ularga chek qo‘yish, javobgarlikning muqarrarligi 📜')
async def start(message:types.Message):
    await message.answer('Modalarni Oqish Uchun Menyudan Birini tanlang',reply_markup=menyubesh_Button)

@dp.message_handler(text='6-bob. Yakunlovchi qoidalar 📜')
async def start(message:types.Message):
    await message.answer('Modalarni Oqish Uchun Menyudan Birini tanlang',reply_markup=menyuiki_Button)


@dp.message_handler(text='1 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''1-modda. Ushbu Qonunning maqsadi
Ushbu Qonunning maqsadi korrupsiyaga qarshi kurashish sohasidagi munosabatlarni tartibga solishdan iborat.''',reply_markup=menyu_button)


@dp.message_handler(text='2 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''2-modda. Korrupsiyaga qarshi kurashish to‘g‘risidagi qonunchilik
Korrupsiyaga qarshi kurashish to‘g‘risidagi qonunchilik ushbu Qonun va boshqa qonunchilik hujjatlaridan iboratdir.
Agar O‘zbekiston Respublikasining xalqaro shartnomasida korrupsiyaga qarshi kurashish to‘g‘risidagi qonunchilikda nazarda tutilganidan boshqacha qoidalar belgilangan bo‘lsa, xalqaro shartnoma qoidalari qo‘llaniladi.
(2-modda O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)''',reply_markup=menyu_button)

@dp.message_handler(text='3 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''3-modda. Asosiy tushunchalar
Ushbu Qonunda quyidagi asosiy tushunchalar qo‘llaniladi:
korrupsiya — shaxsning o‘z mansab yoki xizmat mavqeyidan shaxsiy manfaatlarini yoxud o‘zga shaxslarning manfaatlarini ko‘zlab moddiy yoki nomoddiy naf olish maqsadida qonunga xilof ravishda foydalanishi, xuddi shuningdek bunday nafni qonunga xilof ravishda taqdim etish;
Oldingi tahrirga qarang.
korrupsiyaga oid huquqbuzarlik — korrupsiya alomatlariga ega bo‘lgan, sodir etilganligi uchun qonunchilikda javobgarlik nazarda tutilgan qilmish;
(3-modda birinchi qismining uchinchi xatboshisi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
Oldingi tahrirga qarang.
manfaatlar to‘qnashuvi — shaxsning shaxsiy (bevosita yoki bilvosita) manfaatdorligi uning o‘z lavozim yoki xizmat majburiyatlarini lozim darajada bajarishiga ta’sir ko‘rsatayotgan yoxud ta’sir ko‘rsatishi mumkin bo‘lgan hamda shaxsiy manfaatdorlik bilan fuqarolarning, tashkilotlarning, jamiyatning yoki davlatning huquqlari, qonuniy manfaatlari o‘rtasida qarama-qarshilik yuzaga kelayotgan (mavjud manfaatlar to‘qnashuvi) yoki yuzaga kelishi mumkin bo‘lgan (ehtimoliy manfaatlar to‘qnashuvi) vaziyat.
(3-moddaning to‘rtinchi xatboshisi O‘zbekiston Respublikasining 2024-yil 5-iyundagi O‘RQ-931-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 05.06.2024-y., 03/24/931/0402-son — 2024-yil 6-dekabrdan kuchga kiradi)''',reply_markup=menyu_button)


@dp.message_handler(text='4 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''4-modda. Korrupsiyaga qarshi kurashishning asosiy prinsiplari
Korrupsiyaga qarshi kurashishning asosiy prinsiplari quyidagilardan iborat:
qonuniylik;
fuqarolar huquqlari, erkinliklari va qonuniy manfaatlarining ustuvorligi;
ochiqlik va shaffoflik;
tizimlilik;
davlat va fuqarolik jamiyatining hamkorligi;
korrupsiyaning oldini olishga doir chora-tadbirlar ustuvorligi;
javobgarlikning muqarrarligi.''',reply_markup=menyu_button)


@dp.message_handler(text='5 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''5-modda. Korrupsiyaga qarshi kurashish sohasidagi davlat siyosatining asosiy yo‘nalishlari
Korrupsiyaga qarshi kurashish sohasidagi davlat siyosatining asosiy yo‘nalishlari quyidagilardan iborat:
aholining huquqiy ongi va huquqiy madaniyatini yuksaltirish, jamiyatda korrupsiyaga nisbatan murosasiz munosabatni shakllantirish;
davlat va jamiyat hayotining barcha sohalarida korrupsiyaning oldini olishga doir chora-tadbirlarni amalga oshirish;
korrupsiyaga oid huquqbuzarliklarni o‘z vaqtida aniqlash, ularga chek qo‘yish, ularning oqibatlarini, ularga imkon beruvchi sabablar va shart-sharoitlarni bartaraf etish, korrupsiyaga oid huquqbuzarliklarni sodir etganlik uchun javobgarlikning muqarrarligi prinsipini ta’minlash.
''',reply_markup=menyu_button)

@dp.message_handler(text='6 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''6-modda. Korrupsiyaga qarshi kurashish sohasidagi davlat dasturlari va boshqa dasturlar
Korrupsiyaga qarshi kurashish sohasidagi davlat siyosati davlat dasturlari va boshqa dasturlar asosida amalga oshirilishi mumkin.
Davlat dasturlari va boshqa dasturlar ushbu Qonunning qoidalari samarali ijro etilishini ta’minlash, korrupsiyaning holati hamda tendensiyalaridan kelib chiqqan holda korrupsiyaga qarshi kurashish bo‘yicha kompleks va tizimli chora-tadbirlar ko‘rish maqsadida ishlab chiqiladi hamda amalga oshiriladi.
 LexUZ sharhi
Qarang: O‘zbekiston Respublikasi Prezidentining 2021-yil 6-iyuldagi PF-6257-sonli “Korrupsiyaga qarshi murosasiz munosabatda bo‘lish muhitini yaratish, davlat va jamiyat boshqaruvida korrupsiyaviy omillarni keskin kamaytirish va bunda jamoatchilik ishtirokini kengaytirish chora-tadbirlari to‘g‘risida”gi Farmoni, O‘zbekiston Respublikasi Prezidentining 2019-yil 27-maydagi PF-5729-sonli Farmoni bilan tasdiqlangan “2019-2020-yillarda korrupsiyaga qarshi kurashish davlat dasturi”.''',reply_markup=menyu_button)

@dp.message_handler(text='ORQAGA 🔙')
async def start(message:types.Message):
    await message.answer('''SIZ ORQAGA QAYTINGIZ 🔙''',reply_markup=kb)

@dp.message_handler(text='7 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''
7-modda. Korrupsiyaga qarshi kurashish bo‘yicha faoliyatni amalga oshiruvchi davlat organlari
Korrupsiyaga qarshi kurashish bo‘yicha faoliyatni bevosita amalga oshiruvchi davlat organlari quyidagilardan iborat:
Oldingi tahrirga qarang.
O‘zbekiston Respublikasi Korrupsiyaga qarshi kurashish agentligi;
(7-moddaning birinchi qismi O‘zbekiston Respublikasining 2021-yil 18-noyabrdagi O‘RQ-729-sonli Qonuniga asosan ikkinchi xatboshi bilan to‘ldirilgan — Qonunchilik ma’lumotlari milliy bazasi, 19.11.2021-y., 03/21/729/1064-son)
 LexUZ sharhi
Qarang: O‘zbekiston Respublikasi Prezidentining 2020-yil 29-iyundagi PF-6013-sonli “O‘zbekiston Respublikasida korrupsiyaga qarshi kurashish tizimini takomillashtirish bo‘yicha qo‘shimcha chora-tadbirlar to‘g‘risida”gi Farmoni.
O‘zbekiston Respublikasi Bosh prokuraturasi;
 LexUZ sharhi
Qarang: O‘zbekiston Respublikasi “Prokuratura to‘g‘risida”gi Qonunning 2, 4-moddalari.
Oldingi tahrirga qarang.
O‘zbekiston Respublikasi Davlat xavfsizlik xizmati;
(7-modda birinchi qismining uchinchi xatboshisi O‘zbekiston Respublikasining 2019-yil 18-fevraldagi O‘RQ-522-sonli Qonuni tahririda — O‘zbekiston Respublikasi Oliy Majlisi palatalarining Axborotnomasi, 2019-y., 2-son, 47-modda)
 LexUZ sharhi
Qarang: O‘zbekiston Respublikasi “O‘zbekiston Respublikasi Davlat xavfsizlik xizmati to‘g‘risida”gi Qonunning 5-moddasi.
O‘zbekiston Respublikasi Ichki ishlar vazirligi;
 LexUZ sharhi
Qarang: O‘zbekiston Respublikasi “Ichki ishlar organlari to‘g‘risida”gi Qonunning 4-moddasi.
O‘zbekiston Respublikasi Adliya vazirligi;
 LexUZ sharhi
Qarang: O‘zbekiston Respublikasi Prezidentining 2018-yil 13-apreldagi PF-3666-sonli “O‘zbekiston Respublikasi Adliya vazirligi faoliyatini yanada takomillashtirishga doir tashkiliy chora-tadbirlar to‘g‘risida”gi Farmoni.
Oldingi tahrirga qarang.
''',reply_markup=menyuiki_Button)

@dp.message_handler(text='8 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''8-modda. O‘zbekiston Respublikasining Korrupsiyaga qarshi kurashish bo‘yicha milliy kengashi va uning hududiy kengashlari
(8-moddaning nomi O‘zbekiston Respublikasining 2021-yil 18-noyabrdagi O‘RQ-729-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 19.11.2021-y., 03/21/729/1064-son)
Oldingi tahrirga qarang.
Korrupsiyaga qarshi kurashish bo‘yicha faoliyatni amalga oshiruvchi va unda ishtirok etuvchi organlar hamda tashkilotlarning faoliyatini muvofiqlashtirish uchun O‘zbekiston Respublikasining korrupsiyaga qarshi kurashish bo‘yicha milliy kengashi (bundan buyon matnda Milliy kengash deb yuritiladi) tashkil etiladi.
(8-moddaning birinchi qismi O‘zbekiston Respublikasining 2021-yil 18-noyabrdagi O‘RQ-729-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 19.11.2021-y., 03/21/729/1064-son)
Oldingi tahrirga qarang.
Qoraqalpog‘iston Respublikasida, viloyatlarda va Toshkent shahrida korrupsiyaga qarshi kurashish bo‘yicha hududiy kengashlar (bundan buyon matnda hududiy kengashlar deb yuritiladi) qonunchilikda belgilangan tartibda tashkil etiladi.
(8-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 18-noyabrdagi O‘RQ-729-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 19.11.2021-y., 03/21/729/1064-son)
Oldingi tahrirga qarang.
Milliy kengashning asosiy vazifalari quyidagilardan iborat:
(8-modda uchinchi qismining birinchi xatboshisi O‘zbekiston Respublikasining 2021-yil 18-noyabrdagi O‘RQ-729-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 19.11.2021-y., 03/21/729/1064-son)
korrupsiyaga qarshi kurashish sohasidagi davlat dasturlarining va boshqa dasturlarning ishlab chiqilishi hamda amalga oshirilishini tashkil etish;
korrupsiyaga qarshi kurashish bo‘yicha faoliyatni amalga oshiruvchi va unda ishtirok etuvchi organlar hamda tashkilotlarning faoliyatini muvofiqlashtirish va hamkorligini ta’minlash;
aholining huquqiy ongi va huquqiy madaniyatini yuksaltirishga, jamiyatda korrupsiyaga nisbatan murosasiz munosabatni shakllantirishga doir chora-tadbirlarning ishlab chiqilishi hamda amalga oshirilishini tashkil etish;
korrupsiyaga oid huquqbuzarliklarning oldini olishga, ularni aniqlashga, ularga chek qo‘yishga, ularning oqibatlarini, shuningdek ularga imkon beruvchi sabablar va shart-sharoitlarni bartaraf etishga doir chora-tadbirlar samaradorligi oshirilishini ta’minlash;
korrupsiyaning holati va tendensiyalari to‘g‘risidagi axborotni yig‘ish hamda tahlil etish;
korrupsiyaga qarshi kurashish bo‘yicha chora-tadbirlar amalga oshirilishi yuzasidan monitoringni amalga oshirish, ushbu sohadagi mavjud tashkiliy-amaliy va huquqiy mexanizmlarning samaradorligini baholash;
Oldingi tahrirga qarang.
korrupsiyaga qarshi kurashish to‘g‘risidagi qonunchilikni takomillashtirish va ushbu sohadagi ishlarni yaxshilash yuzasidan takliflar tayyorlash;
(8-modda uchinchi qismining sakkizinchi xatboshisi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
Oldingi tahrirga qarang.
hududiy kengashlar faoliyatini muvofiqlashtirish.
''',reply_markup=menyuiki_Button)

@dp.message_handler(text='9 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''9-modda. O‘zbekiston Respublikasi Bosh prokuraturasining korrupsiyaga qarshi kurashish sohasidagi vakolatlari
O‘zbekiston Respublikasi Bosh prokuraturasi o‘z vakolatlari doirasida:
korrupsiyaga qarshi kurashish sohasidagi davlat dasturlarini va boshqa dasturlarni ishlab chiqish hamda amalga oshirishda ishtirok etadi;
Oldingi tahrirga qarang.
korrupsiyaga qarshi kurashish to‘g‘risidagi qonunchilikning aniq va bir xilda ijro etilishi ustidan nazoratni amalga oshiradi;
(9-modda birinchi qismining uchinchi xatboshisi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
Oldingi tahrirga qarang.
korrupsiyaga qarshi kurashish sohasidagi tezkor-qidiruv faoliyatini, tergovga qadar tekshiruvni, surishtiruvni, dastlabki tergovni amalga oshiruvchi organlar faoliyatini muvofiqlashtiradi;
(9-modda birinchi qismining to‘rtinchi xatboshisi O‘zbekiston Respublikasining 2021-yil 18-noyabrdagi O‘RQ-729-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 19.11.2021-y., 03/21/729/1064-son)
korrupsiya bilan bog‘liq jinoyatlar bo‘yicha dastlabki tergovni amalga oshiradi;
korrupsiyaning holati va korrupsiyaga qarshi kurashish natijalari to‘g‘risidagi axborotni yig‘ish hamda tahlil qilishni amalga oshiradi;
jismoniy va yuridik shaxslarning korrupsiya faktlariga doir murojaatlarini ko‘rib chiqadi hamda ularning buzilgan huquqlarini tiklash va qonuniy manfaatlarini himoya qilish choralarini ko‘radi;
korrupsiyaga qarshi kurashish sohasidagi qonun ijodkorligi faoliyatida, shu jumladan qonunchilik tashabbusi huquqini amalga oshirishda ishtirok etadi;
aholi o‘rtasida jamiyatda huquqiy ongni, huquqiy madaniyatni yuksaltirishga va qonuniylikni mustahkamlashga qaratilgan huquqiy targ‘ibotga doir faoliyatda ishtirok etadi;
korrupsiyaga oid huquqbuzarliklarning o‘z vaqtida oldi olinishini, aniqlanishini va ularga chek qo‘yilishini ta’minlashga, ularning oqibatlarini, shuningdek ularga imkon beruvchi sabablar va shart-sharoitlarni bartaraf etishga doir tadbirlarni ishlab chiqadi hamda amalga oshiradi;
korrupsiyaga qarshi kurashish bo‘yicha faoliyatni amalga oshiruvchi va unda ishtirok etuvchi boshqa organlar hamda tashkilotlar bilan hamkorlik qiladi;
korrupsiyaga qarshi kurashish sohasida xalqaro hamkorlikni amalga oshiradi.
Oldingi tahrirga qarang.
O‘zbekiston Respublikasi Bosh prokuraturasi qonunchilikka muvofiq boshqa vakolatlarni ham amalga oshirishi mumkin.
(9-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
 LexUZ sharhi
Qarang: O‘zbekiston Respublikasi “Prokuratura to‘g‘risida”gi Qonunning 2, 4-moddalari.
Oldingi tahrirga qarang.
10-modda. O‘zbekiston Respublikasi Davlat xavfsizlik xizmatining korrupsiyaga qarshi kurashish sohasidagi vakolatlari
(10-moddaning nomi O‘zbekiston Respublikasining 2019-yil 18-fevraldagi O‘RQ-522-sonli Qonuni tahririda — O‘zbekiston Respublikasi Oliy Majlisi palatalarining Axborotnomasi, 2019-y., 2-son, 47-modda)
Oldingi tahrirga qarang.''',reply_markup=menyuiki_Button)

@dp.message_handler(text='10 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''(10-modda birinchi qismining birinchi xatboshisi O‘zbekiston Respublikasining 2019-yil 18-fevraldagi O‘RQ-522-sonli Qonuni tahririda — O‘zbekiston Respublikasi Oliy Majlisi palatalarining Axborotnomasi, 2019-y., 2-son, 47-modda)
korrupsiyaga qarshi kurashish sohasidagi davlat dasturlarini va boshqa dasturlarni ishlab chiqish hamda amalga oshirishda ishtirok etadi;
Oldingi tahrirga qarang.
korrupsiya bilan bog‘liq jinoyatlar bo‘yicha tezkor-qidiruv faoliyatini, tergovga qadar tekshiruvni va dastlabki tergovni amalga oshiradi;
(10-modda birinchi qismining uchinchi xatboshisi O‘zbekiston Respublikasining 2019-yil 23-maydagi O‘RQ-542-sonli Qonuni tahririda — Qonun hujjatlari ma’lumotlari milliy bazasi, 24.05.2019-y., 03/19/542/3177-son)
korrupsiyaning holati va korrupsiyaga qarshi kurashish natijalari to‘g‘risidagi axborotni yig‘adi hamda tahlil qiladi, milliy xavfsizlik uchun tahdidlarni baholashni amalga oshiradi, tegishli davlat organlariga zarur axborotni taqdim etadi;
jismoniy va yuridik shaxslarning korrupsiya faktlariga doir murojaatlarini ko‘rib chiqadi hamda ularning buzilgan huquqlarini tiklash va qonuniy manfaatlarini himoya qilish choralarini ko‘radi;
korrupsiyaga oid huquqbuzarliklarning o‘z vaqtida oldi olinishini, aniqlanishini va ularga chek qo‘yilishini ta’minlashga, ularning oqibatlarini, shuningdek ularga imkon beruvchi sabablar va shart-sharoitlarni bartaraf etishga doir tadbirlarni ishlab chiqadi hamda amalga oshiradi;
korrupsiyaga qarshi kurashish bo‘yicha faoliyatni amalga oshiruvchi va unda ishtirok etuvchi boshqa organlar hamda tashkilotlar bilan hamkorlik qiladi;
korrupsiyaga qarshi kurashish sohasida xalqaro hamkorlikni amalga oshiradi.
Oldingi tahrirga qarang.
O‘zbekiston Respublikasi Davlat xavfsizlik xizmati qonunchilikka muvofiq boshqa vakolatlarni ham amalga oshirishi mumkin.
(10-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
11-modda. O‘zbekiston Respublikasi Ichki ishlar vazirligining korrupsiyaga qarshi kurashish sohasidagi vakolatlari
O‘zbekiston Respublikasi Ichki ishlar vazirligi o‘z vakolatlari doirasida:
korrupsiyaga qarshi kurashish sohasidagi davlat dasturlarini va boshqa dasturlarni ishlab chiqish hamda amalga oshirishda ishtirok etadi;
Oldingi tahrirga qarang.
korrupsiya bilan bog‘liq jinoyatlar bo‘yicha tezkor-qidiruv faoliyatini, tergovga qadar tekshiruvni, surishtiruvni va dastlabki tergovni amalga oshiradi;
''',reply_markup=menyuiki_Button)

@dp.message_handler(text='11 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''11-modda birinchi qismining uchinchi xatboshisi O‘zbekiston Respublikasining 2019-yil 23-maydagi O‘RQ-542-sonli Qonuni tahririda — Qonun hujjatlari ma’lumotlari milliy bazasi, 24.05.2019-y., 03/19/542/3177-son)
korrupsiyaning holati va korrupsiyaga qarshi kurashish natijalari to‘g‘risidagi axborotni yig‘adi hamda tahlil qiladi, tegishli davlat organlariga zarur axborotni taqdim etadi;
jismoniy va yuridik shaxslarning korrupsiya faktlariga doir murojaatlarini ko‘rib chiqadi hamda ularning buzilgan huquqlarini tiklash va qonuniy manfaatlarini himoya qilish choralarini ko‘radi;
aholi o‘rtasida jamiyatda huquqiy ongni, huquqiy madaniyatni yuksaltirishga va qonuniylikni mustahkamlashga qaratilgan huquqiy targ‘ibotga doir faoliyatda ishtirok etadi;
korrupsiyaga oid huquqbuzarliklar to‘g‘risidagi statistika ma’lumotlarining hisobi yuritilishini va tahlil qilinishini ta’minlaydi;
korrupsiyaga oid huquqbuzarliklarning o‘z vaqtida oldi olinishini, aniqlanishini va ularga chek qo‘yilishini ta’minlashga, ularning oqibatlarini, shuningdek ularga imkon beruvchi sabablar va shart-sharoitlarni bartaraf etishga doir tadbirlarni ishlab chiqadi hamda amalga oshiradi;
korrupsiyaga qarshi kurashish bo‘yicha faoliyatni amalga oshiruvchi va unda ishtirok etuvchi boshqa organlar hamda tashkilotlar bilan hamkorlik qiladi;
korrupsiyaga qarshi kurashish sohasida xalqaro hamkorlikni amalga oshiradi.
Oldingi tahrirga qarang.
O‘zbekiston Respublikasi Ichki ishlar vazirligi qonunchilikka muvofiq boshqa vakolatlarni ham amalga oshirishi mumkin.
(11-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)''',reply_markup=menyuiki_Button)

@dp.message_handler(text='12 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''12-modda. O‘zbekiston Respublikasi Adliya vazirligining korrupsiyaga qarshi kurashish sohasidagi vakolatlari
O‘zbekiston Respublikasi Adliya vazirligi o‘z vakolatlari doirasida:
korrupsiyaga qarshi kurashish sohasidagi davlat dasturlarini va boshqa dasturlarni ishlab chiqish hamda amalga oshirishda ishtirok etadi;
korrupsiyaga qarshi kurashish sohasidagi qonun ijodkorligi faoliyatida ishtirok etadi;
aholi o‘rtasida jamiyatda huquqiy ongni, huquqiy madaniyatni yuksaltirishga va qonuniylikni mustahkamlashga qaratilgan huquqiy targ‘ibotga doir faoliyatni amalga oshiradi hamda muvofiqlashtiradi;
ta’lim muassasalarida korrupsiyaga qarshi kurashish sohasida huquqiy ta’lim va tarbiyaga doir chora-tadbirlarni amalga oshirishda ishtirok etadi;
normativ-huquqiy hujjatlardagi hamda ularning loyihalaridagi korrupsiya uchun shart-sharoitlar yaratadigan qoidalar va normalarni aniqlash maqsadida ushbu hujjatlar va loyihalarning tahlilini amalga oshiradi;
korrupsiyaga imkon beruvchi sabablar va shart-sharoitlarni bartaraf etish bo‘yicha choralar ko‘radi;
korrupsiyaga qarshi kurashish bo‘yicha faoliyatni amalga oshiruvchi va unda ishtirok etuvchi boshqa organlar hamda tashkilotlar bilan hamkorlik qiladi;
korrupsiyaga qarshi kurashish sohasida xalqaro hamkorlikni amalga oshiradi.
Oldingi tahrirga qarang.
O‘zbekiston Respublikasi Adliya vazirligi qonunchilikka muvofiq boshqa vakolatlarni ham amalga oshirishi mumkin.
(12-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
Oldingi tahrirga qarang.
''',reply_markup=menyuiki_Button)

@dp.message_handler(text='13 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''13-modda. O‘zbekiston Respublikasi Bosh prokuraturasi huzuridagi Iqtisodiy jinoyatlarga qarshi kurashish departamentining korrupsiyaga qarshi kurashish sohasidagi vakolatlari
(13-moddaning nomi O‘zbekiston Respublikasining 2019-yil 15-yanvardagi O‘RQ-516-sonli Qonuni tahririda — Qonun hujjatlari ma’lumotlari milliy bazasi, 16.01.2019-y., 03/19/516/2484-son)
Oldingi tahrirga qarang.
O‘zbekiston Respublikasi Bosh prokuraturasi huzuridagi Iqtisodiy jinoyatlarga qarshi kurashish departamenti o‘z vakolatlari doirasida:
(13-modda birinchi qismining birinchi xatboshisi O‘zbekiston Respublikasining 2019-yil 15-yanvardagi O‘RQ-516-sonli Qonuni tahririda — Qonun hujjatlari ma’lumotlari milliy bazasi, 16.01.2019-y., 03/19/516/2484-son)
korrupsiyaga qarshi kurashish sohasidagi davlat dasturlarini va boshqa dasturlarni ishlab chiqish hamda amalga oshirishda ishtirok etadi;
Oldingi tahrirga qarang.
jinoiy faoliyatdan olingan daromadlarni legallashtirish bilan bog‘liq jinoyatlar, iqtisodiy va korrupsiya bilan bog‘liq boshqa jinoyatlar bo‘yicha tezkor-qidiruv faoliyatini, tergovga qadar tekshiruvni va surishtiruvni amalga oshiradi;
(13-modda birinchi qismining uchinchi xatboshisi O‘zbekiston Respublikasining 2019-yil 15-yanvardagi O‘RQ-516-sonli Qonuni tahririda — Qonun hujjatlari ma’lumotlari milliy bazasi, 16.01.2019-y., 03/19/516/2484-son)
jinoiy faoliyatdan olingan daromadlarni legallashtirishning ehtimol tutilgan yo‘llari va mexanizmlarini aniqlash uchun pul mablag‘lari yoki boshqa mol-mulk bilan bog‘liq operatsiyalarning monitoringini tashkil etadi hamda o‘tkazadi;
jinoiy ta’qib etishni tashkil qilish va huquqiy ta’sir ko‘rsatishning boshqa choralarini ko‘rish uchun tegishli davlat organlarini korrupsiyaga oid aniqlangan huquqbuzarliklar to‘g‘risida o‘z vaqtida xabardor qiladi;
korrupsiyaga oid huquqbuzarliklarning o‘z vaqtida oldi olinishini, aniqlanishini va ularga chek qo‘yilishini ta’minlashga, ularning oqibatlarini, shuningdek ularga imkon beruvchi sabablar va shart-sharoitlarni bartaraf etishga doir tadbirlarni ishlab chiqadi hamda amalga oshiradi;
korrupsiyaga qarshi kurashish bo‘yicha faoliyatni amalga oshiruvchi va unda ishtirok etuvchi boshqa organlar hamda tashkilotlar bilan hamkorlik qiladi;
korrupsiyaga qarshi kurashish sohasida xalqaro hamkorlikni amalga oshiradi.
Oldingi tahrirga qarang.
O‘zbekiston Respublikasi Bosh prokuraturasi huzuridagi Iqtisodiy jinoyatlarga qarshi kurashish departamenti qonunchilikka muvofiq boshqa vakolatlarni ham amalga oshirishi mumkin.
(13-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)''',reply_markup=menyuiki_Button)

@dp.message_handler(text='14 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''14-modda. Fuqarolar o‘zini o‘zi boshqarish organlarining, nodavlat notijorat tashkilotlarining va fuqarolarning korrupsiyaga qarshi kurashishda ishtirok etishi
Fuqarolarning o‘zini o‘zi boshqarish organlari, nodavlat notijorat tashkilotlari va fuqarolar:
korrupsiyaga qarshi kurashish sohasidagi davlat dasturlarini va boshqa dasturlarni ishlab chiqish hamda amalga oshirishda ishtirok etishi;
aholining huquqiy ongi va huquqiy madaniyatini yuksaltirishda, jamiyatda korrupsiyaga nisbatan murosasiz munosabatni shakllantirishda ishtirok etishi;
Oldingi tahrirga qarang.
korrupsiyaga qarshi kurashish to‘g‘risidagi qonunchilikning ijro etilishi ustidan jamoatchilik nazoratini amalga oshirishi;
(14-modda birinchi qismining to‘rtinchi xatboshisi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
Oldingi tahrirga qarang.
korrupsiyaga qarshi kurashish to‘g‘risidagi qonunchilikni takomillashtirish yuzasidan takliflar kiritishi;
(14-modda birinchi qismining beshinchi xatboshisi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
korrupsiyaga qarshi kurashish sohasida davlat organlari va boshqa tashkilotlar bilan hamkorlik qilishi mumkin.
Oldingi tahrirga qarang.
Fuqarolarning o‘zini o‘zi boshqarish organlari, nodavlat notijorat tashkilotlari va fuqarolar qonunchilikka muvofiq boshqa tadbirlarda ham ishtirok etishi mumkin.
(14-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
Oldingi tahrirga qarang.
Nodavlat notijorat tashkilotlari ushbu moddada nazarda tutilgan tadbirlarni amalga oshirish maqsadida Milliy kengash va hududiy kengashlar faoliyatida, shuningdek davlat organlari huzuridagi ishchi guruhlar, komissiyalar va jamoat-maslahat organlari faoliyatida qonunchilikda belgilangan tartibda ishtirok etadi.
(14-moddaning uchinchi qismi O‘zbekiston Respublikasining 2021-yil 18-noyabrdagi O‘RQ-729-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 19.11.2021-y., 03/21/729/1064-son)''',reply_markup=menyuiki_Button)

@dp.message_handler(text='15 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''15-modda. Ommaviy axborot vositalarining korrupsiyaga qarshi kurashishda ishtirok etishi
Ommaviy axborot vositalari:
korrupsiyaga qarshi kurashish sohasidagi davlat dasturlarini va boshqa dasturlarni ishlab chiqish hamda amalga oshirishda ishtirok etadi;
korrupsiyaga qarshi kurashish sohasidagi davlat siyosatini amalga oshirishga, shu jumladan aholining huquqiy ongi va huquqiy madaniyatini yuksaltirishga, jamiyatda korrupsiyaga nisbatan murosasiz munosabatni shakllantirishga qaratilgan tadbirlarni yoritadi;
Oldingi tahrirga qarang.
korrupsiyaga qarshi kurashish to‘g‘risidagi qonunchilikning ijro etilishi ustidan jamoatchilik nazoratini amalga oshiradi;
(15-modda birinchi qismining to‘rtinchi xatboshisi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
korrupsiyaga qarshi kurashish sohasida davlat organlari va boshqa tashkilotlar bilan hamkorlik qiladi.
Oldingi tahrirga qarang.
Ommaviy axborot vositalari qonunchilikka muvofiq boshqa tadbirlarda ham ishtirok etishi mumkin.
(15-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
''',reply_markup=menyuiki_Button)

@dp.message_handler(text='16 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''16-modda. Aholining huquqiy ongi va huquqiy madaniyatini yuksaltirish, jamiyatda korrupsiyaga nisbatan murosasiz munosabatni shakllantirish
Davlat organlari va boshqa tashkilotlar korrupsiyaga qarshi kurashish maqsadida aholining huquqiy ongi va huquqiy madaniyatini yuksaltirish, jamiyatda korrupsiyaga nisbatan murosasiz munosabatni shakllantirish bo‘yicha zarur chora-tadbirlar ko‘radi, shu jumladan korrupsiyaga qarshi kurashish masalalariga doir tushuntirish ishlarini amalga oshirish, huquqiy tarbiya va ta’limni, ilmiy-amaliy tadbirlarni tashkil etish, o‘quv-uslubiy va ilmiy adabiyotlarni ishlab chiqish yo‘li bilan zarur chora-tadbirlar ko‘radi.
 LexUZ sharhi
Qarang: O‘zbekiston Respublikasi Prezidentining “Jamiyatda huquqiy ong va huquqiy madaniyatni yuksaltirish tizimini tubdan takomillashtirish to‘g‘risida”gi Farmoni.''',reply_markup=menyuch_Button)

@dp.message_handler(text='17 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''17-modda. Davlat organlari va boshqa tashkilotlar xodimlarining huquqiy savodxonligini oshirish
Davlat organlari va boshqa tashkilotlar o‘z mansabdor shaxslarining hamda boshqa xodimlarining korrupsiyaga qarshi kurashish sohasidagi huquqiy savodxonligini, shu jumladan huquqiy bilimlari darajasini oshirish yuzasidan zarur chora-tadbirlar ko‘radi.''',reply_markup=menyuch_Button)

@dp.message_handler(text='18 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''18-modda. Ta’lim muassasalarida korrupsiyaga qarshi kurashish sohasidagi huquqiy ta’lim va tarbiya
Ta’lim muassasalarida korrupsiyaga qarshi kurashish sohasidagi huquqiy ta’lim va tarbiya belgilangan davlat ta’lim standartlariga muvofiq amalga oshiriladi.
Davlat ta’limni boshqarish organlari va ta’lim muassasalari korrupsiyaga qarshi kurashish sohasidagi davlat siyosatining asosiy yo‘nalishlarini inobatga olgan holda ta’lim muassasalarida huquqiy ta’lim va tarbiyaga, mutaxassislarni kasbiy tayyorlashning sifatini oshirishga, ta’lim dasturlarini doimiy ravishda takomillashtirib borishga qaratilgan chora-tadbirlarni ishlab chiqadi.''',reply_markup=menyuch_Button)

@dp.message_handler(text='19 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''19-modda. Davlat boshqaruvi sohasida korrupsiyaning oldini olishga doir chora-tadbirlar
Davlat boshqaruvi sohasida korrupsiyaning oldini olishga doir chora-tadbirlar quyidagilardan iborat:
davlat organlari faoliyatining ochiqligini va ularning hisobdorligini ta’minlash, davlat boshqaruvi tizimining samaradorligini oshirish, davlat organlarining, ular mansabdor shaxslarining va boshqa xodimlarining o‘z zimmasiga yuklatilgan vazifalarni bajarishi yuzasidan mas’uliyatini kuchaytirish;
korrupsiyaga qarshi kurashish sohasida davlat organlarining faoliyati ustidan parlament va jamoatchilik nazoratini amalga oshirish;
davlat organlarining va ular xodimlarining faoliyatida korrupsiyaga oid huquqbuzarliklarga yo‘l qo‘ymaslik;
davlat organlarining mansabdor shaxslari va boshqa xodimlari tomonidan o‘z mansab yoki xizmat majburiyatlarining bajarilishi samaradorligi mezonlarini, standartlarini va uning sifatini baholash tizimlarini joriy etish;
davlat organlari xodimlarining kasbiy hamda xizmatdan tashqari faoliyatdagi odob-axloqining yagona prinsiplari va qoidalarini belgilovchi odob-axloq qoidalarini samarali amalga oshirish;
davlat organlari xodimlari manfaatlarining to‘qnashuvini hal qilishning tashkiliy-huquqiy asoslarini takomillashtirish, ularga rioya etilishi yuzasidan monitoring o‘tkazilishini ta’minlash;
davlat organlari xodimlarining huquqiy maqomini belgilash, xizmatni o‘tashning shaffof tartibini o‘rnatish, shaxsiy va kasbiy sifatlar, ochiqlik, beg‘arazlik, adolatlilik va xolislik prinsiplari asosida tanlov bo‘yicha saralash hamda xizmatda ko‘tarilish tizimini joriy etish;
Oldingi tahrirga qarang.
davlat organlari tomonidan jismoniy va yuridik shaxslarning murojaatlari to‘g‘risidagi qonunchilik talablariga rioya etilishi, murojaatlarning to‘liq, xolisona va o‘z vaqtida ko‘rib chiqilishi, ular tomonidan jismoniy va yuridik shaxslarning buzilgan huquqlari, erkinliklarini tiklash hamda qonuniy manfaatlarini himoya qilish bo‘yicha o‘z vakolatlari doirasida choralar ko‘rilishi ustidan nazoratni ta’minlash;
(19-modda birinchi qismining to‘qqizinchi xatboshisi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
davlat organlari faoliyatida korrupsiyaning oldini olishga doir tadbirlarning amalga oshirilishi yuzasidan ushbu organlar tomonidan ko‘rilayotgan chora-tadbirlar samaradorligini baholagan holda muntazam ravishda monitoring o‘tkazish;
normativ-huquqiy hujjatlarning va ular loyihalarining korrupsiyaga qarshi ekspertizasini tashkil etish;
davlat organlarining mansabdor shaxslari va boshqa xodimlarining samarali ijtimoiy himoya qilinishini, moddiy ta’minot olishini va rag‘batlantirilishini ta’minlash.
Oldingi tahrirga qarang.
Qonunchilikda davlat boshqaruvi sohasida korrupsiyaning oldini olishga doir boshqa chora-tadbirlar ham nazarda tutilishi mumkin.
(19-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
Oldingi tahrirga qarang.
Davlat organlarining va o‘zga tashkilotlarning mansabdor shaxslari hamda boshqa xodimlari qonunchilikka rioya etishi, o‘z mansab yoki xizmat majburiyatlarini beg‘arazlik bilan, xolisona, vijdonan, odob-axloq qoidalariga rioya etgan holda bajarishi hamda korrupsiyaga oid biror-bir huquqbuzarlikni sodir etishdan yoki bunday huquqbuzarliklarni sodir etish uchun shart-sharoitlar yaratadigan boshqa har qanday harakatlardan o‘zini tiyishi shart.
(19-moddaning uchinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)''',reply_markup=menyutor_Button)

@dp.message_handler(text='20 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''20-modda. Ijtimoiy-iqtisodiy rivojlanish va tadbirkorlik sohasida korrupsiyaning oldini olishga doir chora-tadbirlar
Ijtimoiy-iqtisodiy rivojlanish va tadbirkorlik sohasida korrupsiyaning oldini olishga doir chora-tadbirlar quyidagilardan iborat:
ma’muriy va byurokratik to‘siqlarni bartaraf etish, ro‘yxatga olish, ruxsat etish va litsenziyaga doir tartib-taomillarni soddalashtirish hamda ularning tezkorligini oshirish;
davlat organlarining nazorat-tekshiruv vazifalarini maqbullashtirish, tadbirkorlik subyektlarining faoliyatini tekshirish tizimini takomillashtirish, ularning faoliyatiga qonunga xilof ravishda aralashishga yo‘l qo‘ymaslik;
davlat organlari va tadbirkorlik subyektlari o‘rtasidagi o‘zaro munosabatlarning masofaviy shakllarini keng joriy etish;
tadbirkorlik faoliyatini olib borish uchun teng shart-sharoitlar yaratish va insofsiz raqobatga yo‘l qo‘ymaslik;
davlat xaridlarining samarali huquqiy mexanizmlarini joriy etish, davlat xaridlarini joylashtirishda oshkoralik, shaffoflikni ta’minlash hamda raqobat muhitini qo‘llab-quvvatlash;
ta’lim, sog‘liqni saqlash, ijtimoiy ta’minot, kommunal xizmat ko‘rsatish sohasida va ijtimoiy-iqtisodiy rivojlanishning boshqa sohalarida aholi uchun adolatli shart-sharoitlarni hamda teng imkoniyatlarni yaratish, korrupsiyaga oid huquqbuzarliklarga yo‘l qo‘ymaslik;
nodavlat tashkilotlarda korrupsiyaga qarshi kurashishning samarali mexanizmlarini joriy etish.
Oldingi tahrirga qarang.
Qonunchilikda ijtimoiy-iqtisodiy rivojlanish va tadbirkorlik sohasida korrupsiyaning oldini olishga doir boshqa chora-tadbirlar ham nazarda tutilishi mumkin.
(20-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)''',reply_markup=menyutor_Button)

@dp.message_handler(text='21 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''21-modda. Manfaatlar to‘qnashuvining oldini olish va uni bartaraf etishga doir chora-tadbirlar
Davlat organlarining xodimlari mansab yoki xizmat majburiyatlarini bajarish chog‘ida manfaatlar to‘qnashuviga olib keladigan yoki olib kelishi mumkin bo‘lgan shaxsiy manfaatdorlikka yo‘l qo‘ymasligi kerak.
Manfaatlar to‘qnashuvi yuzaga kelgan taqdirda, davlat organlarining xodimlari o‘zining bevosita rahbarini darhol xabardor qilishi kerak. Manfaatlar to‘qnashuvi mavjudligi to‘g‘risida ma’lumotlar olgan rahbar bu to‘qnashuvning oldini olish yoki uni bartaraf etish yuzasidan o‘z vaqtida choralar ko‘rishi shart.
Davlat organlarining maxsus bo‘linmalari yoki odob komissiyalari manfaatlar to‘qnashuvini hal etish qoidalariga rioya etilishi yuzasidan monitoringni amalga oshiradi.
Oldingi tahrirga qarang.
Davlat organlarining manfaatlar to‘qnashuvining oldini olish yoki uni bartaraf etish talablari buzilishiga yo‘l qo‘ygan xodimlari, shuningdek ularning rahbarlari qonunchilikka muvofiq javobgar bo‘ladi.
(21-moddaning to‘rtinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)''',reply_markup=menyutor_Button)

@dp.message_handler(text='22 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''22-modda. Ma’muriy tartib-taomillar sohasida korrupsiyaning oldini olishga doir chora-tadbirlar
Ma’muriy tartib-taomillar sohasida korrupsiyaning oldini olishga doir chora-tadbirlar quyidagilardan iborat:
qonuniylik va adolatlilik prinsiplarini ta’minlash, ma’muriy-boshqaruv jarayonining beg‘arazligi kafolatlarini yaratish, ushbu jarayonning shaffofligini, tashqi va ichki nazorat uchun ochiqligini oshirish;
o‘z ixtiyoricha harakat qilish vakolatlarini cheklagan holda ma’muriy tartib-taomillarni batafsil tartibga solish, byurokratik rasmiyatchilikka yo‘l qo‘ymaslik;
soddalashtirilgan ma’muriy tartib-taomillarni joriy etish;
davlat organlarining qarorlari ustidan shikoyat qilishning va yetkazilgan zarar o‘rnini qoplashning samarali mexanizmlarini belgilash.
Oldingi tahrirga qarang.
Qonunchilikda ma’muriy tartib-taomillar sohasida korrupsiyaning oldini olishga doir boshqa chora-tadbirlar ham nazarda tutilishi mumkin.
(22-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)''',reply_markup=menyutor_Button)

@dp.message_handler(text='23 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''23-modda. Davlat xaridlarini amalga oshirish sohasida korrupsiyaning oldini olishga doir chora-tadbirlar
Davlat xaridlarini amalga oshirish sohasida korrupsiyaning oldini olishga doir chora-tadbirlar quyidagilardan iborat:
davlat xaridlarini amalga oshirish tartib-taomillari to‘g‘risidagi axborotning shaffofligi va ochiqligini ta’minlash;
adolatli raqobatni va qarorlar qabul qilish chog‘ida xolisona mezonlardan foydalanilishini ta’minlash;
ichki nazoratning samarali tizimini, shuningdek davlat xaridlarini o‘tkazish natijalari yuzasidan shikoyat qilish va nizolashishning samarali tartib-taomilini yaratish;
davlat elektron savdolarining samarali ishlashini ta’minlash.
Oldingi tahrirga qarang.
Qonunchilikda davlat xaridlarini amalga oshirish sohasida korrupsiyaning oldini olishga doir boshqa chora-tadbirlar ham nazarda tutilishi mumkin.
(23-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)''',reply_markup=menyutor_Button)

@dp.message_handler(text='24 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''24-modda. Normativ-huquqiy hujjatlarning va ular loyihalarining korrupsiyaga qarshi ekspertizasi
Normativ-huquqiy hujjatlarning va ular loyihalarining korrupsiyaga qarshi ekspertizasi:
korrupsiyaga oid huquqbuzarliklarni sodir etish imkoniyatini yaratadigan, korrupsiyaga sabab bo‘ladigan omillarni aniqlashga;
korrupsiyaga oid huquqbuzarliklarni sodir etish imkoniyatini yaratadigan loyihani qabul qilish oqibatlarini umumiy baholashga;
normativ-huquqiy hujjatlarni qo‘llash jarayonida korrupsiya xususiyatiga ega xavflarning yuzaga kelishi ehtimolini prognoz qilishga;
korrupsiyaga sabab bo‘lgan, aniqlangan omillarni bartaraf etishga qaratilgan tavsiyalarni ishlab chiqishga va choralar ko‘rishga yo‘naltirilgan jarayondan iborat bo‘ladi.
Oldingi tahrirga qarang.
Normativ-huquqiy hujjatlarning va ular loyihalarining korrupsiyaga qarshi ekspertizasi “Normativ-huquqiy hujjatlarning va ular loyihalarining korrupsiyaga qarshi ekspertizasi to‘g‘risida”gi O‘zbekiston Respublikasi Qonunida belgilangan tartibda o‘tkaziladi.
(24-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2023-yil 8-avgustdagi O‘RQ-860-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 09.08.2023-y., 03/23/860/0571-son)
 LexUZ sharhi
Qarang: O‘zbekiston Respublikasi adliya vazirining 2021-yil 24-fevraldagi 2-mh-sonli “Normativ-huquqiy hujjatlar va ular loyihalarining korrupsiyaga qarshi ekspertizasini o‘tkazish tartibi to‘g‘risidagi nizomni tasdiqlash haqida”gi buyrug‘i (ro‘yxat raqami 3287, 24.02.2021-y.), O‘zbekiston Respublikasi Prezidentining 2021-yil 22-oktabrdagi PF-5263-sonli “Normativ-huquqiy hujjatlar va ularning loyihalarini korrupsiyaga qarshi ekspertizadan o‘tkazishni yanada takomillashtirish chora-tadbirlari to‘g‘risida”gi qarori.''',reply_markup=menyutor_Button)


@dp.message_handler(text='25 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''25-modda. Korrupsiyaga oid huquqbuzarliklarni o‘z vaqtida aniqlash va ularga chek qo‘yishga, korrupsiyaga oid huquqbuzarliklarni sodir etganlik uchun javobgarlikning muqarrarligi prinsipini ta’minlashga doir chora-tadbirlar
Korrupsiyaga oid huquqbuzarliklarni o‘z vaqtida aniqlash va ularga chek qo‘yishga, korrupsiyaga oid huquqbuzarliklarni sodir etganlik uchun javobgarlikning muqarrarligi prinsipini ta’minlashga doir chora-tadbirlar quyidagilardan iborat:
korrupsiyaga qarshi kurashish bo‘yicha faoliyatni bevosita amalga oshiruvchi davlat organlarining korrupsiyaning holatini va tendensiyalarini tizimli tahlil qilishga asoslangan samarali ishini tashkil etish, ularning faoliyatida korrupsiyaga oid huquqbuzarliklarga yo‘l qo‘ymaslik;
korrupsiyaga oid huquqbuzarliklarga qarshi kurashning zamonaviy shakllari va usullaridan foydalanish, huquqni muhofaza qiluvchi organlarning texnik ta’minoti darajasini oshirish, ularning ishiga zamonaviy axborot-kommunikatsiya texnologiyalarini joriy etish;
sudlarning mustaqilligi va erkinligini, ular faoliyatining ochiqligini ta’minlash;
korrupsiyaga qarshi kurashish bo‘yicha faoliyatni bevosita amalga oshiruvchi davlat organlari o‘rtasida muvofiqlashtirishni va hamkorlikni ta’minlash;
jismoniy va yuridik shaxslarning korrupsiyaga oid huquqbuzarliklar faktlariga doir murojaatlari to‘liq, xolisona va o‘z vaqtida ko‘rib chiqilishini ta’minlash;
korrupsiyaga oid huquqbuzarliklar to‘g‘risida axborot bergan shaxslarning himoya qilinishini ta’minlash;
korrupsiyaga qarshi kurashning samarali jinoyat-huquqiy va jinoyat-protsessual mexanizmlarini yaratish.''',reply_markup=menyubesh_Button)

@dp.message_handler(text='26 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''26-modda. Davlat organlari xodimlarining korrupsiyaga oid huquqbuzarliklar faktlari to‘g‘risida xabar qilish majburiyati
Davlat organlarining xodimlari ularni korrupsiyaga oid huquqbuzarliklar sodir etishga ko‘ndirish maqsadida biror-bir shaxs o‘zlariga murojaat etganligiga doir barcha hollar to‘g‘risida, shuningdek davlat organlarining boshqa xodimlari tomonidan sodir etilgan shunga o‘xshash huquqbuzarliklarning o‘zlariga ma’lum bo‘lib qolgan har qanday faktlari haqida o‘z rahbarini yoxud huquqni muhofaza qiluvchi organlarni xabardor etishi shart.
Oldingi tahrirga qarang.
Ushbu moddaning birinchi qismida nazarda tutilgan majburiyatning davlat organlarining xodimlari tomonidan bajarilmaganligi qonunchilikka muvofiq javobgarlikka sabab bo‘ladi.
(26-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
 LexUZ sharhi
Qarang: O‘zbekiston Respublikasi Jinoyat kodeksining 241, 2411-moddalari, O‘zbekiston Respublikasi Ma’muriy javobgarlik to‘g‘risidagi kodeksi 1758-moddasining to‘rtinchi qismi.
''',reply_markup=menyubesh_Button)


@dp.message_handler(text='27 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''27-modda. Korrupsiyaga oid huquqbuzarliklar uchun javobgarlik
Oldingi tahrirga qarang.
Korrupsiyaga oid huquqbuzarliklar sodir etganlik qonunchilikka muvofiq javobgarlikka sabab bo‘ladi.
(27-moddaning birinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
Korrupsiyaga oid huquqbuzarlik sodir etgan shaxslar sudning qaroriga ko‘ra muayyan huquqlardan, shu jumladan muayyan lavozimlarni egallash huquqidan qonunga muvofiq mahrum etilishi mumkin.
Yuridik shaxslar korrupsiyaga oid huquqbuzarliklarni sodir etganlik uchun qonunda belgilangan tartibda javobgar bo‘ladi.
 LexUZ sharhi
Qarang: O‘zbekiston Respublikasi Jinoyat kodeksining 210 – 214-moddalari.
Oldingi tahrirga qarang.''',reply_markup=menyubesh_Button)

@dp.message_handler(text='28 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''28-modda. Korrupsiyaga oid huquqbuzarliklar to‘g‘risidagi axborotni xabar qiluvchi shaxslarni va ularning yaqin qarindoshlarini himoya qilish
Korrupsiyaga oid huquqbuzarliklar to‘g‘risidagi axborotni xabar qiluvchi shaxslar va ularning yaqin qarindoshlari davlat himoyasida bo‘ladi.
Korrupsiyaga oid huquqbuzarliklar to‘g‘risida xabar qiluvchi shaxslar to‘g‘risidagi ma’lumotlar xizmat sirini tashkil etadi hamda faqat qonunda nazarda tutilgan hollarda va shaxsning o‘zining, shuningdek korrupsiyaga qarshi kurashish bo‘yicha faoliyatni amalga oshiruvchi organ rahbarining yozma ruxsati asosida oshkor etiladi.
Korrupsiyaga oid huquqbuzarliklar to‘g‘risida xabar qiluvchi shaxslarning hamda ularning yaqin qarindoshlarining hayotiga va sog‘lig‘iga haqiqiy tahdidni, ularga nisbatan zo‘rlik ishlatilganligini, ularning mol-mulki yo‘q qilinganligini yoki shikastlantirilganligini tasdiqlovchi yetarli asoslar mavjud bo‘lgan taqdirda, korrupsiyaga qarshi kurashishni amalga oshiruvchi organlar “Jabrlanuvchilarni, guvohlarni va jinoyat protsessining boshqa ishtirokchilarini himoya qilish to‘g‘risida”gi O‘zbekiston Respublikasi Qonuniga muvofiq ularni himoya qilish bo‘yicha zarur choralar ko‘rishi shart.
Korrupsiyaga oid huquqbuzarliklar to‘g‘risidagi axborotni xabar qiluvchi shaxslarning va ularning yaqin qarindoshlarining huquqlari va qonuniy manfaatlariga korrupsiyaga oid huquqbuzarliklar to‘g‘risida xabar qilganligi sababli tajovuz qilishga, shuningdek ish beruvchi tomonidan ularning mehnatga oid huquqlari buzilishiga yo‘l qo‘yilmaydi hamda bu qonunga ko‘ra javobgarlikka sabab bo‘ladi.
Korrupsiyaga oid huquqbuzarliklar to‘g‘risida xabar qiluvchi shaxslarni rag‘batlantirish O‘zbekiston Respublikasi Vazirlar Mahkamasi tomonidan belgilangan tartibda amalga oshiriladi.
 LexUZ sharhi
Qarang: Vazirlar Mahkamasining 2020-yil 31-dekabrdagi 829-son “Korrupsiyaga oid huquqbuzarlik haqida xabar bergan yoki korrupsiyaga qarshi kurashishga boshqa tarzda ko‘maklashgan shaxslarni rag‘batlantirish tartibi to‘g‘risidagi nizomni tasdiqlash haqida”gi qarori.
Ushbu moddaning qoidalari korrupsiyaga oid huquqbuzarliklar to‘g‘risida bila turib yolg‘on axborotni xabar qilgan shaxslarga nisbatan tatbiq etilmaydi, ular bunday huquqbuzarlik uchun qonunga muvofiq javobgar bo‘ladi.
(28-modda O‘zbekiston Respublikasining 2021-yil 18-noyabrdagi O‘RQ-729-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 19.11.2021-y., 03/21/729/1064-son)''',reply_markup=menyubesh_Button)


@dp.message_handler(text='29 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''29-modda. Korrupsiyaga oid huquqbuzarliklar natijasida qabul qilingan qarorlarni bekor qilish yoki o‘zgartirish
Korrupsiyaga oid huquqbuzarliklar natijasida qabul qilingan qarorlar manfaatdor shaxsning arizasiga ko‘ra vakolatli davlat organi, boshqa tashkilot yoki mansabdor shaxs tomonidan bekor qilinishi yoxud o‘zgartirilishi yoki sud tartibida haqiqiy emas deb topilishi mumkin.
Oldingi tahrirga qarang.
Korrupsiyaga oid huquqbuzarliklar sodir etilganligi natijasida qabul qilingan qaror bekor qilingan, o‘zgartirilgan yoki haqiqiy emas deb topilgan taqdirda, uning qabul qilinishi natijasida jismoniy va yuridik shaxslarga yetkazilgan zararning o‘rni qonunchilikda belgilangan tartibda qoplanishi lozim.
(29-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
 LexUZ sharhi
Qarang: O‘zbekiston Respublikasi Fuqarolik kodeksining 11-12 hamda 14 moddalari.
''',reply_markup=menyubesh_Button)

@dp.message_handler(text='30 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''30-modda. Korrupsiya sohasidagi tadqiqotlar
Korrupsiyaning holatini, xususiyatini, miqyoslarini, o‘zgarishlarini va tendensiyalarini, shuningdek korrupsiyaga qarshi kurashish sohasidagi davlat siyosatining amalga oshirilish samaradorligini o‘rganish davlat organlari tomonidan fuqarolarning o‘zini o‘zi boshqarish organlari, nodavlat notijorat tashkilotlari va boshqa tashkilotlar, ommaviy axborot vositalari, shuningdek fuqarolar bilan hamkorlikda sotsiologik, maxsus, ilmiy tadqiqotlar hamda boshqa turdagi tadqiqotlar o‘tkazish yo‘li bilan doimiy asosda amalga oshiriladi.
Sotsiologik tadqiqotlar korrupsiyaga eng ko‘p duchor bo‘lgan tarmoqlar va sohalarni, uning yuzaga kelishi sabablari va shart-sharoitlarini aniqlash, shuningdek mazkur faoliyatga jalb etilgan ijtimoiy guruhlarni aniqlash maqsadida sotsiologik so‘rovlar o‘tkazish va boshqa usullardan foydalanish yo‘li bilan jamoatchilik fikrini tizimli o‘rganishni o‘z ichiga oladi.
Maxsus tadqiqotlar huquqni muhofaza qiluvchi va nazorat qiluvchi organlarning korrupsiyaga qarshi kurashish bo‘yicha faoliyati natijalarini, korrupsiyaga oid jinoyatchilikning holatini, korrupsiya ko‘rsatkichlarining statistika hisobini muntazam ravishda tizimli tahlil qilishni, davlat va jamiyat hayotining barcha sohalarida korrupsiyaning xususiyati va miqyoslarini, o‘zgarishlari va tendensiyalarini o‘rganishni o‘z ichiga oladi.
Ilmiy tadqiqotlar korrupsiyaga qarshi kurashish muammolari bo‘yicha ilmiy tadqiqotlar o‘tkazishni, ilmiy uslubiyotlar va tavsiyalar ishlab chiqishni, ularni amaliyotga oqilona joriy etishni, korrupsiyaga qarshi kurashishda qo‘llanilayotgan shakllar va usullar samaradorligini prognoz qilish hamda ilmiy tahlil etishni o‘z ichiga oladi.
Davlat korrupsiyaga qarshi kurashish sohasidagi tadqiqotlarni qo‘llab-quvvatlaydi va rag‘batlantiradi.''',reply_markup=menyuolti_Button)

@dp.message_handler(text='31 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''31-modda. Axborot olish
Har kim davlat organlarining tashkil etilishi va faoliyat ko‘rsatishi to‘g‘risida, shu shaxsning o‘ziga yoki shaxslar guruhiga taalluqli bo‘lgan hujjatlarning qabul qilinish jarayonlari haqida axborot olish huquqiga ega.
Oldingi tahrirga qarang.
Davlat organlari, fuqarolarning o‘zini o‘zi boshqarish organlari, nodavlat notijorat tashkilotlari va boshqa tashkilotlar korrupsiya bilan bog‘liq bo‘lgan, jamiyat uchun ahamiyatga molik voqealar, faktlar, hodisalar va jarayonlar to‘g‘risidagi xabarlarni qonunchilikda belgilangan tartibda ommaviy axborot vositalariga taqdim etadi.
(31-moddaning ikkinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
Axborot olish faqat qonunga muvofiq cheklanishi mumkin.''',reply_markup=menyuolti_Button)

@dp.message_handler(text='32 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''32-modda. Korrupsiyaga qarshi kurashish sohasida xalqaro hamkorlik
Oldingi tahrirga qarang.
Korrupsiyaga qarshi kurashish sohasida xalqaro hamkorlik O‘zbekiston Respublikasining qonunchiligi va xalqaro shartnomalariga muvofiq amalga oshiriladi.
(32-moddaning birinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
Korrupsiyaga qarshi kurashish bo‘yicha faoliyatni amalga oshiruvchi davlat organlari chet davlatlarning vakolatli organlariga zarur axborotni taqdim etish to‘g‘risida so‘rovlar yuborish va ularning so‘rovlariga javob berish huquqiga ega.
Oldingi tahrirga qarang.
Korrupsiyaga qarshi kurashish bo‘yicha faoliyatni amalga oshiruvchi davlat organlari korrupsiyaga oid huquqbuzarliklar natijasida olingan mol-mulkni O‘zbekiston Respublikasining qonunchiligi va xalqaro shartnomalariga muvofiq qaytarish choralarini ko‘radi.
(32-moddaning uchinchi qismi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
 LexUZ sharhi
Qarang: Birlashgan Millatlar Tashkilotining Korrupsiyaga qarshi Konvensiyasi.
Oldingi tahrirga qarang.''',reply_markup=menyuolti_Button)

@dp.message_handler(text='33 MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''33-modda. Qonunchilikni ushbu Qonunga muvofiqlashtirish
(33-moddaning nomi O‘zbekiston Respublikasining 2021-yil 21-apreldagi O‘RQ-683-sonli Qonuni tahririda — Qonunchilik ma’lumotlari milliy bazasi, 21.04.2021-y., 03/21/683/0375-son)
O‘zbekiston Respublikasi Vazirlar Mahkamasi:
hukumat qarorlarini ushbu Qonunga muvofiqlashtirsin;
davlat boshqaruvi organlari ushbu Qonunga zid bo‘lgan o‘z normativ-huquqiy hujjatlarini ko‘rib chiqishlari va bekor qilishlarini ta’minlasin.
''',reply_markup=menyuolti_Button)

@dp.message_handler(text='34MODANI OQISH 📜')
async def start(message:types.Message):
    await message.answer('''34-modda. Ushbu Qonunning kuchga kirishi
Ushbu Qonun rasmiy e’lon qilingan kundan e’tiboran kuchga kiradi.
 LexUZ sharhi
Ushbu Qonun “Xalq so‘zi” gazetasining 2017-yil 4-yanvardagi 2 (6696)-sonida e’lon qilingan.
''',reply_markup=menyuolti_Button)

@dp.message_handler(text='OTZIV QOLDIRISH 📨')
async def start(message:types.Message):
    await message.answer('''OTZIF QOLDIRMOQCHI BOLGANINGIZ UCHUN RAXMAT 🙂''',reply_markup=q_Button)


@dp.message_handler(text='BIZNI SAYTGA OTISH 📋')
async def start(message: types.Message):
    web_app_button = InlineKeyboardButton(text="Open Web App", web_app=types.WebAppInfo(url="https://web-app-baar.vercel.app/"))
    web_app_markup = InlineKeyboardMarkup().add(web_app_button)
    await message.answer("Click below to open the web app:", reply_markup=web_app_markup)

@dp.message_handler(text='★')
async def start(message: types.Message):
    await message.answer('bundan kengi butoni tanlang',reply_markup=menyutoqiz_Button)
    await message.delete()

@dp.message_handler(text='★★')
async def start(message: types.Message):
    await message.answer('bundan kengi butoni tanlang',reply_markup=menyuon_Button)
    await message.delete()

@dp.message_handler(text='★★★')
async def start(message: types.Message):
    await message.answer('bundan kengi butoni tanlang',reply_markup=menyuonbir_Button)
    await message.delete()

@dp.message_handler(text='★★★★')
async def start(message: types.Message):
    await message.answer('bundan kengi butoni tanlang',reply_markup=menyuoniki_Button)
    await message.delete()

@dp.message_handler(text='★★★★★')
async def start(message: types.Message):
    await message.answer('bundan kengi butoni tanlang',reply_markup=menyuonuch_Button)
    await message.delete()

@dp.message_handler(text='ORQAGA QAYTISH 🔙')
async def start(message: types.Message):
    await message.answer('SIZ ORQAGA QAYTINGIZ 🔙',reply_markup=q_Button)
    await message.delete()

@dp.message_handler(text='OVOZNI YUBORISH 📨')
async def start(message: types.Message):
    await message.answer('Fikiringiz Uchun Raxmat 🙂')



if __name__== "__main__":
    executor.start_polling(dp, skip_updates=True)