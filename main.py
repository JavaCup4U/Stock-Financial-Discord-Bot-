#dependencies 
import os
import discord
import requests
import json
import random
from bs4 import BeautifulSoup
from keep_alive import keep_alive
from urllib.request import urlopen
import finplot as fplt
import yfinance
import pandas as pd
import finvizfinance
from finvizfinance.quote import finvizfinance


#############################################################################
############################  tickers ###########################
aapl_stock = finvizfinance('aapl')

crm_stock = finvizfinance('crm')

msft_stock = finvizfinance('msft')

pltr_stock = finvizfinance('pltr')

amd_stock = finvizfinance('amd')

client = discord.Client()



########################## real time price for tickers #################################



#FOR APPLE 
def get_stock_price():
  response = requests.get("https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=1fabfb443fb550f28a2d8c94710e65d3")
  json_data1 = json.loads(response.text)


  stock_price = json_data1[0]['symbol'],'current price:' , json_data1[0]['price'],'current volume: ', json_data1[0]['volume']
  return(stock_price)

#FOR MSFT
def get_stock_price1():
  response = requests.get("https://financialmodelingprep.com/api/v3/quote-short/MSFT?apikey=1fabfb443fb550f28a2d8c94710e65d3")
  json_data2 = json.loads(response.text)
  stock_price = json_data2[0]['symbol'], 'current price:' , json_data2[0]['price'],'current volume: ', json_data2[0]['volume']
  return(stock_price)

#for crm 

def get_crm_q():
  response = requests.get("https://financialmodelingprep.com/api/v3/quote-short/CRM?apikey=1fabfb443fb550f28a2d8c94710e65d3")
  json_crm = json.loads(response.text)
  crm_quote = json_crm[0]['symbol'],' current price:', json_crm[0]['price'],' current volume: ',json_crm[0]['volume']
  return(crm_quote)


#for pltr
def get_pltr_q():
  response = requests.get("https://financialmodelingprep.com/api/v3/quote-short/PLTR?apikey=1fabfb443fb550f28a2d8c94710e65d3")
  json_pltr = json.loads(response.text)
  pltr_q = json_pltr[0]['symbol'], '  current price: ', json_pltr[0]['price'], '  current volume: ', json_pltr[0]['volume']
  return(pltr_q)

#for spy
def get_spy_q():
  response = requests.get("https://financialmodelingprep.com/api/v3/quote-short/SPY?apikey=1fabfb443fb550f28a2d8c94710e65d3")
  json_spy = json.loads(response.text)
  spy_q = json_spy[0]['symbol'], '  current price: ', json_spy[0]['price'], '  current volume: ', json_spy[0]['volume']
  return(spy_q)
#################################### end ##########################################################


########################client run#############################################################
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))



############################# end ####################################################



@client.event
async def on_message(message):
  if message.author == client:
    return

######################## stock quote prices ####################################################

  if message.content.startswith('!AAPL'):
    stock_price = get_stock_price()
    await message.channel.send(stock_price)

  if message.content.startswith('!MSFT'):
    stock_price = get_stock_price1()
    await message.channel.send(stock_price)

  if message.content.startswith('!CRM'):
    stock_price = get_crm_q()
    await message.channel.send(stock_price)
  
  if message.content.startswith('!PLTR'):
    stock_price = get_pltr_q()
    await message.channel.send(stock_price)

  if message.content.startswith('!SPY'):
    stock_price = get_spy_q()
    await message.channel.send(stock_price)

#################################### end ##################################################

#################################chart data ##############################################
  if message.content.startswith('!cd aapl'):
   await message.channel.send(aapl_stock.TickerCharts('daily', 'candle', urlonly=False))

  if message.content.startswith('!cd crm'):
    await message.channel.send(crm_stock.TickerCharts('daily', 'candle', urlonly=False))

  if message.content.startswith('!cd msft'):
    await message.channel.send(msft_stock.TickerCharts('daily', 'candle', urlonly=False))
  
  if message.content.startswith('!cd pltr'):
    await message.channel.send(pltr_stock.TickerCharts('daily', 'candle', urlonly=False))

  if message.content.startswith('!cd amd'):
    await message.channel.send(amd_stock.TickerCharts('daily', 'candle', urlonly=False))




#################################################END#########################################


  ################TICKER NEWS####################




keep_alive()
client.run( os.getenv('TOKEN'))
