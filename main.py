import discord
import os
from datetime import datetime


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


year_month = datetime.now()


@client.event
async def on_ready():
        print(f'We have logged in as {client.user}')

@client.event
async def on_message(message,):
    global count_mute, count_ban, count_warn, year_month


    if message.content.startswith('/collection-statadmin'):
        print(year_month.year, year_month.month)
        print(message.author)
        os.mkdir(f'data//{str(message.author)}')
        all_stat = open(f'data//{message.author}//all_stat.txt', 'w')
        all_stat.write('0')
        month_ban = open(f'data//{message.author}//ban{str(year_month.year) + "." + str(year_month.month)}.txt', 'w')
        month_ban.write('0')
        month_mute = open(f'data//{message.author}//mute{str(year_month.year) + "." + str(year_month.month)}.txt', 'w')
        month_mute.write('0')
        month_warn = open(f'data//{message.author}//warn{str(year_month.year) + "." + str(year_month.month)}.txt', 'w')
        month_warn.write('0')
        all_ban = open(f'data//{message.author}//allban.txt', 'w')
        all_ban.write('0')
        all_mute = open(f'data//{message.author}//allmute.txt', 'w')
        all_mute.write('0')
        all_warn = open(f'data//{message.author}//allwarn.txt', 'w')
        all_warn.write('0')
        await message.channel.send(f'{message.author}, теперь бот отслеживает вашу статистику!')
    if message.content.startswith('!stat'):
        list_top = {}
        for filename in os.listdir("data"):
            for txtname in os.listdir(f"data/{filename}"):
                # print(txtname)    вывод папки юзера со статой
                if txtname == 'all_stat.txt':
                    with open(f'data/{filename}/{txtname}') as top_all_stat:
                        add_list_top = int(top_all_stat.read())
                        list_top[filename] = add_list_top
        # print(list_top)
        sort_list_top = dict(sorted(list_top.items(), reverse = True, key=lambda x: x[1]))
        print(sort_list_top)
        count_top = 1
        for i in sort_list_top.keys():
            if str(message.author) == str(i):
                print(f'Место в топе: {count_top}')
                break
            else:
                count_top += 1
        with open(f'data//{message.author}//all_stat.txt') as y_stat:
            num_txt_year = str(y_stat.read())
        with open(f'data//{message.author}//ban{str(year_month.year) + "." + str(year_month.month)}.txt') as m_stat:
            num_txt_month_ban = str(m_stat.read())
        with open(f'data//{message.author}//mute{str(year_month.year) + "." + str(year_month.month)}.txt') as m_stat:
            num_txt_month_mute = str(m_stat.read())
        with open(f'data//{message.author}//warn{str(year_month.year) + "." + str(year_month.month)}.txt') as m_stat:
            num_txt_month_warn = str(m_stat.read())
        with open(f'data//{message.author}//allban.txt') as all_ban:
            num_txt_allban = str(all_ban.read())
        with open(f'data//{message.author}//allwarn.txt') as all_warn:
            num_txt_allwarn = str(all_warn.read())
        with open(f'data//{message.author}//allmute.txt') as all_mute:
            num_txt_allmute = str(all_mute.read())


        text_stat = f'{message.author}' + '\n' + ':x:'  + f'Наказаний за все время: {num_txt_year}' + '\n'+ ':x:' + f'Кол-во банов за все время: {num_txt_allban } ' + f'За месяц: {num_txt_month_ban}' + '\n' +'\n' + f'Кол-во мутов за все время: {num_txt_allmute} ' + f'За месяц: {num_txt_month_mute}' + '\n' + '\n' + f'Кол-во пред за все время: {num_txt_allwarn} ' + f'За месяц: {num_txt_month_warn}' + '\n' + '\n' + f'Место в топе: {count_top}'
        await message.channel.send(text_stat)

    if message.content.startswith('/ban') or message.content.startswith('ban') or message.content.startswith('tempban') or message.content.startswith('/tempban'):
        if os.path.exists(f'data//{message.author}//ban{str(year_month.year) + "." + str(year_month.month)}.txt') != True:
            month_stat = open(f'data//{message.author}//ban{str(year_month.year) + "." + str(year_month.month)}.txt', 'w')
            month_stat.write('0')
        with open(f'data//{message.author}//ban{str(year_month.year) + "." + str(year_month.month)}.txt') as m_stat:     # открываем файл на чтение и присваиваем переменной num_txt_month число из txt файла
            num_txt_month = int(m_stat.read())
            num_txt_month += 1
        m_stat_write = open(f'data//{message.author}//ban{str(year_month.year) + "." + str(year_month.month)}.txt', 'w')
        m_stat_write.write(str(num_txt_month))
        with open(f'data//{message.author}//all_stat.txt') as y_stat:
            num_txt_year = int(y_stat.read())
            num_txt_year += 1
        y_stat_write = open(f'data//{message.author}//all_stat.txt', 'w')
        y_stat_write.write(str(num_txt_year))

        with open(f'data//{message.author}//allban.txt') as all_ban:
            num_txt_allban = int(all_ban.read())
            num_txt_allban += 1
        all_ban_write = open(f'data//{message.author}//allban.txt', 'w')
        all_ban_write.write(str(num_txt_allban))


    if message.content.startswith('/mute') or message.content.startswith('mute'):
        if os.path.exists(f'data//{message.author}//mute{str(year_month.year) + "." + str(year_month.month)}.txt') != True:
            month_stat = open(f'data//{message.author}//mute{str(year_month.year) + "." + str(year_month.month)}.txt', 'w')
            month_stat.write('0')
        with open(f'data//{message.author}//mute{str(year_month.year) + "." + str(year_month.month)}.txt') as m_stat:     # открываем файл на чтение и присваиваем переменной num_txt_month число из txt файла
            num_txt_month = int(m_stat.read())
            num_txt_month += 1
        m_stat_write = open(f'data//{message.author}//mute{str(year_month.year) + "." + str(year_month.month)}.txt', 'w')
        m_stat_write.write(str(num_txt_month))
        with open(f'data//{message.author}//all_stat.txt') as y_stat:
            num_txt_year = int(y_stat.read())
            num_txt_year += 1
        y_stat_write = open(f'data//{message.author}//all_stat.txt', 'w')
        y_stat_write.write(str(num_txt_year))

        with open(f'data//{message.author}//allmute.txt') as all_mute:
            num_txt_allmute = int(all_mute.read())
            num_txt_allmute += 1
        all_mute_write = open(f'data//{message.author}//allmute.txt', 'w')
        all_mute_write.write(str(num_txt_allmute))

    if message.content.startswith('pred'):
        if os.path.exists(f'data//{message.author}//warn{str(year_month.year) + "." + str(year_month.month)}.txt') != True:
            month_stat = open(f'data//{message.author}//warn{str(year_month.year) + "." + str(year_month.month)}.txt', 'w')
            month_stat.write('0')
        with open(f'data//{message.author}//warn{str(year_month.year) + "." + str(year_month.month)}.txt') as m_stat:     # открываем файл на чтение и присваиваем переменной num_txt_month число из txt файла
            num_txt_month = int(m_stat.read())
            num_txt_month += 1
        m_stat_write = open(f'data//{message.author}//warn{str(year_month.year) + "." + str(year_month.month)}.txt', 'w')
        m_stat_write.write(str(num_txt_month))
        with open(f'data//{message.author}//all_stat.txt') as y_stat:
            num_txt_year = int(y_stat.read())
            num_txt_year += 1
        y_stat_write = open(f'data//{message.author}//all_stat.txt', 'w')
        y_stat_write.write(str(num_txt_year))
        with open(f'data//{message.author}//allwarn.txt') as all_warn:
            num_txt_allwarn = int(all_warn.read())
            num_txt_allwarn += 1
        all_warn_write = open(f'data//{message.author}//allwarn.txt', 'w')
        all_warn_write.write(str(num_txt_allwarn))

client.run('___    MTA0MjE2O     _____    Dc5ODM4OTc      zOTY1MA.GBjDQv.dGFn      nHnkQ6nrZZaImJ_       4iec1n8dEJL      maa9g_R8')
