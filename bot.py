import discord
from discord.ext import commands
from datetime import datetime

#Intent
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)




@bot.event

#Send DM on script load
async def on_ready():
    user_id = YOUR_USER_ID_HERE  # Replace with the user ID of the user you wish to DM on each script load
    
    # Get current date and time
    now = datetime.now()        
    current_time = now.strftime("%m/%d/%Y-%I:%M %p") #Time format in standard time (Month/Day/Year - Hour:Minute AM/PM)
    
    #Message Content
    message_content = f"I am online! {current_time}"
    
    #Fetch userid
    user = await bot.fetch_user(user_id)
    if user:
        await user.send(message_content)
        print("Message sent to the user!")
    else:
        print("User not found!")

    await bot.close() #Logs the bot out and kills the script once message is sent

bot.run('YOUR BOTS SECRET/KEY HERE')

