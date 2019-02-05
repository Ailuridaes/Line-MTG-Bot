rm line_mtg_bot.zip
cd package
zip -r ../line_mtg_bot.zip *
cd ..
zip -g line_mtg_bot.zip line_mtg_bot.py
zip -g line_mtg_bot.zip config.json
aws lambda update-function-code --function-name Line_MTG_Bot --zip-file fileb://line_mtg_bot.zip