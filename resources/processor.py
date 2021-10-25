def gpu_tpu():
    '''
    Get the information about GPU or TPU's available
    '''
    try:
        import pynvml
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        device_name = pynvml.nvmlDeviceGetName(handle)
        return device_name
    except:
        try:
            import os
            from tensorflow.python.profiler import profiler_client

            tpu_profile_service_address = os.environ['COLAB_TPU_ADDR'].replace('8470', '8466')
            return profiler_client.monitor(tpu_profile_service_address, 100, 2)
        except:
            return 'running on CPU'

