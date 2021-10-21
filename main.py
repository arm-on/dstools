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


def colab_prevent_disconnection():
    '''
    Prevents Colab Session from Being Closed
    '''
    import IPython
    from google.colab import output

    display(IPython.display.Javascript('''
    function ClickConnect(){
    btn = document.querySelector("colab-connect-button")
    if (btn != null){
        console.log("Click colab-connect-button"); 
        btn.click() 
        }
    
    btn = document.getElementById('ok')
    if (btn != null){
        console.log("Click reconnect"); 
        btn.click() 
        }
    }
    
    setInterval(ClickConnect,60000)
    '''))

    print("Done.")


def kaggle_link(file_path):
    '''
    Given a file path, outputs the direct link to that file over the internet
    '''
    from IPython.display import FileLink
    return FileLink(file_path)