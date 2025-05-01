// const form = document.getElementById('aiagent');
// const messageContainer = document.querySelector('.storing');
// const textInput = document.getElementById('text');
// const button = document.querySelector('.prompting input[type="button"]');

// function addMessage(query) {
//   if (query.trim() !== '') {
//     const para = document.createElement('p');
//     para.innerHTML = query;
//     messageContainer.appendChild(para);
//     textInput.value = ''; 
//   }
// }
// async function promptreply(prompt,selectedModel){
//     try{
//         const response=await fetch('http://locahost:8003/chatprompt',{
//             method:'post',
//             headers:{
//                 'Content-type':'application/json'
//             },
//             body:JSON.stringify({
//                 item:prompt,
//                 model:selectedModel
//             }),
    
//         });
//         const result =await response.json();
//         answer.style.backgroundColor='red';
//         answer.innerHtml=result;z
//     }
//     catch{

//     }   
// }

// button.addEventListener('click', function(e) {
//   e.preventDefault();
//   const selectedModel = document.querySelector('input[name="model"]:checked').value;
//   const query = textInput.value;
//   addMessage(query);
//   promptreply(query,selectedModel);
// });

// textInput.addEventListener('keydown', function(e) {
//   if (e.key === 'Enter') {
//     e.preventDefault(); 
//     const selectedModel = document.querySelector('input[name="model"]:checked').value;
//     const query = textInput.value;
//     addMessage(query);
//     promptreply(query,selectedModel)
//   }
// });
const form = document.getElementById('aiagent');
const messageContainer = document.querySelector('.storing');
const textInput = document.getElementById('text');
const button = document.querySelector('.prompting input[type="button"]');
// const answer = document.querySelector('.response'); // Add this to match your HTML
function scrollToBottom() {
    messageContainer.scrollTop = messageContainer.scrollHeight;
  }

function addMessage(query) {
  if (query.trim() !== '') {
    const para = document.createElement('p');
    para.innerHTML = query;
    para.style.backgroundColor='blue'
    messageContainer.appendChild(para);
    textInput.value = ''; 
    scrollToBottom();
  }
}

async function promptreply(prompt, selectedModel) {
  try {
    const response = await fetch('http://localhost:8003/chatprompt', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify({
        item: prompt,
        model: selectedModel
      }),
    });
    console.log(response)

    const result = await response.json();
    console.log(result);
    const para2=document.createElement('p');
    para2.style.backgroundColor='red';
    para2.innerHTML = result.response || JSON.stringify(result);
    messageContainer.appendChild(para2);
    scrollToBottom(); // Adjust based on actual response shape
  } catch (error) {
    console.error("Error fetching reply:", error);
    const para2=document.createElement('p');
    para2.style.backgroundColor='red';
    para2.innerHTML= "Failed to get a response.";
    messageContainer.appendChild(para2);
    scrollToBottom();
  }
}

button.addEventListener('click', function(e) {
  e.preventDefault();
  const selectedModel = document.querySelector('input[name="model"]:checked').value;
  console.log(selectedModel)
  const query = textInput.value;
  addMessage(query);
  promptreply(query, selectedModel);
});

textInput.addEventListener('keydown', function(e) {
  if (e.key === 'Enter') {
    e.preventDefault(); 
    const selectedModel = document.querySelector('input[name="model"]:checked').value;
    const query = textInput.value;
    addMessage(query);
    promptreply(query, selectedModel);
  }
});

