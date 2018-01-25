from baike import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.url_manager = url_manager.UrlManger()
        self.html_downloader = html_downloader.HtmlDownloader()
        self.html_parser = html_parser.HtmlParser()
        self.html_outputer = html_outputer.HtmlOutputer()


    def craw(self, root_url, page):
        count = 1
        self.url_manager.add_new_url(root_url)
        while self.url_manager.has_new_url():
            try:
                new_url = self.url_manager.get_new_url()
                print("craw %d : %s" %(count,new_url))
                html_content = self.html_downloader.download(new_url)
                new_urls,new_data = self.html_parser.parse(new_url,html_content)
                self.url_manager.add_new_urls(new_urls)

                self.html_outputer.collect_data(new_data)
                if count >= page:
                    break
                count += 1

            except Exception as e:
                print(str(e))

            self.html_outputer.output_html()



if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    page = 1000
    obj_spider = SpiderMain()
    obj_spider.craw(root_url,page)