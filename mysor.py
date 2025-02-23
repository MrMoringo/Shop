#PRICE = types.LabeledPrice(label="Дрон 5 дюймов", amount=500*100)  # в копейках (руб)

#@dp.message_handler(commands=['buy'])
#async def buy(message: types.Message):
#    if config.PAYMENTS_TOKEN.split(':')[1] == 'Продукт':
#        await bot.send_message(message.chat.id, "Оплата первого продукта")
# 
#    await bot.send_invoice(message.chat.id,
#                           title="Дрон 5 дюймов",
#                           description="Покупка дрона",
#                           provider_token=config.PAYMENTS_TOKEN,
#                           currency="rub",
#                           photo_url="https://avatars.mds.yandex.net/i?id=e6807e171314f679e1b5db1b5f2fb515_l-12486332-images-thumbs&n=13",
#                           photo_width=1000,
#                           photo_height=1000,
#                          prices=[PRICE],
#                           start_parameter="one-month-subscription",
#                           payload="test-invoice-payload")
#@dp.pre_checkout_query_handler(lambda query: True)
#async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
#    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
#
#@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
#async def successful_payment(message: types.Message):
#    print("SUCCESSFUL PAYMENT:")
#    payment_info = message.successful_payment.to_python()
#    for k, v in payment_info.items():
#        print(f"{k} = {v}")
#
#    await bot.send_message(message.chat.id,
#                           f"Платёж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")