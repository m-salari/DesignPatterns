"""
    Adapter
        - a structural design pattern that allows objects with incompatible interfaces to collaborate.

"""
import xmltodict


class Application:
    def send_request(self):
        return 'data.xml'


class Analytic:
    def receive_request(self, json):
        return json


class Adapter:
    def concert_xml2json(self, file):
        with open(file, 'r') as my_file:
            # convert to json
            data_dict = xmltodict.parse(my_file.read())
        return data_dict


def client():
    data_xml = Application().send_request()
    converted_data = Adapter().concert_xml2json(data_xml)
    receiver = Analytic().receive_request(converted_data)
    print(receiver)


client()