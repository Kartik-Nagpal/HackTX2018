const zerorpc = require("zerorpc")
let client = new zerorpc.Client()
client.connect("tcp://127.0.0.1:4242")


client.invoke("echo", "server ready", (error, res) => {
  if(error || res !== 'server ready') {
    console.error(error)
  } else {
    console.log("server is ready")
  }
})

function getData(){
    // Get data from email input field
    emailText = document.getElementById("email").value
    // console.log(emailText)

    const zerorpc = require("zerorpc")
    let client = new zerorpc.Client()
    client.connect("tcp://127.0.0.1:4242")

    // Get data from file selector
    var filePathsRaw = document.getElementById("files").files
    var filePaths = ""

    //check if files is empty
    if(filePathsRaw.length == 0){
        console.log("No documents chosen")
    }
    //check email.
    else if(emailText.length == 0){
        console.log("No email")
    }
    else {
        for (i = 0; i < filePathsRaw.length; i++){
            filePaths += filePathsRaw[i].path + ","
        }
        
        // console.log(filePaths)

        client.invoke("transmitData", filePaths, (error, res) => {
            if(error) {
                console.error(error)
            } else {
                console.log(res)
            }
        })
    }
}

document.querySelector('#email')
