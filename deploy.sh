# rm line_mtg_bot.zip
# cd packages
# zip -r ../line_mtg_bot.zip *
# cd ..
zip -g line_mtg_bot.zip *.py
zip -g line_mtg_bot.zip models/*.py
zip -g line_mtg_bot.zip config.json
aws lambda update-function-code --function-name Line_MTG_Bot --zip-file fileb://line_mtg_bot.zip