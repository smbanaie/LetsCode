from scrapy import cmdline
cmdline.execute("scrapy crawl isna -o news.csv -t csv".split())
# cmdline.execute("scrapy crawl test -o items.csv -t csv".split())