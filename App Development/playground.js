fetch('http://localhost:3000', {
    method:'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
    body: JSON.stringify({"CompanyName":'Rohit'})
    }).then((content) => content.json()).then(function(content){
        console.log(content)
        cname.innerHTML =fname
    }).catch(function(e)
    {
        console.log(e)
    });