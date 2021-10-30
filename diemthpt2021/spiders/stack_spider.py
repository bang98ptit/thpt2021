import json
from abc import ABC

from scrapy import Spider, Request

from diemthpt2021.items import Diemthpt2021Item


class DiemTHPTSpider(Spider, ABC):
    name = 'thpt'
    allowed_domains = ['d3ewbr0j99hudd.cloudfront.net']

    code = 200

    def start_requests(self):
        url_start = 'https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/{}{}.json'
        for i in range(1, 65):
            j = 1
            while self.code == 200:
                if i < 10:
                    province_code = '0' + str(i)
                else:
                    province_code = str(i)
                if j < 100000:
                    sbd = (6 - len(str(j))) * '0' + str(j)
                else:
                    sbd = str(j)
                yield Request(url_start.format(province_code, sbd), callback=self.parse)
                j += 1

    def parse(self, response):
        data = json.loads(response.body)
        item = Diemthpt2021Item()
        if data['A00'] == '':
            item['ka00'] = '-1'
        else:
            item['ka00'] = data['A00']
        if data['A01'] == '':
            item['ka01'] = '-1'
        else:
            item['ka01'] = data['A01']
        if data['B00'] == '':
            item['kb00'] = '-1'
        else:
            item['kb00'] = data['B00']
        if data['C00'] == '':
            item['kc00'] = '-1'
        else:
            item['kc00'] = data['C00']
        if data['CODE_NGOAINGU'] == '':
            item['codeNgoaiNgu'] = '-1'
        else:
            item['codeNgoaiNgu'] = data['CODE_NGOAINGU']
        if data['D01'] == '':
            item['kd01'] = '-1'
        else:
            item['kd01'] = data['D01']
        if data['DIA'] == '':
            item['mDia'] = '-1'
        else:
            item['mDia'] = data['DIA']
        if data['GDCD'] == '':
            item['mGdcd'] = '-1'
        else:
            item['mGdcd'] = data['GDCD']
        if data['HKTN'] == '':
            item['mHktn'] = '-1'
        else:
            item['mHktn'] = data['HKTN']
        if data['HKXH'] == '':
            item['mHkxh'] = '-1'
        else:
            item['mHkxh'] = data['HKXH']
        if data['HOA'] == '':
            item['mHoa'] = '-1'
        else:
            item['mHoa'] = data['HOA']
        if data['LY'] == '':
            item['mLy'] = '-1'
        else:
            item['mLy'] = data['LY']
        if data['NGOAINGU'] == '':
            item['mNgoaiNgu'] = '-1'
        else:
            item['mNgoaiNgu'] = data['NGOAINGU']
        if data['SINH'] == '':
            item['mSinh'] = '-1'
        else:
            item['mSinh'] = data['SINH']
        if data['SU'] == '':
            item['mSu'] = '-1'
        else:
            item['mSu'] = data['SU']
        if data['TOAN'] == '':
            item['mToan'] = '-1'
        else:
            item['mToan'] = data['TOAN']
        if data['VAN'] == '':
            item['mVan'] = '-1'
        else:
            item['mVan'] = data['VAN']
        if data['groupCode'] == '':
            item['groupCode'] = '-1'
        else:
            item['groupCode'] = data['groupCode']
        if data['groupName'] == '':
            item['groupName'] = '-1'
        else:
            item['groupName'] = data['groupName']
        if data['schoolYear'] == '':
            item['schoolYear'] = '-1'
        else:
            item['schoolYear'] = data['schoolYear']
        if data['stt'] == '':
            item['stt'] = '-1'
        else:
            item['stt'] = data['stt']
        if data['studentCode'] == '':
            item['studentCode'] = '-1'
        else:
            item['studentCode'] = data['studentCode']
        self.code = response.status
        yield item
