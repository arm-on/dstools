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