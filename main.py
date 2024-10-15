import Collector


urls: list[str] = Collector.ReadWebsites("top-10000-websites.txt", 10)
Collector.Collect(urls, 10)