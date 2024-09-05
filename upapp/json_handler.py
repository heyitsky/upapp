class JSONHandler:
    def get_data(self, response):        
        if "data" in response:
            data = []
            data_list = []            
            for element in response["data"]:
                data.append(element)
            data_list.append(data)
            if "links" in response:
                links = []
                for element in response["links"]:
                    links.append(element)
                data_list.append(links)
            return data_list
        # TO DO: return data list and 2 flags, whether a next page exists or a prev page exists.