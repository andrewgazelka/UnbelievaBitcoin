from discord.ext import commands
import discord
from credentials import DiscordToken
from exchanges.bitfinex import Bitfinex
import sys
# logging.basicConfig(level=logging.DEBUG)
bot = commands.Bot(command_prefix='bit!', case_insensitive=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def value(ctx):
    price = Bitfinex().get_current_price()
    priceembed = discord.Embed(title=f'**Price of 1 BTC:** {price}',type='rich',url='https://www.bitfinex.com/')
    await ctx.send(embed=priceembed)
@bot.command()
async def buy(ctx,*,amount):
    price = Bitfinex().get_current_price()
    if amount.isdigit():
        amount = int(amount)
        payable = price * amount
        await ctx.send(f'Please send {payable} UnBelievaBoat currency to me and type b!check')
    else:
        await ctx.send('no')
@bot.command()
@commands.is_owner()
async def kill(ctx):
    sys.exit()


@bot.command()
async def help(ctx):
    help_embed = discord.Embed(title="**Commands**", color=0x00afff, type="rich", url="https://github.com/dxf/Alexa",
                               footer="*All commands are prefixed with \"bit!\"")
    help_embed.add_field(name="**All Users**",
                         value="asdf")
    help_embed.add_field(name="**Bot Owner**", value="Kill - Kills the bot.")
    help_embed.set_footer(text='All commands are prefixed with \"bit!\"')
    await ctx.send(embed=help_embed)
def error():
    bot.add_cog(CommandErrorHandler(bot))


bot.run(DiscordToken)
