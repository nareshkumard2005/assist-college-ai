from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("colleges.csv")
df.columns = df.columns.str.lower()

last_results = None
user_name = None


@app.route("/")
def home():
    return """

<!DOCTYPE html>
<html>

<head>

<title>Assist College AI</title>

<style>

:root{
--main:#f97316;
--main2:#fb923c;
--user:#f97316;
--bg:#1f2937;
--panel:white;
--text:black;
}

.dark{
--bg:#020617;
--panel:#111827;
--text:white;
}

*{
box-sizing:border-box;
font-family:Segoe UI;
}

body{
margin:0;
background:var(--bg);
height:100vh;
display:flex;
justify-content:center;
align-items:center;
color:var(--text);
}

.container{
width:420px;
height:90vh;
background:var(--panel);
border-radius:12px;
display:flex;
flex-direction:column;
overflow:hidden;
box-shadow:0 8px 25px rgba(0,0,0,0.25);
}

.header{
background:linear-gradient(90deg,var(--main),var(--main2));
color:white;
padding:14px;
font-weight:bold;
display:flex;
justify-content:space-between;
align-items:center;
}

.theme-tools{
display:flex;
align-items:center;
gap:8px;
}

.color{
width:14px;
height:14px;
border-radius:50%;
cursor:pointer;
}

.orange{background:#f97316}
.green{background:#22c55e}
.purple{background:#8b5cf6}

.theme{
cursor:pointer;
font-size:18px;
}

.chat{
flex:1;
overflow-y:auto;
padding:10px;
background:#f3f4f6;
}

.dark .chat{
background:#1e293b;
}

.msg{
padding:10px;
margin:6px 0;
border-radius:10px;
max-width:80%;
font-size:14px;
}

.user{
background:var(--user);
color:white;
margin-left:auto;
}

.bot{
background:#e5e7eb;
}

.dark .bot{
background:#334155;
color:white;
}

.input{
display:flex;
padding:8px;
gap:6px;
}

input{
flex:1;
padding:8px;
border-radius:6px;
border:1px solid #ccc;
}

button{
padding:8px 12px;
border:none;
background:var(--main);
color:white;
border-radius:6px;
cursor:pointer;
}

.suggestions{
display:flex;
gap:8px;
overflow-x:auto;
padding:10px;
background:#111827;
}

.suggestions button{
background:var(--main);
white-space:nowrap;
}

</style>

</head>

<body id="body">

<div class="container">

<div class="header">

<span>🤖 Assist College AI</span>

<div class="theme-tools">

<div class="color orange" onclick="theme('#f97316','#fb923c','#f97316')"></div>
<div class="color green" onclick="theme('#22c55e','#16a34a','#22c55e')"></div>
<div class="color purple" onclick="theme('#8b5cf6','#6366f1','#8b5cf6')"></div>

<span class="theme" onclick="toggleTheme()">🌙</span>

</div>

</div>


<div id="chat" class="chat">

<div class="msg bot">
Hello 👋 Welcome. What is your name?
</div>

</div>


<div class="input">

<input id="msg" placeholder="Type message...">

<button onclick="send()">Send</button>
<button onclick="newChat()">New</button>

</div>


<div class="suggestions">

<button onclick="quick('Top colleges in Chennai')">Top colleges in Chennai</button>
<button onclick="quick('Top colleges in Coimbatore')">Top colleges in Coimbatore</button>
<button onclick="quick('Best arts and science colleges')">Best arts and science colleges</button>
<button onclick="quick('Colleges with hostel')">Colleges with hostel</button>
<button onclick="quick('Affordable colleges')">Affordable colleges</button>
<button onclick="quick('Best women colleges')">Best women's colleges</button>
<button onclick="quick('Colleges in Madurai')">Colleges in Madurai</button>
<button onclick="quick('Government arts colleges')">Government arts colleges</button>

</div>

</div>


<script>

function theme(c1,c2,u){
document.documentElement.style.setProperty('--main',c1)
document.documentElement.style.setProperty('--main2',c2)
document.documentElement.style.setProperty('--user',u)
}

function toggleTheme(){
document.body.classList.toggle("dark")
}

function addUser(text){
let chat=document.getElementById("chat")
chat.innerHTML+=`<div class="msg user">${text}</div>`
chat.scrollTop=chat.scrollHeight
}

function typeBotMessage(text){

let chat=document.getElementById("chat")

let botDiv=document.createElement("div")
botDiv.className="msg bot"
chat.appendChild(botDiv)

let i=0
let temp=""

function type(){

if(i<text.length){

temp += text.charAt(i)

botDiv.innerHTML = temp

i++

chat.scrollTop=chat.scrollHeight

setTimeout(type,15)

}

}

type()

}


function send(){

let input=document.getElementById("msg")
let text=input.value.trim()

if(text==="") return

addUser(text)

let chat=document.getElementById("chat")
chat.innerHTML+=`<div class="msg bot">Thinking...</div>`

fetch("/ask",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({msg:text})
})
.then(res=>res.json())
.then(data=>{

document.querySelector(".msg.bot:last-child").remove()

typeBotMessage(data.reply)

})

input.value=""
}


function quick(q){

addUser(q)

let chat=document.getElementById("chat")
chat.innerHTML+=`<div class="msg bot">Thinking...</div>`

fetch("/ask",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({msg:q})
})
.then(res=>res.json())
.then(data=>{

document.querySelector(".msg.bot:last-child").remove()

typeBotMessage(data.reply)

})

}


function newChat(){

fetch("/reset")

document.getElementById("chat").innerHTML =
'<div class="msg bot">Hello 👋 Welcome. What is your name?</div>'

}


/* ENTER KEY SUPPORT ADDED */

document.getElementById("msg").addEventListener("keypress", function(event){

if(event.key === "Enter"){

event.preventDefault()

send()

}

});

</script>

</body>
</html>
"""


@app.route("/reset")
def reset():
    global user_name,last_results
    user_name=None
    last_results=None
    return jsonify({"ok":True})


@app.route("/ask",methods=["POST"])
def ask():

    global user_name,last_results

    msg=request.json["msg"].strip()
    lower=msg.lower()

    if lower in ["hi","hello","hey"]:
        return jsonify({"reply":"Hello 👋 Ask me about colleges."})

    if lower in ["thanks","thank you"]:
        return jsonify({"reply":"You're welcome 😊 Happy to help!"})

    if lower in ["bye"]:
        return jsonify({"reply":"Goodbye 👋 Have a great day!"})


    if user_name is None:
        user_name = msg
        return jsonify({"reply":f"Nice to meet you {user_name}! Ask me about colleges."})


    if msg.isdigit() and last_results is not None:

        num=int(msg)-1

        if 0<=num<len(last_results):

            row=last_results.iloc[num]

            reply=f"<b>{row['college']}</b><br>"
            reply+=f"Location: {row['location']}<br>"
            reply+=f"Fees: {row['fees']}<br>"
            reply+=f"Hostel: {row['hostel']}<br>"
            reply+=f"<a href='{row['website']}' target='_blank'>Visit Website</a>"

            return jsonify({"reply":reply})


    if "chennai" in lower:
        data=df[df["location"].str.contains("chennai",case=False)]
    elif "coimbatore" in lower:
        data=df[df["location"].str.contains("coimbatore",case=False)]
    elif "madurai" in lower:
        data=df[df["location"].str.contains("madurai",case=False)]
    elif "women" in lower:
        data=df[df["college"].str.contains("women",case=False)]
    elif "government" in lower:
        data=df[df["college"].str.contains("government",case=False)]
    elif "hostel" in lower:
        data=df[df["hostel"].str.contains("yes",case=False)]
    elif "affordable" in lower:
        data=df
    elif "arts" in lower:
        data=df[df["college"].str.contains("arts",case=False)]
    else:
        return jsonify({"reply":"Sorry, I couldn't find that information."})

    last_results=data.reset_index(drop=True)

    reply=""

    for i,row in last_results.iterrows():
        reply+=f"{i+1}. {row['college']}<br>"

    reply+="<br>Type college number to see details."

    return jsonify({"reply":reply})


if __name__=="__main__":
    app.run(debug=True)