import urllib.request, datetime, logging

class GoogleFinance:

    def __init__(self, symbol=None, start_date=None):
        self.symbol = symbol
        self.start_date = start_date
        self.base_url = "http://www.google.com/finance/historical?q="
        logging.info("Started an instance of google finance with {} and {}".format(self.symbol, self.start_date))

    def get_historical_stock_data(self, fileName):
        today_date_time = datetime.datetime.today()
        today_date = datetime.date(today_date_time.year, today_date_time.month, today_date_time.day)
        company_url = self.base_url + self.symbol + "&startdate=" + self.start_date \
                      + "&enddate=" + str(today_date) + "&output=csv"
        print(company_url)
        logging.info(company_url)
        url_data = urllib.request.urlopen(company_url)
        csv = (url_data.read()).decode("utf - 8 - sig").encode("utf -8")

        if fileName is not None:
            try:
                file = open(fileName, "w")
                file.write(csv.decode("utf-8"))
                file.close()
            except FileNotFoundError as e:
                logging.error(e.filename)