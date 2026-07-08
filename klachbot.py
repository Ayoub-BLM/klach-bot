import discord
from discord.ext import commands
from discord.ui import Button, View
from flask import Flask
from threading import Thread
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# إعداد الصلاحيات (Intents)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# إنشاء كلاس الأزرار وتفاعلها
class LanguageView(View):
    def __init__(self):
        super().__init__(timeout=None) # يجعل الأزرار تعمل دائماً دون توقف

    # زر اللغة العربية
    @discord.ui.button(label="العربية", style=discord.ButtonStyle.primary, emoji="🇸🇦", custom_id="lang_ar")
    async def arabic_button(self, interaction: discord.Interaction, button: Button):
        # إنشاء إيمبد الرد العربي
        ar_embed = discord.Embed(
            title="القوانين العربية",
            description='''
╭─── ✦ 𝐊𝐋𝐀𝐒𝐇 𝐒𝐄𝐑𝐕𝐄𝐑 𝐑𝐔𝐋𝐄𝐒 ✦ ───╮
✦ 𝟭. الاحترام
يمنع منعا باتا السب أو الإهانة أو العنصرية أو التقليل من أي شخص بأي شكل.
✦ 𝟮. المحتوى غير اللائق
ممنوع إرسال أي صور أو رسائل أو تعليقات غير مناسبة أو مخالفة للأدب العام.
✦ 𝟯. السبام والتكرار
يمنع إرسال رسائل متكررة أو سبام أو إزعاج الأعضاء داخل الشات.
✦ 𝟰. الإعلانات
ممنوع الإعلان لأي سيرفر أو رابط بدون إذن الإدارة.
✦ 𝟱. المحتوى المخالف
يمنع أي محتوى NSFW أو مزعج أو يسبب إزعاج للأعضاء.
✦ 𝟲. استخدام الرومات
كل روم مخصص لغرضه، يرجى الالتزام وعدم التخريب أو الخروج عن الموضوع.
✦ 𝟳. اللغة
ممنوع التحدث بالعربي في الرومات الإنجليزية، وممنوع التحدث بالإنجليزي في الرومات العربية. يجب استخدام اللغة المناسبة لكل شات.
✦ 𝟴. احترام الإدارة
يجب الالتزام بكلام الإدارة وعدم الجدال أو مخالفة التعليمات.
⚠️ نظام العقوبات (PUNISHMENT SYSTEM)
▸ المخالفة الأولى → تحذير
▸ المخالفة الثانية → تايم أوت
▸ تكرار المخالفات → تايم أوت أطول
▸ الاستمرار بالمخالفة → باند دائم (Permanent Ban)
╰─── ✦ 𝐄𝐍𝐃 𝐎𝐅 𝐑𝐔𝐋𝐄𝐒 ✦ ───╯
{<@1354932825610256647> }
{<@984962229336145940> }
''',
            color=discord.Color.green()
        )
        # الرد هنا مخفي (ephemeral=True) يراه المستخدم الذي ضغط فقط
        await interaction.response.send_message(embed=ar_embed, ephemeral=True)

    # زر اللغة الإنجليزية
    @discord.ui.button(label="English", style=discord.ButtonStyle.secondary, emoji="🇺🇸", custom_id="lang_en")
    async def english_button(self, interaction: discord.Interaction, button: Button):
        # إنشاء إيمبد الرد الإنجليزي
        en_embed = discord.Embed(
            title="englich ruels",
            description='''
╭─── ✦ 𝐊𝐋𝐀𝐒𝐇 𝐒𝐄𝐑𝐕𝐄𝐑 𝐑𝐔𝐋𝐄𝐒 ✦ ───╮
✦ 𝟭. Respect
It is strictly forbidden to insult, disrespect, practice racism, or belittle anyone in any way.
✦ 𝟮. Inappropriate Content
It is forbidden to send any inappropriate images, messages, or comments that violate public decency.
✦ 𝟯. Spam and Repetition
It is forbidden to send repetitive messages, spam, or disturb members within the chat.
✦ 𝟰. Advertisements
Advertising for any server or link without management's permission is forbidden.
✦ 𝟱. Violating Content
Any NSFW, disturbing, or annoying content that causes discomfort to members is forbidden.
✦ 𝟲. Channel Usage
Every channel is designated for its specific purpose; please commit to it and do not disrupt or go off-topic.
✦ 𝟳. Language
It is forbidden to speak Arabic in English channels, and forbidden to speak English in Arabic channels. The appropriate language must be used for each chat.
✦ 𝟴. Respecting Management
You must comply with the management's instructions and avoid arguing or violating directives.
⚠️ PUNISHMENT SYSTEM
▸ First violation → Warning
▸ Second violation → Timeout
▸ Repeated violations → Longer timeout
▸ Continuous violation → Permanent Ban
╰─── ✦ 𝐄𝐍𝐃 𝐎𝐅 𝐑𝐔𝐋𝐄𝐒 ✦ ───╯
{<@1354932825610256647> }
{<@984962229336145940> }
''',
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=en_embed, ephemeral=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    # لتسجيل الأزرار بحيث تعمل حتى لو أعدت تشغيل البوت لاحقاً
    bot.add_view(LanguageView())

# أمر لإرسال البانل الرئيسي إلى روم محدد
@bot.command()

async def send_panel(ctx, channel: discord.TextChannel = None):
    target_channel = channel or ctx.channel

    # تصميم البانل الرئيسي (Embed)
    main_embed = discord.Embed(
        title="اختر لغتك | Select Your Language",
        description="الرجاء الضغط على الزر أدناه لاختيار لغتك المفضلة.\n\nPlease click the button below to select your preferred language.",
        color=discord.Color.blue()
    )
    main_embed.set_thumbnail(url="https://iili.io/Clg0R1I.md.png")
    main_embed.set_image(url="https://iili.io/ClgZ9Kx.md.png")
    main_embed.set_footer(text="Language System")

    # إرسال البانل مع الأزرار
    await target_channel.send(embed=main_embed, view=LanguageView())


# ضع توكن البوت الخاص بك هنا
bot.run("MTUyNDIwMzk4NTgyMzU5Njc3NQ.GMCQPW.d1brJsE4MfDaRaZTnnFsyHzDhwVmBo74ftW1Bs")