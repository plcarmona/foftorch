#module to get price of a BTC of the last 5 years every 4 hours
import pandas as pd
from binance.client import Client
from lightning.pytorch import LightningDataModule
from torch.utils.data import DataLoader

client = Client("ZH0rsgot9SuWzRL7DeIXMJ1CHNWToxOG9bZ8yIDv7g39n9tKtTAu4V78acGXuIIQ","4Y0jy8b4F0lPTowgsSnhaas9rskrmIEl3vNcHHr0q91yACWO8kNEjAHBKldAzJa8")
def gethourlydata(symbol,tf='4h',lookback='100 days ago UTC'):
    frame = pd.DataFrame(client.get_historical_klines(symbol, tf, lookback))
    frame= frame[[0,1,2,3,4,5]]
    frame.columns=['time','open','high','low','close','volume']
    frame.open =frame.open.astype(float)
    frame.close=frame.close.astype(float)
    frame.low=frame.low.astype(float)
    frame.high=frame.high.astype(float)
    frame.volume=frame.volume.astype(float)
    frame.time=pd.to_datetime(frame.time,unit='ms')
    return frame



