class JSONHandler:
    def get_data(self, response):
        if "data" in response:
            data_list = []
            for element in response["data"]:
                data_list.append(element)
            return data_list