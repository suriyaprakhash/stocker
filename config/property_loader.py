import configparser

config = configparser.ConfigParser()

# this load the config dynamically
def load_config():
    config.read('resources/config.ini')
    config_stock_list = config['stock']['list']
    stock_list = config_stock_list.split(',')
    print(stock_list)
    return stock_list