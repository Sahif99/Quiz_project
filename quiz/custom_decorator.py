from quiz import settings 
def response_modify_decorator_list_or_get_after_execution_for_onoff_pagination(func): 
    def inner(self, request, *args, **kwargs): 
        response = func(self, request, *args, **kwargs) 
        print('response----->', response) 
        data_dict = {} 
        #data_dict['status_code'] = response.status_code 
        print("after Execution") 
        if 'results' in response.data: 
            data_dict = response.data 
        else: 
            data_dict['results'] = response.data 
        if response.data: 
            data_dict['request_status'] = 1 
            # data_dict['msg'] = settings.MSG_SUCCESS 
        elif len(response.data) == 0: 
            data_dict['request_status'] = 1 
        # data_dict['msg'] = settings.MSG_NO_DATA 
        else: 
            data_dict['request_status'] = 0 
        # data_dict['msg'] = settings.MSG_ERROR 
        response.data = data_dict 
        return response 
    return inner 
def response_modify_decorator_get(func): 
    def inner(self, request, *args, **kwargs): 
        print("model", self._module) 
        response = super(self.class_, self).get(self, request, args, kwargs) 
        print("before Execution") 
        data_dict = {} 
        data_dict['result'] = response.data 
        # data_dict['status_code'] = response.status_code 
        if response.data: 
            data_dict['request_status'] = 1 
            # data_dict['msg'] = settings.MSG_SUCCESS 
        elif len(response.data) == 0: 
            data_dict['request_status'] = 1 
            # data_dict['msg'] = settings.MSG_NO_DATA 
        else: 
            data_dict['request_status'] = 0 
            # data_dict['msg'] = settings.MSG_ERROR 
            response.data = data_dict 
            return response 
        # getting the returned value func(self, request, *args, **kwargs) 
        print("after Execution") 
        # returning the value to the original frame 
        return inner