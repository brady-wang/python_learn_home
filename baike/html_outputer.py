__author__ = 'wang'


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return None
        self.datas.append(data)



    def output_html(self):
        fout = open("output.html",'w',encoding='utf-8')
        fout.write("<html><body>")
        for data in self.datas:
            fout.write("<a href = '%s'> %s </a>" %(data['url'],data['title']))
            fout.write('<p>%s</p>' % data['summary'])
        fout.write("</body></html>")
        fout.close()

