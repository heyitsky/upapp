class JSONHandler:
    def get_data(self, response):
        if "data" in response:
            data_list = []
            for element in response["data"]:
                data_list.append(element)
            return data_list
        # return data list and 2 flags, whether a next page exists or a prev page exists.