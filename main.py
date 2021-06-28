from processor import process
import time
import schedule

def scheduler():
    # process.current_value()
    process.fit()
    # process.buy_and_sell_same_day()
    # schedule.every(120).seconds.do(process.current_value)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

if __name__ == '__main__':
   scheduler()

