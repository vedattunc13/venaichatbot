from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Örnek veri
texts = ["Merhaba dünya!", "Python ile veri bilimi"]

# Veriyi bir DataFrame'e dönüştür
df = pd.DataFrame(texts, columns=['text'])

# Basit bir metin vektörizer kullanımı
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])

print(X.toarray())

# Botun token'ı (BotFather'dan aldığın token'ı buraya yapıştır)
TOKEN = '7529075347:AAH4W7z8dEwH_0T3_-2aZw9PpThxq3ms0m0'

# Loglama ayarları
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# /start komutu
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Merhaba! Ben senin sohbet botunum.")

# Kullanıcı mesajlarına yanıt verme
def echo(update: Update, context: CallbackContext):
    user_message = update.message.text
    update.message.reply_text(f"Sen şöyle dedin: {user_message}")

# Hata durumu
def error(update: Update, context: CallbackContext):
    logger.warning(f'Update "{update}" caused error "{context.error}"')

def main():
    # Bot'u başlatma
    updater = Updater(TOKEN, use_context=True)

    # Dispatcher, komutları ve mesajları yönetir
    dp = updater.dispatcher

    # /start komutu için handler
    dp.add_handler(CommandHandler("start", start))

    # Mesajları aynen yanıtlayan handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Hataları loglayan handler
    dp.add_error_handler(error)

    # Botu başlat
    updater.start_polling()

    # Botu çalışır halde tut
    updater.idle()

if __name__ == '__main__':
    main()Enter
