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

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    # Implement here your logic...

    bot.execute(r"C:\Program Files\Fakturama2\Fakturama.exe")

    # Searching for element 'new_product'
    if not bot.find("new_product", matching=0.97, waiting_time=20000):
        not_found("new_product")
    bot.click()
    
     # Searching for element 'item_number'
    if not bot.find("item_number", matching=0.97, waiting_time=10000):
        not_found("item_number")
    bot.click_relative(128, 5)

    # item number
    bot.paste("519")
    bot.tab()

    # name
    bot.paste("Lâmpada LED")
    bot.tab()

    # category
    bot.paste("Escritório")
    bot.tab()

    # GTIN
    bot.paste("2345678901234")
    bot.tab()

    # supcode
    bot.paste("DEF456")
    bot.tab()

    # description
    bot.paste("Lâmpada LED de mesa")
    bot.tab()

    # price
    bot.control_a()
    bot.paste("25,00")
    bot.tab()

    # cost price
    bot.control_a()
    bot.paste("15,00")
    bot.tab()

    # allowance
    bot.paste("0")
    bot.tab()
    
    # VAT
    # Searching for element 'vat'
    if not bot.find("vat", matching=0.97, waiting_time=10000):
        not_found("vat")
    bot.click_relative(107, 8)

    # Searching for element 'free_of_tax'
    if not bot.find("free_of_tax", matching=0.97, waiting_time=10000):
        not_found("free_of_tax")
    bot.click()

    

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