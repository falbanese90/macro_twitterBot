This script extracts Macro Events from [Trading Economics](https://www.tradingeconomics.com/calendar),
executes java to select current week and and most important headlines,
and posts event to twitter on a weekly basis.

>This program was made to exercise what I learned about selenium calendar
Beautiful Soup.

The script will require an executable driver file for your web browser
for Selenium to access.

It will also require a profile with the twitter API and the necessary access codes.

I am looking to expand on this by:

1. Adding dates and times to the headlines.
2. Having the bot tweet the result when the headline actually prints.
3. Adding an email function.
4. Have it load an excel file that will be populated to a Google
   Spreadsheet for further tracking analysis.
