async function sendMessage(){

let msg = document.getElementById("msg").value;

let response = await fetch("/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body: JSON.stringify({message: msg})
});

let data = await response.json();

document.getElementById("chat").innerHTML += "<p>"+data.reply+"</p>";
}