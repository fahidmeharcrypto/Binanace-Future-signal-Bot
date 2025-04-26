import random

def signal_generator():
    # Simple random signal (Buy or Sell)
    signals = ['Buy', 'Sell']
    return random.choice(signals)
