import os

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', 'pk_test_51PlXvOFaq5KzR1tRSP9TRkF8WsU7cMkRudIYueRuo5mcwiuBrWIjkY1x8TrEBeBPU9MeyKv8VXgnFJqNHvxLPYnV00VbYktpRU')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', 'sk_test_51PlXvOFaq5KzR1tRHkARqAkTA4hZnaGxTGokeKROSaIvVdlrQsWX2ZFJ7GrjaOHMcgeS6z5thzE4ik55YCeDL3Eh00UXnXTF9M')