"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Import for CSV Plugin
from botcity.plugins.csv import BotCSVPlugin

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    planilha = BotCSVPlugin()

    dados = planilha.read(r"C:\Bots\BotWorkSpace\bot-fakturama\resources\produtos\items.csv").as_list()

    bot = DesktopBot()

    # Implement here your logic...

    bot.execute(r"C:\Program Files\Fakturama2\Fakturama.exe")

    for item in dados:

    # Searching for element 'new_product'
        if not bot.find("new_product", matching=0.97, waiting_time=10000):
            not_found("new_product")
        bot.click()
        
        # Searching for element 'item_number'
        if not bot.find("item_number", matching=0.97, waiting_time=10000):
            not_found("item_number")
        bot.click_relative(112, 7)

        # item number
        bot.paste(item[1])
        bot.tab()

        # name
        bot.paste(item[2])
        bot.tab()

        # category
        bot.paste(item[3])
        bot.tab()

        # GTIN
        bot.paste(item[4])
        bot.tab()

        # supcode
        bot.paste(item[5])
        bot.tab()

        # description
        bot.paste(item[6])
        bot.tab()

        # price
        bot.control_a()
        bot.paste(item[7])
        bot.tab()

        # cost price
        bot.control_a()
        bot.paste(item[8])
        bot.tab()

        # allowance
        bot.control_a()
        bot.paste(item[9])
        bot.tab()
        
        # VAT
        # Searching for element 'vat'
        if not bot.find("vat", matching=0.97, waiting_time=20000):
            not_found("vat")
        bot.click_relative(107, 8)

        # Searching for element 'free_of_tax'
        if not bot.find("free_of_tax", matching=0.97, waiting_time=20000):
            not_found("free_of_tax")
        bot.click()
        bot.tab()

        # quantity
        bot.control_a()
        bot.paste(item[14])

        # Searching for element 'select_picture'
        if not bot.find("select_picture", matching=0.97, waiting_time=20000):
            not_found("select_picture")
        bot.click()

        bot.paste(rf"C:\Bots\BotWorkSpace\bot-fakturama\resources\produtos\imagens_produtos\{item[13]}")
        bot.enter()

        # save
        # Searching for element 'save'
        if not bot.find("save", matching=0.97, waiting_time=20000):
            not_found("save")
        bot.click()
        
        # close form
        bot.control_w()

        # close fakturama
        bot.alt_f4()


    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
        main()