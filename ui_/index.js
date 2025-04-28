const form=document.getElementById('data_')
const answer=document.getElementById('answer')
form.addEventListener('submit',async(event)=>{
    event.preventDefault();
    try{
        const prompt=document.getElementById('prompt').value
        const selectedModel = document.querySelector('input[name="model"]:checked').value;
        console.log(selectedModel)
        const response=await fetch('http://localhost:8003/chatprompt',{
            method:'post',
            headers:{
                'Content-type':'application/json'
            },
            body:JSON.stringify({
                item:prompt,
                model:selectedModel
            }),
        });
        const result=await response.json();
        answer.style.backgroundColor='red'
        answer.innerHTML = `<h4>${JSON.stringify(result)}</h4>`;
    }
    catch{

    }


})