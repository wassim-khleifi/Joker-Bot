import discord
from discord.ext import commands
import datetime
import random
import economy
from economy.vars import *
import config
from config import *
import json
import economy
from economy.system import *
bot = commands.Bot(command_prefix= prefix, case_insensitive=True  , intents=discord.Intents.all(), help_command=None)
@bot.command(aliases=['bal'])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f'{ctx.author.name} Balance',color = discord.Color.random())
    em.add_field(name="**Wallet Balance**", value=f"`{wallet_amt}`")
    em.add_field(name="**Bank Balance**",value=f"`{bank_amt}`")
    await ctx.send(embed= em)


@bot.command()
@commands.cooldown(1, 60 * 30, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(30)
    bg = discord.Embed(title=f"**{user}**" , description=f"""
Someone Gave You `{earnings}` Coins !""" , color = discord.Colour.random())

    await ctx.reply(embed=bg)

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)



@bot.command()
@commands.cooldown(1, 60 * 60 * 5 , commands.BucketType.user)
async def work(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randint(50 , 150)
    bg = discord.Embed(title=f"**{user} Job**" , description=f"""
You Got `{earnings}` For Working Today!""" , color = discord.Colour.random())

    await ctx.reply(embed=bg)

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)

##############################################

@bot.command(aliases=['with'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    withdraw = discord.Embed(title=f"{ctx.author.name}", description=f"""
You Have Withdrawed `{amount}` From Your Bank!""" , color=discord.Colour.random())
    await ctx.reply(embed=withdraw)

@bot.command(aliases=['give'])
@commands.is_owner()
async def addmoney(ctx,member:discord.Member=None,amount : int=None):
    if member ==None:
        await ctx.reply("Please Metion A Member")
    elif amount==None:
        await ctx.reply("Please Enter Amount")
    else:
        await open_account(ctx.author)
        user = member
        users = await get_bank_data()
        bg = discord.Embed(title=f"**{user} Job**" , description=f"""
Owner {ctx.author.mention} Donated `{amount}` to {member.mention}""" , color = discord.Colour.random())
        await ctx.reply(embed=bg)
        users[str(user.id)]["wallet"] += amount
        with open("mainbank.json",'w') as f:
            json.dump(users,f)

@bot.command()
@commands.is_owner()
async def kill(ctx,member:discord.Member=None):
    if member ==None:
        await ctx.reply("Please Metion A Member")
    else:
        await open_account(ctx.author)
        user = member
        users = await get_bank_data()
        bg = discord.Embed(title=f"**{user} Job**" , description=f"""
Owner {ctx.author.mention} Killed {member.mention}
{member.mention} All Coins Down!""" , color = discord.Colour.random())
        await ctx.reply(embed=bg)
        users[str(user.id)]["wallet"] = 0
        with open("mainbank.json",'w') as f:
            json.dump(users,f)
@bot.command(aliases=['dep'])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    dep = discord.Embed(title=f"{ctx.author.name}", description=f"""
You Have Deposited `{amount}` To Your Bank!""" , color=discord.Colour.random())
    await ctx.reply(embed=dep)


@bot.command(aliases = ["rich"])
async def richest(ctx,x = 1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        name = ctx.message.guild.get_member(id_)
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = True)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)

#################################################
async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json','w') as f:
        json.dump(users,f)

    return True

async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)

    return users


async def update_bank(user,change=0,mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json','w') as f:
        json.dump(users,f)
    bal = users[str(user.id)]['wallet'],users[str(user.id)]['bank']
    return bal