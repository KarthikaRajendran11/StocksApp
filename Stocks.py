import sys, time, configparser, logging

import GoogleFinance

if __name__  == "__main__":
    try:
        config = configparser.RawConfigParser()
        config.read("stocks.cfg")
    except FileNotFoundError as e:
        print("Opening config file failed")
        sys.exit(1)

    if config.has_option("LOGGING", "LOG_FILE"):
        file_name = config["LOGGING"]["LOG_FILE"]
    else:
        file_name = "default.log"

    print(file_name)

    try:
        log = logging.basicConfig(filename=file_name, level=logging.DEBUG,
                              format="%(asctime)s,%(message)s", datefmt="%m/%d/%y")
    except Exception as e:
        print("Creating log object failed")
        sys.exit(2)

    logging.info("Program started")

    sections = config.sections()
    # List comprehension
    symbol = [section for section in sections if section != "LOGGING"]
    print(symbol)
    stock_date = config[symbol[0]]["DATE"]
    print(stock_date)
    struct_time = time.strptime(stock_date, "%d %B %Y")
    print(str(struct_time))

    googleFinance = GoogleFinance.GoogleFinance(symbol[0], time.strftime("%Y-%m-%d", struct_time))
    s_stock = symbol[0] + ".csv"
    print(s_stock)
    googleFinance.get_historical_stock_data(s_stock)
    logging.info("Program done")
    sys.exit(0)




